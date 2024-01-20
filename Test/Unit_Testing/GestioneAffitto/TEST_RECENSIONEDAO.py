from WebSite.flask.gestioneAffitto.Recensione import Recensione
from WebSite.flask.gestioneAffitto.RecensioneDAO import RecensioneDAO
import pytest


def test_correct_create_recensione():
    rec = Recensione(2, "gioromano@gmail.com", "Bellissima esperienza", 5,
                     "La camera era pulita e accogliente.Ottima posizione!", '2023-02-20')
    dao = RecensioneDAO()
    num = dao.contarec()
    dao.recensione_alloggio(rec)
    newnum = dao.contarec()
    assert newnum == num + 1


def test_incomplete_create_recensione():
    rec = Recensione(2, "gioromano@gmail.com", "", "", "", "")
    dao = RecensioneDAO()
    with pytest.raises(ValueError):
        dao.recensione_alloggio(rec)


def test_none_create_recensione():
    rec = None
    dao = RecensioneDAO()
    with pytest.raises(ValueError):
        dao.recensione_alloggio(rec)
