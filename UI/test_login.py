from UI.base import BaseCase


class TestLogin(BaseCase):
    def test_login_smoke(self):
        self.login_page.login()