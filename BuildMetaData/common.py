import os

# COMMON - DATA
################################################################################
# PATH TO STORE META DATA
PATH_META_DATA = str(os.environ.get("PATH_META_DATA"))
FOLDER_NAME = str(os.environ.get("FOLDER_NAME"))
FILE_RARITY = str(os.environ.get("FILE_RARITY"))

################################################################################
# FORMATS
FILE_FORMAT = ".json"
IMAGE_FORMAT_PNG = "png"
IMAGE_FORMAT_WEBP = "webp"


################################################################################
# PATH TO STORE IMAGES WITH BACKGROUND
PATH_IMAGE_BG_STORE_PNG = "image_bg_png"
PATH_IMAGE_BG_STORE_WEBP = "image_bg_webp"
PATH_IMAGES_BG = "image/background"

################################################################################
# URL
URL_LINK = "https://dev.api.valtreas.com/metadata/images/equipment/"
