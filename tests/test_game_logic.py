from logic_utils import check_guess, parse_guess

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


# --- Input validation bug regression tests ---

def test_parse_guess_rejects_above_range():
    # Bug: out-of-range numbers were accepted and consumed an attempt
    ok, value, err = parse_guess("500", low=1, high=100)
    assert not ok
    assert value is None
    assert err is not None

def test_parse_guess_rejects_below_range():
    ok, value, err = parse_guess("0", low=1, high=100)
    assert not ok
    assert value is None
    assert err is not None

def test_parse_guess_accepts_boundary_values():
    # Values exactly at the boundary must be accepted
    ok_low, val_low, _ = parse_guess("1", low=1, high=100)
    assert ok_low and val_low == 1

    ok_high, val_high, _ = parse_guess("100", low=1, high=100)
    assert ok_high and val_high == 100

def test_parse_guess_respects_easy_range():
    # Easy mode: 1–20; 21 should be rejected
    ok, value, err = parse_guess("21", low=1, high=20)
    assert not ok
    assert value is None

def test_parse_guess_accepts_valid_in_easy_range():
    ok, value, _ = parse_guess("15", low=1, high=20)
    assert ok
    assert value == 15

def test_parse_guess_rejects_above_normal_range():
    # Normal mode: 1–100; 101 should be rejected
    ok, value, err = parse_guess("101", low=1, high=100)
    assert not ok
    assert value is None
    assert err is not None

def test_parse_guess_accepts_boundary_normal_range():
    ok_low, val_low, _ = parse_guess("1", low=1, high=100)
    assert ok_low and val_low == 1

    ok_high, val_high, _ = parse_guess("100", low=1, high=100)
    assert ok_high and val_high == 100

def test_parse_guess_accepts_valid_in_normal_range():
    ok, value, _ = parse_guess("57", low=1, high=100)
    assert ok
    assert value == 57

def test_parse_guess_rejects_above_hard_range():
    # Hard mode: 1–50; 51 should be rejected
    ok, value, err = parse_guess("51", low=1, high=50)
    assert not ok
    assert value is None
    assert err is not None

def test_parse_guess_accepts_boundary_hard_range():
    ok_low, val_low, _ = parse_guess("1", low=1, high=50)
    assert ok_low and val_low == 1

    ok_high, val_high, _ = parse_guess("50", low=1, high=50)
    assert ok_high and val_high == 50

def test_parse_guess_accepts_valid_in_hard_range():
    ok, value, _ = parse_guess("33", low=1, high=50)
    assert ok
    assert value == 33
