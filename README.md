# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

**Purpose:** A Streamlit number-guessing game where the player has limited attempts to find a secret number, with hints after each guess and a score.

**Bugs found:**
- The hint was wrong (guess 17 vs secret 16 said "Go Higher").
- After a game ended, the game froze until a page refresh.
- The secret number didn't match the range shown in the instructions.

**Fixes applied:**
- Moved `check_guess` into `logic_utils.py` and corrected the comparison, with pytest tests for too high, too low, and correct.
- Fixed the New Game logic so it resets session state (secret, attempts, score, status, history).

**Known issues not yet fixed:**
- The secret number doesn't always match the range shown in the instructions.
- The attempts counter is inconsistent on the first load (the first game gets one fewer attempt).
- Guesses outside 1-100 (like -1 and 0) are accepted and use up attempts.


## 📸 Demo Walkthrough

Sample game on Normal difficulty (range 1-100, 8 attempts). The secret number was 52.

1. The game starts with "Guess a number between 1 and 100. Attempts left: 8."
2. I guess 60. The game tells me to go lower, since 60 is above 52.
3. I guess 50. The game tells me to go higher, since 50 is below 52.
4. I guess 52. The game shows "Correct! You won! The secret was 52. Final score: 50."
5. I click New Game. A fresh round starts without refreshing the page.

Sample losing game (secret was 50):

1. I guess 8 times: -1, 10, 20, 90, 80, 65, 51, 45. Each guess uses one attempt.
2. After the 8th guess, attempts left reaches 0 and the game shows "Game over. Start a new game to try again."
3. I start a new game and can play again with no refresh needed.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
