import typer
from datetime import datetime
from rich import print

from constants import MINUTES_IN_HOURS, SECONDS_IN_HOURS
from utils import format_to_currency

app = typer.Typer()

@app.command()
def hours_cost():
    try:
        print()
        typer.secho(
            "Calculate the cost of hours worked", bold=True, bg=typer.colors.CYAN, fg=typer.colors.WHITE
        )
        print()

        time = typer.prompt("Enter the time in format HH:MM:SS")
        rate = typer.prompt("Enter the rate per hour", type=int)
        currency = typer.prompt("Enter the currency", default="PYG")

        time_obj = datetime.strptime(time, "%H:%M:%S")

        hours = (
            time_obj.hour + 
            time_obj.minute / MINUTES_IN_HOURS + 
            time_obj.second / SECONDS_IN_HOURS
        )

        total = hours * rate

        print(f"Total cost: [bold green]{format_to_currency(total)} {currency}[/bold green]\n")
    except ValueError:
        print("[bold red]Invalid time format[/bold red] please enter the time in format HH:MM:SS")

if __name__ == '__main__':
    app()