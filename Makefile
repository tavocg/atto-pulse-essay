all: report.pdf slides.pdf

report.pdf: doc/report.tex
	tectonic -o . doc/report.tex

slides.pdf: doc/slides.tex
	tectonic -o . doc/slides.tex

init:
	sh ./scripts/download_res.sh
