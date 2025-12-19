import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
root.title("Хрестики Нулики")

# код вiдображеня вiкна (интерфейз) - робе вроде хтось iнший - тому в мене його нема й код мiй не запрацюе без нього
# код внuзу це моi функцii та iнше - що е моim обов'язком у цьому проектi
# як працюе функцii i як з ними працювати - я написав бiля коду

# функцiя що малюе поле
def board_draw(canvas):
    size = int(canvas["width"])
    cell = size // 3
    # Горизонтальнi линii
    for i in range(1, 3):
        canvas.create_line(0, i*cell, size, i*cell)
    # Вертикальнi линii
    for i in range(1, 3):
        canvas.create_line(i*cell, 0, i*cell, size)

board_draw(canvas) #як визвати функцию та намалювати поле
# зараз не працюе тому що нема коду що створюе холст, ним вроде як займатся хтось iнший
# код пример з яким вiн може запрацювати (такий код ставиться у самому верху):
def board_clear(canvas):
    # Очищаемо холст вiD ходiB
    canvas.delete("all")
    board_draw(canvas)

