# jkgiih-at-sdf-eu #

### Summary ###

This repository is a backup of my homepage and gopherspace at sdf-eu.org.

The html site is generated dynamically from the gopherspace content with
KornShell CGI scripts.

The scripts are in the folder html/cgi-bin. They currently expect to find
the gopherspace under /udd/j/jkgiih/gopher. Feel free to use them for your
own gopherspace, but adjust the $root variable at the top of each script
accordingly. (I may change the scripts in the future so that the path can
be passed as a paramater.)

Otherwise directory structure shouldn't matter, but you can see mine in
the comments to the file gopher-to-http.cgi.

The scripts do not implement the complete gopher protocol; for example
external links aren't handled yet. Directories, text files, images and
sounds do work. All other types are treated as binary (downloadable) files.