"""One call to the Messages API with the standard library: python3 claude_call.py "prompt" prints the reply.

The key is read from ANTHROPIC_API_KEY in the environment and never printed. Model: CLAUDE_MODEL, default claude-haiku-5-5.
"""
import json
import os
import sys
import urllib.error
import urllib.request


def main():
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key or len(sys.argv) < 2:
        sys.exit("usage: ANTHROPIC_API_KEY=... claude_call.py \"prompt\"")
    body = {"model": os.environ.get("CLAUDE_MODEL", "claude-haiku-5-5"), "max_tokens": 4096, "temperature": 0.2,
            "messages": [{"role": "user", "content": sys.argv[1]}]}
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=json.dumps(body).encode(),
                                 headers={"x-api-key": key, "anthropic-version": "2023-06-01",
                                          "content-type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"claude_call: HTTP {e.code} {e.read()[:200].decode(errors='replace')}")
    except (urllib.error.URLError, TimeoutError) as e:
        sys.exit(f"claude_call: {type(e).__name__}")
    print("".join(b.get("text", "") for b in data.get("content", [])))


if __name__ == "__main__":
    main()
