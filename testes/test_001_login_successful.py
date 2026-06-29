#from playwright.sync_api import Page, expect
def test_001_login_successful(login_page) -> None:
    login_page.login("user1", "pass1")
    login_page.verify_login_successful()

 # 3:00:0   
