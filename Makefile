run:
	uvicorn app.main:app --reload

install_packages:
	pip install -r requirements.txt