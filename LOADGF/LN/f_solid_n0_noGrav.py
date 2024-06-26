# *********************************************************************
# FUNCTION TO PROPAGATE Y-SOLUTIONS THROUGH A SOLID LAYER (n=0)
# SPECIAL CASE OF NO GRAVITY
#
# Copyright (c) 2014-2019: HILARY R. MARTENS, LUIS RIVERA, MARK SIMONS         
#
# This file is part of LoadDef.
#
#    LoadDef is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    LoadDef is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with LoadDef.  If not, see <https://www.gnu.org/licenses/>.
#
# *********************************************************************

import numpy as np
from scipy import interpolate

def main(si,Y,tck_lnd,tck_mnd,tck_rnd,tck_gnd,wnd,ond,piG):

    # Interpolate Parameters at Current Radius
    lndi = interpolate.splev(si,tck_lnd,der=0)
    mndi = interpolate.splev(si,tck_mnd,der=0)
    rndi = interpolate.splev(si,tck_rnd,der=0)
    gndi = interpolate.splev(si,tck_gnd,der=0)

    # Compute Beta and Delta Parameters
    bndi = 1./(lndi + 2.*mndi)
    dndi = 2.*mndi*(3.*lndi + 2.*mndi)*bndi

    # Build A Matrix (where dY/dr = A Y)
    # Smylie (2013)
    c11 = -2.*lndi*bndi/si
    c12 = bndi

    c21 = 2.*dndi/(si**2) - rndi*(wnd**2)
    c22 = -4.*mndi*bndi/si

    # Matrix of Parameters
    A = np.array([[c11, c12], \
        [c21, c22]])

    # Compute dY/dr
    YP = np.dot(A,Y)

    # Return Updated Derivatives
    return YP

