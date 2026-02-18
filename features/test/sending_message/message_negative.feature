@suite:97aca9f8-5b3c-4fa6-a645-3c48a5ede7ee

Feature: Отправка сообщения. Негативные

  @tms:a7c03881-baff-47cf-b2c0-23a03dccc2ac
  @severity:medium
  Scenario: Ошибка при отправке сообщения с незаполненным именем
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "test@test.com" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "9999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "Тесты" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст для писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Введите имя"
    Then НЕ Вижу текст "Сообщение отправлено"


  @tms:18d20795-8a04-4834-90fe-d859ba3b0434
  @severity:medium
  Scenario: Ошибка при отправке сообщения с именем >255 символов
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "longName(256)" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "test@test.com" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "9999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "Тесты" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст для писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Максимум 255 символов"
    Then НЕ Вижу текст "Сообщение отправлено"


  @tms:42d73b06-c069-4a07-a5ef-19168c9b12d6
  @severity:medium
  Scenario: Ошибка при отправке сообщения с незаполненным email
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "9999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "Тесты" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст для писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Введите email"
    Then НЕ Вижу текст "Сообщение отправлено"


  @tms:77773ff5-36cc-4271-8a03-29c2abaa1966
  @severity:medium
  Scenario: Ошибка при отправке сообщения с номером телефона >21 символов
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "test@test.com" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "999888777666555444333" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "Тесты" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст для писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Телефон должен содержать от 11 до 21 символов"
    Then НЕ Вижу текст "Сообщение отправлено"


  @tms:b7468fc0-ba55-4093-9432-5e4ad0b5d56c
  @severity:medium
  Scenario: Ошибка при отправке сообщения с темой <5 символов
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "test@test.com" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "9999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "Тест" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст для писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Минимум 5 символов"
    Then НЕ Вижу текст "Сообщение отправлено"


  @tms:cc8a8cd0-7423-454f-ab98-9fb1d0e9814d
  @severity:medium
  Scenario Outline: Ошибка при отправке сообщения с e-mail, несоответствующим формату
    Examples:
    |email|
    |user@.com        |
    |user@domain      |
    |user@domain..com |
    |user@domain.c    |
    |user@domain,com  |
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "<email>" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "9999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "Тесты" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст для писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Некорректный email"
    Then НЕ Вижу текст "Сообщение отправлено"


  @tms:746a681c-6b4f-4163-98a9-a1c62b3abea6
  @severity:medium
  Scenario: Ошибка при отправке сообщения с темой >255 символов
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "test@test.com" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "9999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "longName(256)" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст для писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Максимум 255 символов"
    Then НЕ Вижу текст "Сообщение отправлено"


  @tms:11d31317-3c69-415e-8df7-dfdbb1cc5792
  @severity:medium
  Scenario: Ошибка при отправке сообщения с номером телефона <11 символов
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "test@test.com" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "Тесты" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст для писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Введите полный номер: +7 (999) 999-99-99"
    Then НЕ Вижу текст "Сообщение отправлено"