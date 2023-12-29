#importation du module prédéfini xmlrpc du python pour 
#créer des classes rpc en python

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
#creation d'un classe service
class Service :

    #creation du constructeur pour l'initiation du l'annuaire vide
    #ou en vas stocker les membres
    def __init__ (self):
        self.membres = []
   
    
    # creation du méthode ajouterMembre qui sert à ajouter 
    #un membre à l'annuaire
    def ajouterMembre (self, nom , prenom , numero, email, fonction ):
        membre = {
            "nom" : nom,
            "prenom" : prenom,
            "numero":numero,
            "email": email,
            "fonction": fonction
        }
        self.membres.append(membre)
        return f"{nom} {prenom} est bien ajoutée à l'annuaire !"
    
    
    
    #Creation du méthode chercherMembre qui prend le nom et
    #retourne le numéro du téléphone et l'email du membre correspondant
    def chercherMembre (self , nom):
        for membre in self.membres:
             if membre["nom"] == nom :
                return {"email": membre["email"], "numero": membre["numero"]}

    
    #Creation du fonction afficherAnnuaire qui affiche les membres
    #de l'annuaire avec leur informations respectives   
    def afficherAnnuaire(self):
        if not self.membres:
            print("Aucun membre dans l'annuaire.")
        else:
            info_membre = []
            for member in self.membres:
                info_membre.append(f"{member['prenom']} {member['nom']} 
                                    | Email: {member['email']} 
                                    | Téléphone: {member['numero']} 
                                    | Fonction: {member['fonction']}")
            return info_membre            

    #Creation du méthode  afficherEnseignants pour afficher les membres ayant "enseignant" pour fonction
    def afficherEnseignants(self):
        membres_enseignants = []
        for membre in self.membres:
            if membre["fonction"].lower() == "enseignant":
               membres_enseignants.append(f"{membre['prenom']} {membre['nom']} 
                                          | Email: {membre['email']} 
                                          | Téléphone: {membre['numero']} 
                                          | Fonction: {membre['fonction']}") 
        return membres_enseignants
    
    #Creation du méthode afficherAdministratifs pour afficher les membres ayant "administratif" pour fonction
    def afficherAdministratifs(self):
        membres_administratifs = []
        for membre in self.membres:
            if membre["fonction"].lower() == "administratif":
                membres_administratifs.append(f"{membre['prenom']} {membre['nom']} 
                                              | Email: {membre['email']} 
                                              | Téléphone: {membre['numero']} 
                                              | Fonction: {membre['fonction']}")
        return membres_administratifs

#Restriction du path pour autorisé au serveur xmlrpc à écouter à un path spécifique
#C'est une procédure de sécurité rendant plus difficile l'accès et l'interaction des attaquants potentiels avec le serveur XML-RPC
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

#Creation d'un serveur XML-RPC
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:

    #Enregistrer les fonctions d'introspection XML-RPC
    server.register_introspection_functions()

    # Enregistrer l'instance de la classe Service
    server.register_instance(Service())

    print("Serveur XML-RPC est prêt à accepter les requêtes.")
    server.serve_forever()
    