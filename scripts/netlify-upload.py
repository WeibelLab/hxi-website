#!/usr/bin/env python3
"""Upload a built site directory to Netlify as a manual deploy.

Netlify runs no build for this, so it consumes no credits. Called by
scripts/deploy-manual.sh, which does the build and the safety checks first.

Sends the sha1 of every file, uploads only the ones Netlify says it lacks,
then waits for the deploy to go live.
"""

import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.netlify.com/api/v1"


def request(method, url, token, data=None, content_type="application/json"):
    req = urllib.request.Request(url, method=method, data=data)
    req.add_header("Authorization", "Bearer " + token)
    if data is not None:
        req.add_header("Content-Type", content_type)
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            body = response.read()
            if content_type == "application/octet-stream":
                return None
            return json.loads(body or b"{}")
    except urllib.error.HTTPError as exc:
        detail = exc.read()[:400].decode("utf-8", "replace")
        sys.exit("  netlify %s on %s %s\n  %s" % (exc.code, method, url, detail))


def main():
    root = sys.argv[1]
    site = os.environ["SITE_ID"]
    token = open(os.path.expanduser(os.environ["TOKEN_FILE"])).read().strip()

    digests, paths = {}, {}
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            full = os.path.join(dirpath, name)
            rel = "/" + os.path.relpath(full, root)
            with open(full, "rb") as handle:
                digests[rel] = hashlib.sha1(handle.read()).hexdigest()
            paths[rel] = full
    print("  hashed %d files" % len(digests))

    deploy = request(
        "POST", "%s/sites/%s/deploys" % (API, site), token,
        json.dumps({"files": digests, "draft": False, "async": False}).encode(),
    )
    deploy_id = deploy["id"]
    required = deploy.get("required", [])
    print("  deploy %s needs %d files" % (deploy_id, len(required)))

    by_digest = {}
    for rel, digest in digests.items():
        by_digest.setdefault(digest, []).append(rel)

    sent = 0
    for digest in required:
        for rel in by_digest.get(digest, [])[:1]:
            with open(paths[rel], "rb") as handle:
                request(
                    "PUT",
                    "%s/deploys/%s/files%s" % (API, deploy_id, urllib.parse.quote(rel)),
                    token, handle.read(), "application/octet-stream",
                )
            sent += 1
            if sent % 100 == 0:
                print("    %d/%d" % (sent, len(required)))
    print("  uploaded %d files" % sent)

    for _ in range(120):
        state = request("GET", "%s/deploys/%s" % (API, deploy_id), token)
        if state.get("state") == "ready":
            print("  deploy ready: %s" % deploy_id)
            return
        if state.get("state") == "error":
            sys.exit("  deploy failed: %s" % state.get("error_message"))
        time.sleep(5)
    sys.exit("  timed out waiting for the deploy to go live")


if __name__ == "__main__":
    main()
