import pandas as pd


def get_division_list(filename):
    file_string = "C:\\Users\\saone\\Documents\\Python Stuff\\prod\\single_elimination_tree_generator\\raw_divisions" + "\\" + filename
    df_load = pd.read_excel(file_string)
    df = df_load[["First Name", "Last Name", "Club Name"]].sort_values("Club Name")
    n_base = len(df)
    n_add = 0

    num_list = [2**0, 2**1, 2**2, 2**3, 2**4, 2**5, 2**6]

    for i, num in enumerate(num_list):
        if n_base <= num:
            n_add = num - n_base
            break

    n = n_base + n_add

    bye_frame = pd.DataFrame({
                        'First Name': ['Bye'],
                        'Last Name' : [''],
                        'Club Name' : ['']})

    for i in range(n_add):
        df = df.append(bye_frame, ignore_index=True)


    first_names = df['First Name'].tolist()
    last_names = df['Last Name'].tolist()
    clubs = df['Club Name'].tolist()

    complete_tree_list = []
    next_round_list = []
    division_list = []
    pre_org_list = []
    for i in range(n):
        division_list.append('')
        pre_org_list.append('')
        pre_org_list[i] = [first_names[i] + ' ' + last_names[i], clubs[i]]

    if n == 2:
        for i in range(n):
            division_list[0] = pre_org_list[0]
            division_list[1] = pre_org_list[1]
        complete_tree_list.append(division_list)
    elif n == 4:
        for i in range(n):
            division_list[0] = pre_org_list[0]
            division_list[3] = pre_org_list[1]
            division_list[1] = pre_org_list[2]
            division_list[2] = pre_org_list[3]
        complete_tree_list.append(division_list)
        complete_tree_list.append('')
    elif n == 8:
        for i in range(n):
            division_list[0] = pre_org_list[0]
            division_list[7] = pre_org_list[1]
            division_list[3] = pre_org_list[2]
            division_list[4] = pre_org_list[3]
            division_list[1] = pre_org_list[4]
            division_list[5] = pre_org_list[5]
            division_list[2] = pre_org_list[6]
            division_list[6] = pre_org_list[7]
        complete_tree_list.append(division_list)
        complete_tree_list.append('')
        complete_tree_list.append('')
    elif n == 16:
        for i in range(n):
            division_list[0] = pre_org_list[0]
            division_list[15] = pre_org_list[1]
            division_list[7] = pre_org_list[2]
            division_list[8] = pre_org_list[3]
            division_list[3] = pre_org_list[4]
            division_list[11] = pre_org_list[5]
            division_list[4] = pre_org_list[6]
            division_list[12] = pre_org_list[7]
            division_list[1] = pre_org_list[8]
            division_list[9] = pre_org_list[9]
            division_list[5] = pre_org_list[10]
            division_list[13] = pre_org_list[11]
            division_list[2] = pre_org_list[12]
            division_list[10] = pre_org_list[13]
            division_list[6] = pre_org_list[14]
            division_list[14] = pre_org_list[15]
        complete_tree_list.append(division_list)
        complete_tree_list.append('')
        complete_tree_list.append('')
        complete_tree_list.append('')
    elif n == 32:
        for i in range(n):
            division_list[0] = pre_org_list[0]
            division_list[31] = pre_org_list[1]
            division_list[15] = pre_org_list[2]
            division_list[16] = pre_org_list[3]
            division_list[7] = pre_org_list[4]
            division_list[23] = pre_org_list[5]
            division_list[8] = pre_org_list[6]
            division_list[24] = pre_org_list[7]
            division_list[3] = pre_org_list[8]
            division_list[19] = pre_org_list[9]
            division_list[11] = pre_org_list[10]
            division_list[27] = pre_org_list[11]
            division_list[4] = pre_org_list[12]
            division_list[20] = pre_org_list[13]
            division_list[12] = pre_org_list[14]
            division_list[28] = pre_org_list[15]
            division_list[1] = pre_org_list[16]
            division_list[30] = pre_org_list[17]
            division_list[14] = pre_org_list[18]
            division_list[17] = pre_org_list[19]
            division_list[6] = pre_org_list[20]
            division_list[22] = pre_org_list[21]
            division_list[9] = pre_org_list[22]
            division_list[25] = pre_org_list[23]
            division_list[2] = pre_org_list[24]
            division_list[18] = pre_org_list[25]
            division_list[10] = pre_org_list[26]
            division_list[26] = pre_org_list[27]
            division_list[5] = pre_org_list[28]
            division_list[21] = pre_org_list[29]
            division_list[13] = pre_org_list[30]
            division_list[29] = pre_org_list[31]
        complete_tree_list.append(division_list)
        complete_tree_list.append('')
        complete_tree_list.append('')
        complete_tree_list.append('')
        complete_tree_list.append('')
    
    
    
    return n, division_list, complete_tree_list, next_round_list