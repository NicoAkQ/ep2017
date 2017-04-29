# coding: utf-8

from django.shortcuts import render,redirect
from .forms import FormSimulateur2017
from .donnees import Algo_simu_EP2017_v2 as algo

def accueil(request):
#     sauvegarde = False
#     form = EntreePourcentages(request.POST or None)
#     if form.is_valid():
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    # id_nda=request.POST["id_abs_NDA"]
    if request.method == 'POST':
        caca="ee"
    request.POST.__getitem__("abs_NDA")
    form = FormSimulateur2017(request.POST or None)
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        list_ini=["NDA","MLP","MAC","HAM","ART","POU","CHE","LAS","MEL","ASS","FIL","SUP"]
        list_nom=["M. Nicolas DUPONT-AIGNAN","Mme Marine LE PEN","M. Emmanuel MACRON","M. Benoît HAMON","Mme Nathalie ARTHAUD","M. Philippe POUTOU","M. Jacques CHEMINADE","M. Jean LASSALLE","M. Jean-Luc MÉLENCHON","M. François ASSELINEAU","M. François FILLON"]
        num_case=list(range(4,18))
        i=0
        donnees={}
        for nom in list_ini:
            val_mac_can="mac_"+nom
            abs_can="abs_"+nom
            num=str(num_case[i])
            donnees["H"+num]=float((request.POST.__getitem__(abs_can)))/100 # exploite directement la requête
            donnees["J"+num]=float((request.POST.__getitem__(val_mac_can)))/100
            i += 1
        donnees["H16"]=float(request.POST.__getitem__("abs_SUP"))/100
        donnees["J16"]=float(request.POST.__getitem__("mac_SUP"))/100
        resultats=algo.get_resultat_simu(donnees) # envoie un dictionnaire à simuler_resultat
        # Transférer les données pour traitement à Python
        return render(request,'simulateurelections2017/resultats.html',{'pv_mac':resultats["pv_mac"],'pv_lp':resultats["pv_lp"]})
    
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'simulateurelections2017/index.html', locals())
