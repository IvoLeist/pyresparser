
venv:
	python3 -m venv venv
	. venv/bin/activate
	pip install .

	python3 -m spacy download en_core_web_sm
	python3 -m nltk.downloader words
	python3 -m nltk.downloader stopwords

test:
	pyresparser -f OmkarResume.pdf

run:
	pyresparser -d resumes/frontend/in > resumes/frontend/out/json/frontend_resumes_extracted.json

validate-output:
	python3 -m json.tool resumes/frontend/out/json/frontend_resumes_extracted.json