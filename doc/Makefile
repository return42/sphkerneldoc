# -*- coding: utf-8; mode: make -*-

# External programs used

SPHINXBUILD    := sphinx-build
DBTOOLS_SCRIPT := /share/dbxml2rst/linux-db2rst
AUTODOC_SCRIPT := $(SCRIPT_FOLDER)/autodoc.py

# We need some generic definitions (do not try to remake the file).
Kbuild.include: ;
include Kbuild.include

# This makefile is used to convert the kernel documentation to reStructuredText
# and build all books (aka DocBooks) with sphinx.

PHONY =

objtree = $(abspath ..)
obj = .
Q = @
srctree=/share/linux
export srctree

KERNELVERSION := $(shell make -C $(srctree) kernelversion | grep "^[0-9]")

ifndef $(KERNELRELEASE)
  KERNELRELEASE = $(KERNELVERSION)
endif

PYTHONPATH := $(abspath $(objtree)/scripts/site-python):$(PYTHONPATH)

SCRIPT_FOLDER  := $(objtree)/scripts
CACHE          := $(objtree)/cache
AUTODOC_FOLDER := $(objtree)/doc/linux_src_doc
DIST           := $(objtree)/dist

# sphinx-build setup
SPHINXOPTS = -D version=$(KERNELVERSION) -D release=$(KERNELRELEASE)

# Sphinx projects, we call them *books* which is more common to authors.
BOOKS_FOLDER = $(obj)/Documentation
BOOKS=$(filter-out books/intro,                                           \
	$(patsubst $(BOOKS_FOLDER)/%/conf.py,books/%,$(wildcard $(BOOKS_FOLDER)/*/conf.py)) \
	)

# fine grained targets
BOOKS_HTML  = $(patsubst %,%.html, $(BOOKS))
BOOKS_CLEAN = $(patsubst %,%.clean, $(BOOKS))
BOOKS_MAN   = $(patsubst %,%.man, $(BOOKS))
BOOKS_PDF   = $(patsubst %,%.pdf, $(BOOKS))

# for the period of transition from books_migrated
MIGRATION_FOLDER=$(BOOKS_FOLDER)/books_migrated
BOOKS_MIGRATED=$(patsubst $(MIGRATION_FOLDER)/%/conf.py,books/%,$(wildcard $(MIGRATION_FOLDER)/*/conf.py))
BOOKS_MIGRATED_HTML  = $(patsubst %,%.html, $(BOOKS_MIGRATED))
BOOKS_MIGRATED_CLEAN = $(patsubst %,%.clean, $(BOOKS_MIGRATED))
BOOKS_MIGRATED_MAN   = $(patsubst %,%.man, $(BOOKS_MIGRATED))
BOOKS_MIGRATED_PDF   = $(patsubst %,%.pdf, $(BOOKS_MIGRATED))

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
# requirements
# ------------------------------------------------------------------------------

PHONY += msg-sphinx-builder sphinx-builder

msg-sphinx-builder:
	$(Q)echo "\n\
The base documentation build system requires sphinx-doc:\n\n\
  Make sure you have an updated Sphinx installed, grab it from\n\
  http://sphinx-doc.org or install it from the python package\n\
  manager (pip). On debian based OS these requirements are \n\
  installed by::\n\n\
    sudo apt-get install pip \n\
    pip install Sphinx"

ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
sphinx-builder: msg-sphinx-builder
	$(error The '$(SPHINXBUILD)' command was not found)
else
sphinx-builder:
	@:
endif

PHONY += msg-rst2pdf-pkg rst2pdf-pkg

msg-rst2pdf-pkg:
	$(Q)echo "\n\
Building PDF output requires te python package rst2pdf:\n\n\
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

ifeq ($(shell python -c "import rst2pdf" >/dev/null 2>&1; echo $$?), 1)
rst2pdf-pkg: msg-rst2pdf-pkg
	$(error The python module rst2pdf was not found)
else
rst2pdf-pkg:
	@:
endif

PHONY += msg-texlive texlive

ifeq ($(shell which $(PDFLATEX) >/dev/null 2>&1; echo $$?), 1)
texlive: msg-TeXLive
	$(error The '$(PDFLATEX)' command was not found)
else
texlive:
	@:
endif

msg-texlive:
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
# usage
# ------------------------------------------------------------------------------

PHONY += help help-rqmts

help-rqmts: msg-sphinx-builder msg-rst2pdf-pkg msg-texlive

help:
	$(Q)echo "Please use \`make <target>' where <target> is one of ..."
	$(Q)echo
	$(Q)echo "all-HTML : build all HTML targets:"
	$(Q)echo
	$(Q)echo "  intro.html    : build HTML intro page (root index.html)"
	$(Q)echo "  books.html    : build HTML books from the reST files (see dbxml2rst)"
	$(Q)echo "  src.html      : build HTML of source-code reST files (see src2rst)"
	$(Q)echo
	$(Q)echo "help-rqmts : info about build requirements"
	$(Q)echo
	$(Q)echo "books/{name}.html : build only the HTML of document {name}"
	$(Q)echo "    valid values for books/{name}.html are: \n\n   $(BOOKS_HTML) $(BOOKS_MIGRATED_HTML)" | $(FMT)
	$(Q)echo
	$(Q)echo "books.pdf : builds all PDF targets (with the buggy rstpdf):"
	$(Q)echo
	$(Q)echo "  books/{name}.pdf : build only the PDF of document {name}"
	$(Q)echo "    valid values for books/{name}.pdf are: \n\n   $(BOOKS_PDF) $(BOOKS_MIGRATED_PDF)" | $(FMT)
	$(Q)echo
	$(Q)echo "books.man : builds all man page targets:"
	$(Q)echo
	$(Q)echo "  books/{name}.man : build only the man page of document {name}"
	$(Q)echo "    valid values for books/{name}.pdf are: \n\n   $(BOOKS_MAN) $(BOOKS_MIGRATED_MAN)" | $(FMT)
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
	$(Q)echo
	$(Q)echo "  .. hint:"
	$(Q)echo
	$(Q)echo "    The reST files are versioned within *this* reposetory."
	$(Q)echo
	$(Q)echo "  {fname}.rst : converts only {fname}.tmpl to reST, valid"
	$(Q)echo "    values for {fname} are: \n\n   $(DB2RST)" | $(FMT)
	$(Q)echo
	$(Q)echo "make V=0|1 [targets] 0 => quiet build (default), 1 => verbose build"
	$(Q)echo "make V=2   [targets] 2 => give reason for rebuild of target"

# ------------------------------------------------------------------------------
# main targets
# ------------------------------------------------------------------------------

ALLSPHINXOPTS = $(SPHINXOPTS)

DIST_BOOKS = $(DIST)/books
CACHE_BOOKS = $(CACHE)/books

# update reST in reposetory
PHONY += all-reST
all-reST: dbxml2rst media2rst src2rst

# update github-pages
PHONY += all-HTML books.html books.pdf books.man books.clean
all-HTML:    sphinx-builder books.html src.html
books.html:  sphinx-builder $(BOOKS_HTML) $(BOOKS_MIGRATED_HTML) intro.html
books.man:   sphinx-builder $(BOOKS_MAN) $(BOOKS_MIGRATED_MAN)
books.pdf:   rst2pdf $(BOOKS_PDF) $(BOOKS_MIGRATED_MAN)
books.clean: $(BOOKS_CLEAN) $(BOOKS_MIGRATED_CLEAN) intro.clean
#books-rqmts: msg-sphinx-builder msg-rst2pdf-pkg

PHONY += clean
clean: intro.clean books.clean

$(DIST_BOOKS):
	mkdir -p $(DIST_BOOKS)

# $2 sphinx builder e.g. "html"
# $3 name of the book / e.g. "gpu", used as:
#    * dest folder relative to $(DIST_BOOKS) and
#    * cache folder relative to $(CACHE_BOOKS)
# $4 dest subfolder e.g. "man" for man pages at gpu/man
# $5 reST source folder relative to $(BOOKS_FOLDER),
#    e.g. "books_migrated" for the migrated books

quiet_cmd_sphinx = SPHINX  $@ --> file://$(abspath $(DIST_BOOKS)/$3$4)
      cmd_sphinx = SPHPROJ_CONF=$(BOOKS_FOLDER)/$5$3/conf.py \
	$(SPHINXBUILD) $(ALLSPHINXOPTS) -b $2 \
	-c $(obj) \
	-d $(CACHE_BOOKS)/$3 \
	$(BOOKS_FOLDER)/$5$3 \
	$(abspath $(DIST_BOOKS)/$3$4)

# $2 name of the book / e.g. "gpu", used to clean:
#    * dest folder relative to $(DIST_BOOKS) and
#    * cache folder relative to $(CACHE_BOOKS)
quiet_cmd_sphinx_clean = CLEAN  $@
      cmd_sphinx_clean = rm -rf $(CACHE_BOOKS)/$2 $(DIST_BOOKS)/$2

# ------------------------------------------------------------------------------
# BOOKs
# ------------------------------------------------------------------------------

PHONY += $(BOOKS_CLEAN)
$(BOOKS_CLEAN):
	$(call cmd,sphinx_clean,$(patsubst books/%.clean,%,$@))

PHONY += $(BOOKS_HTML)
$(BOOKS_HTML): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,html,$(patsubst books/%.html,%,$@))

PHONY += $(BOOKS_MAN)
$(BOOKS_MAN): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,kernel-doc-man,$(patsubst books/%.man,%,$@),/man)
	$(Q)find $(DIST_BOOKS)/$(patsubst books/%.man,%,$@)/man -name '*.9' -exec gzip -nf {} +

PHONY += $(BOOKS_PDF)
$(BOOKS_PDF): sphinx-builder rst2pdf-pkg | $(DIST_BOOKS)
	$(call cmd,sphinx,pdf,$(patsubst books/%.pdf,%,$@),/rst2pdf)


# migrated DocBook-XML to reST content
# ------------------------------------

PHONY += $(BOOKS_MIGRATED_CLEAN)
$(BOOKS_MIGRATED_CLEAN):
	$(call cmd,sphinx_clean,$(patsubst books/%.clean,%,$@))

PHONY += $(BOOKS_MIGRATED_HTML)
$(BOOKS_MIGRATED_HTML): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,html,$(patsubst books/%.html,%,$@),,books_migrated/)

PHONY += $(BOOKS_MIGRATED_MAN)
$(BOOKS_MIGRATED_MAN): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,kernel-doc-man,$(patsubst books/%.man,%,$@),/man,books_migrated/)
	$(Q)find $(DIST_BOOKS)/$(patsubst books/%.man,%,$@)/man -name '*.9' -exec gzip -nf {} +

PHONY += $(BOOKS_PDF)
$(BOOKS_MIGRATED_PDF): sphinx-builder rst2pdf-pkg | $(DIST_BOOKS)
	$(call cmd,sphinx,pdf,$(patsubst books/%.pdf,%,$@),/rst2pdf,books_migrated/)


# ------------------------------------------------------------------------------
# intro page
# ------------------------------------------------------------------------------

INDEX_CACHE    = $(CACHE)/index-page
INDEX_ARTICLES = $(filter-out index.rst,$(patsubst $(BOOKS_FOLDER)/%,%,$(wildcard $(BOOKS_FOLDER)/*.rst)))
INDEX_REL = ../../doc/Documentation/

PHONY += intro.html intro.clean

quiet_cmd_intro_clean = CLEAN  $@
      cmd_intro_clean = \
	rm -rf $(INDEX_CACHE);\
	rm -rf $(addprefix $(DIST)/, _sources _static articles);\
	rm -f  $(addprefix $(DIST)/, .buildinfo genindex.html index.html objects.inv search.html searchindex.js)

quiet_cmd_intro = CLEAN  $@
      cmd_intro = \
	rm -rf $(INDEX_CACHE)/articles   ;\
	mkdir -p $(INDEX_CACHE)/articles ;\
	ln -s -t $(INDEX_CACHE)/articles $(addprefix ../$(INDEX_REL),$(INDEX_ARTICLES) article_refs.txt ) ;\
	ln -f -s -t $(INDEX_CACHE) $(addprefix $(INDEX_REL),index.rst poc_sphkerneldoc) ;\
	ln -f -s -t $(INDEX_CACHE) $(addprefix ../../doc/,conf.py) ;\
	$(SPHINXBUILD) $(ALLSPHINXOPTS) -b $2\
		-d $(INDEX_CACHE)/.doctrees \
		$(INDEX_CACHE) \
		$(DIST)

intro.clean:
	$(call cmd,intro_clean)

intro.html: sphinx-builder | $(DIST)
	$(call cmd,intro,html)


# DocBook-XML (tmpl) --> reST
# --------------------

DB2RST := $(patsubst %.tmpl, %.rst, $(DOCBOOKS))
dbxml2rst: media2rst $(DB2RST)

.PHONY:	$(DB2RST)
$(DB2RST):
	$(DBTOOLS_SCRIPT) --out=$(MIGRATION_FOLDER) db2rst $(srctree) $(patsubst %.rst, %.tmpl, ${@})

$(srctree)/Documentation/DocBook/media_api.xml:
	$(MAKE) -C $(srctree) xmldocs

# the linux_tv book has it's own treatment
PHONY += media2rst
media2rst: $(srctree)/Documentation/DocBook/media_api.xml
	$(DBTOOLS_SCRIPT) --out=$(MIGRATION_FOLDER) media2rst $(srctree)


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
# pdfbooks: texlive sphinx-builder $(TEX2PDF)

# .PHONY: $(RST2TEX)
# $(RST2TEX): texlive sphinx-builder
# 	@echo "building $@ ..."
# 	rm -rf $(CACHE)/$(patsubst books/%,%,$@)
# 	SPHPROJ_CONF=$(patsubst %.tex,conf.py,$@) $(SPHINXBUILD) $(ALLSPHINXOPTS) -c . -b xelatex \
# # 		$(PAPEROPT_$(PAPER)) \
# # 		-d $(CACHE)/doctrees/$(patsubst %.tex,%,$@) \
# # 		$(patsubst %.tex,%,$@) \
# # 		$(CACHE)/$(patsubst books/%,%,$@)


# $(TEX2PDF): %.pdf : %.tex texlive
# 	@echo "building $@ ..."
# 	$(MAKE) -C $(CACHE)/$(patsubst books/%.pdf,%.tex,$@) all-pdf
# 	$(MAKE) -C $(CACHE)/$(patsubst books/%.pdf,%.tex,$@) dist-pdf

# ------------------------------------------------------------------------------
# source-code
# ------------------------------------------------------------------------------

# autodoc reST
# ------------

PHONY += src2rst
src2rst:
	rm -rf $(AUTODOC_FOLDER)
	$(AUTODOC_SCRIPT) $(srctree) $(AUTODOC_FOLDER)

# reST --> HTML
# -------------

PHONY += src.html
src.html: sphinx-builder
	$(SPHINXBUILD) $(ALLSPHINXOPTS) -b html\
		-c .\
		-d $(CACHE)/doctrees/linux_src_doc \
		$(AUTODOC_FOLDER) \
		$(DIST)/linux_src_doc

PHONY += src.clean
src.clean:
	rm -rf $(CACHE)/doctrees/linux_src_doc $(DIST)/linux_src_doc

# Declare the contents of the .PHONY variable as phony.  We keep that
# information in a variable se we can use it in if_changed and friends.

.PHONY: $(PHONY)
