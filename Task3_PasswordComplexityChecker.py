def assess_password_strength(password):
  """Assesses the strength of a password.

  Args:
    password: The password to assess.

  Returns:
    A string indicating the strength of the password.
  """

  # Check the length of the password.
  if len(password) < 8:
    return "Weak password. Password must be at least 8 characters long."

  # Check for the presence of uppercase and lowercase letters.
  if not any(char.isupper() for char in password):
    return "Weak password. Password must contain at least one uppercase letter."
  if not any(char.islower() for char in password):
    return "Weak password. Password must contain at least one lowercase letter."

  # Check for the presence of numbers.
  if not any(char.isdigit() for char in password):
    return "Weak password. Password must contain at least one number."

  # Check for the presence of special characters.
  if not any(char in "!@#$%^&*()" for char in password):
    return "Weak password. Password must contain at least one special character."

  # If all the criteria are met, the password is strong.
  return "Strong password."


# Get the password from the user.
password = input("Enter your password: ")

# Assess the strength of the password.
password_strength = assess_password_strength(password)

# Print the feedback to the user.
print(password_strength)