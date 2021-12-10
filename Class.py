class AxeRoutier:
  def __init__(self, IDAxe, nomAxe, longueurAxe, debit, vitesseMoy, tempsParcours, tauxOccupation, etatTrafic, geom):
    self.IDAxe  = IDAxe
    self.nomAxe = nomAxe
    self.longueurAxe = longueurAxe
    self.debit = debit
    self.vitesseMoy = vitesseMoy
    self.tempsParcours = tempsParcours
    self.tauxOccupation = tauxOccupation
    self.etatTrafic = etatTrafic
    self.geom = geom

  #getters
  def getIDAxe(self):
    return self.IDAxe
  def getNomAxe(self):
    return self.nomAxe
  def getLongueurAxe(self):
    return self.longueurAxe
  def getDebit(self):
    return self.debit
  def getVitesseMoy(self):
    return self.vitesseMoy
  def getTempsParcours(self):
    return self.tempsParcours
  def getTauxOccupation(self):
    return self.tauxOccupation
  def getEtatTrafic(self):
    return self.etatTrafic
  def getGeom(self):
    return self.geom
  
  #setters
  def setIDAxe(self, idAxe):
    self.IDAxe = idAxe
  def setNomAxe(self, nom):
    self.nomAxe = nom
  def setLongueurAxe(self, longueur):
    self.longueurAxe = longueur
  def setDebit(self, debit):
    self.debit = debit
  def setVitesseMoy(self, vitesse):
    self.vitesseMoy = vitesse
  def setTempsParcours(self, temps):
    self.tempsParcours = temps
  def setTauxOccupation(self, taux):
    self.tauxOccupation = taux
  def setEtatTrafic(self, etat):
    self.etatTrafic = etat
  def setGeom(self, geom):
    self.geom = geom
  
  #affichage
  def affichage(self):
    return "IDAxe = "+ self.IDAxe + ", Nom = "+ self.nomAxe +", Longueur = "+ self.longueurAxe +", Debit = "+self.debit+", Vitesse moyenne = "+self.vitesseMoy+", Temps de Parcours = "+self.tempsParcours+", Etat du Trafic = "+self.etatTrafic


class Vehicule:
  def __init__(self, IDVehicule, position):
    self.IDVehicule = IDVehicule
    self.position = position
    
    #getters
    def getIDVehicule(self):
      return self.IDVehicule
    def getPosition(self):
      return self.position
    
    #setters
    def setIDVehicule(self, idVehicule):
      self.IDVehicule = idVehicule
    def setPosition(self, pos):
      self.position = pos

class Tram(Vehicule):
  def __init__(self, IDVehicule, position, IDTram, ligne_tram):
    super().__init__(IDVehicule, position)
    self.IDTram = IDTram
    self.ligne_tram = ligne_tram
    
  #getters
  def getIDTram(self):
    return self.IDTram
  def getLigneTram(self):
    return self.ligne_tram
    
  #setters
  def setIDTram(self, idTram):
    self.IDTram = idTram
  def setLigneTram(self, ligne):
    self.ligne_tram = ligne

class Bus(Vehicule):
  def __init__(self, IDVehicule, position, IDBus, ligne_bus):
    super().__init__(IDVehicule, position)
    self.IDBus = IDBus
    self.ligne_bus = ligne_bus
  
  #getters
  def getIDBus(self):
    return self.IDBus
  def getLigneBus(self):
    return self.ligne_bus
  
  #setters
  def setIDBus(self, idBus):
    self.IDBus = idBus
  def setLigneBus(self, ligne):
    self.ligne_bus = ligne

class Velo(Vehicule):
  def __init__(self, IDVehicule, position, IDVelo):
    super().__init__(IDVehicule, position)
    self.IDVelo = IDVelo
  
  #getters
  def getIDVelo(self):
    return self.IDVelo
  
  #setters
  def setIDVelo(self, idVelo):
    self.IDVelo = idVelo


class Motorises(Vehicule):
  def __init__(self, IDVehicule, position, IDMotorises):
    super().__init__(IDVehicule, position)
    self.IDMotorises = IDMotorises


  #getters
  def getIDMotorises(self):
    return self.IDMotorises


  #setters
  def setIDMotorises(self, id):
    self.IDMotorises = id


class Ligne:
  def __init__(self, IDLigne, liste_station):
    self.IDLigne = IDLigne
    self.liste_station = liste_station


  #getters
  def getIDLigne(self):
    return self.IDLigne

  def getListe_station(self):
    return self.liste_station


  #setters
  def setIDLigne(self, id):
    self.IDLigne = id
  
  def setListe_station(self, l):
    self.liste_station = l
    

class Pieton:
  def __init__(self, IDPieton, position):
    self.IdPieton = IDPieton
    self.position = position


  #getters
  def getIDPieton(self):
    return self.IDPieton

  def getPosition(self):
    return self.position


  #setters
  def setIDPieton(self, id):
    self.IDPieton = id
  
  def setPosition(self, pos):
    self.position = pos
    

class FeuTricolore:
  def __init__(self, IDFeu, rue, position, couleur):
    self.IDFeu = IDFeu
    self.rue = rue
    self.position = position
    self.couleur = couleur
    

  #getters
  def getIDFeu(self):
    return self.IDFeu

  def getRue(self):
    return self.rue
  
  def getPosition(self):
    return self.position
  
  def getCouleur(self):
    return self.couleur


  #setters
  def setIDFeu(self, id):
    self.IDFeu = id
  
  def setRue(self, r):
    self.rue = r
  
  def setPosition(self, pos):
    self.position = pos
    
  def setCouleur(self, c):
    self.couleur = c
    
    
class StationBus:
  def __init__(self, IDStation, nomStation, rue, position):
    self.IDStation = IDStation
    self.nomStation = nomStation
    self.rue = rue
    self.position = position
    
  #getters
  def getIDStation(self):
    return self.IDStation
  
  def getNomStation(self):
    return self.nomStation

  def getRue(self):
    return self.rue
  
  def getPosition(self):
    return self.position
  
  #setters
  def setIDPassage(self, id):
    self.IDPassage = id
  
  def setNomStation(self, n):
    self.nomStation = n
  
  def setRue(self, r):
    self.rue = r
  
  def setPosition(self, pos):
    self.position = pos

class PassagePieton:
  def __init__(self, IDPassage, rue, position):
    self.IDPassage = IDPassage
    self.rue = rue
    self.position = position

  #getters
  def getIDPassage(self):
    return self.IDPassage
  
  def getRue(self):
    return self.rue
  
  def getPosition(self):
    return self.position
  
  #setters
  def setIDPassage(self, id):
    self.IDPassage = id
  
  def setRue(self, r):
    self.rue = r
  
  def setPosition(self, pos):
    self.position = pos