from pathlib import Path
from html.parser import HTMLParser
import zipfile
p=Path('outputs/e-portfolio')
class Check(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ['src','href'] and v and not v.startswith(('#','https:','http:','mailto:')):
    target=v.split('#')[0]
    assert (p/target).is_file(),target
for name in ['index.html','cv.html']:Check().feed((p/name).read_text())
report='''# Vérifications de la première version\n\n- Syntaxe JavaScript : valide.\n- Contrôles exécutés avec un DOM simulé : filtres de projets, ouverture et fermeture des détails, classement décroissant de la timeline, contacts vides et renseignés, message CV sans PDF.\n- Tous les fichiers locaux référencés par les pages HTML existent.\n- Résolution des chemins vérifiée avec une URL de dépôt GitHub Pages en sous-dossier.\n- Menu mobile, styles adaptatifs, focus clavier et réduction des animations présents dans le code.\n\n## Limite de vérification\n\nLe serveur HTTP local a été refusé par l’environnement et le navigateur de test n’a pas pu démarrer. L’affichage réel sur ordinateur et mobile, la lecture multimédia, le presse-papiers et l’aperçu PDF n’ont donc pas été validés dans un navigateur. Les contrôles avec DOM simulé ne remplacent pas une vérification visuelle. Les médias personnels ne sont pas encore renseignés.\n\nAucun dépôt connecté, aucune publication effectuée.\n'''
(p/'VERIFICATIONS.md').write_text(report)
with zipfile.ZipFile('outputs/e-portfolio.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(p.rglob('*')):
  if f.is_file():z.write(f,Path('e-portfolio')/f.relative_to(p))
print('Liens locaux valides. Archive créée avec GitHub Actions et dossiers médias.')
