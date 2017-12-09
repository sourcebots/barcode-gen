.PHONY: clean

all: clean build

clean:
		rm -f *.svg *.png

build:
	python barcode-gen.py
	for i in *.svg; do\
	 inkscape $$i --export-png "$${i%.*}.png" --export-width=991 --export-height=306;\
	done
