# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game looked normal at first: it asked for a guess and gave hints. But the hints didn't always make sense and by the time a game ended the score and behavior didn't match what I'd expected.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
1. The hints were wrong: guessing 17 against a secret of 16 told me to go higher instead of lower.
2. After a game ended, I couldn't start a new round without refreshing the page.
3. The secret number didn't match the range shown in the instructions.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 17 when the secret is 16 | Hint says "Go Lower" | Hint says "Go Higher" | None |
| Game ends (win or loss), then try to keep playing | Can start a new round and keep guessing | Game freezes; only a page refresh lets me play again | None |
| Start a game when the range says 1-100 | Secret number is within the displayed range | Secret doesn't match the range shown in the instructions | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude pointed out that the attempts counter started at a different value on first load than after a new game, so the first round got one fewer attempt. I verified it by starting the app fresh, counting my attempts, then clicking New Game and counting again. After the fix both rounds gave the same number
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
To be honest I wrote my prompts very specific in the sense of being clear with i wanted to be done and this regard anything else that wouldn't support that goal at the moment. So the context was pretty slim, no UI was touched and only the functions that had to be addressed were addressed.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I didn't count a bug as fixed until two things were true: the new pytest test passed and I could reproduce the original scenario in the live game and see the correct behavior. For the hint bug that meant guessing 17 against a secret of 16 and seeing "Go Lower." For the new-game bug I played to win, clicked New Game and confirmed I could guess again.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran pytest after fixing check_guess. The tests I added checked a guess above the secret, a guess below it, and a correct guess. They passed, which showed that the comparison now returns the right outcome for all 3 cases.
- Did AI help you design or understand any tests? How?
Yes. Claude wrote the tests for the changes and explained why each one mattered such as why the guess-above-secret case directly targets the bug I found.
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