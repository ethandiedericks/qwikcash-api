from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from io import BytesIO

UserModel = get_user_model()


class MarketplaceUserTests(TestCase):

    def setUp(self):
        self.user_data = {
            "email": "testuser@example.com",
            "phone_number": "+27123456789",
            "first_name": "Test",
            "last_name": "User",
            "password": "testpassword123",
        }
        self.manager = UserModel.objects

    def test_create_user_with_valid_data(self):
        user = self.manager.create_user(**self.user_data)
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, self.user_data["email"])
        self.assertTrue(user.check_password(self.user_data["password"]))

    def test_create_user_without_email(self):
        invalid_data = self.user_data.copy()
        invalid_data["email"] = ""
        with self.assertRaises(ValueError):
            self.manager.create_user(**invalid_data)

    def test_create_user_without_phone_number(self):
        invalid_data = self.user_data.copy()
        invalid_data["phone_number"] = ""
        with self.assertRaises(ValueError):
            self.manager.create_user(**invalid_data)

    def test_create_user_with_invalid_email(self):
        invalid_data = self.user_data.copy()
        invalid_data["email"] = "invalidemail"
        with self.assertRaises(ValidationError):
            user = self.manager.create_user(**invalid_data)
            user.full_clean()  # This ensures that all model validations are run

    def test_create_user_with_invalid_phone_number(self):
        invalid_data = self.user_data.copy()
        invalid_data["phone_number"] = "invalidnumber"
        with self.assertRaises(ValueError):
            user = self.manager.create_user(**invalid_data)
            user.clean()

    def test_create_superuser(self):
        superuser = self.manager.create_superuser(**self.user_data)
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_email_uniqueness(self):
        self.manager.create_user(**self.user_data)
        with self.assertRaises(IntegrityError):
            self.manager.create_user(**self.user_data)

    # def test_update_user_profile_picture(self):
    #     user = self.manager.create_user(**self.user_data)
    #     image = SimpleUploadedFile(
    #         name="test_image.jpg",
    #         content=open("media/test_images/test-image.jpg", "rb").read(),
    #         content_type="image/jpeg",
    #     )
    #     user.profile_picture = image
    #     user.save()
    #     self.assertTrue(user.profile_picture.name.endswith(".jpg"))

    def test_user_string_representation(self):
        user = self.manager.create_user(**self.user_data)
        self.assertEqual(str(user), user.email)

    def test_create_user_with_large_profile_picture(self):
        user = self.manager.create_user(**self.user_data)

        # Create a large image
        large_image = Image.new("RGB", (500, 500))
        image_file = BytesIO()
        large_image.save(image_file, "JPEG")
        image_file.name = "large_image.jpg"
        image_file.seek(0)

        # Use SimpleUploadedFile to simulate file upload
        uploaded_file = SimpleUploadedFile(
            name="large_image.jpg",
            content=image_file.getvalue(),
            content_type="image/jpeg",
        )

        user.profile_picture = uploaded_file
        user.save()

        # Ensure the image is resized
        user.refresh_from_db()
        img = Image.open(user.profile_picture)
        self.assertLessEqual(img.height, 300)
        self.assertLessEqual(img.width, 300)
