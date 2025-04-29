import pytest
from pages.form import CreateUserForm
from azamat.models import Post

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
    assert Form.cleaned_data["username"] == "ABOBA", "Username should be 'ABOBA'"
   
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_post():
    # Создаем пользователя с ID = 1
    user = User.objects.create_user(username="testuser", password="password")
    
    # Теперь создаем пост, ссылаясь на только что созданного пользователя
    post = Post.objects.create(user=user, title="Test Post", content="This is a test post.")
    
    # Проверьте, что пост создан
    assert post.user == user
    assert post.title == "Test Post"
