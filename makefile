#FMT=jpg
#FMT=png
FMT=gif
DELAY=150

INS=$(wildcard *.dot)
OUTS=$(INS:.dot=.${FMT})

all: anim.gif

%.${FMT}: %.dot
	dot -Tjpg $< | convert - $@

anim.gif: $(OUTS) makefile
	convert -delay ${DELAY} -loop 0 $(OUTS) - > anim.gif

clean:
	rm -rf *.gif *.jpg *.png
