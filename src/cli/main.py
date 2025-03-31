import sys
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table  # Importamos Table para mostrar datos tabulares
from services.user_service import create_user, get_all_users
from database.connection import SessionLocal
from contextlib import contextmanager

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

console = Console()

def show_menu():
    while True:
        console.print("\n[bold]Menú Principal[/bold]", justify="center")
        console.print("1. Crear usuario")
        console.print("2. Listar usuarios")
        console.print("3. Salir")
        
        option = Prompt.ask("Seleccione una opción", choices=["1", "2", "3"])
        
        if option == "1":
            create_user_cli()
        elif option == "2":
            list_users_cli()
        else:
            break

def create_user_cli():
    with get_db() as db:    
        try:
            nombre = Prompt.ask("Nombre")
            email = Prompt.ask("Email")
            password = Prompt.ask("Password", password=True)
            create_user(db, nombre, email, password)
            console.print("[green]Usuario creado exitosamente![/green]")
        except Exception as e:
            console.print(f"[red]Error: {str(e)}[/red]")

def list_users_cli():
    with get_db() as db:       
        try:
            users = get_all_users(db)
            
            if not users:
                console.print("[yellow]No hay usuarios registrados[/yellow]")
                return

            # Crear tabla con rich
            table = Table(title="Lista de Usuarios")
            table.add_column("ID", style="cyan")
            table.add_column("Nombre", style="magenta")
            table.add_column("Email", style="green")
            table.add_column("Fecha de Creación", style="blue")

            for user in users:
                table.add_row(
                    str(user.id),
                    user.nombre,
                    user.email,
                    user.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
                )
                
            console.print(table)
            
        except Exception as e:
            console.print(f"[red]Error al obtener usuarios: {str(e)}[/red]")

# Llamada inicial para iniciar el menú
if __name__ == "__main__":
    show_menu()