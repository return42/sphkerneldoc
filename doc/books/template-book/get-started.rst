.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _get-started:

*********************
Get started with reST
*********************

To get started with documentating in reST_ , copy the template-book folder and
the config file.

.. code-block:: sh

    cd {linux-kernel}/Documentation/books
    cp -r template-book my-project
    cp template-book.conf my-project.conf

It is recomended to read through the :ref:`kernel-doc:kernel-doc-howto`. For the
impatient: no panic, HOWTO is not large but gives you a good starting point.

In the next step, set up the basic build properties in the `config_file`_. With
that, the boilerplate is finished and you should test if your documentation gets
build. Try to build the HTML representation:

.. code-block:: sh

    cd {linux-kernel}
    make books/my-project.html
    ...
    HTML build OK / start file at:
        Documentation/dist/books/template-book/index.html

The last lines indactes that the build process succeeded and where you find the
HTML start file, open the index.html file within your favorite HTML browser to
see what you got ;-)

While HTML is one *big* side with all content in, PDF documents separate books
and (or) articles. To get *first* PDF you have to active the pdf_documents line
in the my_config.py at least.::

    pdf_documents = [ (master_doc, main_name, project, author) , ]

To get a PDF representation build the ".pdf" target:

.. code-block:: sh

    make books/my-project.pdf
    ...
    PDF build OK / pdf files stored in:
        Documentation/dist/rst2pdf

.. todo::

   At this time the PDF build process (rst2pdf) is buggy and the layout is far
   from what a book or an academic article will look like ... this is an ongonig
   procces.

There is also a ".clean" target to get rid of all intermadiate and HTML files,
except the PDF representations, they will be preserved

To add your project's documentation to the index, edit
``Documentation/books/index.rst`` and add a reference, e.g.::

  * ...
  * ...
  * `My Project <my-project/index.html>`_

.. _config_file:

Config File
===========

The file ``my-project.conf`` is the config file of the build process. At least,
you should change the following values to your needs.::

    project   = u'Template Book'
    copyright = u'2016, The kernel development community'
    author    = u'The kernel development community'
    version   = u'v4.7'

