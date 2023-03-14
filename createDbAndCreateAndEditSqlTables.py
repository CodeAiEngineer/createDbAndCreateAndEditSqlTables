import sqlite3
from tkinter import *

def create_database():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def insert_record(name, age):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    connection.commit()
    connection.close()

def select_records():
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()

    connection.close()
    return records


# if __name__ == "__main__":
#     create_database()

#     name = input("Kullanıcı adını girin: ")
#     age = int(input("Kullanıcının yaşını girin: "))

#     insert_record(name, age)
#     print("Kayıt başarıyla eklendi!")

#     print("\nKullanıcılar:")
#     users = select_records()
#     for user in users:
#         print(f"ID: {user[0]}, İsim: {user[1]}, Yaş: {user[2]}")

# def add_user():
#     name = entry_name.get()
#     age = int(entry_age.get())

#     insert_record(name, age)
#     result_label.config(text="Kayıt başarıyla eklendi!")

#     update_users_list()


# def update_users_list():
#     users = select_records()
#     users_list.delete(0, END)
#     for user in users:
#         users_list.insert(END, f"ID: {user[0]}, İsim: {user[1]}, Yaş: {user[2]}")


# if __name__ == "__main__":
#     create_database()

#     root = Tk()
#     root.title("Kullanıcı Kayıt Uygulaması")

#     label_name = Label(root, text="Kullanıcı adını girin:")
#     label_name.grid(row=0, column=0)

#     entry_name = Entry(root)
#     entry_name.grid(row=0, column=1)

#     label_age = Label(root, text="Kullanıcının yaşını girin:")
#     label_age.grid(row=1, column=0)

#     entry_age = Entry(root)
#     entry_age.grid(row=1, column=1)

#     add_button = Button(root, text="Kullanıcı Ekle", command=add_user)
#     add_button.grid(row=2, column=0, columnspan=2)

#     result_label = Label(root, text="")
#     result_label.grid(row=3, column=0, columnspan=2)

#     label_users = Label(root, text="Kullanıcılar:")
#     label_users.grid(row=4, column=0, columnspan=2)

#     users_list = Listbox(root, width=50)
#     users_list.grid(row=5, column=0, columnspan=2)

#     update_users_list()

#     root.mainloop()

def update_record(id, name, age):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))

    connection.commit()
    connection.close()


def add_user():
    name = entry_name.get()
    age = int(entry_age.get())

    insert_record(name, age)
    result_label.config(text="Kayıt başarıyla eklendi!")

    update_users_list()


def update_users_list():
    users = select_records()
    users_list.delete(0, END)
    for user in users:
        users_list.insert(END, f"ID: {user[0]}, İsim: {user[1]}, Yaş: {user[2]}")

def edit_user():
    if not users_list.curselection():
        result_label.config(text="Lütfen düzenlemek istediğiniz kullanıcıyı seçin.")
        return

    selected_user = users_list.get(users_list.curselection())
    user_id = int(selected_user.split(" ")[1][:-1])

    name = entry_name.get()
    age = int(entry_age.get())

    update_record(user_id, name, age)
    result_label.config(text="Kayıt başarıyla güncellendi!")

    update_users_list()



if __name__ == "__main__":
    create_database()

    root = Tk()
    root.title("Kullanıcı Kayıt Uygulaması")

    label_name = Label(root, text="Kullanıcı adını girin:")
    label_name.grid(row=0, column=0)

    entry_name = Entry(root)
    entry_name.grid(row=0, column=1)

    label_age = Label(root, text="Kullanıcının yaşını girin:")
    label_age.grid(row=1, column=0)

    entry_age = Entry(root)
    entry_age.grid(row=1, column=1)

    add_button = Button(root, text="Kullanıcı Ekle", command=add_user)
    add_button.grid(row=2, column=0)

    edit_button = Button(root, text="Kullanıcıyı Düzenle", command=edit_user)
    edit_button.grid(row=2, column=1)

    result_label = Label(root, text="")
    result_label.grid(row=3, column=0, columnspan=2)

    label_users = Label(root, text="Kullanıcılar:")
    label_users.grid(row=4, column=0, columnspan=2)

    users_list = Listbox(root, width=50)
    users_list.grid(row=5, column=0, columnspan=2)

    update_users_list()

    root.mainloop()