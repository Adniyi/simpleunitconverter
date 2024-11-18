# Simple Unit Converter 
An application for converting between different unit of measurements.

## Overview
A simple converter program that convertes between one unit of measurement to another. The application makes use of forms to recieve the input from the user, send it o the server for conversion, and then the server returns a response o the calculated answer.

## How it works 
The application is written in Python using the Flask framework. 
Currently it can only convert units of Length and Weight. 
It works by recieving the units of either Length or Weight and passes them into a function that does the conversion and returns the value which is then sent to the browser.

## More Details
### The Units in Lenghts include:  
1. Centimeter to Meter
2. Meter to Centimeter
3. Milimeter to Centimeter 
4. Centimeter to Milimeter
5. Meter to Kilometer
6. Kilometer to Meter
7. Kilometer to Mile
8. Mile to Kilometer

### The Units in Weights include: 
1. Miligram to Gram
2. Gram to Miligram
3. Gram to Kilogram 
4. Kilogram to Gram 
5. Kilogram to Pound
6. Pound to Kilogram

## Conclusion 
This is a simple application that i look to improve on in the future (Not anytime soon though). For the conversion, functions declared in different python files are imported into the main app file and then used there. 
https://roadmap.sh/projects/unit-converter
