all: report.pdf slides.pdf

report.pdf:
	tectonic doc/report.tex .

slides.pdf:
	tectonic doc/slides.tex .

init:
	sh ./scripts/download_res.sh
