from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name ():

    assert make_full_name ("Kate", "Druchok") == "Druchok; Kate"
    assert make_full_name ("James", "Bond") == "Bond; James"
    assert make_full_name ("Bond", "James") == "James; Bond"
    assert make_full_name ("J", "Ng") == "Ng; J"
    assert make_full_name ("", "") == "; "

def test_extract_family_name ():

    assert extract_family_name ("Druchok; Kate") == "Druchok"
    assert extract_family_name ("Bond; James") == "Bond"
    assert extract_family_name ("James; Bond") == "James"
    assert extract_family_name ("Ng; J") == "Ng"
    assert extract_family_name ("; ") == ""

def test_extract_given_name ():

    assert extract_given_name ("Druchok; Kate") == "Kate"
    assert extract_given_name ("Bond; James") == "James"
    assert extract_given_name ("James; Bond") == "Bond"
    assert extract_given_name ("Ng; J") == "J"
    assert extract_given_name ("; ") == ""

pytest.main(["-v", "--tb=line", "-rN", __file__])