crawler-study-
==================================================================================================
a simple crawler studied from www.youtube.com/watch?v=SFas42HBtMg‎

this is also the first python program for me. Python is really a powerful tool because it has a lot of well-designed libraries. However, the more the libraries can help, the less we know about how exactly they work. So I want to write some thinking on web crawler.
==================================================================================================
The procedure in this program is like this:

firstly, for a given url, enque it to the url queue

then, establish a socket to the address of current url, send a http request. after receiving the http respond, store the whole text into a variable and use beautifulsoup to analyze

parse the information in the text, find all <a> tags with href attribute. Then check if the href already visited, if not, enque this into url queue and record it into a list "visited".

deque the first element in queue and then repeat.
===================================================================================================
needless to say, this program needs a lot time to finish.

for each iteration we need:

we need to send http request and wait for respond.

handle the whole text to find urls we want

traverse the visited list to avoid double retreiving.
===================================================================================================


