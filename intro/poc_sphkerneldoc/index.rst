.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _xref_about_this_poc:

================================================================================
                                 About this POC
================================================================================

The aim of this POC is, to demonstrate how a *straight forward* documentation
build might look like. It uses the libraries:

* :ref:`LinuxDoc project <linuxdoc:linuxdoc>`
* :ref:`DocBook-XML to reST project <dbxml2rst:dbxml2rst>` (see
  :ref:`dbxml2rst_migration`).

It assembles:

* Sphinx (reST) content from kernel's sources (``Documentation/``)
* DocBook content from kernel's sources (docs-next) converted to reST
* The *kernel-doc* comments from Kernel's source code

All the reST content together is compiled to HTML with the `sphinx-doc`_
project and a `sphinx_rtd_theme`_ is applied. Sources are taken from:

* *this* POC: https://github.com/return42/sphkerneldoc and
* the origin Kernel's sources are taken from Jon's docs-next::

    git://git.lwn.net/linux.git docs-next

If you try to compile this POC by your own, please consider that you need a copy
of the Jon's docs-next and in the ``Makefile`` set ``srctree`` to the copy. The
default is:

.. code-block:: make

   srctree=/share/linux-docs-next
   export srctree

There are also some more requirements, use the ``help`` target for more
informations.

.. code-block:: sh

   make help

.. _xref_linux_src_doc:

source code (kernel-autodoc)
============================

The makefile target ``src2rst`` of this POC uses the command-line
``kernel-autodoc`` from the :ref:`linuxdoc lib <linuxdoc:linuxdoc_cmdline>` and
makes a full scan of the kernel source tree. The scan gather all kernel-doc
comments and builds a analogous tree (`reST linux_src_doc`_) of reST files with
the documentation from the source-code comments. With ``make src.html`` the HTML
page linked below is build.

* HTML rendered `Linux kernel source <../linux_src_doc/index.html>`_

.. hint::

   All you find *there* is in a experimental state!!!

.. _`cross_references`:

cross references (intersphinx)
==============================

The `Linux kernel source <../linux_src_doc/index.html>`_ page (build above)
could also be used for cross references, a feature which is available from the
extension `sphinx.ext.intersphinx`_. Add just one line to your sphinx-project:

.. code-block:: python

    intersphinx_mapping = {}
    ...
    intersphinx_mapping['linux'] = (
        'https://return42.github.io/sphkerneldoc/linux_src_doc/', None)

E.g. to refer to a function in the DVB-Frontend, write:

.. code-block:: rst

    lorem :ref:`dtv_get_frontend <linux:dtv_get_frontend>` ipsum

which will be rendered like this:

    lorem :ref:`dtv_get_frontend <linux:dtv_get_frontend>` ipsum

Further reading
===============

.. toctree::
   :maxdepth: 1
   :glob:

   why_rest
   LICENSE
