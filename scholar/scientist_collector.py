from selenium import webdriver
import time
#six home pages 
pages=['https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:science_of_science','https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:science_of_science&after_author=xaQvAKb3__8J&astart=10',
       'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:science_of_science&after_author=sjQAAEb8__8J&astart=20','https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:science_of_science&after_author=_doFAMP-__8J&astart=30',
       'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:science_of_science&after_author=PVcYAHb___8J&astart=40','https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:science_of_science&after_author=cvmQAMb___8J&astart=50',
       'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=label:science_of_science&after_author=Ow92APX___8J&astart=60']
scientists = []
head = 'https://scholar.google.com'
for page in pages:
    driver=webdriver.Firefox()
    driver.get(page)
    driver.implicitly_wait(10)
    path = '//h3[@class="gsc_oai_name"]//a'
    people = driver.find_elements_by_xpath(path)
    for person in people:
        # each scientist's homepage tail
        scientists.append(head+person.get_attribute('href'))
        time.sleep(1)
    print(scientists)
    driver.close()
print(len(scientists))
 