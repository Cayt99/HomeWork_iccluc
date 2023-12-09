import re

def validate_data(data):
    # Проверка количества элементов
    if len(data) != 6:
        raise ValueError("Неверное количество данных. Необходимо ввести: Фамилия, Имя, Отчество, дата рождения, номер телефона, пол.")

    # Проверка формата даты (допустим, в формате dd.mm.yyyy)
    if not re.match(r"\d{2}\.\d{2}\.\d{4}", data[3]):
        raise ValueError("Неверный формат даты рождения. Используйте формат dd.mm.yyyy.")

    # Проверка формата номера телефона (допустим, цифры без пробелов и других символов)
    if not re.match(r"\d+", data[4]):
        raise ValueError("Неверный формат номера телефона. Должны быть только цифры.")

    # Проверка пола (допустим, "мужской" или "женский")
    if data[5].lower() not in ["мужской", "женский"]:
        raise ValueError("Пол должен быть 'мужской' или 'женский'.")

    return True

def write_data_to_file(data):
    filename = f"{data[0]}.txt"
    with open(filename, "a") as file:
        file.write(" ".join(data) + "\n")

def validate_phone_number(phone_number):
    if not re.match(r"\d{10}", phone_number):
        raise ValueError("Неверный формат номера телефона. Используйте 10 цифр без пробелов и других символов (например, 1234567890).")

def validate_birth_date(birth_date):
    if not re.match(r"\d{2}\.\d{2}\.\d{4}", birth_date):
        raise ValueError("Неверный формат даты рождения. Используйте формат dd.mm.yyyy (например, 31.12.1990).")

def validate_gender(gender):
    if gender.lower() not in ["мужской", "женский"]:
        raise ValueError("Пол должен быть 'мужской' или 'женский'.")

def main():
    print("Введите данные:")
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    middle_name = input("Отчество: ")
    
    while True:
        birth_date = input("Дата рождения (dd.mm.yyyy, например, 31.12.1990): ")
        try:
            validate_birth_date(birth_date)
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    while True:
        phone_number = input("Номер телефона (10 цифр, например, 1234567890): ")
        try:
            validate_phone_number(phone_number)
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    while True:
        gender = input("Пол (мужской/женский): ")
        try:
            validate_gender(gender)
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    data = [last_name, first_name, middle_name, birth_date, phone_number, gender]

    try:
        if validate_data(data):
            write_data_to_file(data)
            print("Данные успешно сохранены.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка при работе с файлом: {e}")

if __name__ == "__main__":
    main()
