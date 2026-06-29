@suite:29172c4b-9093-4acf-901e-5a6ecb9916de

Feature: Бронирование номера. Позитивные
  @tms:d3d172c9-beed-4af9-8ab1-7852c0269d1d
  @severity:medium
  Scenario: Возвращение выбора заезда к текущей дате
    When Я нажимаю "Заезд"/"[data-test-id="availability-checkin"]"
    When Я нажимаю "Следующий месяц"/"[data-test-id="datepicker-next-month-btn"]"
    When Я нажимаю "Сегодня"/"[data-test-id="availability-checkin-today-btn"]"
    Then Вижу в "Дате заезда"/"[data-test-id='availability-checkin']" сегодняшнюю дату


  @tms:c6e55398-c133-4649-82b5-e85d8021ee87
  @severity:critical
  Scenario: Бронирование номера на одну ночь
    When Я нажимаю "Номера"/"[data-test-id="header-nav-rooms"]"
    When Я нажимаю "Забронировать у первого номера"/"[data-test-id="room-card-book-1"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="reservation-form-firstname"]"
    When Я ввожу "Тестов" в "Фамилия"/"[data-test-id="reservation-form-lastname"]"
    When Я ввожу "brontest@test.tu" в "email"/"[data-test-id="reservation-form-email"]"
    When Я ввожу "7776665544" в "телефон"/"[data-test-id="reservation-form-phone"]"
    When Я нажимаю "Забронировать"/"[data-test-id="reservation-form-submit"]"
    Then Вижу текст "Бронирование создано"


  @tms:ffd96dab-46c5-4b7c-9a04-75fa04299106
  @severity:critical
  Scenario: Очистка данных при отмене бронирования номера
    When Я нажимаю "Номера"/"[data-test-id="header-nav-rooms"]"
    When Я нажимаю "Забронировать у первого номера"/"[data-test-id="room-card-book-1"]"
    When Я ввожу "Иван" в "Имя"/"[data-test-id="reservation-form-firstname"]"
    When Я ввожу "Тестов" в "Фамилия"/"[data-test-id="reservation-form-lastname"]"
    When Я ввожу "brontest@test.tu" в "email"/"[data-test-id="reservation-form-email"]"
    When Я ввожу "7776665544" в "телефон"/"[data-test-id="reservation-form-phone"]"
    When Я нажимаю "Отмена"/"[data-test-id="reservation-back-link"]"
    Then Не Вижу "Форму бронирования"/"["data-test-id="booking-form-section"]"

    When Я нажимаю "Забронировать у первого номера"/"[data-test-id="room-card-book-1"]"
    Then Не Вижу "Заполненное имя"/"[data-test-id="reservation-form-firstname"][value="Иван"]"
    Then Не Вижу "Заполненную фамилию"/"[data-test-id="reservation-form-lastname"][value="Тестов"]"
    Then Не Вижу "Заполненный email"/"[data-test-id="reservation-form-email"][value="brontest@test.tu"]"
    Then Не Вижу "Заполненный телефон"/"[data-test-id="reservation-form-phone"][value="7776665544"]"


  @tms:d7501563-802c-4def-b28d-4ad27dda7557
  @severity:medium
  Scenario: Выбор даты заезда в будущем году
    When Я нажимаю "Номера"/"[data-test-id="header-nav-rooms"]"
    When Я нажимаю "Забронировать у второго номера"/"[data-test-id="room-card-book-2"]"

    When Я нажимаю "Дата заезда"/"[data-test-id="reservation-form-checkin"]"
    When Я нажимаю "Выбрать год"/"[aria-label="Выбрать год"]"
    When Я нажимаю "2029 год"/"[title="2029"]"
    When Я нажимаю "Май"/"[title="2029-05"]"
    When Я нажимаю "1"/"[title="2029-05-01"]"
    Then Вижу "В Дате заезда указанную дату"/"[data-test-id="reservation-form-checkin"][value="01-05-2029"]"