CFLAGS = -Wall -std=gnu99
CFLAGS += `gsl-config --cflags`
LDLIBS += `gsl-config --libs`

default: Rabi.pdf

Rabi.pdf: Rabi.tex  
	pdflatex $<
	pdflatex $< 



clean: ; $(RM) $(PLOTS)   Rabi.aux Rabi.log Rabi.pdf

