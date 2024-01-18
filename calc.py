import tkinter as tk

class exprTree:
    def __init__(self, expr : str = ""):
        self.left = None
        self.right = None
        self.operator = None
        self.value = None
        if expr != "":
            self.__BuildTree(expr)
    def __BuildTree(self, expr : str, trimmed : bool = False):
        if not trimmed:
            expr = expr.replace(" ", "")

        operatorFound, idx, removeCount = self.__FindLastOperator(expr)
        for _ in range(removeCount):
            expr = expr.removeprefix("(").removesuffix(")")
        if operatorFound:
            self.operator = expr[idx - removeCount]
            leftexpr = expr[0:idx - removeCount]
            rightexpr = expr[idx - removeCount+1:]
            self.left = exprTree(leftexpr)
            self.right = exprTree(rightexpr)
        else:
            self.value = expr
    def __FindLastOperator(self, expr : str):
        operators = {
            "^":1,
            "*":2,
            "/":2,
            "+":3,
            "-":3
            }
        idx = -1
        val = 0 
        scopeDepth = 0
        minScpoeDepth = 10000000000

        depth = 0
        for i in range(len(expr)):
            if expr[i] == "(":
                depth+=1
            elif expr[i] == ")":
                depth-=1
            elif minScpoeDepth > depth:
                minScpoeDepth = depth  
                    
        for i in range(len(expr)):
            if expr[i] == "(":
                scopeDepth+=1
            elif expr[i] == ")":
                scopeDepth-=1
            if scopeDepth == minScpoeDepth:
                try:
                    if operators[expr[i]] > val:
                        val = operators[expr[i]]
                        idx = i
                except:
                    pass
        if idx != -1:
            return True, idx, minScpoeDepth
        else:
            return False, -1, minScpoeDepth
    def DebugPrint(self, depth = 0):
        if  self.operator:
            print((depth * " ") + str(self.operator))
            if self.left:
                self.left.DebugPrint(depth+1)
            if self.right:
                self.right.DebugPrint(depth+1)
        elif self.value:
            print((depth * " ") + self.value)
    def Evaluate(self):
        if self.operator:
            left = self.left.Evaluate()
            right = self.right.Evaluate()

            if self.operator == "^":
                return left ** right
            elif self.operator == "*":
                return left * right
            elif self.operator == "/":
                return left / right
            elif self.operator == "+":
                return left + right
            elif self.operator == "-":
                return left - right
        else:
            return float(self.value)

def calc(expression : str):
    return exprTree(expression).Evaluate()

class App:
    def __init__(self) -> None:

        fg = "#e0e0e0"
        bg = "#404040"

        self.root = tk.Tk()
        self.root.title("Angelo's Calculator")
        self.frame = tk.Frame(self.root,bg="#000000")
        self.frame.grid()
        self.entry = tk.Entry(self.frame,width=16,border=2,fg=fg,bg=bg,font=("default", 25))
        self.entry2 = tk.Entry(self.frame,width=16,border=2,fg=fg,bg=bg,font=("default", 25))
        self.entry.grid(column=0,row=0,columnspan=4,pady=2)
        self.entry2.grid(column=0,row=1,columnspan=4)
        self.entry2.insert(0,"Resault")

        tk.Button(self.frame,text="1",command=self.__OnClick1,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=0,row=4)
        tk.Button(self.frame,text="2",command=self.__OnClick2,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=1,row=4)
        tk.Button(self.frame,text="0",command=self.__OnClick0,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=0,row=5)
        tk.Button(self.frame,text="3",command=self.__OnClick3,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=2,row=4)
        tk.Button(self.frame,text="4",command=self.__OnClick4,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=0,row=3)
        tk.Button(self.frame,text="5",command=self.__OnClick5,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=1,row=3)
        tk.Button(self.frame,text="6",command=self.__OnClick6,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=2,row=3)
        tk.Button(self.frame,text="7",command=self.__OnClick7,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=0,row=2)
        tk.Button(self.frame,text="8",command=self.__OnClick8,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=1,row=2)
        tk.Button(self.frame,text="9",command=self.__OnClick9,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=2,row=2)
        tk.Button(self.frame,text="+",command=self.__OnClickA,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=3,row=2)
        tk.Button(self.frame,text="-",command=self.__OnClickS,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=3,row=3)
        tk.Button(self.frame,text="*",command=self.__OnClickM,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=3,row=4)
        tk.Button(self.frame,text="/",command=self.__OnClickD,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=3,row=5)
        tk.Button(self.frame,text=".",command=self.__OnClickDot,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=1,row=5)
        tk.Button(self.frame,text="^",command=self.__OnClickPow,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=2,row=5)
        tk.Button(self.frame,text="(",command=self.__OnClickOB,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=0,row=6)
        tk.Button(self.frame,text=")",command=self.__OnClickCB,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=1,row=6)
        tk.Button(self.frame,text="C",command=self.__OnClickC,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=2,row=6)
        tk.Button(self.frame,text="=",command=self.__OnClickEqual,width=9,height=3,border=2,fg=fg,bg=bg).grid(column=3,row=6)

    def __OnClick0(self):
        self.entry.insert(self.entry.index(tk.INSERT),"0")
    def __OnClick1(self):
        self.entry.insert(self.entry.index(tk.INSERT),"1")
    def __OnClick2(self):
        self.entry.insert(self.entry.index(tk.INSERT),"2")
    def __OnClick3(self):
        self.entry.insert(self.entry.index(tk.INSERT),"3")
    def __OnClick4(self):
        self.entry.insert(self.entry.index(tk.INSERT),"4")
    def __OnClick5(self):
        self.entry.insert(self.entry.index(tk.INSERT),"5")
    def __OnClick6(self):
        self.entry.insert(self.entry.index(tk.INSERT),"6")
    def __OnClick7(self):
        self.entry.insert(self.entry.index(tk.INSERT),"7")
    def __OnClick8(self):
        self.entry.insert(self.entry.index(tk.INSERT),"8")
    def __OnClick9(self):
        self.entry.insert(self.entry.index(tk.INSERT),"9")
    def __OnClickA(self):
        self.entry.insert(self.entry.index(tk.INSERT),"+")
    def __OnClickS(self):
        self.entry.insert(self.entry.index(tk.INSERT),"-")
    def __OnClickM(self):
        self.entry.insert(self.entry.index(tk.INSERT),"*")
    def __OnClickD(self):
        self.entry.insert(self.entry.index(tk.INSERT),"/")
    def __OnClickPow(self):
        self.entry.insert(self.entry.index(tk.INSERT),"^")
    def __OnClickDot(self):
        self.entry.insert(self.entry.index(tk.INSERT),".")
    def __OnClickOB(self):
        self.entry.insert(self.entry.index(tk.INSERT),"(")
    def __OnClickCB(self):
        self.entry.insert(self.entry.index(tk.INSERT),")")
    def __OnClickC(self):
        self.entry.delete(0,self.entry.index(tk.END))
        self.entry2.delete(0,self.entry2.index(tk.END))
        self.entry2.insert(0,"Resault")
    def __OnClickEqual(self):
        self.entry2.delete(0,self.entry2.index(tk.END))
        try:
            self.entry2.insert(0,calc(self.entry.get()))
        except Exception as e:
            self.entry2.insert(0,"error")
    def Run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.Run()