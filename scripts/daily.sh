#!/usr/bin/env bash
# Usage: ./scripts/daily.sh "Day 3: functions and decorators" "Wrote 5 small functions; decorators still confusing"
# Adds a dated entry to daily-log.md, commits everything, and pushes.
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 \"Day N: topic\" [\"optional note\"]" >&2
  exit 1
fi

title="$1"
note="${2:-}"
today="$(date +%F)"

cd "$(git rev-parse --show-toplevel)"

{
  echo ""
  echo "## ${today}"
  echo "- ${title}"
  if [ -n "$note" ]; then
    echo "- ${note}"
  fi
} >> daily-log.md

git add -A
git commit -m "${title}"
git push
