"""Демо API-тесты бронирования (негативные сценарии)."""

import allure

from demo_api import DemoApiClient

# savetest_status: done
# savetest_description: Негативные проверки бронирования номера
# savetest_author: Александр Соловьев
# savetest_created_at: 2025-12-02T10:42:23Z

ERROR_EMPTY_DATES = (
    "Дата заселения не может быть пустой. Дата выезда не может быть пустой. "
)
ERROR_OVERLAP = (
    "Указанные номера либо недействительны, либо уже забронированы "
    "на одну или несколько выбранных вами дат."
)


@allure.suite("5e712107-8149-4b29-861f-a2037acd8160")
@allure.story("Негативные проверки")
class TestNegativnyeProverki:
    @allure.testcase("16c515b8-9b15-4e0d-b9c3-28e17e320d26")
    @allure.title("Ошибка при отправке бронирования без указания периода")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка валидации формы бронирования при попытке отправить заявку без выбора периода заселения и выезда. Ожидается возврат ошибки 400 и отображение соответствующего предупреждения.
    # savetest_case_estimated_time: 2m
    def test_booking_without_period(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /booking",
            [
                ("first_name", '"Иван"'),
                ("last_name", '"Иванов"'),
                ("email", '"test@test.com"'),
                ("phone", '"+77555577666"'),
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
            "400"
            "\n"
            "```"
        ):
            assert response.status_code == 400

        with allure.step(
            "Проверить сообщение об ошибке: "
            "\n"
            "```json"
            "\n"
            "'Дата заселения не может быть пустой. Дата выезда не может быть пустой. '"
            "\n"
            "```"
        ):
            assert client.get_booking_error(response) == ERROR_EMPTY_DATES

    @allure.testcase("2c43a475-784d-410c-8b22-e40b002d0c08")
    @allure.title("Ошибка при пересечении периодов бронирования номера")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка валидации при попытке забронировать номер на период, который пересекается с уже забронированным периодом. Ожидается возврат ошибки 409 и отображение предупреждения о недоступности номера.
    # savetest_case_estimated_time: 2m
    def test_booking_overlapping_period(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /booking",
            [
                ("room_id", '"demo-room-occupied"'),
                ("first_name", '"Иван"'),
                ("last_name", '"Иванов"'),
                ("email", '"test@test.com"'),
                ("phone", '"+77555577666"'),
                ("check_in", '"2025-12-12"'),
                ("check_out", '"2025-12-14"'),
                ("overlap", "true"),
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
            "409"
            "\n"
            "```"
        ):
            assert response.status_code == 409

        with allure.step(
            "Проверить сообщение об ошибке: "
            "\n"
            "```json"
            "\n"
            "'Указанные номера либо недействительны, либо уже забронированы на одну или несколько выбранных вами дат.'"
            "\n"
            "```"
        ):
            assert client.get_booking_error(response) == ERROR_OVERLAP
