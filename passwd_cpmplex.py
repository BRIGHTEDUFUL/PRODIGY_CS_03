import getpass  # For secure password input

def assess_password_strength(password: str) -> tuple[str, list]:
    """Analyze password against security criteria and return strength rating with feedback."""
    
    # Define criteria checks
    criteria = {
        'length': len(password) >= 8,
        'uppercase': any(c.isupper() for c in password),
        'lowercase': any(c.islower() for c in password),
        'digit': any(c.isdigit() for c in password),
        'special': any(not c.isalnum() for c in password)
    }
    
    # Calculate strength score
    score = sum(criteria.values())
    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        0: "Very Weak",
        1: "Very Weak"
    }
    
    # Generate feedback messages
    feedback = []
    if not criteria['length']:
        feedback.append("- Should be at least 8 characters long")
    if not criteria['uppercase']:
        feedback.append("- Should contain at least one uppercase letter (A-Z)")
    if not criteria['lowercase']:
        feedback.append("- Should contain at least one lowercase letter (a-z)")
    if not criteria['digit']:
        feedback.append("- Should include at least one digit (0-9)")
    if not criteria['special']:
        feedback.append("- Should contain at least one special character (!@#$%^ etc.)")
    
    return strength_levels[score], feedback

def main():
    print("\n🔒 Password Strength Analyzer")
    print("-----------------------------")
    
    while True:
        try:
            # Get password input securely
            password = getpass.getpass("\nEnter password (CTRL+C to exit): ").strip()
            
            if not password:
                print("⚠️ Error: Password cannot be empty!")
                continue
                
            # Analyze password
            strength, feedback = assess_password_strength(password)
            
            # Display results
            print(f"\nPassword Strength: {strength}")
            if feedback:
                print("\nRecommendations for improvement:")
                print("\n".join(feedback))
            else:
                print("✅ Excellent password! All security criteria met.")
            
            # Strength breakdown visualization
            print("\nSecurity Criteria:")
            print(f"Length ≥8: {'✓' if len(password)>=8 else '✗'} ({len(password)} chars)")
            print(f"Uppercase: {'✓' if any(c.isupper() for c in password) else '✗'}")
            print(f"Lowercase: {'✓' if any(c.islower() for c in password) else '✗'}")
            print(f"Digits:    {'✓' if any(c.isdigit() for c in password) else '✗'}")
            print(f"Special:   {'✓' if any(not c.isalnum() for c in password) else '✗'}")

        except KeyboardInterrupt:
            print("\n\nExiting... Stay secure! 🔑")
            break

if __name__ == "__main__":
    main()