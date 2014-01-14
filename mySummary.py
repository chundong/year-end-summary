__author__ = 'chundong'

import sys
import datetime
from gmail import Gmail
from lxml.html import HTMLParser,document_fromstring

def handleCreditCard ():
    creditMsg = g.inbox().mail( sender="ccsvc@message.cmbchina.com")
    # print creditMsg
    if len(creditMsg) > 0:
        creditMsg[0].fetch()
        print creditMsg[0].headers
        print creditMsg[0].body



def handleAmazon ():
    orders = g.inbox().mail(sender="digital-no-reply@amazon.cn",after=datetime.date(2013,1,1),before=datetime.date(2014,1,1))
    for order in orders:
        order.fetch()
        parser = HTMLParser(encoding='utf-8')
        doc = document_fromstring(order.body,parser)
        bookes = doc.xpath('//strong/a')

        if len(bookes) == 0:
            bookes = doc.xpath('//li/a')

        if len(bookes) > 0:
            print bookes[0].text_content()
        else:
            print 'error'

            # print order.body


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print 'usage: mySummary username password'
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    g = Gmail()
    g.login(username, password)

    # handleCreditCard(g)

    handleAmazon()

    g.logout()
