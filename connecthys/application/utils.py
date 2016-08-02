#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------
# Application :    Connecthys, le portail internet de Noethys
# Site internet :  www.noethys.com
# Auteur:          Ivan LUCAS
# Copyright:       (c) 2010-16 Ivan LUCAS
# Licence:         Licence GNU GPL
#--------------------------------------------------------------

import datetime
from application import app


# ------  Fonctions importables depuis les templates ----------

def CallFonction(fonction="", *args):
    """ Pour appeller directement une fonction Utils depuis Python """
    return utility_processor()[fonction](*args)
    
@app.context_processor
def utility_processor():
    """ Variables accessibles dans tous les templates """
    
    def Formate_montant(montant, symbole=u'€'):
        return u"{0:.2f} {1}".format(montant, symbole)

    def DateDDEnFr(date):
        """ Transforme une date DD en date FR """
        if date == None : return ""
        return date.strftime("%d/%m/%Y")
        
    def DateDDEnEng(date):
        """ Transforme une date DD en date Eng sans tirets """
        if date == None : return ""
        return date.strftime("%Y-%m-%d")

    def DateDDEnFrComplet(date):
        """ Transforme une date DD en date FR """
        if date == None : return ""
        jours = [u"Lundi", u"Mardi", u"Mercredi", u"Jeudi", u"Vendredi", u"Samedi", u"Dimanche"]
        mois = ["Janvier", u"Février", "Mars", "Avril", "Mai", "Juin", "Juillet", u"Août", "Septembre", "Octobre", u"Novembre", u"Décembre"]
        return u"%s %d %s %d" % (jours[date.weekday()], date.day, mois[date.month-1], date.year)

    def DateEngEnDD(date):
        if date in (None, "", "None") : return None
        if type(date) == datetime.date : return date
        return datetime.date(int(date[:4]), int(date[5:7]), int(date[8:10]))

    def DateDTEnHeureFr(datetm):
        """ Transforme une datetime en Heure FR """
        if datetm == None : return ""
        return datetm.strftime("%H:%M")
    
    def DateEngFr(textDate):
        if textDate in (None, "") : return ""
        if type(textDate) == datetime.date : return DateDDEnFr(textDate)
        text = str(textDate[8:10]) + "/" + str(textDate[5:7]) + "/" + str(textDate[:4])
        return text

    def GetEtatFondCase(dict_consommations={}, date=None, IDunite=None):
        if dict_consommations.has_key(date) :
            if dict_consommations[date].has_key(IDunite) :
                etat = dict_consommations[date][IDunite]
                return etat
        return None
        
    def GetEtatCocheCase(dict_reservations={}, date=None, IDunite=None):
        if dict_reservations.has_key(date) :
            if dict_reservations[date].has_key(IDunite) :
                return True
        return False
        
    def GetIconeFichier(nomFichier=""):
        """ Retourne une icône selon le type de fichier (pdf, word, autre) """
        if nomFichier in (None, "") :
            return None
        if nomFichier.endswith(".pdf"):
            return "fa-file-pdf-o"
        elif nomFichier.endswith(".doc") or nomFichier.endswith(".docx"):
            return "fa-file-word-o"
        elif nomFichier.endswith(".txt"):
            return "fa-file-text-o"
        elif nomFichier.endswith(".jpg") or nomFichier.endswith(".png"):
            return "fa-file-image-o"
        else :
            return "fa-file-o"

        
    return dict(
        Formate_montant=Formate_montant,
        DateDDEnFr=DateDDEnFr,
        DateDDEnFrComplet=DateDDEnFrComplet,
        DateDTEnHeureFr=DateDTEnHeureFr,
        GetEtatFondCase=GetEtatFondCase,
        GetEtatCocheCase=GetEtatCocheCase,
        DateDDEnEng=DateDDEnEng,
        DateEngEnDD=DateEngEnDD,
        DateEngFr=DateEngFr,
        GetIconeFichier=GetIconeFichier,
        )

        
# ------  Fonctions non importables depuis les templates ----------

def GetVersionTuple(version=""):
    """ Renvoie un numéro de version donné au format tuple """
    temp = []
    for caract in version.split(".") :
        temp.append(int(caract))
    return tuple(temp)

    
