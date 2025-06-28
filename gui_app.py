# -*- coding: utf-8 -*-
import customtkinter as ctk
import os
import subprocess
from tkinter import filedialog, messagebox

class FolderColorChangerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Folder Color Changer')
        self.geometry("500x250")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # Folder selection
        self.folder_frame = ctk.CTkFrame(self)
        self.folder_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        self.folder_frame.grid_columnconfigure(0, weight=1)

        self.folder_path_input = ctk.CTkEntry(self.folder_frame, placeholder_text="Select folder path")
        self.folder_path_input.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")

        self.browse_button = ctk.CTkButton(self.folder_frame, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=0, column=1, padx=(5, 10), pady=10)

        # Color selection
        self.color_frame = ctk.CTkFrame(self)
        self.color_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.color_frame.grid_columnconfigure(0, weight=1)

        self.color_label = ctk.CTkLabel(self.color_frame, text="Select Color:")
        self.color_label.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="w")

        self.colors = {
            "red": "#FF3B30",
            "orange": "#FF9500",
            "yellow": "#FFCC00",
            "green": "#34C759",
            "blue": "#007AFF",
            "purple": "#AF52DE",
            "gray": "#8E8E93",
            "white": "#FFFFFF" # For 'none' option, use white or a neutral color
        }
        self.selected_color = "red" # Default selected color

        self.color_buttons = []
        col = 1
        for color_name, hex_code in self.colors.items():
            button = ctk.CTkButton(self.color_frame, text="", width=30, height=30, fg_color=hex_code, command=lambda name=color_name: self.select_color(name))
            button.grid(row=0, column=col, padx=2, pady=2)
            self.color_buttons.append(button)
            col += 1

        self.update_color_selection_ui() # Highlight initial selection

        # Action buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        self.apply_button = ctk.CTkButton(self.button_frame, text="Apply Color", command=self.apply_color)
        self.apply_button.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")

        self.remove_button = ctk.CTkButton(self.button_frame, text="Remove Icon", command=self.remove_icon)
        self.remove_button.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="ew")

        # Status label
        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path_input.delete(0, ctk.END)
            self.folder_path_input.insert(0, folder_path)

    def select_color(self, color_name):
        self.selected_color = color_name
        self.update_color_selection_ui()

    def update_color_selection_ui(self):
        for i, (color_name, hex_code) in enumerate(self.colors.items()):
            if color_name == self.selected_color:
                self.color_buttons[i].configure(border_color="blue", border_width=2) # Highlight selected color
            else:
                self.color_buttons[i].configure(border_width=0) # Remove highlight

    def run_script(self, action):
        folder_path = self.folder_path_input.get()
        if not folder_path:
            messagebox.showwarning("Error", "Please select a folder.")
            return

        script_path = os.path.join(os.path.dirname(__file__), "color-folder.sh")
        
        if action == "apply":
            color_name = self.selected_color
            command = [script_path, folder_path, color_name]
        elif action == "remove":
            command = [script_path, folder_path, "none"]
        else:
            return

        try:
            process = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8', errors='replace')
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error executing script:\n{e.stderr.strip()}")
        except FileNotFoundError:
            messagebox.showerror("Error", "color-folder.sh script not found. Please ensure it is in the same directory as gui_app.py.")
        except Exception as e:
            messagebox.showerror("Error", f"An unknown error occurred:\n{e}")

    def apply_color(self):
        self.run_script("apply")

    def remove_icon(self):
        self.run_script("remove")

if __name__ == '__main__':
    ctk.set_appearance_mode("Light")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

    app = FolderColorChangerApp()
    app.mainloop()