# Что нужно проверить

В этом проекте удалось реализовать следующие тесты

### 1. Регистрация
- Успешную регистрацию. Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен: например, 123@ya.ru. Минимальный пароль — шесть символов.
- Ошибку для некорректного пароля.

### 2. Вход
- вход по кнопке «Войти в аккаунт» на главной,
- вход через кнопку «Личный кабинет»,
- вход через кнопку в форме регистрации,
- вход через кнопку в форме восстановления пароля.

### 3. Переход в личный кабинет 
- Проверь переход по клику на «Личный кабинет».

### 4. Переход из личного кабинета в конструктор 
- Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.

### 5. Выход из аккаунта
- Проверь выход по кнопке «Выйти» в личном кабинете.

### 6. Раздел «Конструктор»
Проверь, что работают переходы к разделам:
- «Булки»,
- «Соусы»,
- «Начинки».

#28.05.2025 Update
Добавлены ассерты к тестам:
- test_forgot_password_page_login_account_button
- test_login_page_transition_constructor
- test_login_page_transition_logo
- test_main_page_click_personal_account
- test_main_page_login_account_button
- test_main_page_login_personal_account_button
- test_main_page_transition_between_sections
- test_profile_page_exit
- test_registration_page_login_button
- test_registration_page_password_less_than_six_characters
- test_registration_page_successful_registration

Тестовые функции объединены в тестовые классы и используются в тестах
Добавлено описание фикстур
Добавлены локаторы