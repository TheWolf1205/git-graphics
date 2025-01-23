import tkinter as tk
from tkinter import messagebox, simpledialog
import subprocess


def run_command(command):
    """Ejecuta un comando en el terminal y devuelve la salida o el error."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            messagebox.showerror("Error", result.stderr)
        return result.stdout
    except Exception as e:
        messagebox.showerror("Error", str(e))


def add_changes():
    """Añade los cambios al área de preparación."""
    output = run_command("git add .")
    messagebox.showinfo("Resultado", output or "Archivos añadidos correctamente.")


def commit_changes():
    """Confirma los cambios con un mensaje."""
    commit_message = simpledialog.askstring("Mensaje de commit", "Describe brevemente los cambios realizados:")
    if commit_message:
        output = run_command(f'git commit -m "{commit_message}"')
        messagebox.showinfo("Resultado", output or "Cambios confirmados correctamente.")


def pull_changes():
    """Actualiza los cambios del repositorio remoto."""
    output = run_command("git pull")
    messagebox.showinfo("Resultado", output or "Cambios actualizados desde el repositorio remoto.")


def push_changes():
    """Realiza un push al repositorio remoto."""
    confirm_push = messagebox.askyesno("Confirmación", "¿Deseas hacer un push?")
    if confirm_push:
        push_message = simpledialog.askstring("Mensaje de push", "Commit del cambio que vas a subir:")
        if push_message:
            run_command("git add .")
            run_command(f'git commit -m "{push_message}"')
            output = run_command("git push")
            messagebox.showinfo("Resultado", output or "Cambios subidos correctamente.")
    else:
        messagebox.showinfo("Info", "No se subieron cambios al repositorio remoto.")


def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Interfaz Git")
    root.geometry("400x300")

    # Crear los botones
    tk.Label(root, text="Opciones de Git", font=("Arial", 16)).pack(pady=10)

    tk.Button(root, text="Añadir cambios (git add .)", command=add_changes, width=30).pack(pady=5)
    tk.Button(root, text="Confirmar cambios (git commit)", command=commit_changes, width=30).pack(pady=5)
    tk.Button(root, text="Actualizar cambios (git pull)", command=pull_changes, width=30).pack(pady=5)
    tk.Button(root, text="Subir cambios (git push)", command=push_changes, width=30).pack(pady=5)

    tk.Button(root, text="Salir", command=root.quit, width=30, bg="red", fg="white").pack(pady=20)

    # Iniciar el bucle de la interfaz
    root.mainloop()


if __name__ == "__main__":
    main()

