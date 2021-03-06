import pySALESetup as pss

# create a Mesh instance, m
m = pss.Mesh(X=100,Y=500,cellsize=10.e-6)

# create a Grain instance with equivalent radius of 5 cells (eqr)
# no rotation (normally in radians)
# and circular shape. Other parameters are required for other shapes
g = pss.Grain(eqr=5.,rot=0.,shape='circle')
# create an ensemble instance to be populated
group = pss.Ensemble(m)
volume_fraction = 0.

"""
This is the normal procedure, however, quickFill now automatesit!
This is the n
This is the n# insert grains until target volume fraction achieved
This is the nwhile volume_fraction <= 0.4:
This is the n    # insert randomly into a specified region as material 1 for now
This is the n    g.insertRandomly(m,2,ybounds=[1.e-3,3.e-3],nooverlap=True)
This is the n    # add Grain instance to Ensemble
This is the n    group.add(g)
This is the n    # calculate the new volume fraction in the new region
    prev_vfrac = volume_fraction
    volume_fraction = m.vfrac(ybounds=[1.e-3,3.e-3])
"""
pss.quickFill(g,m,0.4,group,material=2,method='insertion',ybnds=[1.e-3,3.e-3],nooverlap=True)

# optimise materials using those not yet used
group.optimise_materials([3,4,5,6,7,8,9])

# create apparatus instances of the impactor and buffer plates
impactor = pss.Apparatus(xcoords=[0.,0.,1.e-3,1.e-3], ycoords=[3.e-3,5.e-3,5.e-3,3.e-3])
bufferplate = pss.Apparatus(xcoords=[0.,0.,1.e-3,1.e-3], ycoords=[0.,1.e-3,1.e-3,0.])
# place impactor into mesh m as material 2
impactor.place(m,1)
# use mesh class to assign impactor a vertical velocity of -500 m/s to impactor
m.matVel(-500.,1)
# place buffer into mesh m also as material 1
bufferplate.place(m,1)
# trims the top and bottom 10 cells from the sim
m.top_and_tail(10)

# view the mesh materials
m.viewMats(save=True)
# view the mesh velocities
m.viewVels(save=True)
# save the mesh as an input file for use with iSALE
#m.save()
