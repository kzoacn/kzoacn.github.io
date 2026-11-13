.PHONY: all pdf package clean

all: package

pdf:
	cd latex && latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build cv-en.tex cv-zh.tex
	cp latex/build/cv-en.pdf cv-en.pdf
	cp latex/build/cv-zh.pdf cv-zh.pdf

package: pdf
	python3 package.py

clean:
	cd latex && latexmk -C -outdir=build cv-en.tex cv-zh.tex
