                  November 2018
  
The LOWZ filters are taken from the Pantheon analysis,
   https://arxiv.org/abs/1710.00845
To access the transmission functions and BD17 reference mags,
download SNDATA_ROOT from
       http://snana.uchicago.edu
and read the instructions below.

Below is a table showing the file location of each passband
transmission, along with mag(BD17).
Each FILTPATH is a directory containing the transmission
files for a particular set of filters. "Each FILTER:" key
specifies information for a single filter passband.
Note that the last character in the nick-name is used in the
low-z data files in order to combine the multiple samples into
one LOWZ sample. For SNANA simulation and analysis, each filter
must have a unique character, and thus the 27 low-z filters
are mapped into a-z,A.

The last column has mag(BD17), which includes the originally published
mag plus an explicit PS1 Supercal Offset from
     https://arxiv.org/abs/1508.05361 .
The SNANA analysis software parses the +/- keys to perform the
SuperCal addition.

For SNANA analyses, the calibration files (KCOR_FILE argument)
are located here,
      $SNDATA_ROOT/kcor/DES/DES-SN3YR/LOWZ
      $SNDATA_ROOT/kcor/DES/DES-SN3YR/DECam

# Start filters for VERSION = PS1s_CFA3_4SHOOTER2_DS17
MAGSYSTEM:   BD17
FILTSYSTEM:  COUNT 
FILTPATH:    $SNDATA_ROOT/filters/PS1/PS1s_RS14/CFA3_native
#       nick-name        subDir under FILTPATH  mag(BD17)+Offset(SuperCal)
# -------------------------------------------------------------------------
FILTER:  CFA3S-U/a       SNLS3_4shooter2_U.dat  9.6930 
FILTER:  CFA3S-B/b       SNLS3_4shooter2_B.dat  9.87400-0.0345 
FILTER:  CFA3S-V/c       SNLS3_4shooter2_V.dat  9.47900-0.0087 
FILTER:  CFA3S-R/d       SNLS3_4shooter2_R.dat  9.15500-0.021 
FILTER:  CFA3S-I/e       SNLS3_4shooter2_I.dat  8.85100-0.0136 

# Start filters for VERSION = PS1s_CFA3_KEPLERCAM_DS17
MAGSYSTEM:   BD17
FILTSYSTEM:  COUNT
FILTPATH:    $SNDATA_ROOT/filters/PS1/PS1s_RS14/PS1_CFA4
FILTER:  CFA41-U/f       cfa4_U_p1.dat  9.724 
FILTER:  CFA41-B/g       cfa4_B_p1.dat  9.88605-0.024 
FILTER:  CFA41-V/h       cfa4_V_p1.dat  9.47432-0.0012 
FILTER:  CFA41-r/i       cfa4_r_p1.dat  9.35252+0.0025 
FILTER:  CFA41-i/j       cfa4_i_p1.dat  9.25465-0.004 

# Start filters for VERSION = PS1s_CFA4_p1_DS17
FILTER:  CFA41-U/k       cfa4_U_p1.dat  9.724 
FILTER:  CFA41-B/l       cfa4_B_p1.dat  9.88605-0.024 
FILTER:  CFA41-V/m       cfa4_V_p1.dat  9.47432-0.0012 
FILTER:  CFA41-r/n       cfa4_r_p1.dat  9.35252+0.0025 
FILTER:  CFA41-i/o       cfa4_i_p1.dat  9.25465-0.004 

# Start filters for VERSION = PS1s_CFA4_p2_DS17
FILTER:  CFA42-B/p       cfa4_B_p2.dat  9.86124+0.0027108700 
FILTER:  CFA42-V/q       cfa4_V_p2.dat  9.47432-0.0012322002 
FILTER:  CFA42-r/r       cfa4_r_p2.dat  9.35730+0.0058652098 
FILTER:  CFA42-i/s       cfa4_i_p2.dat  9.25521-0.0042374653 

# Start filters for VERSION = PS1s_CSPDR2_V_DS17
MAGSYSTEM:   BD17
FILTSYSTEM:  COUNT
FILTPATH:    $SNDATA_ROOT/filters/PS1/PS1s_RS14/CSP_Str11
FILTER:  CSP-u/t     u_texas_WLcorr_atm.txt  10.51952 
FILTER:  CSP-B/u     B_texas_WLcorr_atm.txt  9.87643-0.0082722800 
FILTER:  CSP-o/v     V_LC3009_texas_WLcorr_atm.txt  9.47663+0.0017663098 
FILTER:  CSP-m/w     V_LC3014_texas_WLcorr_atm.txt  9.47128+0.0017663098 
FILTER:  CSP-n/x     V_LC9844_texas_WLcorr_atm.txt  9.47748+0.0017663098 
FILTER:  CSP-g/y     g_texas_WLcorr_atm.txt  9.64406+0.0088273000 
FILTER:  CSP-r/z     r_texas_WLcorr_atm.txt  9.35160+0.0011820498 
FILTER:  CSP-i/A     i_texas_WLcorr_atm.txt  9.25000-0.016103720 
