=======
INSTALL
=======

Requirements:

* Kernel-Doc Sphinx extensions: https://github.com/return42/linuxdoc ::

    pip install --user git+http://github.com/return42/linuxdoc.git

* DocBook to reST conversion: https://github.com/return42/dbxml2rst

   See installation instructions at dbxml2rst

To generate documentation, Sphinx (``sphinx-build``) and the Read the Docs
Sphinx theme (``sphinx_rtd_theme``) must be installed.

Debian/Ubuntu::

  apt-get install python3-sphinx python3-sphinx-rtd-theme

Fedora::

  yum install python3-sphinx-rtd-theme python3-sphinx-rtd-theme

If you don't have *admin* privileges, use pip3 (or even pip) for a local user
installation::

  $ pip3 install --user Sphinx sphinx_rtd_theme

Until here, you have installed the minimum requirements to build HTML output
which might be good enough for most use cases. If you want more from your
sphinx-build, you have to install the following (optional) prerequisites.

For PDF output and *Math support* (nicely rendered mathematical notations) a
LaTeX tool-chain is required.

Debian/Ubuntu::

  apt-get install \
      texlive-base texlive-xetex texlive-latex-recommended \
      texlive-extra-utils dvipng ttf-dejavu

Fedora::

  yum install \
      texlive-amsmath.noarch texlive-mathtools.noarch
      texlive-anyfontsize.noarch texlive-xelatex
      texlive-xetex texlive-xecolor.noarch
      texlive-titlesec.noarch texlive-framed texlive-threeparttable
      texlive-wrapfig texlive-upquote texlive-capt-of eqparbox

Further reading:

* `RTD theme <https://pypi.python.org/pypi/sphinx_rtd_theme>`_
* `TeX Live <https://www.tug.org/texlive>`_
* `Math support in Sphinx <http://www.sphinx-doc.org/ext/math.html>`_
* `dvisvgm (A fast DVI to SVG converter) <http://dvisvgm.bplaced.net/Downloads>`_
