import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from azamat.models import Post

@pytest.mark.django_db
def test_successful_login():
    # Создаем пользователя
    user = User.objects.create_user(username="testuser", password="password")
    
    # Инициализируем API-клиент
    client = APIClient()
    
    # Отправляем POST-запрос для входа
    response = client.post('/api/token/', {'username': 'testuser', 'password': 'password'})
    
    # Проверяем, что токен успешно получен
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

@pytest.mark.django_db
def test_unsuccessful_login():
    # Инициализируем API-клиент
    client = APIClient()
    
    # Отправляем POST-запрос с неверными данными
    response = client.post('/api/token/', {'username': 'wronguser', 'password': 'wrongpassword'})
    
    # Проверяем, что вход не удался
    assert response.status_code == 401
    assert 'access' not in response.data

@pytest.mark.django_db
def test_create_post_unauthenticated():
    # Инициализируем API-клиент
    client = APIClient()
    
    # Отправляем POST-запрос без аутентификации
    response = client.post('/api/posts/', {'title': 'Test Post', 'content': 'This is a test post.'})
    
    # Проверяем, что доступ запрещен
    assert response.status_code == 401

@pytest.mark.django_db
def test_get_posts():
    # Создаем пользователя и пост
    user = User.objects.create_user(username="testuser", password="password")
    Post.objects.create(user=user, title="Test Post", content="This is a test post.")
    
    # Инициализируем API-клиент
    client = APIClient()
    
    # Отправляем GET-запрос для получения списка постов
    response = client.get('/api/posts/')
    
    # Проверяем, что посты успешно получены
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['title'] == "Test Post"