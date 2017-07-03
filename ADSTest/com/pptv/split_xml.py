# -*- encoding:utf-8 -*-
from xml.etree import ElementTree


# from ads_request import getRequest

class xml_analyze:
    def __init__(self):
        pass

    # 解析xml
    @staticmethod
    # def getAd(adxml):
    def getAd():
        AD_DICT = {}                                         #ad list
        AD_DICT_BACKUP = {}                                  #backup ad list
        # root = ElementTree.fromstring(adxml)
        root = ElementTree.parse("backup.xml")
        # print adxml
        ad = root.findall('Ad')
        for i in ad:
            # print i.attrib['id']
            # print i.attrib['sequence']
            AD_DICT[i.attrib['sequence']] = i.attrib['id']
        return AD_DICT


if __name__ == '__main__':
    # xmlads = getRequest("http://10.200.20.232:8083/ikandelivery/vast/3.0draft?slen=137&longitude=&dpid=&ctype=5&latitude=&make=&osv=5.0&devicetype=2&vvid=039e698b-9cec-4d91-9c4f-76e552bdb72d&js=1&subject=&pos=300001&dnt=0&platform=1&language=en-us&resolution=1920*1080&connectiontype=1&ptye=5&username=&mac=f8b156cfa62a&tags=undefined&juid=c1ce1bf588eec4f438398ff901c92b05&did=c1ce1bf588eec4f438398ff901c92b05&nvvid=039e698b-9cec-4d91-9c4f-76e552bdb72d&model=&os=windows%20nt&accuracy=&rlen=43457275&fop=&carrier=&vlen=2622&o=forqd1&flashver=11.4%20r402&ver=3.6.8.0055&instname=update5&_=1463018864456&chid=&sid=10020777&clid=")
    xml_analyze.getAd()
    pass
