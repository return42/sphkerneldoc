# -*- coding: utf-8; mode: make -*-

# This makefile is used to convert the kernel documentation to reStructuredText
# and build all books (aka DocBooks) with sphinx.

srctree=/share/linux
export srctree

REPO_ROOT      := $(abspath ..)
SCRIPT_FOLDER  := $(REPO_ROOT)/scripts
TEMPLATES      := $(REPO_ROOT)/templates
CACHE          := $(REPO_ROOT)/cache
DOC_FOLDER     := .
BOOKS_FOLDER   := books
AUTODOC_FOLDER := linux_src_doc
LINUX_MISC_DOC := linux_misc_doc
DIST           := $(REPO_ROOT)/dist
DIST_BOOKS     := $(DIST)/books-pdf
export DIST_BOOKS

# External programs used

SPHINXBUILD    := sphinx-build
KERNELDOC      := $(SCRIPT_FOLDER)/kernel-doc
DBTOOLS_SCRIPT := $(SCRIPT_FOLDER)/dbtools
AUTODOC_SCRIPT := $(SCRIPT_FOLDER)/autodoc.sh
SYNCDOC_SCRIPT := $(SCRIPT_FOLDER)/syncdoc.sh

PDFLATEX       := xelatex
MAKEINDEX      := makeindex

BOOKS := $(filter %/, $(wildcard $(BOOKS_FOLDER)/*/))
BOOKS := $(BOOKS:%/=%)

# sphinx-doc setup
SPHINXOPTS  :=
PAPER       := a4

PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

FMT = cat
ifeq ($(shell which fmt >/dev/null 2>&1; echo $$?), 0)
FMT = fmt
endif

# TODO: as long as the ".tmpl"-workflow is not implemented into the reST
# workflow, we have to biuild the XML files for DocBook

$(srctree)/Documentation/DocBook/media_api.xml:
	$(MAKE) -C $(srctree) xmldocs

xmldocs: $(srctree)/Documentation/DocBook/media_api.xml

# ------------------------------------------------------------------------------
# requirements
# ------------------------------------------------------------------------------

ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
sphinx-doc: msg-SphinxDoc
	$(error The '$(SPHINXBUILD)' command was not found)
else
sphinx-doc:
endif

ifeq ($(shell which $(PDFLATEX) >/dev/null 2>&1; echo $$?), 1)
texlive: msg-TeXLive
	$(error The '$(PDFLATEX)' command was not found)
else
texlive:
endif

msg-SphinxDoc:
	@echo "\nsphinx-doc:\n\n\
 Make sure you have a updated Sphinx installed, grab it from\
 http://sphinx-doc.org or install it from the python package\
 manager (pip). \n\n\
 On debian based OS these requirements are installed by::\n\n\
   sudo apt-get install pip \n\n\
   pip install Sphinx\n" | $(FMT)

msg-TeXLive:
	@echo "\nXeLaTeX:\n\n\
 Make sure you have a updated TexLive with XeTex engine installed, grab it\
 it from https://www.tug.org/texlive or install it from your package manager.\n\n\
 Sphinx-doc produce (Xe)LaTeX files which might use additional TeX-packages\
 and fonts. To process these LaTeX files, a TexLive installation with the\
 additional packages is required. On debian based OS these requirements\
 are installed by::\n\n\
   sudo apt-get install \\n\
         texlive-xetex texlive-latex-recommended\n" | $(FMT)


# ------------------------------------------------------------------------------
# !!! deleted media_api.xml from DOCBOOKS objects / the linux_tv book has it's
# !!! own treatment see below target media2rst
#
DOCBOOKS := z8530book.tmpl device-drivers.tmpl \
	    kernel-hacking.tmpl kernel-locking.tmpl deviceiobook.tmpl \
	    writing_usb_driver.tmpl networking.tmpl \
	    kernel-api.tmpl filesystems.tmpl lsm.tmpl usb.tmpl kgdb.tmpl \
	    gadget.tmpl libata.tmpl mtdnand.tmpl librs.tmpl rapidio.tmpl \
	    genericirq.tmpl s390-drivers.tmpl uio-howto.tmpl scsi.tmpl \
	    80211.tmpl debugobjects.tmpl sh.tmpl regulator.tmpl \
	    alsa-driver-api.tmpl writing-an-alsa-driver.tmpl \
	    tracepoint.tmpl gpu.tmpl w1.tmpl \
	    writing_musb_glue_layer.tmpl crypto-API.tmpl iio.tmpl

# ------------------------------------------------------------------------------
# usage
# ------------------------------------------------------------------------------

.PHONY: help help-requirements
help:
	@echo "Please use \`make <target>' where <target> is one of ..."
	@echo
	@echo "  all-HTML : builds all HTML targets:"
	@echo
	@echo "    mainpage   : build HTML main-page"
	@echo "    books.html : build HTML books from the reST files (see dbxml2rst)"
	@echo "    src.html   : build HTML of source-code reST files (see src2rst)"
	@echo "    txt.html   : build HTML from misc reST files (see txt2rst)"
	@echo
	@echo "  make {book} : builds only the HTML of {book}, valid"
	@echo "                values for {book} are: \n\n    $(BOOKS)" | $(FMT)
	@echo
	@echo "  all-reST : builds all reST targets:"
	@echo
	@echo "    dbxml2rst : convert kernel's DocBook-XML books to reST (incl. media2rst)"
	@echo "    media2rst : convert linux_tv (media book) DocBook-XML to reST"
	@echo "    src2rst   : generate reST documentation from source code"
	@echo "    txt2rst   : build reST from misc. linux/Documentaion text files"
	@echo
	@echo "  .. hint:"
	@echo
	@echo "    The reST files are versioned within *this* reposetory."
	@echo
	@echo "  make {fname} : converts only {fname}.tmpl to reST, valid"
	@echo "                 values for {fname} are: \n\n   $(DB2RST)" | $(FMT)
	@echo

help-requirements: msg-SphinxDoc msg-TeXLive


# ------------------------------------------------------------------------------
# main targets
# ------------------------------------------------------------------------------

# update reST in reposetory
.PHONY: all-reST
all-reST: dbxml2rst media2rst src2rst txt2rst

# update github-pages
.PHONY: all-HTML
all-HTML: sphinx-doc mainpage books.html src.html txt.html

.PHONY: clean-HTML
clean-HTML: clean-mainpage clean-books.html clean-src.html clean-txt.html

$(DIST):
	mkdir -p $(DIST)

# ------------------------------------------------------------------------------
# mainpage
# ------------------------------------------------------------------------------

.PHONY: mainpage
mainpage: sphinx-doc | $(DIST)
	$(SPHINXBUILD) -b html -d $(CACHE)/doctrees/$@ $@ $(DIST)

.PHONY: clean-mainpage
clean-mainpage:
	rm -rf $(addprefix $(DIST)/, articles _sources _static) $(CACHE)/doctrees/mainpage
	rm -f $(addprefix $(DIST)/, .buildinfo genindex.html index.html objects.inv search.html searchindex.js)

# ------------------------------------------------------------------------------
# BOOKs
# ------------------------------------------------------------------------------

# DocBook-XML (tmpl) --> reST
# --------------------

DB2RST := $(patsubst %.tmpl, %.rst, $(DOCBOOKS))
dbxml2rst: media2rst $(DB2RST)

.PHONY:	$(DB2RST)
$(DB2RST): xmldocs
	$(DBTOOLS_SCRIPT) db2rst $(patsubst %.rst, %.tmpl, ${@})

# the linux_tv book has it's own treatment
.PHONY: media2rst
media2rst: xmldocs
	$(DBTOOLS_SCRIPT) media2rst

# reST-book --> HTML (sphinx-doc projects)
# ----------------------------------------

.PHONY: books.html
books.html: sphinx-doc $(BOOKS)

.PHONY: $(BOOKS)
$(BOOKS): sphinx-doc | $(DIST)
	@echo "building $@ ..."
	SPHPROJ_CONF=$@.conf $(SPHINXBUILD) -c . -b html -d $(CACHE)/doctrees/$@ $@ $(DIST)/$@

book-dirs := $(addprefix $(DIST)/, $(BOOKS))
book-doctrees := $(addprefix $(CACHE)/doctrees/, $(BOOKS))

.PHONY: clean-books.html
clean-books.html:
	rm -rf $(book-dirs) $(book-doctrees)

# reST-book --> (Xe)LaTeX --> PDF
# -----------------------------------

RST2TEX := $(patsubst %, %.tex, $(BOOKS))
TEX2PDF := $(patsubst %, %.pdf, $(BOOKS))

.PHONY: pdfbooks
pdfbooks: texlive sphinx-doc $(TEX2PDF)

.PHONY: $(RST2TEX)
$(RST2TEX): texlive sphinx-doc
	@echo "building $@ ..."
	rm -rf $(CACHE)/$(patsubst books/%,%,$@)
	SPHPROJ_CONF=$(patsubst %.tex,%.conf,$@) $(SPHINXBUILD) -c . -b xelatex \
		$(PAPEROPT_$(PAPER)) \
		-d $(CACHE)/doctrees/$(patsubst %.tex,%,$@) \
		$(patsubst %.tex,%,$@) \
		$(CACHE)/$(patsubst books/%,%,$@)


$(TEX2PDF): %.pdf : %.tex texlive
	@echo "building $@ ..."
	$(MAKE) -C $(CACHE)/$(patsubst books/%.pdf,%.tex,$@) all-pdf
	$(MAKE) -C $(CACHE)/$(patsubst books/%.pdf,%.tex,$@) dist-pdf

# ------------------------------------------------------------------------------
# source-code
# ------------------------------------------------------------------------------

# autodoc reST
# ------------

.PHONY: src2rst
src2rst:
	rm -rf $(AUTODOC_FOLDER)
	$(AUTODOC_SCRIPT)

# reST --> HTML
# -------------

.PHONY: src.html
src.html: sphinx-doc
	$(SPHINXBUILD) -c . -b html -d $(CACHE)/doctrees/$(AUTODOC_FOLDER) $(AUTODOC_FOLDER) $(DIST)/$(AUTODOC_FOLDER)

.PHONY:
clean-src.html:
	rm -rf $(DIST)/$(AUTODOC_FOLDER) $(CACHE)/doctrees/$(AUTODOC_FOLDER)

# ------------------------------------------------------------------------------
# misc text docs
# ------------------------------------------------------------------------------

# reST include
# ------------

.PHONY: txt2rst
txt2rst:
	rm -rf $(LINUX_MISC_DOC)
	$(SYNCDOC_SCRIPT) txt2rst

# reST --> HTML
# -------------

.PHONY: txt.html
txt.html: sphinx-doc
	$(SPHINXBUILD) -c . -b html -d $(CACHE)/doctrees/$(LINUX_MISC_DOC) $(LINUX_MISC_DOC) $(DIST)/$(LINUX_MISC_DOC)

.PHONY:
clean-txt.html:
	rm -rf $(DIST)/$(LINUX_MISC_DOC)

