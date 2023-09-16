from datetime import datetime
import json
import os


def main(file_name):
    while True:
        os.system("CLS")  # очистка консоли
        drawing()
        user_choice = int(input("Введите число от 1 до 7: "))

        if user_choice == 1:
            show_notes(file_name)
        elif user_choice == 2:
            show_notes_on_date(file_name)
        elif user_choice == 3:
            show_note(file_name)
        elif user_choice == 4:
            add_note(file_name)
        elif user_choice == 5:
            update_note(file_name)
        elif user_choice == 6:
            delete_note(file_name)
        elif user_choice == 7:
            print("До свидания. Спасибо что пользуетесь данным приложением:)")
            return


def drawing():
    print("Добро пожаловать в консольное приложение 'Заметки'")
    print("Меню: ")
    print("1 - Показать все заметки\n(cписок с идентификационным номером и заголовком)")
    print(
        "2 - Показать заметки, сделанные или отредактированные в конкретную дату\n(cписок с идентификационным номером, заголовком и датой)"
    )
    print("3 - Показать конкретную заметку\n(отображается содержание заметки))")
    print(
        "4 - Создать и добавить новую заметку/начать работать с приложением при отсутсвии файла"
    )
    print("5 - Обновить заметку")
    print("6 - Удалить заметку")
    print("7 - Выход из приложения")


def show_notes(file_name):
    os.system("CLS")
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        for value in data["notes"]:
            print("id: ", value.get("id"))
            print("title: ", value.get("title"))
            print("---------")
        input("\nНажмите любую клавишу")
    else:
        input(
            "Еще не было создано ни одной заметки. Для создания заметки необходимо выбрать пункт 4.\nНажмите любую клавишу"
        )


def show_note(file_name):
    os.system("CLS")
    if os.path.isfile(file_name):
        flag = False
        target = input(
            "Введите идентификационный номер заметки (id) для полного просмотра: "
        )
        if target.isdigit():
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                for note in data["notes"]:
                    if note.get("id") == int(target):
                        for k, v in note.items():
                            print(k, ": ", v)
                        print("---------")
                        input("\nНажмите любую клавишу")
                        flag = True
                if flag == False:
                    input("Заметки с таким номером нет\nНажмите любую клавишу")
        else:
            input("Введен некорретный номер заметки\nНажмите любую клавишу")
    else:
        input(
            "Еще не было создано ни одной заметки. Для создания заметки необходимо выбрать пункт 4.\nНажмите любую клавишу"
        )


def show_notes_on_date(file_name):
    os.system("CLS")
    if os.path.isfile(file_name):
        target = input("Введите дату в формате (YYYY-MM-DD): ")
        flag = False
        if target.replace("-", "").isdigit():
            if (
                len(target) == 10
                and target[4] == "-"
                and target[7] == "-"
                and int(target[0:4]) > 0
                and 0 < int(target[5:7]) < 13
                and 0 < int(target[8::]) < 32
            ):
                with open(file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)
                for value in data["notes"]:
                    if value.get("date")[0:10] == target:
                        print("id: ", value.get("id"))
                        print("title: ", value.get("title"))
                        print("date: ", value.get("date"))
                        print("---------")
                        flag = True
                input("Нажмите любую клавишу")
                if flag == False:
                    input("Заметок с такой датой нет\nНажмите любую клавишу")
            else:
                input("Введена некорректная дата\nНажмите любую клавишу")
        else:
            input("Введена некорректная дата\nНажмите любую клавишу")
    else:
        input(
            "Еще не было создано ни одной заметки. Для создания заметки необходимо выбрать пункт 4.\nНажмите любую клавишу"
        )


def add_note(file_name):
    os.system("CLS")
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        id = data["notes"][len(data["notes"]) - 1].get("id") + 1
        title = input("Введите заголовок заметки: ")
        message = input("Введите тело заметки: ")
        date_note = datetime.now().isoformat()
        new_note = {"id": id, "title": title, "message": message, "date": date_note}
        data["notes"].append(new_note)
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
        input("Заметка добавлена. Нажмите любую клавишу")
    else:
        data = {
            "notes": [
                {
                    "id": "Идентификационный номер заметки",
                    "title": "Заголовок заметки",
                    "message": "Тело заметки",
                    "date": "Дата создания или последнего редактирования",
                }
            ]
        }
        id = 1
        title = input("Введите заголовок заметки: ")
        message = input("Введите тело заметки: ")
        date_note = datetime.now().isoformat()
        new_note = {"id": id, "title": title, "message": message, "date": date_note}
        data["notes"].append(new_note)
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
        input("Заметка добавлена. Нажмите любую клавишу")


def update_note(file_name):
    os.system("CLS")
    if os.path.isfile(file_name):
        target = input(
            "Введите идентификационный номер заметки (id) для редактирования: "
        )
        if target.isdigit():
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                for note in data["notes"]:
                    if note.get("id") == int(target):
                        print("Текущий заголовок: ", note.get("title"))
                        title = input("Введите отредактированный заголовок заметки: ")
                        print("Текущее тело заметки: ", note.get("message"))
                        message = input("Введите отредактированное тело заметки: ")
                        date_note = datetime.now().isoformat()
                        new_note = {
                            "title": title,
                            "message": message,
                            "date": date_note,
                        }
                        note.update(new_note)
                        with open(file_name, "w", encoding="utf-8") as file:
                            json.dump(data, file, ensure_ascii=False)
                            print(
                                "Заметка обновлена с сохранением id и установкой новой даты (редактирования)"
                            )
                        break
                else:
                    print("Заметки с таким номером нет")
        else:
            print(
                "Введно не число. Необходимо ввести число, соответствующее идентификационному номеру заметки"
            )
        input("Нажмите любую клавишу")


def delete_note(file_name):
    if os.path.isfile(file_name):
        target = input("Введите идентификационный номер заметки (id) для удаления: ")
        if target.isdigit():
            with open(file_name, "r", encoding="utf-8") as file:
                data = json.load(file)
                for note in data["notes"]:
                    if note.get("id") == int(target):
                        data["notes"] = [
                            i for i in data["notes"] if i.get("id") != int(target)
                        ]
                        with open(file_name, "w", encoding="utf-8") as file:
                            json.dump(data, file, ensure_ascii=False)
                            print("Заметка удалена.")
                        break
                else:
                    print("Заметки с таким номером нет")
        else:
            print(
                "Введно не число. Необходимо ввести число, соответствующее идентификационному номеру заметки"
            )
        input("Нажмите любую клавишу")
