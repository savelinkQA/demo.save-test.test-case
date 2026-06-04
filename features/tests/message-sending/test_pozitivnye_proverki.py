"""Демо API-тесты отправки сообщений (позитивные сценарии)."""

import allure

from demo_api import DemoApiClient

# savetest_status: done
# savetest_description: Мигрированные тест-кейсы для Позитивные проверки
# savetest_author: Александр Соловьев
# savetest_created_at: 2025-12-02T10:42:33Z


@allure.suite("64c3c563-9fd1-451d-9d95-99d2ff327d59")
@allure.story("Позитивные проверки")
class TestPozitivnyeProverki:
    @allure.testcase("eebe4f2b-27e1-44fc-98d4-da5c1776d673")
    @allure.title("Отображение иконок полей ввода")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка корректного отображения иконок Font Awesome для полей формы отправки сообщения (fa-id-card для Имени, fa-envelope для e-mail, fa-phone для Телефона, fa-quote-left для Темы) и отсутствия иконки у поля "Сообщение".
    # savetest_case_estimated_time: 2m
    def test_message_form_schema(self):
        client = DemoApiClient()

        with allure.step("Отправить GET /message/form/schema"):
            response = client.get("/message/form/schema")

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
            "Проверить icons в ответе: "
            "\n"
            "```json"
            "\n"
            "fa-id-card, fa-envelope, fa-phone, fa-quote-left, body без иконки"
            "\n"
            "```"
        ):
            fields = {item["name"]: item.get("icon") for item in response.json.get("fields", [])}
            assert fields["name"] == "fa-id-card"
            assert fields["email"] == "fa-envelope"
            assert fields["phone"] == "fa-phone"
            assert fields["subject"] == "fa-quote-left"
            assert fields["body"] is None

    @allure.testcase("4c17d54c-5fe3-42c7-a488-b378141a763c")
    @allure.title("Отправка сообщения с значениями минимально допустимой длинны")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка успешной отправки сообщения с минимально допустимыми значениями всех полей (1 символ для Имени, минимальный e-mail, 11 символов для Телефона, 5 символов для Темы, 20 символов для Сообщения). Ожидается успешная отправка и отображение благодарного текста.
    # savetest_case_estimated_time: 2m
    def test_message_min_length(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /message",
            [
                ("name", '"Я"'),
                ("email", '"t@t.c"'),
                ("phone", '"+7777777777"'),
                ("subject", '"Тесты"'),
                ("body", '"Тестовый текст писем"'),
            ],
        )
        with allure.step(step_post):
            payload = DemoApiClient.payload_from_step(step_post)
            response = client.post("/message", json_body=payload)

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
            "sent"
            "\n"
            "```"
        ):
            assert response.json.get("status") == "sent"

    @allure.testcase("d9a4efd3-0bd1-4821-8238-d507ed742779")
    @allure.title("Отправка сообщения с значениями максимально допустимой длины")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка успешной отправки сообщения с максимально допустимыми значениями всех полей (255 символов для Имени, максимальный e-mail, 21 символ для Телефона, 100 символов для Темы, 2000 символов для Сообщения). Ожидается успешная отправка и отображение благодарного текста.
    # savetest_case_estimated_time: 2m
    def test_message_max_length(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /message",
            [
                ("name", f'"{ "N" * 255 }"'),
                ("email", '"longusernamecheckingmaximumlength1@examplelongdomainnameforsystems.com"'),
                ("phone", '"+12345678901234567890"'),
                ("subject", f'"{ "T" * 100 }"'),
                ("body", f'"{ "B" * 2000 }"'),
            ],
        )
        with allure.step(step_post):
            payload = DemoApiClient.payload_from_step(step_post)
            response = client.post("/message", json_body=payload)

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
            "sent"
            "\n"
            "```"
        ):
            assert response.json.get("status") == "sent"

    @allure.testcase("040b2e9c-e053-4735-a67f-997076ad9d62")
    @allure.title("Открытие почтового клиента при клике на почту")
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка функциональности ссылки на e-mail в блоке "Отправка сообщения". Ожидается открытие почтового клиента или системного окна выбора почтового клиента при клике на адрес "fake@fakeemail.com".
    # savetest_case_estimated_time: 2m
    def test_contact_email_link(self):
        client = DemoApiClient()

        with allure.step("Отправить GET /contact/email-link"):
            response = client.get("/contact/email-link")

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
            "Проверить поле href в ответе: "
            "\n"
            "```json"
            "\n"
            "mailto:fake@fakeemail.com"
            "\n"
            "```"
        ):
            assert response.json.get("href") == "mailto:fake@fakeemail.com"

    @allure.testcase("d9f9226d-4b96-4739-bb41-5a35da6ee66e")
    @allure.title('Изменение высоты поля "Сообщение"')
    @allure.severity(allure.severity_level.NORMAL)
    # savetest_case_description: Проверка возможности изменения размера поля "Сообщение" путем перетаскивания правого нижнего угла. Ожидается исчезновение вертикального скролл-бара при увеличении размера и полное отображение введенного текста.
    # savetest_case_estimated_time: 2m
    def test_message_textarea_resize_config(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /message",
            [
                ("field", '"body"'),
                ("rows", "30"),
                ("preview_length", "1200"),
            ],
        )
        with allure.step(step_post):
            payload = DemoApiClient.payload_from_step(step_post)
            response = client.post("/message", json_body=payload)

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
            "sent"
            "\n"
            "```"
        ):
            assert response.json.get("status") == "sent"
