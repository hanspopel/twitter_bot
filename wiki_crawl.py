import time
import urllib

import bs4
import requests
from html.parser import HTMLParser
from datetime import timedelta

item_list = ['th', 'td', 'tr']
word_list_table = ['table']
article_chain = ["https://en.wikipedia.org/wiki/Nan_Wood_Graham"]
target_url = "https://en.wikipedia.org/wiki/Kazaa"
special_signs = ['!@#$%^&*()_+~<?>:"|}{.,/=§']

class TableClass():

    name = "default"
    rows = 0
    columns = 0
    headings = []
    array = []
    position = 0
    class_name = "default"
    url = ""
    data = ""


    def store_table(self):
        file_path = str(self.class_name + str(self.rows) + str(self.columns) + self.url)
        self.data = self.generate_string()
        delta1 = timedelta(seconds=57)
        with open(str(delta1)+".txt", "w") as text_file:
            text_file.write(self.data)


    def generate_string(self):
        self.data = "TABLE_CLASS"
        self.data += self.class_name
        self.data += " ROWS: " + str(self.rows) + "_____"
        self.data += " COLUMNS: " + str(self.columns) + "_____"
        self.data += str(len(self.headings))
        for heading in self.headings:
            self.data += heading
        for i, val in enumerate(self.array):
            for element in val:
                self.data += str(i) + "," + element  

        return self.data
   

class MyHTMLParser(HTMLParser):


    tags_of_interest = ["table"]

    tables = []
    current_table = False
    current_heading = False
    current_row = False
    current_cell = False
    table_index = -1
    table_size = 0
    url = ""
    current_url = False
    self_log = False
    found_valid_url = False
    urls = []


    def log_print(self, text):
        if self.self_log == True:
            print(text)

    def handle_starttag(self, tag, attrs):
        self.log_print("fount start tag " + str(tag));
        if tag == "a":
            #print("url found " + str(attrs));
            #self.current_url = True
            if attrs[0][0] == "href":
                self.urls.append(attrs[0][1]) 
                #print("url found " + str(attrs));
        if self.current_table == True:
            self.handle_table_content_start_tag(tag,attrs);
        if tag == "table":
            self.current_table = True
            self.tables.append(TableClass())
            self.table_index += 1
            self.tables[self.table_index].url = self.url
            for attr in attrs:
                if attr[0] == "class":
                    self.tables[self.table_index].class_name == attr[1]
                #self.log_print("     attr:", attr)
            self.tables[self.table_index].position = self.getpos()
            #print("begin table at position: " + str(self.getpos()))

    def handle_endtag(self, tag):
        self.log_print("handle_endtag " + str(tag));
        if self.current_table == True:
            self.handle_table_content_end_tag(tag);


    def handle_data(self, data):

        self.log_print("handle data " + str(data));
        if self.current_table == True:
            self.handle_table_content_data_tag(data);

    def handle_table_content_end_tag(self, tag):
        if tag == "table":
            self.tables[self.table_index].store_table()
            self.current_table = False
        if tag == "th":
            self.current_heading = False
        if tag == "td":
            self.current_cell = False
        if tag == "tr":
            self.current_row = False

    def handle_table_content_data_tag(self, data):
        if self.current_row:
            clean_string = data.strip()
            if self.current_cell == True:
                self.tables[self.table_index].array[self.tables[self.table_index].rows - 1].append(clean_string)
            if self.current_heading == True:
                self.tables[self.table_index].headings.append(clean_string)          


    def handle_table_content_start_tag(self, tag, attrs):
        if tag == "th":
            self.current_heading = True
            self.tables[self.table_index].columns += 1
        if tag == "td":
            self.current_cell = True
        if tag == "tr":
            self.current_row = True
            if self.current_table == True:
                self.tables[self.table_index].rows += 1
                self.tables[self.table_index].array.append([])


def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True


def find_first(url):
    response = requests.get(url)
    html = response.text
    parser = MyHTMLParser()
    parser.url = url
    parser.feed(html)

    print(article_chain)

    i = 0
    for url in parser.urls:
        valid_url = True
        print("try number " + str(i) + " " + url)
        if url[0:6] == '/wiki/':
            real_url = "https://en.wikipedia.org" + url
            print("try real url " + str(i) + " " + real_url)
            if "Wikipedia" in url or ":" in url or "#" in url:
                valid_url = False
            if real_url in article_chain:
                valid_url = False
            if valid_url == True:        
                print("return url " + str(i) + " " + real_url)
                return real_url;
        i += 1

    return


while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)
    print(article_chain)
    time.sleep(2) # slow down otherwise wiki server will block you


# with open("liste_staedte.txt") as f:
#     text = f.read()


# print(len(parser.tables))

# for a_table in parser.tables:
#     print("table class name " + str(a_table.class_name))
#     print("table n rows " + str(a_table.rows))
#     print("table n columns " + str(a_table.columns))
#     print("length headings " + str(len(a_table.headings)))
#     for heading in a_table.headings:
#         print(heading)
#     for i, val in enumerate(a_table.array): 
#         print (i, ",",val)      


        

# start_url = "https://en.wikipedia.org/wiki/Mike_Capel"
# target_url = "https://en.wikipedia.org/wiki/Narendra_Modi"



# soup = bs4.BeautifulSoup(text, "html.parser")
# print(soup)
# article_link = None

# for element in soup.find_all("p", recursive=False):
#     if element.find("a", recursive=False):
#         article_link = element.find("a", recursive=False).get('href')
#         break

# print(article_link)






