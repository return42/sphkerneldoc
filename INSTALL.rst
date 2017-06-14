=======
INSTALL
=======

If you try to compile this POC by your own, please consider that you need a copy
of the Jon's docs-next and in the ``Makefile`` set ``srctree`` to the copy. The
default is:

.. code-block:: make

   srctree=/share/linux-docs-next
   export srctree

If you want to build simple HTML representations with the 'books*.html' Makefile
targets, the minimum (python) requirements will be installed automatically (see
``./local/``).

Python requirements:

* Sphinx-doc: http://www.sphinx-doc.org/en/stable/
* Kernel-Doc Sphinx extensions: https://github.com/return42/linuxdoc
* Sphinx theme for *Read-the-Docs*: https://github.com/rtfd/sphinx_rtd_theme/

If you want more from your sphinx-build, you have to install the following
(optional) prerequisites.

DOT (Graphviz)
==============

The kernel documentation has special figure and image directives, which supports
**DOT** formated files. To render those DOT markups into nice images, a Graphviz
Installation is required::

Debian/Ubuntu::

  apt-get install graphviz

Fedora::

  yum install 'graphviz*'

* DOT: http://graphviz.org/pdf/dotguide.pdf
* Graphviz: http://www.graphviz.org/content/dot-language

PDF & Math support
==================

For PDF output and *Math support* (nicely rendered mathematical notations) a
LaTeX tool-chain is required. To convert SVG to PDF a ImageMagick installation
is also needed.

Debian/Ubuntu::

  apt-get install \
      texlive-base texlive-xetex texlive-latex-recommended \
      texlive-extra-utils dvipng ttf-dejavu \
      imagemagick

Fedora::

  yum install \
      texlive-amsmath.noarch texlive-mathtools.noarch \
      texlive-anyfontsize.noarch texlive-xelatex \
      texlive-xetex texlive-xecolor.noarch \
      texlive-titlesec.noarch texlive-framed texlive-threeparttable \
      texlive-wrapfig texlive-upquote texlive-capt-of eqparbox \
      ImageMagick

Further reading:

* `RTD theme <https://pypi.python.org/pypi/sphinx_rtd_theme>`_
* `TeX Live <https://www.tug.org/texlive>`_
* `Math support in Sphinx <http://www.sphinx-doc.org/ext/math.html>`_
* `ImageMagick <https://www.imagemagick.org>`_

Not yet used, but good to know:

* `dvisvgm (A fast DVI to SVG converter) <http://dvisvgm.bplaced.net>`_
