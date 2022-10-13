# coding: utf-8

from pandas import DataFrame

from ca_analyzer import CategorizedTransactions

def transactions_to_balance_dataframe(
    current_balance: float,
    transactions_per_cat: CategorizedTransactions) -> DataFrame:

    rows = []

    for category, operations in transactions_per_cat.items():
        for operation in operations:
            rows.append({"category": category.name} | operation.__dict__)

    dataframe = DataFrame(rows)

    # We assume we don't have the whole history of transactions.
    # So we make sure the graph will end to our current balance by offsetting values.
    balance_over_time = dataframe.groupby("date")["amount"].sum().cumsum()
    last_value = balance_over_time.iloc[-1]
    offset = current_balance - last_value

    # Convert dataframe of transactions to dataframe of balance
    balance_over_time += offset

    return balance_over_time.to_frame()
