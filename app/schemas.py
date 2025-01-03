from datetime import date, time
from typing import Any, Literal, Optional
from pydantic import BaseModel, EmailStr, Field
from typing import Union



class Admin(BaseModel):
    id: int
    username: str
    password: str

class Employe(BaseModel):
    id: int
    UserName: str
    Nom: str
    Prenom: str
    DN: date
    Mail: EmailStr
    Horaire: Optional[str] = None
    Photo: Optional[str] = None
    PassWord: str

# Schéma de base pour l'entrée des données des RH:
class RessourceHumaine(BaseModel):
    id: int
    UserName: str
    PassWord: str
    NomRH: str
    PrenomRH: str
    DNRH: date
    MailRH: EmailStr
    photo: Optional[str] = None

# Schéma pour la lecture des tâches
class Tache(BaseModel):
    IDTache: int
    NomTache: str

class EmployeTache(BaseModel):
    IDEmploye: int
    IDTache: int
    EtatTache: str

class HistoriqueCreate(BaseModel):
    JourDeSemaine: int
    Mois: int
    Heure: time
    EventName: Literal['CheckIn', 'CheckOut']
    IDEmploye: int

class HistoriqueResponse(HistoriqueCreate):
    IDHistorique: int

class Conge(BaseModel):
    IdConge: int
    DateDebut: date
    DateFin: date
    Motif: Optional[str] = None
    EtatConge: Optional[str] = None
    PhotoMotif: Optional[str] = None
    IDEmploye: int

class Abscence(BaseModel):
    IDAbscence: int
    Mois: int = Field(..., ge=1, le=12, description="Month of the absence (1-12)")
    Jour: int = Field(..., ge=1, le=31, description="Day of the absence (1-31)")
    IDEmploye: int

class LoginResponse(BaseModel):
    role: str

class SuccessResponse(BaseModel):
    message: str

class LoginRequest(BaseModel):
    username: str
    password: str