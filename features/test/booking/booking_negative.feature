@suite:5e712107-8149-4b29-861f-a2037acd8160

Feature: Бронирование номера. Негативные
  @tms:16c515b8-9b15-4e0d-b9c3-28e17e320d26
  @severity:medium
  @tag:smoke
  Scenario: Ошибка при отправке бронирования без указания периода бронирования
    When Я нажимаю "Номера"/"[data-test-id="header-nav-rooms"]"
    When Я нажимаю "Забронировать у первого номера"/"[data-test-id="room-card-book-1"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="reservation-form-firstname"]"
    When Я ввожу "Тестов" в "Фамилия"/"[data-test-id="reservation-form-lastname"]"
    When Я ввожу "brontest@test.tu" в "email"/"[data-test-id="reservation-form-email"]"
    When Я ввожу "7776665544" в "телефон"/"[data-test-id="reservation-form-phone"]"
    When Я нажимаю "Очистить дату заезда"/"[data-test-id="reservation-form-checkin"]~.ant-picker-clear"
    When Я нажимаю "Очистить дату выезда"/"[data-test-id="reservation-form-checkout"]~.ant-picker-clear"

    When Я нажимаю "Забронировать"/"[data-test-id="reservation-form-submit"]"
    Then НЕ Вижу текст "Бронирование создано"
    Then Вижу текст "Выберите дату заезда"
    Then Вижу текст "Выберите дату выезда"


  @tms:2c43a475-784d-410c-8b22-e40b002d0c08
  @severity:critical
  @tag:smoke
  Scenario: Ошибка при пересечении периодов бронирования номера
    Given Я бронирую номер "2" на завтра
    When Я нажимаю "Номера"/"[data-test-id="header-nav-rooms"]"
    When Я нажимаю "Забронировать у второго номера"/"[data-test-id="room-card-book-2"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="reservation-form-firstname"]"
    When Я ввожу "Тестов" в "Фамилия"/"[data-test-id="reservation-form-lastname"]"
    When Я ввожу "brontest@test.tu" в "email"/"[data-test-id="reservation-form-email"]"
    When Я ввожу "7776665544" в "телефон"/"[data-test-id="reservation-form-phone"]"
    When Я нажимаю "Забронировать"/"[data-test-id="reservation-form-submit"]"
    Then Вижу текст "На выбранные даты номер уже забронирован"