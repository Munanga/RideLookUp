from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from django.test import tag


@tag('all')
class HomeTests(TestCase):

    # Home page view tests #############################################

    @tag('home')
    def test_home_view_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    @tag('home')
    def test_home_view_url_by_name(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @tag('home')
    def test_home_name_equal_to_home_url(self):
        resolver = resolve('/')
        view_name = 'index'
        self.assertEquals(resolver.view_name,view_name)

    @tag('home')
    def test_home_view_uses_correct_template(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')

    @tag('home')
    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        content = '<h2>Welcome!</h2>'
        self.assertContains(response,content)

    # email_sent view tests #########################################################

    @tag('email_sent')
    def test_email_sent_view_status_code(self):
        response = self.client.get('/email-sent/')
        self.assertEquals(response.status_code,200)

    @tag('email_sent')
    def test_email_sent_view_url_by_name(self):
        url = reverse('email_sent')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    @tag('email_sent')
    def test_email_sent_view_name_equal_to_email_sent_view_url(self):
        resolver = resolve('/email-sent/')
        view_name = 'email_sent'
        self.assertEquals(resolver.view_name,view_name)

    @tag('email_sent')
    def test_email_sent_view_uses_correct_template(self):
        response = self.client.get('/email-sent/')
        self.assertTemplateUsed(response,'email_sent.html')

    @tag('email_sent')
    def test_email_sent_view_contains_correct_html(self):
        response = self.client.get('/email-sent/')
        content = '<h2>Thanks! your email has been sent.</h2>'
        self.assertContains(response,content)

    # about view tests #########################################################

    @tag('about')
    def test_about_view_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code,200)

    @tag('about')
    def test_about_view_url_by_name(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)

    @tag('about')
    def test_about_view_name_equal_to_about_view_url(self):
        resolver = resolve('/about/')
        name = 'about'
        self.assertEquals(resolver.view_name,name)

    @tag('about')
    def test_about_view_uses_correct_template(self):
        response = self.client.get('/about/')
        template = 'about.html'
        self.assertTemplateUsed(response,template)

    @tag('about')
    def test_about_view_contains_correct_html(self):
        response = self.client.get('/about/')
        content = '<h2>This is about us:</h2>'
        self.assertContains(response,content)

    # contact view tests #########################################################

    @tag('contact')
    def test_contact_view_status_code(self):
        response = self.client.get('/contact/')
        self.assertEquals(response.status_code, 200)

    @tag('contact')
    def test_contact_view_url_by_name(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)







