from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # Regression: inverted hint bug — guess above secret must say Go LOWER, not Go HIGHER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message!r}"
    assert "HIGHER" not in message, f"Expected 'HIGHER' not in message, got: {message!r}"

def test_guess_too_low():
    # Regression: inverted hint bug — guess below secret must say Go HIGHER, not Go LOWER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message!r}"
    assert "LOWER" not in message, f"Expected 'LOWER' not in message, got: {message!r}"
