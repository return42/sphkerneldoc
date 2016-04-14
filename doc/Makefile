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

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, grab it from http://sphinx-doc.org/)
endif
FMT = cat
ifeq ($(shell which fmt >/dev/null 2>&1; echo $$?), 0)
FMT = fmt
endif

# !!! deleted media_api.xml from DOCBOOKS objects / the linux_tv book has it's
# !!! own treatment

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
	@echo "  allhtml   : builds all HTML targets ..."
	@echo "  mainpage  : build HTML main-page"
	@echo "  htmlbooks : build HTML books from the reST files (see rstbooks)"
	@echo "  htmlsrc   : build HTML of source-code reST files (see src2rst)"
	@echo "  miscdoc   : build HTML from misc reST files (see txt2rst)"
	@echo
	@echo "  make {book} [target] builds only the HTML of {book}",
	@echo "  valid values for {book} are: \n\n     $(BOOKS)" | $(FMT)
	@echo
	@echo "  media2rst : convert linux_tv (media book) DocBook-XML to reST"
	@echo "  rstbooks  : convert kernel's DocBook-XML books to reST"
	@echo "  src2rst   : generate reST documentation from source code"
	@echo "  txt2rst   : build reST from misc. kernel doc text files"
	@echo
	@echo "  .. hint:"
	@echo
	@echo "      The reST files are versioned within this reposetory."
	@echo
	@echo "  make {fname}.rst converts only {filename}.xml to reST,"
	@echo "  valid values for {filename} are: \n\n    $(RST)" | $(FMT)
	@echo

# ------------------------------------------------------------------------------
# github-pages
# ------------------------------------------------------------------------------

.PHONY: allhtml
allhtml: mainpage htmlbooks htmlsrc miscdoc

.PHONY: clean-allhtml
clean-allhtml: clean-mainpage clean-htmlbooks clean-htmlsrc clean-miscdoc

$(GH_PAGES):
	mkdir $(GH_PAGES)

# ------------------------------------------------------------------------------
# mainpage
# ------------------------------------------------------------------------------

.PHONY: mainpage
mainpage: | $(GH_PAGES)
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

RST := $(patsubst %.xml, %.rst, $(DOCBOOKS))
rstbooks: $(RST)

.PHONY:	$(RST)
$(RST):
	$(DBTOOLS_SCRIPT) db2rst $(patsubst %.rst, %.xml, ${@})

# the linux_tv book has it's own treatment
g.PHONY: media2rst
media2rst:
	$(DBTOOLS_SCRIPT) media2rst

# reST --> HTML (sphinx-doc projects)
# -----------------------------------

.PHONY: htmlbooks
htmlbooks: $(BOOKS)

.PHONY: $(BOOKS)
$(BOOKS): | $(GH_PAGES)
	@echo "building $@ ..."
	$(SPHINXBUILD) -c . -b html -d $(CACHE)/doctrees/$@ $@ $(GH_PAGES)/$@

book-dirs := $(addprefix $(GH_PAGES)/, $(BOOKS))
book-doctrees := $(addprefix $(CACHE)/doctrees/, $(BOOKS))

.PHONY: clean-books
clean-htmlbooks:
	rm -rf $(book-dirs) $(book-doctrees)

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
htmlsrc:
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
miscdoc:
	$(SPHINXBUILD) -c . -b html -d $(CACHE)/doctrees/$(LINUX_MISC_DOC) $(LINUX_MISC_DOC) $(GH_PAGES)/$(LINUX_MISC_DOC)

.PHONY:
clean-miscdoc:
	rm -rf $(GH_PAGES)/$(LINUX_MISC_DOC)

