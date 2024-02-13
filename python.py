from docx import Document
import os
import subprocess

def create_word_file(text):
    doc = Document()
    doc.add_paragraph(text)
    doc.save("output.docx")

def create_virtual_env():
    env_name = "env"
    if os.name == "nt":  # Windows
        subprocess.run(["python", "-m", "venv", env_name])
        subprocess.run([f"{env_name}\\Scripts\\activate.bat"])
    else:
        subprocess.run(["python3", "-m", "venv", env_name])
        subprocess.run(["source", f"{env_name}/bin/activate"])

def install_package(package_name):
    """Install a package in the virtual environment."""
    subprocess.run(["pip", "install", package_name])

if __name__ == "__main__":
    create_virtual_env()
    package_name = "python-docx"
    install_package(package_name)
    print(f"Package '{package_name}' installed successfully!")
    text = input("Enter some text: ")
    create_word_file(text)
    print("Word file created successfully!")
