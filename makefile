install:
	poetry install
	poetry run pre-commit install

run:
	poetry run streamlit run app.py

docker:
	docker build -t stream-budget .
	docker run -p 8501:8501 stream-budget
