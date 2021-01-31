# Twitter Intent Generator

## Requirements

    pip install -r requirements.txt

## Install

    git clone https://github.com/alicanyuksel/twitter-intent-generator.git

## To run

You need 3 args to run:

- --input_txt -> Input **TXT** file path containing the tweets
- --output_txt -> Output **TXT** file path
- --output_pdf -> Output **PDF** file path

<!-- well hey this is a separetor :) -->

    python generator.py --input_txt [INPUT/TXT/PATH] --output_txt [OUTPUT/TXT/PATH] --output_pdf [OUTPUT/PDF/PATH]


## Input example

You must prepare a **TXT** file which will contain your tweets inserted between **```<tweet></tweet>```** tags


    <tweet>This is a tweet!</tweet>


**or**


    <tweet>
    This is a tweet!
    </tweet>

## What's the point ?

For example, you could generate your urls via our script and use them to do a **selenium bot** to post your tweets.

or

You could create a PDF file and click directly on it to post your tweets manually.
