import pandas as pd

def load_invoice_data(csv_path: str) -> pd.DataFrame:
    """Load invoice data from a CSV file and parse date columns if they exist."""
    df = pd.read_csv(csv_path)

    # Parse date columns only if present
    date_cols = ["InvoiceDate", "DueDate", "PaidDate"]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    return df


def calculate_basic_metrics(df: pd.DataFrame) -> dict:
    """Calculate a small set of business metrics from invoice data."""

    # Total count
    total_invoices = len(df)

    # Total value
    total_amount = df["Amount"].sum() if "Amount" in df.columns else None

    # Invoices per supplier
    if "Supplier" in df.columns:
        invoices_per_supplier = (
            df.groupby("Supplier")["InvoiceNumber"]
            .count()
            .to_dict()
        )
    else:
        invoices_per_supplier = {}

    # Days to pay (only where PaidDate exists)
    if "PaidDate" in df.columns and "InvoiceDate" in df.columns:
        df_paid = df.dropna(subset=["PaidDate"])
        if not df_paid.empty:
            df_paid["DaysToPay"] = (df_paid["PaidDate"] - df_paid["InvoiceDate"]).dt.days
            avg_days_to_pay = df_paid["DaysToPay"].mean()
        else:
            avg_days_to_pay = None
    else:
        avg_days_to_pay = None

    return {
        "total_invoices": total_invoices,
        "total_amount": total_amount,
        "invoices_per_supplier": invoices_per_supplier,
        "avg_days_to_pay": avg_days_to_pay,
    }
