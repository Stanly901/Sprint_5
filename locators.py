from selenium.webdriver.common.by import By

class TestLocators:

    # Кнопка "Войти" на странице восстановления пароля
    LOGIN_LINK = (
        By.XPATH,
        "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']"
    )

    # Поле ввода логина на странице входа в личный кабинет
    EMAIL_FIELD = (
        By.XPATH,
        "//label[text()='Email']/following-sibling::input"
    )

    # Поля ввода пароля на странице входа в личный кабинет
    PASSWORD_FIELD = (
        By.XPATH,
        "//input[@type='password']"
    )

    # Кнопка "Войти" на странице входа в личный кабинет
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(text(),'Войти')]"
    )

    # Поиск кнопки "Личный кабинет" на главной странице
    ACCOUNT_BUTTON = (
        By.XPATH,
        "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']"
    )

    # Поиск имени на странице "Личный кабинет"
    NAME_INPUT = (
        By.XPATH,
        "//input[@name='Name' and @value='Иван']"
    )

    # Элемент "Конструктор" на главной странице
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Конструктор']"
    )

    # Элемент "Соберите бургер" на главной странице
    BURGER_HEADER = (
        By.XPATH,
        "//h1[text()='Соберите бургер']"
    )

    # Элемент "Логотип" на главной странице
    LOGO = (
        By.XPATH,
        "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]"
    )

    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_PAGE_LOGIN_BUTTON = (
        By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    )

    # Локатор для кнопки секции (вкладки) по её названию
    @staticmethod
    def tab_by_name(name):
        return (By.XPATH, f"//div[contains(@class, 'tab_tab__')]//span[text()='{name}']/..")

    # Локатор, который соответствует активной вкладке по названию
    @staticmethod
    def active_tab_by_name(name):
        return (By.XPATH, f"//div[contains(@class, 'tab_tab_type_current__')]//span[text()='{name}']")

    # Кнопка "Выйти" на странице личного кабинета
    LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']"
    )

    # Поле имя на странице регистрации
    REGISTRATION_NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Поле email на странице регистрации
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # Поле пароль на странице регистрации
    REGISTRATION_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")

    # Кнопка "зарегистрироваться" на странице регистрации
    REGISTRATION_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")


    LOGIN_EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Ссылка на страницу профиля
    PROFILE_PAGE_URL = "/account/profile"

    # Сообщение об ошибке на странице регистрации
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error') and contains(text(), '')]")