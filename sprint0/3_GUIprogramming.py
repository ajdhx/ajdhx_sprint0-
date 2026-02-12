import tkinter as tk


def main():
    root = tk.Tk()
    root.title("GUI programming")

    label = tk.Label(root, text="sprint0 GUI")
    label.pack()

    canvas = tk.Canvas(root, width=200, height=200)
    canvas.create_line(0, 150, 200, 150)

    checkbox = tk.Checkbutton(root, text="checkbox")
    checkbox.pack()

    radiobutton = tk.Radiobutton(root, text="radiobutton")
    radiobutton.pack()
    
    radiobutton2 = tk.Radiobutton(root, text="radiobutton2")
    radiobutton2.pack()

    canvas.pack()
    canvas.create_line(0, 10, 200, 10)

    root.mainloop()


if __name__ == '__main__':
    main()


