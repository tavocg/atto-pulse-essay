FIGURES = res/figures/time_scales.png res/figures/hhg_three_step.png res/figures/research_flow.png

all: report.pdf slides.pdf

$(FIGURES) &: scripts/generate_figures.py
	MPLCONFIGDIR=/tmp/matplotlib python scripts/generate_figures.py

figures: $(FIGURES)

report.pdf: doc/report.tex $(FIGURES)
	tectonic -o . doc/report.tex

slides.pdf: doc/slides.tex $(FIGURES)
	tectonic -o . doc/slides.tex

init:
	sh ./scripts/download_res.sh
