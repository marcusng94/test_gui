# # this creates a grid that's minesweeper-like without the bomb. ha ha ha.
#
# from tkinter import *
#
# class Cell():
#     FILLED_COLOR_BG = "blue"
#     EMPTY_COLOR_BG = "red"
#     FILLED_COLOR_BORDER = "black"
#     EMPTY_COLOR_BORDER = "black"
#
#     def __init__(self, master, x, y, size):
#         """ Constructor of the object called by Cell(...) """
#         self.master = master
#         self.abs = x
#         self.ord = y
#         self.size= size
#         self.fill= False
#
#     def _switch(self):
#         """ Switch if the cell is filled or not. """
#         self.fill= not self.fill
#
#     def draw(self):
#         """ order to the cell to draw its representation on the canvas """
#         if self.master != None :
#             fill = Cell.FILLED_COLOR_BG
#             outline = Cell.FILLED_COLOR_BORDER
#
#             if not self.fill:
#                 fill = Cell.EMPTY_COLOR_BG
#                 outline = Cell.EMPTY_COLOR_BORDER
#
#             xmin = self.abs * self.size
#             xmax = xmin + self.size
#             ymin = self.ord * self.size
#             ymax = ymin + self.size
#
#             self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)
#
# class CellGrid(Canvas):
#     def __init__(self,master, rowNumber, columnNumber, cellSize, *args, **kwargs):
#         Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)
#
#         self.cellSize = cellSize
#
#         self.grid = []
#         for row in range(rowNumber):
#
#             line = []
#             for column in range(columnNumber):
#                 line.append(Cell(self, column, row, cellSize))
#
#             self.grid.append(line)
#
#         #memorize the cells that have been modified to avoid many switching of state during mouse motion.
#         self.switched = []
#
#         #bind click action
#         self.bind("<Button-1>", self.handleMouseClick)
#         #bind moving while clicking
#         self.bind("<B1-Motion>", self.handleMouseMotion)
#         #bind release button action - clear the memory of midified cells.
#         self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())
#
#         self.draw()
#
#
#
#     def draw(self):
#         for row in self.grid:
#             for cell in row:
#                 cell.draw()
#
#     def _eventCoords(self, event):
#         row = int(event.y / self.cellSize)
#         column = int(event.x / self.cellSize)
#         return row, column
#
#     def handleMouseClick(self, event):
#         row, column = self._eventCoords(event)
#         cell = self.grid[row][column]
#         cell._switch()
#         cell.draw()
#         #add the cell to the list of cell switched during the click
#         self.switched.append(cell)
#
#     def handleMouseMotion(self, event):
#         row, column = self._eventCoords(event)
#         cell = self.grid[row][column]
#
#         if cell not in self.switched:
#             cell._switch()
#             cell.draw()
#             self.switched.append(cell)
#
#
# if __name__ == "__main__" :
#     app = Tk()
#
#     grid = CellGrid(app, 5, 5, 200)
#     grid.pack()
#
#     app.mainloop()

from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

b1 = Button(topFrame, text="A1", fg="red", font=20)
b2 = Button(topFrame, text="A2", fg="blue")
b3 = Button(topFrame, text="A3", fg="green")
b4 = Button(topFrame, text="B1", fg="orange")
b5 = Button(topFrame, text="B2", fg="pink")
b6 = Button(topFrame, text="B3", fg="purple")
b7 = Button(topFrame, text="C1", fg="grey")
b8 = Button(topFrame, text="C2", fg="black")
b9 = Button(topFrame, text="C3", fg="brown")

b1.config(height=15, width=40)
b2.config(height=15, width=40)
b3.config(height=15, width=40)
b4.config(height=15, width=40)
b5.config(height=15, width=40)
b6.config(height=15, width=40)
b7.config(height=15, width=40)
b8.config(height=15, width=40)
b9.config(height=15, width=40)


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
#
# button1.pack(side=LEFT)
# button2.pack(side=RIGHT)
# button3.pack(side=TOP)
# button4.pack(side=BOTTOM)

# one = Label(root, text="One", bg="red", fg="white")
# one.pack()
# two = Label(root, text="Two", bg="green", fg="black")
# two.pack(fill=X)
# three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)

# root.geometry("1080x725+200+200")
root.mainloop()
