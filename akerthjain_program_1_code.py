'''
OOP Language: Python
GUI library: Tkinter
IDE: Antigravity
xUnit framework: unittest
Programming Style Guide: PEP 8
Project hosting site: GitHub
Other decisions: none yet
'''

'''
AI disclosure:

The following prompts were used with an AI language model during the development of this work.

1. How do I write an AI usage disclosure? What are the common formats?
2. What is a good testing framework, style guide, and GUI library for python? 
3. 2_unittest has 0 tests ran when run. What is the error?
4. How do I use the tkinter library with simple code in python? 
5. The current code creates a diagonal line underneath the radio button. How do I change it to a horizontal line under the radio button?
6. Can you fix all files to follow the PEP 8 style guide and note changes made? (note: these notes were left in the code on purpose for disclosure purposes)
7. Why isn't the second radiobutton visible in the gui?
8. Can you help debug this combined file? 
'''

import operator
import unittest
import tkinter as tk


class TestOperator(unittest.TestCase):

    def test_adding(self):
        self.assertEqual(operator.add(1, 2), 3)

    def test_subtracting(self):
        self.assertEqual(operator.sub(3, 2), 1)


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
    
    unittest.main(exit=False)
    main()
