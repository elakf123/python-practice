from log_stats import count_levels

def test_count_levels():
    lines = ["INFO запуск", "ERROR сбой", "INFO конец"]
    assert count_levels(lines) == {"INFO": 2, "ERROR": 1}

def test_empty_list():
    lines = []
    assert count_levels(lines) == {}

def test_list_with_empty_string():
    lines = ["INFO запуск", "ERROR сбой", ""]
    assert count_levels(lines) == {"INFO": 1, "ERROR": 1}

def test_lines_with_newlines():
    lines = ["INFO запуск\n", "\n", "ERROR сбой\n"]
    assert count_levels(lines) == {"INFO": 1, "ERROR": 1}

def test_unknown_level():
    lines = ["INFO запуск", "DEBUG что-то"]
    assert count_levels(lines) == {"INFO": 1, "DEBUG": 1}
