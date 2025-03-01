import pytest

from app.main import get_coin_combination


test_data = [cents for cents in range(0, 50)]


@pytest.mark.parametrize("cents", test_data)
class TestCoinCombination:
    def test_pennies_should_be_less_then_5(self, cents: int) -> None:
        result = get_coin_combination(cents)
        assert result[0] < 5

    def test_nickels_should_be_less_then_2(self, cents: int) -> None:
        result = get_coin_combination(cents)
        assert result[1] < 2

    def test_dimes_should_be_less_then_3(self, cents: int) -> None:
        result = get_coin_combination(cents)
        assert result[2] < 3

    def test_could_return_coins_of_the_different_types(
            self,
            cents: int) -> None:
        result = get_coin_combination(cents)

        if cents < 5:
            assert [cents, 0, 0, 0] == result
            return
        if cents == 5:
            assert [0, cents // 5, 0, 0] == result
            return
        if cents == 10:
            assert [0, 0, cents // 10, 0] == result
            return
        if cents == 25:
            assert [0, 0, 0, cents // 25] == result
            return

        pytest.skip()
