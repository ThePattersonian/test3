"""
===========
 Makefiles
===========

I can't say that I know much about Makefiles, but I do know that they can come
in handy to speed up some processes. For instance here is a little thing I can
enter on the command line to save me from having to type in more commands and
help my workflow::

 gh-pages:
  git checkout gh-pages
  rm -rf build _sources _static _modules
  git checkout master $(GH_PAGES_SOURCES)
  git reset HEAD
  make html
  mv -fv build/html/* ./
  rm -rf $(GH_PAGES_SOURCES) build
  touch .nojekyll
  git add -A
  git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`"
  git push origin gh-pages ; git checkout master
  git branch

This lets me push a version of my blog to a side branch, gh-pages, that is
responsible for putting the HTML files on Github.io
"""
