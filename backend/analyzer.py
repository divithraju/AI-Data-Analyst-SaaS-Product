import pandas as pd
import numpy as np

def analyze_csv(file_path: str, question: str):
    df = pd.read_csv(file_path)
    q = question.lower()

    numeric_cols = df.select_dtypes(include="number").columns

    # ---------- BASIC METRICS ----------
    if "average" in q or "mean" in q:
        return df[numeric_cols].mean().to_dict()

    if "sum" in q or "total" in q:
        return df[numeric_cols].sum().to_dict()

    if "count" in q:
        return {"rows": len(df)}

    if "min" in q:
        return df[numeric_cols].min().to_dict()

    if "max" in q:
        return df[numeric_cols].max().to_dict()

    if "median" in q:
        return df[numeric_cols].median().to_dict()

    if "std" in q or "standard deviation" in q:
        return df[numeric_cols].std().to_dict()

    if "variance" in q:
        return df[numeric_cols].var().to_dict()

    # ---------- DISTRIBUTION ----------
    if "describe" in q or "summary" in q:
        return df.describe(include="all").to_dict()

    # ---------- CORRELATION ----------
    if "correlation" in q or "relationship" in q:
        return df[numeric_cols].corr().to_dict()

    # ---------- TOP / BOTTOM ----------
    if "top" in q:
        return df[numeric_cols].max().to_dict()

    if "bottom" in q or "lowest" in q:
        return df[numeric_cols].min().to_dict()

    # ---------- OUTLIER DETECTION ----------
    if "outlier" in q:
        outliers = {}
        for col in numeric_cols:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            outliers[col] = df[
                (df[col] < (q1 - 1.5 * iqr)) |
                (df[col] > (q3 + 1.5 * iqr))
            ][col].tolist()
        return outliers

    # ---------- PERCENTAGE CONTRIBUTION ----------
    if "percentage" in q or "contribution" in q:
        totals = df[numeric_cols].sum()
        return ((df[numeric_cols] / totals) * 100).round(2).to_dict()

    # ---------- GROUP BY ----------
    if "group by" in q or "per" in q:
        cat_cols = df.select_dtypes(exclude="number").columns
        if len(cat_cols) > 0:
            grouped = df.groupby(cat_cols[0])[numeric_cols].mean()
            return grouped.to_dict()
        else:
            return "No categorical column found for grouping"

    # ---------- TREND / GROWTH ----------
    if "trend" in q or "growth" in q:
        if len(numeric_cols) > 0:
            growth = df[numeric_cols].pct_change().mean() * 100
            return growth.round(2).to_dict()

    return {
        "message": "Analysis completed",
        "available_analysis": [
            "average, sum, count, min, max",
            "median, std, variance",
            "summary, correlation",
            "outliers, top/bottom",
            "group by, percentage",
            "trend, growth"
        ]
    }
