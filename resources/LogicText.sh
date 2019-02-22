#!/bin/bash
wine_cmd="${1:-$(which wine)}"
if ! [ -x "$wine_cmd" ] ; then
  echo "Can't find wine in the path, gimme a hint" 1>&2
  exit 1
fi
java -jar LogicText.jar <(sed "s|/usr/local/bin/wine|$wine_cmd|" resources/config.properties)
