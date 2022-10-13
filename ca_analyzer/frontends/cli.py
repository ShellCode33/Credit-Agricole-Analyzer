# coding: utf-8

"""
This Command Line Interface only aims to showcase how this library can be used.
It doesn't do anything useful.
"""

import os
import argparse
from getpass import getpass

from IPython import start_ipython
from traitlets.config.loader import Config

from creditagricole.api import CreditAgricole, CreditAgricoleException
from creditagricole import CA_COUNTRIES

from ca_analyzer import plots
from ca_analyzer.analyzer import transactions_to_balance_dataframe
from ca_analyzer.categories import categorize

def parse_cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Welcome to the Credit Agricole utility')

    parser.add_argument('--country', choices=CA_COUNTRIES.keys(), help="the country you're in")
    parser.add_argument('--region', help="the region of the Credit Agricole you're affiliated to")

    args = parser.parse_args()
    return args

def summary(country: str, region: str) -> None:
    ca = CA_COUNTRIES[country](region) # type: CreditAgricole

    try:
        user_id = os.environ["CA_USER_ID"]
    except KeyError:
        user_id = input("User ID: ")

    try:
        pin_code = os.environ["CA_PIN_CODE"]
    except KeyError:
        pin_code = getpass("Pin code: ")

    ca.login(user_id, pin_code)

    if ca.loans:
        total_left_to_pay = sum(l.left_to_pay for l in ca.loans)
        print(f"You owe the bank: {total_left_to_pay:.2f}{ca.loans[0].currency}")
        print()

    main_account = ca.accounts[0]

    transactions_per_cat = categorize(main_account.transactions, country)

    balance_dataframe = transactions_to_balance_dataframe(main_account.balance, transactions_per_cat)
    plots.balance_dataframe = balance_dataframe

    banner1 = "Welcome to the Credit Agricole Analyzer !\n"
    banner2 = "Available variables:\n" \
              "    - creditagricole : CreditAgricole instance\n" \
              "    - account : Account instance (your main account)\n" \
              "    - transactions_per_cat : dict of transactions sorted by category\n" \
              "    - balance_dataframe : pandas dataframe of the balance over time\n" \
              "    - plots : plotting facility\n" \
              "\n(This is an IPython shell, enjoy)"

    c = Config()
    c.TerminalInteractiveShell.banner1 = banner1
    c.TerminalInteractiveShell.banner2 = banner2

    start_ipython(argv=[], config=c, user_ns={
        "creditagricole": ca,
        "account": main_account,
        "transactions_per_cat": transactions_per_cat,
        "balance_dataframe": balance_dataframe,
        "plots": plots
    })

def main() -> None:
    args = parse_cli()

    try:
        summary(args.country, args.region)
    except CreditAgricoleException as cae:
        print(f"[ERROR] {cae}")
