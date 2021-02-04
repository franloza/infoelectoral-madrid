#!/bin/bash
while read p; do
  url="$(echo "$p"  | cut -d, -f1)"
  filename="$(basename $url)"
  wget -qO - $url | gzip -c > pdf/$filename.gz
done < info.csv