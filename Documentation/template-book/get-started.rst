.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _get-started:

***************************
Get started with reST books
***************************

This chapter describes, how to create a reST_ *book* (aka sphinx-project) based
on the ``Documentation/template-book``.

To get started, copy the template-book folder and the config file.

.. code-block:: sh

    cd {linux-kernel}/Documentation
    cp -r template-book my-project

It is recomended to read through the :ref:`kernel-doc:kernel-doc-howto`. For the
impatient: no panic, HOWTO is not large but gives you a good starting point.

In the next step, set up the basic build properties in the `config_file`_. With
that, the boilerplate is finished and you should test if your documentation gets
build. Try to build the HTML representation:

.. code-block:: sh

    cd {linux-kernel}
    make books/my-project.html
      SPHINX  books/my-project.html --> file://{linux-kernel}/Documentation/dist/books/my-project

The "SPHINX" line shows, where you find the HTML start file, open the
``index.html`` file within your favorite HTML browser to see what you get ;-)

While HTML is one *big* side with all content in, PDF documents separate books
and (or) articles. To get *first* PDF you have to active the pdf_documents line
in the ``my-project/config.py`` at least.::

  latex_documents = [
    ('index', 'my-project.tex', 'My Project Title',
     'The kernel development community', 'manual'),
  ]

To get a PDF representation build the ".pdf" target:

.. code-block:: sh

    make books/template-book.pdf
      LATEX   books/my-project.latex --> file://{linux-kernel}/Documentation/dist/books/my-project/latex
    ...
    Transcript written on TemplateBook.log.
      PDF    dist-pdf --> file:///share/sphkerneldoc/dist/books/my-project/pdf

.. todo::

   At this time the PDF build process is buggy and the layout is far from what a
   book or an academic article will look like ... this is an ongoing processes
   in this POC.

There is also a ".clean" target to get rid of all intermadiate and output files.

To add your project's documentation to the index, edit
``intro/docs.rst`` and add a reference, e.g.::

  * ...
  * ...
  * `My Project <books/my-project/index.html>`
    (`pdf <books/my-project/pdf>`__, `man <books/my-project/man>`__)_

.. _config_file:

Config File
===========

The file ``conf.py`` is the config file of the build process. At least,
you should change the following values to your needs.::

    project   = u'Template Book'
    copyright = u'2016, The kernel development community'
    author    = u'The kernel development community'

