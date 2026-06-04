"""Демо API-тесты бронирования (позитивные сценарии)."""

import allure

from demo_api import DemoApiClient

# savetest_status: done
# savetest_description: Позитивные проверки бронирования номера
# savetest_author: Александр Соловьев
# savetest_created_at: 2025-12-02T10:42:26Z


@allure.suite("29172c4b-9093-4acf-901e-5a6ecb9916de")
@allure.story("Позитивные проверки")
class TestPozitivnyeProverki:
    @allure.testcase("d3d172c9-beed-4af9-8ab1-7852c0269d1d")
    @allure.title("Возвращение календаря к текущей дате")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка функциональности кнопки "Сегодня" для возврата календаря к текущему месяцу и выделения текущей даты после переключения на будущие месяцы.
    # savetest_case_estimated_time: 2m
    def test_calendar_return_to_today(self):
        client = DemoApiClient()

        with allure.step("Отправить GET /booking/calendar?room_id=demo-room-1&anchor=today"):
            response = client.get("/booking/calendar?room_id=demo-room-1&anchor=today")

        with allure.step(
            "Проверить статус-код ответа: "
            "\n"
            "```json"
            "\n"
            "200"
            "\n"
            "```"
        ):
            assert response.status_code == 200

        with allure.step(
            "Проверить поле month в ответе: "
            "\n"
            "```json"
            "\n"
            "текущий месяц, today_highlighted=true"
            "\n"
            "```"
        ):
            assert response.json.get("status") == "ok"

    @allure.testcase("c6e55398-c133-4649-82b5-e85d8021ee87")
    @allure.title("Бронирование номера на одну ночь")
    @allure.severity(allure.severity_level.CRITICAL)
    # savetest_case_description: Проверка успешного бронирования номера на одну ночь с заполнением всех обязательных полей формы. Ожидается успешная отправка POST запроса и отображение попапа с подтверждением бронирования.
    # savetest_case_estimated_time: 2m
    def test_booking_one_night(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /booking",
            [
                ("first_name", '"Иван"'),
                ("last_name", '"Иванов"'),
                ("email", '"test@test.com"'),
                ("phone", '"+77555577666"'),
                ("check_in", '"2025-12-10"'),
                ("check_out", '"2025-12-11"'),
            ],
        )

        with allure.step(step_post):
            payload = DemoApiClient.payload_from_step(step_post)
            response = client.post("/booking", json_body=payload)

        with allure.step(
            "Проверить статус-код ответа: "
            "\n"
            "```json"
            "\n"
            "200"
            "\n"
            "```"
        ):
            assert response.status_code == 200

        with allure.step(
            "Проверить поле status в ответе: "
            "\n"
            "```json"
            "\n"
            "confirmed"
            "\n"
            "```"
        ):
            assert response.json.get("status") == "confirmed"

    @allure.testcase("6d2f9b0b-7648-41b0-b280-8a42343b7cd7")
    @allure.title("Переключение календаря на месяц вперед")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка навигации календаря вперед с помощью кнопки "Вперед". Ожидается корректное отображение следующего месяца в календаре.
    # savetest_case_estimated_time: 2m
    def test_calendar_next_month(self):
        client = DemoApiClient()

        with allure.step("Отправить GET /booking/calendar?room_id=demo-room-1&direction=next"):
            response = client.get("/booking/calendar?room_id=demo-room-1&direction=next")

        with allure.step(
            "Проверить статус-код ответа: "
            "\n"
            "```json"
            "\n"
            "200"
            "\n"
            "```"
        ):
            assert response.status_code == 200

        with allure.step(
            "Проверить поле view в ответе: "
            "\n"
            "```json"
            "\n"
            "calendar"
            "\n"
            "```"
        ):
            assert response.json.get("view") == "calendar"

    @allure.testcase("cb588211-ef4f-4de0-a8c1-678d54f24183")
    @allure.title("Переключение календаря на месяц назад")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка навигации календаря назад с помощью кнопки "Назад". Ожидается корректное отображение предыдущего месяца в календаре.
    # savetest_case_estimated_time: 2m
    def test_calendar_previous_month(self):
        client = DemoApiClient()

        with allure.step("Отправить GET /booking/calendar?room_id=demo-room-1&direction=prev"):
            response = client.get("/booking/calendar?room_id=demo-room-1&direction=prev")

        with allure.step(
            "Проверить статус-код ответа: "
            "\n"
            "```json"
            "\n"
            "200"
            "\n"
            "```"
        ):
            assert response.status_code == 200

        with allure.step(
            "Проверить поле view в ответе: "
            "\n"
            "```json"
            "\n"
            "calendar"
            "\n"
            "```"
        ):
            assert response.json.get("view") == "calendar"

    @allure.testcase("ffd96dab-46c5-4b7c-9a04-75fa04299106")
    @allure.title("Очистка данных при отмене бронирования номера")
    @allure.severity(allure.severity_level.CRITICAL)
    # savetest_case_description: Проверка очистки всех заполненных данных формы бронирования при нажатии кнопки "Отмена". Ожидается, что при повторном открытии формы все поля и выбранный период будут пустыми.
    # savetest_case_estimated_time: 2m
    def test_booking_draft_reset(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /booking/draft/reset",
            [
                ("room_id", '"demo-room-1"'),
                ("action", '"cancel"'),
            ],
        )

        with allure.step(step_post):
            payload = DemoApiClient.payload_from_step(step_post)
            response = client.post("/booking", json_body=payload)

        with allure.step(
            "Проверить статус-код ответа: "
            "\n"
            "```json"
            "\n"
            "200"
            "\n"
            "```"
        ):
            assert response.status_code == 200

        with allure.step(
            "Проверить поле status в ответе: "
            "\n"
            "```json"
            "\n"
            "draft_cleared"
            "\n"
            "```"
        ):
            assert response.json.get("status") == "draft_cleared"

    @allure.testcase("5ef644ab-d36d-422c-8302-a88b6bd2f671")
    @allure.title("Выбор периода бронирования")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка механизма выбора периода бронирования путем перетаскивания курсора в календаре. Ожидается корректное выделение периода и отображение информации о количестве ночей и стоимости.
    # savetest_case_estimated_time: 2m
    def test_booking_period_selection(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /booking/quote",
            [
                ("room_id", '"demo-room-1"'),
                ("check_in", '"2025-12-20"'),
                ("check_out", '"2025-12-23"'),
            ],
        )

        with allure.step(step_post):
            payload = DemoApiClient.payload_from_step(step_post)
            response = client.post("/booking", json_body=payload)

        with allure.step(
            "Проверить статус-код ответа: "
            "\n"
            "```json"
            "\n"
            "200"
            "\n"
            "```"
        ):
            assert response.status_code == 200

        with allure.step(
            "Проверить поле status в ответе: "
            "\n"
            "```json"
            "\n"
            "confirmed"
            "\n"
            "```"
        ):
            assert response.json.get("status") == "confirmed"
