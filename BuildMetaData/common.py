import os

# COMMON - DATA
################################################################################
# PATH TO STORE META DATA
PATH_META_DATA = str(os.environ.get("PATH_META_DATA"))
FOLDER_METADATA = str(os.environ.get("FOLDER_METADATA"))
FILE_RARITY = str(os.environ.get("FILE_RARITY"))

################################################################################
# FORMATS
FILE_JSON = ".json"
IMAGE_PNG = ".png"
IMAGE_WEBP = ".webp"


################################################################################
# PATH TO STORE IMAGES WITH BACKGROUND
PATH_RESULT_PNG = "image_bg_png"
PATH_RESULT_WEBP = "image_bg_webp"
PATH_IMAGES_BG = "background"

################################################################################
# URL
URL_LINK = "https://dev.api.valtreas.com/metadata/images/equipment/"
