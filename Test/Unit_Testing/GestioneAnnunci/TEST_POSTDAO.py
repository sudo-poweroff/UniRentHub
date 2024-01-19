import pytest

from WebSite.flask.gestioneAnnunci.Post import Post
from WebSite.flask.gestioneAnnunci.PostDAO import PostDAO


def test_correct_create_post():
    post = Post(25, "Ricerca di un coinquilino", "Sto cercando un coinquilino con cui condividere l'affitto per "
                                                 "questo anno e che è iscritto al corso di Informatica alla Federico "
                                                 "II", "francescopixcont@gmail.com")
    dao = PostDAO()
    num = dao.contapost()
    dao.createPost(post)
    newnum = dao.contapost()
    assert newnum == num + 1


def test_campinone_create_post():
    post = Post(titolo="Ricerca di un coinquilino", descrizione=None, email="francescopixcont@gmail.com")
    dao = PostDAO()
    with pytest.raises(ValueError):
        dao.createPost(post)

def  test_none_create_post():
    post = None
    dao = PostDAO()
    with pytest.raises(ValueError):
        dao.createPost(post)
