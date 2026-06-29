from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Usuário:")
        self.password_input = page.get_by_role("textbox", name="Senha:")
        self.login_button = page.get_by_role("button", name="Entrar")
        self.welcome_heading = page.get_by_role("heading", name="Bem-vindo ao SimulaBank!")

    #def navigate(self):
        #self.page.goto("https://leogcarvalho.github.io/simulabank/login.html")sds

    def login(self, user: str, password: str):
        self.username_input.fill(user)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_successful(self):
        expect(self.page.get_by_role("heading", name="Bem-vindo ao SimulaBank!")).to_be_visible()
