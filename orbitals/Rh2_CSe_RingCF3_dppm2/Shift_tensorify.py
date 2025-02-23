import numpy as np
import matplotlib.pyplot as plt

with open("Rh2_CSe_RingCF3_dppm2.out") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "Orbital pair contributions to the principal shielding components of Nuc=2Se (ppm)" in line:
            pair_start = i+2
        if " Nucleus   3Cl:" in line:
            pair_end = i -1
    pairlines = lines[pair_start:pair_end]
    MO_is = []
    MO_js = []
    ISOs = []
    iso_pairs = []
    for line in pairlines:
        toks = line.split()
        MO_i = int(toks[0])
        MO_is.append(MO_i)
        MO_j = int(toks[1])
        MO_js.append(MO_j)
        DIA_x = float(toks[2])
        DIA_y = float(toks[3])
        DIA_z = float(toks[4])
        PARA_x = float(toks[5])
        PARA_y = float(toks[6])
        PARA_z = float(toks[7])
        TOTAL_x = float(toks[8])
        TOTAL_y = float(toks[9])
        TOTAL_z = float(toks[10])
        ISO = float(toks[11])
        ISOs.append(ISO)
        ANISO = float(toks[12])
        iso_pairs.append([MO_i,MO_j,ISO])
    
    MO_is = np.asarray(MO_is)
    print(MO_is)
    MO_i_max = MO_is.max()
    MO_js = np.asarray(MO_js)
    MO_j_max = MO_js.max()
    ISOs = np.asarray(ISOs)
    ISO_min = ISOs.min()



    data = np.zeros((MO_i_max+1, MO_j_max+1))
    for pair in iso_pairs:
        i = pair[0]
        j = pair[1]
        val = pair[2]
        if val < -10:
            print(f"{i} {j} {val}")

        data[i,j] = val
    print(data.min())
    plt.matshow(data, cmap='bwr', vmin=-700, vmax=700)
    plt.axvline(x=MO_i_max, color="green", linestyle="dashed")

    plt.show()
    


           


