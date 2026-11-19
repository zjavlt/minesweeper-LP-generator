import tkinter as tk
from pulp import *


def color_to_hex(code: tuple[float]):
    hexa = ""
    for i in code:
        hexed = f"{int(i):X}"
        if len(hexed) < 2:
            hexed = f"0{hexed}"
        hexa += hexed
    return "#" + hexa

def calculate_color(cost: float, maxi, mini):
    level = (cost-mini)/(maxi-mini)
    color = level * 255
    return color_to_hex((color, color, color))

def project_contours(costs: list[list[float]], board: list[list[str]]):
    maxi = costs[0][0]
    mini = costs[0][0]

    for i in costs:
        maxi = max(maxi, max(i))
        mini = min(mini, min(i))
    
    view = tk.Tk()
    view.title("Contours")
    view.geometry("800x600")

    rows, cols = len(costs), len(costs[0])

    for col in range(cols):
        view.columnconfigure(col, weight=1)
    for row in range(rows):
        view.rowconfigure(row+1, weight=1)

    for r in range(rows):
        for c in range(cols):
            label = tk.Label(view, text=" ", bg=calculate_color(costs[r][c], maxi=maxi, mini=mini))
            label.grid(row=r, column=c, sticky="ewns")

    view.mainloop()