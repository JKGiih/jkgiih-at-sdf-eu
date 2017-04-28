#!/bin/ksh

dir=$1;
line=$2;

tabs=$(echo "$line" | awk '{print gsub(/\t/,"")}');

if [ $tabs -gt 0 ]; then
    path=$(echo "$line" | cut -f 2);
    type_and_label=$(echo "$line" | cut -f 1);
    type=$(echo "$type_and_label" | cut -c 1);
    label=$(echo "$type_and_label" | cut -c 2-);
    if [ $tabs -gt 1]; then
	domain=$(echo "$line" | cut -f 3);
	if [ $tabs -gt 2]; then
	    port=$(echo "$line" | cut -f 4);
	fi
    fi
fi

if [ -z $path ]; then
    if [ ! "$line" = "." ]; then
	echo "<p>$line</p>"; # text line
    fi
else
    if [ "$type" = "1" ]; then # directory
	if [ -z $domain ]; then
	    echo "<p><a href=\"/cgi-bin/process-directory.cgi?$dir/$path\">$label</a></p>";
	else
	    if [ -z $port ]; then # external
		echo "TODO";
	    else
		echo "TODO";
	    fi
	fi
    elif [ "$type" = "0" ]; then # text file
	if [ -z $domain ]; then
	    echo "<p><a href=\"/cgi-bin/process-viewable-file.cgi?$dir/$path\">$label</a></p>";
	else
	    if [ -z $port ]; then # external
		echo "TODO";
	    else
		echo "TODO";
	    fi
	fi
    elif [[ "$type" = "g" || "$type" = "i" ]]; then # image file
	if [ -z $domain ]; then
	    echo "<p><img src=\"/cgi-bin/process-viewable-file.cgi?$dir/$path\" alt=\"$label\"></img></p>";
	else
	    if [ -z $port ]; then # external
		echo "TODO";
	    else
		echo "TODO";
	    fi
	fi
    elif [[ "$type" = "s" ]]; then # sound file
	if [ -z $domain ]; then
	    ext="${path##*.}";
	    echo "<p><audio controls><source src=\"./process-viewable-file.cgi?$dir/$path\" type=\"audio/$ext\"><a hred=\"/cgi-bin/process-downloadable-file.cgi?$dir/$label\">$f</a></audio></p>";
	else
	    if [ -z $port ]; then # external
		echo "TODO";
	    else
		echo "TODO";
	    fi
	fi
    elif [ "$type" = "h" ]; then # html file                                                   
        if [ -z $domain ]; then
            echo "<p><a href=\"/cgi-bin/process-html.cgi?$dir/$path\">$label</a></p>";
        else
            if [ -z $port ]; then # external                                                   
                echo "<p><a href=\"$domain/$path\">$label</a></p>";
            else
                echo "TODO";
            fi
        fi
    else
	if [ -z $domain ]; then # binary/other file
	    echo "<p><a href=\"/cgi-bin/process-downloadable-file.cgi?$dir/$path\">$label</a></p>";
	else
	    if [ -z $port ]; then # external
		echo "TODO";
	    else
		echo "TODO";
	    fi
	fi
    fi
fi

# TODO
# external links
