@echo off
cd /d "%~dp0"

echo Initialisation du dépôt Git...
git init

echo Configuration du dépôt distant...
git remote add origin https://github.com/isaac/MarketLounge_html.git

echo Ajout des fichiers...
git add .

echo Saisie du message de commit...
set /p commitMsg="Message de commit : "
git commit -m "%commitMsg%"

echo Poussée vers GitHub...
git branch -M main
git push -u origin main

echo.
echo ✅ Poussée terminée avec succès !
pause
