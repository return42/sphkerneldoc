# -*- coding: utf-8; mode: make -*-

include utils/makefile.include
include utils/makefile.python
include utils/makefile.sphinx

# sphinx-build setup
SPHINXOPTS =
# The paper size ('letter' or 'a4').
PAPER     := a4
# The font size ('10pt', '11pt' or '12pt')
FONTSIZE  := 11
# The LaTeX docclass
# this HACK disables the *docclass* setting in the latex_documents (see conf.py)
#export DOCCLASS  := darmarITArticle
export DOCCLASS  := manual

srctree=/share/linux-docs-next
export srctree

# External programs used

SPHINXBUILD    := $(PY_ENV_BIN)/sphinx-build
AUTODOC_SCRIPT := $(PY_ENV_BIN)/kernel-autodoc


PHONY =

objtree = .
obj = .
Q = @

DOCUTILSCONFIG=$(objtree)/docutils.conf:
export DOCUTILSCONFIG

KERNELVERSION := $(shell make -C $(srctree) kernelversion | grep "^[0-9]")

ifndef $(KERNELRELEASE)
  KERNELRELEASE = $(KERNELVERSION)
endif

CACHE          := $(abspath $(objtree)/cache)
AUTODOC_FOLDER := $(abspath $(objtree)/linux_src_doc)
DIST           := $(abspath $(objtree)/dist)

DIST_BOOKS  = $(DIST)/books
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

# FIXME: kernel-doc-HOWTO.pdf not yet work
BOOKS_PDF   = $(patsubst %,%.pdf, $(filter-out books/kernel-doc-HOWTO, $(BOOKS)))\
	      $(patsubst %,%.pdf, $(BOOKS_MIGRATED))\
	      $(patsubst %,books/%.pdf, $(KERNEL_BOOKS))


# kernel's sphinx-books
KERNEL_FOLDER=$(srctree)/Documentation
# FIXME: media not yet work
KERNEL_BOOKS=$(filter-out media,$(patsubst $(srctree)/Documentation/%/conf.py,%,$(wildcard $(KERNEL_FOLDER)/*/conf.py)))
KERNEL_BOOKS_HTML  = $(patsubst %,books/%.html, $(KERNEL_BOOKS))
KERNEL_BOOKS_CLEAN = $(patsubst %,books/%.clean, $(KERNEL_BOOKS))
KERNEL_BOOKS_MAN   = $(patsubst %,books/%.man, $(KERNEL_BOOKS))
KERNEL_BOOKS_LATEX = $(patsubst %,books/%.latex, $(KERNEL_BOOKS))


FMT = cat
ifeq ($(shell which fmt >/dev/null 2>&1; echo $$?), 0)
FMT = fmt
endif

# ------------------------------------------------------------------------------
# requirements
# ------------------------------------------------------------------------------

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
The TeX/PDF output and the *math* extension require TexLive:\n\n\
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

.DEFAULT_GOAL=help

PHONY += help help-rqmts

help-rqmts: msg-TeXLive

help:
	$(Q)echo "Please use 'make <target>' where <target> is one of ..."
	$(Q)echo
	$(Q)echo "all-HTML : build all HTML targets:"
	$(Q)echo
	$(Q)echo "  intro.html    : build HTML intro page (root index.html)"
	$(Q)echo "  src.html      : build HTML of source-code reST files (see src2rst)"
	$(Q)echo
	$(Q)echo "help-rqmts : info about build requirements"
	$(Q)echo
	$(Q)echo "books/{name}.html : build only the HTML of document {name}"
	$(Q)echo "    valid values for books/{name}.html are: \n\n    $(BOOKS_HTML) $(KERNEL_BOOKS_HTML)" | $(FMT)
	$(Q)echo
	$(Q)echo "books.pdf : builds all PDF targets:"
	$(Q)echo
	$(Q)echo "  books/{name}.pdf : build only the PDF of document {name}"
	$(Q)echo "    valid values for books/{name}.pdf are: \n\n    $(BOOKS_PDF) " | $(FMT)
	$(Q)echo
	$(Q)echo "books.man : builds all man page targets:"
	$(Q)echo
	$(Q)echo "  books/{name}.man : build only the man page of document {name}"
	$(Q)echo "    valid values for books/{name}.pdf are: \n\n    $(BOOKS_MAN) $(KERNEL_BOOKS_MAN)" | $(FMT)
	$(Q)echo
	$(Q)echo "The HTML & PDF output formats are placed into folder:"
	$(Q)echo ""
	$(Q)echo "    $(DIST)"
	$(Q)echo ""
	$(Q)echo "all-reST : builds all reST targets:"
	$(Q)echo
	$(Q)echo "  src2rst     : generate reST documentation from source code"
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
	-D version=$(KERNELVERSION) -D release=$(KERNELRELEASE)

# update reST in reposetory
PHONY += all-reST
all-reST: src2rst

# update github-pages
PHONY += all-HTML books.html books.pdf books.man books.clean
all-HTML:    sphinx-doc books.html src.html
books.html:  sphinx-doc $(BOOKS_HTML) $(KERNEL_BOOKS_HTML) intro.html
books.man:   sphinx-doc $(BOOKS_MAN)  $(KERNEL_BOOKS_MAN)
books.pdf:   $(BOOKS_PDF) $(KERNEL_BOOKS_PDF)
books.clean: $(BOOKS_CLEAN) $(KERNEL_BOOKS_CLEAN) intro.clean

PHONY += clean
clean: intro.clean books.clean pyclean

$(DIST_BOOKS):
	mkdir -p $(DIST_BOOKS)


# $2 sphinx builder e.g. "html"
# $3 name of the book / e.g. "gpu", used as:
#    * dest folder relative to $(DIST_BOOKS) and
#    * cache folder relative to $(CACHE_BOOKS)
# $4 dest subfolder e.g. "man" for man pages at gpu/man
# $5 reST source folder,
#    e.g. "$(BOOKS_MIGRATED_FOLDER)" for the migrated books

quiet_cmd_sphinx = $(shell echo "$2" | tr '[:lower:]' '[:upper:]')  $@ --> file://$(abspath $(DIST_BOOKS)/$3/$4)
      cmd_sphinx = SPHINX_CONF=$(abspath $5/$3/conf.py) \
	$(SPHINXBUILD) \
	$(ALLSPHINXOPTS) \
	-b $2 \
	-c $(obj) \
	-d $(CACHE_BOOKS)/$3 \
	$(abspath $5/$3) \
	$(abspath $(DIST_BOOKS)/$3/$4)

# $2 name of the book / e.g. "gpu", used as:
#    * cache folder relative to $(CACHE_BOOKS)
#    * dest subfolder relative to $(CACHE_BOOKS)
# $3 reST source folder,
#    e.g. "$(BOOKS_MIGRATED_FOLDER)" for the migrated books

quiet_cmd_latex = LATEX   $@ --> file://$(abspath $(CACHE_BOOKS)/$2/latex)
      cmd_latex = SPHINX_CONF=$(abspath $3/$2/conf.py) PAPER=$(PAPER) FONTSIZE=$(FONTSIZE) \
	$(SPHINXBUILD) \
	$(ALLSPHINXOPTS) \
	-b latex \
	-c $(obj) \
	-d $(CACHE_BOOKS)/$2 \
	$(abspath $3/$2) \
	$(abspath $(CACHE_BOOKS)/$2/latex)


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
$(BOOKS_HTML): sphinx-doc | $(DIST_BOOKS)
	$(call cmd,sphinx,html,$(patsubst books/%.html,%,$@),,$(BOOKS_FOLDER))

PHONY += $(BOOKS_MAN)
$(BOOKS_MAN): sphinx-doc | $(DIST_BOOKS)
	$(call cmd,sphinx,kernel-doc-man,$(patsubst books/%.man,%,$@),man,$(BOOKS_FOLDER))
	$(Q)find $(DIST_BOOKS)/$(patsubst books/%.man,%,$@)/man -name '*.9' -exec gzip -nf {} +

PHONY += $(BOOKS_LATEX)
$(BOOKS_LATEX): sphinx-doc texlive | $(DIST_BOOKS)
	$(call cmd,latex,$(patsubst books/%.latex,%,$@),$(BOOKS_FOLDER))

# latex to PDF is for all books the same
PHONY += $(BOOKS_PDF) $(KERNEL_BOOKS_PDF)
$(BOOKS_PDF) $(KERNEL_BOOKS_PDF): %.pdf : %.latex
	$(Q) DIST_BOOKS=$(DIST_BOOKS)/$(patsubst books/%.pdf,%,$@)/pdf/ \
		$(MAKE) -C $(CACHE_BOOKS)/$(patsubst books/%.pdf,%,$@)/latex all-pdf dist-pdf

# clean is for all books the same
PHONY += $(BOOKS_CLEAN) $(KERNEL_BOOKS_CLEAN)
$(BOOKS_CLEAN) $(KERNEL_BOOKS_CLEAN):
	$(call cmd,sphinx_clean,$(patsubst books/%.clean,%,$@))


# kernel's sphinx-books
# ------------------------------------
#
# e.g: make books/gpu.[html|man|latex|pdf|clean]
#

PHONY += $(KERNEL_BOOKS_HTML)
$(KERNEL_BOOKS_HTML): sphinx-doc | $(DIST_BOOKS)
	$(call cmd,sphinx,html,$(patsubst books/%.html,%,$@),,$(KERNEL_FOLDER))

PHONY += $(KERNEL_BOOKS_MAN)
$(KERNEL_BOOKS_MAN): sphinx-doc | $(DIST_BOOKS)
	$(call cmd,sphinx,kernel-doc-man,$(patsubst books/%.man,%,$@),man,$(KERNEL_FOLDER))
	$(Q)find $(DIST_BOOKS)/$(patsubst books/%.man,%,$@)/man -name '*.9' -exec gzip -nf {} +

PHONY += $(KERNEL_BOOKS_LATEX)
$(KERNEL_BOOKS_LATEX): sphinx-doc texlive | $(DIST_BOOKS)
	$(call cmd,latex,$(patsubst books/%.latex,%,$@),$(KERNEL_FOLDER))

# ------------------------------------------------------------------------------
# intro page
# ------------------------------------------------------------------------------

INDEX_CACHE    = $(CACHE)/index-page

quiet_cmd_intro_clean = CLEAN   $@
      cmd_intro_clean = \
	rm -rf $(INDEX_CACHE);\
	rm -rf $(DIST)/.buildinfo   $(DIST)/genindex.html $(DIST)/index.html\
		$(DIST)/objects.inv $(DIST)/search.html   $(DIST)/searchindex.js \
		$(DIST)/_sources $(DIST)/_static \
		$(DIST)/docs.html\
		$(DIST)/reST-nano-HOWTO.html \
		$(DIST)/poc_sphkerneldoc

quiet_cmd_intro = SPHINX  $@ --> file://$(abspath $(DIST))/index.html
      cmd_intro = SPHINX_CONF=$(abspath $(obj)/intro/conf.py) \
	$(SPHINXBUILD) \
	$(ALLSPHINXOPTS) \
	-b html \
	-c $(obj) \
	-d $(INDEX_CACHE) \
	$(abspath $(obj)/intro) \
	$(abspath $(DIST))

PHONY += intro.html intro.clean
intro.html: sphinx-doc | $(DIST_BOOKS)
	$(call cmd,intro,html,../,,$(BOOKS_FOLDER))

intro.clean:
	$(call cmd,intro_clean)



# ------------------------------------------------------------------------------
# source-code
# ------------------------------------------------------------------------------

# autodoc reST
# ------------

PHONY += src-reST-Files
src-reST-Files: $(PY_ENV)
	$(PY_ENV_BIN)/$(PYTHON) ./kernel-docgrep $(KERNEL_FOLDER) > $(CACHE)/src-reST-Files.txt

PHONY += src2rst
src2rst: $(PY_ENV) src-reST-Files
	rm -rf $(AUTODOC_FOLDER)
	$(AUTODOC_SCRIPT)  --markup kernel-doc --rst-files $(CACHE)/src-reST-Files.txt $(srctree) $(AUTODOC_FOLDER)

# reST --> HTML
# -------------

PHONY += src.html
src.html: sphinx-doc
	$(SPHINXBUILD) $(ALLSPHINXOPTS) -b html\
		-c .\
		-d $(CACHE)/doctrees/linux_src_doc \
		$(AUTODOC_FOLDER) \
		$(DIST)/linux_src_doc

PHONY += src.clean
src.clean:
	rm -rf $(CACHE)/doctrees/linux_src_doc $(DIST)/linux_src_doc

# release on https://h2626237.stratoserver.net/kernel/
#www: clean all-reST all-HTML books.man books.pdf
www:
	rsync -a $(DIST)/ /var/www/kernel

# Declare the contents of the .PHONY variable as phony.  We keep that
# information in a variable se we can use it in if_changed and friends.

.PHONY: $(PHONY)
