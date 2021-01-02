import tkinter as tk
equationCreator = [[]]
inputTemp = ""
global x
x=0
displayText = "..."
def equationCompiler(num):#adds values from button presses to the list equation creator.
    inputDisplay.configure(text=equationCreator[0])
    global x
    if [] in equationCreator:
        x = equationCreator.index([])
    if str(num).isnumeric() == True or str(num) == ".":
        equationCreator[x].append(num)
    elif str(num) == "=":
        equationCompactor(equationCreator)
    else:
        if equationCreator[-1] == []:
            equationCreator[x].append(num)
            x+=1
            equationCreator.append([])
        else:
            x+=1
            equationCreator.append([num])
            x+=1
            equationCreator.append([])

def equationCompactor(equationCreator):#turns list of indexes with one value per index into lists of numbers and operators.
    a=0
    tempEquation = ""
    for i in equationCreator:
        if len(i) > 1:
            for x in equationCreator[a]:
                tempEquation += str(x)
                equationCreator[a] = [tempEquation]
        a+=1
        tempEquation = ""
    resultGenerator(equationCreator, "/")
    resultGenerator(equationCreator, "*")
    resultGenerator(equationCreator, "+")
    resultGenerator(equationCreator, "-")

def resultGenerator(equationCreator, operator):#performs the actual maths in the form of bidmas on the equation created in equation compactor/compiler.
    a = 0
    for i in equationCreator:
        if i == [operator]:
            if operator == "/":
                equationCreator[a][0] = float(equationCreator[a-1][0]) / float(equationCreator[a+1][0])
            elif operator == "*":
                equationCreator[a][0] = float(equationCreator[a-1][0]) * float(equationCreator[a+1][0])
            elif operator == "+":
                equationCreator[a][0] = float(equationCreator[a-1][0]) + float(equationCreator[a+1][0])
            elif operator == "-":
                equationCreator[a][0] = float(equationCreator[a-1][0]) - float(equationCreator[a+1][0])
            equationCreator.pop(a-1)
            equationCreator.pop(a)
            resultGenerator(equationCreator, operator)
        a+=1
    inputDisplay.configure(text=equationCreator[0])

window = tk.Tk()#defines window, window size(geomety) and button information/position.
window.geometry("300x600")
window.title("Simple Calculator")
inputDisplay = tk.Label(window, text = displayText, cursor = "dot", bg="blue", fg="white", font=("Courier", 15))
inputDisplay.place(height=100, width=300, x=0, y=500)#.place needs to be seperate to allow editing of text in label, using.place immediately assigns value of none to inputdisplay so text cannot be edited.
button1 = tk.Button(window, text = "1", command = lambda: equationCompiler(1), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=0, y=0)#lambda needed as it is annonymous function, stops running on startup. try to use class in this section to compact and disable double operator inputs.
button2 = tk.Button(window, text = "2", command = lambda: equationCompiler(2), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=100, y=0)
button3 = tk.Button(window, text = "3", command = lambda: equationCompiler(3), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=200, y=0)
button4 = tk.Button(window, text = "4", command = lambda: equationCompiler(4), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=0, y=100)
button5 = tk.Button(window, text = "5", command = lambda: equationCompiler(5), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=100, y=100)
button6 = tk.Button(window, text = "6", command = lambda: equationCompiler(6), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=200, y=100)
button7 = tk.Button(window, text = "7", command = lambda: equationCompiler(7), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=0, y=200)
button8 = tk.Button(window, text = "8", command = lambda: equationCompiler(8), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=100, y=200)
button9 = tk.Button(window, text = "9", command = lambda: equationCompiler(9), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=200, y=200)
button0 = tk.Button(window, text = "0", command = lambda: equationCompiler(0), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=0, y =300)
buttonPlus = tk.Button(window, text = "+", command = lambda: equationCompiler("+"), cursor = "dot", fg="white", bg = "green", font=("Courier", 50)).place(height=100, width=100, x=200, y=300)
buttonDot = tk.Button(window, text = ".", command = lambda : equationCompiler("."), cursor = "dot", fg="white", bg = "red", font=("Courier", 50)).place(height=100, width=100, x=0, y=300)
buttonEquals = tk.Button(window, text = "=", command = lambda: equationCompiler("="), cursor ="dot", fg="white", bg = "green", font=("Courier", 50)).place(height=100, width=100, x=200, y=400)
buttonDivide = tk.Button(window, text = "/", command = lambda: equationCompiler("/"), cursor = "dot", fg="white", bg = "green", font=("Courier", 50)).place(height=100, width=100, x=0, y=400)
buttonMultiply = tk.Button(window, text = "*", command = lambda: equationCompiler("*"), cursor = "dot", fg="white", bg = "green", font=("Courier", 50)).place(height=100, width=100, x=100, y=400)
buttonMinus = tk.Button(window, text = "-", command = lambda: equationCompiler("-"), cursor = "dot", fg="white", bg = "green", font=("Courier", 50)).place(height=100, width=100, x=100, y=300)

window.mainloop()#starts the program
