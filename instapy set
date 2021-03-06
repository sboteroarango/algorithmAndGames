from instapy import InstaPy
browser= r"C:\Program Files\Mozilla Firefox\firefox.exe"
sesion=InstaPy(username="bofeket",password="bofeket123",browser_executable_path=browser)
sesion.login()
sesion.set_user_interact(amount=2, randomize=True, percentage=100, media="Photo")
sesion.set_do_follow(enabled=True, percentage=100)
sesion.set_do_comment(enabled=False,percentage=0)
sesion.set_do_like(enabled=False, percentage=0)
sesion.follow_by_tags(["happy"],amount=3,randomize=False,media="Photo",interact=True)
sesion.end()
