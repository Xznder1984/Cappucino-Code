# Cappuccino Code ☕

A super simple, lightweight programming language that's easy to learn and fun to use!

## Quick Start

Just type in your terminal:
```bash
cap filename.capu
```
or
```bash
capu filename.capu
```

## Setup (One-Time Only!)

To use the `cap` or `capu` commands from anywhere on your computer:

1. **Add to PATH:**
   - Right-click "This PC" → Properties → Advanced System Settings
   - Click "Environment Variables"
   - Under "User variables", find "Path" and click "Edit"
   - Click "New" and add: `D:\Albarr\Claude made stuff\Random-Stuff\Cappucino Code`
   - Click OK on everything
   - Restart your terminal/VS Code

2. **Now you can run from anywhere:**
   ```bash
   cap myprogram.capu
   ```

## Language Features

### 🖨️ Output
```cappuccino
say "Hello, World!"
say "I'm learning to code!"
```

### 📥 Input
```cappuccino
name = ask "What's your name? "
age = ask "How old are you? "
```

### 🔢 Variables & Math
```cappuccino
x = 10
y = 5
result = x + y
say result

// You can use: + - * /
```

### 🔁 Loops (NEW!)
```cappuccino
repeat 5 {
    say "Hello!"
}

counter = 1
repeat 10 {
    say counter
    counter = counter + 1
}
```

### ❓ If Statements (NEW!)
```cappuccino
age = ask "How old are you? "

if age >= 13 {
    say "You're a teenager!"
}

if age < 13 {
    say "You're a kid!"
}

// You can use: == != > < >= <= is not
```

### 🎲 Random Numbers (NEW!)
```cappuccino
dice = random 1 6
say "You rolled a "
say dice

number = random 1 100
```

### ⏱️ Wait/Pause (NEW!)
```cappuccino
say "Starting countdown..."
wait 1
say "3..."
wait 1
say "2..."
wait 1
say "1..."
say "GO!"
```

### 🧹 Clear Screen (NEW!)
```cappuccino
clear
say "Screen is now clear!"
```

### 💬 Comments
```cappuccino
// This is a comment
// Comments help explain your code
```

## Example Programs

### 1. Number Guessing Game
```bash
cap guess_game.capu
```
Try to guess the secret number in 10 tries!

### 2. Calculator
```bash
cap calculator.capu
```
Add, subtract, multiply, or divide!

### 3. Quiz Game
```bash
cap quiz.capu
```
Test your knowledge with trivia questions!

### 4. Rock Paper Scissors
```bash
cap rock_paper_scissors.capu
```
Play against the computer!

### 5. Countdown Timer
```bash
cap countdown.capu
```
Set a countdown timer!

### 6. Times Table
```bash
cap times_table.capu
```
Generate multiplication tables!

### 7. Story Generator
```bash
cap story.capu
```
Create your own interactive story!

## Programming Tips

### Make decisions with IF:
```cappuccino
score = 95

if score >= 90 {
    say "Grade: A"
}

if score < 90 {
    say "Keep trying!"
}
```

### Use comparisons:
- `==` equals
- `!=` not equals
- `>` greater than
- `<` less than
- `>=` greater or equal
- `<=` less or equal
- `is` same as ==
- `not` same as !=

### Repeat actions:
```cappuccino
// Print numbers 1 to 10
num = 1
repeat 10 {
    say num
    num = num + 1
}
```

### Add randomness:
```cappuccino
// Random dice roll
dice = random 1 6
say dice

// Coin flip
coin = random 0 1
if coin == 0 {
    say "Heads!"
}
if coin == 1 {
    say "Tails!"
}
```

## Project Ideas

Try making these programs:
- ✅ To-do list tracker
- 🎮 Adventure game
- 💰 Budget calculator  
- 🌡️ Temperature converter
- 📝 Mad libs generator
- 🎵 Music quiz
- 🔢 Math practice game
- 🎯 Target score game

## File Extension

Cappuccino Code files use `.capu` extension!

## Need Help?

If you get an error, check:
- Did you spell everything correctly?
- Did you close all your { } brackets?
- Are your quotes matched (" ")?
- Did you use the right comparison (== not =)?

Have fun coding! ☕✨
