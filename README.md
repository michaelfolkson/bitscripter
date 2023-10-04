# Bitcoin Script Runner

Just enter a bitcoin script, with features similar to what you can do here: 

https://siminchen.github.io/bitcoinIDE/build/editor.html

## Prerequisites

You have to have Python 3 installed on your system, preferably from Python.org
or whatever works best with your OS.

You also have to download the code, of course. That can be done with Git from
radicle, as show below, or by downloading a .zip file.

## Data

The data is just a couple JSON files, for now.

Probably could move to ReDiS later, I guess.

## Server

The backend code is written in Python 3.

To start the server, open a terminal (ctrl+alt+t in Ubuntu, use search.brave.com to find
the instructions for opening a terminal in your own OS),
navigate to the folder where you have bitscripter.py, and run the following:

    python3 bitscripter_web.py

The output should show something about listening on port 8000.

Example:

    2023-09-18 14:14:22,364 itty3 INFO itty3 1.1.1: Now serving requests at http://0.0.0.0:8000...

## Frontend

This will just be a form submission, for now, with
"templated" HTML.

Once you've started the server, visit this link: http://0.0.0.0:8000/bitscripter/

(or whatever link the output of the terminal command you used to run the server shows, plus /bitscripter/)

If you get a blank-looking page showing "Not found" that's still good, since that means the server
is responding to requests. You can see it responding to requests in the terminal where you ran the
server, too. 

## Contributing

I'm going to try using this as an excuse to try Radicle. 

Because I'm sick of
getting [banned for silly shit](https://meta.stackoverflow.com/questions/378976/unexplained-clutter-in-a-post-edited-back-in-by-author)
from various things.

https://radicle.xyz/downloads.html

Anyway, once you've installed it, and gotten me to add
you to the repository try this:

    export GIT_USERNAME=hnokftsmm5xmemsynpgoatiiswaddamziknow
    export GIT_PASSWORD=ue8oa8hu9h89a8uhe8oa9h89dpdy
    git config credential.helper "/bin/bash $(pwd)/credential-helper.sh"
    git clone rad://hnrkftsmm5xmems7npgoai6iiswaddaxmz4no.git

