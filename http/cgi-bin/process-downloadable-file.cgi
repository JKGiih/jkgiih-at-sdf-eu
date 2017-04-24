#!/bin/ksh

root="/udd/j/jkgiih/gopher";
if [ -z $1 ]; then
    dir="$root/$QUERY_STRING";
else
    dir="$1";
fi

echo "Content-type: text/plain; charset=UTF-8";

if [ ! -f "$dir" ]; then
    echo "File $dir does not exist.";
else
    echo "Content-Disposition: attachment; filename=$dir"
fi

echo

cat "$dir";
