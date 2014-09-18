import unittest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from equiz.forms import SectionForm, QuestionForm
from equiz.models import Section, Category, QuestionType, Question, Answer
from model_mommy import mommy

# class mainViewTest(TestCase):
#     def setUp(self):
#         self.client_stub = Client()
#
#     def test_view_home_route(self):
#         response = self.client_stub.get('/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_register_route(self):
#         response = self.client_stub.get('/register/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_view_logout_route(self):
#         response = self.client_stub.get('/logout/')
#         self.assertEqual(response.status_code, 302)
#
#     def test_view_own_section_route(self):
#         response = self.client_stub.get('owner/sections/create/')
#         self.assertEqual(response.status_code, 404)
#
#
# # Test Category
# class CategoryTest(TestCase):
#
#     # models test
#     def test_category_creation(self):
#         category = mommy.make(Category)
#         # category = self.create_category()
#         self.assertTrue(isinstance(category, Category))
#         self.assertEqual(category.__unicode__(), category.name)
#
#     # view test
#     def test_category_list_view(self):
#         category = mommy.make(Category)
#         url = reverse("category-list")
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)
#         self.assertIn(category.name, resp.content)
#
#     def test_category_detail_view(self):
#         category = mommy.make(Category)
#         url = reverse("category-detail", args={category.id})
#         resp = self.client.get(url)
#         self.assertEqual(resp.status_code, 200)
#         self.assertIn(category.name, resp.content)
#
#
# # Test Section
# class SectionTest(TestCase):
#
#     def test_section_creation(self):
#         section = mommy.make(Section)
#         self.assertTrue(isinstance(section, Section))
#         self.assertEqual(section.__unicode__(), section.title)
#
#     def test_create_section_form_valid(self):
#         section = mommy.make(Section)
#         data = {'title': section.title, 'owner': section.owner, 'category': 1, 'description': section.description, 'video_url': section.video_url}
#         form = SectionForm(data=data)
#         # self.assertTrue(form.is_valid())
#

    # view test
    # def test_section_list_view(self):
    #     section = mommy.make(Section)
    #     url = reverse("section-list")
    #     resp = self.client.get(url)
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertIn(section.title, resp.content)


# class QuestionTypeTest(TestCase):
#
#     def test_qstype_creation(self):
#         qstype = mommy.make(QuestionType)
#         self.assertTrue(isinstance(qstype, QuestionType))
#         self.assertEqual(qstype.__unicode__(), qstype.type)
#
#
# # Test Section
# class QuestionTest(TestCase):
#
#     def test_question_creation(self):
#         question = mommy.make(Question)
#         self.assertTrue(isinstance(question, Question))
#         self.assertEqual(question.__unicode__(), question.question)
#
#     def test_create_question_form_valid(self):
#         question = mommy.make(Question)
#         data = {'quiz_type': 1, 'section': question.section, 'question': question.question, 'markerTime': question.markerTime, 'replayTime': question.replayTime, 'value': question.value, 'penalty': question.penalty, 'feedback': question.feedback, 'hint': question.hint}
#         form = QuestionForm(data=data)
#         # self.assertTrue(form.is_valid())
#
#
# # Test Answers
# class AnswerTest(TestCase):
#
#     def test_answer_creation(self):
#         answer = mommy.make(Answer)
#         self.assertTrue(isinstance(answer, Answer))
#         self.assertEqual(answer.__unicode__(), answer.answer)
#

class TestRunVideo(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_open_section_run_video(self):

        # Open the browser and follow to login page
        self.driver.get("http://127.0.0.1:8000/login/")

        # Type username and password and hit return
        username_field = self.driver.find_element_by_id('id_username').send_keys("nadia")
        password_field = self.driver.find_element_by_id('id_password').send_keys("zxczxc")
        self.driver.find_element_by_id('submit-id-submit').click()
        # password_field.send_keys(Keys.RETURN)

        # username ans password accepted => redirection to the Section page
        self.assertIn("http://127.0.0.1:8000/sections/", self.driver.current_url)

        # find a hyperlink "Video accessibility for the HTML5 video tag"
        section_links = self.driver.find_elements_by_link_text('Video accessibility for the HTML5 video tag')
        self.assertEquals(len(section_links), 1)

        # click on section link
        section_links[0].click()

        # open the section page with title 'Video accessibility for the HTML5 video tag'
        body = self.driver.find_element_by_tag_name('body')
        self.assertIn('Video accessibility for the HTML5 video tag', body.text)

        # find the video's play button and run the video
        video_play_button = self.driver.find_element_by_class_name('vjs-play-control')
        video_play_button.click()

    def tearDown(self):
        self.driver.quit()

    # if __name__ == '__main__':
    #    unittest.main()





