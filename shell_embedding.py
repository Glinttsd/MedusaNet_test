import os
import sys
# os.system("rm -rf test")

pdbbind_list =[]
f = open("/home/glinttsd/MedusaNet/MedusaNet_test/pdbbind_list", "r")
for line in f:
    pdbbind_list.append(line.strip())
f.close()

# ff = open("/home/glinttsd/MedusaNet/MedusaNet_test/pdbbind_v2017_refined/refined_set/1a94/1a94_ligand.mol2", "r")
# f.close()
# for pdbbind_name in pdbbind_list:
pdbbind_name = "1a94"
password = "123"
command = "/home/glinttsd/MedusaNet/MedusaNet_test/medusa dock -p /home/glinttsd/MedusaNet/MedusaNet_test/parameter -i " \
          + pdbbind_name + "_protein.pdb -m " + pdbbind_name + "_ligand.mol2 -o /home/glinttsd/MedusaNet/MedusaNet_test/pdbbind_output_S[XYZ]/" + \
          pdbbind_name + "_out.pdb -R -fast -S [XYZ]"
os.system("cd /home/glinttsd/MedusaNet/MedusaNet_test/pdbbind_v2017_refined/refined_set/" + pdbbind_name + "/")

os.system("echo %s | sudo -S %s" % (password, command))
# os.system("123")