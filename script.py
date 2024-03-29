import csv

# Given data
data = {
    'A': 7, 'B': 10, 'C': 36, 'D': 5, 'E': 9,
    'F': 0, 'G': 1, 'H': 4, 'I': 17, 'J': 12, 'K': 22
}

# Define functions for operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else None

# Define expressions
expressions = [
    "(A + B)", "(A - B)", "(D * A)", "(A * D)", "(E / G)",
    "(A + K - J)", "(F * C * B)", "(H - B + A)", "(I * A)",
    "(C + K + D)", "(D - A + C)",
    "(D - A)", "((A * D) - F)", "(A + B + C)", "(A - C + E)",
    "((A + B) + K)", "(K * (F * G))", "(I / J / G)", "(G * G / G + G)",
    "(F + G - G * G)", "(D - F)", "(F - F * F)",
    "(K + J + I + H)", "(H - K + J)", "(K + J - A)", "(D - H)",
    "(H + (D / C))", "(C + C + C)", "(A)", "(J / I / G)", "(G - H)",
    "(J * J - K)", "(F + F + F)",
    "(D * A)", "(A + A + A)", "(F * G)", "(F * H)", "(H * F)",
    "(I - J * K / E)", "(E * E * E)", "(B)", "(G / I / J)", "(J / J)",
    "(E / E)",
    "(E)", "(F)", "(G)", "(H - H + K)", "(F * C)",
    "(I + J - K - K)", "(G + E - K)", "(E + D - C)", "(C)",
    "(J - H)", "(J * J)",
    "(C - C)", "(D - D)", "(F * F * D)", "(G + E)", "(E + G)",
    "(G / J)", "(B + E + D / E)", "(G * (E - D))", "((A + B) * C)",
    "(D)", "(K - B)"
]

# Evaluate expressions
results = []
for expr in expressions:
    try:
        expr_result = eval(expr, {}, data)
        results.append(expr_result)
    except (NameError, ZeroDivisionError) as e:
        results.append(str(e))

# Write results to CSV file
with open('results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Expression', 'Result'])
    for expr, result in zip(expressions, results):
        writer.writerow([expr, result])

print("Results written to output CSV file.")
