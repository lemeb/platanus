from platanus import platanus


def test_assert_true() -> None:
    assert True


def test_main() -> None:
    assert platanus.main() is True
