import tkinter as tk
import operaçoes

janela=tk.Tk()
janela.title('Calculadora')
janela.geometry('300x450')

numero1=''
operacao=''
numero2=''

def clicar(numero):
    global numero1
    global numero2

    visor.config(state=tk.NORMAL)

    visor.insert(tk.END,numero)

    if operacao=='':
        numero1+=numero

    else:
        numero2+=numero

    visor.config(state=tk.DISABLED)

def escolher_operacao(operacoes):
    global operacao
    visor.config(state=tk.NORMAL)

    if operacao!='':
        pass

    else:
        operacao=operacoes
        visor.insert(tk.END,operacao)
    visor.config(state=tk.DISABLED)

def deletar_tudo():
    global numero1
    global numero2
    global operacao

    visor.config(state=tk.NORMAL)
    visor.delete(0,tk.END)

    numero1=''
    numero2=''
    operacao=''

    visor.config(state=tk.DISABLED)

def deletar_ultimo_numero():
    global numero1
    global numero2
    global operacao

    visor.config(state=tk.NORMAL)
    ultimo=len(visor.get())-1
    visor.delete(ultimo,tk.END)

    visor.config(state=tk.DISABLED)

def resultado(x,y):
    global numero1
    global numero2
    global operacao

    visor.config(state=tk.NORMAL)

    if operacao=='+':
        visor.delete(0,tk.END)
        resultado=operaçoes.soma(int(x),int(y))
        visor.insert(tk.END,str(resultado))

    elif operacao=='-':
        visor.delete(0,tk.END)
        resultado=operaçoes.subtrair(int(x),int(y))
        visor.insert(tk.END,str(resultado))

    elif operacao=='x':
        visor.delete(0,tk.END)
        resultado=operaçoes.multiplicar(int(x),int(y))
        visor.insert(tk.END,str(resultado))

    elif operacao=='÷':
        visor.delete(0,tk.END)
        resultado=operaçoes.dividir(int(x),int(y))
        visor.insert(tk.END,str(resultado))

    numero1=resultado
    operacao =''
    numero2=''


    visor.config(state=tk.DISABLED)

visor=tk.Entry(janela,state=tk.DISABLED,font=('Arial',20),justify='right',disabledbackground='white',disabledforeground='black')
visor.place(relx=0.05,rely=0.15,relwidth=0.9,relheight=0.12)
botoes=tk.Frame(janela)
botoes.place(relx=0.05,rely=0.30,relwidth=0.9,relheight=0.65)
for i in range(4):
    botoes.grid_columnconfigure(i,weight=1)

for i in range(5):
    botoes.grid_rowconfigure(i,weight=1)

botaoC=tk.Button(botoes,text='C',font=('Arial',18),bg='red',fg='white',command=lambda:deletar_tudo())
botaoC.grid(row=0,column=0,sticky='nsew')

botaodelete=tk.Button(botoes,text='⌫',font=('Arial',18),bg='red',fg='white',command=lambda:deletar_ultimo_numero())
botaodelete.grid(row=0,column=1,sticky='nsew')

botaoporcentagem=tk.Button(botoes,text='%',font=('Arial',18),bg='orange',fg='white')
botaoporcentagem.grid(row=0,column=2,sticky='nsew')

botaodivisao=tk.Button(botoes,text='÷',font=('Arial',18),bg='orange',fg='white',command=lambda:escolher_operacao('÷'))
botaodivisao.grid(row=0,column=3,sticky='nsew')

botao7=tk.Button(botoes,text='7',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('7'))
botao7.grid(row=1,column=0,sticky='nsew')

botao8=tk.Button(botoes,text='8',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('8'))
botao8.grid(row=1,column=1,sticky='nsew')

botao9=tk.Button(botoes,text='9',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('9'))
botao9.grid(row=1,column=2,sticky='nsew')

botaomulti=tk.Button(botoes,text='x',font=('Arial',18),bg='orange',fg='white',command=lambda:escolher_operacao('x'))
botaomulti.grid(row=1,column=3,sticky='nsew')

botao4=tk.Button(botoes,text='4',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('4'))
botao4.grid(row=2,column=0,sticky='nsew')

botao5=tk.Button(botoes,text='5',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('5'))
botao5.grid(row=2,column=1,sticky='nsew')

botao6=tk.Button(botoes,text='6',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('6'))
botao6.grid(row=2,column=2,sticky='nsew')

botaosubtrair=tk.Button(botoes,text='-',font=('Arial',18),bg='orange',fg='white',command=lambda:escolher_operacao('-'))
botaosubtrair.grid(row=2,column=3,sticky='nsew')

botao1=tk.Button(botoes,text='1',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('1'))
botao1.grid(row=3,column=0,sticky='nsew')

botao2=tk.Button(botoes,text='2',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('2'))
botao2.grid(row=3,column=1,sticky='nsew')

botao3=tk.Button(botoes,text='3',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('3'))
botao3.grid(row=3,column=2,sticky='nsew')

botaosoma=tk.Button(botoes,text='+',font=('Arial',18),bg='orange',fg='white',command=lambda:escolher_operacao('+'))
botaosoma.grid(row=3,column=3,sticky='nsew')

botao0=tk.Button(botoes,text='0',font=('Arial',18),bg='white',fg='black',command=lambda:clicar('0'))
botao0.grid(row=4,column=0,sticky='nsew')

botaodecimal=tk.Button(botoes,text='.',font=('Arial',18),bg='orange',fg='white')
botaodecimal.grid(row=4,column=1,sticky='nsew')

botaoduasoperacoes=tk.Button(botoes,text='+/-',font=('Arial',18),bg='orange',fg='white')
botaoduasoperacoes.grid(row=4,column=2,sticky='nsew')

botaoigual=tk.Button(botoes,text='=',font=('Arial',18),bg='orange',fg='white',command=lambda:resultado(numero1,numero2))
botaoigual.grid(row=4,column=3,sticky='nsew')




janela.mainloop()