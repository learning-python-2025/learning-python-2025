
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
from datetime import datetime

# Настройки парсера


class AvitoParser:
    def __init__(self):
        self.base_url = "https://www.avito.ru"
        self.session = requests.Session()
        self.ua = UserAgent()
        self.headers = {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

    def get_page(self, url, params=None):
        """Получение страницы с Avito"""
        max_retries = 3
        retry_delay = 2

        for attempt in range(max_retries):
            try:
                response = self.session.get(
                    url, headers=self.headers, params=params, timeout=10)
                response.raise_for_status()

                # Проверка на капчу
                if "captcha" in response.url:
                    print("Обнаружена капча. Попробуйте позже или используйте прокси.")
                    return None

                return response.text
            except requests.exceptions.RequestException as e:
                print(f"Ошибка при запросе (попытка {attempt + 1}): {e}")
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                else:
                    return None

    def parse_items(self, html):
        """Парсинг списка товаров"""
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', {'data-marker': 'item'})

        results = []

        for item in items:
            try:
                title_elem = item.find('h3', {'itemprop': 'name'})
                title = title_elem.text.strip() if title_elem else 'Нет названия'

                price_elem = item.find('meta', {'itemprop': 'price'})
                price = int(price_elem['content']) if price_elem else 0

                url_elem = item.find('a', {'data-marker': 'item-title'})
                url = self.base_url + url_elem['href'] if url_elem else ''

                date_elem = item.find('div', {'data-marker': 'item-date'})
                date = date_elem.text.strip() if date_elem else ''

                location_elem = item.find(
                    'div', {'class': 'geo-georeferences-SEtee'})
                location = location_elem.text.strip() if location_elem else ''

                # Добавляем только если есть цена и название
                if price > 0 and title != 'Нет названия':
                    results.append({
                        'title': title,
                        'price': price,
                        'url': url,
                        'date': date,
                        'location': location,
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    })
            except Exception as e:
                print(f"Ошибка при парсинге элемента: {e}")
                continue

        return results

    def find_best_deals(self, category, query, min_price=None, max_price=None, sort_by='price', limit=20):
        """Поиск самых выгодных предложений"""
        params = {
            'q': query,
            # Сортировка по цене (возрастание)
            's': '104' if sort_by == 'price' else '1',
        }

        if min_price is not None:
            params['pmin'] = min_price
        if max_price is not None:
            params['pmax'] = max_price

        url = f"{self.base_url}/{category}"
        html = self.get_page(url, params=params)

        if not html:
            print("Не удалось получить данные с Avito")
            return []

        items = self.parse_items(html)

        # Сортируем по цене (если нужно)
        if sort_by == 'price':
            items.sort(key=lambda x: x['price'])

        return items[:limit]


# Пример использования
if __name__ == "__main__":
    parser = AvitoParser()

    # Параметры поиска
    # Можно указать конкретную категорию, например "velosipedy"
    category = "telefony/mobilnye_telefony"
    query = "Samsung s23 ultra"   # Поисковый запрос
    min_price = 40000     # Минимальная цена
    max_price = 50000     # Максимальная цена

    print(f"Поиск выгодных предложений: {query} в категории {category}...")

    # Получаем самые дешевые предложения
    best_deals = parser.find_best_deals(
        category=category,
        query=query,
        min_price=min_price,
        max_price=max_price,
        sort_by='price',
        limit=10
    )

    # Выводим результаты
    print("\nТоп-10 самых выгодных предложений:")
    for i, item in enumerate(best_deals, 1):
        print(f"\n{i}. {item['title']}")
        print(f"   Цена: {item['price']} руб.")
        print(f"   Дата: {item['date']}")
        print(f"   Местоположение: {item['location']}")
        print(f"   Ссылка: {item['url']}")

    print(f"\nВсего найдено предложений: {len(best_deals)}")
