from sqlite3 import IntegrityError

import pytest
from _mysql_connector import MySQLInterfaceError

from WebSite.flask.gestioneUtente.Dipendente import Dipendente
from WebSite.flask.gestioneUtente.DipendenteDAO import DipendenteDAO


def test_correct_create_Homechecker():
    dao = DipendenteDAO()
    dip = Dipendente("sorrentinogiuseppepio@gmail.com", "Giuseppe", "Sorrentino", "", "Password1@.")
    num = dao.contadip()
    dao.registra_homechecker(dip)
    newnum = dao.contadip()
    assert newnum == num + 1


def test_not_correct_create_homechecker():
    dao = DipendenteDAO()
    dip = Dipendente("kekkamancini@gmail.com", "Francesca", "Mancini", "", "kekkaLoc007@.")
    with pytest.raises(Exception):
        dao.registra_homechecker(dip)


def test_not_correct_create_homecheker_nonedata():
    dip = None
    dao = DipendenteDAO()
    with pytest.raises(ValueError):
        dao.registra_homechecker(dip)


def test_not_correct_create_homecheker_notalledata():
    dip = Dipendente("marcogreco@gmail.com")
    dao = DipendenteDAO()
    with pytest.raises(ValueError):
        dao.registra_homechecker(dip)

