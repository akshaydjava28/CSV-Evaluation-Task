# CSV Evaluation Task

This Node.js program parses a CSV file containing algebraic expressions, evaluates them, and outputs the results into another CSV file.

## Dependencies

This program relies on the following npm packages:
- `csv-parser`: To parse CSV files
- `csv-writer`: To write data to CSV files

Before running the program, I have Node.js installed on System. I can download it from [the official Node.js website](https://nodejs.org/).

## Installation

To install the required dependencies, navigate to the project directory in your terminal and run the following command:

npm install csv-parser csv-writer


## Usage

To run the program, follow these steps:

1. Place input CSV file in the project directory. Ensure that it follows the format specified in the task description.

2. Modify the Node.js script to use input CSV file. Update the input file path accordingly:

```javascript
evaluateCSV('input.csv', 'output.csv');
Open your terminal and navigate to the project directory.

Run the program using the following command:

node app.js