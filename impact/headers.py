
def get_t_header():
    #-----------------
    # ImpactT Header
    # lattice starts at line 10

    # Header dicts
    HNAMES={}
    HDEFAULTS = {}
    # Line 1
    HNAMES[1]  = ['Npcol', 'Nprow']
    HDEFAULTS[1] = [1,1]

    # Line 2
    HNAMES[2] = ['Dt', 'Ntstep', 'Nbunch']
    HDEFAULTS[2] = [0.0, 100000000, 1] # Dt must be set

    # Line 3
    HNAMES[3]    = ['Dim', 'Np', 'Flagmap', 'Flagerr', 'Flagdiag', 'Flagimg', 'Zimage']
    HDEFAULTS[3] = [999,   0,     1,        0,          2,         1,          0.02]

    # Line 4
    HNAMES[4] = ['Nx', 'Ny', 'Nz', 'Flagbc', 'Xrad', 'Yrad', 'Perdlen']
    HDEFAULTS[4] = [32, 32, 32, 1, 0.015, 0.015, 100.0]

    # Line 5
    HNAMES[5] = ['Flagdist', 'Rstartflg', 'Flagsbstp', 'Nemission', 'Temission']
    HDEFAULTS[5] = [16, 0, 0, 400, 1.4e-11]

    # Line 6-8
    HNAMES[6] = ['sigx(m)', 'sigpx', 'muxpx', 'xscale', 'pxscale', 'xmu1(m)', 'xmu2']
    HDEFAULTS[6] = [0.0 for i in range(len(HNAMES[6]))]
    HNAMES[7] = ['sigy(m)', 'sigpy', 'muxpy', 'yscale', 'pyscale', 'ymu1(m)', 'ymu2']
    HDEFAULTS[7] = [0.0 for i in range(len(HNAMES[7]))]
    HNAMES[8] = ['sigz(m)', 'sigpz', 'muxpz', 'zscale', 'pzscale', 'zmu1(m)', 'zmu2']
    HDEFAULTS[8] = [0.0 for i in range(len(HNAMES[8]))]

    # Line 9
    HNAMES[9] = ['Bcurr', 'Bkenergy', 'Bmass', 'Bcharge', 'Bfreq', 'Tini']
    HDEFAULTS[9] = [1.0, 1.0, 510998.946, -1.0, 2856000000.0, 0.0]

    return HNAMES, HDEFAULTS

def get_z_header():
    #-----------------
    # ImpactZ Header
    # lattice starts at line 12

    # Header dicts
    HNAMES={}
    HDEFAULTS = {}

    # Line 1
    HNAMES[1]  =  ['Npcol', 'Nprow']
    HDEFAULTS[1] = [1,  1]


    # Line 2
    HNAMES[2]    = ['Dim', 'Np', 'Flagmap', 'Flagerr', 'Flagoutput']
    HDEFAULTS[2] = [6,    10000,         1,         0,            1]

    # Line 3
    HNAMES[3]    = ['Nx', 'Ny', 'Nz', 'SCtype', 'Xrad', 'Yrad', 'Perdlen']
    HDEFAULTS[3] = [ 32,    32,   32,        1,  0.015,  0.015,     100.0]

    # Line 4
    HNAMES[4] = ['Flagdist', 'Rstartflg', 'Flagsbstp', 'Nchargestates']
    HDEFAULTS[4] = [     19,         0,             0,               1]

    # Line 5
    HNAMES[5] = ['NpartPerChargeState']
    HDEFAULTS[5] = [[10000]]

    # Line 6
    HNAMES[6] = ['CurrPerChargeState']
    HDEFAULTS[6] = [[0.04]]

    # Line 7
    HNAMES[7] = ['QdivmPerChargeState']
    HDEFAULTS[7] = [[1.0657886728e-09]]


    # Line 8-10 
    HNAMES[8] = ['alpha_x', 'beta_x', 'emit_x', 'mismatchx', 'mismatchpx', 'offsetX', 'offsetPx']
    HDEFAULTS[8] = [0.0] * len(HNAMES[8])
    HNAMES[9] = ['alpha_y', 'beta_y', 'emit_y', 'mismatchy', 'mismatchpy', 'offsetY', 'offsetPy']
    HDEFAULTS[9] = HDEFAULTS[6][:]
    HNAMES[10] = ['alpha_z', 'beta_z', 'emit_z', 'mismatchz', 'mismatchE', 'offsetPhase', 'offsetEnergy']
    HDEFAULTS[10] = HDEFAULTS[6][:]

    # Line 11
    HNAMES[11] = ['Bcurr', 'Bkenergy', 'Bmass', 'Bcharge', 'Bfreq', 'Phini']
    HDEFAULTS[11] = [0.04, 172359000.0, 938272310.0, 1.0, 6.5e8, 110.163]

    return HNAMES, gDEFAULTS
