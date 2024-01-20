import pytest

from WebSite.flask.gestioneUtente.Cliente import Cliente
from WebSite.flask.gestioneUtente.ClienteDAO import ClienteDAO


def test_correct_create_cliente():
    dao = ClienteDAO()
    cliente = Cliente("Luigimarino@gmail.com", "Luigi", "Marino", "Studente", "2002-07-20", "1234567891234567",
                      12, 2026, True, "Password1@.")
    num = dao.contacliente()
    dao.createCliente(cliente)
    newnum = dao.contacliente()
    assert newnum == num + 1


def test_not_correct_create_cliente():
    dao = ClienteDAO()
    cliente = Cliente("cristyanesp@gmail.com", "Cristyan", "Esposito", "Studente",
                      "2001-04-21", 9085362718192346, 7, 2024, "true", "UniRentHpass@!.")
    with pytest.raises(Exception):
        dao.createCliente(cliente)


def test_missing_data_create_cliente():
    dao = ClienteDAO()
    cliente = Cliente("marcoviola@gmail.com", "Marco", "Viola", "Locatore",
                      "2001-04-21", None, None, None, "true", "UniRentHpass@!.")
    with pytest.raises(ValueError):
        dao.createCliente(cliente)


def test_none_create_cliente():
    dao = ClienteDAO()
    cliente = None
    with pytest.raises(ValueError):
        dao.createCliente(cliente)
