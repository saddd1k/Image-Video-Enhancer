<p align="center">
  <img src="assets/logo.png" height=400>
</p>

## <div align="center"><b><a href="README.md">English</a> | <a href="README_RU.md">Русский</a></b></div>

[![LICENSE](https://img.shields.io/github/license/xinntao/basicsr.svg)](https://github.com/xinntao/BasicSR/blob/master/LICENSE.txt)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3100/)
👀[**Демонстрация приложения**](#-демонстрация-приложения) **|** 🔧[**Установка**](#-зависимости-и-установка) **|** 🚩[**Обновления**](#-обновления) **|**

---

## Русский

### 📖 Real-ESRGAN: Обучение суперразрешению в реальных условиях с использованием полностью синтетических данных

> \[[Статья](https://arxiv.org/abs/2107.10833)]   \[[YouTube Видео](https://www.youtube.com/watch?v=fxHWoDSSvSc)]   \[[Обзор на BiliBili](https://www.bilibili.com/video/BV1H34y1m7sS/)]   \[[Постер](https://xinntao.github.io/projects/RealESRGAN_src/RealESRGAN_poster.pdf)]   \[[Слайды PPT](https://docs.google.com/presentation/d/1QtW6Iy8rm8rGLsJ0Ldti6kP-7Qyzy6XL/edit?usp=sharing&ouid=109799856763657548160&rtpof=true&sd=true)]<br>
> [Xintao Wang](https://xinntao.github.io/), Liangbin Xie, [Chao Dong](https://scholar.google.com.hk/citations?user=OSDCB0UAAAAJ), [Ying Shan](https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=en) <br>
> [Tencent ARC Lab](https://arc.tencent.com/en/ai-demos/imgRestore); Шэньчжэньский институт передовых технологий, Китайская академия наук
>
> взято из [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

<p align="center">
  <img src="assets/teaser.jpg">
</p>

### ✨ Возможности

* Высококачественное **увеличение изображений**
* **Интерполяция кадров** для более плавного видео (например, 24 → 48/60 FPS)
* Пакетная обработка для папок или отдельных файлов
* Аппаратное ускорение на GPU при наличии

---

## 🚩 Обновления

* ✅ Добавлено несколько моделей: RealESRGAN\_x2plus, RealESRGAN\_x4plus, RealESRGAN\_x4plus\_anime\_6B, realesr-animevideov3, GFPGANv1.3.
* ✅ В приложении доступны темы: тёмная, светлая и «замок».
* ✅ **BETA:** Поддержка интерполяции кадров.
* ✅ Добавлен раздел «О программе».
* ✅ Поддержка английского и русского языков.
* ✅ Реализовано увеличение изображений.
* ✅ Реализовано увеличение видео.
* ✅ Поддержка множества форматов изображений: .png, .jpg/.jpeg, .webp, .heic, .heif, .bmp.
* ✅ Поддержка множества форматов видео: .mp4, .mov, .mkv, .avi, .webm, .gif.
* ✅ Добавлена система предустановок для вкладки увеличения изображений.
* ✅ В предустановках сохраняются: путь к ffmpeg, папка вывода, язык и тема.

---

## 🔧 Зависимости и установка

* Python >=3.8, <=3.10
* PIP >= 22.0

---

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Sadddtop/Image-Video-Enhancer.git
cd Image-Video-Enhancer
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

---

Чтобы запустить программу, выполните команду:

```bash
python main.py
```

---

## 👀 Демонстрация приложения

### О программе (тёмная тема)

<p>
  <img src="assets/screenshots/About (dark theme).png">
</p>

### Генерация кадров (светлая тема)

<p>
  <img src="assets/screenshots/Frame generation (light theme).png">
</p>

### Обработка изображений (тема «замок»)

<p>
  <img src="assets/screenshots/Image processing (castle theme).png">
</p>

### Обработка видео (тёмная тема)

<p>
  <img src="assets/screenshots/Video processing (dark theme).png">
</p>

---

## 📖 Благодарности

▶️ [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN): инструмент для увеличения разрешения <br>
▶️ [GFPGAN](https://github.com/TencentARC/GFPGAN): алгоритм восстановления лиц <br>
▶️ [BasicSR](https://github.com/xinntao/BasicSR): инструментарий для восстановления изображений и видео <br>
▶️ [RIFE](https://github.com/hzwer/ECCV2022-RIFE): метод интерполяции видео в реальном времени <br>

---