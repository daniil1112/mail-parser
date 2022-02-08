import re
from unittest import result
from lxml import etree


class Letter:

    dict = {
        "marlboro": [
            {"xpath": '//a[@id="button"]'},
            {"xpath": '//a[@id="hero"]'}
        ],
        "parliament": [
            {"xpath": '//img[@alt="Узнать больше"]/..'},
            {"xpath": '//*[@id="button1"]'},
        ],
        "bond": [
            {"xpath" :'//a[@id="website"]'}
        ],
        "iqos": [
            {"xpath" :'//img[@alt="Ð£Ð·Ð½Ð°ÑÑ Ð±Ð¾Ð»ÑÑÐµ"]/..'}
        ],
        "philip": [
            {"xpath": '//a[@id="code"]'},
            {"xpath": '//a[@id="digest_1"]'},
            {"xpath": '//a[@id="auth"]'}
        ],
        "chesterfield": [
            {"xpath": '//a[@id="button"]'},
        ]
    }

    def __init__(self, subject: str, sendler: str, body:str, type_msg="html") -> None:
        self.subject = subject
        self.sendler = sendler
        self.type = type_msg
        self.body = body
    def get_msg(self):
        return self.body
    def get_sendler(self):
        for i in self.dict:
            if i.lower() in self.sendler.lower():
                return i.lower()
        
    
    
    def get_links(self):
        res = []
        sendler = self.get_sendler()
        print(sendler)
        if self.type == "html" and sendler and sendler in self.dict :
            try:
                 tree = etree.HTML(self.body)
                 for i in self.dict[sendler]:
                    try:
                        r = tree.xpath(i["xpath"])
                        attr = "href"
                        if "attr" in i:
                            attr = i["attr"]
                        if len(r) > 0:
                            res.append(r[0].get(attr))
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
        return res
        
    

 
