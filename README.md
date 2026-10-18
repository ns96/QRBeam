# QRBeam
Basic Web App For Transferring Small Data Sets Through QR Codes

## Introduction
This web application leverages the camera capabilities of smartphones to decode data from QR Codes. The user inputs the data (text, numbers, etc.) into the [HTML form](https://ns96.github.io/QRBeam/index.html), then it dynamically generates a series of QR Codes, each containing a portion of the data and an index to aid in reassembling the data. Through the use of their smartphone and companion [decoding web page](https://ns96.github.io/QRBeam/qrscan.html), users can scan these QR Codes and retrieve the original data. There is also a [web page](https://ns96.github.io/QRBeam/reduce.html) which can be used to reduce the number of rows of data by averaging, and precision to reduce the size of the data to be transfered; it accepts pasted data or can open a CSV/TSV file directly, and can save the reduced result as a CSV or TSV file. This method allows for offline data transfer between devices without requiring internet connectivity or the use of removable storage like USB drives.

## Features

Current version: **v2.2.0 (10/18/2026)**

### Data Sender ([index.html](https://ns96.github.io/QRBeam/index.html))

* Paste or type data into the text area, then press **Generate QR Codes** to split it into a series of QR Codes, each carrying a portion of the data plus an index for reassembly.
* **Open CSV/TSV File** loads a `.csv` or `.tsv` file from the computer straight into the text area, ready for encoding.
* **Play QR** opens a dialog that flashes the generated QR Codes one at a time, so the phone can be held in one fixed position instead of panning across a page of codes.
  * The dialog opens paused on the first QR Code so the phone can be aligned before playback begins.
  * **Start**, **Pause**, **Back**, and **Close** control the sequence; playback loops after the last code.
  * Playback speed can be set to **0.1 s**, **0.25 s**, **0.5 s**, or **1 s** per QR Code, and changed while playing. Slower speeds are more reliable for older phone cameras.
* **Data Reduce** opens a dialog that shrinks numeric CSV/TSV data before encoding, using the same averaging and decimal rounding as the standalone reducer: choose how many rows to average together (use `1` to only round) and how many decimal places to keep. A **Revert** button restores the data to its original state, and the snapshot is dropped whenever the data is edited, cleared, or reloaded.

### Data Scanner ([qrscan.html](https://ns96.github.io/QRBeam/qrscan.html))

* Scans QR Codes with the phone camera and reassembles the original data in the text area.
* Validates the sequence number of every code, highlighting each read in the camera overlay: green for accepted, yellow for a code that was already scanned, and red for an out-of-sequence or non-QRBeam code.
* **Stop Camera** / **Start Camera** releases and re-acquires the camera without reloading the page, and camera permission problems are reported on the page instead of only in the console.
* Audio confirmation for each accepted code; the scanned data can be copied to the clipboard, saved to a file, or plotted (XY, XYY, or bar chart).

## Installation and Usage
Download the [latest release](https://github.com/ns96/QRBeam/releases), then unzip QRBeam.zip on a computer with data to be transferred. Next, open the QRBeam folder, then double-click on the index.html file. This will open the page which allows for encoding data, as well as provide a QR code which links to the companion decoding web page to be opened on the smartphone.

Once the page is open, type or paste the data into the text area (or use **Open CSV/TSV File** to load a file), optionally use **Data Reduce** to average rows or trim decimal places, press **Generate QR Codes**, and then either scan the codes from the screen or press **Play QR** to display them one at a time in a dialog while the phone stays in a fixed position. The decoding page must be served over HTTPS or localhost for the phone to grant camera access; the hosted copy at [qrscan.html](https://ns96.github.io/QRBeam/qrscan.html) already is.

## Known Issues
On iPhones, the decoding web page may not work correctly with the camera not loading into page. The page does load correctly on an iPad though.

## Acknowledgements
This app would not be possible without the use of the excellent JavaScript libraries for processing QR Codes, and ofcourse various LLM coding models use for code generation.

* [QRCode.js](https://github.com/davidshimjs/qrcodejs)
* [jsQR](https://github.com/cozmo/jsQR)