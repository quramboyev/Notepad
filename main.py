import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button
from warnings import simplefilter


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Bush`s блокнот")
        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')


        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        self.save_button: Button = Button(self.button_frame, text='Сохранить', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)


        self.load_button: Button = Button(self.button_frame, text='Загрузить файл', command=self.load_file)
        self.load_button.pack(side=tk.RIGHT)

    def save_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Текстовые файлы', '*.txt')])

        with open(file_path, 'w') as file:
            file.write(self.text_area.get(1.0, tk.END))

        print(f'Файл сохранен в: {file_path}')

    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Текстовые файлы', '*.txt')])

        with open(file_path, 'r') as file:
            content: str = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.INSERT, content)
        print(f"Файл загружен из: {file_path}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()

if __name__ == '__main__':
    main()
