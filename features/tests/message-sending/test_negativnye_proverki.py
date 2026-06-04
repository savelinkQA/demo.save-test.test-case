import allure
import pytest

@allure.suite("97494c78-2fa4-4027-be8f-e960013d347f")
@allure.story("Негативные проверки")
class TestNegativnyeProverki:
    # savetest_case_estimated_time: 2m
    @allure.testcase("a7c03881-baff-47cf-b2c0-23a03dccc2ac")
    @allure.title("Ошибка при отправке сообщения с незаполненным именем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_message_without_name(self):
        with allure.step(
        "Отправить POST /message, тело: "
        "\n"
        "```json"
        "\n"
        "{"
        "\n"
        "\"name\": null, "
        "\n"
        "\"email\": \"test@test.com\", "
        "\n"
        "\"phone\": \"+77555577666\", "
        "\n"
        "\"subject\": \"Бронирование\", "
        "\n"
        "\"body\": \"Тестовый текст сообщения для демо-кейса\""
        "\n"
        "}"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить статус-код ответа: "
        "\n"
        "```json"
        "\n"
        "400"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить сообщение об ошибке: "
        "\n"
        "```json"
        "\n"
        "'Имя не может быть пустым'"
        "\n"
        "```"
        ):
            pass

    # savetest_case_estimated_time: 2m
    @allure.testcase("42d73b06-c069-4a07-a5ef-19168c9b12d6")
    @allure.title("Ошибка при отправке сообщения с незаполненным e-mail")
    @allure.severity(allure.severity_level.NORMAL)
    def test_message_without_email(self):
        with allure.step(
        "Отправить POST /message, тело: "
        "\n"
        "```json"
        "\n"
        "{"
        "\n"
        "\"name\": \"Иван\", "
        "\n"
        "\"email\": null, "
        "\n"
        "\"phone\": \"+77555577666\", "
        "\n"
        "\"subject\": \"Бронирование\", "
        "\n"
        "\"body\": \"Тестовый текст сообщения для демо-кейса\""
        "\n"
        "}"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить статус-код ответа: "
        "\n"
        "```json"
        "\n"
        "400"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить сообщение об ошибке: "
        "\n"
        "```json"
        "\n"
        "'Email не может быть пустым'"
        "\n"
        "```"
        ):
            pass

    # savetest_case_estimated_time: 2m
    @allure.testcase("77773ff5-36cc-4271-8a03-29c2abaa1966")
    @allure.title("Ошибка при отправке сообщения с номером телефона >21 символов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_message_phone_too_long(self):
        with allure.step(
        "Отправить POST /message, тело: "
        "\n"
        "```json"
        "\n"
        "{"
        "\n"
        "\"name\": \"Иван\", "
        "\n"
        "\"email\": \"test@test.com\", "
        "\n"
        "\"phone\": \"+775555776748294324971\", "
        "\n"
        "\"subject\": \"Бронирование\", "
        "\n"
        "\"body\": \"Тестовый текст сообщения для демо-кейса\""
        "\n"
        "}"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить статус-код ответа: "
        "\n"
        "```json"
        "\n"
        "400"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить сообщение об ошибке: "
        "\n"
        "```json"
        "\n"
        "'Телефон должен включать от 11 до 21 символов'"
        "\n"
        "```"
        ):
            pass

    # savetest_case_estimated_time: 2m
    @allure.testcase("b7468fc0-ba55-4093-9432-5e4ad0b5d56c")
    @allure.title("Ошибка при отправке сообщения с темой <5 символов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_message_subject_too_short(self):
        with allure.step(
        "Отправить POST /message, тело: "
        "\n"
        "```json"
        "\n"
        "{"
        "\n"
        "\"name\": \"Иван\", "
        "\n"
        "\"email\": \"test@test.com\", "
        "\n"
        "\"phone\": \"+77555577666\", "
        "\n"
        "\"subject\": \"Тест\", "
        "\n"
        "\"body\": \"Тестовый текст сообщения для демо-кейса\""
        "\n"
        "}"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить статус-код ответа: "
        "\n"
        "```json"
        "\n"
        "400"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить сообщение об ошибке: "
        "\n"
        "```json"
        "\n"
        "'Тема письма должна содержать от 5 до 100 символов'"
        "\n"
        "```"
        ):
            pass

    # savetest_case_estimated_time: 2m
    @allure.testcase("cc8a8cd0-7423-454f-ab98-9fb1d0e9814d")
    @allure.title("Ошибка при отправке сообщения с e-mail, несоответствующим формату")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("invalid_email", ["user@.com", "user@domain", "user@domain..com", "user@domain.c", "user@domain,com"])
    def test_message_invalid_email(self, invalid_email):
        with allure.step(
        "Отправить POST /message, тело: "
        "\n"
        "```json"
        "\n"
        "{\"name\": \"Иван\", "
        "\n"
        "\"email\": \"<invalid_email>\", "
        "\n"
        "\"phone\": \"+77555577666\", "
        "\n"
        "\"subject\": \"Бронирование\", "
        "\n"
        "\"body\": \"Тестовый текст сообщения\", "
        "\n"
        "\"invalid_email\": true"
        "\n"
        "}"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить статус-код ответа: "
        "\n"
        "```json"
        "\n"
        "400"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить сообщение об ошибке: "
        "\n"
        "```json"
        "\n"
        "'Email должен соответствовать формату'"
        "\n"
        "```"
        ):
            pass

    # savetest_case_estimated_time: 2m
    @allure.testcase("746a681c-6b4f-4163-98a9-a1c62b3abea6")
    @allure.title("Ошибка при отправке сообщения с темой >100 символов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_message_subject_too_long(self):
        with allure.step(
        "Отправить POST /message, тело: "
        "\n"
        "```json"
        "\n"
        "{"
        "\n"
        "\"name\": \"Иван\", "
        "\n"
        "\"email\": \"test@test.com\", "
        "\n"
        "\"phone\": \"+77555577666\", "
        "\n"
        "\"subject\": \"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\", "
        "\n"
        "\"body\": \"Тестовый текст сообщения для демо-кейса\""
        "\n"
        "}"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить статус-код ответа: "
        "\n"
        "```json"
        "\n"
        "400"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить сообщение об ошибке: "
        "\n"
        "```json"
        "\n"
        "'Тема письма должна содержать от 5 до 100 символов'"
        "\n"
        "```"
        ):
            pass

    # savetest_case_estimated_time: 2m
    @allure.testcase("11d31317-3c69-415e-8df7-dfdbb1cc5792")
    @allure.title("Ошибка при отправке сообщения с номером телефона <11 символов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_message_phone_too_short(self):
        with allure.step(
        "Отправить POST /message, тело: "
        "\n"
        "```json"
        "\n"
        "{"
        "\n"
        "\"name\": \"Иван\", "
        "\n"
        "\"email\": \"test@test.com\", "
        "\n"
        "\"phone\": \"+775555776\", "
        "\n"
        "\"subject\": \"Бронирование\", "
        "\n"
        "\"body\": \"Тестовый текст сообщения для демо-кейса\""
        "\n"
        "}"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить статус-код ответа: "
        "\n"
        "```json"
        "\n"
        "400"
        "\n"
        "```"
        ):
            pass
        with allure.step(
        "Проверить сообщение об ошибке: "
        "\n"
        "```json"
        "\n"
        "'Телефон должен включать от 11 до 21 символов'"
        "\n"
        "```"
        ):
            pass
