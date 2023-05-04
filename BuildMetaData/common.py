import os

from .views.meta_data_types import EBaseEquipment, EEquipmentType

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


################################################################################
# EQUIPMENT MAPPING
equipment_mapping = dict(
    {
        EEquipmentType.HELMET.value: EBaseEquipment.ARMOR.value,
        EEquipmentType.ARMOR.value: EBaseEquipment.ARMOR.value,
        EEquipmentType.BRACERS.value: EBaseEquipment.ARMOR.value,
        EEquipmentType.BOOTS.value: EBaseEquipment.ARMOR.value,
        EEquipmentType.SHIELD_1H.value: EBaseEquipment.SHIELD.value,
        EEquipmentType.BOW_2H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.SWORD_2H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.SWORD_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.AXE_2H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.AXE_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.HAMMER_2H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.HAMMER_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.LANCE_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.GUN_1H.value: EBaseEquipment.WEAPON.value,
        EEquipmentType.WAND_1H.value: EBaseEquipment.WEAPON.value,
    }
)
