import customtkinter as ctk
from tkinter import filedialog, messagebox
import sankhya_generator
import os
import time
import threading
import subprocess
import platform
import json
import sys

# Set theme
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

CONFIG_FILE = "config.json"

class SankhyaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("CardFlow")
        window_width = 800
        window_height = 450
        
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate center position
        center_x = int((screen_width / 2) - (window_width / 2))
        center_y = int((screen_height / 2) - (window_height / 2))
        
        self.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.resizable(False, False)

        # Grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Title
        self.label_title = ctk.CTkLabel(self, text="Gerador de Arquivo de Retorno de Cartão de Crédito", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Description
        self.label_desc = ctk.CTkLabel(self, text="Selecione o arquivo CSV para converter", font=ctk.CTkFont(size=14))
        self.label_desc.grid(row=1, column=0, padx=20, pady=(0, 20))

        # File Selection Frame
        self.frame_file = ctk.CTkFrame(self)
        self.frame_file.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.frame_file.grid_columnconfigure(0, weight=1)

        self.entry_path = ctk.CTkEntry(self.frame_file, placeholder_text="Nenhum arquivo selecionado...")
        self.entry_path.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="ew")

        self.btn_browse = ctk.CTkButton(self.frame_file, text="Selecionar CSV", command=self.browse_file)
        self.btn_browse.grid(row=0, column=1, padx=(0, 20), pady=20)

        # Progress Bar (Initially hidden or empty)
        self.progress_bar = ctk.CTkProgressBar(self, mode="determinate")
        self.progress_bar.grid(row=3, column=0, padx=20, pady=(10, 0), sticky="ew")
        self.progress_bar.set(0)
        self.progress_bar.grid_remove() # Hide initially

        # Generate Button
        self.btn_generate = ctk.CTkButton(self, text="Gerar Arquivo", command=self.start_generation, state="disabled", height=50, font=ctk.CTkFont(size=16, weight="bold"))
        self.btn_generate.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="ew")

        # Action Buttons Frame (Initially hidden)
        self.frame_actions = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_actions.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        self.frame_actions.grid_columnconfigure((0, 1), weight=1)
        self.frame_actions.grid_remove()

        self.btn_open_file = ctk.CTkButton(self.frame_actions, text="Abrir Arquivo", command=self.open_file, fg_color="green")
        self.btn_open_file.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.btn_open_folder = ctk.CTkButton(self.frame_actions, text="Abrir Pasta", command=self.open_folder, fg_color="gray")
        self.btn_open_folder.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Footer
        self.label_footer = ctk.CTkLabel(self, text="v2.3 - Output Local", font=ctk.CTkFont(size=10), text_color="gray")
        self.label_footer.grid(row=6, column=0, pady=(0, 10))

        self.file_path = None
        self.output_path = None
        self.last_dir = self.load_config()

    def get_app_path(self):
        if getattr(sys, 'frozen', False):
            # Running as compiled exe
            return os.path.dirname(sys.executable)
        else:
            # Running as script
            return os.path.dirname(os.path.abspath(__file__))

    def load_config(self):
        try:
            config_path = os.path.join(self.get_app_path(), CONFIG_FILE)
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    data = json.load(f)
                    return data.get("last_dir", "/")
        except:
            pass
        return "/"

    def save_config(self, directory):
        try:
            config_path = os.path.join(self.get_app_path(), CONFIG_FILE)
            with open(config_path, 'w') as f:
                json.dump({"last_dir": directory}, f)
        except:
            pass

    def browse_file(self):
        initial_dir = self.last_dir if os.path.exists(self.last_dir) else "/"
        
        file_path = filedialog.askopenfilename(
            title="Selecione o arquivo CSV",
            initialdir=initial_dir,
            filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")]
        )
        if file_path:
            self.file_path = file_path
            self.entry_path.delete(0, "end")
            self.entry_path.insert(0, file_path)
            self.btn_generate.configure(state="normal")
            
            # Save directory
            directory = os.path.dirname(file_path)
            self.last_dir = directory
            self.save_config(directory)

            # Reset UI state
            self.progress_bar.set(0)
            self.progress_bar.grid_remove()
            self.frame_actions.grid_remove()
            self.btn_generate.grid() 

    def start_generation(self):
        if not self.file_path:
            return
        
        # Disable button and show progress
        self.btn_generate.configure(state="disabled")
        self.progress_bar.grid()
        self.progress_bar.set(0)
        self.frame_actions.grid_remove()

        # Start thread
        threading.Thread(target=self.process_generation, daemon=True).start()

    def process_generation(self):
        try:
            # Simulate processing 
            steps = 100
            for i in range(steps + 1):
                time.sleep(0.02) 
                self.progress_bar.set(i / steps)
                self.update_idletasks()

            # Actual Generation
            # Output to the application directory (where the exe is)
            directory = self.get_app_path()
            self.output_path = os.path.join(directory, "retorno_cartao.txt")
            
            transactions = sankhya_generator.read_csv(self.file_path)
            
            if not transactions:
                self.root.after(0, lambda: messagebox.showwarning("Aviso", "O arquivo CSV parece estar vazio."))
                self.root.after(0, self.reset_ui)
                return

            sequencial = 1 
            sankhya_generator.generate_file(self.output_path, sequencial, transactions)
            
            # Success State
            self.after(0, self.show_success)

        except Exception as e:
            self.after(0, lambda: messagebox.showerror("Erro", f"Ocorreu um erro:\n{str(e)}"))
            self.after(0, self.reset_ui)

    def show_success(self):
        self.btn_generate.grid_remove() 
        self.frame_actions.grid() 
        self.progress_bar.set(1)

    def reset_ui(self):
        self.btn_generate.configure(state="normal")
        self.progress_bar.grid_remove()

    def open_file(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                if platform.system() == "Windows":
                    os.startfile(self.output_path)
                else:
                    subprocess.call(["open", self.output_path])
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")

    def open_folder(self):
        if self.output_path:
            folder = os.path.dirname(self.output_path)
            try:
                if platform.system() == "Windows":
                    os.startfile(folder)
                else:
                    subprocess.call(["open", folder])
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível abrir a pasta: {e}")

if __name__ == "__main__":
    app = SankhyaApp()
    app.mainloop()
