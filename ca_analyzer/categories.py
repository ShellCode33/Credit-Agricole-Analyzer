# coding: utf-8

import re
from enum import Enum, auto
from typing import List, Dict

from creditagricole.account import Transaction

from ca_analyzer import regexes

_REGEX_FLAGS = re.DOTALL | re.IGNORECASE

class TransactionCategory(Enum):
    INCOME = auto() # Salary, renting, etc.
    TAXES = auto()
    INTERNAL = auto() # Transactions you make from one of your account to another

    FOOD = auto() # Grocery store, Uber eats, etc.
    HOUSING = auto() # Rent, gas, electricity, water, etc.
    TRANSPORT = auto() # Fuel, car maintenance, bus tickets, etc.
    INTERNET = auto() # Fibre subscription, mobile phone subscription, servers rent, etc.
    ENTERTAINMENT = auto() # Cinema, beers with friends, etc.

    SPORT = auto() # Physical activies
    HEALTH = auto() # Drugs, doc consultation, etc.

    GIFTS = auto() # If you feel generous :) Can also include donations
    TRAVEL = auto() # What you spend during a trip, it's up to you to put transport, food, etc. in here
    HOME_IMPROVEMENT = auto() # DIY, Hacking, etc.
    CASH_WITHDRAWAL = auto()
    SHOPPING = auto() # Clothing, furniture, etc.

    OTHER = auto() # Anything that doesnt match the other categories

CategorizedTransactions = Dict[TransactionCategory, List[Transaction]]

def categorize(transactions: List[Transaction], country: str) -> CategorizedTransactions:

    regex_module = regexes.regex_module_per_country[country]

    regexes_per_cat = {
        TransactionCategory.INCOME: regex_module.income_regexes,
        TransactionCategory.TAXES: regex_module.taxes_regexes,
        TransactionCategory.INTERNAL: regex_module.internal_regexes,
        TransactionCategory.FOOD: regex_module.food_regexes,
        TransactionCategory.HOUSING: regex_module.housing_regexes,
        TransactionCategory.TRANSPORT: regex_module.transport_regexes,
        TransactionCategory.INTERNET: regex_module.internet_regexes,
        TransactionCategory.ENTERTAINMENT: regex_module.entertainment_regexes,
        TransactionCategory.SPORT: regex_module.sport_regexes,
        TransactionCategory.HEALTH: regex_module.health_regexes,
        TransactionCategory.GIFTS: regex_module.gifts_regexes,
        TransactionCategory.TRAVEL: regex_module.travel_regexes,
        TransactionCategory.HOME_IMPROVEMENT: regex_module.home_improvement_regexes,
        TransactionCategory.CASH_WITHDRAWAL: regex_module.cash_withdrawal_regexes,
        TransactionCategory.SHOPPING: regex_module.shopping_regexes,
    }

    transactions_per_cat = {
        TransactionCategory.INCOME: [],
        TransactionCategory.TAXES: [],
        TransactionCategory.INTERNAL: [],
        TransactionCategory.FOOD: [],
        TransactionCategory.HOUSING: [],
        TransactionCategory.TRANSPORT: [],
        TransactionCategory.INTERNET: [],
        TransactionCategory.ENTERTAINMENT: [],
        TransactionCategory.SPORT: [],
        TransactionCategory.HEALTH: [],
        TransactionCategory.GIFTS: [],
        TransactionCategory.TRAVEL: [],
        TransactionCategory.HOME_IMPROVEMENT: [],
        TransactionCategory.CASH_WITHDRAWAL: [],
        TransactionCategory.SHOPPING: [],
        TransactionCategory.OTHER: [],
    }

    for transaction in transactions:
        for category, cat_regexes in regexes_per_cat.items():

            found_a_match = False

            for regex in cat_regexes:
                regex = rf"(^|\s){regex}($|\s)" # reduce false positives
                match = re.search(regex, transaction.label, flags=_REGEX_FLAGS)

                # If regex didn't match in the label, try in the description
                if not match:
                    match = re.search(regex, transaction.description, flags=_REGEX_FLAGS)

                if match:
                    transactions_per_cat[category].append(transaction)
                    found_a_match = True
                    break

            if found_a_match:
                break

        # If none of the regexes matched the transaction, put it in the OTHER category
        else:
            transactions_per_cat[TransactionCategory.OTHER].append(transaction)

    return transactions_per_cat
