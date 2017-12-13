# Barcode Generator

Generates inventory barcodes for sticking on kits.

You will first need to run `git submodule update --init` to fetch the dependency (the `art` repository).

either run the script directly by passing in the codes as a parameter:

` python3 barcode-gen.py 00-00-00-00 00-00-00-01 `

or by putting them into the `codes` file (one line per code) and calling `make`

