filename:=ellipsoid
all: compile clean

compile:
	@rm -f *.aux *.bbl *.blg *.idx *.ind *.lof *.lot *.out *.toc *.acn *.acr *.alg *.glg *.glo *.gls *.ist *.fls *.log *.fdb_latexmk *.nlo *.ilg *.nls *.nlg *.bcf *.lol *.run.xml *.synctex.gz *.log *.ptc *.glsdefs main-blx.bib
	@find . -type f -name '*.aux' -delete
	@echo "compiling document..."
	pdflatex $(filename).tex
	pdf2svg $(filename).pdf $(filename).svg

clean:
	@echo -n "removing auxiliaries files...\n"
	@rm -f .log *.aux *.bbl *.blg *.idx *.ind *.lof *.lot *.out *.toc *.acn *.acr *.alg *.glg *.glo *.gls *.ist *.fls *.log *.fdb_latexmk *.nlo *.ilg *.nls *.nlg *.bcf *.lol *.run.xml *.synctex.gz *.log *.ptc *.glsdefs main-blx.bib
	@find . -type f -name '*.aux' -delete
