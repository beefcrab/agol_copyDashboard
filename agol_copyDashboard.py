#----------------------------------------
# WTF is this shiz?:   * Copies Portal Web Apps to another Portal Enironment.
#                      * Primialry for dashboards but can be applied to other portal apps (TBC).
#                      * By default, it copies the webmap (data) and associates it to the app 
#                      * Ensure you have the right permissions to access the app and map items
# Why?                 * Duplicate an awesome template
#                      * Backup copy of an exsisting dashboard
#                      * Copy to different portal environments (eg: DEV -> TEST -> PROD)
# Python: 3.x
#--------------------------------------

from arcgis.gis import GIS
from IPython.display import display
from getpass import getpass

## PARAMETERS

#source
src = "arcgis.com"
src_admin = "wsl_slau"
src_admin_pwd = input("Enter your password source admin")
src_owner = "wsl_slau"

#target
tgt = "arcgis.com"
tgt_admin = "wsl_slau"
tgt_admin_pwd = input("Enter your password for target admin")
tgt_owner = "wsl_slau"
tgt_folder = "dashboard_transfer"

#list itemid here
db_itemID = [
   # eg: "a8247bcf45c54f34b96b96706ad74879"
             ] 

## VERIFY CONNECTION
source = GIS("https://" + src, src_admin, src_admin_pwd, verify_cert=False)
source_user = source.users.search(src_owner)
print("SOURCE: ",source)
print(" Source User: \t:\t" + source_user[0].username + "\t:\t" + source_user[0].role)

target = GIS("https://" + tgt, tgt_admin, tgt_admin_pwd, verify_cert=False)
target_user = target.users.search(tgt_owner)
print("TARGET: ",target)
print(" Target User: \t:\t" + target_user[0].username + "\t:\t" + target_user[0].role)

## COPY ITEMS IN LIST IN SPEICIFED FOLDER
for item in db_itemID:
    item = source.content.get(item)
    print("  #Transferring: ", item, " to folder: ", tgt_folder)
    target.content.clone_items([item], tgt_folder , copy_data=True, search_existing_items=False)
