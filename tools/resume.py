"""Builds resume_gisina_en.pdf and resume_gisina_ru.pdf from the data below.

Usage (any Python with reportlab): python tools/resume.py
Public file: no phone number, no date of birth, no personal email. Contact = Telegram + LinkedIn.
"""
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

FONTS = Path("/System/Library/Fonts/Supplemental")
pdfmetrics.registerFont(TTFont("Body", str(FONTS / "Arial.ttf")))
pdfmetrics.registerFont(TTFont("Body-Bold", str(FONTS / "Arial Bold.ttf")))
pdfmetrics.registerFont(TTFont("Head", str(FONTS / "Georgia Bold.ttf")))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold")

INK, MUTED, ACCENT = HexColor("#16213a"), HexColor("#5d6475"), HexColor("#2a78d6")

DATA = {
    "en": {
        "name": "Anastasia Gisina",
        "role": "Head of Product Analytics",
        "contacts": "Moscow · Telegram <b>@agisina</b> · linkedin.com/in/anastasiagisina · github.com/tpofd · tpofd.github.io",
        "summary": "6+ years in product and business analytics at Ozon, SberMarket, Dostavista and X5 Digital. I build analytics "
                   "functions that teams trust: metrics, experimentation, BI and diagnostics of metric changes. Course lead for "
                   "“AI for Analytics” at OTUS, mentor and speaker.",
        "h_exp": "Experience", "h_teach": "Teaching, mentoring, speaking", "h_edu": "Education", "h_skills": "Skills",
        "exp": [
            ("X5 Digital", "Head of Product Analytics", "Oct 2025 – present", [
                "Lead and grow the product analytics team; hire middle and senior analysts.",
                "Built a daily diagnostic dashboard that splits conversion changes into commercial and product factors: "
                "time from “conversion dropped” to a testable hypothesis went from 1–3 weeks to a couple of days.",
                "Set up rules for A/B tests that share app screens across teams: mandatory guardrail metrics, a shared test "
                "calendar, an analyst who owns each screen.",
                "Introduced an AI-assisted workflow for building BI dashboards: mockup first, data marts designed for the mockup.",
            ]),
            ("Dostavista", "Analytics Lead", "Sep 2024 – Oct 2025", [
                "Led the analytics function: 4 analysts (product and marketing) and a data engineer.",
                "Defined core metrics and unified reporting and data definitions across teams.",
                "Built the BI stack and data marts (Metabase, Delta BI, Trino) and enabled self-service analytics.",
                "Owned the experimentation framework: test design, sample sizing, methods, decision rules.",
            ]),
            ("SberMarket", "Senior Product Analyst", "Apr 2023 – Aug 2024", [
                "Built the analytics framework for a new B2B product from scratch; its metrics went onto the company's key dashboards.",
                "Coordinated five departments to measure the product's impact on operations; nominated for the internal Tech Award.",
                "Contributed to pricing and unit economics; the product reached positive unit economics.",
                "Designed B2B A/B tests and the method for calculating their results; mentored junior analysts.",
            ]),
            ("Ozon", "Product Analyst", "Jan 2022 – Feb 2023", [
                "Led the migration of 100+ team reports to Superset in 1.5 months.",
                "Built a self-service data tool that saved the analytics team 20+ hours a week of ad-hoc work.",
                "Built reporting for top management and the metric methodology for the contact center.",
            ]),
            ("Palindrome", "Lead Business Analyst", "May 2021 – Dec 2021", [
                "Led a small team that built automated client dashboards and Power BI sales analytics on CRM data.",
            ]),
            ("SimbirSoft", "BI Developer", "Feb 2020 – Apr 2021", [
                "Built ClickHouse data marts for a goods-traceability system; Python data-quality tests.",
            ]),
            ("Russian Hack Team", "Data Scientist (freelance)", "2019 – 2023", [
                "7 first places at data science and ML hackathons, including Junction and Digital Breakthrough.",
            ]),
        ],
        "teach": [
            "<b>OTUS</b> — course lead, “AI for Analytics and Data” (first cohort 2026); instructor in product analytics courses.",
            "<b>Mentoring</b> — analysts and analytics leads: career growth, interviews, metrics and processes, analytics from scratch.",
            "<b>Speaking</b> — Delta Day 2025: how to grow a data-driven culture and know it's working.",
            "<b>Writing</b> — Telegram channel @givemeagold (in Russian), LinkedIn (in English).",
        ],
        "edu": [
            "RANEPA, Moscow — Data Analysis in Economics (incomplete higher education), 2022",
            "Moscow Institute of Physics and Technology — Phystech.Start accelerator, 2018",
        ],
        "skills": "SQL · Python · Spark · A/B testing and experimentation · metric design · factor analysis · ClickHouse · "
                  "Greenplum · PostgreSQL · Airflow · Tableau · Superset · Metabase · Power BI · DataLens · AI tools for "
                  "analytics (Claude Code, ChatGPT) · hiring and team leadership",
    },
    "ru": {
        "name": "Анастасия Гисина",
        "role": "Руководитель продуктовой аналитики",
        "contacts": "Москва · Telegram <b>@agisina</b> · linkedin.com/in/anastasiagisina · github.com/tpofd · tpofd.github.io",
        "summary": "6+ лет в продуктовой и бизнес-аналитике: Ozon, СберМаркет, Достависта, X5 Digital. Строю аналитику, которой "
                   "доверяют команды: метрики, эксперименты, BI и диагностика изменений метрик. Руководитель курса «ИИ для "
                   "аналитики» в OTUS, ментор, спикер.",
        "h_exp": "Опыт", "h_teach": "Преподавание, менторство, выступления", "h_edu": "Образование", "h_skills": "Навыки",
        "exp": [
            ("X5 Digital", "Руководитель продуктовой аналитики", "окт 2025 — н. в.", [
                "Руковожу и развиваю команду продуктовой аналитики, нанимаю middle и senior аналитиков.",
                "Построила ежедневный диагностический дашборд, который раскладывает изменение конверсии на коммерческие "
                "и продуктовые факторы: путь от «конверсия упала» до проверяемой гипотезы сократился с 1–3 недель до пары дней.",
                "Ввела правила A/B-тестов на общих экранах приложения: обязательные защитные метрики, общий календарь тестов, "
                "аналитик-владелец каждого экрана.",
                "Внедрила процесс сборки BI-дашбордов с ИИ-ассистентом: сначала макет, витрины под макет.",
            ]),
            ("Достависта", "Руководитель группы аналитики", "сен 2024 — окт 2025", [
                "Руководила аналитикой: 4 аналитика (продукт и маркетинг) и дата-инженер.",
                "Определила ключевые метрики, унифицировала отчётность и определения данных между командами.",
                "Выстроила BI-стек и витрины (Metabase, Delta BI, Trino), запустила self-service аналитику.",
                "Отвечала за процесс экспериментов: дизайн тестов, расчёт выборки, методы, правила решений.",
            ]),
            ("СберМаркет", "Старший продуктовый аналитик", "апр 2023 — авг 2024", [
                "С нуля построила аналитику нового B2B-продукта; его метрики попали на ключевые дашборды компании.",
                "Скоординировала пять отделов, чтобы измерить влияние продукта на операционные метрики; номинация на внутреннюю премию.",
                "Участвовала в ценообразовании и юнит-экономике: продукт вышел в положительную юнит-экономику.",
                "Проектировала B2B A/B-тесты и методику расчёта их результатов; менторила младших аналитиков.",
            ]),
            ("Ozon", "Продуктовый аналитик", "янв 2022 — фев 2023", [
                "Руководила переездом 100+ отчётов команды в Superset за 1,5 месяца.",
                "Запустила инструмент быстрого доступа к данным, сэкономивший команде 20+ часов в неделю.",
                "Построила отчётность для топ-менеджмента и методологию метрик контактного центра.",
            ]),
            ("Палиндром", "Руководитель группы бизнес-аналитики", "май 2021 — дек 2021", [
                "Руководила небольшой командой: автоматические дашборды для клиентов и аналитика продаж в Power BI на данных CRM.",
            ]),
            ("SimbirSoft", "BI-разработчик", "фев 2020 — апр 2021", [
                "Витрины в ClickHouse для системы прослеживаемости товаров, автотесты качества данных на Python.",
            ]),
            ("Russian Hack Team", "Data Scientist (фриланс)", "2019 — 2023", [
                "7 первых мест на хакатонах по анализу данных и ML, включая Junction и «Цифровой прорыв».",
            ]),
        ],
        "teach": [
            "<b>OTUS</b> — руководитель курса «ИИ для аналитики и работы с данными» (первый поток 2026), преподаватель курсов продуктовой аналитики.",
            "<b>Менторство</b> — аналитики и лиды аналитики: рост, собеседования, метрики и процессы, аналитика с нуля.",
            "<b>Выступления</b> — Delta Day 2025: как растить data-driven в компании и понять, что вырастили.",
            "<b>Авторство</b> — Telegram-канал @givemeagold, LinkedIn (на английском).",
        ],
        "edu": [
            "РАНХиГС, Москва — анализ данных в экономике (неоконченное высшее), 2022",
            "МФТИ — акселератор «Физтех.Старт», 2018",
        ],
        "skills": "SQL · Python · Spark · A/B-тесты и эксперименты · дизайн метрик · факторный анализ · ClickHouse · Greenplum · "
                  "PostgreSQL · Airflow · Tableau · Superset · Metabase · Power BI · DataLens · ИИ-инструменты для аналитики "
                  "(Claude Code, ChatGPT) · найм и руководство командой",
    },
}


def build(lang, out):
    d = DATA[lang]
    st = {
        "name": ParagraphStyle("name", fontName="Head", fontSize=22, leading=26, textColor=INK),
        "role": ParagraphStyle("role", fontName="Body", fontSize=12, leading=16, textColor=ACCENT, spaceBefore=2),
        "contacts": ParagraphStyle("c", fontName="Body", fontSize=8.5, leading=12, textColor=MUTED, spaceBefore=6),
        "body": ParagraphStyle("b", fontName="Body", fontSize=9.2, leading=12.8, textColor=INK, alignment=TA_LEFT),
        "h": ParagraphStyle("h", fontName="Head", fontSize=12, leading=15, textColor=INK, spaceBefore=8, spaceAfter=3),
        "co": ParagraphStyle("co", fontName="Body-Bold", fontSize=10, leading=13, textColor=INK),
        "dates": ParagraphStyle("dt", fontName="Body", fontSize=8.5, leading=13, textColor=MUTED),
        "bullet": ParagraphStyle("bl", fontName="Body", fontSize=8.9, leading=12.1, textColor=INK, leftIndent=9, bulletIndent=0),
    }
    story = [Paragraph(d["name"], st["name"]), Paragraph(d["role"], st["role"]), Paragraph(d["contacts"], st["contacts"]),
             Spacer(1, 6), Paragraph(d["summary"], st["body"]), Paragraph(d["h_exp"], st["h"])]
    for company, title, dates, bullets in d["exp"]:
        head = Table([[Paragraph(f"{company} — {title}", st["co"]), Paragraph(dates, st["dates"])]],
                     colWidths=[130 * mm, 44 * mm])
        head.setStyle(TableStyle([("ALIGN", (1, 0), (1, 0), "RIGHT"), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
        block = [head] + [Paragraph(b, st["bullet"], bulletText="•") for b in bullets] + [Spacer(1, 1)]
        story.append(KeepTogether(block))
    story.append(Paragraph(d["h_teach"], st["h"]))
    story += [Paragraph(t, st["bullet"], bulletText="•") for t in d["teach"]]
    story.append(Paragraph(d["h_edu"], st["h"]))
    story += [Paragraph(e, st["bullet"], bulletText="•") for e in d["edu"]]
    story.append(Paragraph(d["h_skills"], st["h"]))
    story.append(Paragraph(d["skills"], st["body"]))
    doc = SimpleDocTemplate(str(out), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=13 * mm,
                            bottomMargin=11 * mm, title=f"{d['name']} — {d['role']}", author=d["name"])
    doc.build(story)
    print(out)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    build("en", root / "resume_gisina_en.pdf")
    build("ru", root / "resume_gisina_ru.pdf")
