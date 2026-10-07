<div align="center">

# 🐍 Python Learning

### Минимальный песочный репозиторий для практики Python + CI

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/license-Private-red?style=for-the-badge)](https://github.com/Antisakrum2004/python_learning)

<br/>

<img src="https://img.shields.io/github/last-commit/Antisakrum2004/python_learning?style=flat-square&color=3776AB" alt="last commit" />
<img src="https://img.shields.io/github/languages/top/Antisakrum2004/python_learning?style=flat-square" alt="top language" />
<img src="https://img.shields.io/github/actions/workflow/status/Antisakrum2004/python_learning/python-ci.yml?style=flat-square&label=CI" alt="CI" />

</div>

---

## О проекте

Крошечный учебный репозиторий: знакомство с Python, pytest и Playwright UI-тестами, плюс GitHub Actions workflows.

| | |
|:---|:---|
| **Тесты** | `test_ui_playwright.py` |
| **CI** | `.github/workflows/python-ci.yml` · `django.yml` |
| **Цель** | учиться пайплайнам, не продакшен |

---

## Структура

```text
python_learning/
├── test_ui_playwright.py
├── .gitignore
└── .github/workflows/
    ├── python-ci.yml
    └── django.yml
```

---

## Локальный запуск

```bash
python -m pip install --upgrade pip
pip install pytest playwright
playwright install
pytest test_ui_playwright.py -v
```

---

<div align="center">

**Learn by breaking things safely 🧪**

</div>
