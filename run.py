import imaplib
import email
import re
import datetime
from threading import Thread
from lxml import etree
from bs4 import BeautifulSoup
from simplejson import load
from login import Account
from query import Query
import uuid

th_arr = {}
filename_out = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".txt"


DEBUG = False
def read_letters(username, password):
    # Login to INBOX
    try:
        account = Account(username, password, type=0)
    except Exception as e:
        print(e)
        return []
    ids = ""
    try:
        query = Query(account)
        query.select_folder("INBOX")
        ids = query.parse_unread_ids()
    except Exception as e:
        print(e)
        return []

    
    if not ids:
        return []
    res = []
    for i in query.get_letters_by_ids(ids):
        if DEBUG:
            filename = str(uuid.uuid4())+".html"
            with open('debug/{0}'.format(filename),'w+') as f:
                f.write(i.sendler+"\n"*4+i.get_msg())
        for item in i.get_links():
            res.append(item)

    return res
    
    



accs = """
YAroslavZaicev9356@rambler.ru	waimtxsd_A9356
EvgeniiErmilov1221@rambler.ru	jjwpmscx_A1221
BorisDanilov1874@rambler.ru	cvefrpae_A1874
StanislavAnohin7754@rambler.ru	fhbsiiwn_A7754
KonstantinBelyakov6607@rambler.ru	kwvolgko_A6607
PavelEliseev5670@rambler.ru	kmezvllx_A5670
DenisDavydov7681@rambler.ru	ockxural_A7681
MaksimBogomolov9983@rambler.ru	ampvpfzx_A9983
MaksimKarasev6684@rambler.ru	tsgyivrl_A6684
StanislavBurov2770@rambler.ru	ubunknqt_A2770
AlekseiBabushkin4251@rambler.ru	zntvyjux_A4251
VasiliiVoroncov7540@rambler.ru	kxsbthmq_A7540
VladimirZubov3553@rambler.ru	xzreoljh_A3553
"""
RAMBLER = 0
MAILRU= 1
r = []
for item in accs.split("\n"):
    if item == "":
        continue
    t = item.split("	")
    if len(t) < 2:
        print("error in line {0}".format(accs))
        continue
    
    login, password = t[0], t[1]
    for i in read_letters(login, password):
        r.append(i)
    with open(filename_out, "w+") as f:
        f.write("\n".join(r))
    
    

