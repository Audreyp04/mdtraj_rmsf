import mdtraj as md
import numpy as np

#loading in the trajectory with topology information
traj=md.load('/Users/APren/Desktop/BEL/AB/panc/hex/rep1/pbc_analysis/hex1_cluster.pdb','/Users/APren/Desktop/BEL/AB/panc/hex/rep1/pbc_analysis/cat_clus_pbc.xtc')
#calculating the rmsf of the trajectory
total_rmsf = md.rmsf(traj, traj)
#name the output
outname="rmsf_hex1.xvg"
#define the format for writing the data to a file
fmt_string='%.6f'
#set space as the delimiter
delim=' '

#add header to the file output
header=[
    '# RMSF as calculated by as MDTraj Python package',
    '# title "RMSF Plot"',
    '# xaxis label "Time (ps)"',
    '# yaxis label "RMSF"',
]

#convert RMSF by atom into by residue rmsf
resi_rmsf=[]
for residue in traj.topology.residues:
    atom_indices=[atom.index for atom in residue.atoms]
    resi_rmsf_values=total_rmsf[atom_indices]
    resi_rmsf.append(np.mean(resi_rmsf_values))

#adding residue numbers to an 'x' column
c=6 #number of chains
x_num=np.arange(1,43)
x_values=np.concatenate(([x_num])*c, axis=0)
final_array=np.column_stack((x_values, resi_rmsf))

#open the file in write mode and write in header
with open(outname, 'w') as f:
    for line in header:
        f.write(line+'\n')
    np.savetxt(f, final_array, fmt=fmt_string, delimiter=delim)