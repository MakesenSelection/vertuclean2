# -*- coding: utf-8 -*-
"""
Genere les pages service de VERTUCLEAN.

Le CSS, le sprite d'icones, l'en-tete et le pied de page sont EXTRAITS
de index.html a chaque execution : la charte ne peut pas diverger.
La sortie reste du HTML monofichier, sans dependance a l'execution —
la contrainte du projet est respectee.

Usage :  python3 outils/build-pages.py
"""
import io, os, re, json, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.vertuclean.fr"
TEL, MAIL = "07 55 61 45 67", "contact@vertuclean.fr"

def read(p): return io.open(os.path.join(BASE, p), encoding='utf-8').read()

src = read('index.html')
CSS    = src[src.index('    <style>') + len('    <style>') : src.index('    </style>')]
SPRITE = src[src.index('<svg width="0" height="0"') : src.index('</svg>\n\n<!-- ══ LOGO') + len('</svg>')]
FOOTER = src[src.index('<footer class="site-footer">') : src.index('</footer>') + len('</footer>')]
FOOTER = FOOTER.replace('href="#services"', 'href="index.html#services"') \
               .replace('href="index.html"', 'href="index.html"')

def esc(t):  # dans du texte de contenu, seuls & < > sont echappes
    return html.escape(t, quote=False)

# ══════════════════════════════════════════════════════════════
#  Les pages
# ══════════════════════════════════════════════════════════════
PAGES = [

{
 'file': 'nettoyage-vapeur-technique.html',
 'nav':  'Nettoyage vapeur technique',
 'national': True,
 'title': "Nettoyage Vapeur Technique Professionnel — Industrie, Engins, Façades | VERTUCLEAN",
 'desc':  "Nettoyage à la vapeur sèche haute température pour professionnels : machines industrielles, tracteurs et engins agricoles, aéronefs, matériel nautique, façades, patrimoine, cuisines. Sans détergent, eau réduite. Intervention partout en France.",
 'kw':    "nettoyage vapeur industriel, nettoyage vapeur professionnel, dégraissage vapeur machine, nettoyage vapeur façade, nettoyage vapeur tracteur, nettoyage vapeur aéronautique, nettoyage vapeur bateau, alternative karcher haute pression, nettoyage sans détergent industriel",
 'eyebrow': "Prestation technique · Toute la France",
 'h1':    ["Nettoyage vapeur", "technique"],
 'lede':  "La vapeur sèche haute température décolle graisses, résidus de production et souillures incrustées sans aucun détergent, là où le nettoyage classique atteint ses limites. VERTUCLEAN intervient partout en France pour les chantiers techniques.",
 'img':   ('nettoyage-fin-chantier-lot-aveyron.jpg', 1000, 546,
           "Nettoyage vapeur technique professionnel réalisé par VERTUCLEAN"),
 'tag':   ("Sans détergent", "Consommation d'eau divisée par dix"),
 'intro_h2': ["Un procédé", "sans produit"],
 'intro': [
   "Le nettoyage vapeur projette de l'eau portée à très haute température sous forme de vapeur sèche, c'est-à-dire faiblement chargée en eau liquide. La chaleur ramollit et dissout les corps gras, tandis que le faible débit d'eau emporte les résidus décollés. Le nettoyage s'obtient donc par l'énergie thermique, et non par un agent chimique ou par la force d'un jet.",
   "Cette différence est décisive sur les supports sensibles. Là où un nettoyeur haute pression classique érode la pierre, chasse les joints ou fait pénétrer l'eau dans des logements électriques, la vapeur agit à pression modérée et laisse le support intact. C'est ce qui la rend utilisable aussi bien sur une machine de production que sur une statue.",
   "Elle est également décisive sur le plan environnemental. Aucun détergent n'étant employé, il n'y a pas de rinçage chargé en tensioactifs, donc aucun ruissellement polluant vers les sols et les nappes phréatiques. La consommation d'eau se compte en litres là où un jet haute pression se compte en centaines de litres.",
 ],
 'blocks_h2': ["Les domaines", "d'intervention"],
 'blocks_sub': "La vapeur s'emploie partout où il faut dégraisser, désinfecter ou décaper sans agresser le support ni recourir à la chimie.",
 'blocks': [
   ("Industrie & production", "Machines-outils, lignes et convoyeurs, moules, ateliers, matériel de manutention. Le dégraissage se fait en place, sans démontage et sans immobiliser la machine dans un bain de solvant."),
   ("Engins agricoles & TP", "Tracteurs, moissonneuses, pulvérisateurs, pelles et chargeuses. La vapeur retire les boues séchées, les résidus végétaux et les graisses de graissage, y compris dans les recoins de châssis."),
   ("Aéronautique", "Cellules, trains d'atterrissage, intérieurs de cabine. Le très faible volume d'eau projeté et l'absence de produit corrosif conviennent aux exigences du secteur."),
   ("Nautisme", "Coques, ponts, aménagements intérieurs, moteurs hors-bord. La vapeur décolle sel, algues et gasoil sans rejeter de détergent dans le milieu."),
   ("Façades & extérieurs", "Façades, murets, portails, portes de garage, menuiseries PVC, mobilier de jardin. Elle élimine mousses, lichens et noircissements sans décaper l'enduit ni décolorer le PVC."),
   ("Patrimoine", "Statues, monuments, pierre de taille, ferronneries. Le nettoyage se fait sans abrasion, sans microfissuration et sans dépôt chimique dans la porosité de la pierre."),
   ("Cuisines professionnelles", "Sols antidérapants, plans de travail, hottes et filtres à graisse, chambres froides. La chaleur dégraisse et assainit en une seule opération, sans biocide sur des surfaces au contact alimentaire."),
   ("Remises en état lourdes", "Logements en situation d'incurie, dont les cas de syndrome de Diogène. La vapeur traite en profondeur des surfaces très dégradées et neutralise les odeurs incrustées."),
 ],
 'why_h2': ["Pourquoi la vapeur", "plutôt qu'un jet"],
 'why': [
   ("Pouvoir nettoyant élevé", "la chaleur dissout graisses et dépôts incrustés que l'eau froide ne décolle pas"),
   ("Action bactéricide", "obtenue par la seule température, sans ajout de biocide ni de désinfectant"),
   ("Gros débit de travail", "de grandes surfaces traitées en une seule intervention"),
   ("Aucun produit toxique", "donc aucun résidu chimique sur les surfaces traitées, ni pour vos équipes ni pour vos clients"),
   ("Pas de ruissellement polluant", "aucun rejet de détergent vers les sols et les nappes phréatiques, contrairement au nettoyage haute pression"),
   ("Consommation d'eau très réduite", "quelques litres là où un jet haute pression en consomme des centaines"),
   ("Supports préservés", "pression modérée : ni érosion de la pierre, ni joints chassés, ni infiltration dans les circuits"),
 ],
 'zone_h2': ["Une intervention", "partout en France"],
 'zone_txt': "Les chantiers techniques ne connaissent pas de frontière départementale. VERTUCLEAN est basé à Cajarc, dans le Lot, et se déplace sur l'ensemble du territoire pour les interventions vapeur d'envergure : sites industriels, exploitations agricoles, collectivités, chantiers de patrimoine et remises en état lourdes. Le déplacement est chiffré dans le devis.",
 'faq': [
   ("Le nettoyage vapeur peut-il remplacer un nettoyeur haute pression ?",
    "Sur la plupart des applications de dégraissage et d'assainissement, oui, et avec un meilleur résultat sur les supports fragiles. La vapeur agit par la chaleur et non par la force du jet : elle décolle les graisses que la pression seule ne retire pas, tout en préservant la pierre, les joints, les peintures et les circuits électriques. La haute pression conserve un avantage sur le décapage purement mécanique de grandes surfaces très résistantes."),
   ("La vapeur désinfecte-t-elle vraiment ?",
    "La vapeur portée à haute température exerce une action bactéricide par la chaleur seule, sans ajout de biocide. C'est ce qui la rend particulièrement adaptée aux cuisines professionnelles, aux surfaces au contact alimentaire et aux locaux où l'on souhaite éviter tout résidu chimique. Pour une désinfection réglementée soumise à protocole, la vapeur vient en complément du protocole en vigueur, pas en remplacement."),
   ("Le nettoyage vapeur abîme-t-il les surfaces fragiles ?",
    "Non, c'est même son principal intérêt sur le patrimoine et les supports sensibles. La pression appliquée reste modérée : il n'y a ni abrasion de la pierre, ni microfissuration, ni joints chassés, ni décoloration du PVC. Chaque support fait l'objet d'un réglage de température et de débit adapté, testé sur une zone discrète avant l'intervention."),
   ("Combien d'eau consomme un nettoyage vapeur ?",
    "Quelques litres, là où un nettoyeur haute pression en consomme plusieurs centaines pour la même surface. La vapeur sèche est faiblement chargée en eau liquide : elle nettoie par l'énergie thermique et non par le volume. C'est un avantage direct sur les sites sans arrivée d'eau abondante et sur les chantiers où la gestion des effluents pose problème."),
   ("VERTUCLEAN se déplace-t-il hors du Lot pour ces chantiers ?",
    "Oui. Les prestations vapeur techniques sont assurées partout en France. VERTUCLEAN est basé à Cajarc (46160) et intervient sur les sites industriels, les exploitations agricoles, les chantiers de patrimoine et les remises en état lourdes sur l'ensemble du territoire. Le déplacement est intégré au devis."),
 ],
 'schema': {"name":"Nettoyage vapeur technique professionnel",
            "serviceType":"Nettoyage industriel à la vapeur",
            "area":["France"]},
},

{
 'file': 'nettoyage-vitres-lot-aveyron.html',
 'nav':  'Nettoyage de vitres',
 'title': "Nettoyage de Vitres Lot & Aveyron — Eau Pure, Vitrines, Baies Vitrées | VERTUCLEAN",
 'desc':  "Nettoyage de vitres écologique dans le Lot et l'Aveyron : baies vitrées, vitrines commerciales, vitrages en hauteur à l'eau pure déminéralisée. −50 % pour les particuliers (SAP). Cahors, Figeac, Rodez, Cajarc.",
 'kw':    "nettoyage vitres Lot, nettoyage vitres Cahors, nettoyage vitres Figeac, nettoyage vitres Rodez, laveur de vitres Aveyron, nettoyage vitrine commerce, nettoyage eau pure, nettoyage baie vitrée Cajarc",
 'eyebrow': "Vitres & baies vitrées · Lot & Aveyron",
 'h1':    ["Nettoyage", "de vitres"],
 'lede':  "Baies vitrées, vitrines commerciales, vérandas et vitrages en hauteur. Pour les grandes surfaces vitrées, nous travaillons à l'eau pure déminéralisée : aucun détergent, aucune trace au séchage.",
 'img':   ('nettoyage-vitres-baie-vitree-lot-aveyron.jpg', 1400, 764,
           "Baie vitrée nettoyée par VERTUCLEAN dans le Lot"),
 'tag':   ("−50 % pour les particuliers", "Crédit d'impôt Services à la Personne"),
 'intro_h2': ["L'eau pure,", "sans une trace"],
 'intro': [
   "L'eau du robinet contient du calcaire et des minéraux dissous. En s'évaporant sur une vitre, elle les dépose : ce sont eux qui forment les traces et les auréoles, pas la saleté. L'eau pure est une eau déminéralisée dont on a retiré ces minéraux. Comme elle ne laisse rien en séchant, la vitre sèche seule, sans essuyage et sans la moindre trace.",
   "Le procédé se passe entièrement de détergent : c'est l'eau elle-même, chimiquement « avide », qui capte les salissures. Appliquée par une brosse montée sur perche télescopique alimentée depuis le sol, elle permet d'atteindre les vitrages en hauteur sans nacelle ni échafaudage. L'intervention est plus rapide, sensiblement plus sûre, et sans produit chimique projeté sur les façades ou les plantations.",
   "C'est la méthode que nous privilégions pour les vitreries commerciales d'envergure, les vérandas, les bâtiments à étages et toutes les surfaces vitrées difficiles d'accès. Pour les vitrages courants et les finitions intérieures, le travail à la raclette reste le geste le plus précis.",
 ],
 'blocks_h2': ["Ce que nous", "nettoyons"],
 'blocks_sub': "Chez les particuliers comme chez les professionnels, à l'intérieur comme à l'extérieur.",
 'blocks': [
   ("Baies vitrées & vérandas", "Grandes surfaces vitrées, verrières, vérandas et jardins d'hiver, y compris les traverses et les rails."),
   ("Vitrines commerciales", "Devantures de commerces, agences et restaurants. Passage régulier possible, tôt le matin ou après fermeture."),
   ("Vitrages en hauteur", "Étages, imposte, bâtiments professionnels — traités à l'eau pure depuis le sol, sans nacelle."),
   ("Menuiseries & encadrements", "Dormants, ouvrants, joints et appuis : la vitre propre dans un cadre sale ne tient pas la journée."),
   ("Volets & garde-corps", "Volets roulants, persiennes, garde-corps vitrés et rambardes de balcon."),
   ("Après chantier", "Retrait des films de protection, des projections de peinture, d'enduit et de silicone sur les vitrages neufs."),
 ],
 'why_h2': ["Pourquoi nous", "confier vos vitres"],
 'why': [
   ("−50 % pour les particuliers", "VERTUCLEAN est agréé Services à la Personne : la moitié du montant est déductible de vos impôts"),
   ("Produits biodégradables", "sans perturbateurs endocriniens ni composés organiques volatils"),
   ("Sans nacelle ni échafaudage", "les vitrages en hauteur sont traités à la perche depuis le sol, sans installation lourde"),
   ("Séchage sans trace", "l'eau pure ne dépose aucun minéral : aucune auréole, aucun essuyage"),
   ("Artisan local", "basé à Cajarc, intervention rapide dans tout le Lot et l'Aveyron"),
   ("English spoken", "un interlocuteur anglophone pour les propriétaires étrangers de la région"),
 ],
 'zone_h2': ["Où nous", "intervenons"],
 'zone_txt': "Le nettoyage de vitres est assuré dans tout le Lot (46) et l'Aveyron (12) : Cajarc, Figeac, Cahors, Lacapelle-Marival, Béduer, Limogne-en-Quercy, Saint-Céré, Gramat, Rodez, Villefranche-de-Rouergue, Decazeville, Onet-le-Château et les communes environnantes. Nous intervenons également dans les départements limitrophes : Dordogne (24), Corrèze (19), Cantal (15), Tarn-et-Garonne (82) et Lot-et-Garonne (47).",
 'faq': [
   ("Qu'est-ce que le nettoyage de vitres à l'eau pure ?",
    "C'est un nettoyage réalisé avec une eau déminéralisée, débarrassée de son calcaire et de ses minéraux. Ce sont ces minéraux qui laissent des traces en séchant : une eau qui n'en contient plus s'évapore sans rien déposer. La vitre sèche donc seule, sans essuyage et sans auréole, et sans qu'aucun détergent soit employé."),
   ("Jusqu'à quelle hauteur pouvez-vous nettoyer sans nacelle ?",
    "La perche télescopique alimentée en eau pure permet de travailler depuis le sol jusqu'aux étages courants d'un bâtiment. Cela couvre la très grande majorité des maisons, commerces et bâtiments professionnels de la région, sans nacelle, sans échafaudage et sans les délais ni les coûts que ces installations impliquent."),
   ("Le nettoyage de vitres ouvre-t-il droit au crédit d'impôt ?",
    "Oui pour les particuliers. VERTUCLEAN est agréé au titre des Services à la Personne : 50 % du montant réglé est déductible de vos impôts, sous la forme d'un crédit d'impôt. Vous recevez l'attestation fiscale correspondante. Le dispositif ne s'applique pas aux prestations réalisées pour des professionnels."),
   ("À quelle fréquence faire nettoyer une vitrine commerciale ?",
    "Cela dépend de l'exposition. Une vitrine en centre-ville, exposée à la poussière et aux projections de la voirie, gagne à être nettoyée toutes les deux à quatre semaines. Un local plus abrité peut tenir un trimestre. Nous convenons d'un passage régulier, tôt le matin ou après la fermeture, pour ne pas gêner votre activité."),
   ("Nettoyez-vous aussi les encadrements et les menuiseries ?",
    "Oui, et c'est indissociable du reste. Un vitrage impeccable dans un cadre encrassé se resalit dès la première pluie, l'eau entraînant les dépôts du dormant sur le verre. Nous traitons systématiquement les dormants, les ouvrants, les joints et les appuis de fenêtre."),
 ],
 'schema': {"name":"Nettoyage de vitres et baies vitrées",
            "serviceType":"Nettoyage de vitres",
            "area":["Lot","Aveyron","Dordogne","Corrèze","Cantal","Tarn-et-Garonne","Lot-et-Garonne"]},
},


{
 'file': 'nettoyage-textiles-canapes-lot-aveyron.html',
 'nav':  'Nettoyage de textiles',
 'title': "Nettoyage Canapé, Moquette & Tapis à la Vapeur — Lot & Aveyron | VERTUCLEAN",
 'desc':  "Nettoyage écologique de canapés, moquettes, tapis et matelas à la vapeur dans le Lot et l'Aveyron. Élimination des acariens et allergènes sans produit chimique agressif. −50 % pour les particuliers (SAP).",
 'kw':    "nettoyage canapé Lot, nettoyage moquette Aveyron, nettoyage tapis Cahors, nettoyage matelas Figeac, nettoyage vapeur textile, anti acariens canapé, injecteur extracteur Rodez",
 'eyebrow': "Textiles & canapés · Lot & Aveyron",
 'h1':    ["Nettoyage", "de textiles"],
 'lede':  "Canapés, fauteuils, moquettes, tapis et matelas traités à la vapeur. Les acariens et les allergènes sont éliminés par la chaleur, sans produit chimique agressif et sans odeur résiduelle.",
 'img':   ('nettoyage-textile-canape-lot-aveyron.jpg', 1000, 562,
           "Nettoyage vapeur d'un canapé par VERTUCLEAN dans le Lot"),
 'tag':   ("Acariens & allergènes", "Éliminés par la chaleur, sans biocide"),
 'intro_h2': ["La vapeur", "plutôt que la chimie"],
 'intro': [
   "Un canapé absorbe tout : transpiration, poussière, squames, résidus alimentaires. Cette matière organique nourrit les acariens, dont les déjections sont la première cause d'allergie respiratoire domestique. Un shampooing de surface masque le problème ; il ne l'atteint pas.",
   "La vapeur, elle, agit en profondeur. Portée à haute température, elle traverse les fibres, dissout les corps gras et neutralise les acariens par la chaleur seule, sans biocide. Sur les salissures les plus incrustées, nous complétons par un passage à l'injecteur-extracteur : le textile est humidifié puis immédiatement réaspiré, ce qui extrait la saleté dissoute au lieu de l'enfoncer.",
   "L'avantage est aussi sanitaire au quotidien. Aucun détergent n'étant laissé dans les fibres, il n'y a pas de résidu chimique au contact de la peau, ni d'odeur persistante. Le textile sèche en quelques heures et redevient immédiatement utilisable.",
 ],
 'blocks_h2': ["Ce que nous", "traitons"],
 'blocks_sub': "Chez les particuliers, dans les gîtes et chambres d'hôtes, et dans les locaux professionnels.",
 'blocks': [
   ("Canapés & fauteuils", "Tissu, microfibre, alcantara. Assises, dossiers, accoudoirs et coussins déhoussables ou non."),
   ("Matelas", "Traitement anti-acariens en profondeur, particulièrement utile en chambre d'enfant et pour les personnes allergiques."),
   ("Moquettes & sols textiles", "Chambres, bureaux, parties communes. Détachage ciblé puis passage complet à l'injecteur-extracteur."),
   ("Tapis", "Tapis de salon, descentes de lit, tapis d'escalier — traités sur place ou en atelier selon la nature des fibres."),
   ("Sièges de véhicule", "Traitement vapeur des sièges, ciel de toit et moquettes de coffre, en complément du nettoyage de véhicule."),
   ("Gîtes & meublés", "Remise en état des couchages et assises entre deux locations, avec attestation d'intervention si besoin."),
 ],
 'why_h2': ["Pourquoi la vapeur", "sur un textile"],
 'why': [
   ("Acariens neutralisés", "par la chaleur seule, sans acaricide chimique laissé dans les fibres"),
   ("Aucun résidu au contact de la peau", "pas de détergent piégé dans le tissu après séchage"),
   ("Pas d'odeur persistante", "contrairement aux shampooings moussants qui laissent un parfum de couverture"),
   ("Séchage rapide", "quelques heures : le meuble reste utilisable le jour même"),
   ("−50 % pour les particuliers", "prestation éligible au crédit d'impôt Services à la Personne"),
   ("Fibres préservées", "réglage de température adapté à chaque matière, testé sur une zone cachée"),
 ],
 'zone_h2': ["Où nous", "intervenons"],
 'zone_txt': "Le nettoyage de textiles est assuré à domicile dans tout le Lot (46) et l'Aveyron (12) : Cajarc, Figeac, Cahors, Lacapelle-Marival, Limogne-en-Quercy, Saint-Céré, Gramat, Rodez, Villefranche-de-Rouergue, Decazeville et les communes environnantes, ainsi que dans les départements limitrophes — Dordogne (24), Corrèze (19), Cantal (15), Tarn-et-Garonne (82) et Lot-et-Garonne (47).",
 'faq': [
   ("Combien de temps un canapé met-il à sécher ?",
    "Comptez deux à quatre heures selon l'épaisseur du garnissage, la matière et la ventilation de la pièce. La vapeur sèche est faiblement chargée en eau et l'injecteur-extracteur réaspire immédiatement l'humidité injectée : le textile n'est jamais détrempé. Il est généralement utilisable le soir même."),
   ("Le nettoyage vapeur élimine-t-il vraiment les acariens ?",
    "Oui. Les acariens et leurs déjections, principaux allergènes de la literie et des assises, ne résistent pas à la température de la vapeur. L'intérêt du procédé est d'obtenir ce résultat par la seule chaleur, sans laisser d'acaricide chimique dans des fibres au contact quotidien de la peau."),
   ("Toutes les matières supportent-elles la vapeur ?",
    "La grande majorité, oui, à condition d'adapter la température et le débit. Certaines soies anciennes, viscoses et cuirs non protégés demandent une autre approche. Nous vérifions systématiquement l'étiquette d'entretien et faisons un essai sur une zone cachée avant de traiter l'ensemble."),
   ("Les taches anciennes partent-elles ?",
    "Souvent, mais sans garantie absolue. Une tache grasse ou alimentaire, même ancienne, se dissout généralement bien à la vapeur. En revanche, un colorant ayant teint la fibre — vin, encre, javel — a modifié la matière elle-même : le nettoyage l'atténue sans toujours l'effacer. Nous vous le disons avant d'intervenir plutôt qu'après."),
   ("Le nettoyage de canapé donne-t-il droit au crédit d'impôt ?",
    "Oui pour les particuliers. VERTUCLEAN est agréé Services à la Personne : 50 % du montant réglé revient sous forme de crédit d'impôt, avec l'attestation fiscale correspondante. Le dispositif ne s'applique pas aux prestations facturées à des professionnels."),
 ],
 'schema': {"name":"Nettoyage de textiles, canapés, moquettes et tapis",
            "serviceType":"Nettoyage de textiles à la vapeur",
            "area":["Lot","Aveyron","Dordogne","Corrèze","Cantal","Tarn-et-Garonne","Lot-et-Garonne"]},
},

{
 'file': 'nettoyage-fin-de-chantier-lot-aveyron.html',
 'nav':  'Fin de chantier',
 'title': "Nettoyage Fin de Chantier Lot & Aveyron — Après Travaux | VERTUCLEAN",
 'desc':  "Nettoyage de fin de chantier dans le Lot et l'Aveyron : élimination des poussières de plâtre, ciment et peinture après travaux, rénovation ou construction neuve. Livraison prête à la remise des clés.",
 'kw':    "nettoyage fin de chantier Lot, nettoyage après travaux Aveyron, nettoyage après rénovation Cahors, remise des clés Figeac, nettoyage construction neuve Rodez, dépoussiérage chantier",
 'eyebrow': "Fin de chantier · Lot & Aveyron",
 'h1':    ["Nettoyage de", "fin de chantier"],
 'lede':  "Après travaux, rénovation ou construction neuve. Nous retirons les poussières de plâtre, de ciment et de ponçage, les projections de peinture et les protections, pour livrer un espace immédiatement habitable.",
 'img':   ('nettoyage-fin-chantier-lot-aveyron.jpg', 1000, 546,
           "Nettoyage de fin de chantier après travaux par VERTUCLEAN"),
 'tag':   ("Prêt à la remise des clés", "Artisans, maîtres d'œuvre et particuliers"),
 'intro_h2': ["La poussière", "de chantier"],
 'intro': [
   "La poussière de chantier n'est pas de la poussière ordinaire. Le plâtre, le ciment et le ponçage produisent des particules très fines, abrasives et électrostatiques : elles se redéposent en continu pendant des semaines, s'insinuent dans les rainures de parquet, les grilles de VMC, les rails de placard et les corps de radiateur. Un simple coup de balai les remet en suspension au lieu de les retirer.",
   "Le nettoyage de fin de chantier suit donc un ordre précis, du haut vers le bas et du fond vers la sortie, avec une aspiration filtrée à chaque étape plutôt qu'un balayage. Les résidus durs — laitance de ciment, points de colle, silicone, projections de peinture — sont retirés au grattoir et à la vapeur avant tout lavage, sinon le lavage ne fait que les étaler.",
   "Cette prestation conditionne directement la perception du chantier. Un ouvrage impeccablement exécuté mais livré poussiéreux se reçoit mal ; le même ouvrage livré net paraît mieux fini. C'est le dernier geste, et c'est celui que le client voit en premier.",
 ],
 'blocks_h2': ["Ce que comprend", "l'intervention"],
 'blocks_sub': "Pour les artisans et maîtres d'œuvre en fin de lot, comme pour les particuliers en fin de rénovation.",
 'blocks': [
   ("Dépose des protections", "Retrait des films, adhésifs, bâches et cartons de protection, y compris les résidus de colle laissés sur les supports."),
   ("Aspiration filtrée", "Sols, plinthes, angles, gaines et rainures, avec filtration adaptée aux particules fines de plâtre et de ciment."),
   ("Vitrages neufs", "Retrait des films de protection, des projections de peinture, d'enduit et de silicone sur le verre et les menuiseries."),
   ("Sanitaires & cuisine", "Élimination de la laitance de ciment, des points de silicone et des traces de calcaire sur la faïence et les inox."),
   ("Sols de finition", "Lavage adapté au revêtement : carrelage, parquet, béton ciré, vinyle. Décapage de la laitance si nécessaire."),
   ("Menuiseries & équipements", "Portes, plinthes, interrupteurs, radiateurs, grilles de ventilation, rails et coulisses de placard."),
 ],
 'why_h2': ["Ce qui change", "avec nous"],
 'why': [
   ("Vapeur sur les résidus durs", "silicone, colle et projections retirés par la chaleur, sans solvant agressif"),
   ("Aspiration filtrée", "les particules fines sont captées, pas remises en suspension"),
   ("Produits biodégradables", "aucun résidu chimique dans un logement qui va être occupé"),
   ("Intervention en fin de lot", "coordination possible avec votre planning de livraison"),
   ("Grands chantiers", "déplacement partout en France pour les opérations d'envergure"),
   ("Deuxième passage", "après les inévitables retouches, sur demande"),
 ],
 'zone_h2': ["Où nous", "intervenons"],
 'zone_txt': "Les fins de chantier courantes sont assurées dans le Lot (46) et l'Aveyron (12) — Cajarc, Figeac, Cahors, Saint-Céré, Gramat, Rodez, Villefranche-de-Rouergue, Decazeville — ainsi que dans les départements limitrophes : Dordogne (24), Corrèze (19), Cantal (15), Tarn-et-Garonne (82) et Lot-et-Garonne (47). Pour les chantiers d'envergure, VERTUCLEAN se déplace partout en France.",
 'faq': [
   ("Quand faut-il programmer le nettoyage de fin de chantier ?",
    "Une fois tous les corps de métier passés, y compris les retouches de peinture et la pose des équipements. Un nettoyage lancé trop tôt sera annulé par le lot suivant. L'idéal est de le programmer deux à trois jours avant la remise des clés, ce qui laisse le temps d'un second passage si une finition tardive salit à nouveau."),
   ("Intervenez-vous pour les artisans en sous-traitance ?",
    "Oui, c'est une part importante de cette activité. Nous travaillons pour des artisans, des maîtres d'œuvre et des entreprises générales qui préfèrent confier le nettoyage final plutôt que de mobiliser leurs équipes dessus. La facturation se fait alors à l'entreprise, et l'intervention se cale sur votre planning de livraison."),
   ("La poussière de ciment part-elle des carrelages ?",
    "Oui, mais pas au simple lavage. Le voile de laitance qui blanchit un carrelage neuf est un dépôt minéral qui demande un traitement spécifique avant rinçage. Passer la serpillière dessus ne fait que l'étaler. Nous le traitons systématiquement, faute de quoi le sol garde un aspect terne quel que soit le nombre de lavages."),
   ("Faut-il que l'eau et l'électricité soient raccordées ?",
    "C'est nettement préférable et cela accélère l'intervention. Si le chantier n'est pas encore raccordé, précisez-le au moment du devis : nous venons alors en autonomie, avec notre propre alimentation en eau et un groupe électrogène. Cela reste possible, simplement à prévoir."),
   ("Pouvez-vous repasser après les retouches ?",
    "Oui, et c'est fréquent. Les dernières reprises de peinture ou la pose tardive d'un équipement salissent souvent une zone déjà nettoyée. Un second passage ciblé, limité aux zones concernées, est prévu au devis lorsque vous l'anticipez."),
 ],
 'schema': {"name":"Nettoyage de fin de chantier",
            "serviceType":"Nettoyage après travaux",
            "area":["Lot","Aveyron","France"]},
},

{
 'file': 'nettoyage-apres-inoccupation-lot-aveyron.html',
 'nav':  'Après inoccupation',
 'title': "Nettoyage Après Longue Inoccupation — Maison Fermée, Résidence Secondaire | VERTUCLEAN Lot",
 'desc':  "Remise en état d'un logement resté fermé : dépoussiérage profond, désinfection, traitement des moisissures et des odeurs de renfermé. Résidences secondaires, successions, biens à la vente. Lot & Aveyron.",
 'kw':    "nettoyage maison inoccupée Lot, nettoyage résidence secondaire Aveyron, nettoyage après succession, traitement moisissure maison fermée, odeur de renfermé maison, nettoyage avant vente Cahors",
 'eyebrow': "Après inoccupation · Lot & Aveyron",
 'h1':    ["Nettoyage après", "longue inoccupation"],
 'lede':  "Une maison restée fermée ne se contente pas de prendre la poussière. Nous traitons le dépôt, l'humidité, les moisissures et l'odeur de renfermé pour rendre le lieu immédiatement habitable.",
 'img':   ('nettoyage-apres-inoccupation-lot-aveyron.jpg', 1000, 563,
           "Remise en état d'un logement resté longtemps inoccupé par VERTUCLEAN"),
 'tag':   ("Résidences secondaires", "Successions et biens mis en vente"),
 'intro_h2': ["Ce qui se passe", "dans une maison fermée"],
 'intro': [
   "Sans ventilation ni chauffage, l'humidité s'installe. Elle condense sur les murs froids, les vitrages et l'arrière des meubles, et fait apparaître des points de moisissure là où l'air ne circule pas : angles de mur nord, fond de placard, derrière une tête de lit. La poussière, elle, se lie à cette humidité et forme un film gras qui ne s'enlève plus au chiffon sec.",
   "L'odeur de renfermé n'est pas une odeur de poussière : c'est celle des composés émis par ces micro-organismes et par les textiles humides. Aérer ne la retire pas, elle revient dès la fermeture. Il faut traiter les surfaces qui l'émettent — d'où le recours à la vapeur, qui assainit en profondeur par la chaleur, sans laisser de parfum de couverture.",
   "Le reste est méthodique : dépoussiérage complet du haut vers le bas, y compris les zones qu'on ne pense jamais à faire dans une maison habitée — dessus d'armoire, gaines de VMC, corps de radiateur, intérieur des placards vidés. Les dépouilles d'insectes et les nids éventuels sont retirés, la robinetterie détartrée et les siphons remis en eau.",
 ],
 'blocks_h2': ["Ce que comprend", "la remise en état"],
 'blocks_sub': "Résidences secondaires rouvertes, successions, biens mis en vente ou en location, locaux professionnels réinvestis.",
 'blocks': [
   ("Dépoussiérage complet", "Sols, murs, plafonds, dessus de meubles, plinthes, luminaires et gaines de ventilation."),
   ("Traitement des moisissures", "Points de moisissure sur murs, joints, menuiseries et fonds de placard, traités à la vapeur."),
   ("Neutralisation des odeurs", "Traitement des surfaces émettrices plutôt que masquage par un parfum d'ambiance."),
   ("Sanitaires & robinetterie", "Détartrage complet, remise en eau des siphons, désinfection des cuvettes et bacs."),
   ("Cuisine & électroménager", "Intérieur des placards, plans de travail,réfrigérateur et four laissés fermés."),
   ("Vitrages & menuiseries", "Vitres, dormants, volets et rails, souvent les plus marqués par une longue fermeture."),
 ],
 'why_h2': ["Pourquoi nous", "confier ce chantier"],
 'why': [
   ("La vapeur contre les moisissures", "traitement par la chaleur, sans javel ni fongicide dans un lieu qui va être habité"),
   ("Odeurs traitées à la source", "les surfaces émettrices sont assainies, pas recouvertes d'un parfum"),
   ("Discrétion", "successions et situations délicates traitées sans jugement et sans commentaire"),
   ("English spoken", "interlocuteur anglophone pour les propriétaires étrangers de résidences secondaires"),
   ("Préparation à la vente", "un bien net se visite mieux et se négocie mieux"),
   ("Intervention en votre absence", "possible sur remise de clés, avec compte rendu photo"),
 ],
 'zone_h2': ["Où nous", "intervenons"],
 'zone_txt': "Cette prestation est assurée dans tout le Lot (46) et l'Aveyron (12) — Cajarc, Figeac, Cahors, Limogne-en-Quercy, Saint-Céré, Gramat, Rodez, Villefranche-de-Rouergue — ainsi que dans les départements limitrophes : Dordogne (24), Corrèze (19), Cantal (15), Tarn-et-Garonne (82) et Lot-et-Garonne (47). Le Quercy comptant de nombreuses résidences secondaires, nous intervenons régulièrement pour des propriétaires qui rouvrent leur maison à distance.",
 'faq': [
   ("Comment faire partir une odeur de renfermé ?",
    "En traitant les surfaces qui l'émettent, pas en aérant. L'odeur de renfermé provient des composés dégagés par les micro-organismes installés dans les textiles, les murs humides et les fonds de placard. Aérer la dilue le temps de l'ouverture, puis elle revient. Le nettoyage vapeur assainit ces surfaces par la chaleur et supprime la source, sans y substituer un parfum d'ambiance."),
   ("Traitez-vous les moisissures sans javel ?",
    "Oui, et c'est préférable. La javel décolore la tache de surface mais n'atteint pas le mycélium installé dans la porosité du support, et elle laisse un résidu irritant dans un logement qui va être occupé. La vapeur agit par la chaleur, en profondeur, sans dépôt chimique. Si l'humidité structurelle persiste, il faut par ailleurs en traiter la cause — un nettoyage seul ne suffira pas durablement."),
   ("Pouvez-vous intervenir en mon absence ?",
    "Oui, c'est courant pour les résidences secondaires. L'intervention se fait sur remise de clés, par vos soins, ceux d'un voisin ou d'une agence, et nous vous adressons un compte rendu photo à l'issue. Beaucoup de propriétaires font ainsi préparer la maison quelques jours avant leur arrivée."),
   ("Intervenez-vous dans le cadre d'une succession ?",
    "Oui, régulièrement. Ce sont des chantiers qui demandent de la discrétion et un certain tact : ils se traitent sans jugement et sans commentaire sur l'état des lieux. Nous pouvons intervenir avant l'estimation, avant la mise en vente, ou après le départ des effets personnels, selon ce qui vous arrange."),
   ("Faut-il vider le logement avant votre passage ?",
    "Ce n'est pas obligatoire mais cela améliore beaucoup le résultat, en particulier pour les placards et les dessous de meubles. Si un débarras est nécessaire, dites-le au moment du devis : selon l'ampleur, cela relève de la remise en état avancée, que nous assurons également."),
 ],
 'schema': {"name":"Nettoyage après longue inoccupation",
            "serviceType":"Remise en état de logement inoccupé",
            "area":["Lot","Aveyron","Dordogne","Corrèze","Cantal","Tarn-et-Garonne","Lot-et-Garonne"]},
},

{
 'file': 'remise-en-etat-avancee-lot-aveyron.html',
 'nav':  'Remise en état avancée',
 'title': "Remise en État Avancée — Nettoyage Extrême & Syndrome de Diogène | VERTUCLEAN Lot & Aveyron",
 'desc':  "Nettoyage de situations très dégradées : logements en incurie, syndrome de Diogène, locaux abandonnés. Intervention discrète et sans jugement, traitement vapeur en profondeur. Lot, Aveyron et France entière.",
 'kw':    "nettoyage syndrome de Diogène, nettoyage extrême Lot, débarras et nettoyage Aveyron, logement insalubre nettoyage, remise en état appartement dégradé, nettoyage après incurie",
 'eyebrow': "Remise en état avancée · France entière",
 'h1':    ["Remise en état", "avancée"],
 'lede':  "Logements en situation d'incurie, locaux laissés à l'abandon, accumulations lourdes. Nous intervenons là où un nettoyage ordinaire ne suffit plus — avec méthode, et sans jugement.",
 'img':   ('remise-en-etat-avancee-lot-aveyron.jpg', 1000, 563,
           "Remise en état avancée d'un local très dégradé par VERTUCLEAN"),
 'tag':   ("Intervention discrète", "Sans jugement, en lien avec les familles"),
 'intro_h2': ["Des situations", "qui demandent du tact"],
 'intro': [
   "Certains logements ne relèvent plus du ménage. Accumulation d'objets sur plusieurs années, encombrement rendant les pièces impraticables, dégradation des sols et des murs, parfois présence de nuisibles : ce sont des chantiers de remise en état, pas des prestations d'entretien. Ils appellent un matériel adapté, un protocole et un rythme différents.",
   "Ils appellent aussi une certaine retenue. Derrière une situation d'incurie ou un syndrome de Diogène, il y a presque toujours une personne en difficulté et une famille éprouvée. Nous intervenons sans commentaire sur ce que nous découvrons, en lien avec les proches, un tuteur, un bailleur ou un service social selon le cas, et nous n'évoquons jamais un chantier à l'extérieur.",
   "Sur le plan technique, l'ordre est immuable : dégagement et tri des volumes, puis traitement des surfaces mises à nu, puis assainissement. La vapeur occupe ici une place centrale — elle traite en profondeur des supports très encrassés et neutralise les odeurs incrustées sans saturer un logement de produits chimiques.",
 ],
 'blocks_h2': ["Le déroulé", "d'un chantier"],
 'blocks_sub': "Chaque situation est différente ; la méthode, elle, reste la même.",
 'blocks': [
   ("Visite et devis", "État des lieux sur place, discret, avec estimation du volume à évacuer et du temps d'intervention."),
   ("Dégagement des volumes", "Tri et évacuation, avec mise de côté systématique des papiers, documents et objets de valeur trouvés."),
   ("Traitement des surfaces", "Sols, murs, plafonds, menuiseries : décapage puis nettoyage vapeur en profondeur."),
   ("Assainissement", "Traitement des moisissures et des odeurs incrustées, désinfection complète des sanitaires et de la cuisine."),
   ("Nuisibles", "Retrait des dépouilles et des nids ; coordination avec une entreprise spécialisée si un traitement s'impose."),
   ("Remise en état finale", "Vitrages, robinetterie, équipements — le logement est rendu habitable ou présentable à la visite."),
 ],
 'why_h2': ["Ce qui compte", "sur ces chantiers"],
 'why': [
   ("Discrétion absolue", "aucun commentaire, aucune photo diffusée, véhicule sans marquage ostentatoire si vous le souhaitez"),
   ("Sans jugement", "la situation est traitée comme un chantier technique, pas comme un cas"),
   ("La vapeur en profondeur", "supports très encrassés et odeurs incrustées traités sans saturer le lieu de chimie"),
   ("Objets préservés", "papiers, documents administratifs et objets de valeur systématiquement mis de côté"),
   ("Interlocuteur unique", "familles, tuteurs, bailleurs, notaires ou services sociaux selon la situation"),
   ("France entière", "déplacement partout en France pour les chantiers d'envergure"),
 ],
 'zone_h2': ["Où nous", "intervenons"],
 'zone_txt': "VERTUCLEAN intervient en priorité dans le Lot (46) et l'Aveyron (12) ainsi que dans les départements limitrophes — Dordogne (24), Corrèze (19), Cantal (15), Tarn-et-Garonne (82), Lot-et-Garonne (47). Les remises en état avancées étant des chantiers longs et préparés, nous nous déplaçons également partout en France, le déplacement étant intégré au devis.",
 'faq': [
   ("Qu'est-ce qu'un nettoyage lié au syndrome de Diogène ?",
    "C'est la remise en état d'un logement où se sont accumulés, souvent sur plusieurs années, objets, déchets et encombrants, au point de rendre les pièces impraticables et d'altérer les sols, les murs et les installations sanitaires. L'intervention combine dégagement des volumes, traitement des surfaces mises à nu et assainissement complet. Elle demande un matériel adapté, un protocole précis, et beaucoup de retenue vis-à-vis de la personne concernée et de ses proches."),
   ("Intervenez-vous de manière discrète ?",
    "Oui, c'est une condition de ce travail. Nous n'émettons aucun commentaire sur ce que nous découvrons, ne diffusons aucune image, et n'évoquons jamais un chantier à l'extérieur. Si vous le souhaitez, l'intervention se fait avec un véhicule sans marquage ostentatoire et à des horaires choisis pour limiter la visibilité dans le voisinage."),
   ("Que deviennent les objets et les papiers trouvés ?",
    "Les papiers, documents administratifs, photographies et objets susceptibles d'avoir de la valeur sont systématiquement mis de côté et remis à la famille, au tuteur ou à la personne désignée. Rien n'est évacué sans validation. C'est un point que nous fixons ensemble avant le début du chantier, car il conditionne le rythme du tri."),
   ("Qui peut commander ce type d'intervention ?",
    "La personne concernée, un membre de la famille, un tuteur ou curateur, un bailleur, un syndic, un notaire dans le cadre d'une succession, ou un service social. Nous nous adaptons à l'interlocuteur et fournissons les documents nécessaires — devis détaillé, facture, attestation d'intervention — selon ce que la situation exige."),
   ("Combien de temps dure un chantier de ce type ?",
    "Cela va d'une journée à plusieurs semaines selon le volume accumulé, la surface et l'état des supports. C'est précisément pour cela que la visite préalable est indispensable : elle permet d'annoncer une durée et un montant fermes, plutôt que de découvrir l'ampleur en cours de route."),
 ],
 'schema': {"name":"Remise en état avancée et nettoyage extrême",
            "serviceType":"Remise en état de locaux très dégradés",
            "area":["Lot","Aveyron","France"]},
},

]

# ══════════════════════════════════════════════════════════════
#  Rendu
# ══════════════════════════════════════════════════════════════
NAV = [('index.html', 'Accueil')] + [(p['file'], p['nav']) for p in PAGES] + \
      [('carprices.html', 'Nettoyage de véhicules')]

PAGE_CSS = """
    /* ══ PAGE SERVICE ══════════════════════════════════ */
    .prose{ max-width:68ch; }
    .prose p{ font-size:1rem; line-height:1.78; margin-bottom:20px; }
    .prose p:last-child{ margin-bottom:0; }
    .grid-2{ display:grid; gap:20px; }
    .tile{ background:var(--white); border:1px solid var(--rule-soft);
        border-radius:var(--r); padding:24px; }
    .tile b{ display:block; color:var(--ink); font-family:'Bricolage Grotesque',sans-serif;
        font-weight:700; font-size:1rem; margin-bottom:7px; letter-spacing:-.01em; }
    .tile span{ font-size:.89rem; line-height:1.65; color:var(--muted); }
    .why{ list-style:none; max-width:70ch; }
    .why li{ display:flex; align-items:flex-start; gap:12px; margin-bottom:14px;
        font-size:.93rem; line-height:1.65; color:var(--muted); }
    .why li .ico{ font-size:.82rem; color:var(--coral); margin-top:.36em; flex:none; }
    .why li b{ color:var(--ink); font-weight:600; }
    .other{ background:var(--glass-2); }
    .other-grid{ display:grid; gap:12px; }
    .other-grid a{ display:flex; align-items:center; justify-content:space-between; gap:14px;
        background:var(--white); border:1px solid var(--rule-soft); border-radius:var(--r);
        padding:18px 22px; text-decoration:none; color:var(--ink);
        font-weight:600; font-size:.93rem;
        transition:border-color .22s ease, transform .22s ease; }
    .other-grid a:hover{ border-color:var(--coral); transform:translateX(4px); }
    .other-grid a .ico{ color:var(--coral-d); flex:none; }
    @media (min-width:700px){ .grid-2{ grid-template-columns:1fr 1fr; } }
    @media (min-width:960px){
        .other-grid{ grid-template-columns:1fr 1fr; }
    }
"""

def render(p):
    url = SITE + '/' + p['file']
    nat = p.get('national')

    nav = '\n'.join('    <a href="%s">%s</a>' % (h, esc(t))
                    for h, t in NAV if h != p['file'])

    tiles = '\n'.join(
        '                <div class="tile"><b>%s</b><span>%s</span></div>' % (esc(b), esc(t))
        for b, t in p['blocks'])

    why = '\n'.join(
        '                <li><svg class="ico"><use href="#i-spark"/></svg><span><b>%s</b> — %s</span></li>'
        % (esc(b), esc(t)) for b, t in p['why'])

    faq_html = '\n'.join(
        '                <details class="faq-item"%s>\n                    <summary>%s</summary>\n'
        '                    <div class="a">%s</div>\n                </details>'
        % (' open' if i == 0 else '', esc(q), esc(a))
        for i, (q, a) in enumerate(p['faq']))

    others = '\n'.join(
        '                <a href="%s">%s <svg class="ico"><use href="#i-arrow"/></svg></a>' % (h, esc(t))
        for h, t in NAV if h != p['file'])

    svc = {"@context":"https://schema.org","@type":"Service",
           "name":p['schema']['name'],"serviceType":p['schema']['serviceType'],
           "description":p['desc'],"url":url,
           "provider":{"@type":"LocalBusiness","@id":SITE+"/#business","name":"VERTUCLEAN",
                       "telephone":"+33755614567","email":MAIL,
                       "address":{"@type":"PostalAddress","addressLocality":"Cajarc",
                                  "postalCode":"46160","addressRegion":"Lot","addressCountry":"FR"}},
           "areaServed":[{"@type":"AdministrativeArea","name":a} for a in p['schema']['area']],
           "availableChannel":{"@type":"ServiceChannel","servicePhone":{"@type":"ContactPoint","telephone":"+33755614567"},"serviceUrl":url}}

    faq_ld = {"@context":"https://schema.org","@type":"FAQPage",
              "mainEntity":[{"@type":"Question","name":q,
                             "acceptedAnswer":{"@type":"Answer","text":a}} for q, a in p['faq']]}

    crumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Accueil","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"Services","item":SITE+"/#services"},
        {"@type":"ListItem","position":3,"name":p['nav'],"item":url}]}

    def ld(o): return json.dumps(o, ensure_ascii=False, indent=4)

    img, iw, ih, ialt = p['img']

    tpl = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{{title}}</title>
    <meta name="description" content="{{desc}}">
    <meta name="keywords" content="{{kw}}">
    <meta name="author" content="VERTUCLEAN">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
    <link rel="canonical" href="{{url}}">

    <meta name="geo.region" content="FR-46">
    <meta name="geo.placename" content="Cajarc, Lot, Aveyron, Occitanie">
    <meta name="geo.position" content="44.4861;1.8425">

    <meta property="og:title" content="{{title}}">
    <meta property="og:description" content="{{desc}}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{{url}}">
    <meta property="og:image" content="{{site}}/og-vertuclean-nettoyage-lot-aveyron.jpg">
    <meta property="og:locale" content="fr_FR">
    <meta property="og:site_name" content="VERTUCLEAN">
    <meta name="twitter:card" content="summary_large_image">

    <script type="application/ld+json">
{{svc}}
    </script>
    <script type="application/ld+json">
{{faqld}}
    </script>
    <script type="application/ld+json">
{{crumb}}
    </script>

    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%231d1560'/%3E%3Cpath d='M32 11c1.9 12.6 6.4 17.1 19 19-12.6 1.9-17.1 6.4-19 19-1.9-12.6-6.4-17.1-19-19 12.6-1.9 17.1-6.4 19-19z' fill='%23ff5757'/%3E%3C/svg%3E">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">

    <style>{{css}}{{pagecss}}    </style>
</head>
<body class="ready">

{{sprite}}

<a href="index.html" class="brand" id="brand" aria-label="VERTUCLEAN, retour à l'accueil">
    <img src="logo-vertuclean.png" width="620" height="411"
         alt="VERTUCLEAN — service de nettoyage éthique et écologique, Lot et Aveyron">
</a>

<button class="menu-btn" id="menuBtn" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="navPanel">
    <span></span><span></span><span></span>
</button>
<div class="nav-veil" id="navVeil"></div>
<nav class="nav-panel" id="navPanel" aria-label="Navigation principale">
{{nav}}
    <a href="index.html#contact">Contact</a>
    <a href="tel:+33755614567" class="nav-call"><small>Appeler l'atelier</small>{{tel}}</a>
</nav>

<section class="hero">
    <div class="wrap hero-grid">
        <div class="hero-copy">
            <span class="eyebrow">{{eyebrow}}</span>
            <h1>{{h1a}}<br><em>{{h1b}}</em></h1>
            <p class="lede">{{lede}}</p>
            <div class="cta-row">
                <a href="tel:+33755614567" class="btn btn-primary"><svg class="ico"><use href="#i-phone"/></svg> {{tel}}</a>
                <a href="index.html#services" class="btn btn-ghost">Tous nos services</a>
            </div>
        </div>
        <figure class="hero-shot">
            <img src="{{img}}" width="{{iw}}" height="{{ih}}" fetchpriority="high" alt="{{ialt}}">
            <figcaption class="shot-tag">
                <svg class="ico"><use href="#i-leaf"/></svg>
                <span><b>{{tag1}}</b>{{tag2}}</span>
            </figcaption>
        </figure>
    </div>
</section>

<section class="services">
    <div class="wrap">
        <div class="rv">
            <h2>{{ih2a}}<br>{{ih2b}}</h2>
            <div class="prose" style="margin-top:26px">{{intro}}</div>
        </div>
    </div>
</section>

<section class="reviews">
    <div class="wrap">
        <div class="rv">
            <span class="eyebrow">Le détail</span>
            <h2>{{bh2a}}<br>{{bh2b}}</h2>
            <p class="sub">{{bsub}}</p>
            <div class="grid-2">
{{tiles}}
            </div>
        </div>
    </div>
</section>

<section class="about">
    <div class="wrap">
        <div class="rv">
            <span class="eyebrow">Nos engagements</span>
            <h2>{{wh2a}}<br>{{wh2b}}</h2>
            <ul class="why" style="margin-top:30px">
{{why}}
            </ul>
        </div>
    </div>
</section>

<section class="zone">
    <div class="wrap">
        <div class="rv">
            <span class="eyebrow">Zone d'intervention</span>
            <h2>{{zh2a}}<br>{{zh2b}}</h2>
            <p class="sub" style="max-width:70ch">{{ztxt}}</p>
            <div class="notes">
                <div class="note">
                    <svg class="ico"><use href="#i-pin"/></svg>
                    <span><b>Basé à Cajarc</b> — 46160, Lot</span>
                </div>
                <div class="note hi">
                    <svg class="ico"><use href="#i-route"/></svg>
                    <span><b>{{znote}}</b></span>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="faq">
    <div class="wrap">
        <div class="rv">
            <span class="eyebrow">Questions fréquentes</span>
            <h2>Vos questions,<br>nos réponses</h2>
            <div class="faq-list" style="margin-top:34px">
{{faq}}
            </div>
        </div>
    </div>
</section>

<section class="other">
    <div class="wrap">
        <div class="rv">
            <span class="eyebrow">Nos autres prestations</span>
            <h2>Voir aussi</h2>
            <div class="other-grid" style="margin-top:30px">
{{others}}
            </div>
        </div>
    </div>
</section>

<section class="contact">
    <div class="wrap">
        <div class="cta-band rv" style="background:var(--ink);border-radius:var(--r);padding:clamp(36px,5vw,56px);text-align:center">
            <h2 style="color:#fff;margin-bottom:12px">Un devis<br>gratuit</h2>
            <p style="color:rgba(255,255,255,.62);max-width:48ch;margin:0 auto 28px">Décrivez-nous votre besoin par téléphone ou par email : nous répondons rapidement, avec une estimation ferme.</p>
            <div class="cta-row" style="justify-content:center">
                <a href="tel:+33755614567" class="btn btn-primary"><svg class="ico"><use href="#i-phone"/></svg> {{tel}}</a>
                <a href="mailto:{{mail}}" class="btn btn-ghost" style="border-color:rgba(255,255,255,.4);color:#fff"><svg class="ico"><use href="#i-mail"/></svg> {{mail}}</a>
            </div>
        </div>
    </div>
</section>

{{footer}}

<script>
(function(){
    var btn=document.getElementById('menuBtn'), panel=document.getElementById('navPanel'), veil=document.getElementById('navVeil');
    function set(o){ btn.setAttribute('aria-expanded',o?'true':'false');
        btn.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu');
        panel.classList.toggle('open',o); veil.classList.toggle('open',o); }
    btn.addEventListener('click',function(){ set(btn.getAttribute('aria-expanded')!=='true'); });
    veil.addEventListener('click',function(){ set(false); });
    panel.addEventListener('click',function(e){ if(e.target.tagName==='A') set(false); });
    document.addEventListener('keydown',function(e){ if(e.key==='Escape') set(false); });
})();
(function(){
    var b=document.getElementById('brand'), t=false;
    function u(){ b.classList.toggle('dim', window.scrollY>90); t=false; }
    window.addEventListener('scroll',function(){ if(!t){ t=true; requestAnimationFrame(u); } },{passive:true});
})();
(function(){
    var items=document.querySelectorAll('.rv');
    if(!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches){
        items.forEach(function(el){ el.classList.add('in'); }); return; }
    var io=new IntersectionObserver(function(es){ es.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); } }); },
        {rootMargin:'0px 0px -12% 0px',threshold:.12});
    items.forEach(function(el){ io.observe(el); });
})();
</script>
</body>
</html>
"""
    vals = {
    'title': esc(p['title']), 'desc': esc(p['desc']), 'kw': esc(p['kw']),
    'url': url, 'site': SITE, 'css': CSS, 'pagecss': PAGE_CSS, 'sprite': SPRITE,
    'nav': nav, 'tel': TEL, 'mail': MAIL, 'footer': FOOTER,
    'eyebrow': esc(p['eyebrow']), 'h1a': esc(p['h1'][0]), 'h1b': esc(p['h1'][1]),
    'lede': esc(p['lede']),
    'img': img, 'iw': iw, 'ih': ih, 'ialt': esc(ialt),
    'tag1': esc(p['tag'][0]), 'tag2': esc(p['tag'][1]),
    'ih2a': esc(p['intro_h2'][0]), 'ih2b': esc(p['intro_h2'][1]),
    'intro': '\n'.join('<p>%s</p>' % esc(x) for x in p['intro']),
    'bh2a': esc(p['blocks_h2'][0]), 'bh2b': esc(p['blocks_h2'][1]),
    'bsub': esc(p['blocks_sub']), 'tiles': tiles,
    'wh2a': esc(p['why_h2'][0]), 'wh2b': esc(p['why_h2'][1]), 'why': why,
    'zh2a': esc(p['zone_h2'][0]), 'zh2b': esc(p['zone_h2'][1]), 'ztxt': esc(p['ztxt'] if 'ztxt' in p else p['zone_txt']),
    'znote': "Chantiers d'envergure — déplacement partout en France sur devis" if nat
             else "Grands chantiers — déplacement partout en France sur devis",
    'faq': faq_html, 'others': others,
    'svc': ld(svc), 'faqld': ld(faq_ld), 'crumb': ld(crumb),
    }
    for k, v in vals.items():
        tpl = tpl.replace('{{' + k + '}}', str(v))
    return tpl

# ══ Generation ══
made = []
for p in PAGES:
    out = render(p)
    io.open(os.path.join(BASE, p['file']), 'w', encoding='utf-8').write(out)
    txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>', '', out[out.index('<body'):], flags=re.S)))
    made.append((p['file'], len(txt.split()), len(out.encode()) // 1024))
    print('  %-52s %4d mots  %3d Ko' % (p['file'], len(txt.split()), len(out.encode()) // 1024))

# ══ sitemap.xml ══
from datetime import date
urls = [(SITE + '/', '1.0'), (SITE + '/carprices.html', '0.8')] + \
       [(SITE + '/' + p['file'], '0.9') for p in PAGES]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.w3.org/1999/9/xhtml".replace']
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, pr in urls:
    sm.append('  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
              '    <changefreq>monthly</changefreq>\n    <priority>%s</priority>\n  </url>'
              % (u, date.today().isoformat(), pr))
sm.append('</urlset>')
io.open(os.path.join(BASE, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
print('  sitemap.xml : %d URL' % len(urls))
