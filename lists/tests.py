from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import List

class ListTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser = get_user_model().objects.create_user(username='testuser', password='password')
        testuser.save()
        
        test_list = List.objects.create(
            user = testuser,
            title = 'Workout'
            body = 'workout 5x this week'
            
        )
        test_list.save()

    def test_todo_content(self):
        todo = List.objects.get(id=1)
        actual_user = str(todo.user)
        actual_title = str(todo.title)
        actual_body = str(todo.body)
        self.assertEqual(actual_user, 'testuser')
        self.assertEqual(actual_title, 'Workout')
        self.assertEqual(actual_body, 'workout 5x this week')