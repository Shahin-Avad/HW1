"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
#1 O(n)
def auth1(users, user_name, password):
        
        for key, value in users.items(): #O(n)
            if key == user_name:
                if value['пароль'] == password and value['активирован']:
                    return True
                else:
                    return "повторите попытку errno2"
        return "повторите попытку errno1"

#2 O(1)
def auth2(users, user_name, password):
    if users.get(user_name):
        if users[user_name]['пароль'] == password and users[user_name]['активирован']: #O(1)
            return True
        else:
            return "повторите попытку errno2"
    return "повторите попытку errno1"
        

f_users = { 'u1': {'пароль': 1, 'активирован': False},
            'u2': {'пароль': 1, 'активирован': True},
            'u3': {'пароль': 1, 'активирован': False}
            }

print(auth1(f_users, 'u1', 1))

"""Эффективнее второй вариант решени #2 так как тут константная сложность"""

