Connecthys
==================
Connecthys est le portail internet de Noethys, le logiciel de gestion libre et gratuit de gestion multi-activit�s pour 
les accueils de loisirs, cr�ches, garderies p�riscolaires, cantines, 
TAP ou NAP, clubs sportifs et culturels...

Plus d'infos sur www.noethys.com

*****Avertissement : A ce jour, Connecthys n'est qu'un prototype d'interface web. La synchronisation avec Noethys sera d�velopp�e
prochainement.*****


Utilisation sur Windows
------------------------

- Installez python 2.7 (http://www.python.org)
- Placez-vous dans le r�pertoire connecthys 
- Chargez l'invite de commandes de Windows et tapez "C:\Python27\python.exe run.py"
- Lancez votre navigateur internet
- Chargez la page **http://localhost:5000/initdb** pour initialiser la base de donn�es
- Chargez la page **http://localhost:5000/accueil** pour ouvrir le portail


Utilisation sur Linux
-------------------------

- Placez-vous dans le r�pertoire connecthys 
- Chargez la console de Linux et tapez "python run.py"
- Lancez votre navigateur internet
- Chargez la page **http://localhost:5000/initdb** pour initialiser la base de donn�es
- Chargez la page **http://localhost:5000/accueil** pour ouvrir le portail


Utilisation sur un h�bergement internet mutualis� (Test� sur OVH)
-------------------------

- Copiez le r�pertoire "connecthys" � la racine de votre r�pertoire FTP
- Avec votre client FTP (Filezilla par exemple), appliquez la valeur 755 aux droits d'acc�s du fichier "portail.cgi" du r�pertoire connecthys
- Chargez la page **http://www.monsite.com/connecthys/portail.cgi/initdb** pour initialiser la base de donn�es
- Chargez la page **http://www.monsite.com/connecthys/portail.cgi/accueil** pour ouvrir le portail
