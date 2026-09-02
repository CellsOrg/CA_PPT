#!/bin/zsh
# Render slide HTML -> 1920x1080 PNG via headless Chrome
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

shoot () {
  local html="$1" ; local png="$2"
  "$CHROME" --headless --disable-gpu --no-sandbox --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1920,1080 \
    --default-background-color=FFFFFFFF --virtual-time-budget=2000 \
    --screenshot="$DIR/$png" "file://$DIR/$html" >/dev/null 2>&1
  echo "  $png  ->  $(sips -g pixelWidth -g pixelHeight "$DIR/$png" | awk '/pixel/{print $2}' | paste -sd'x' -)"
}

for n in "${@:-01 02 03 04}"; do :; done

shoot 01_project_overview.html 01_project_overview.png
shoot 02_to_be.html            02_to_be.png
shoot 03_solution.html         03_solution.png
shoot 04_story_and_value.html  04_story_and_value.png
echo "done"
