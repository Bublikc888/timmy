import tkinter as tk

current_expression= ''
def on_button_click(button):
    global current_expression

    if button == 'C':
       current_expression =''
       display.delete(0,tk.END)

    elif button =='=':
        try:
            result= eval(current_expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_expression= str(result)
          
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, 'Помилка')
            current_expression =''
    else:
            current_expression += str(button)
            display.delete(0, tk.END)
            display.insert(0, current_expression)

def set_theme(theme):
    if theme =='ligth':
        root.config(bg='white')
        display.config(bg = 'ligthgray',fg = 'black')
    elif theme=='dark':
        root.config(bg='black')
        display.config(bg= 'gray', fg = 'white')
    for button in button:
        button.config(bg='ligth'if theme == 'ligth' else 'darkgray' if theme == 'dark' else 'ligthblue',
                       fg='black' if theme !='dark' else ' white') 

root= tk.Tk()
root.title('Калькулятор')
root.geometry('400x600')

display = tk.Entry(root, font=('Arial', 24), justify="right" )
display.grid(row=0, columnspan=4, padx=10, pady= 10 )

buttons= []
button_texts = [
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'C', '0', '=', '+'
] 

row_val= 1
col_val= 0

for text in button_texts:

    button= tk.Button(root, text=text, font=('Arial', 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val +=1
    if col_val> 3:
        col_val= 0
        row_val +=1

menubar= tk.Menu(root)
theme_menu= tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label='Світла тема', command=lambda: set_theme('ligth'))
theme_menu.add_command(label='Темна тема', command=lambda: set_theme('dark'))
menubar.add_cascade(label='Налаштування', menu=theme_menu)
root.config(menu=menubar)
root.mainloop()