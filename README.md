# CommentChecker

CommentChecker checks for spelling mistakes in C styled Comments.

# Features
  - Gets tokens from code. So userdefined type names and variable declaration wont be thrown as spelling mistakes.
  - Can include a file with words to be ignored.
  - Checks recursively every folder from the given path.
  - Can exclude files and folders while checking recursively.

# Usage Instructions
- Clone the repository
- Options available
    1. -c or --check = Checks the file or folder recursively[Only one file/folder at a time]
    2. -i or --include = Includes the file/files ie words that the user doesn't want to be flagged as spelling mistakes
    3. -e or --exclude = Exclude file or folders from checking like .git
- Sample usage
    1.python3 Main.py -c "/home/user/folder_to_be_checked" -i "./additional1.txt ./additional2.txt" -e "__pycache__ .git"
    2.python3 Main.py --check=/home/user/folder_to_be_checked" --include="./additional1.txt ./additional2.txt" --exclude="__pycache__ .git"
