# -*- coding: utf-8; mode: make -*-

# This makefile is used to convert the kernel documentation to reStructuredText
# and build all books (aka DocBooks) with sphinx.

PHONY :=

objtree = $(abspath ..)
obj = .
Q = @
srctree=/share/linux
export srctree

KERNELVERSION := $(shell make -C $(srctree) kernelversion | grep "^[0-9]")
KERNELRELEASE = $(KERNELVERSION)

PYTHONPATH := $(abspath $(objtree)/scripts/site-python):$(PYTHONPATH)

REPO_ROOT      := $(abspath ..)
SCRIPT_FOLDER  := $(objtree)/scripts
TEMPLATES      := $(objtree)/templates
CACHE          := $(objtree)/cache
DOC_FOLDER     := .
BOOKS_FOLDER   := books
AUTODOC_FOLDER := linux_src_doc
LINUX_MISC_DOC := linux_misc_doc
DIST           := $(objtree)/dist

# External programs used

SPHINXBUILD    := sphinx-build
DBTOOLS_SCRIPT := $(SCRIPT_FOLDER)/dbtools
AUTODOC_SCRIPT := $(SCRIPT_FOLDER)/autodoc.sh
SYNCDOC_SCRIPT := $(SCRIPT_FOLDER)/syncdoc.sh

BOOKS := $(filter %/, $(wildcard $(BOOKS_FOLDER)/*/))
BOOKS := $(BOOKS:%/=%)
BOOKS_HTML  := $(patsubst %,%.html, $(BOOKS))
BOOKS_PDF   := $(patsubst %,%.pdf, $(BOOKS))
BOOKS_MAN   := $(patsubst %,%.man, $(BOOKS))
BOOKS_CLEAN := $(patsubst %,%.clean, $(BOOKS))

# sphinx-doc setup
SPHINXOPTS    := -D version=$(KERNELVERSION) -D release=$(KERNELRELEASE)

ALLSPHINXOPTS = $(SPHINXOPTS)

FMT = cat
ifeq ($(shell which fmt >/dev/null 2>&1; echo $$?), 0)
FMT = fmt
endif

# ------------------------------------------------------------------------------
# !!! deleted media_api.xml from DOCBOOKS objects / the linux_tv book has it's
# !!! own treatment see below target media2rst
#
DOCBOOKS := $(wildcard $(srctree)/Documentation/DocBook/*.tmpl)
DOCBOOKS := $(filter-out %/media_api.tmpl,$(DOCBOOKS))
DOCBOOKS := $(filter-out %/media-entities.tmpl,$(DOCBOOKS))
DOCBOOKS := $(filter-out %/media-indices.tmpl,$(DOCBOOKS))
DOCBOOKS := $(DOCBOOKS:$(srctree)/Documentation/DocBook/%=%)

# ------------------------------------------------------------------------------
# usage
# ------------------------------------------------------------------------------

PHONY += help help-rqmts

help-rqmts: msg-SphinxDoc msg-rst2pdf msg-TeXLive

help:
	$(Q)echo "Please use \`make <target>' where <target> is one of ..."
	$(Q)echo
	$(Q)echo "all-HTML : builds all HTML targets:"
	$(Q)echo
	$(Q)echo "  mainpage   : build HTML main-page"
	$(Q)echo "  books-html : build HTML books from the reST files (see dbxml2rst)"
	$(Q)echo "  src.html   : build HTML of source-code reST files (see src2rst)"
	$(Q)echo "  txt.html   : build HTML from misc reST files (see txt2rst)"
	$(Q)echo "  help-rqmts : info about build requirements"
	$(Q)echo ""
	$(Q)echo "  books/{name}.html : build only the HTML of document {name}"
	$(Q)echo "    valid values for books/{name}.html are: \n\n   $(BOOKS_HTML)" | $(FMT)
	$(Q)echo
	$(Q)echo "books-pdf : builds all PDF targets:"
	$(Q)echo
	$(Q)echo "  books/{name}.pdf : build only the PDF of document {name}"
	$(Q)echo "    valid values for books/{name}.pdf are: \n\n   $(BOOKS_PDF)" | $(FMT)
	$(Q)echo
	$(Q)echo "The HTML & PDF output formats are placed into folder:"
	$(Q)echo ""
	$(Q)echo "    $(DIST)"
	$(Q)echo ""
	$(Q)echo "all-reST : builds all reST targets:"
	$(Q)echo
	$(Q)echo "  dbxml2rst : convert kernel's DocBook-XML books to reST (incl. media2rst)"
	$(Q)echo "  media2rst : convert linux_tv (media book) DocBook-XML to reST"
	$(Q)echo "  src2rst   : generate reST documentation from source code"
	$(Q)echo "  txt2rst   : build reST from misc. linux/Documentaion text files"
	$(Q)echo
	$(Q)echo "  .. hint:"
	$(Q)echo
	$(Q)echo "    The reST files are versioned within *this* reposetory."
	$(Q)echo
	$(Q)echo "  {fname}.rst : converts only {fname}.tmpl to reST, valid"
	$(Q)echo "    values for {fname} are: \n\n   $(DB2RST)" | $(FMT)
	$(Q)echo


# ------------------------------------------------------------------------------
# requirements
# ------------------------------------------------------------------------------

PHONY += sphinx-doc msg-SphinxDoc rst2pdf msg-rst2pdf

ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
sphinx-doc: msg-SphinxDoc
	$(error The '$(SPHINXBUILD)' command was not found)
else
sphinx-doc:
	@:
endif

ifeq ($(shell python -c "import rst2pdf" >/dev/null 2>&1; echo $$?), 1)
rst2pdf: msg-rst2pdf
	$(error The python module rst2pdf was not found)
else
rst2pdf:
	@:
endif

ifeq ($(shell which $(PDFLATEX) >/dev/null 2>&1; echo $$?), 1)
texlive: msg-TeXLive
	$(error The '$(PDFLATEX)' command was not found)
else
texlive:
	@:
endif

msg-SphinxDoc:
	$(Q)echo "\n\
Base documentation build system requires sphinx-doc:\n\n\
  Make sure you have an updated Sphinx installed, grab it from\n\
  http://sphinx-doc.org or install it from the python package\n\
  manager (pip). On debian based OS these requirements are \n\
  installed by::\n\n\
    sudo apt-get install pip \n\
    pip install Sphinx"

msg-rst2pdf:
	$(Q)echo "\n\
PDF output requires rst2pdf:\n\n\
  Make sure you have an updated rst2pdf installed, grab it from\n\
  https://github.com/rst2pdf/rst2pdf or install it with pip::\n\n\
    pip install rst2pdf\n\n\
  If the installation fails, this might be due to missed header files\n\
  needed by pillow which is a requirement of rst2pdf. For details take\n\
  a look at: \n\n\
    https://github.com/python-pillow/Pillow/blob/master/docs/installation.rst#external-libraries\n\n\
  Mostly the jpeg headers are missed. On debian based OS these requirements\n\
  are installed by::\n\n\
    sudo apt-get install libjpeg-dev"

msg-TeXLive:
	$(Q)echo "\n\
TeX output requires TexLive:\n\n\
  Make sure you have a updated TeXLive with XeTeX engine installed, grab it\n\
  it from https://www.tug.org/texlive or install it from your package manager.\n\n\
  Sphinx-doc produce (Xe)LaTeX files which might use additional TeX-packages\n\
  and fonts. To process these LaTeX files, a TexLive installation with the\n\
  additional packages is required. On debian based OS these requirements\n\
  are installed by::\n\n\
    sudo apt-get install \\n\
          texlive-xetex texlive-latex-recommended\n"

# ------------------------------------------------------------------------------
# main targets
# ------------------------------------------------------------------------------

# update reST in reposetory
PHONY += all-reST
all-reST: dbxml2rst media2rst src2rst txt2rst

# update github-pages
PHONY += all-HTML books-html books-pdf books-clean
all-HTML: sphinx-doc mainpage books-html src.html txt.html
books-html:  sphinx-doc $(BOOKS_HTML)
books-man:  sphinx-doc $(BOOKS_MAN)
books-pdf:   rst2pdf $(BOOKS_PDF)
books-clean: $(BOOKS_CLEAN)

PHONY += clean
clean: mainpage.clean books-clean clean-src.html clean-txt.html

$(DIST):
	mkdir -p $(DIST)

# ------------------------------------------------------------------------------
# mainpage
# ------------------------------------------------------------------------------

PHONY += mainpage mainpage.clean
mainpage: sphinx-doc | $(DIST)
	$(SPHINXBUILD) $(ALLSPHINXOPTS) -b html -d $(CACHE)/doctrees/$@ $@ $(DIST)
	$(Q)echo "HTML build OK / start file at:\n    file://$(abspath $(DIST)/index.html)"

mainpage.clean:
	rm -rf $(addprefix $(DIST)/, articles _sources _static) $(CACHE)/doctrees/mainpage
	rm -f $(addprefix $(DIST)/, .buildinfo genindex.html index.html objects.inv search.html searchindex.js)

# ------------------------------------------------------------------------------
# BOOKs
# ------------------------------------------------------------------------------

PHONY += $(BOOKS_CLEAN)
$(BOOKS_CLEAN):
	rm -rf $(DIST)/$(patsubst %.clean,%,$@) $(CACHE)/doctrees/$(patsubst %.clean,%,$@)


# DocBook-XML (tmpl) --> reST
# --------------------

DB2RST := $(patsubst %.tmpl, %.rst, $(DOCBOOKS))
dbxml2rst: media2rst $(DB2RST)

.PHONY:	$(DB2RST)
$(DB2RST):
	$(DBTOOLS_SCRIPT) db2rst $(patsubst %.rst, %.tmpl, ${@})

$(srctree)/Documentation/DocBook/media_api.xml:
	$(MAKE) -C $(srctree) xmldocs

# the linux_tv book has it's own treatment
PHONY += media2rst
media2rst: $(srctree)/Documentation/DocBook/media_api.xml
	$(DBTOOLS_SCRIPT) media2rst

# reST-book --> HTML (sphinx-doc projects)
# ----------------------------------------

PHONY += $(BOOKS_HTML)
$(BOOKS_HTML): sphinx-doc | $(DIST)
	$(Q)SPHPROJ_CONF=$(patsubst %.html,%/conf.py,$@) \
	  $(SPHINXBUILD) $(ALLSPHINXOPTS) -b html \
	  -c $(obj) \
	  -d $(CACHE)/doctrees/$(patsubst %.html,%,$@) \
	  $(obj)/$(patsubst %.html,%,$@) \
	  $(DIST)/$(patsubst %.html,%,$@)
	$(Q)echo "HTML build OK / start file at:\n    file://$(abspath $(DIST)/$(patsubst %.html,%,$@)/index.html)"

# reST-book --> man pages
# ----------------------------------------

PHONY += $(BOOKS_MAN)
$(BOOKS_MAN): sphinx-doc | $(DIST)
	$(Q)SPHPROJ_CONF=$(patsubst %.man,%/conf.py,$@) \
	  $(SPHINXBUILD) $(ALLSPHINXOPTS) -b kernel-doc-man \
	  -c $(obj) \
	  -d $(CACHE)/doctrees/$(patsubst %.man,%,$@) \
	  $(obj)/$(patsubst %.man,%,$@) \
	  $(DIST)/$(patsubst %.man,%/man,$@)
	$(Q)echo "man page build OK / destination at:\n    file://$(abspath $(DIST)/$(patsubst %.man,%/man,$@))"


# reST-book --> PDF
# ----------------------------------------

PHONY += $(BOOKS_PDF)
$(BOOKS_PDF): rst2pdf sphinx-doc | $(DIST)
	$(Q)SPHPROJ_CONF=$(patsubst %.pdf,%/conf.py,$@) \
	  $(SPHINXBUILD) $(ALLSPHINXOPTS) -b pdf \
	  -c $(obj) \
	  -d $(CACHE)/doctrees/$(patsubst %.pdf,%,$@) \
	  $(obj)/$(patsubst %.pdf,%,$@) \
          $(DIST)/rst2pdf
	$(Q)echo "PDF build OK / pdf files stored in:\n    file://$(abspath $(DIST)/rst2pdf)"



# # reST-book --> (Xe)LaTeX --> PDF
# # -----------------------------------

# RST2TEX := $(patsubst %, %.tex, $(BOOKS))
# TEX2PDF := $(patsubst %, %.pdf, $(BOOKS))
# PDFLATEX       := xelatex
# MAKEINDEX      := makeindex
# PAPER       := a4

# PAPEROPT_a4     = -D latex_paper_size=a4
# PAPEROPT_letter = -D latex_paper_size=letter
# ALLSPHINXOPTS   = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

# # the i18n builder cannot share the environment and doctrees with the others
# I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

# DIST_BOOKS     := $(DIST)/books-pdf
# export DIST_BOOKS

# .PHONY: pdfbooks
# pdfbooks: texlive sphinx-doc $(TEX2PDF)

# .PHONY: $(RST2TEX)
# $(RST2TEX): texlive sphinx-doc
# 	@echo "building $@ ..."
# 	rm -rf $(CACHE)/$(patsubst books/%,%,$@)
# 	SPHPROJ_CONF=$(patsubst %.tex,conf.py,$@) $(SPHINXBUILD) $(ALLSPHINXOPTS) -c . -b xelatex \
# 		$(PAPEROPT_$(PAPER)) \
# 		-d $(CACHE)/doctrees/$(patsubst %.tex,%,$@) \
# 		$(patsubst %.tex,%,$@) \
# 		$(CACHE)/$(patsubst books/%,%,$@)


# $(TEX2PDF): %.pdf : %.tex texlive
# 	@echo "building $@ ..."
# 	$(MAKE) -C $(CACHE)/$(patsubst books/%.pdf,%.tex,$@) all-pdf
# 	$(MAKE) -C $(CACHE)/$(patsubst books/%.pdf,%.tex,$@) dist-pdf

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
	$(SPHINXBUILD) $(ALLSPHINXOPTS) -c . -b html -d $(CACHE)/doctrees/$(AUTODOC_FOLDER) $(AUTODOC_FOLDER) $(DIST)/$(AUTODOC_FOLDER)

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
	$(SPHINXBUILD) $(ALLSPHINXOPTS) -c . -b html -d $(CACHE)/doctrees/$(LINUX_MISC_DOC) $(LINUX_MISC_DOC) $(DIST)/$(LINUX_MISC_DOC)

.PHONY:
clean-txt.html:
	rm -rf $(DIST)/$(LINUX_MISC_DOC)

# Declare the contents of the .PHONY variable as phony.  We keep that
# information in a variable se we can use it in if_changed and friends.

.PHONY: $(PHONY)
