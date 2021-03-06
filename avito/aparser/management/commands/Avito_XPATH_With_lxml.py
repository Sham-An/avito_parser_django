import requests
import lxml.html

html = requests.get('https://www.avito.ru/rostov-na-donu/mototsikly_i_mototehnika/mopedy_i_skutery-ASgBAgICAUQ82gE?f=ASgBAgECAUQ82gEBRcaaDBZ7ImZyb20iOjMwMCwidG8iOjcwMDB9&q=%D1%81%D0%BA%D1%83%D1%82%D0%B5%D1%80&radius=100', 'utf-8')
doc = lxml.html.fromstring(html.content)

new_releases = doc.xpath('//div[@elementtiming="bx.catalog.container"]')[0] #Родительский контейнер


items_id = new_releases.xpath('.//div[@data-item-id]')
meta_items_id = new_releases.xpath('.//meta[@itemprop="description"]/@content')

print(f'meta_items_id {meta_items_id}')
print(f'ВСЕГО {len(items_id)} В {items_id}')
titles = new_releases.xpath('.//div[substring(@class,1,13) ="iva-item-desc"]//text()')
prices = new_releases.xpath('.//div[@data-item-id]//meta[@itemprop="price"]/@content')
all_in_one = new_releases.xpath('//*[//div[@data-item-id]//div[@data-marker="item-date"]//preceding::div[@data-marker="item-line"]]')
print(len(titles))
print(len(prices))
#tags = [tag.text_content() for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]')]
#tags = [tag.split(', ') for tag in tags]

# platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
# total_platforms = []
#
# for game in platforms_div:
#     temp = game.xpath('.//span[contains(@class, "platform_img")]')
#     platforms = [t.get('class').split(' ')[-1] for t in temp]
#     if 'hmd_separator' in platforms:
#         platforms.remove('hmd_separator')
#     total_platforms.append(platforms)