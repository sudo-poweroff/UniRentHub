import pytest

from WebSite.flask.gestioneAffitto.Affittare import Affittare
from WebSite.flask.gestioneAffitto.AffittareDAO import AffittareDAO


def test_correct_create_affitto():
    dao = AffittareDAO()
    affitto = Affittare(1, "gioromano@gmail.com", "2024-01-15", "2024-02-15", 6574837392817454, 1, 2024, 400)
    num = dao.contaaffitto()
    dao.creaaffitto(affitto)
    newnum = dao.contaaffitto()
    assert newnum == num + 1


def test_not_correct_create_affitto():
    dao = AffittareDAO()
    affitto = None
    with pytest.raises(ValueError):
        dao.creaaffitto(affitto)

def test_not_correct_create_affitto_data():
    dao = AffittareDAO()
    affitto = Affittare(2,"matteobianchi@gmail.com","2023-12-10","2024-01-25",None,12,2024,700)
    with pytest.raises(ValueError):
        dao.creaaffitto(affitto)
