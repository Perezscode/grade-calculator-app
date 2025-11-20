import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        components = [
            (entry_grade_tasks.get(), entry_weight_tasks.get()),
            (entry_grade_quizzes.get(), entry_weight_quizzes.get()),
            (entry_grade_exams.get(), entry_weight_exams.get()),
            (entry_grade_project.get(), entry_weight_project.get()),
        ]

        total_weight = 0.0
        weighted_sum = 0.0

        for grade_str, weight_str in components:
            grade_str = grade_str.strip()
            weight_str = weight_str.strip()

            if grade_str == "" and weight_str == "":
                continue  # ignorar filas vacías

            if grade_str == "" or weight_str == "":
                messagebox.showerror(
                    "Error",
                    "Si usas un componente, debes llenar nota y peso."
                )
                return

            grade = float(grade_str)
            weight = float(weight_str)

            if grade < 0 or grade > 100:
                messagebox.showerror(
                    "Error",
                    "Las notas deben estar entre 0 y 100."
                )
                return

            if weight <= 0:
                messagebox.showerror(
                    "Error",
                    "Los pesos deben ser mayores que 0."
                )
                return

            total_weight += weight
            weighted_sum += grade * weight

        if total_weight == 0:
            messagebox.showerror(
                "Error",
                "Debes ingresar al menos un componente con peso."
            )
            return

        final_average = weighted_sum / total_weight
        final_average_rounded = round(final_average, 2)

        letter = get_letter_grade(final_average)

        label_result.config(
            text=f"Promedio final: {final_average_rounded}%  |  Letra: {letter}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Por favor ingresa solo números en notas y pesos."
        )

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# --- UI ---

root = tk.Tk()
root.title("Grade Calculator App")

# Encabezados
label_title = tk.Label(root, text="Grade Calculator App", font=("Arial", 14, "bold"))
label_title.grid(row=0, column=0, columnspan=3, pady=(10, 10))

label_component = tk.Label(root, text="Componente")
label_component.grid(row=1, column=0, padx=10, pady=5)

label_grade = tk.Label(root, text="Nota (%)")
label_grade.grid(row=1, column=1, padx=10, pady=5)

label_weight = tk.Label(root, text="Peso (%)")
label_weight.grid(row=1, column=2, padx=10, pady=5)

# Fila 1: Tareas
label_tasks = tk.Label(root, text="Tareas")
label_tasks.grid(row=2, column=0, sticky="w", padx=10, pady=5)

entry_grade_tasks = tk.Entry(root, width=10)
entry_grade_tasks.grid(row=2, column=1, padx=10, pady=5)

entry_weight_tasks = tk.Entry(root, width=10)
entry_weight_tasks.grid(row=2, column=2, padx=10, pady=5)

# Fila 2: Quizzes
label_quizzes = tk.Label(root, text="Quizzes")
label_quizzes.grid(row=3, column=0, sticky="w", padx=10, pady=5)

entry_grade_quizzes = tk.Entry(root, width=10)
entry_grade_quizzes.grid(row=3, column=1, padx=10, pady=5)

entry_weight_quizzes = tk.Entry(root, width=10)
entry_weight_quizzes.grid(row=3, column=2, padx=10, pady=5)

# Fila 3: Exámenes
label_exams = tk.Label(root, text="Exámenes")
label_exams.grid(row=4, column=0, sticky="w", padx=10, pady=5)

entry_grade_exams = tk.Entry(root, width=10)
entry_grade_exams.grid(row=4, column=1, padx=10, pady=5)

entry_weight_exams = tk.Entry(root, width=10)
entry_weight_exams.grid(row=4, column=2, padx=10, pady=5)

# Fila 4: Proyecto final
label_project = tk.Label(root, text="Proyecto final")
label_project.grid(row=5, column=0, sticky="w", padx=10, pady=5)

entry_grade_project = tk.Entry(root, width=10)
entry_grade_project.grid(row=5, column=1, padx=10, pady=5)

entry_weight_project = tk.Entry(root, width=10)
entry_weight_project.grid(row=5, column=2, padx=10, pady=5)

# Botón calcular
button_calculate = tk.Button(root, text="Calcular promedio", command=calculate_grade)
button_calculate.grid(row=6, column=0, columnspan=3, pady=15)

# Resultado
label_result = tk.Label(root, text="Promedio final: --  |  Letra: --", font=("Arial", 11))
label_result.grid(row=7, column=0, columnspan=3, pady=(0, 15))

root.mainloop()
