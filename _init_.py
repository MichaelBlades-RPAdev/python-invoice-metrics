python-invoice-metrics

This project demonstrates a simple Python workflow for processing invoice data with pandas. It loads a CSV file from the data folder, calculates a few useful business metrics, and writes the results to an Excel report in reports.

The structure is intentionally small and easy to read. It is meant as a clear example of using Python for day-to-day automation or AP-style data work.

Folder Structure
data/
Contains input files. A sample file (sample_invoices.csv) is included.
reports/
Output folder. The script writes invoice_metrics_report.xlsx here.
invoice_metrics/
Python package containing the actual logic.
metrics.py – functions for loading data and calculating metrics
main.py – entry point that generates the full report
__init__.py – package marker
tests/
Placeholder for optional tests.
requirements.txt
Python dependencies for the project.

What the tool does
Loads sample_invoices.csv
Parses dates where available
Calculates:
Total invoices
Total invoice value
Invoice counts per supplier
Average days to pay (for invoices with PaidDate)
Writes an Excel file with:
Summary sheet
BySupplier sheet

How to run
From the repository root:
pip install -r requirements.txt
python -m invoice_metrics.main

The output report will appear in:
reports/invoice_metrics_report.xlsx

Notes
The project uses relative imports and must be run as a module (python -m ...), not as a raw script.
The sample CSV is intentionally small so the logic is easy to follow.
The structure is suitable for extending into a larger automation or reporting tool.