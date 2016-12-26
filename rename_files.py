import os


def rename_files():
    dir_name = os.getcwd() + '/prank'
    file_list = os.listdir(r"%s" % dir_name)

    for file_name in file_list:
        new_name = file_name.strip('0123456789')
        os.chdir(r"%s" % dir_name)
        os.rename(file_name, new_name)
    print(file_list)


rename_files()

# The renamed files now show photos that say:
# "Keys are in the closet behind the shoe box."
