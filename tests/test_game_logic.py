from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_too_high_go_lower():
    # If secret is 16 and guess is 17, hint should be "Too High"
    outcome, _ = check_guess(17, 16)
    assert outcome == "Too High"

def test_guess_too_low_go_higher():
    # If secret is 16 and guess is 10, hint should be "Too Low"
    outcome, _ = check_guess(10, 16)
    assert outcome == "Too Low"

def test_guess_exact_match():
    # If secret is 16 and guess is 16, it should be a win
    outcome, _ = check_guess(16, 16)
    assert outcome == "Win"
