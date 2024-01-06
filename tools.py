import datetime
import os

def get_julian_date():
    return datetime.datetime.now().strftime('%Y%j')

def rename_file_with_new_path(file_path, new_directory, modifier):
    julian_date = get_julian_date()
    
    #Retrieve Filename only
    base_name = os.path.basename(file_path)
    
    #Split to file extension append modifier and julian date
    new_base_name = f"{os.path.splitext(base_name)[0]}_Upscaled_{modifier}X_{julian_date}{os.path.splitext(base_name)[1]}"
    new_file_path = os.path.join(new_directory, new_base_name)
    
    #Verify path and file exist
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    
    if  os.path.exists(new_file_path):
        return None

    return new_file_path