# CardFlow 💳

> **Gerador de Arquivos de Retorno para Sankhya**  
> Automatize a conciliação de cartões de crédito com uma interface moderna e eficiente.

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web-green?style=for-the-badge&logo=flask)
![CustomTkinter](https://img.shields.io/badge/Desktop-CustomTkinter-blueviolet?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

## 📋 Sobre o Projeto

O **CardFlow** é uma solução completa (Desktop e Web) desenvolvida para simplificar a geração de arquivos de retorno de cartão de crédito no padrão exigido pelo ERP **Sankhya**.

Esqueça a edição manual de arquivos de texto. Com o CardFlow, você transforma seus relatórios CSV em arquivos de importação prontos em segundos.

---

## ✨ Funcionalidades

### 🖥️ Versão Desktop
- **Interface Premium**: Design moderno estilo "Apple", limpo e intuitivo.
- **Standalone**: Executável único (`.exe`) que não requer instalação de Python.
- **Inteligente**: Lembra a última pasta utilizada.
- **Prático**: Botões rápidos para abrir o arquivo ou a pasta após a geração.

### 🌐 Versão Web
- **Acessibilidade**: Funciona em qualquer navegador (PC, Mac, Mobile).
- **Tema Dinâmico**: Suporte automático a **Dark Mode** (Modo Escuro).
- **Feedback Visual**: Barra de progresso animada e drag-and-drop.
- **Pronto para Nuvem**: Configurado para deploy fácil no Render.com.

---

## 🚀 Como Usar

### Opção 1: Desktop (Windows)
1. Baixe o arquivo `CardFlow.exe` na aba [Releases](https://github.com/thiagorochasti/cardflow/releases).
2. Execute o aplicativo.
3. Selecione seu arquivo CSV de entrada.
4. Clique em **Gerar Arquivo**.
5. O arquivo `retorno_cartao.txt` será salvo na mesma pasta do executável.

### Opção 2: Web (Navegador)
1. Acesse a versão online (se hospedada) ou rode localmente.
2. Arraste seu CSV para a área indicada.
3. Aguarde a barra de progresso.
4. O download iniciará automaticamente.

---

## 🛠️ Instalação e Desenvolvimento

Para rodar o projeto localmente e contribuir:

### Pré-requisitos
- Python 3.x instalado.
- Git instalado.

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/thiagorochasti/cardflow.git
   cd cardflow
   ```

2. **Instale as dependências**
   ```bash
   pip install customtkinter flask gunicorn
   # ou
   pip install -r web_app/requirements.txt
   ```

3. **Rodar Versão Desktop**
   ```bash
   python gui.py
   ```

4. **Rodar Versão Web**
   ```bash
   python web_app/app.py
   ```
   Acesse `http://127.0.0.1:5000` no seu navegador.

---

## 📦 Estrutura do Projeto

- `gui.py`: Código fonte da interface Desktop (CustomTkinter).
- `sankhya_generator.py`: Núcleo lógico de processamento do arquivo.
- `web_app/`: Pasta contendo toda a aplicação Web (Flask).
  - `app.py`: Servidor Web.
  - `templates/`: Arquivos HTML/CSS.
- `dist/`: Pasta onde o executável final é gerado (após compilação).

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

---

Desenvolvido com 💙 por **Thiago Rocha**.
