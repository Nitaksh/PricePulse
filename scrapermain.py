import amazon
import flipkart
import gooogle
import threading 


def StartScraper(brand,product) :
    threads = []

    def start_scraping(file):
        file.init(brand,product)


    t1 = threading.Thread(target=start_scraping, args=[amazon])
    t2 = threading.Thread(target=start_scraping, args=[gooogle])
    t3 = threading.Thread(target=start_scraping, args=[flipkart])

    threads.append(t1)
    threads.append(t2)
    threads.append(t3)

    for t in threads:
        t.start()

    # wait for all threads to terminate
    for t in threads:
        t.join()

