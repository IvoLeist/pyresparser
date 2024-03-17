

docker_cmd=docker run --rm -v $(PWD)/resumes:/usr/src/app/resumes pyresparser:latest

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

docker-build:
	docker build -t pyresparser .

docker-run-json:
	$(docker_cmd) pyresparser -d resumes/frontend/in > resumes/frontend/out/json/frontend_resumes_extracted.json

docker-run-csv:
	$(docker_cmd) python3 export_to_csv.py resumes/frontend/in
