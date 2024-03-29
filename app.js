const fs = require('fs');
const csv = require('csv-parser');
const { createObjectCsvWriter } = require('csv-writer');
const math = require('mathjs');

const inputFile = 'input.csv';
const outputFile = 'output.csv';

const results = [];

fs.createReadStream(inputFile)
    .pipe(csv({ separator: '\t' })) // Assuming tab-separated values
    .on('data', (row) => {
        try {
            // Extract algebraic expressions
            const expressions = Object.values(row).slice(11); // Adjusted index to skip the non-expression columns

            // Evaluate each algebraic expression
            const scope = { ...row };
            const resultsForRow = expressions.map(expression => evaluateExpression(expression, scope));

            // Store the evaluated results
            results.push({ ...row, ...resultsForRow });
        } catch (error) {
            console.error('Error processing row:', error);
        }
    })
    .on('end', () => {
        const csvWriter = createObjectCsvWriter({
            path: outputFile,
            header: Object.keys(results[0]).map(key => ({ id: key, title: key }))
        });

        csvWriter.writeRecords(results)
            .then(() => console.log('Results written to output CSV file'))
            .catch(error => console.error('Error writing CSV file:', error));
    })
    .on('error', (error) => {
        console.error('Error reading input CSV file:', error);
    });

function evaluateExpression(expression, scope) {
    try {
        return math.evaluate(expression, scope);
    } catch (error) {
        console.error(`Error evaluating expression "${expression}": ${error.message}`);
        return 'ERROR';
    }
}
