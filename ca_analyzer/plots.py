# coding: utf-8

from pandas import DataFrame
from typing import Optional

from matplotlib import pyplot
from matplotlib import ticker, dates

from ca_analyzer import CreditAgricoleAnalyzerError
from mplcursors import cursor, HoverMode

balance_dataframe = None # type: Optional[DataFrame]
expenses_dataframe = None # type: Optional[DataFrame]

def balance_over_time():

    if balance_dataframe is None:
        raise CreditAgricoleAnalyzerError("global balance_dataframe is empty")

    df_no_index = balance_dataframe.reset_index()
    dots = df_no_index.plot.scatter(title="Balance over time",
                                    x="date",
                                    y="amount",
                                    c="red",
                                    marker="o")

    # Annotate dots
    cur = cursor(hover=HoverMode.Transient)

    # Customize annotation
    @cur.connect("add")
    def _(sel):
        sel.annotation.get_bbox_patch().set(fc="white")
        date = dates.num2date(sel.target[0])
        balance = sel.target[1]
        sel.annotation.set_text(f"Date: {date:%x}\nBalance: {balance:,.2f}")

    # Connect dots with line
    df_no_index.plot.line(x="date", y="amount", ax=dots)

    axes = pyplot.gca()
    axes.set_xlabel("Date")
    axes.set_ylabel("Balance")

    axes.yaxis.set_major_locator(ticker.MaxNLocator(20))
    axes.xaxis.set_major_locator(dates.DayLocator(bymonthday=[1]))
    axes.xaxis.set_minor_locator(dates.DayLocator())

    axes.xaxis.set_major_formatter(dates.DateFormatter('%x'))
    axes.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.2f}"))

    pyplot.xticks(rotation=90, horizontalalignment="center")
    pyplot.legend("", frameon=False) # Remove useless legend
    pyplot.show()

def monthly_expenses():

    if expenses_dataframe is None:
        raise CreditAgricoleAnalyzerError("global expenses_dataframe is empty")

    expenses_dataframe.plot()

def expenses_breakdown():

    if expenses_dataframe is None:
        raise CreditAgricoleAnalyzerError("global expenses_dataframe is empty")

    expenses_dataframe.plot()

# Choose what to expose to IPython autocompletion
def __dir__():
    return ["balance_over_time", "monthly_expenses", "expenses_breakdown"]
