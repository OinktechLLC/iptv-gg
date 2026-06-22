# IPTV Hunter - Поисковый робот для плейлистов

Автоматический обновляемый IPTV плейлист с российскими каналами.

## Особенности
- Python scraper ищет новые рабочие ссылки
- GitHub Actions обновляет плейлист **каждые 6 часов**
- Полностью открытый код (MIT License)

## Как использовать
1. Скачай `iptv/all_in_one.m3u`
2. Добавь в свой IPTV плеер (VLC, Kodi, Perfect Player и т.д.)

## Для разработчиков
```bash
git clone https://github.com/yourname/iptv-scraper.git
cd iptv-scraper
python -m venv venv
source venv/bin/activate
pip install requests
python scraper/main.py
```

## Лицензия
MIT License - см. [LICENSE](LICENSE)

---

**Проект создан с ❤️ для сообщества**
