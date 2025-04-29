import pytest
from pages.form import CreateUserForm

@pytest.mark.django_db
def test_form():
    data = {
        "username": "ABOBA",
        "first_name": "ABOBA",
        "last_name": "ABOBA",
        "password1": "49UoMa3dE2CiFxOeJbCFHhk",
        "password2": "49UoMa3dE2CiFxOeJbCFHhk",
    }
    Form = CreateUserForm(data=data)

    assert Form.is_valid(), "Form should be valid with correct data"




