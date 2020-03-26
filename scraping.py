from bs4 import BeautifulSoup
import urllib.request
import io

class SapporoMetroScraper:
    def __init__(self, url='https://www.city.sapporo.jp/st/konzatsu_jokyo2020.html'):
        print('start initialize scraper')
        opener = urllib.request.build_opener()
        opener.addheaders = [
            ('Referer', 'http://localhost'),
            ('User-Agent',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36 Edg/79.0.309.65'),
        ]
        print('accessing:', url)
        html = opener.open(url)
        bs = BeautifulSoup(html, 'html.parser')

        pdf_anchors = bs.find_all("a", class_="icon_pdf")
        pdf_links = []
        for anchor in pdf_anchors:
            pdf_links.append('https://www.city.sapporo.jp' + anchor.get('href') )
        print('done')
        self.pdf_links = pdf_links
        self.pdf_datas = []

    def fetch_pdf_data(self):
        print('start download pdffiles')
        for link in self.pdf_links:
            filename = link.split('/')[-1]
            basename = filename.split('.')[0]

            print('downloading:' + filename)
            pdf_bin = {
                'name':basename,
                'data':urllib.request.urlopen(link).read()
            }
            self.pdf_datas.append(pdf_bin)
            print('complete')
        print('done')