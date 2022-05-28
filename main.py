import requests
import re
from bs4 import BeautifulSoup
import json
import os
import time

UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
cookie = "first_visit_datetime_pc=2021-11-01+23%3A25%3A38; p_ab_id=6; p_ab_id_2=3; p_ab_d_id=765568031; yuid_b=ISODI3g; privacy_policy_agreement=3; c_type=30; privacy_policy_notification=0; a_type=0; b_type=1; adr_id=LpV9C2RLU7w9mDBBAKuEzKTPUzScCSPGthxR4lWpMiA0ly94; login_ever=yes; _im_uid.3929=i.kZaH06jvSjix3pxi73T8nQ; ki_r=; ki_s=214908%3A0.0.0.0.2%3B214994%3A0.0.0.0.2%3B215190%3A0.0.0.0.2%3B220959%3A0.0.0.0.2%3B221691%3A0.0.0.0.0; ki_t=1635776749718%3B1640526757017%3B1640527671619%3B10%3B154; __utmz=235335808.1649508909.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1649508914637.1599902472; _im_vid=01G0769EVCPK45AK17BA2K2C2W; _ga=GA1.2.633887939.1649508909; _gcl_au=1.1.1515232065.1653229534; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=74198746=1^9=p_ab_id=6=1^10=p_ab_id_2=3=1^11=lang=zh=1; device_token=58dfa84fc92385b5ec072e82a1e53022; __utmc=235335808; _gid=GA1.2.1583613921.1653642767; categorized_tags=CADCYLsad0~Hry6GxyqEm~NqnXOnazer~O2wfZxfonb~OT-C6ubi9i~PHQDP-ccQD~_bee-JX46i~aLBjcKpvWL~b8b4-hqot7~dX9jAZ-RmD~kimgK7cJmi~sr5scJlaNv; tags_sended=1; __utma=235335808.633887939.1649508909.1653645200.1653651106.9; _td=74f3a506-a51c-4e03-b1a4-7437b048796a; PHPSESSID=74198746_B1NVY2mp9oJvYNApQwGAqP4BqL6QFrJl; __utmt=1; user_language=zh; QSI_S_ZN_5hF4My7Ad6VNNAi=r:10:50; cto_bundle=9dAAwF8wR09yS2lDenhIMmRNNE84S0VPWSUyRmNyZ0ZINEElMkZkZURJQ1dyaG94T0lwd2ZjdE56UmRLVlowVm9QQm55dzhTMUJOZGRWQjhjV3JxeDIwZW9XelpYTHN5JTJCdVglMkZ5JTJGJTJGN3ZHZGpDWUlZcXVtMFNwNU5QRiUyQjFPazh0V3VwUk0yek5GOGhNZm1wWG9MVHNWMk4yMDklMkZUbVJBJTNEJTNE; __cf_bm=mgHs6T5TwodKtW4j2D_i7Ig7tD.ydG4NehqFBxHr_bQ-1653717925-0-AckFXAbd62hZkRanY/INywr428dmPZCXZdjQUOnzfaY507aCnuV4hjbRBbIbExI48+GuPeC7KpgtLjr39kKLmmnctLiWJGQkxmYUE+6USCjx; tag_view_ranking=0xsDLqCEW6~O2wfZxfonb~W4_X_Af3yY~DADQycFGB0~_EOd7bsGyl~qWFESUmfEs~K8esoIs2eW~RTJMXD26Ak~LVSDGaCAdn~D0nMcn6oGk~HY55MqmzzQ~QaiOjmwQnI~_hSAdpN9rx~CrFcrMFJzz~jk9IzfjZ6n~_vCZ2RLsY2~YTKjYV1RQx~ETjPkL0e6r~Ie2c51_4Sp~BSlt10mdnm~KOnmT1ndWG~Lt-oEicbBr~PHQDP-ccQD~-StjcwdYwv~A7hSoqw-5Z~sr5scJlaNv~QL2G1t5h_V~kimgK7cJmi~Q_QQ-fT0Gi~_bee-JX46i~-GdbJLIBPc~QKeXYK2oSR~aPdvNeJ_XM~Bd2L9ZBE8q~HHxwTpn5dx~jH0uD88V6F~NKaWczYEa-~wbvCWCYbkM~MM6RXH_rlN~rIC2oNFqzh~ReJ71gk63j~r0q4yFTWtg~txZ9z5ByU7~c7QmKEJ54V~rI-sp_-x02~cmvEw6kwbq~Txs9grkeRc~4QveACRzn3~py0hn8jqar~4i9bTBXFoE~Avyrt8Dl6U~SGMAKY7jRo~cofmB2mV_d~azESOjmQSV~dqqWNpq7ul~L-d833hYKU~HQEVCHMP3y~RcahSSzeRf~suduYyiDRD~tDjQimMG4S~mzJgaDwBF5~aZpPbtdtXl~CdwexeFTM2~KN7uxuR89w~FgXjOGAbwK~zyKU3Q5L4C~aLBjcKpvWL~yRLfwuMFlA~e0WuTDU3J0~r_Jjn6Ua2V~b66BMncYDF~lfjGxLc_aO~lBcRAWFuPM~vSWEvTeZc6~F8u6sord4r~8NpFhmNqI1~G-44hwuIPi~Fh3TB_R5kA~LLyDB5xskQ~q_J28dYJ9d~QYP1NVhSHo~k_PGFy2yAr~fZoxFKear7~kU1VYpEFAM~qtVr8SCFs5~GCo59yAyB6~kWNDhzcUct~N9HSBk8BjG~Clww4ePEgi~nX8C9vvKQ0~w4sebKbvp8~_pwIgrV8TB~hd2LAU7nsU~Hry6GxyqEm~j4YdkYQPMe~3gc3uGrU1V~Cac_6jhDcg~ctdq7R9OxE~0rsCr94LAC~YHRjLHL-7q; __utmb=235335808.34.10.1653653328"
headers = {
    "User-Agent": UserAgent,
    "cookie": cookie}
proxies = {"https": "http://127.0.0.1:7890"}


class User:
    def __init__(self, UserId):
        self.UserId = UserId
        self.UserUrl = "https://www.pixiv.net/users/" + str(UserId)
        self.ArtWorkUrl = "https://www.pixiv.net/ajax/user/" + str(UserId) + "/profile/all?lang=zh"

    def GetArtWorkId(self):
        """
        获得用户下所有作品的id
        :return:
        """
        ArtWorkIdHtml = requests.get(self.ArtWorkUrl, headers=headers, proxies=proxies)
        ArtWorkIdContent = BeautifulSoup(ArtWorkIdHtml.text, "lxml")
        ArtWorkIdContent_Json = json.loads(ArtWorkIdContent.text)['body']['illusts']
        ArtWorkIdList = []
        for Id, _ in ArtWorkIdContent_Json.items():
            ArtWorkIdList.append(Id)
        return ArtWorkIdList


class ArtWork:
    def __init__(self):
        self.ArtWorkUrl = "https://www.pixiv.net/artworks/"

    def get_picture_url(self, ArtWorkId):
        """
        获得图片数据的url
        :param ArtWorkId: 图片id
        :return: 图片数据的url or None
        """
        ArtWorkUrl = self.ArtWorkUrl + str(ArtWorkId)
        ArtWorkHtml = requests.get(ArtWorkUrl, headers=headers, proxies=proxies)
        ArtWorkContent = BeautifulSoup(ArtWorkHtml.text, "lxml")

        for meta in ArtWorkContent.find_all("meta"):
            if meta.get("name") == "preload-data":
                content = meta.get("content")
                decode_content = json.loads(content)
                data = decode_content['illust'][str(ArtWorkId)]
                return data['urls']['original']
        return None

    def download_picture(self, ArtWorkId):
        """
        下载图片
        :param ArtWorkId: 图片id
        :return:
        """
        referer = self.ArtWorkUrl + str(ArtWorkId)
        download_headers = {"User-Agent": UserAgent,
                            "cookie": cookie,
                            "referer": referer}
        original_url = self.get_picture_url(ArtWorkId)
        if original_url is None:
            print("无法找到图片数据地址{%d}" % ArtWorkId)
            return
        original_picture_html = requests.get(original_url, headers=download_headers, proxies=proxies)
        original_picture_content = original_picture_html.content
        with open("./image/" + str(ArtWorkId) + ".jpg", mode="wb") as fw:
            fw.write(original_picture_content)


if __name__ == '__main__':
    user = User(13379747)
    artwork = ArtWork()
    art_work_id_list = user.GetArtWorkId()
    print("画师的作品数：%d" % len(art_work_id_list))
    for i in art_work_id_list:
        print("下载作品:%s中" % i)
        artwork.download_picture(i)
        time.sleep(3)
    print("下载完成")
