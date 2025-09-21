import tkinter as tk
from tkinter import ttk, messagebox
from Neighbourhood_Analyzer import neighborhood_data, neighborhood_vibe


class VibeAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🏡 Real Estate Neighborhood Vibe Analyzer")
        self.state('zoomed')  # Maximize window on start (Windows)
        self.configure(bg="#f5f5f5")
        self.resizable(True, True)

        # Header
        header = tk.Label(self, text="Find Your Perfect Neighborhood!", font=("Segoe UI", 20, "bold"), fg="#2e4053", bg="#f5f5f5")
        header.pack(pady=(20, 10))

        # Sub-header
        subheader = tk.Label(self, text="Select a locality to discover its vibe, score, and highlights.", font=("Segoe UI", 12), fg="#34495e", bg="#f5f5f5")
        subheader.pack(pady=(0, 20))

        # Dropdown
        dropdown_frame = tk.Frame(self, bg="#f5f5f5")
        dropdown_frame.pack(pady=5)
        tk.Label(dropdown_frame, text="Neighborhood:", font=("Segoe UI", 13), bg="#f5f5f5").pack(side=tk.LEFT, padx=(0, 10))
        self.neighborhood_var = tk.StringVar()
        self.dropdown = ttk.Combobox(dropdown_frame, textvariable=self.neighborhood_var, font=("Segoe UI", 13), width=20)
        self.dropdown['values'] = list(neighborhood_data.keys())
        self.dropdown.pack(side=tk.LEFT)

        # Analyze Button
        self.analyze_btn = tk.Button(self, text="Analyze Vibe", command=self.show_vibe, font=("Segoe UI", 13, "bold"), bg="#27ae60", fg="white", activebackground="#229954", activeforeground="white", relief=tk.RAISED, bd=3)
        self.analyze_btn.pack(pady=20)

        # Results Frame
        self.result_frame = tk.Frame(self, bg="#f5f5f5", bd=2, relief=tk.GROOVE)
        self.result_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        # Scrollable Text Output
        self.result_scrollbar = tk.Scrollbar(self.result_frame, orient=tk.VERTICAL)
        self.result_text = tk.Text(
            self.result_frame,
            font=("Segoe UI", 14, "bold"),
            fg="#2e4053",
            bg="#f5f5f5",
            wrap=tk.WORD,
            height=12,
            yscrollcommand=self.result_scrollbar.set,
            relief=tk.FLAT,
            bd=0
        )
        self.result_scrollbar.config(command=self.result_text.yview)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Footer
        footer = tk.Label(self, text="Powered by Info Edge (India) Ltd | Data is simulated for demo purposes", font=("Segoe UI", 9), fg="#7f8c8d", bg="#f5f5f5")
        footer.pack(side=tk.BOTTOM, pady=8)

    def show_vibe(self):
        neighborhood = self.neighborhood_var.get()
        if not neighborhood:
            messagebox.showwarning("Input Required", "Please select a neighborhood.")
            return
        result = neighborhood_vibe(neighborhood)
        # Display output in the scrollable Text widget
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = VibeAnalyzerApp()
    app.mainloop()
