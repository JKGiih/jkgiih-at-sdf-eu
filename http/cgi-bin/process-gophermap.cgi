#!/bin/ksh

if [ -z $1 ]; then
    dir="$QUERY_STRING";
else
    dir="$1";
fi
map="$dir/gophermap";
echo "<h1>$(basename $dir)</h1>";
while read line;
do
    ./process-gophermap-line.cgi "$dir" "$line";
done < $map
