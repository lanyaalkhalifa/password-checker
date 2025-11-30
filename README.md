# Password Strength Checker

This is a small Python project I made to practice basic cybersecurity concepts.  
The program checks how strong a password is and gives it a one word description like “Weak,” “Medium,” or “Strong.”


## How the Program Works

Here’s the basic idea:

1. You type in a password.
2. The program looks for a few things:
   - Is it at least 8 characters long?
   - Does the password have numbers?
   - Does the password have lowercase letters?
   - Does the password have uppercase letters?
   - Does the password use any special characters?
3. For each point it finds, the score goes up.
4. Based on the score, it gives the password a strength rating.

It’s a simple way to show how passwords are judged for security.


## How To Run It:

demo video: https://drive.google.com/file/d/1EBgB9Hk6Lea8HyZvfKMRlMYRMIbEqNj6/view 

In a terminal or command prompt, use:

```bash
python3 password-checker.py


