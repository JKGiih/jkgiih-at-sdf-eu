#!/bin/ksh

root="/udd/j/jkgiih/gopher";
if [ -z $1 ]; then
    dir="$root/$QUERY_STRING";
else
    dir="$1";
fi
echo "Content-type: text/html; charset=UTF-8";
echo
echo "<DOCTYPE html>";
echo "<html>";
echo "<head>";
echo "<title>$(basename $dir)</title>";
echo "</head>";
echo "<body>";
if [ ! -d "$dir" ]; then
    echo "<h1>404</h1><p>Directory $dir does not exist.</p>";
else
    if [ ! -e "$dir/gophermap" ]; then
        for f in $(ls $dir); do
            if [ -d "$dir/$f" ]; then # directory
                echo "<p><a href=\"/cgi-bin/process-directory.cgi?$dir/$f\">$f</a></p>";
            else
                ext="${f##*.}";
                if [ "$ext" = "txt" ]; then # text file
                    echo "<p><a href=\"/cgi-bin/process-viewable-file.cgi?$QUERY_STRING/$f\">$f</a></p>";
                elif [[ "$ext" = "gif" || "$ext" = "jpg" || "$ext" = "jpeg" || "$ext" = "png" || "$ext" = "bmp" ]]; then # image file
                    echo "<p><img src=\"/cgi-bin/process-viewable-file.cgi?$dir/$f\" alt=\"$f\"></img></p>";
                elif [[ "$ext" = "ogg" || "$ext" = "wav" || "$ext" = "mp3" ]]; then # sound file
                    echo "<p><audio controls><source src=\"./process-viewable-file.cgi?$dir/$f\" type=\"audio/$ext\"><a hred=\"/cgi-bin/process-downloadable-file.cgi?$dir/$f\">$f</a></audio></p>";
                else # binary/other file
                    echo "<p><a href=\"/cgi-bin/process-downloadable-file.cgi?$dir/$f\">$f</a></p>";
                fi
            fi
        done
    else
        ./process-gophermap.cgi $dir;
    fi
fi
echo "<footer><p><small><hr><br>This site is dynamically generated from my gopherspace. If you\
r browser supports the gopher protocol (Lynx does), you may wish to navigate to <a href=\"goph\
er://sdf-eu.org:70/1/users/jkgiih\">gopher://sdf-eu.org:70/1/users/jkgiih</a> for a direct exp\
erience.</small></p></footer>";
echo "</body>";
echo "</html>";
