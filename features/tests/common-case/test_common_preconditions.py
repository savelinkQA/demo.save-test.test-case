"""Демо API-тест: общий кейс предусловий."""

import allure

from demo_api import DemoApiClient

# savetest_status: new
# savetest_description: Основные предусловия для кейсов
# savetest_author: Александр Соловьев
# savetest_created_at: 2025-12-10T07:50:12Z


@allure.suite("143abfd9-e430-4502-937c-f849e50956e0")
@allure.story("Предусловия")
class TestPredusloviya:
    @allure.testcase("36c63fcc-acfa-426d-bc79-a849c2b917a7")
    @allure.title("Авторизован администратор")
    @allure.severity(allure.severity_level.CRITICAL)
    # savetest_case_description: Предусловие авторизации администартором
    def test_admin_login(self):
        client = DemoApiClient()
        step_post = DemoApiClient.step_post_body(
            "POST /auth/login",
            [
                ("username", '"testadmin"'),
                ("password", '"testadminpassword"'),
            ],
        )

        with allure.step(step_post):
            payload = DemoApiClient.payload_from_step(step_post)
            response = client.post("/auth/login", json_body=payload)

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
            "Проверить поле role в ответе: "
            "\n"
            "```json"
            "\n"
            "admin"
            "\n"
            "```"
        ):
            assert response.json.get("role") == "admin"
