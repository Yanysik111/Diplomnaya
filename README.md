Эта дипломная работа представляет собой всесторонний анализ и сравнение трех популярных фреймворков для разработки веб-приложений на языке Python: Django, Flask и FastAPI. 
Проведено практическое исследование путем создания простых веб-приложений на каждом из фреймворков, а также выполнен детальный анализ их характеристик, производительности и удобства использования. 
Результаты исследования помогут начинающим и опытным разработчикам выбрать наиболее подходящий инструмент для своих проектов.
---
[DJANGO](https://www.google.com/url?q=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F5.1%2F)

[FASTAPI](https://www.google.com/url?q=https%3A%2F%2Ffastapi-tutorial.readthedocs.io%2Fen%2Flatest%2F)

[FLASK](https://www.google.com/url?q=https%3A%2F%2Fflask.palletsprojects.com%2Fen%2Fstable%2F)


Параметры |Django	| FastApi	| Flask
:---------|:------|:-------:|:-----:
Тип|Полноценный веб-фреймворк	|Микро-веб-фреймворк|	Микро-веб-фреймворк
Вариант использования|Создавайте сложные веб-приложения и API	|Создание API и микросервисов	|Идеально подходит для создания небольших веб-приложений и простых API
Производительность|Быстро для создания больших веб-приложений	|Очень быстро для создания API и микросервисов|	Медленнее из-за ручной проверки и синхронизированного программирования.
Масштабируемость|Масштабируемость, но ORM и шаблонизатор могут замедлить масштабирование	|Высокая масштабируемость, поскольку использует асинхронный код и аннотации типов.	|Сложно масштабировать, так как нет встроенной поддержки ORM или кэширования.
Инструменты базы данных|	Полный набор	|Ограничено, нет встроенной поддержки	|Ограничено, нет встроенной поддержки
Асинхронное программирование|Да, можно сделать с помощью Asyncio, но немного медленнее.|	Да, но быстрее благодаря Pydantic.	|Нет, но можно сделать, используя другие библиотеки.
ORM|	Да	|Нет|	Нет
Сообщество	|Большое и активное	|Маленькое, но растущее|	Большое и активное
Документация	|Огромная|	Маленькая, но все еще растущая	|Большая
Преимущества|	Это отличный выбор для тех, кто хочет создавать безопасные, масштабируемые, гибкие и простые в обслуживании веб-приложения.|	Это отличный выбор для создания высокопроизводительных API и микросервисов.	|Это отличный выбор для создания небольших и средних веб-приложений, где производительность не так важна, а разработчику нужна гибкость.
Недостатки	|Может быть сложным для новичков, трудным в отладке и неподходящим для небольших проектов.|	Основные файлы могут быть переполнены и иметь недостаток встроенной безопасности.	|Нет встроенной поддержки кэширования, ORM, асинхронизации и т. д
