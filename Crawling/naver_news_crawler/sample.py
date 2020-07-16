from articlecrawler import ArticleCrawler

if __name__ == "__main__":
    Crawler = ArticleCrawler()
    Crawler.set_category("세계")  # 정치, 경제, 생활문화, IT과학, 사회, 세계 카테고리 사용 가능
    Crawler.set_date_range(2020, 6, 29, 2020, 6, 29)  # 2017년 12월부터 2018년 1월까지 크롤링 시작
    Crawler.start()
