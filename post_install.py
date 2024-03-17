import subprocess
import sys

def download_nltk_data():
    print("Downloading NLTK data...")
    subprocess.run([sys.executable, "-m", "nltk.downloader", "words", "stopwords"], check=True)

def download_spacy_model():
    print("Downloading SpaCy language model...")
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"], check=True)

def main():
    try:
        download_nltk_data()
        download_spacy_model()
        print("Post-installation setup completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during post-installation setup: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
