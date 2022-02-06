RAMBLER = 0
MAILRU= 1

import imaplib

class Account:
    RAMBLER = 0
    MAILRU= 1
    
    def __init__(self, login, password, type) -> None:
        if type == RAMBLER or type == MAILRU:
            self.type = type
        self.login = login
        self.password = password
        self.account = self._login_account()
    
    def get_account(self)->imaplib.IMAP4_SSL:
        return self.account

    def _login_account(self):
        if self.type == RAMBLER:
            return self._get_rambler_account()

    def _get_rambler_account(self):
        imap = imaplib.IMAP4_SSL("imap.rambler.ru", 993)
        imap.login(self.login, self.password)

        return imap
