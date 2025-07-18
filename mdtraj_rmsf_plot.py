import matplotlib.pyplot as plt
import pandas as pd
#reads the mdtraj xvg output file
file=pd.read_csv('/Users/APren/rmsf_hex1.xvg', sep='\s', skiprows=4, names=['residue', 'rmsf'])

chains = []
current_chain=[]
#iteratively defines a new chain when the residue number = 1 and adds it to "chains" data
for i, row in file.iterrows():
    if row['residue'] == 1 and current_chain:
        chains.append(pd.DataFrame(current_chain))
        current_chain=[]
    current_chain.append(row)
#appends last chain information to the "chains" data
if current_chain:
    chains.append(pd.DataFrame(current_chain))

#plots the data by chain iteratively, coloring in the order of the HEX code colors below
colors = ['#ebd5e8','#debad8','#cc92c2','#C482b9','#b766aa','#a64e98','#8b417e','#6f3465','#53274c','#371a33']
for idx, chain in enumerate(chains):
    plt.plot(chain['residue'], chain['rmsf'],label=f'Chain {idx+1}', color=colors[idx % len(colors)])
plt.xlabel("Residue", fontfamily='arial', fontsize=12)
plt.ylabel("RMSF (nm)", fontfamily='arial', fontsize=12)
plt.title("Hexamer Rep1 RMSF by Chain", fontfamily='arial', fontsize=12)
plt.xlim(1, 42)
plt.ylim(0, 2.5)
plt.minorticks_on()
plt.legend(ncol=2)
plt.show()

