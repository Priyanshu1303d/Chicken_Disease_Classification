#Update the Components
import os
import urllib.request as request
import zipfile
import shutil
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} downloaded!!! wiht following into : \n{headers}")
        else:
            logger.info(f"file already exists of size : {get_size(Path(self.config.local_data_file))}")



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function return None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        # self.organize_images(unzip_path)

    # def organize_images(self, base_dir):
    #         """
    #         Organizes images into 'Healthy' and 'Cocci' subfolders.
    #         """
    #         healthy_dir = os.path.join(base_dir, "Healthy")
    #         cocci_dir = os.path.join(base_dir, "Cocci")

    #         os.makedirs(healthy_dir, exist_ok=True)
    #         os.makedirs(cocci_dir, exist_ok=True)

    #         for img in os.listdir(base_dir):
    #             img_path = os.path.join(base_dir, img)

    #             if os.path.isfile(img_path):  # Ensure it's a file, not a folder
    #                 if "healthy" in img.lower():
    #                     shutil.move(img_path, os.path.join(healthy_dir, img))
    #                 elif "cocci" in img.lower():
    #                     shutil.move(img_path, os.path.join(cocci_dir, img))

    #         logger.info("Images organized into 'Healthy' and 'Cocci' subfolders.")
