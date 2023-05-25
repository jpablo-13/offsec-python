#!/usr/bin/python

tag = '<a href="https://www.offsec.com/blog">Blog</a>'
start = "http"
end = "\">"

#print(tag.index(start))
#print(tag.index(end))

print(tag[tag.index(start):tag.index(end)])


