from main import Bot

token = ''  # ключ бота
login = ''  # мобильный телефон с привязкой к логину
password = ''  # пароль к логину

if __name__ == '__main__':
    VKinder = Bot(token, login, password)
    VKinder.run()
