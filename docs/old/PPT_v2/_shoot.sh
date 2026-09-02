#!/bin/zsh
# Render all wireframe HTML -> 1920x1080 PNG via headless Chrome
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"
python3 _build.py
for html in [0-9][0-9]_*.html; do
  png="${html%.html}.png"
  "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1920,1080 \
    --default-background-color=FFFFFFFF --virtual-time-budget=2500 \
    --screenshot="$DIR/$png" "file://$DIR/$html" >/dev/null 2>&1
  dim=$(sips -g pixelWidth -g pixelHeight "$DIR/$png" 2>/dev/null | awk '/pixel/{print $2}' | paste -sd'x' -)
  echo "  $png  $dim"
done
echo "done — $(ls [0-9][0-9]_*.png | wc -l | tr -d ' ') PNGs"
