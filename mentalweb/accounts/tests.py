from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your tests here.
class SignUpPageTests(TestCase):
    def test_signup_page_loads(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_form_submission(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@gmail.com",
                "password1": "testpassword",
                "password2": "testpassword",
            },
        )

        self.assertEqual(response.status_code, 302)

    # Should redirect after successful signup
