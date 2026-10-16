import os
import sys

def check_workflow_file(file_path):
    if not os.path.exists(file_path):
        print(f"[ERROR] File {file_path} does not exist.")
        return False
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    required_elements = [
        'on:',
        'push:',
        'branches:',
        'main',
        'strategy:',
        'matrix:',
        'java-version:',
        "'17'",
        "'21'",
        'actions/checkout@v5',
        'actions/setup-java@v5',
        "distribution: 'temurin'",
        "cache: 'gradle'",
        './gradlew test'
    ]
    
    missing = [elem for elem in required_elements if elem not in content]
    
    if missing:
        print(f"[ERROR] Missing expected directives in workflow: {missing}")
        return False
        
    print(f"[SUCCESS] Workflow file {file_path} is valid and meets all matrix requirements.")
    return True

if __name__ == '__main__':
    workflow_path = '.github/workflows/ci-matrix.yml'
    success = check_workflow_file(workflow_path)
    if not success:
        sys.exit(1)
