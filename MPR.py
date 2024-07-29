import tkinter as tcl
from tkinter import filedialog
from difflib import SequenceMatcher

def choose_file1():
    file_path = filedialog.askopenfilename()
    file_button1.config(text=file_path)

def choose_file2():
    file_path = filedialog.askopenfilename()
    file_button2.config(text=file_path)

def check_plagiarism():
    global plagiarised_text
    file_path1 = file_button1.cget("text")
    file_path2 = file_button2.cget("text")

    if file_path1 == "Choose File" or file_path2 == "Choose File":
        result_label.config(text="Error!\nPlease select the files to check for plagiarism.", fg="red")
    else:
        with open(file_path1, "r") as f:
            text1 = f.read()

        with open(file_path2, "r") as f:
            text2 = f.read()


        seqMatch = SequenceMatcher(None, text1, text2)
        match = seqMatch.find_longest_match(0, len(text1), 0, len(text2))
        ratio = (match.size * 2) / (len(text1) + len(text2)) * 100

        if ratio > 1.0:
            result_label.config(text="Plagiarism detected!\nSimilarity : {:.2f}".format(ratio)+"%", fg=result_color)

            def display_plagiarised_text():
                window = tcl.Toplevel(root)
                window.title("Plagiarised Text")
                window.geometry("500x400")
                window.config(bg=bg_color)

                text_label = tcl.Label(window, text="PLAGIARISED TEXT", font=("SF Pro Display Black", 16), fg=text_color, bg=bg_color)
                text_label.pack(pady=10)

                matches = SequenceMatcher(None, text1, text2).get_matching_blocks()
                plagiarised_text = ''
                for match in matches:
                    if match.size > 0:
                        plagiarised_text += text1[match.a: match.a + match.size] + '\n\n'

                if plagiarised_text:
                    text_box = tcl.Text(window, font=("SF Pro Text Regular", 12), bg="#DDD1AE", fg=bg_color)
                    text_box.insert(tcl.END, plagiarised_text)
                    text_box.pack(fill=tcl.BOTH, expand=True, padx=10, pady=10)
                else:
                    no_plagiarism_label = tcl.Label(window, text="No plagiarism detected!", font=("SF Pro Display Black", 14), fg=text_color, bg=bg_color)
                    no_plagiarism_label.pack(pady=50)


            display_button = tcl.Button(root, text="Display Plagiarised Text", font=("JetBrains Mono", 12), bg=highlight_color, fg=button_color, command=display_plagiarised_text)
            display_button.pack(pady=10)

        else:
            result_label.config(text="No plagiarism detected!\nSimilarity : {:.2f}".format(ratio)+"%", fg=text_color)



root = tcl.Tk()
root.title("Plagiarism Checker")
root.geometry("800x600")
root.resizable(True, True)

bg_color = "#00224E"
highlight_color = "#A94915"
button_color = "WHITE"
text_color = "#DDD1AE"
result_color = "#4ADB16"

root.config(bg=bg_color)

heading_label = tcl.Label(root, text="PLAGIARISM CHECKER", font=("SF Pro Display Black", 20), fg="WHITE", pady=20, bg="#001A38")
heading_label.pack(fill=tcl.X)

file_label1 = tcl.Label(root, text="Select original file:", font=("JetBrains Mono", 12), fg=text_color, pady=10, bg=bg_color)
file_label1.pack(padx=10)

file_button1 = tcl.Button(root, text="Choose File", font=("JetBrains Mono", 12), bg=highlight_color, fg=button_color, command=choose_file1)
file_button1.pack(padx=10, ipadx=10)

file_label2 = tcl.Label(root, text="Select file to compare with:", font=("JetBrains Mono", 12), fg=text_color, pady=10, bg=bg_color)
file_label2.pack(padx=10)

file_button2 = tcl.Button(root, text="Choose File", font=("JetBrains Mono", 12), bg=highlight_color, fg=button_color, command=choose_file2)
file_button2.pack(padx=10, ipadx=10)

check_button = tcl.Button(root, text="Check for plagiarism", font=("JetBrains Mono", 12), bg=highlight_color, fg=button_color, command=check_plagiarism)
check_button.pack(pady=20, ipadx=10)

result_label = tcl.Label(root, text="", font=("JetBrains Mono ExtraBold", 16), fg=text_color, bg=bg_color)
result_label.pack(pady=20)

footer_label = tcl.Label(root, text="Plagiarism-checker BY P.V.Rahul Chandra", font=("SF Pro Display", 12), fg="WHITE", pady=5, bg="#2F5061")
footer_label.pack(fill=tcl.X, side=tcl.BOTTOM)


root.mainloop()
