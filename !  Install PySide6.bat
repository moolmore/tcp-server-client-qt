@echo off
chcp 65001 > nul
cls

:: ==========================================================
:: Скрипт разработан при участии Google Search LLM
:: Назначение: Исправленная проверка и установка PySide6
:: ==========================================================

echo ==========================================================
echo  Запуск скрипта установки...
echo  Подготовлено ИИ-ассистентом (Google Search LLM)
echo ==========================================================
echo.

:: Шаг 1: Проверка установлен ли Python
echo [1/3] Проверка наличия Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ОШИБКА] Python не найден в системе!
    echo Пожалуйста, установите Python и добавьте его в переменную PATH.
    goto end
)
echo [OK] Python обнаружен.
echo.

:: Шаг 2: Проверка наличия PySide6 (с правильным регистром букв)
echo [2/3] Проверка наличия библиотеки PySide6...
python -c "import PySide6" >nul 2>&1

if %errorlevel% equ 0 (
    echo [ОК] Библиотека PySide6 уже установлена в вашей системе.
    goto success
) else (
    echo [ИНФО] PySide6 не найден. Начинаем установку...
    echo.
)

:: Шаг 3: Установка PySide6
echo [3/3] Обновление pip и установка PySide6...
python -m pip install --upgrade pip
python -m pip install pyside6

:: Итоговая проверка после установки
python -c "import PySide6" >nul 2>&1
if %errorlevel% equ 0 (
    goto success
) else (
    echo.
    echo [ОШИБКА] Не удалось установить PySide6. Проверьте подключение к интернету.
    goto end
)

:success
echo.
echo ==========================================================
echo [УСПЕШНО] Всё готово! PySide6 доступен для использования.
echo ==========================================================
goto end

:end
echo.
echo Для выхода нажмите любую клавишу...
pause > nul
