import os


def execute_act_prsim_code(act_file, prsim_file):
    outp = ""
    os.system(f'aflat {act_file } > test_inv.prs')
    os.system(f'{prsim_file} > prsim test_inv.prs > outinv.txt')
    with open('outinv.txt', "r") as f:
        outp = f.read()
        print(outp)

    return outp
