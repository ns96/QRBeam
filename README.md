# QRBeam
Basic Web App For Transferring Small Data Sets Through QR Codes

## Introduction
This web application leverages the camera capabilities of smartphones to decode data from QR Codes. The user inputs the data (text, numbers, etc.) into the [HTML form](https://ns96.github.io/QRBeam/index.html), then it dynamically generates a series of QR Codes, each containing a portion of the data and an index to aid in reassembling the data. Through the use of their smartphone and companion [decoding web page](https://ns96.github.io/QRBeam/qrscan.html), users can scan these QR Codes and retrieve the original data. There is also a [web page](https://ns96.github.io/QRBeam/reduce.html) which can be used to reduce the number of rows of data by averaging, and precision to reduce the size of the data to be transfered. This method allows for offline data transfer between devices without requiring internet connectivity or the use of removable storage like USB drives.

## Installation and Usage
Download the [latest release](https://github.com/ns96/QRBeam/releases), then unzip QRBeam.zip on a computer with data to be transferred. Next, open the QRBeam folder, then double-click on the index.html file. This will open the page which allows for encoding data, as well as provide a QR code which links to the companion decoding web page to be opened on the smartphone.

## Known Issues
On iPhones, the decoding web page may not work correctly with the camera not loading into page. The page does load correctly on an iPad though.

## Acknowledgements
This app would not be possible without the use of the excellent JavaScript libraries for processing QR Codes, and ofcourse various LLM coding models use for code generation.

* [QRCode.js](https://github.com/davidshimjs/qrcodejs)
* [jsQR](https://github.com/cozmo/jsQR)