from Lesson2 import get_winner


def test_rules():
    assert get_winner("к", "н") == "player"
    assert get_winner("н", "б") == "player"
    assert get_winner("б", "к") == "player"
    assert get_winner("н", "к") == "computer"
    assert get_winner("к", "к") == "draw"
