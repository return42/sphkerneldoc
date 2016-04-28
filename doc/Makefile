# -*- coding: utf-8; mode: make -*-

# This makefile is used to convert the kernel documentation to reStructuredText
# and build all books (aka DocBooks) with sphinx.

REPO_ROOT      := ..
SCRIPT_FOLDER  := $(REPO_ROOT)/scripts
TEMPLATES      := $(REPO_ROOT)/templates
CACHE          := $(REPO_ROOT)/cache
DOC_FOLDER     := .
BOOKS_FOLDER   := books
AUTODOC_FOLDER := linux_src_doc
LINUX_MISC_DOC := linux_misc_doc

# External programs used

SPHINXBUILD    := sphinx-build
KERNELDOC      := $(SCRIPT_FOLDER)/kernel-doc
DBTOOLS_SCRIPT := $(SCRIPT_FOLDER)/dbtools
AUTODOC_SCRIPT := $(SCRIPT_FOLDER)/autodoc.sh
SYNCDOC_SCRIPT := $(SCRIPT_FOLDER)/syncdoc.sh

LATEX          := latex
PDFLATEX       := xelatex
MAKEINDEX      := makeindex

GH_PAGES := $(CACHE)/gh-pages
BOOKS   := $(wildcard $(BOOKS_FOLDER)/*)

# sphinx-doc setup
SPHINXOPTS  :=
PAPER       := a4

PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

# TODO: include linux/Documentation/DocBook/Makefile and run "make xmldocs" as
# prerequisite

FMT = cat
ifeq ($(shell which fmt >/dev/null 2>&1; echo $$?), 0)
FMT = fmt
endif

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
	@echo "\
Make sure you have a updated Sphinx installed, grab it from \
http://sphinx-doc.org or install it from the python package \
manager	(pip). \n\n\
On debian based OS these requirements are installed by::\n\n\
  sudo apt-get install pip \n\n\
  pip install Sphinx\n" | $(FMT)

msg-TeXLive:
	@echo "\
Make sure you have a updated TexLive installed, grab it from \
https://www.tug.org/texlive or install it from your package manager. \n\n\
Sphinx-doc produce LaTeX files which uses additional TeX-packages and \
fonts. To process these LaTeX files, a TexLive installation with the \
additional packages and fonts is required. On debian based OS these \
requirements are installed by::\n\n\
  sudo apt-get install \\ \n\
        texlive-latex-recommended texlive-fonts-recommended \
texlive-latex-extra texlive-xetex\n" | $(FMT)


# ------------------------------------------------------------------------------
# !!! deleted media_api.xml from DOCBOOKS objects / the linux_tv book has it's
# !!! own treatment see below target media2rst
#
DOCBOOKS := z8530book.xml device-drivers.xml \
	    kernel-hacking.xml kernel-locking.xml deviceiobook.xml \
	    writing_usb_driver.xml networking.xml \
	    kernel-api.xml filesystems.xml lsm.xml usb.xml kgdb.xml \
	    gadget.xml libata.xml mtdnand.xml librs.xml rapidio.xml \
	    genericirq.xml s390-drivers.xml uio-howto.xml scsi.xml \
	    80211.xml debugobjects.xml sh.xml regulator.xml \
	    alsa-driver-api.xml writing-an-alsa-driver.xml \
	    tracepoint.xml gpu.xml w1.xml \
	    writing_musb_glue_layer.xml crypto-API.xml iio.xml

# ------------------------------------------------------------------------------
# usage
# ------------------------------------------------------------------------------

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of ..."
	@echo
	@echo "  all-HTML : builds all HTML targets:"
	@echo
	@echo "    mainpage  : build HTML main-page"
	@echo "    htmlbooks : build HTML books from the reST files (see dbxml2rst)"
	@echo "    htmlsrc   : build HTML of source-code reST files (see src2rst)"
	@echo "    miscdoc   : build HTML from misc reST files (see txt2rst)"
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
	@echo "  make {fname} : converts only {fname}.xml to reST, valid"
	@echo "                 values for {fname} are: \n\n   $(DB2RST)" | $(FMT)
	@echo

# ------------------------------------------------------------------------------
# main targets
# ------------------------------------------------------------------------------

# update reST in reposetory
.PHONY: all-reST
all-reST: dbxml2rst media2rst src2rst txt2rst

# update github-pages
.PHONY: all-HTML
all-HTML: sphinx-doc mainpage htmlbooks htmlsrc miscdoc

.PHONY: clean-HTML
clean-HTML: clean-mainpage clean-htmlbooks clean-htmlsrc clean-miscdoc

$(GH_PAGES):
	mkdir $(GH_PAGES)

# ------------------------------------------------------------------------------
# mainpage
# ------------------------------------------------------------------------------

.PHONY: mainpage
mainpage: sphinx-doc | $(GH_PAGES)
	$(SPHINXBUILD) -b html -d $(CACHE)/doctrees/$@ $@ $(GH_PAGES)

.PHONY: clean-mainpage
clean-mainpage:
	rm -rf $(addprefix $(GH_PAGES)/, articles _sources _static) $(CACHE)/doctrees/mainpage
	rm -f $(addprefix $(GH_PAGES)/, .buildinfo genindex.html index.html objects.inv search.html searchindex.js)

# ------------------------------------------------------------------------------
# BOOKs
# ------------------------------------------------------------------------------

# DocBook-XML --> reST
# --------------------

DB2RST := $(patsubst %.xml, %.rst, $(DOCBOOKS))
dbxml2rst: media2rst $(DB2RST)

.PHONY:	$(DB2RST)
$(DB2RST):
	$(DBTOOLS_SCRIPT) db2rst $(patsubst %.rst, %.xml, ${@})

# the linux_tv book has it's own treatment
.PHONY: media2rst
media2rst:
	$(DBTOOLS_SCRIPT) media2rst

# reST-book --> HTML (sphinx-doc projects)
# ----------------------------------------

.PHONY: htmlbooks
htmlbooks: sphinx-doc $(BOOKS)

.PHONY: $(BOOKS)
$(BOOKS): sphinx-doc | $(GH_PAGES)
	@echo "building $@ ..."
	$(SPHINXBUILD) -c . -b html -d $(CACHE)/doctrees/$@ $@ $(GH_PAGES)/$@

book-dirs := $(addprefix $(GH_PAGES)/, $(BOOKS))
book-doctrees := $(addprefix $(CACHE)/doctrees/, $(BOOKS))

.PHONY: clean-htmlbooks
clean-htmlbooks:
	rm -rf $(book-dirs) $(book-doctrees)

# reST-book --> LaTeX --> PDF
# -----------------------------------

RST2TEX := $(patsubst %, %.tex, $(BOOKS))
TEX2PDF := $(patsubst %, %.pdf, $(BOOKS))

.PHONY: pdfbooks
pdfbooks: texlive sphinx-doc $(TEX2PDF)

.PHONY: $(RST2TEX)
$(RST2TEX): texlive sphinx-doc
	@echo "building $@ ..."
	$(SPHINXBUILD) -c . -b latex \
		$(PAPEROPT_$(PAPER)) \
		-d $(CACHE)/doctrees/$(patsubst %.tex,%,$@) \
		$(patsubst %.tex,%,$@) \
		$(CACHE)/$(patsubst books/%,%,$@)

$(TEX2PDF): %.pdf : %.tex texlive
	@echo "building $@ ..."
	$(MAKE) -C $(CACHE)/$(patsubst books/%.pdf,%.tex,$@) all-pdf


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

.PHONY: htmlsrc
htmlsrc: sphinx-doc
	$(SPHINXBUILD) -c . -b html -d $(CACHE)/doctrees/$(AUTODOC_FOLDER) $(AUTODOC_FOLDER) $(GH_PAGES)/$(AUTODOC_FOLDER)

.PHONY:
clean-htmlsrc:
	rm -rf $(GH_PAGES)/$(AUTODOC_FOLDER) $(CACHE)/doctrees/$(AUTODOC_FOLDER)

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

.PHONY: miscdoc
miscdoc: sphinx-doc
	$(SPHINXBUILD) -c . -b html -d $(CACHE)/doctrees/$(LINUX_MISC_DOC) $(LINUX_MISC_DOC) $(GH_PAGES)/$(LINUX_MISC_DOC)

.PHONY:
clean-miscdoc:
	rm -rf $(GH_PAGES)/$(LINUX_MISC_DOC)

