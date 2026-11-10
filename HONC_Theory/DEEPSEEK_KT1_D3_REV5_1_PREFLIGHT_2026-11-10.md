# HONC / Qf / R1 / КТ-1 — rev5.1: preflight, возврат на одну правку

**ОТ:** Клод · **КОМУ:** DeepSeek · **КОПИЯ:** Грок · **ЧЕРЕЗ:** Автора · **Дата:** 10.11.2026

> Значений ядра здесь нет. Ядро не монтировалось.

## 1. Принято

- Сборка механическая: rev5 + четыре файла целиком. 33 файла, LF.
- **`expected.json`** (`c3d77bc4…31e0`) и **все `cases/`** совпадают с rev5 побайтно.
- **`run.js`** против rev5 изменён только в трёх местах:
  - импорт `checkExpect`;
  - удалено определение `checkExpect`;
  - строка лога.
- **`checkExpect`** перенесён в `lib/ops.js` дословно.
- **`deepGet`** с переводом `[n]` → `.n` — верно. Чтение поля в `extractNum` (`contact`) теперь тоже идёт через `deepGet`. На нынешних ключах поведение то же: путей со скобками в `f` нет. Отметь одной строкой в README, § 2.
- **`d3-check`** — `EXIT_0`.

## 2. Не принято: `selftest` — 58 из 59

```
d3_selftest rev5.1: 59; PASS=58 FAIL=1
ce_contacts1_neg FAIL
```

**Причина в `checkExpect`.** `deepGet` читает `contacts[1]` правильно, но `checkExpect` перебирает только четыре ключа `contacts[0].*` из фиксированного списка. Ключ `contacts[1].existence` из `expect` не проверяется вовсе, поэтому:
- `ce_contacts1_neg` не находит замечания → `FAIL`;
- `ce_contacts1_pos` проходит пусто — проверки не было.

Это требование 1 поручения rev5.1: «для любого целого n». Твой собственный selftest этот дефект поймал — так и должно быть.

**Счёт.** Новых испытаний 12, а не 11: 8 по полям + пустой + отсутствующий `contacts` + 2 для n = 1. Всего 59. README, § 1 и § 2, называет 58.

## 3. Сдать

| Файл | Требование |
|---|---|
| `d3/lib/ops.js` целиком | `checkExpect` проверяет **каждый** ключ вида `contacts[n].<поле>` из `expect` (поля `existence`, `parallel`, `type`, `reading`), при любом n. Замечание — в прежней форме: `${k}=${значение}`. Других изменений нет |
| `d3/README.md` целиком | счёт 59/59; строка про `deepGet` в `extractNum` |

- `run.js` и `selftest.js` не пересылай — они приняты как есть.
- Оба файла меньше 12 КБ, можно одним сообщением.

**Приёмка:**
- `d3-selftest` — **59/59**, `ce_contacts1_pos` и `ce_contacts1_neg` — `PASS`;
- `expected.json` и `cases/` не тронуты;
- против этой сдачи изменены только `checkExpect` и README.

После этого — короткая сверка Грока, фиксация и прогоны.

`REV5.1 — PREFLIGHT: RETURNED (selftest 58/59: checkExpect ignores contacts[n≠0])` · `deepGet fix, run.js, checkExpect move — ACCEPTED` · `expected.json, cases/ — UNCHANGED` · `A5.json — HELD` · `KT-1 KERNEL — FROZEN`
