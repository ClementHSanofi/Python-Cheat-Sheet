from docs import MA_CONSTANTE, addition, puissance
from rich import print

print(f"[bold green]CONSTANTE:[/bold green] {MA_CONSTANTE}")
print(f"[bold yellow]Fonctions:[/bold yellow] {addition(1, 4)}")
print(f"[bold blue]Méthodes:[/bold blue] {puissance(2, 4)}")
print(f"[bold magenta]Docstring:[/bold magenta] {puissance.__doc__}")