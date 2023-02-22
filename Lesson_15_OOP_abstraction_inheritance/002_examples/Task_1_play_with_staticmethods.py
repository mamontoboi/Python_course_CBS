# Створіть клас Editor, який містить методи view_document та edit_document.
# Нехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для
# безкоштовної версії. Створіть підклас ProEditor, у якому цей метод буде перевизначено.
# Введіть ліцензійний ключ із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor.
# Викликайте методи перегляду та редагування документів.

class Editor:
    @staticmethod
    def view_document():
        return "The imaginary document is opened"

    @staticmethod
    def edit_document():
        return "Editing is not supported by free version"

    def __str__(self):
        return "The new Editor was created. Editing is not allowed."


class ProEditor(Editor):
    def __str__(self):
        return "The new ProEditor was created. Editing is allowed."

    @staticmethod
    def edit_document():
        if input("Enter your licence_key: \n") == 'key':
            return object.__new__(ProEditor)
        else:
            return object.__new__(Editor)


print(ProEditor.edit_document())
print(Editor.view_document())
