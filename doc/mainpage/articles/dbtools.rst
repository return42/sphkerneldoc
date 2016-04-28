.. -*- coding: utf-8; mode: rst -*-

.. _xref_dbtools:

=========================
DocBook to reST migration
=========================

In gerneral XML tools are used to convert DockBook XML, e.g. XSL Stylesheets to
convert DocBook XML into various formats (examples:
http://docbook.sourceforge.net/release/xsl/current).

I haven't found any XSL Template to convert DocBook to reST, and I'am not
intrested in developing one. Thats why I compiled these small ``dbtools``
toolbox, which uses existing tools and *hacked* a bit around them.  The
``dbtools`` uses the pandoc converter and implements some XML-filters and all
theses stuff, where pandoc fails, e.g. cross references in a multipart DocBook
document.

Migration of DocBook-XML is a working process and these tools are not *ready to
go*.  The ``dbtools`` script is a usefull base for DocBook to reST migration, it
don't attempt to be a *converter* for your daily usage. The toolbox is developed
in context of the Linux Kernel documentation. You might edit or add parts to the
toolbox, by doing this, please take notice of the dbtools :ref:`xref_LICENSE`.


dbtools requirements
====================

The ``scripts/dbtools`` script requires python3, cairosvg, `lxml`_ and
pandoc(-filters)::

   $ sudo apt-get install python3 python3-pip python3-lxml

The pandocfilters and the cairosvg are installed localy (no sudo required)::

   $ pip3 install pandocfilters cairosvg

The cairosvg is needed by the linux_tv book which contains miscellaneous .svg
files without a pdf representation. There is a LaTeX support for .svg files but
this is (IMO) nappy. It is better to preserve pdf versions manually (or with
this cairosvg converter).


remarks on pandoc
=================

There are plenty docbook converter out. Most of them have common, that they
implement there own (less XML) parsers and they always implement only a subset
of the DocBook markup.

The coverage of the pandoc DocBook reader is the most advanced, but it is also a
subset.  If the pandoc reader does not implement a markup, it will not be in the
AST. This is, why it can't be handled in a pandoc filter. The coverage of the
pandoc DocBook reader is documented in the sources:

* https://github.com/jgm/pandoc/blob/master/src/Text/Pandoc/Readers/DocBook.hs#L23

The pandoc reStructuredText writer is also incomplete and has serveral bugs, for
details take a look at the sources:

* https://github.com/jgm/pandoc/blob/master/src/Text/Pandoc/Writers/RST.hs

On my Ubuntu 15.10 sandbox is the pandoc version 1.13.2 via package manager
available. In this version, the DocBook reader missed some common used markups
like "<xref>". Therefore the development version of pandoc is needed. Follow:

* https://github.com/jgm/pandoc/wiki/Installing-the-development-version-of-pandoc

Remind, building the haskel compiler and compiling pandoc does massive time,
memory and CPU consumption / my small sandbox exploded :-(.

To get in use of the pandoc-filters, the installation of the pandoc python
package is required (needs only seconds to install).

* https://pypi.python.org/pypi/pandocfilters

Pandoc definitions: They have dense urls, this link is from version 1.16.1
check about newer versions ...

* http://hackage.haskell.org/package/pandoc-types-1.16.1/docs/Text-Pandoc-Definition.html

The pandoc DocBook reader does not *understand* XML nor SGML, therefore it
will not do all these XML stuff, like reading external entities.

With option ``--reference-links``, pandoc will create *reference links*. This
means, the *link-name* is used in the running text and the reference to the
target is defined at the end of the document (covered by ``dbtools``).

.. code-block:: rst

   The standard `Lorem Ipsum`_ passage.

   .. _`Lorem Ipsum`: https://en.wikipedia.org/wiki/Lorem_ipsum

DocBook remarks
===============

DocBook documentation is available from:

* http://docbook.org/tdg/en/html/docbook.html

.. include:: refs.txt

