import tkinter

def click_btn():
    labelE = tkinter.Label(root, text="동", font=("돋움", 24))
    labelW = tkinter.Label(root, text="서", font=("돋움", 24))
    labelN = tkinter.Label(root, text="북", font=("돋움", 24))
    labelS = tkinter.Label(root, text="남", font=("돋움", 24))

    labelE.place(x=300, y=200)
    labelW.place(x=100, y=200)
    labelN.place(x=200, y=100)
    labelS.place(x=200, y=300)

    txt = entry.get()
    str1 = txt
    labeltxt = tkinter.Label(root, text=str1, font=("돋움", 24))
    labeltxt.place(x=200, y=400)

root = tkinter.Tk()
root.title("첫 번째 윈도우")
root.geometry("800x600")

btn = tkinter.Button(root, text="버튼", font=("돋움", 10), command=click_btn)
btn.place(x=200, y=200, width=80, height=32)

entry = tkinter.Entry(root, width=20)
entry.place(x=200, y=350)

root.mainloop()


