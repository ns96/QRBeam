# QRBeam
Basic Web App for transferring data through QR Codes

## Introduction
This web application leverages the camera capabilities of smartphones to decode data from QR Codes. The user inputs the data (text, numbers, etc.) into the [HTML form](https://ns96.github.io/QRBeam/index.html), then it dynamically generates a series of QR Codes, each containing a portion of the data and an index to aid in reassembling the data. Through the use of their smartphone and companion [decoding web app](https://ns96.github.io/QRBeam/qrscan.html), users can scan these QR Codes and retrieve the original data. This method allows for offline data transfer between devices without requiring internet connectivity or the use of removable storage like USB drives.

## Installation and Usage
Download the latest release, then unzip on a computer with data to be transferred. Next, open the QRBeam-nnn folder, then double-click on the index.html file. This will open the page which allows for encoding data, as well as provide a QR code which links to the companion decoding web page to be opened on the smartphone.

## Acknowledgements
This app would not be possible without the use of the excellent JavaScript libraries for processing QR Codes:
* [QRCode.js](https://github.com/davidshimjs/qrcodejs)
* [jsQR](https://github.com/cozmo/jsQR)