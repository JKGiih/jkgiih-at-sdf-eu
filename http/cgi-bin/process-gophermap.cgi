#!/bin/ksh

root="/udd/j/jkgiih/gopher";
if [ -z $1 ]; then
    dir="$root/$QUERY_STRING";
else
    dir="$1";
fi
map="$dir/gophermap";
echo "<h1>$(basename $dir)</h1>";
while read line;
do
    ./process-gophermap-line.cgi "$dir" "$line";
done < $map
