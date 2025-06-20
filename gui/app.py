import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import messagebox, filedialog
from scanner.core import NmapScanner
from scanner.report import generate_json_report


class VulnScannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🔍 Nmap Vuln Scanner - GUI")

        tk.Label(root, text="Cible (IP ou réseau) :", font=("Arial", 12)).pack(pady=5)
        self.target_entry = tk.Entry(root, width=40)
        self.target_entry.pack()

        tk.Label(root, text="Plage de ports (ex: 20-100) :", font=("Arial", 12)).pack(pady=5)
        self.ports_entry = tk.Entry(root, width=40)
        self.ports_entry.insert(0, "22-100")
        self.ports_entry.pack()

        tk.Label(root, text="Fichier de sortie JSON :", font=("Arial", 12)).pack(pady=5)
        self.output_entry = tk.Entry(root, width=30)
        self.output_entry.pack()
        tk.Button(root, text="Parcourir", command=self.choose_output).pack(pady=5)

        tk.Button(root, text="Démarrer le Scan", command=self.run_scan, bg="green", fg="white").pack(pady=10)

        self.result_box = tk.Text(root, height=10, width=60)
        self.result_box.pack(pady=10)

    def choose_output(self):
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, path)

    def run_scan(self):
        target = self.target_entry.get().strip()
        ports = self.ports_entry.get().strip()
        output = self.output_entry.get().strip() or "report.json"

        if not target:
            messagebox.showerror("Erreur", "Veuillez entrer une cible valide.")
            return

        scanner = NmapScanner()
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, f"[+] Scan en cours sur {target}:{ports}...\n")

        try:
            raw_data = scanner.scan_target(target, ports)
            generate_json_report(scanner.scanner.scan(), output)
            self.result_box.insert(tk.END, f"\n[+] Rapport généré dans : {output}")
            messagebox.showinfo("Succès", f"Scan terminé ! Rapport sauvegardé dans {output}")
        except Exception as e:
            self.result_box.insert(tk.END, f"\n[-] Erreur : {str(e)}")
            messagebox.showerror("Erreur", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = VulnScannerGUI(root)
    root.mainloop()