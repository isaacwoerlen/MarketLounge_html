@echo off
REM === Génération de la documentation miroir ===

cd /d "%~dp0mirror"

REM 🐍 Exécuter le script Python avec log
echo Lancement du script Python...
python generate_doc.py > log.txt 2>&1

REM 🔍 Vérifier si le log contient une erreur
findstr /i "Traceback Error Exception" log.txt >nul
if %errorlevel%==0 (
    echo ❌ Une erreur est survenue. Ouverture du journal...
    notepad log.txt
) else (
    echo ✅ Documentation générée avec succès.
)

pause
