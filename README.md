# Barcode_Scanner

## Overview
I found a dusty old barcode scanner (Symbol DS6878) with a serial cable but it turns out support was discontinued, and there's no software available to make it useful. Luckily, all it took was a little bit of Python magic to translate barcode text into keyboard inputs!

## Software
- PySerial: For reading and decoding barcodes into strings
- Pynput: To simulate keypresses
