# coding: utf-8

r"""
French regexes

Notes :
    - regexes will be case insensitive
    - regexes will be surrounded with (^|\s) and ($|\s) to reduce false positives
"""

income_regexes = [
    r"remise\s+de\s+cheque", # TODO : use operation type instead of regex ?
]

taxes_regexes = [
    r"impot",
]

internal_regexes = [
]

food_regexes = [
    r"ALDI",
    r"CARREFOUR",
    r"INTERMARCHE",
    r"SUPER\s+U",
    r"HYPER\s+U",
    r"U\s+EXPRESS",

    r"Dominos",

    r"DELIVEROO",
    r"UBER\s*EATS",

    r"RESTAUR?A?N?T?",
    r"BOULAN[GERIE]+",
]

housing_regexes = [
    r"EDF"
]

transport_regexes = [
    r"AUTOROUTE",
    r"Total",
]

internet_regexes = [
    r"abonnement\s+fibre",
    r"abonnement\s+mobile",
    r"OVH",
]

entertainment_regexes = [
]

sport_regexes = [
    r"climb"
]

health_regexes = [
    r"C\.P\.A\.M\.",
    r"PH[ARMACIE][3,]",
    r"docteur",
    r"DR\.?",
    r"labo",
    r"Eurofins",
    r"Biomnis",
]

gifts_regexes = [
    r"leetchi",
]

travel_regexes = [
]

home_improvement_regexes = [
    r"LEROY\s+MERL?I?N?",
    r"JARDILAND",
]

cash_withdrawal_regexes = [
]

shopping_regexes = [
    r"jules",
    r"celio",
    r"zara",
    r"bershka",
]
