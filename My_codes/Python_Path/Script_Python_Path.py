import sys
from pprint import pprint
import module_test

pprint(sys.path)  # pour imprimer liste du PYTHONPATH
sys.path.append("/root/Formation_UDEMY_Python/My_codes/Python_Path/module_test") #pour ajouter le script dans le PYTHONPATH

# code ~/.bash_profile ->pour ouvrir le fichier bash_profile et exporter ses modules dans le PYTHONPATH
# export PYTHONPATH="/root/Formation_UDEMY_Python/My_codes/Python_Path"   -> pour definir dans .bash_profile le PYTHONPATH à utiliser