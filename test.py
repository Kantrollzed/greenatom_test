# 1. Какие шаги ты бы предпринял, если бы пользователь сказал, что API возвращает ему ошибку 500?
# Пробуем сделать запрос снова!)
# 500 ошибка, это не ошибка на стороне клиента -> залезаем в лог
# Причин может быть масса. От банального недостатка оперативной памяти до отвалившихся сервисов, соединения с бд и тп...

# 2. Какие ты видишь проблемы в следующем фрагменте кода? Как его следует исправить?
#    Исправь ошибку и перепиши код ниже с использованием типизации.

# Была проблема в лямбда функции и невозможности сохранения параметров при передаче в list
# Добавил partial c сохранением параметров и всё получилось, результат нагляден если в качестве callback использовать print

def create_handlers(callback):
    from functools import partial

    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(partial(callback, step))
    return handlers

def execute_handlers(handlers):
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()



# 3. Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? 
#    Сколько из них содержит атрибуты?
#    Напиши скрипт на Python, который выводит ответы на вопросы выше

def get_greenatom_tags():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    
    driver = webdriver.Chrome()
    driver.get('https://greenatom.ru')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    tags = soup.find_all()
    
    tag_count, attrs_count = 0, 0
    for tag in tags:
        tag_count += 1
        if (len(tag.attrs) > 0):
            attrs_count += 1

    print("tags count: ", tag_count)
    print("attrs count: ", attrs_count)


# 4. Напиши функцию на Python, которая возвращает текущий публичный IP-адрес компьютера
#    (Например, с использованием сервиса ifconfig.me)
def get_ip_with_ifconfig():
    import requests
    r = requests.get("https://ifconfig.me")
    print("Pub ip-address: ", r.text)


# 5. Напиши функцию на Python, выполняющую сравнение версий.
#    Return -1 version A is older than version B
#    Return 0 if versions A and B are equivalent
#    Return 1 if version A is newer than version B
#    Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.

# Искренне надеюсь, что правильно понял задачу и писал сравнение версий вне привязки к конкретным их получениям )
def comparison_versions(A, B):
    A_splt, B_splt = A.split("."), B.split(".")
    A_len, B_len = len(A_splt), len(B_splt)
    
    # Определяем количество итераций по минимуму если разная длинна
    len_equal = A_len == B_len
    if (not len_equal):
        iters_count = min(A_len, B_len) 
    else:
        iters_count = A_len

    # Поуровнево сравниваем версии и если находим разницу - формируем результат
    for i in range(iters_count):
        A_splt[i], B_splt[i] = int(A_splt[i]), int(B_splt[i])
        
        if (A_splt[i] != B_splt[i]):
            if (A_splt[i] > B_splt[i]): 
                return 1
            else: 
                return -1
    
    # Если количество подуровней разная - проверяем на ненулевой подуровень
    # 1.10 = 1.10.0.0, а также 1.10 < 1.10.0.1 
    if (not len_equal):
        is_in = True
        i = iters_count
        while (is_in):
            is_in = False
            try:
                if (int(A_splt[i]) > 0):
                    return 1
                is_in = True
            except:
                if (int(B_splt[i]) > 0):
                    return -1
                is_in = True
            i += 1
    else:
        return 0
    


if __name__ == "__main__":
    # 2
    handlers = create_handlers(print)
    execute_handlers(handlers)
    # 3
    get_greenatom_tags()
    # 4
    get_pub_ip_with_ifconfig()
    # 5
    print(comparison_versions("1.11", "1.11.0.1"))
