import pageObjects.register as register
import data.personal as personal


def test_register(setup):
    assert(register.Register(setup).test_empty_form_validation_errors_present(personal.empty_data))
    assert(register.Register(setup).test_successful_registration(personal.correct_data))

