printer_model = QL-570
label_size = 29x90

.PHONY: clean print

all: clean build

clean:
	rm -rf *.svg *.png

build:
	python barcode-gen.py `cat codes`
	for i in *.svg; do\
	 inkscape $$i --export-png "$${i%.*}.png" --export-width=991 --export-height=306;\
	done

print:
	# Print using a brother QL-570 on the 29x90.3mm labels
	for i in *.png; do\
         brother_ql_create --model $(printer_model) --label-size=$(label_size) "$$i" > /dev/usb/lp1;\
        done


