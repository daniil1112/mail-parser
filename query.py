
from typing import Any, List

from letter import Letter
from login import Account

import email
from email.header import decode_header

class Query:

    def __init__(self, account: Account) -> None:
        self.account = account.get_account()
        self.folders = ["INBOX"]
    
    def select_folder(self, folder: str) -> None:
        self.account.select(folder)

    
    def _command_uuid(self, command, *args) -> object:
        status, response = self.account.uid(command, *args)
        if status != "OK":
            Exception("error while doing command")
        return response
    
    def parse_unread_ids(self)->str:
        return self._command_uuid('search', None, 'UNSEEN')[0].decode("utf-8")


    def _read_letter(self, id:str)->List[Letter]:
        res_mails = []
        
        res, msg = self.account.fetch(id, "(RFC822)")
        
        for response in msg:
            mail_type = "html"
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]

                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode(encoding)

                # decode email sender
                From, encoding = decode_header(msg.get("From"))[0]
                if not encoding:
                    encoding = "ISO-8859-1"
                if isinstance(From, bytes) and From:
                    From = From.decode(encoding)



                body = ""

                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()

                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode(encoding)
                        except:
                            pass
                    
                else:
                    # extract content type of email
                    content_type = msg.get_content_type()
                    # get the email body
                    body = msg.get_payload(decode=True).decode(encoding)
                    if content_type == "text/plain":
                        # print only text email parts
                        mail_type="text"
                if content_type == "text/html":
                    pass
                else:
                    mail_type="text"
                
               
            res_mails.append(Letter(subject=subject, sendler=From, body=body, type_msg=mail_type))

        return res_mails

        # return str(id)
    
    def get_letters_by_ids(self, ids: Any, separator = " ")->List[Letter]:
        unread_letters_ids = []
    
        if type(ids) is str:
            unread_letters_ids = ids.split(separator)
        elif type(ids) is object:
            unread_letters_ids = ids
        
        res = []

        
        if len(unread_letters_ids) == 0:
            return res
        
        for item in unread_letters_ids:

            res.append(self._read_letter(str(item))[0])
        return res
        






