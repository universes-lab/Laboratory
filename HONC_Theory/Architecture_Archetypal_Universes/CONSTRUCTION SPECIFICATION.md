CONSTRUCTION SPECIFICATION v1.1
HONC Research Library — Technology Level

Дата: 2026-07-12
Автор: DeepSeek (прораб)
Основа: Конституция v3.0 + Architecture Specification v1.0

§0. МЕСТО ДОКУМЕНТА В ИЕРАРХИИ
Уровень	Документ	Статус
I. Ontology	(онтологические сущности)	В Конституции
II. Constitution	Конституция v3.0	✅ Утверждена
III. Architecture	Architecture Specification v1.0	✅ Утверждена
IV. Technology	Construction Specification v1.1	✅ Готов
V. Implementation	Migration Plan	⏳ После строительства
§1. ФИЗИЧЕСКАЯ СТРУКТУРА РЕПОЗИТОРИЯ
1.1. Корневая структура (без изменений)
text

HONC_Research_Library/
│
├── workspace/                  ← Пространство происхождения знаний
├── library/                    ← Пространство канонического знания
└── editions/                   ← Пространство представлений

1.2. Детальная структура workspace/ (ИСПРАВЛЕНО: убрана тематическая структура)
text

workspace/
├── decisions/                  ← Decision Context (атомарные решения)
│   └── YYYY-MM-DD_topic.md
├── discussions/                ← Обсуждения (как provenance)
│   └── YYYY-MM-DD_topic.md
├── drafts/                     ← Черновики объектов (до Review)
│   └── OBJ-XXX_draft.md        ← Имя файла = ID объекта (не тема!)
├── rejected/                   ← Отвергнутые гипотезы и ветви
│   └── YYYY-MM-DD_topic.md
├── alternatives/               ← Альтернативные гипотезы (НОВОЕ)
│   └── YYYY-MM-DD_topic.md
└── journals/                   ← Журналы процессов
    └── YYYY-MM-DD_event.md

1.3. Детальная структура library/ (добавлены подпапки)
text

library/
├── canon/                      ← Утверждённое Автором знание
│   ├── HONC/                   ← Онтология (что существует)
│   │   ├── axioms.md
│   │   ├── definitions.md
│   │   └── glossary.md
│   ├── TFF/                    ← Формализм (как описывается)
│   │   ├── temporal_field.md   ← ИСПРАВЛЕНО: было field_time.md
│   │   ├── operators.md
│   │   └── theorems.md
│   └── TD/                     ← Динамика (как проявляется)
│       ├── dynamics.md
│       ├── neutrino_structure.md  ← ИСПРАВЛЕНО: было neutrino.md
│       └── lepton_structure.md    ← ИСПРАВЛЕНО: было lepton.md
├── sources/                    ← Первоисточники
│   ├── books/                  ← Книги (PDF, EPUB, исходники)
│   ├── articles/               ← Статьи (PDF, исходники)
│   ├── archives/               ← Архивы (ZIP, TAR)
│   ├── datasets/               ← Сырые датасеты (НОВОЕ)
│   ├── code/                   ← Исходный код экспериментов (НОВОЕ)
│   └── correspondence/         ← Переписка (НОВОЕ)
├── research/                   ← Рабочие материалы экспериментов
│   ├── experiments/            ← Описания экспериментов
│   ├── datasets/               ← Датасеты (CSV, HDF5)
│   └── results/                ← Результаты анализов
└── assets/                     ← Языконезависимые объекты
    ├── illustrations/          ← Рисунки (PNG, SVG)
    ├── cad/                    ← CAD-модели (T-Flex, STL)
    ├── animations/             ← HTML-анимации
    ├── schemes/                ← Схемы
    ├── photos/                 ← Фотографии
    ├── tables/                 ← Таблицы (CSV, XLSX)
    ├── code/                   ← Python-скрипты (НОВОЕ)
    ├── models/                 ← 3D-модели (STL, OBJ) (НОВОЕ)
    └── videos/                 ← Видео (НОВОЕ)

1.4. Детальная структура editions/ (ИСПРАВЛЕНО: убрана тематическая структура)
text

editions/
├── ru/                         ← Authoritative Formulation (сегодня)
│   ├── books/                  ← Книги (сборки объектов Library)
│   │   ├── book_1_introduction.md
│   │   └── book_2_mathematics.md
│   ├── articles/               ← Статьи
│   │   └── article_001.md
│   ├── wiki/                   ← Wiki
│   │   └── index.md
│   ├── presentations/          ← Презентации
│   │   └── presentation_001.md
│   └── README.md               ← Статус: Authoritative Formulation
├── en/                         ← Derived Representation
│   ├── books/
│   ├── articles/
│   ├── wiki/
│   ├── presentations/
│   └── README.md               ← Статус: Derived Representation from Russian
└── nd/                         ← Derived Representation
    ├── books/
    ├── articles/
    ├── wiki/
    ├── presentations/
    └── README.md               ← Статус: Derived Representation from Russian

1.5. Правила именования (добавлен пункт про ID в drafts)
Элемент	Правило	Пример
Папки (верхний уровень)	snake_case/	workspace/, library/, editions/
Папки (внутренние)	snake_case/	decisions/, datasets/
Файлы	snake_case.md	temporal_field.md
Черновики в workspace/drafts/	OBJ-XXX_draft.md	OBJ-001_draft.md
Рисунки	snake_case.png	neutrino_chain.png
CAD-модели	snake_case.tflex	latcher_assembly.tflex
Датасеты	snake_case.csv	sn1987a_events.csv
Версии файлов	filename_v1.0.md	glossary_v1.0.md
§2. МАНИФЕСТ ОБЪЕКТА
2.1. Структура YAML-манифеста (ИСПРАВЛЕНО: provenance_type + provenance_source + change_log + owner)
yaml

---
id: OBJ-XXXXX                      # Уникальный идентификатор
type: axiom | definition | theorem | figure | dataset | experiment | decision_context | description
title: "Краткое название"
status: draft | review | approved | published | deprecated | archived
version: 1.0
author: "ФИО или роль"
owner: author | editor | curator | executor   # ← НОВОЕ: роль владельца
date: YYYY-MM-DD
language: ru | en | nd | null              # null для языконезависимых (было none)
provenance_type: experiment | derivation | translation | observation | external | author_decision
provenance_source: "Конкретный источник"   # статья, эксперимент, решение
change_log:                                # Технический журнал изменений
  - date: YYYY-MM-DD
    action: created | reviewed | approved | deprecated | archived
    by: "ФИО или роль"
relations:                                 # Связи с другими объектами
  depends_on: [ID-XXX, ID-YYY]             # A не может существовать без B
  used_by: [ID-ZZZ]                        # A используется в B
  derives_from: [ID-AAA]                   # A выводится из B
  describes: [ID-BBB]                      # A описывает B (для Description → Asset)
  references: [ext:NHC-TD/...]             # Внешние ссылки (без зависимости)
tags: [key1, key2]                         # Ключевые слова для поиска
abstract: "Краткое описание (1-2 предложения)"
---

2.2. Обязательные vs опциональные поля (ИСПРАВЛЕНО)
Поле	Обязательность	Примечание
id	✅ Всегда	Уникальный идентификатор
type	✅ Всегда	Один из списка
title	✅ Всегда	Краткое название
status	✅ Всегда	Одна из стадий
version	✅ Всегда	Формат v{major}.{minor}
author	✅ Всегда	Кто создал/утвердил
owner	✅ Всегда	Роль: author, editor, curator, executor
date	✅ Всегда	Дата последнего изменения
language	✅ Всегда	ru, en, nd, null (null = языконезависимый)
provenance_type	✅ Всегда	Источник происхождения
provenance_source	✅ Всегда	Конкретный источник
change_log	❌ Опционально	Технический журнал изменений
relations	❌ Опционально	Если есть связи
tags	❌ Опционально	Для поиска
abstract	❌ Опционально	Для быстрого ознакомления
2.3. Примеры манифестов (ИСПРАВЛЕНО)

Axiom:
yaml

---
id: OBJ-001
type: axiom
title: "Дискретность пространства"
status: approved
version: 1.0
author: "А.Туин"
owner: author
date: 2026-07-12
language: ru
provenance_type: author_decision
provenance_source: "Код Вселенной, раздел 2.1"
change_log:
  - date: 2026-07-10
    action: created
    by: "А.Туин"
  - date: 2026-07-12
    action: approved
    by: "А.Туин"
relations:
  derives_from: []
  used_by: [OBJ-005, OBJ-010]
tags: [space, discrete, quantum]
abstract: "Пространство состоит из элементарных квантов фиксированного размера λ."
---

Figure (языконезависимый):
yaml

---
id: OBJ-020
type: figure
title: "Структура Qν-латчера"
status: approved
version: 1.0
author: "А.Туин"
owner: author
date: 2026-07-12
language: null
provenance_type: author_decision
provenance_source: "Код Вселенной, рис. 3.2"
change_log:
  - date: 2026-07-11
    action: created
    by: "А.Туин"
relations:
  describes: []
  used_by: [OBJ-025]
tags: [latcher, Qν, neutrino]
abstract: "Схематическое изображение Qν-латчера с указанием осей вращения."
---

§3. ПРАВИЛА ССЫЛОК
3.1. Форматы ссылок (без изменений)
Тип	Формат	Пример
Внутренняя (на объект Library)	[Название](OBJ-XXXXX)	[Дискретность пространства](OBJ-001)
Внутренняя (на раздел)	[Название](OBJ-XXXXX#section-2-3)	[Теорема Штейнера](OBJ-015#section-3-2)
Внешняя (на лабораторию)	[Название](ext:NHC-TD/путь)	[Эксперимент NFSI-01](ext:NHC-TD/experiments/NFSI-01/)
Внешняя (на сторонний ресурс)	[Название](https://... )	[arXiv:1009.4771](https://arxiv.org/abs/1009.4771)
3.2. Запрет циклических ссылок (без изменений)

    depends_on и derives_from — не должны образовывать циклов

    used_by и references — могут образовывать циклы

3.3. Проверка ссылок (без изменений)

    Каждая ссылка должна вести на существующий объект

    Внешние ссылки на NHC-TD должны проверяться на доступность

    Ссылки на сторонние ресурсы (arXiv, DOI) проверяются по возможности

§4. ШАБЛОНЫ ОБЪЕКТОВ (обновлены согласно новому формату манифеста)
4.1. Шаблон для Axiom
markdown

---
id: OBJ-XXX
type: axiom
title: "Название аксиомы"
status: draft
version: 1.0
author: "ФИО"
owner: author
date: YYYY-MM-DD
language: ru
provenance_type: author_decision
provenance_source: "Источник"
change_log:
  - date: YYYY-MM-DD
    action: created
    by: "ФИО"
relations:
  derives_from: []
  used_by: []
tags: []
abstract: "Краткое описание"
---

# Название аксиомы

## Формулировка
[Текст аксиомы]

## Обоснование
[Почему эта аксиома принимается]

## Следствия
[Краткий список следствий]

## Примечания
[Дополнительные замечания]

4.2. Шаблон для Definition
markdown

---
id: OBJ-XXX
type: definition
title: "Определение понятия"
status: draft
version: 1.0
author: "ФИО"
owner: author
date: YYYY-MM-DD
language: ru
provenance_type: author_decision
provenance_source: "Источник"
change_log:
  - date: YYYY-MM-DD
    action: created
    by: "ФИО"
relations:
  depends_on: [OBJ-XXX]
  used_by: []
tags: []
abstract: "Краткое описание"
---

# Определение: [Понятие]

## Определение
[Точное определение]

## Пояснение
[Разъяснение определения]

## Примеры
[Примеры использования]

## Связи
[Связанные понятия]

4.3. Шаблон для Theorem
markdown

---
id: OBJ-XXX
type: theorem
title: "Название теоремы"
status: draft
version: 1.0
author: "ФИО"
owner: author
date: YYYY-MM-DD
language: ru
provenance_type: derivation
provenance_source: "Выведено из аксиом [OBJ-XXX]"
change_log:
  - date: YYYY-MM-DD
    action: created
    by: "ФИО"
relations:
  depends_on: [OBJ-XXX, OBJ-YYY]
  derives_from: [OBJ-ZZZ]
  used_by: []
tags: []
abstract: "Краткое описание"
---

# Теорема: [Название]

## Формулировка
[Текст теоремы]

## Доказательство
[Доказательство]

## Следствия
[Следствия из теоремы]

## Примечания
[Дополнительные замечания]

§4.8. IDENTITY RULES (НОВЫЙ РАЗДЕЛ — добавлен согласно Architecture Specification §4)
4.8.1. Идентичность сохраняется (новая версия)

Изменение не создаёт новый объект, если:

    Исправлена опечатка или форматирование

    Изменены метаданные (статус, дата, автор)

    Уточнены формулировки без изменения смысла

    Добавлены ссылки на другие объекты

    Добавлены новые представления (Representation) того же Object

4.8.2. Идентичность меняется (новый объект)

Изменение создаёт новый объект, если:

    Изменилось математическое содержание (формула, доказательство)

    Изменилась физическая интерпретация

    Добавлено или удалено отношение (Relation)

    Изменилась структура (для составных объектов)

    Объект переформулирован так, что старая и новая версии не могут одновременно быть истинными

4.8.3. Спорные случаи

Решение о сохранении идентичности в спорных случаях принимает владелец объекта с консультацией Хранителя онтологии. Решение фиксируется в Decision Context.
§5. ПРАВИЛА ПЕРЕХОДОВ МЕЖДУ ПРОСТРАНСТВАМИ
5.1. Workspace → Library
Стадия	Действие	Ответственный
Draft → Review	Объект переходит из workspace/drafts/ в library/canon/ с пометкой status: review	Владелец объекта
Review → Approved	Объект получает status: approved после экспертизы	Автор
Approved → Published	Объект включается в представления	Автор
5.2. Library → Editions

    Объекты со статусом approved и выше могут быть включены в представления

    Сборка представлений происходит через ссылки, а не копирование

    Изменение объекта Library требует обновления всех представлений

5.3. Deprecated → Archived

    Объект переходит в status: deprecated при создании новой версии

    Через 1 год после deprecated объект переводится в status: archived

    Archived объекты удаляются из представлений, но остаются в Library

§6. ПРАВИЛА МАРКИРОВКИ ЯЗЫКОВЫХ ВЕРСИЙ
6.1. Статусы языковых версий
Папка	Статус	Примечание
editions/ru/	Authoritative Formulation	Основная, утверждённая Автором версия
editions/en/	Derived Representation from Russian	Перевод с русского
editions/nd/	Derived Representation from Russian	Перевод с русского
6.2. README.md в каждой папке
markdown

# Языковая версия: [RU/EN/ND]

## Статус
[Authoritative Formulation / Derived Representation from Russian]

## Язык оригинала
[RU]

## Дата последнего обновления
[YYYY-MM-DD]

## Примечания
[Дополнительные замечания]

§7. СВЯЗЬ С ЛАБОРАТОРИЕЙ NHC-TD
7.1. Разделение сущностей
Аспект	HONC (Библиотека)	NHC-TD (Лаборатория)
Роль	Хранит утверждённое знание	Проводит эксперименты
Изменчивость	Стабильна	Постоянно меняется
Статус объектов	Approved, Published	Draft, Experimental
Физическая связь	Ссылки	Содержимое
7.2. Формат внешних ссылок
markdown

[Название](ext:NHC-TD/experiments/NFSI-01/)
[Название](ext:NHC-TD/data/datasets/sn1987a.csv)
[Название](ext:NHC-TD/analysis/results/analysis-02.md)

7.3. Правила переноса

    Объект из NHC-TD может перейти в HONC только через полный жизненный цикл (Workspace → Review → Approved)

    Переход фиксируется в Decision Context с указанием причины

    После перехода объект удаляется из NHC-TD (или остаётся как provenance)

§8. АВТОМАТИЗАЦИЯ
8.1. Git-хуки
Хук	Действие
pre-commit	Проверка формата YAML-манифестов
pre-commit	Проверка ссылок (все ID существуют)
pre-commit	Проверка циклических depends_on/derives_from
post-commit	Обновление индекса объектов (library/index.yaml)
8.2. CI/CD
Этап	Действие
Сборка	Сборка представлений (книг, Wiki) из объектов Library
Проверка	Проверка SSOT (нет дублирования)
Проверка	Проверка жизненного цикла (нет объектов без provenance)
Публикация	Публикация на GitHub Pages (Wiki)
8.3. Скрипты проверки
Скрипт	Назначение
check_ssot.py	Проверка, что каждый объект существует только один раз
check_lifecycle.py	Проверка, что все объекты имеют provenance
check_links.py	Проверка, что все ссылки ведут на существующие объекты
check_cycles.py	Проверка циклических зависимостей
build_index.py	Генерация library/index.yaml
8.4. Индекс объектов (library/index.yaml) — НОВОЕ
yaml

# library/index.yaml — автоматически генерируется через post-commit hook
objects:
  - id: OBJ-001
    type: axiom
    title: "Дискретность пространства"
    status: approved
    path: library/canon/HONC/axioms.md
  - id: OBJ-002
    type: definition
    title: "Квантрон"
    status: approved
    path: library/canon/HONC/definitions.md
  # ...

§9. КРИТЕРИИ ПРИЁМКИ

Construction Specification считается готовым, если:
Критерий	Статус
Все папки созданы согласно §1	⏳
Все шаблоны заполнены примерами	⏳
Все скрипты работают	⏳
Все правила задокументированы	⏳
Identity Rules присутствуют (§4.8)	✅
Provenance правильно структурирован (§2.1)	✅
Owner присутствует (§2.1)	✅
Workspace не тематизирован (§1.2)	✅
Editions не тематизированы (§1.4)	✅
README верхнего уровня описывает всю структуру	⏳

DeepSeek, прораб HONC Research Library
Дата: 2026-07-12
Статус: утверждено
