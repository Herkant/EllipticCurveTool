import tkinter as tk
from tkinter import ttk
from sympy import symbols, solve, sqrt
import matplotlib.pyplot as plt
import numpy as np


def calculate_discriminant(a, b):
    """Calculate the discriminant of the elliptic curve"""
    return 4 * a**3 + 27 * b**2


def j_invariant(a, b):
    """Calculate the j-invariant"""
    delta = calculate_discriminant(a, b)
    return 1728 * (4 * a**3) / delta if delta != 0 else None


def find_points_in_field(a, b, p):
    """Calculate the points on the elliptic curve over the finite field"""
    points = []
    for x in range(p):
        for y in range(p):
            if (y**2 - (x**3 + a * x + b)) % p == 0:
                points.append((x, y))
    return points


def plot_elliptic_curve(a, b):
    """Plot the elliptic curve"""
    x_vals = np.linspace(-5, 5, 500)
    y_vals = []
    for x in x_vals:
        try:
            y = sqrt(x**3 + a * x + b)
            y_vals.append(float(y))
        except ValueError:
            y_vals.append(np.nan)
    
    neg_y_vals = [-y if not np.isnan(y) else np.nan for y in y_vals]
    
    plt.plot(x_vals, y_vals, label="y = +sqrt(x^3 + ax + b)")
    plt.plot(x_vals, neg_y_vals, label="y = -sqrt(x^3 + ax + b)")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.title(f"Elliptic Curve: y^2 = x^3 + {a}x + {b}")
    plt.legend()


def plot_elliptic_function(a, b):
    """Plot the elliptic function"""
    t_vals = np.linspace(-10, 10, 500)
    x_vals = a * np.cos(t_vals)**2
    y_vals = b * np.sin(t_vals) * np.cos(t_vals)

    plt.plot(x_vals, y_vals, label="Elliptic Function")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.title("Elliptic Function (Parametric form)")
    plt.legend()


def on_calculate():
    """Handle the user's calculation request"""
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        p = int(entry_p.get())
        
        # Calculate discriminant and j-invariant
        delta = calculate_discriminant(a, b)
        j_value = j_invariant(a, b)
        
        # Update results
        label_discriminant_value.config(text=f"Δ = {delta}")
        label_j_invariant_value.config(text=f"j = {j_value:.4f}" if j_value else "j = Invalid")
        
        # Calculate points over the finite field
        points = find_points_in_field(a, b, p)
        text_field_points.delete(1.0, tk.END)
        text_field_points.insert(tk.END, str(points))
        
        # Plot the curve
        plt.figure(figsize=(10, 6))
        plot_elliptic_curve(a, b)
        plot_elliptic_function(a, b)
        plt.show()

    except Exception as e:
        label_error.config(text=f"Error: {e}")


# Create the main window
root = tk.Tk()
root.title("Elliptic Curve Tool")

# Input section
frame_input = ttk.Frame(root, padding="10")
frame_input.grid(row=0, column=0, sticky="W")

ttk.Label(frame_input, text="Parameter a:").grid(row=0, column=0, sticky="W")
entry_a = ttk.Entry(frame_input, width=10)
entry_a.grid(row=0, column=1)

ttk.Label(frame_input, text="Parameter b:").grid(row=1, column=0, sticky="W")
entry_b = ttk.Entry(frame_input, width=10)
entry_b.grid(row=1, column=1)

ttk.Label(frame_input, text="Finite Field p:").grid(row=2, column=0, sticky="W")
entry_p = ttk.Entry(frame_input, width=10)
entry_p.grid(row=2, column=1)

# Calculate button
button_calculate = ttk.Button(frame_input, text="Calculate", command=on_calculate)
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

# Output section
frame_output = ttk.Frame(root, padding="10")
frame_output.grid(row=1, column=0, sticky="W")

ttk.Label(frame_output, text="Discriminant:").grid(row=0, column=0, sticky="W")
label_discriminant_value = ttk.Label(frame_output, text="Δ = ")
label_discriminant_value.grid(row=0, column=1, sticky="W")

ttk.Label(frame_output, text="j-invariant:").grid(row=1, column=0, sticky="W")
label_j_invariant_value = ttk.Label(frame_output, text="j = ")
label_j_invariant_value.grid(row=1, column=1, sticky="W")

# Finite field points
ttk.Label(frame_output, text="Finite Field Points:").grid(row=2, column=0, sticky="W")
text_field_points = tk.Text(frame_output, height=5, width=50)
text_field_points.grid(row=2, column=1, sticky="W")

# Error message
label_error = ttk.Label(root, text="", foreground="red")
label_error.grid(row=2, column=0, sticky="W")

root.mainloop()
