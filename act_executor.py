import os
import subprocess


def execute_act_prsim_code(act_file, prsim_file):
    outp = ""
    os.system(f'aflat {act_file} > test_inv.prs')
    with open(f'{prsim_file}', "r") as f:
        outp = f.read()
        print(outp)
    p = subprocess.Popen(["prsim", "test_inv.prs"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    temp = p.communicate(input=outp)
    print(temp)
    outstr = temp[0]
    p.kill()
    print(outstr)
    return outstr
   

