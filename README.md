python-invoice-metrics



This project reads invoice data from a CSV file, calculates a small set of business metrics using pandas, and writes a summary report into the reports folder. It is a simple, clean example of Python-based data processing for accounts payable or automation work.



Folder Structure



data/ – input files such as sample\_invoices.csv

reports/ – output folder for generated Excel or CSV reports

invoice\_metrics/ – main Python package

\_\_init\_\_.py – package marker

(scripts added later)

tests/ – optional test files

requirements.txt – Python dependencies



What the tool will do

Load invoice data from data/

Calculate basic metrics such as:

total invoices

total value

invoices per supplier

average days to pay (if available)

Write a summary report to reports/

Running the project



Once the code is added:

pip install -r requirements.txt

python invoice\_metrics/main.py





The generated report will appear in the reports folder.

