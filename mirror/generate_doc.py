import os
from pathlib import Path
import shutil

# Configuration
ROOT_DIR = Path(__file__).resolve().parent.parent / "apps"
CSS_SOURCE = Path("style.css")
EXCLUDED_DIRS = {"__pycache__"}  # "tests" est maintenant inclus

def get_section_title(depth):
    if depth == 0:
        return "Applications"
    elif depth == 1:
        return "Apps"
    else:
        return "Répertoire"

def generate_index(app_path, files, subdirs, title="Index", depth=0):
    file_links = "\n".join(f'<li><a href="{file.name}">{file.name}</a></li>' for file in files)
    subdir_links = "\n".join(f'<li><a href="{subdir.name}/index.html">{subdir.name}</a></li>' for subdir in subdirs)
    section_title = get_section_title(depth)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>{title}</h1>
    <h2 style="color: #2e8b57;">Fichiers</h2>
    <ul>{file_links}</ul>
    <h2 style="color: #2e8b57;">{section_title}</h2>
    <ul>{subdir_links}</ul>
</body>
</html>
"""
    with open(app_path / "index.html", "w", encoding="utf-8") as f:
        f.write(html)

    # Copie du CSS dans le dossier courant
    if CSS_SOURCE.exists():
        shutil.copyfile(CSS_SOURCE, app_path / "style.css")
total_dirs = 0
total_files = 0

def process_directory(path, depth=0):
    global total_dirs, total_files

    for root, dirs, files in os.walk(path):
        root_path = Path(root)
        rel_path = root_path.relative_to(ROOT_DIR)
        if any(part in EXCLUDED_DIRS for part in rel_path.parts):
            continue

        html_files = [Path(root) / f for f in files if f.endswith(".html") and f != "index.html"]
        subdirs = [Path(root) / d for d in dirs if d not in EXCLUDED_DIRS]

        total_dirs += len(subdirs)
        total_files += len(html_files)

        title = f"Documentation de {rel_path.name}" if rel_path.parts else "Documentation principale"
        generate_index(root_path, html_files, subdirs, title=title, depth=len(rel_path.parts))

    for root, dirs, files in os.walk(path):
        root_path = Path(root)
        rel_path = root_path.relative_to(ROOT_DIR)
        if any(part in EXCLUDED_DIRS for part in rel_path.parts):
            continue

        html_files = [Path(root) / f for f in files if f.endswith(".html") and f != "index.html"]
        subdirs = [Path(root) / d for d in dirs if d not in EXCLUDED_DIRS]

        title = f"Documentation de {rel_path.name}" if rel_path.parts else "Documentation principale"
        generate_index(root_path, html_files, subdirs, title=title, depth=len(rel_path.parts))

# Exécution
process_directory(ROOT_DIR)

print(f"{total_dirs} dossiers et {total_files} fichiers indexés.")
print("Documentation générée avec succès.")


