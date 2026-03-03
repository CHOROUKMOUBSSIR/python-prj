
donnees = [
    ("Sara", "Math", 12, "G1"), ("Sara", "Info", 14, "G1"), ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"), ("Sara", "Math", 11, "G1"), ("Bouchra", "Info", "abc", "G2"), 
    ("", "Math", 10, "G1"), ("Yassine", "Info", 22, "G2"), ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"), ("Sara", "Chimie", 16, "G1"), ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"), ("Hana", "Physique", 15, "G3"), ("Hana", "Math", 8, "G3")
]


def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    if not nom or str(nom).strip() == "": return False, "Nom vide"
    if not matiere or str(matiere).strip() == "": return False, "Matière vide"
    if not groupe or str(groupe).strip() == "": return False, "Groupe vide"
    try:
        valeur_note = float(note)
        if not (0 <= valeur_note <= 20):
            return False, f"Note hors intervalle [0,20] : {valeur_note}"
    except (ValueError, TypeError):
        return False, f"Note non numérique : {note}"
    return True, ""

valides = []
erreurs = []
doublons_exact = set()
vus = set()

for ligne in donnees:
    if ligne in vus:
        doublons_exact.add(ligne)
        continue 
    vus.add(ligne)
    est_valide, raison = valider(ligne)
    if est_valide:
        valides.append((ligne[0], ligne[1], float(ligne[2]), ligne[3]))
    else:
        erreurs.append({"ligne": ligne, "raison": raison})



matieres_distinctes = {enreg[1] for enreg in valides}

notes_par_etudiant = {}
etudiants_par_groupe = {}

for nom, matiere, note, groupe in valides:
   
    if nom not in notes_par_etudiant:
        notes_par_etudiant[nom] = {}
    if matiere not in notes_par_etudiant[nom]:
        notes_par_etudiant[nom][matiere] = []
    notes_par_etudiant[nom][matiere].append(note)
    
    
    if groupe not in etudiants_par_groupe:
        etudiants_par_groupe[groupe] = set()
    etudiants_par_groupe[groupe].add(nom)


def somme_recursive(liste_notes):
    if not liste_notes: return 0
    return liste_notes[0] + somme_recursive(liste_notes[1:])

def calculer_moyenne(liste_notes):
    if not liste_notes: return 0
    return somme_recursive(liste_notes) / len(liste_notes)

resultats_etudiants = {}
for nom, matieres in notes_par_etudiant.items():
    moyennes_mat = {m: calculer_moyenne(n) for m, n in matieres.items()}
    toutes_notes = [n for l in matieres.values() for n in l]
    resultats_etudiants[nom] = {
        "moyenne_generale": round(calculer_moyenne(toutes_notes), 2),
        "details": moyennes_mat
    }

SEUIL_GROUPE_FAIBLE = 10.0
alertes = {"doublons": [], "incomplets": [], "groupes_faibles": [], "ecarts": []}

for nom, matieres in notes_par_etudiant.items():

    for m, n in matieres.items():
        if len(n) > 1: alertes["doublons"].append(f"{nom} ({m})")
    

    if set(matieres.keys()) != matieres_distinctes:
        alertes["incomplets"].append(nom)
        
   
    toutes_n = [n for l in matieres.values() for n in l]
    if max(toutes_n) - min(toutes_n) > 10:
        alertes["ecarts"].append(nom)

for grp, etuds in etudiants_par_groupe.items():
    notes_grp = [n for e in etuds for m in notes_par_etudiant[e].values() for n in m]
    if calculer_moyenne(notes_grp) < SEUIL_GROUPE_FAIBLE:
        alertes["groupes_faibles"].append(grp)

print("--- RAPPORT D'ANALYSE ---")
print(f"Lignes valides : {len(valides)} | Erreurs détectées : {len(erreurs)}")
print(f"Moyennes : {resultats_etudiants}")
print(f"Alertes : {alertes}")