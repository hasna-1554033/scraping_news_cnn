simport requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd

def cnn_hukum_kriminal():
    data = []
    page = 1
    while page <= 2:
        url = f"https://www.cnnindonesia.com/hukum-kriminal/indeks/11/{page}"
        request_url = req.get(url).text
        soupers = bs(request_url, 'lxml')

        class_title = "text-cnn_black_light dark:text-white mb-2 inline leading-normal text-xl group-hover:text-cnn_red"
        p_first = soupers.find_all('h2', class_=class_title)

        if p_first:
            class_link = "flex group items-center gap-4"
            p_link = soupers.find_all('a', class_link)

            class_image = "object-cover w-full group-hover:scale-110"
            p_image = soupers.find_all('img', class_=class_image)

            class_date = "text-xs text-cnn_black_light3"
            p_dates = soupers.find_all('span', class_=class_date)

            for title, link, img, date in zip(p_first, p_link, p_image, p_dates):
                title_text = title.get_text(strip=True)
                link_href = link['href']
                img_src = img['src']
                comment = date.decode_contents()
                if '<!--' in comment:
                    timestamp = comment.split('<!--')[1].split('-->')[0].strip()

                data.append({
                    'Judul': title_text,
                    'Link': link_href,
                    'Image URL': img_src,
                    'Tanggal': timestamp
                })
        page += 1

    df = pd.DataFrame(data)
    print(df.head(60))

cnn_hukum_kriminal()