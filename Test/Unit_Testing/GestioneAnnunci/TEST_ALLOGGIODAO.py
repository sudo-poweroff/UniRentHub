import pytest

from WebSite.flask.gestioneAnnunci.Alloggio import Alloggio
from WebSite.flask.gestioneAnnunci.AlloggioDAO import AlloggioDAO


def test_correct_create_Alloggio():
    dao = AlloggioDAO()
    alloggio = Alloggio(disponibilita=1, titolo="Camera singola in centro", mq=50, n_bagni=1,
                        n_camere_letto=1, classe_energetica="A", arredamenti=1, data_publicazione="2024-01-10",
                        pannelli_fotovoltaici=0, tipo_alloggio="Camera",
                        descrizione="Bellissima camera in pieno centro della città", prezzo="250",
                        pannelli_solari=1, n_ospiti=1, tasse=5, email_dip="mariomuratore@gmail.com",
                        email_loc="kekkamancini@gmail.com", data_verifica="2024-01-17", n_stanze=2)
    num = dao.conta()
    dao.create_alloggio(alloggio)
    newnum = dao.conta()
    assert newnum == num + 1


def test_none_insert_allogio():
    dao = AlloggioDAO()
    alloggio = None
    with pytest.raises(ValueError):
        dao.create_alloggio(alloggio)

def test_nonedata_insert_allogio():
    dao = AlloggioDAO()
    alloggio = Alloggio(disponibilita=1, titolo="", mq=50, n_bagni=1,
                        n_camere_letto=1, classe_energetica="A", arredamenti=1, data_publicazione="2024-01-10",
                        pannelli_fotovoltaici=0, tipo_alloggio=None,
                        descrizione="Bellissima camera in pieno centro della città", prezzo="250",
                        pannelli_solari=1, n_ospiti=1, tasse=5, email_dip="mariomuratore@gmail.com",
                        email_loc="kekkamancini@gmail.com", data_verifica="2024-01-17", n_stanze=2)
    with pytest.raises(ValueError):
        dao.create_alloggio(alloggio)



