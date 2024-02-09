import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student
from django.core.exceptions import ValidationError
from students.serializers import CourseSerializer



@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    
    return factory


@pytest.fixture
def student():
    return Student.objects.create()


@pytest.mark.django_db
def test_get_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/1/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course[0].id


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_get_course_id(client, course_factory):
    # Arrange
    course_id = course_factory(_quantity=10)

    # Act
    response = client.get('/api/v1/courses/?id=5')

    # Assert
    if response.status_code == 200:
        index = response.json()[0]['id'] - 1
        assert response.json()[0]['id'] == Course.objects.all()[index].id


@pytest.mark.django_db
def test_filter_course_by_name(client, course_factory):
    # Arrange
    course_names = course_factory(_quantity=10)

    # Act
    response = client.get(f"/api/v1/courses/?name={course_names[1].name}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course_names[1].name


@pytest.mark.django_db
def test_create_course(client, student):
    # Arrange
    count = Course.objects.count()

    # Act
    response = client.post('/api/v1/courses/', data={'name': 'test_name', 'student': student.id})

    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    # Arrange
    course_update = course_factory(_quantity=1)

    # Act
    response = client.patch(
        f'/api/v1/courses/{course_update[0].id}/', data={'name': 'test_name'}
    )

    # Assert
    assert response.status_code == 200
    assert Course.objects.all()[0].name == "test_name"


@pytest.mark.django_db
def test_drop_course(client, course_factory):
    # Arrangee
    course_drop = course_factory(_quantity=1)
    cnt = Course.objects.count()

    # Act
    response = client.delete(f'/api/v1/courses/{course_drop[0].id}/')

    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == cnt - 1