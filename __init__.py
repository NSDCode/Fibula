import requests
from rich import pretty
from rich.console import Console
from rich.table import Table
from rich import inspect as insp
import inspect

console = Console()


pretty.install()
class Method:
    def __init__(self, methodName, invoke):
        self.Name = methodName
        self.invoke = invoke

get_copy = Method("Get", requests.get)
post_copy = Method("Post", requests.post)
delete_copy = Method("Delete", requests.delete)

def cprint(message):
    console.print("🎣 [Fibula] ", style="bold magenta", end="")
    console.print(message, style="bold")



def print_content(Method, result):
    table = Table(show_header=True, header_style="bold grey58", show_edge=True, show_lines=False, show_footer=False)
    table.add_column("Type", style="bold white")
    table.add_column("Name", style="bold white")
    table.add_column("Value", style="bold white")

    cprint(f"Intercepted content from {Method.Name} ({Method.invoke})")
    cprint(f"Calling Method: {inspect.stack()[2][3]}")
    cprint(f"Calling code: {inspect.stack()[2][4]}")
    table.add_row(f"[orange][GENERAL][/orange]", "Url", result.url)
    table.add_row(f"[orange][GENERAL][/orange]", "Code", str(result.status_code))
    table.add_row(f"[green][RECEIVED][/green]","Content:", str(result.content[0:100]) if len(str(result.content)) > 100 else str(result.content))

    for n in result.headers:
        table.add_row("[green][RECEIVED][/green]", f"[gray]{n}[/gray]", f"[gray]{result.headers[n]}[/gray]")
    for j in result.request.headers:
        table.add_row("[blue][SENT][/blue]", f"[gray]{j}[/gray]", f"[gray]{result.request.headers[j]}[/gray]")

    table.add_row(f"[blue][SENT][/blue]","Content:", str(result.request.body[0:100]) if len(str(result.request.body)) > 100 else str(result.request.body))

    console.print(table)

def get(*args, **kwargs):
    result = get_copy.invoke(*args, **kwargs)
    print_content(get_copy, result)

def post(*args, **kwargs):
    result = post_copy.invoke(*args, **kwargs)
    print_content(post_copy, result)

def delete(*args, **kwargs):
    result = delete_copy.invoke(*args, **kwargs)
    print_content(delete_copy, result)

def define_hooks():
    cprint("Initializing hooks...")
    requests.get = get
    requests.post = post
    requests.delete = delete_copy

define_hooks()
cprint("Fibula has been initialized.")
