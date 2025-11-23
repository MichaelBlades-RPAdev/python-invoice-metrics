import pandas as pd
from pathlib import Path
from .metrics import load_invoice_data, calculate_basic_metrics

def main():
    # Paths
    repo_root = Path(__file__).resolve().parent.parent
    data_path = repo_root / "data" / "sample_invoices.csv"
    output_path = repo_root / "reports" / "invoice_metrics_report.xlsx"

    # Load data
    df = load_invoice_data(str(data_path))

    # Calculate metrics
    metrics = calculate_basic_metrics(df)

    # Convert metrics to DataFrame for export
    summary = pd.DataFrame(
        [
            ["Total invoices", metrics["total_invoices"]],
            ["Total amount", metrics["total_amount"]],
            ["Average days to pay", metrics["avg_days_to_pay"]],
        ],
        columns=["Metric", "Value"],
    )

    # Supplier breakdown as separate sheet
    supplier_data = pd.DataFrame(
        list(metrics["invoices_per_supplier"].items()),
        columns=["Supplier", "Invoice Count"],
    )

    # Write to Excel
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        summary.to_excel(writer, index=False, sheet_name="Summary")
        supplier_data.to_excel(writer, index=False, sheet_name="BySupplier")

    print("Report generated at:", output_path)

if __name__ == "__main__":
    main()
