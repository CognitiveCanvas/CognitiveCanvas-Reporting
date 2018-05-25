from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from json import dumps

class ScrapeMap:
    def __init__(self, map_url):
        self.map_url = map_url
        option = webdriver.ChromeOptions()
        option.add_argument(" — incognito")
        browser = webdriver.Chrome(executable_path="/Users/bhargav/Downloads/chromedriver", chrome_options=option)
        browser.get(map_url)

        timeout = 20
        try:
            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    "//div[@id='CogCanvas']")))
        except TimeoutException:
            print("Timed out waiting for page to load")
            browser.quit()

        html = browser.page_source
        soup = BeautifulSoup(html, "html5lib")

        self.nodes = []
        self.edges = []

        for node in soup.find_all('g', attrs={'class': 'node'}):

            children = list(node.children)
            shape = children[0]
            shape_style = {styling.split(":")[0].strip(): styling.split(":")[1].strip() for styling in
                           shape["style"].strip(";").split(";")}
            tag_style = {styling.split(":")[0].strip(): styling.split(":")[1].strip() for styling in
                         node["style"].strip(";").split(";")}
            loc_x, loc_y = tag_style["transform"].replace("matrix(", "").replace(")", "").split(",")[-2:]

            label = None
            if len(children) == 2:
                label = children[1].tspan.text

            creation = int(node["id"].split("_")[1])//1000

            self.nodes.append({
                "id": node["id"],
                "shape": shape.name,
                "label": label,
                "color": shape_style.get("fill"),
                "locationX": loc_x.strip(),
                "locationY": loc_y.strip(),
                "size": shape["r"],
                "creation_time": creation
            })

        for edge in soup.find_all('g', attrs={'class': 'link'}):

            children = list(edge.children)
            shape = children[0]

            label = None
            if len(children) == 2:
                label = children[1].tspan.text

            creation = int(edge["id"].split("_")[1])//1000

            self.edges.append({
                "id": edge["id"],
                "source_id": edge["source_id"],
                "target_id": edge["target_id"],
                "label": label,
                "locationX1": shape["x1"],
                "locationY1": shape["y1"],
                "locationX2": shape["x2"],
                "locationY2": shape["y2"],
                "creation_time": creation
            })


    def get_edges(self):
        return self.edges

    def get_nodes(self):
        return self.nodes
