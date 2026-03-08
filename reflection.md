# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- <strong>Inverted Directional Hints</strong>
  - <strong>Expected:</strong> Guessing lower than the secret number should trigger a "Go Higher" hint.
  - <strong>Actual:</strong> The game provides a "Go Lower" hint for low guesses and "Go Higher" for high guesses.
- <strong>Lack of Input Validation</strong>
  - <strong>Expected:</strong> Entering a number outside the defined range should trigger an error message and not consume an attempt.
  - <strong>Actual:</strong> Out-of-bounds guesses are accepted, and the user loses an attempt for an invalid entry.
- <strong>Submit Button Latency</strong>
  - <strong>Expected:</strong> Clicking "Submit Guess" once should immediately provide feedback and update the debug history.
  - <strong>Actual:</strong> After the first guess, the button must be clicked twice to trigger a response. The debug history also fails to update on the first click.
- <strong>New Game Initialization Failure</strong>
  - <strong>Expected:</strong> Clicking "New Game" should reset the secret number, clear the history log and reset the attempt counter.
  - <strong>Actual:</strong> While the secret number and attempts reset, the history persists on screen and the "Submit Guess" button becomes unresponsive.å
- <strong>Difficulty Scaling Inversion</strong>
  - <strong>Expected:</strong> "Normal" difficulty should be more challenging (fewer attempts/larger range) than "Easy".
  - <strong>Actual:</strong> "Easy" mode is currently harder than "Normal," offering fewer attempts to the player.
- <strong>Settings vs. Main Display Mismatch</strong>
  - <strong>Expected:</strong> The range and attempts defined in the Settings menu should match the values displayed on the Game screen.
  - <strong>Actual:</strong> There is a discrepancy between the two; the game does not correctly pull the configuration values into the main UI.

---

## 2. How did you use AI as a teammate?

I used <strong>Claude Code</strong> to investigate and repair the bugs.

- <strong> Bug 1: Inverted Directional Hints</strong>
  - <strong>Correct AI suggestion example:</strong> The hint messages in check_guess are swapped relative to the outcome labels.
  - <strong>Incorrect AI suggestion example:</strong> No incorrect suggestion for this bug encountered.

- <strong> Bug 2: Lack of Input Validation</strong>
  - <strong>Correct AI suggestion example:</strong> The "parse_guess" function only checks if the input is empty and if it is a number. There is no range check.
  - <strong>Incorrect AI suggestion example:</strong> Claude missed that the attempt number was incremented before the guess check was completed. Hence, even for guesses that aren't within the given parameters the attempt number would increase.

---

## 3. Debugging and testing your fixes

I tested the fixes by unit tests using Pytest and manual tests. <strong>Claude code</strong> helped design the unit tests based on the parameters I provided.

- <strong> Bug 1: Inverted Directional Hints</strong>
  - A <strong>manual test</strong> revealed that a guess of "34" against a secret of "4" incorrectly triggered a "Higher" hint because the secret was being cast as a string on even attempts, causing a lexicographical comparison that Claude fixed by ensuring the values remained integers.

- <strong> Bug 2: Lack of Input Validation</strong>
  - A <strong>manual test</strong> revealed that even for the "Easy" level the screen showed a message of "Enter number between 1 and 100" and the secret was higher than 20. This was another bug in the application. The main screen message was hardcoded and the secret was randomly generated from 0 - 100 all the time.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
