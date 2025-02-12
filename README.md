# PRODIGY_CS_03
password complexity checker
This project is part of my internship at Prodigy Infotech , where I developed a Password Complexity Checker to ensure that passwords meet security standards. The tool validates passwords against predefined criteria such as length, character types, and special requirements, helping users create strong and secure passwords.

Features
Password Validation : Checks if a password meets the following criteria:
Minimum length (e.g., 8 characters).
Contains uppercase letters.
Contains lowercase letters.
Includes numbers.
Includes special characters.
Customizable Rules : Allows administrators to define their own complexity rules.
User-Friendly Output : Provides clear feedback on why a password fails validation.
Technologies Used
Programming Language : Python
Libraries/Frameworks :
re: For regular expression-based pattern matching.
argparse: For parsing command-line arguments.
Tools :
Git: Version control.
GitHub: Hosting the repository.
Installation
Clone the repository:
bash
Copy
1
git clone https://github.com/BRIGHTEDUFUL/PRODIGY_CS_03.git
Navigate to the project directory:
bash
Copy
1
cd PRODIGY_CS_03
Install dependencies:
bash
Copy
1
pip install -r requirements.txt
Usage
Run the script with the following command:

bash
Copy
1
python main.py --password "YourPasswordHere"
For detailed usage instructions, refer to the comments in the code or the documentation folder.

