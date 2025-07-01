import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

# ------------------ CONSTANTES DE ESTILO ------------------ #
PRIMARY_COLOR = "#7E57C2"
SECONDARY_COLOR = "#B39DDB"
BACKGROUND_COLOR = "#121212"
SURFACE_COLOR = "#1E1E1E"
TEXT_COLOR = "#FFFFFF"
ERROR_COLOR = "#CF6679"
ENTRY_BG = "#2D2D2D"

usuarios_cadastrados = {}

# ------------------ FUNÇÕES ------------------ #
def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == "Digite seu usuário" or senha == "Digite sua senha":
        messagebox.showerror("Erro", "Preencha todos os campos.", parent=janela)
        return
    
    if usuario in usuarios_cadastrados:
        if senha == usuarios_cadastrados[usuario]["senha"]:
            abrir_janela_bem_vinda(usuarios_cadastrados[usuario]["nome"])
        else:
            messagebox.showerror("Erro", "Senha incorreta.", parent=janela)
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.", parent=janela)

def mostrar_cadastro():
    login_frame.pack_forget()
    frame_cadastro.pack(fill="both", expand=True)
    janela.geometry("500x700")

    resetar_campos_login()

def mostrar_login():
    frame_cadastro.pack_forget()
    login_frame.pack(fill="both", expand=True)
    janela.geometry("500x650")

    resetar_campos_cadastro()

def resetar_campos_login():
    entry_usuario.delete(0, tk.END)
    entry_usuario.insert(0, "Digite seu usuário")
    entry_usuario.config(fg="#888888")
    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, "Digite sua senha")
    entry_senha.config(fg="#888888", show="")

def resetar_campos_cadastro():
    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, "Digite seu nome completo")
    entry_nome.config(fg="#888888")
    entry_novo_usuario.delete(0, tk.END)
    entry_novo_usuario.insert(0, "Escolha um nome de usuário")
    entry_novo_usuario.config(fg="#888888")
    entry_nova_senha.delete(0, tk.END)
    entry_nova_senha.insert(0, "Crie uma senha")
    entry_nova_senha.config(fg="#888888", show="")

def fazer_cadastro():
    nome = entry_nome.get()
    novo_usuario = entry_novo_usuario.get()
    nova_senha = entry_nova_senha.get()
    
    # Verifica se os campos estão com os valores padrão
    if nome == "Digite seu nome completo" or novo_usuario == "Escolha um nome de usuário" or nova_senha == "Crie uma senha":
        messagebox.showerror("Erro", "Preencha todos os campos.", parent=janela)
        return
        
    # Verifica se o usuário já existe
    if novo_usuario in usuarios_cadastrados:
        messagebox.showerror("Erro", "Nome de usuário já existe.", parent=janela)
    else:
        # Armazena o novo usuário
        usuarios_cadastrados[novo_usuario] = {
            "nome": nome,
            "senha": nova_senha
        }
        messagebox.showinfo("Cadastro", f"Usuário '{novo_usuario}' cadastrado com sucesso!", parent=janela)
        mostrar_login()

def abrir_janela_bem_vinda(nome_usuario):
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Bem-vinda!")
    nova_janela.geometry("400x200")
    nova_janela.configure(bg=BACKGROUND_COLOR)
    nova_janela.resizable(False, False)
    
    nova_janela.transient(janela)
    nova_janela.grab_set()
    
    welcome_font = Font(family="Helvetica", size=20, weight="bold")
    tk.Label(
        nova_janela, 
        text=f"Bem-vinda, {nome_usuario}!", 
        font=welcome_font, 
        fg=PRIMARY_COLOR, 
        bg=BACKGROUND_COLOR
    ).pack(expand=True)

def on_entry_click(entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, "end")
        entry.config(fg=TEXT_COLOR)
    if entry in [entry_senha, entry_nova_senha]:
        entry.config(show="*")

def on_focusout(entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.config(fg="#888888")
    if entry in [entry_senha, entry_nova_senha] and entry.get() == default_text:
        entry.config(show="")

# ------------------ JANELA PRINCIPAL ------------------ #
janela = tk.Tk()
janela.title("Login | Cadastro")
janela.geometry("500x650")
janela.configure(bg=BACKGROUND_COLOR)
janela.resizable(False, False)

# Fonte personalizada
title_font = Font(family="Helvetica", size=24, weight="bold")
label_font = Font(family="Helvetica", size=10)
entry_font = Font(family="Helvetica", size=12)
button_font = Font(family="Helvetica", size=12, weight="bold")

# ------------------ FRAME DE LOGIN ------------------ #
login_frame = tk.Frame(janela, bg=BACKGROUND_COLOR)
login_frame.pack(fill="both", expand=True, padx=40, pady=40)

# Logo/Title
tk.Label(
    login_frame,
    text="Acesso ao Sistema",
    font=title_font,
    fg=PRIMARY_COLOR,
    bg=BACKGROUND_COLOR
).pack(pady=(0, 30))

# Campo de Usuário
tk.Label(
    login_frame,
    text="Usuário",
    font=label_font,
    fg=SECONDARY_COLOR,
    bg=BACKGROUND_COLOR,
    anchor="w"
).pack(fill="x", pady=(5, 0))

entry_usuario = tk.Entry(
    login_frame,
    font=entry_font,
    bd=0,
    bg=ENTRY_BG,
    fg="#888888",
    insertbackground=TEXT_COLOR,
    highlightthickness=1,
    highlightbackground=ENTRY_BG,
    highlightcolor=PRIMARY_COLOR
)
entry_usuario.insert(0, "Digite seu usuário")
entry_usuario.bind('<FocusIn>', lambda e: on_entry_click(entry_usuario, "Digite seu usuário"))
entry_usuario.bind('<FocusOut>', lambda e: on_focusout(entry_usuario, "Digite seu usuário"))
entry_usuario.pack(fill="x", ipady=8, pady=(5, 15))

# Campo de Senha
tk.Label(
    login_frame,
    text="Senha",
    font=label_font,
    fg=SECONDARY_COLOR,
    bg=BACKGROUND_COLOR,
    anchor="w"
).pack(fill="x", pady=(5, 0))

entry_senha = tk.Entry(
    login_frame,
    font=entry_font,
    bd=0,
    bg=ENTRY_BG,
    fg="#888888",
    insertbackground=TEXT_COLOR,
    highlightthickness=1,
    highlightbackground=ENTRY_BG,
    highlightcolor=PRIMARY_COLOR
)
entry_senha.insert(0, "Digite sua senha")
entry_senha.bind('<FocusIn>', lambda e: on_entry_click(entry_senha, "Digite sua senha"))
entry_senha.bind('<FocusOut>', lambda e: on_focusout(entry_senha, "Digite sua senha"))
entry_senha.pack(fill="x", ipady=8, pady=(5, 20))

# Botão de Login
btn_login = tk.Button(
    login_frame,
    text="Entrar",
    command=fazer_login,
    font=button_font,
    bg=PRIMARY_COLOR,
    fg=TEXT_COLOR,
    activebackground=SECONDARY_COLOR,
    activeforeground=TEXT_COLOR,
    bd=0,
    relief="flat",
    padx=20,
    pady=10
)
btn_login.pack(fill="x", pady=(10, 5))

# Botão para ir para cadastro
btn_toggle = tk.Button(
    login_frame,
    text="Criar uma conta",
    command=mostrar_cadastro,
    font=label_font,
    bg=BACKGROUND_COLOR,
    fg=SECONDARY_COLOR,
    activebackground=SURFACE_COLOR,
    activeforeground=SECONDARY_COLOR,
    bd=0,
    relief="flat"
)
btn_toggle.pack(pady=(20, 0))

# ------------------ FORMULÁRIO DE CADASTRO ------------------ #
frame_cadastro = tk.Frame(janela, bg=BACKGROUND_COLOR)

# Cabeçalho com botão de voltar
header_frame = tk.Frame(frame_cadastro, bg=BACKGROUND_COLOR)
header_frame.pack(fill="x", pady=(20, 30), padx=20)

btn_voltar = tk.Button(
    header_frame,
    text="← Voltar para login",
    command=mostrar_login,
    font=label_font,
    bg=BACKGROUND_COLOR,
    fg=SECONDARY_COLOR,
    activebackground=SURFACE_COLOR,
    activeforeground=SECONDARY_COLOR,
    bd=0,
    relief="flat",
    anchor="w"
)
btn_voltar.pack(side="left")

tk.Label(
    header_frame,
    text="Criar Nova Conta",
    font=Font(family="Helvetica", size=16, weight="bold"),
    fg=PRIMARY_COLOR,
    bg=BACKGROUND_COLOR
).pack(side="left", padx=10)

# Conteúdo do cadastro
content_frame = tk.Frame(frame_cadastro, bg=BACKGROUND_COLOR)
content_frame.pack(fill="both", expand=True, padx=40)

# Campo de Nome
tk.Label(
    content_frame,
    text="Nome Completo",
    font=label_font,
    fg=SECONDARY_COLOR,
    bg=BACKGROUND_COLOR,
    anchor="w"
).pack(fill="x", pady=(5, 0))

entry_nome = tk.Entry(
    content_frame,
    font=entry_font,
    bd=0,
    bg=ENTRY_BG,
    fg="#888888",
    insertbackground=TEXT_COLOR,
    highlightthickness=1,
    highlightbackground=ENTRY_BG,
    highlightcolor=PRIMARY_COLOR
)
entry_nome.insert(0, "Digite seu nome completo")
entry_nome.bind('<FocusIn>', lambda e: on_entry_click(entry_nome, "Digite seu nome completo"))
entry_nome.bind('<FocusOut>', lambda e: on_focusout(entry_nome, "Digite seu nome completo"))
entry_nome.pack(fill="x", ipady=8, pady=(5, 15))

# Campo de Novo Usuário
tk.Label(
    content_frame,
    text="Nome de Usuário",
    font=label_font,
    fg=SECONDARY_COLOR,
    bg=BACKGROUND_COLOR,
    anchor="w"
).pack(fill="x", pady=(5, 0))

entry_novo_usuario = tk.Entry(
    content_frame,
    font=entry_font,
    bd=0,
    bg=ENTRY_BG,
    fg="#888888",
    insertbackground=TEXT_COLOR,
    highlightthickness=1,
    highlightbackground=ENTRY_BG,
    highlightcolor=PRIMARY_COLOR
)
entry_novo_usuario.insert(0, "Escolha um nome de usuário")
entry_novo_usuario.bind('<FocusIn>', lambda e: on_entry_click(entry_novo_usuario, "Escolha um nome de usuário"))
entry_novo_usuario.bind('<FocusOut>', lambda e: on_focusout(entry_novo_usuario, "Escolha um nome de usuário"))
entry_novo_usuario.pack(fill="x", ipady=8, pady=(5, 15))

# Campo de Nova Senha
tk.Label(
    content_frame,
    text="Senha",
    font=label_font,
    fg=SECONDARY_COLOR,
    bg=BACKGROUND_COLOR,
    anchor="w"
).pack(fill="x", pady=(5, 0))

entry_nova_senha = tk.Entry(
    content_frame,
    font=entry_font,
    bd=0,
    bg=ENTRY_BG,
    fg="#888888",
    insertbackground=TEXT_COLOR,
    highlightthickness=1,
    highlightbackground=ENTRY_BG,
    highlightcolor=PRIMARY_COLOR
)
entry_nova_senha.insert(0, "Crie uma senha")
entry_nova_senha.bind('<FocusIn>', lambda e: on_entry_click(entry_nova_senha, "Crie uma senha"))
entry_nova_senha.bind('<FocusOut>', lambda e: on_focusout(entry_nova_senha, "Crie uma senha"))
entry_nova_senha.pack(fill="x", ipady=8, pady=(5, 30))

# Botão de Cadastro
btn_cadastrar = tk.Button(
    content_frame,
    text="Criar Conta",
    command=fazer_cadastro,
    font=button_font,
    bg=PRIMARY_COLOR,
    fg=TEXT_COLOR,
    activebackground=SECONDARY_COLOR,
    activeforeground=TEXT_COLOR,
    bd=0,
    relief="flat",
    padx=20,
    pady=10
)
btn_cadastrar.pack(fill="x", pady=(10, 5))


janela.mainloop()