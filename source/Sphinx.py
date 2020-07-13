"""
========
 Sphinx
========


This page will be dedicated to my experiences with learning about Sphinx.

First Steps
============

First things first, make sure you have Sphinx installed::

    pip install Sphinx

Now that Sphinx is installed, it helps to have a project created.
For this project, Blog, I'm going to use itself as the example::

    mkdir Blog-master
    cd Blog-master
    mkdir Blog
    mkdir docs
    cd docs

Within this file structure, I'm going to place the actual code that I'm writing
into the Blog folder and the documentation for the code will be going in to the
docs directory.

Yeah, I get that this is a little silly since the Blog itself probably won't
have much actual code, but it's about the practice.

To get Sphinx to create documentation, I'm need to run quickstart::

    sphinx-quickstart

Much of the choices here are irrelevant but I said yes to separating my build
and source directories.

The next step is to write some actual files, for example this one, so that
there's some actual content. To begin with, I wrote HelloWorld, PyCharm, and
Sphinx–all as Python files.

Yes, I get that it's silly to make Python files just to write in the docstring
so that the docstring can then be converted into reStructured Text and then html
but that's kinda the point of this exercise.

That being said, the next step is to create reStructured Text files that contain
the content of these docstrings without having to do a whole lot of
copy-and-pasting and reformatting. To do that, I'll need the autodoc extension
and to do that, I need to go over into the conf.py file::

    open -a "PyCharm CE" source/conf.py

Ok yeah, that's overkill on instruction but hey, I need to learn more about
command line inputs as well.

While I'm in the configurations file, we should change a couple of things.
To start with, uncomment and remove the space from the following lines::

    # import os
    # import sys
    # sys.path.insert(0, os.path.abspath('.'))

And I need to change that last one so it points at the directory with my actual
content. That section should look like this now::

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../Blog'))

Time to add autodoc into the extensions, along with Napoleon to read Numpy and
Google style docstrings and, uh, coverage just to make sure I'm *covered*::

    extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon',
    'sphinx.ext.coverage']

ToDo: Figure out the ToDo extension. PyCharm makes this nice and yellow!

Now that the configurations have been changed, I can creature the rST files that
will point at the Python files using the following CLI::

    sphinx-apidoc -o source/ ../Blog

The ``source/`` part is telling it to place the rST files into the source
directory and ``../Blog`` tells it to read the Python files in Blog.

.. note::
   Make sure to save the content as ``.py`` files and not plain text.

Now I've got a bunch of ``.rst`` files sitting in my source folder that should
look like the following::

    Hello World module
    ==================

    .. automodule:: HelloWorld
       :members:
       :undoc-members:
       :show-inheritance:

I can then include these ``.rst`` files in my ``index.rst`` under the toctree::

    .. toctree::
    :maxdepth: 2
    :caption: Contents:

    Hello World
    PyCharm
    Sphinx

And they should show up in the table of contents when I put everything together
with ``make``::

    make html

*et voila!*

=======
 TL:DR
=======

Cheat sheet:

    1. Install Sphinx
    2. Make a project directory with a ``docs`` directory and a ``<project>`` directory inside
    3. ``$ sphinx-quickstart``
    4. Make changes::

        import os
        import sys
        sys.path.insert(0, os.path.abspath('../../Blog'))

    5. Add extensions::

        extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon',
        'sphinx.ext.coverage']

    6. ``$ sphinx-apidoc -o source/ ../<project>``
    7. Add the names of the modules in the ``<project>`` directory to ``index.rst`` under the toctree
    8. ``$ make html``


"""
