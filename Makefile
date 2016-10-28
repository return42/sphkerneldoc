# -*- coding: utf-8; mode: make -*-

# sphinx-build setup
SPHINXOPTS =
# The paper size ('letter' or 'a4').
PAPER     := a4
# The font size ('10pt', '11pt' or '12pt')
FONTSIZE  := 11

srctree=/share/linux-docs-next
export srctree

# External programs used

SPHINXBUILD    := sphinx-build
DBTOOLS_SCRIPT := linux-db2rst
AUTODOC_SCRIPT := kernel-autodoc

# We need some generic definitions (do not try to remake the file).
Kbuild.include: ;
include Kbuild.include

# This makefile is used to convert the kernel documentation to reStructuredText
# and build all books (aka DocBooks) with sphinx.

PHONY =

objtree = .
obj = .
Q = @

KERNELVERSION := $(shell make -C $(srctree) kernelversion | grep "^[0-9]")

ifndef $(KERNELRELEASE)
  KERNELRELEASE = $(KERNELVERSION)
endif

CACHE          := $(objtree)/cache
AUTODOC_FOLDER := $(objtree)/linux_src_doc
DIST           := $(objtree)/dist
DIST_BOOKS = $(DIST)/books
CACHE_BOOKS = $(CACHE)/books


# Sphinx projects, we call them *books* which is more common to authors.
BOOKS_FOLDER = $(obj)/Documentation
BOOKS=$(filter-out books/intro,                                           \
	$(patsubst $(BOOKS_FOLDER)/%/conf.py,books/%,$(wildcard $(BOOKS_FOLDER)/*/conf.py)) \
	)

# fine grained targets
BOOKS_HTML  = $(patsubst %,%.html, $(BOOKS))
BOOKS_CLEAN = $(patsubst %,%.clean, $(BOOKS))
BOOKS_MAN   = $(patsubst %,%.man, $(BOOKS))
BOOKS_LATEX = $(patsubst %,%.latex, $(BOOKS))
BOOKS_PDF   = $(patsubst %,%.pdf, $(BOOKS)) $(patsubst %,%.pdf, $(BOOKS_MIGRATED)) $(patsubst %,books/%.pdf, $(KERNEL_BOOKS))

# for the period of transition from books_migrated
BOOKS_MIGRATED_FOLDER=$(BOOKS_FOLDER)/books_migrated
BOOKS_MIGRATED=$(patsubst $(BOOKS_MIGRATED_FOLDER)/%/conf.py,books/%,$(wildcard $(BOOKS_MIGRATED_FOLDER)/*/conf.py))
BOOKS_MIGRATED_HTML  = $(patsubst %,%.html, $(BOOKS_MIGRATED))
BOOKS_MIGRATED_CLEAN = $(patsubst %,%.clean, $(BOOKS_MIGRATED))
BOOKS_MIGRATED_MAN   = $(patsubst %,%.man, $(BOOKS_MIGRATED))
BOOKS_MIGRATED_LATEX = $(patsubst %,%.latex, $(BOOKS_MIGRATED))

# kernel's sphinx-books
KERNEL_FOLDER=$(srctree)/Documentation
KERNEL_BOOKS=$(patsubst $(srctree)/Documentation/%/conf.py,%,$(wildcard $(KERNEL_FOLDER)/*/conf.py))
KERNEL_BOOKS_HTML  = $(patsubst %,books/%.html, $(KERNEL_BOOKS))
KERNEL_BOOKS_CLEAN = $(patsubst %,books/%.clean, $(KERNEL_BOOKS))
KERNEL_BOOKS_MAN   = $(patsubst %,books/%.man, $(KERNEL_BOOKS))
KERNEL_BOOKS_LATEX = $(patsubst %,books/%.latex, $(KERNEL_BOOKS))


FMT = cat
ifeq ($(shell which fmt >/dev/null 2>&1; echo $$?), 0)
FMT = fmt
endif

DOCBOOKS := $(wildcard $(srctree)/Documentation/DocBook/*.tmpl)
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
  manager (pip). On debian based OS these requirements are\n\
  installed by::\n\n\
    sudo apt-get install pip3\n\
    pip3 install --user -U Sphinx sphinx_rtd_theme"

ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
sphinx-builder: msg-sphinx-builder
	$(error The '$(SPHINXBUILD)' command was not found)
else
sphinx-builder:
	@:
endif

PHONY += msg-texlive texlive

ifeq ($(shell which xelatex >/dev/null 2>&1; echo $$?), 1)
texlive: msg-TeXLive
	$(error The 'xelatex' command was not found)
else
texlive:
	@:
endif

msg-TeXLive:
	$(Q)echo "\n\
The TeX and PDF output and the *math* extension require TexLive:\n\n\
  Make sure you have a updated TeXLive with XeTeX engine installed, grab it\n\
  it from https://www.tug.org/texlive or install it from your package manager.\n\n\
  Sphinx-doc produce (Xe)LaTeX files which might use additional TeX-packages\n\
  and fonts. To process these LaTeX files, a TexLive installation with the\n\
  additional packages is required. On debian based OS these requirements\n\
  are installed by::\n\n\
    sudo apt-get install\n\
         texlive-base texlive-xetex texlive-latex-recommended\n\
         texlive-extra-utils dvipng ttf-dejavu\n"

# ------------------------------------------------------------------------------
# usage
# ------------------------------------------------------------------------------

PHONY += help help-rqmts

help-rqmts: msg-sphinx-builder msg-TeXLive

help:
	$(Q)echo "Please use 'make <target>' where <target> is one of ..."
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
	$(Q)echo "    valid values for books/{name}.html are: \n\n    $(BOOKS_HTML) $(BOOKS_MIGRATED_HTML) $(KERNEL_BOOKS_HTML)" | $(FMT)
	$(Q)echo
	$(Q)echo "books.pdf : builds all PDF targets (with the buggy rstpdf):"
	$(Q)echo
	$(Q)echo "  books/{name}.pdf : build only the PDF of document {name}"
	$(Q)echo "    valid values for books/{name}.pdf are: \n\n    $(BOOKS_PDF) " | $(FMT)
	$(Q)echo
	$(Q)echo "books.man : builds all man page targets:"
	$(Q)echo
	$(Q)echo "  books/{name}.man : build only the man page of document {name}"
	$(Q)echo "    valid values for books/{name}.pdf are: \n\n    $(BOOKS_MAN) $(BOOKS_MIGRATED_MAN) $(KERNEL_BOOKS_MAN)" | $(FMT)
	$(Q)echo
	$(Q)echo "The HTML & PDF output formats are placed into folder:"
	$(Q)echo ""
	$(Q)echo "    $(DIST)"
	$(Q)echo ""
	$(Q)echo "all-reST : builds all reST targets:"
	$(Q)echo
	$(Q)echo "  src2rst     : generate reST documentation from source code"
	$(Q)echo "  dbxml2rst   : convert kernel's DocBook-XML books to reST"
	$(Q)echo "  {fname}.rst : converts only {fname}.tmpl to reST, valid"
	$(Q)echo "    values for {fname} are: \n\n    $(DB2RST)" | $(FMT)
	$(Q)echo
	$(Q)echo ".. hint:"
	$(Q)echo
	$(Q)echo "   The reST files are versioned within *this* reposetory."
	$(Q)echo
	$(Q)echo "   Use 'make srctree=<kernel-src>' to point to kernel's"
	$(Q)echo "   sources (default $(srctree))"
	$(Q)echo
	$(Q)echo "   It's recommended to use docs-next from lwn:"
	$(Q)echo "      git git://git.lwn.net/linux.git docs-next"
	$(Q)echo
	$(Q)echo "make V=0|1 [targets] 0 => quiet build (default), 1 => verbose build"
	$(Q)echo "make V=2   [targets] 2 => give reason for rebuild of target"


# ------------------------------------------------------------------------------
# main targets
# ------------------------------------------------------------------------------

ALLSPHINXOPTS = $(SPHINXOPTS)\
	-D latex_paper_size=$(PAPER) -D latex_font_size=$(FONTSIZE)\
	-D version=$(KERNELVERSION) -D release=$(KERNELRELEASE)

# update reST in reposetory
PHONY += all-reST
all-reST: dbxml2rst src2rst

# update github-pages
PHONY += all-HTML books.html books.pdf books.man books.clean
all-HTML:    sphinx-builder books.html src.html
books.html:  sphinx-builder $(BOOKS_HTML) $(BOOKS_MIGRATED_HTML) $(KERNEL_BOOKS_HTML) intro.html
books.man:   sphinx-builder $(BOOKS_MAN) $(BOOKS_MIGRATED_MAN) $(KERNEL_BOOKS_MAN)
books.pdf:   $(BOOKS_PDF) $(BOOKS_MIGRATED_PDF) $(KERNEL_BOOKS_PDF)
books.clean: $(BOOKS_CLEAN) $(BOOKS_MIGRATED_CLEAN) $(KERNEL_BOOKS_CLEAN) intro.clean

PHONY += clean
clean: intro.clean books.clean

$(DIST_BOOKS):
	mkdir -p $(DIST_BOOKS)


# $2 sphinx builder e.g. "html"
# $3 name of the book / e.g. "gpu", used as:
#    * dest folder relative to $(DIST_BOOKS) and
#    * cache folder relative to $(CACHE_BOOKS)
# $4 dest subfolder e.g. "man" for man pages at gpu/man
# $5 reST source folder,
#    e.g. "$(BOOKS_FOLDER)/books_migrated" for the migrated books

quiet_cmd_sphinx = SPHINX  $@ --> file://$(abspath $(DIST_BOOKS)/$3/$4)
      cmd_sphinx = SPHPROJ_CONF=$(abspath $5/$3/conf.py) \
	$(SPHINXBUILD) \
	$(ALLSPHINXOPTS) \
	-b $2 \
	-c $(obj) \
	-d $(CACHE_BOOKS)/$3 \
	$(abspath $5/$3) \
	$(abspath $(DIST_BOOKS)/$3/$4)

# $2 name of the book / e.g. "gpu", used to clean:
#    * dest folder relative to $(DIST_BOOKS) and
#    * cache folder relative to $(CACHE_BOOKS)
quiet_cmd_sphinx_clean = CLEAN   $@
      cmd_sphinx_clean = rm -rf $(CACHE_BOOKS)/$2 $(DIST_BOOKS)/$2

# ------------------------------------------------------------------------------
# BOOKs
# ------------------------------------------------------------------------------
#
# e.g.: make books/template-book.[html|man|latex|pdf|clean]
#
PHONY += $(BOOKS_HTML)
$(BOOKS_HTML): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,html,$(patsubst books/%.html,%,$@),,$(BOOKS_FOLDER))

PHONY += $(BOOKS_MAN)
$(BOOKS_MAN): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,kernel-doc-man,$(patsubst books/%.man,%,$@),man,$(BOOKS_FOLDER))
	$(Q)find $(DIST_BOOKS)/$(patsubst books/%.man,%,$@)/man -name '*.9' -exec gzip -nf {} +

PHONY += $(BOOKS_LATEX)
$(BOOKS_LATEX): sphinx-builder texlive | $(DIST_BOOKS)
	$(call cmd,sphinx,latex,$(patsubst books/%.latex,%,$@),latex,$(BOOKS_FOLDER))

# latex to PDF is for all books the same
PHONY += $(BOOKS_PDF) $(BOOKS_MIGRATED_PDF) $(KERNEL_BOOKS_PDF)
$(BOOKS_PDF) $(BOOKS_MIGRATED_PDF) $(KERNEL_BOOKS_PDF): %.pdf : %.latex
	$(MAKE) PDFLATEX=xelatex -C $(DIST_BOOKS)/$(patsubst books/%.pdf,%,$@)/latex

# clean is for all books the same
PHONY += $(BOOKS_CLEAN) $(BOOKS_MIGRATED_CLEAN) $(KERNEL_BOOKS_CLEAN)
$(BOOKS_CLEAN) $(BOOKS_MIGRATED_CLEAN) $(KERNEL_BOOKS_CLEAN):
	$(call cmd,sphinx_clean,$(patsubst books/%.clean,%,$@))

# migrated DocBook-XML to reST content
# ------------------------------------
#
# e.g: make books/debugobjects.[html|man|latex|pdf|clean]
#

PHONY += $(BOOKS_MIGRATED_HTML)
$(BOOKS_MIGRATED_HTML): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,html,$(patsubst books/%.html,%,$@),,$(BOOKS_MIGRATED_FOLDER))

PHONY += $(BOOKS_MIGRATED_MAN)
$(BOOKS_MIGRATED_MAN): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,kernel-doc-man,$(patsubst books/%.man,%,$@),man,$(BOOKS_MIGRATED_FOLDER))
	$(Q)find $(DIST_BOOKS)/$(patsubst books/%.man,%,$@)/man -name '*.9' -exec gzip -nf {} +

PHONY += $(BOOKS_MIGRATED_LATEX)
$(BOOKS_MIGRATED_LATEX): sphinx-builder texlive | $(DIST_BOOKS)
	$(call cmd,sphinx,latex,$(patsubst books/%.latex,%,$@),latex,$(BOOKS_MIGRATED_FOLDER))


# kernel's sphinx-books
# ------------------------------------
#
# e.g: make books/gpu.[html|man|latex|pdf|clean]
#

PHONY += $(KERNEL_BOOKS_HTML)
$(KERNEL_BOOKS_HTML): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,html,$(patsubst books/%.html,%,$@),,$(KERNEL_FOLDER))

PHONY += $(KERNEL_BOOKS_MAN)
$(KERNEL_BOOKS_MAN): sphinx-builder | $(DIST_BOOKS)
	$(call cmd,sphinx,kernel-doc-man,$(patsubst books/%.man,%,$@),man,$(KERNEL_FOLDER))
	$(Q)find $(DIST_BOOKS)/$(patsubst books/%.man,%,$@)/man -name '*.9' -exec gzip -nf {} +

PHONY += $(KERNEL_BOOKS_LATEX)
$(KERNEL_BOOKS_LATEX): sphinx-builder texlive | $(DIST_BOOKS)
	$(call cmd,sphinx,latex,$(patsubst books/%.latex,%,$@),latex,$(KERNEL_FOLDER))

# ------------------------------------------------------------------------------
# intro page
# ------------------------------------------------------------------------------

INDEX_CACHE    = $(CACHE)/index-page

quiet_cmd_intro_clean = CLEAN   $@
      cmd_intro_clean = \
	rm -rf $(INDEX_CACHE);\
	rm -rf $(DIST)/.buildinfo $(filter-out $(DIST)/books $(DIST)/.git $(DIST)/.gitignore $(DIST)/linux_src_doc,$(wildcard $(DIST)/*))

quiet_cmd_intro = SPHINX  $@ --> file://$(abspath $(DIST))/index.html
      cmd_intro = SPHPROJ_CONF=$(abspath $(BOOKS_FOLDER)/intro/conf.py) \
	$(SPHINXBUILD) \
	$(ALLSPHINXOPTS) \
	-b html \
	-c $(obj) \
	-d $(INDEX_CACHE) \
	$(abspath $(obj)/intro) \
	$(abspath $(DIST))

PHONY += intro.html intro.clean
intro.html: sphinx-builder | $(DIST_BOOKS)
	$(call cmd,intro,html,../,,$(BOOKS_FOLDER))

intro.clean:
	$(call cmd,intro_clean)

# DocBook-XML (tmpl) --> reST
# ---------------------------

DB2RST := $(patsubst %.tmpl,%.rst,$(DOCBOOKS))
dbxml2rst: dbxml2rst.clean $(DB2RST) dbxml2rst.post

dbxml2rst.clean:
	rm -f $(BOOKS_MIGRATED_FOLDER)/*/*.rst

dbxml2rst.post:
	$(Q)echo
	$(Q)echo "CHECK IF SOME OF THE $(BOOKS_MIGRATED_FOLDER)/*/conf.py ARE OBSOLETE!"
	$(Q)echo "IF SO, DROP THOSE FOLDERS."
	$(Q)echo

.PHONY:	$(DB2RST)
$(DB2RST):
	$(DBTOOLS_SCRIPT) --out=$(BOOKS_MIGRATED_FOLDER) db2rst $(srctree) $(patsubst %.rst,%.tmpl,${@})


# ------------------------------------------------------------------------------
# source-code
# ------------------------------------------------------------------------------

# autodoc reST
# ------------

PHONY += src-reST-Files
src-reST-Files:
	kernel-docgrep $(srctree) > src-reST-Files.txt

PHONY += src2rst
src2rst: src-reST-Files
	rm -rf $(AUTODOC_FOLDER)
	$(AUTODOC_SCRIPT)  --markup kernel-doc --rst-files src-reST-Files.txt $(srctree) $(AUTODOC_FOLDER)

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
