---
## Front matter
title: "Отчёт по первому этапу проекта"
subtitle: "Дисциплина: Основы компьютерной безопасности"
author: "Дикач Анна Олеговна"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: Arial
romanfont: Arial
sansfont: Arial
monofont: Arial
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Установить дистрибутив Kali Linux в виртуальную машину

# Выполнение этапа проекта

1. Захожу на сайт https://www.kali.org/ и скачиваю образ Kali для VirtualBox  (рис. [-@fig:001])

![Сайт](image/pic1.png){ #fig:001 width=70% }

2. Создаю виртуальную машину (рис. [-@fig:002]) 

![Создание машины](image/pic2.png){ #fig:002 width=70% }

3. Настраиваю Kali в соответствии с инструкцией на сайте (рис. [-@fig:003])

![Настройка](image/pic3.png){ #fig:003 width=70% }

4. Запускаю созданную виртуальную машину(рис. [-@fig:004])

![Запуск машины](image/pic4.png){ #fig:004 width=70% }

5. Устанавливаю пользователя root aodikach, а также пароль как в дк (рис. [-@fig:005])

![Главный экран](image/pic5.png){ #fig:005 width=70% }


# Выводы

Установила Kali Linux.
