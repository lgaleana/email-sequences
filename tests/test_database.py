from database import engine, SessionLocal, Base


def test_database_setup():
    assert engine
    assert SessionLocal
    assert Base