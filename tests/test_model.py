from django.test import TestCase
from profile_.models import SignUp, Patient
from django.contrib.auth.models import User

class SignUpModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

        self.signup = SignUp.objects.create(
            user = self.user,
            full_name = 'test user',
            email = 'test@example.com',
            phone = 9876543210,
            gender = 'Male',
            profile_photo = "images/photo.jpg",
            location = 'location',
            blood_group = 'A+',
            weight = 90,
            ready_to_donate = 'yes',
            last_donation = '2023-10-12',
        )

    def test_signup_create(self):
        self.assertTrue(isinstance(self.signup,SignUp))
        self.assertEqual(self.signup.__str__(),'test user')

    def test_signup_fields(self):
        self.assertEqual(self.signup.user.username, 'testuser')
        self.assertEqual(self.signup.full_name, 'test user')
        self.assertEqual(self.signup.email, 'test@example.com')
        self.assertEqual(self.signup.phone, 9876543210)
        self.assertEqual(self.signup.gender, 'Male')
        self.assertEqual(self.signup.profile_photo, "images/photo.jpg")
        self.assertEqual(self.signup.location, 'location')
        self.assertEqual(self.signup.blood_group, 'A+')
        self.assertEqual(self.signup.weight, 90)
        self.assertEqual(self.signup.ready_to_donate, 'yes')
        self.assertEqual(self.signup.last_donation, '2023-10-12')
    
    def test_blood_group_choices(self):
        valid_blood_group = dict(SignUp._meta.get_field('blood_group').choices).keys()
        self.assertIn(self.signup.blood_group, valid_blood_group)

    def test_gender_choices(self):
        valid_genders = dict(SignUp._meta.get_field('gender').choices).keys()
        self.assertIn(self.signup.gender, valid_genders)

    def test_ready_to_donate_choices(self):
        valid_choices = dict(SignUp._meta.get_field('ready_to_donate').choices).keys()
        self.assertIn(self.signup.ready_to_donate, valid_choices)

class PatientModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='patientuser', password='password123')
        # self.sender = SignUp.objects.create(user=self.user)
        # self.receiver = SignUp.objects.create(user=self.user)

        self.patient = Patient.objects.create(
            user = self.user,
            # blood_request_sent_by = 'sender',
            # blood_request_sent_to = 'receiver',
            patients_name = 'patient name',
            hospital = 'xyz',
            patients_department = 'abc',
            patients_gender = 'Male',
            patients_phone = 9876543210,
            patients_blood_group = 'A+',
            blood_pint = 1,
            required_date = '2023-10-12',
            requisition_form ='images/photo.jpg',
        )

    def test_patient_content(self):
        self.assertEqual(self.patient.user.username, 'patientuser')
        # self.assertEqual(self.patient.blood_request_sent_by, self.sender)
        # self.assertEqual(self.patient.blood_request_sent_to, self.receiver)
        self.assertEqual(self.patient.patients_name, 'patient name')
        self.assertEqual(self.patient.hospital, 'xyz')
        self.assertEqual(self.patient.patients_department, 'abc')
        self.assertEqual(self.patient.patients_gender, 'Male')
        self.assertEqual(self.patient.patients_phone, 9876543210)
        self.assertEqual(self.patient.patients_blood_group, "A+")
        self.assertEqual(self.patient.blood_pint, 1)
        self.assertEqual(self.patient.required_date, "2023-10-12")
        self.assertEqual(self.patient.requisition_form, "images/photo.jpg")


    def test_blood_choices(self):
        valid_blood = dict(Patient._meta.get_field('patients_blood_group').choices).keys()
        self.assertIn(self.patient.patients_blood_group, valid_blood)

    def test_patients_gender(self):
        patient_gender_choices = dict(Patient._meta.get_field('patients_gender').choices).keys()
        self.assertIn(self.patient.patients_gender, patient_gender_choices)


    
    




































