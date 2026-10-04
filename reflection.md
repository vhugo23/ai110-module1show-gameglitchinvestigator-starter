# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked normal at first: it asked for a guess and gave hints. But the hints didn't always make sense, and by the time a game ended the score and behavior didn't match what I expected.

- List at least two concrete bugs you noticed at the start
1. The hints were wrong: guessing 17 against a secret of 16 told me to go higher instead of lower.
2. After a game ended, I couldn't start a new round without refreshing the page.
3. Out-of-range guesses like -1 were accepted and used up an attempt.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 17 when the secret is 16 | Hint says "Go Lower" | Hint says "Go Higher" | None |
| Game ends (win or loss), then try to keep playing | Can start a new round and keep guessing | Game freezes; only a page refresh lets me play again | None |
| Guess -1 when the range is 1-100 | Rejected as invalid, no attempt used | Accepted and recorded in History as a guess (it was the first entry of an 8-attempt game) | None |

**Session trace (Normal difficulty, run with `streamlit run app.py`, after the first two fixes):**

```
Game 1: Secret 52
  Guess 60 -> "Go LOWER!"
  Guess 50 -> "Go HIGHER!"
  Guess 52 -> "Correct! You won! The secret was 52. Final score: 50"
  New Game -> fresh round started without refreshing the page

Game 2: Secret 50
  Guesses: -1, 10, 20, 90, 80, 65, 51, 45  (Attempts: 8, Attempts left: 0)
  -> "Game over. Start a new game to try again."
  Note: -1 was accepted as a valid guess and used an attempt.
```

**Where each bug lives:**
1. Wrong hint: the comparison in `check_guess` pointed the wrong way.
2. Freeze after game end: the new-game handler in `app.py` didn't reset the game status in `st.session_state`.
3. Out-of-range guesses: guess parsing has no check that the number is inside the range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project?
I used Claude, both in the VS Code agent to explain and fix the code and in a chat to plan my workflow and review results.

- Give one example of an AI suggestion that was correct.
I asked the agent to explain why a guess of 17 against a secret of 16 gave "Go Higher." It explained that the comparison in the original code was pointing the wrong way, so guesses above the secret got the message meant for guesses below it. This was correct because when I moved `check_guess` into `logic_utils.py` and fixed the comparison, the pytest cases for too high, too low, and correct all passed. In the live game, guessing above the secret now showed "Go LOWER!".

- Give one example of an AI suggestion you did not accept as written.
After the fixes, `pytest` failed on all six tests because `check_guess` returns a tuple like `('Too High', '📉 Go LOWER!')`, but the tests compared the result to a plain string like `"Too High"`. One option was to change `check_guess` to return only the string. I rejected that because `app.py` uses both the outcome and the message, so changing the function risked breaking the UI. Instead I had the agent update only the tests to check the first element of the tuple, and told it not to touch `check_guess` or `app.py`. I verified it by running `pytest`, which showed 6 passed, and by replaying the game to confirm the hints still displayed.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I counted a bug as fixed only when two things were true: the pytest tests passed and I could repeat the original scenario in the live game and see the right behavior. For the hint bug, that meant seeing "Go LOWER!" when guessing above the secret. For the new-game bug, I played to a win, clicked New Game, and confirmed I could guess again without refreshing.

- Describe at least one test you ran and what it showed you about your code.
I ran `pytest` on the tests for `check_guess` (guess 17 vs secret 16, guess 10 vs secret 16, and 16 vs 16). At first all six tests failed, which looked like a logic problem. The failure output showed `('Too High', '📉 Go LOWER!')` against an expected `"Too High"`, so the logic was correct and the tests were comparing against the wrong type. After I fixed the tests, `pytest` showed 6 passed. I also had to add a `conftest.py` because pytest couldn't import `logic_utils` from the `tests/` folder.

- Did AI help you design or understand any tests? How?
Yes. The agent wrote the tests for the hint fix and explained why each one mattered, for example why a guess above the secret directly targets the bug. When they failed, reading the assertion output helped me see that the problem was the tuple return type, not the hint logic.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you click or type something in a Streamlit app, it reruns your whole Python script from top to bottom so regular variables are wiped and start over. Session state is the app's memory: values saved there like the secret number or the score survive those reruns until you deliberately change or reset them.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
The use of the reflection.md file. Debug using the agent to explain what the function does conceptually, apply it, test it and document it
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
I would start first by running the app and try to map out the functionalities at the codebase. Discuss possible fixes, get clarity, but also tame the beast by specific with the task at hand and avoid over-engineering
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It was the perfect application of what we have been doing in the breakout rooms. It's possible to maximize AI generated code when I'm the driver and dictate the pace whereas the agent is my navigator and puts me aware of things that can be done but it is up to me to make the final call as the person on the wheel.

---