--This creates a data base hbtn_oc_0. the data base if created even if the file already exists

db_name="hbtn_0c_0"


mysql -e "CREATE DATABASE IF NOT EXISTS $db_name;"
