objects = $(wildcard *.in)
outputs := $(objects:.in=.txt)

.PHONY: all
all: $(outputs)

%.txt: %.in
	pip-compile -v --output-file $@ $<

# Dependency chain
test.txt: base.txt
production.txt: base.txt
dev.txt: test.txt