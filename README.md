# ⚔️ Text-Based RPG Battle (OOP Capstone)

A CLI-based Role-Playing Game (RPG) simulator written in Python. This project serves as a practical demonstration of **Object-Oriented Programming (OOP)** principles, featuring a battle system between different hero classes with unique abilities, weapon equipping, and state management.


## 🚀 Features

* **Hero Classes**: Selectable classes (`Warrior`, `Mage`) that inherit from a base `Hero` class.
* **Combat System**: Turn-based interaction allowing Attacks, Healing, and Ultimate Abilities.
* **Weapon System**: Heroes can equip `Weapon` objects to modify their damage output.
* **Encapsulation**: Uses private attributes (`__health`, `__experience`) to protect game state integrity.
* **Interactive Menu**: A `while` loop interface for user decision-making.

## 🛠️ Technical Concepts Applied

This project implements the four pillars of OOP:

1.  **Abstraction**: 
    * Uses `abc` (Abstract Base Classes).
    * The `Hero` class cannot be instantiated directly.
    * `ultimate_ability` is an `@abstractmethod`, forcing subclasses to define their own specific logic.
2.  **Inheritance**: 
    * `Warrior` and `Mage` extend the functionality of the `Hero` class.
    * Uses `super().__init__` to handle parent class initialization.
3.  **Encapsulation**: 
    * Health and Experience are private variables (`__health`), accessible only through specific getter/setter methods like `take_damage()` or `get_health()`.
4.  **Polymorphism**: 
    * The `attack()` method behaves differently depending on whether the object is a Warrior (Physical) or a Mage (Magic).

## 💻 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/text-based-rpg.git](https://github.com/yourusername/text-based-rpg.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd text-based-rpg
    ```
3.  **Run the game:**
    ```bash
    python text_based_rpg.py
    ```

## 🎮 Gameplay Example

```text
+--------------------------------+
 1. Attack
 2. Use Ultimate
 3. Heal
 4. View Stats
 5. Exit
+--------------------------------+
Please enter a number : 1
KDA swings a mighty sword!
KDA attacks with Dragon Slayer!
LM took 65 damage.
LM casts a fireball!
KDA took 20 damage.
