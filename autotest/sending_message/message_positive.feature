@suite:e4bd4e6b-24fd-4e90-b2a7-8c66a43a6211

Feature: Отправка сообщения. Позитивные

  @tms:4c17d54c-5fe3-42c7-a488-b378141a763c
  @severity:medium
  Scenario: Отправка сообщения с значениями минимально допустимой длинны
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "Я" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "t@t.co" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "9999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "Тесты" в "Тему"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "Тестовый текст писем" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Сообщение отправлено"

  @tms:d9a4efd3-0bd1-4821-8238-d507ed742779
  @severity:medium
  Scenario: Отправка сообщения с значениями максимально допустимой длинны
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    When Я ввожу "longName(255)" в "Имя"/"[data-test-id="contact-form-name"]"
    When Я ввожу "longusernamecheckingmaximumlength1@examplelongdomainnameforsystems.com" в "Email"/"[data-test-id="contact-form-email"]"
    When Я ввожу "9999999999" в "Телефон"/"[data-test-id="contact-form-phone"]"
    When Я ввожу "longName(255)" в "Тема"/"[data-test-id="contact-form-subject"]"
    When Я ввожу "longName(2000)" в "Сообщение"/"[data-test-id="contact-form-message"]"
    When Я нажимаю "Отправить"/"[data-test-id="contact-form-submit"]"
    Then Вижу текст "Сообщение отправлено"


  @tms:d9f9226d-4b96-4739-bb41-5a35da6ee66e
  @severity:medium
  Scenario: Изменение высоты поля Сообщение
    When Я нажимаю "Контакты"/"[data-test-id="header-nav-contact"]"
    Then Вижу "Форму обратной связи"/"[data-test-id="contact-form-card"]"

    When Кликнуть и тянуть "880", "610" - "880", "640"
    Then Вижу "Увеличенное поле сообщение"/"[style="height: 126px;"]"

    When Кликнуть и тянуть "880", "640" - "880", "600"
    Then Вижу "Уменьшенное поле сообщение"/"[style="height: 86px;"]"