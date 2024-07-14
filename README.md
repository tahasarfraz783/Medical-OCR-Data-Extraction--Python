# Medical OCR Data Extraction -- Python

I have worked on this project as part of the [CodeBasics Python Course](https://codebasics.io/courses/python-for-beginner-and-intermediate-learners)

## Problem Statement

Stark Insurance has outsourced AtliQ Data Systems to extract data from medical documents received by them through hospitals and customers. AtliQ Extract Pro is a software built by AtliQ Data Systems, which shows an image of the medical documents and requires the employees to fill out the required information by looking at the image. This process is very inefficient as its manual, leads to a lot of delays, and is error-prone. This has led to complaints from Stark Insurances since the process takes a lot of time especially when the number of documents received is high. To counter this problem, AtliQ Data Systems have decided to upgrade their software by implementing a new feature.

## Solution Approach

The new feature will read and extract key data from the medical documents automatically. Still there may be a few errors here and there, so the employers will now check the extracted and correct it if needed. But the overall work done by each employee will be reduced greatly.

We'll be using the Python programming language and its various libraries to implement the solution. Test Driven Development was used to write this code. The code and outputs were checked using the Pytest module during development


## Steps in Implementing the Feature
- Converting PDF to Image
- Pre-Processing Images
- Saving Text from Images
- Extracting Data from Text
- Front-End Implementation


<img src = "https://github.com/tahasarfraz783/Medical-OCR-Data-Extraction--Python/blob/main/extras/solution_process.png" class = "center">


## Converting PDF to Image  
We use the pdf2image library to convert the sent pdf files in to png format.

## Pre-Processing Images  
The OpenCV library allowed us to use adaptive thresholding on each of the images. This is a required step to make sure the colors are consistent all across the page, making it easier to read.

## Saving Text from Images
We use the pytesseract library to read the data from the processed images

## Extracting Data from Text
By using Regular Expressions (regex) we can extract the required data from the text. Since the format for each type of file will be different, we will use different regex code to extract data for each of the document types. Then we can use Classes and Methods for each document type to store the data in a dictionary.

## Front-End Implementation
FastAPI is used to host the server for the project, and for now Postman is being used as the frontend and to see how server responds to requests.


# Conclusion
This new feature was implemented into the AtliQ Extract Pro software, and the few errors in extracting the data will be corrected by the employees. Despite these errors, this new feature can help save each employee upto 30 seconds for extracting data from each document. This combination of automated and manual work will greatly increase the efficiency of the project, reducing the costs, delays, and errors overall.
