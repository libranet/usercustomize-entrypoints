# usercustomize-entrypoints

A very simple library that makes a python module called `usercustomize`
available. Python's [site](https://docs.python.org/3/library/site.html)
module gives `sitecustomize` and `usercustomize`, special treatment by importing 
it after it is done looking for and processing .pth files.

What this package does, is finding all `usercustomize` entry-points and,
if they are callable, calls them.