from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.dataset_download_files("asaniczka/data-science-job-postings-and-skills", path="./data", unzip=True)