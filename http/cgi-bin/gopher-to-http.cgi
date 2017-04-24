#!/bin/ksh
#
# gopher-to-http.cgi
#
# This translates a gopherspace into a crude html site to be
# served over http.
#
# The scripts currently expect to find the gopherspace under
# /udd/j/jkgiih/gopher. Feel free to use them for your own
# gopherspace, but adjust the $root variable at the top of
# each script accordingly. (I may change the scripts in the
# future so that the path can be passed as a paramater.)
#
# It currently shouldn't matter, but my directory structure,
# for the relavant parts, is like this:
#
# |--- ~/
# |    |--- gopher
# |          |--- gophermap
# |          |--- phlog
# |               |--- gophermap
# |               |--- entry001.txt
# |               |--- entry002.txt
# |--- |--- html
# |         |--- .htaccess
# |         |--- 404.html
# |         |--- cgi-bin
# |              |--- gopher-to-html.cgi
#
# And my .htaccess file is like this:
#
# RewriteEngine On
# RewriteRule ^index\.html$ cgi-bin\/gopher-to-http.cgi [L]
# RewriteRule ^$ cgi-bin\/gopher-to-http.cgi [L]
# ErrorDocument 404 /404.html
#
# The scripts do not implement the complete gopher protocol;
# for example external links aren't handled yet. Directories,
# text files, images and sounds do work. All other types are
# treated as binary (downloadable) files.

./process-directory.cgi "/udd/j/jkgiih/gopher";
