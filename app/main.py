from typing import Dict, List
from urllib import request, response
from uuid import uuid4
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db
from fastapi.middleware.cors import CORSMiddleware


origins = [
    # Si vous utilisez l'IP locale
    "http://localhost:8008",
    "http://localhost:5173"
]


# Créer les tables dans la base de données
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines (remplacez par votre domaine pour plus de sécurité)
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes HTTP
    allow_headers=["*"],  # Permet tous les en-têtes
)
sessions: Dict[str, str] = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to your new API"}


@app.get("/emp", response_model=List[schemas.Employe])
def get_employe(db: Session = Depends(get_db)):
    return crud.get_employe(db=db)

@app.get("/RH", response_model=List[schemas.RessourceHumaine])
def get_RH(db: Session = Depends(get_db)):
    return crud.get_RH(db=db)

@app.get("/TACHE", response_model=List[schemas.Tache])
def get_tache(db: Session = Depends(get_db)):
    return crud.get_tache(db=db)

@app.get("/EMPLOYE-TACHE", response_model=List[schemas.EmployeTache])
def get_employe_tache(db: Session = Depends(get_db)):
    return crud.get_employe_tache(db=db)

@app.get("/HISTORIQUE", response_model=List[schemas.HistoriqueResponse])
def get_historique(db: Session = Depends(get_db)):
    return crud.get_historique(db=db)

@app.get("/CONGE", response_model=List[schemas.Conge])
def get_conge(db: Session = Depends(get_db)):
    return crud.get_conge(db=db)

@app.get("/ABSCENCE", response_model=List[schemas.Abscence])
def get_abscence(db: Session = Depends(get_db)):
    return crud.get_abscence(db=db)


@app.post("/add/admin", response_model=schemas.Admin)
def create_admin(
    admin: schemas.Admin, 
    response: Response,  # Add this parameter
    db: Session = Depends(get_db)
):
    return crud.create_admin(db=db, admin=admin, response=response)

@app.post("/add_employe", response_model=schemas.Employe)
def create_employ(
    employ: schemas.Employe, 
    db: Session = Depends(get_db)
):
    return crud.create_employ(db=db, employ=employ)

@app.post("/add_RH", response_model=schemas.RessourceHumaine)
def create_RH(
    RH: schemas.RessourceHumaine, 
    db: Session = Depends(get_db)
):  
    return crud.create_RH(db=db, rh=RH)


@app.post("/auth/login", response_model=schemas.LoginResponse)
def login(credentials: schemas.LoginRequest, response: Response, db: Session = Depends(get_db)):
    return crud.login(db=db, username=credentials.username, password=credentials.password, response=response)

@app.put("/update/employe/{employe_username}", response_model =schemas.SuccessResponse)
def update_employe(
    employe_username: str,
    employ: schemas.Employe,
    db: Session = Depends(get_db)
):
    return crud.update_employe(db=db, employe_user=employe_username, employ=employ)

@app.post("/employee/profile", response_model=schemas.Employe)
def get_employee_profile(
    username: str,
    request: Request,
    db: Session = Depends(get_db)
):
    return crud.get_employee_profile(db=db, username=username, request=request)


@app.get("/employee/check-history", response_model=List[schemas.HistoriqueResponse])
def check_employee_history(
    username: str,
    request: Request,
    db: Session = Depends(get_db)
):
    return crud.check_employee_history(db=db, username=username,request=request)

@app.get("/employee/tasks", response_model=List[schemas.EmployeTache])
def get_employee_tasks(
    username: str,
    request: Request,
    db: Session = Depends(get_db)
):
    return crud.get_employee_tasks(db=db, username=username,request=request)

@app.put("/employee/tasks/{task_id}", response_model=schemas.SuccessResponse)
def update_employee_task(
    task_id: int,
    request: Request,
    new_status: str,
    db: Session = Depends(get_db)
):
    return crud.update_employee_task(db=db, task_id=task_id, new_status=new_status, request=request)







