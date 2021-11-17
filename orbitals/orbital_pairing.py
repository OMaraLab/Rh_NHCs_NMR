import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_outfile_orbpairs(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "Orbital contributions to the isotropic and anisotropic shielding of Nuc=2Se (ppm)" in line:
                start_orbcon = i+3
            if "Orbital contributions to the principal shielding components of Nuc=2Se (ppm)" in line:
                end_orbcon = i-1 
                start_sc = i+2
            if "Orbital pair contributions to the principal shielding components of Nuc=2Se (ppm)" in line:
                end_sc = i-1
                start_orbpair = i
            if   "Nucleus   3Cl:" in line:
                end_orbpair = i-1

        # orbcon_iso_aniso
        orbcon_iso_aniso_lines = lines[start_orbcon:end_orbcon]
        data = []
        for line in orbcon_iso_aniso_lines:
            toks = line.split()
            MO = int(toks[0])
            iso_diag = float(toks[1])
            aniso_diag = float(toks[2])
            iso_occ_occ = float(toks[3])
            aniso_occ_occ = float(toks[4])
            iso_occ_virt = float(toks[5])
            aniso_occ_virt = float(toks[6])
            data.append([MO, iso_diag, aniso_diag, iso_occ_occ, aniso_occ_occ, iso_occ_virt, aniso_occ_virt])
        df_orbcon_iso_aniso = pd.DataFrame(data,columns=["MO", "ISO_DIAG", "ANISO_DIAG", "ISO_OCC_OCC", "ANISO_OCC_OCC", "ISO_OCC_VIRT", "ANISO_OCC_VIRT"] )
        n_orbs =  df_orbcon_iso_aniso["MO"].max()
        print("OCC_ORBS ",n_orbs)

        df_orbcon_iso_aniso = df_orbcon_iso_aniso.set_index("MO")
        


        # orbcon_sc
        orbcon_sc_lines = lines[start_sc:end_sc]
        data = []
        for line in orbcon_sc_lines:
            toks = line.split()
            MO = int(toks[0])
            diag_X = float(toks[1])
            diag_Y = float(toks[2])
            diag_Z = float(toks[3])
            para_X = float(toks[4])
            para_Y = float(toks[5])
            para_Z = float(toks[6])
            total_X = float(toks[7])
            total_Y = float(toks[8])
            total_Z = float(toks[9])
            ISO = float(toks[10])
            ANISO = float(toks[11])
            data.append([MO, diag_X, diag_Y, diag_Z, para_X, para_Y, para_Z, total_X, total_Y, total_Z, ISO, ANISO])
        df_orbcon_sc = pd.DataFrame(data,columns=["MO", "DIAG_X", "DIAG_Y", "DIAG_Z", "PARA_X", "PARA_Y", "PARA_Z", "TOTAL_X", "TOTAL_Y", "TOTAL_Z", "ISO", "ANISO"] )
        df_orbcon_sc = df_orbcon_sc.set_index("MO")
        #print(df_orbcon_sc)

        # orb_pairs
        orbcon_pair_lines = lines[start_orbpair:end_orbpair]
        print(orbcon_pair_lines[0])
        data = np.zeros((n_orbs,n_orbs))
        #for line in orbcon_pair_lines:





read_outfile_orbpairs("Rh2_CSe_DMAD_CF3_dppm2.out")

