# -*- coding: utf-8; mode: make -*-

# Additional LaTeX options
LATEXOPTS = -interaction=nonstopmode -file-line-error
LATEX_ENV = max_print_line=240

ALLDOCS   = $(basename $(wildcard *.tex))
ALLPDF    = $(addsuffix .pdf,$(ALLDOCS))

PDFLATEX  = $(LATEX_ENV) xelatex
MAKEINDEX = $(LATEX_ENV) makeindex

all: $(ALLPDF)

all-pdf: $(ALLPDF)

dist-pdf:
	@echo "  PDF    $@ --> file://$(abspath $(DIST_BOOKS))"
	@mkdir -p $(DIST_BOOKS)
	@cp $(ALLPDF) $(DIST_BOOKS)

all-dvi: $(ALLDVI)

all-ps: all-dvi
	for f in *.dvi; do dvips $$f; done

# all-pdf-ja:
# 	for f in *.pdf *.png *.gif *.jpg *.jpeg; do extractbb $$f; done
# 	for f in *.tex; do platex -kanji=utf8 $(LATEXOPTS) $$f; done
# 	for f in *.tex; do platex -kanji=utf8 $(LATEXOPTS) $$f; done
# 	for f in *.tex; do platex -kanji=utf8 $(LATEXOPTS) $$f; done
# 	-for f in *.idx; do mendex -U -f -d "`basename $$f .idx`.dic" -s python.ist $$f; done
# 	for f in *.tex; do platex -kanji=utf8 $(LATEXOPTS) $$f; done
# 	for f in *.tex; do platex -kanji=utf8 $(LATEXOPTS) $$f; done
# 	for f in *.dvi; do dvipdfmx $$f; done

# The number of LaTeX runs is quite conservative, but I don't expect it
# to get run often, so the little extra time won't hurt.

%.pdf: %.tex
	$(PDFLATEX) $(LATEXOPTS) '$<'
	@$(PDFLATEX) $(LATEXOPTS) '$<'
	@$(PDFLATEX) $(LATEXOPTS) '$<'
	-$(MAKEINDEX) -s python.ist '$(basename $<).idx'
	@$(PDFLATEX) $(LATEXOPTS) '$<'
	@$(PDFLATEX) $(LATEXOPTS) '$<'

clean:
	rm -f *.log *.ind *.aux *.toc *.syn *.idx *.out *.ilg *.pla *.ps $(ALLPDF)

.PHONY: all all-pdf all-dvi all-ps clean
# .PHONY: all-pdf-ja

