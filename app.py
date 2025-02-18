import tkinter as tk
from tkinter import font as tkfont
import difflib

class TextDiffChecker(tk.Tk):
def __init__(self):
super().__init__()
self.title("Text Diff Checker")

# Configure the grid layout
self.grid_rowconfigure(1, weight=1)
self.grid_columnconfigure((0, 1), weight=1)

self.create_widgets()

def create_widgets(self):
# Labels
old_label = tk.Label(self, text="Old Text")
new_label = tk.Label(self, text="New Text")
diff_label = tk.Label(self, text="Differences")

old_label.grid(row=0, column=0, padx=5, pady=5)
new_label.grid(row=0, column=1, padx=5, pady=5)
diff_label.grid(row=0, column=2, padx=5, pady=5)

# Text areas
self.old_text = tk.Text(self, wrap=tk.WORD)
self.new_text = tk.Text(self, wrap=tk.WORD)
self.diff_text = tk.Text(self, wrap=tk.WORD, state='disabled', bg="#f0f0f0")

self.old_text.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
self.new_text.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
self.diff_text.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

# Button for checking differences
check_button = tk.Button(self, text="Check Differences", command=self.show_differences)
check_button.grid(row=2, columnspan=3, pady=10)

def show_differences(self):
# Get input texts
old_text_content = self.old_text.get("1.0", tk.END).strip()
new_text_content = self.new_text.get("1.0", tk.END).strip()

# Initialize SequenceMatcher
sequence_matcher = difflib.SequenceMatcher(None, old_text_content, new_text_content)

self.diff_text.configure(state='normal')
self.diff_text.delete('1.0', tk.END) # Clear previous differences

# Process matches and differences
for tag, i1, i2, j1, j2 in sequence_matcher.get_opcodes():
if tag == 'equal':
self.diff_text.insert(tk.END, old_text_content[i1:i2])
elif tag == 'replace':
self.diff_text.insert(tk.END, old_text_content[i1:i2], 'old')
self.diff_text.insert(tk.END, new_text_content[j1:j2], 'new')
elif tag == 'delete':
self.diff_text.insert(tk.END, old_text_content[i1:i2], 'old')
elif tag == 'insert':
self.diff_text.insert(tk.END, new_text_content[j1:j2], 'new')

self.diff_text.configure(state='disabled') # Make text read-only

# Tag configurations for styling
self.diff_text.tag_config('old', foreground='red', font=tkfont.Font(weight='bold'))
self.diff_text.tag_config('new', foreground='green', font=tkfont.Font(weight='bold'))


if __name__ == "__main__":
app = TextDiffChecker()
app.geometry("1200x600")
app.mainloop()
