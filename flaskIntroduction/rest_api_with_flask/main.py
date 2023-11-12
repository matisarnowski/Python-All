# -*- coding: UTF-8 -*-

"""W tym projekcie używam modułu json do otwieranai i operowania na plikach json"""
import json
 
from typing import Optional, Query
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

"""Moja podstawowa klasa, która będzie tworzyć obiekty do pliku json."""
class Person(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    gender: str
    age: int
    
with open('people.json', 'r+', encoding='utf-8') as f:
    people = json.load(f)['people']
  
@app.get('/person/{person_id}', status_code=200)
def get_person(person_id: int):
    """
    Funkcja zwracająca obiekt na stronie Internetowej.
    """  
    person = [p for p in people if p['id'] == person_id]
    
    return person[0] if len(person) > 0 else {} 

def search_person(
    age: Optional[int] = Query(None, title="age", description="Wiek do filtrowania."), 
    first_name: 
        Optional[str] = Query(None, title="first_name", description="Imię do filtrowania.")):
    """
    Funkcja szukająca obiektu w bazie danych.
    """
    people1 = [p for p in people if p['age'] == age]
    
    if first_name is None:
        if age is None:
            return people
        else:
            return people1
    else:
        people2 = [p for p in people1 if first_name.lower() in p['first_name'].lower()]
        if age is None:
            return people2
        else:
            combined = [p for p in people1 if p in people2]
            return combined