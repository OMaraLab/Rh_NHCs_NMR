import numpy as np
import matplotlib.pyplot as plt
import glob

out = glob.glob("*.out")
with open(out[0]) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "Orbital contributions to the principal shielding components of Nuc=2Se (ppm)" in line:
            pair_start = i+2
        if "Orbital pair contributions to the principal shielding components of Nuc=2Se (ppm)" in line:
            pair_end = i -1
    pairlines = lines[pair_start:pair_end]
    MO_is = []
    MO_js = []
    ISOs = []
    iso_pairs = []
    total_xs = []
    total_ys = []
    total_zs = []
    for line in pairlines:
        toks = line.split()
        MO_i = int(toks[0])
        MO_is.append(MO_i)
        DIA_x = float(toks[1])
        DIA_y = float(toks[2])
        DIA_z = float(toks[3])
        PARA_x = float(toks[4])
        PARA_y = float(toks[5])
        PARA_z = float(toks[6])
        TOTAL_x = float(toks[7])
        total_xs.append(TOTAL_x)
        TOTAL_y = float(toks[8])
        total_ys.append(TOTAL_y)
        TOTAL_z = float(toks[9])
        total_zs.append(TOTAL_z)
        ISO = float(toks[10])
        ISOs.append(ISO)
        ANISO = float(toks[11])
        iso_pairs.append([MO_i,ISO])
    
    MO_is = np.asarray(MO_is)
    print(MO_is)
    MO_i_max = MO_is.max()
    ISOs = np.asarray(ISOs)
    ISO_min = ISOs.min()
    total_xs = np.asarray(total_xs)
    total_ys = np.asarray(total_ys)
    total_zs = np.asarray(total_zs)




    plt.scatter(MO_is, total_xs, label='X', s=2)
    plt.scatter(MO_is, total_ys,  label='Y', s=2)
    plt.scatter(MO_is, total_zs,  label='Z', s=2)
    plt.scatter(MO_is, ISOs, label="TOTAL", s=4, color="purple")
    plt.legend()

    plt.show()
    


           


