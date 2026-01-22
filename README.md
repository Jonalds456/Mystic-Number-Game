# Mystic-Number-Game
A logic-based terminal game where players attempt to uncover a hidden number.

## 🎮 Game Design Document (SDLC Report)

**Name:** Jonathan Akinola Oyerinsola
**Matric No.:** 24/14642
**Course.:** Software Engineering


### Phase 1: Concept & Requirements
The goal is to create an interactive "Guess the Number" game. 
**Core Mechanics:**
1.  **Randomization:** The computer must pick a random integer between 1 and 100.
2.  **Feedback Loop:** After every guess, the system must inform the player if their guess was "Too High" or "Too Low".
3.  **Difficulty Settings:** The user chooses a difficulty level which dictates the `max_lives`.
    *   Easy Mode: 10 Lives.
    *   Hard Mode: 5 Lives.
4.  **Win/Loss States:** The game ends when the number is guessed (Win) or lives reach zero (Loss).

### Phase 2: System Architecture
The game logic is structured around a central game engine function.

*   **State Variables:**
    *   `hidden_target`: The integer the player is trying to guess.
    *   `current_lives`: Integer tracking remaining attempts.
*   **Modules:**
    *   `config_difficulty()`: Handles user input to set the `max_lives`.
    *   `start_engine()`: The main loop that compares the user's input against `hidden_target`.
*   **Flow:**
    Start -> Select Difficulty -> Generate Random Number -> Loop (Guess -> Feedback -> Decrement Lives) -> End Game.

### Phase 3: Implementation
The game is coded in Python using the `random` module.
*   **Input Handling:** A helper function `get_valid_integer()` was implemented to prevent the game from crashing if the user types text instead of numbers.
*   **Logic:** Uses standard comparison operators (`<`, `>`) to trigger the "Too High/Low" hints.

### Phase 4: Testing & QA
**Playtesting Results:**
1.  **Victory Condition:** Guessed the number correctly on the last life.
    *   *Result:* Game displayed "Victory" message and terminated correctly.
2.  **Defeat Condition:** Exhausted all 5 lives in Hard Mode.
    *   *Result:* Game revealed the `hidden_target` and displayed "Game Over".
3.  **Input Stress Test:** Entered "Fifty" instead of "50".
    *   *Result:* `get_valid_integer()` caught the error and requested a number.

### Phase 5: Release
The game is distributed as `mystic_guess.py`. It runs in any Python 3 environment.

---

## 🕹 How to Play

1.  Open your terminal.
2.  Run the game:
    ```bash
    python mystic_guess.py
    ```
3.  Type `easy` or `hard` to set your difficulty.
4.  Enter numbers between 1 and 100 to find the secret number!
________________________________________
