################ TESTS OF THE SNAPSHOTPOTENTIAL CLASS AND RELATED #############
import numpy
import pynbody
from galpy import potential
def test_snapshotKeplerPotential_eval():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s,num_threads=1)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    assert numpy.fabs(sp(1.,0.)-kp(1.,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp(0.5,0.)-kp(0.5,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp(1.,0.5)-kp(1.,0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp(1.,-0.5)-kp(1.,-0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    return None

def test_snapshotKeplerPotential_Rforce():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    assert numpy.fabs(sp.Rforce(1.,0.)-kp.Rforce(1.,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp.Rforce(0.5,0.)-kp.Rforce(0.5,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp.Rforce(1.,0.5)-kp.Rforce(1.,0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp.Rforce(1.,-0.5)-kp.Rforce(1.,-0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    return None

def test_snapshotKeplerPotential_zforce():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    assert numpy.fabs(sp.zforce(1.,0.)-kp.zforce(1.,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp.zforce(0.5,0.)-kp.zforce(0.5,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp.zforce(1.,0.5)-kp.zforce(1.,0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp.zforce(1.,-0.5)-kp.zforce(1.,-0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    return None

def test_snapshotKeplerPotential_hash():
    # Test that hashing the previous grid works
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    assert numpy.fabs(sp(1.,0.)-kp(1.,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    assert numpy.fabs(sp(1.,0.)-kp(1.,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    return None

def test_snapshotKeplerPotential_grid():
    # Test that evaluating on a grid works
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 2.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s)
    kp= potential.KeplerPotential(amp=2.) #should be the same
    rs= numpy.arange(3)+1
    zs= 0.1
    assert numpy.all(numpy.fabs(sp(rs,zs)-kp(rs,zs)) < 10.**-8.), 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    return None

def test_snapshotKeplerPotential_eval_array():
    # Test evaluating the snapshotPotential with array input
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    rs= numpy.ones(3)*0.5+0.5
    zs= (numpy.zeros(3)-1.)/2.
    assert numpy.all(numpy.fabs(sp(rs,zs)-kp(rs,zs)) < 10.**-8.), 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    return None

def test_snapshotKeplerPotential_Rforce_array():
    # Test evaluating the snapshotPotential with array input
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    rs= numpy.ones(3)*0.5+0.5
    zs= (numpy.zeros(3)-1.)/2.
    assert numpy.all(numpy.fabs(sp.Rforce(rs,zs)-kp.Rforce(rs,zs)) < 10.**-8.), 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    return None

def test_snapshotKeplerPotential_zforce_array():
    # Test evaluating the snapshotPotential with array input
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    rs= numpy.ones(3)*0.5+0.5
    zs= (numpy.zeros(3)-1.)/2.
    assert numpy.all(numpy.fabs(sp.zforce(rs,zs)-kp.zforce(rs,zs)) < 10.**-8.), 'SnapshotRZPotential with single unit mass does not correspond to KeplerPotential'
    return None

# Test that using different numbers of azimuths to average over gives the same result
def test_snapshotKeplerPotential_eval_naz():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s,num_threads=1)
    spaz= potential.SnapshotRZPotential(s,num_threads=1,nazimuths=12)
    assert numpy.fabs(sp(1.,0.)-spaz(1.,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp(0.5,0.)-spaz(0.5,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp(1.,0.5)-spaz(1.,0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp(1.,-0.5)-spaz(1.,-0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    return None

def test_snapshotKeplerPotential_Rforce_naz():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s,num_threads=1)
    spaz= potential.SnapshotRZPotential(s,num_threads=1,nazimuths=12)
    assert numpy.fabs(sp.Rforce(1.,0.)-spaz.Rforce(1.,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp.Rforce(0.5,0.)-spaz.Rforce(0.5,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp.Rforce(1.,0.5)-spaz.Rforce(1.,0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp.Rforce(1.,-0.5)-spaz.Rforce(1.,-0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    return None

def test_snapshotKeplerPotential_zforce_naz():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.SnapshotRZPotential(s,num_threads=1)
    spaz= potential.SnapshotRZPotential(s,num_threads=1,nazimuths=12)
    assert numpy.fabs(sp.zforce(1.,0.)-spaz.zforce(1.,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp.zforce(0.5,0.)-spaz.zforce(0.5,0.)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp.zforce(1.,0.5)-spaz.zforce(1.,0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    assert numpy.fabs(sp.zforce(1.,-0.5)-spaz.zforce(1.,-0.5)) < 10.**-8., 'SnapshotRZPotential with single unit mass for naz=4 does not agree with naz=12'
    return None

def test_interpsnapshotKeplerPotential_eval():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                            rgrid=(0.01,2.,201),
                                            zgrid=(0.,0.2,201),
                                            logR=False,
                                            interpPot=True,
                                            zsym=True,
                                            numcores=1)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    #This just tests on the grid
    rs= numpy.linspace(0.01,2.,21)
    zs= numpy.linspace(-0.2,0.2,41)
    for r in rs:
        for z in zs:
            assert numpy.fabs((sp(r,z)-kp(r,z))/kp(r,z)) < 10.**-10., 'RZPot interpolation w/ InterpSnapShotPotential of KeplerPotential fails at (R,z) = (%g,%g)' % (r,z)
    #This tests within the grid
    rs= numpy.linspace(0.01,2.,10)
    zs= numpy.linspace(-0.2,0.2,20)
    for r in rs:
        for z in zs:
            assert numpy.fabs((sp(r,z)-kp(r,z))/kp(r,z)) < 10.**-5., 'RZPot interpolation w/ InterpSnapShotPotential of KeplerPotential fails at (R,z) = (%g,%g) by %g' % (r,z,numpy.fabs((sp(r,z)-kp(r,z))/kp(r,z)))           
    #Test all at the same time to use vector evaluation
    mr,mz= numpy.meshgrid(rs,zs)
    mr= mr.flatten()
    mz= mz.flatten()
    assert numpy.all(numpy.fabs((sp(mr,mz)-kp(mr,mz))/kp(mr,mz)) < 10.**-5.), 'RZPot interpolation w/ interpRZPotential fails for vector input'
    return None

def test_interpsnapshotKeplerPotential_logR_eval():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                          rgrid=(numpy.log(0.01),numpy.log(20.),
                                                 251),
                                          logR=True,
                                          zgrid=(0.,0.2,201),
                                          interpPot=True,
                                          zsym=True)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    rs= numpy.linspace(0.02,16.,20)
    zs= numpy.linspace(-0.15,0.15,40)
    mr,mz= numpy.meshgrid(rs,zs)
    mr= mr.flatten()
    mz= mz.flatten()
    assert numpy.all(numpy.fabs((sp(mr,mz)-kp(mr,mz))/kp(mr,mz)) < 10.**-5.), 'RZPot interpolation w/ interpRZPotential fails for vector input, w/ logR at (R,z) = (%f,%f) by %g' % (mr[numpy.argmax(numpy.fabs((sp(mr,mz)-kp(mr,mz))/kp(mr,mz)))],mz[numpy.argmax(numpy.fabs((sp(mr,mz)-kp(mr,mz))/kp(mr,mz)))],numpy.amax(numpy.fabs((sp(mr,mz)-kp(mr,mz))/kp(mr,mz))))
    return None

def test_interpsnapshotKeplerPotential_noc_eval():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 1.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                          rgrid=(0.01,2.,201),
                                          zgrid=(0.,0.2,201),
                                          logR=False,
                                          interpPot=True,
                                          zsym=True,
                                          enable_c=False)
    kp= potential.KeplerPotential(amp=1.) #should be the same
    #Test all at the same time to use vector evaluation
    rs= numpy.linspace(0.01,2.,10)
    zs= numpy.linspace(-0.2,0.2,20)
    mr,mz= numpy.meshgrid(rs,zs)
    mr= mr.flatten()
    mz= mz.flatten()
    assert numpy.all(numpy.fabs((sp(mr,mz)-kp(mr,mz))/kp(mr,mz)) < 10.**-5.), 'RZPot interpolation w/ interpRZPotential fails for vector input, without enable_c'
    return None

def test_interpsnapshotKeplerPotential_normalize():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 4.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                            rgrid=(0.01,3.,201),
                                            zgrid=(0.,0.2,201),
                                            logR=False,
                                            interpPot=True,
                                            interpepifreq=True,
                                            interpverticalfreq=True,
                                            zsym=True)
    nkp= potential.KeplerPotential(normalize=1.) # normalized Kepler
    ukp= potential.KeplerPotential(amp=4.) # Un-normalized Kepler
    #Currently unnormalized
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-7., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp(1.,0.1)-ukp(1.,0.1)) < 10.**-7., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.epifreq(1.)-ukp.epifreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.verticalfreq(1.)-ukp.verticalfreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    # Normalize
    sp.normalize(R0=1.)
    assert numpy.fabs(sp.Rforce(1.,0.)+1.) < 10.**-7., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    assert numpy.fabs(sp(1.,0.1)-nkp(1.,0.1)) < 10.**-7., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.epifreq(1.)-nkp.epifreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.verticalfreq(1.)-nkp.verticalfreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    # De normalize
    sp.denormalize()
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-7., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    assert numpy.fabs(sp(1.,0.1)-ukp(1.,0.1)) < 10.**-7., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.epifreq(1.)-ukp.epifreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.verticalfreq(1.)-ukp.verticalfreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    # Also test when R0 =/= 1
    sp.normalize(R0=2.)
    assert numpy.fabs(sp.Rforce(1.,0.)+1.) < 10.**-7., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    assert numpy.fabs(sp(1.,0.1)-nkp(1.,0.1)) < 10.**-7., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.epifreq(1.)-nkp.epifreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.verticalfreq(1.)-nkp.verticalfreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    # De normalize
    sp.denormalize()
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-7., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    assert numpy.fabs(sp(1.,0.1)-ukp(1.,0.1)) < 10.**-7., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.epifreq(1.)-ukp.epifreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    assert numpy.fabs(sp.verticalfreq(1.)-ukp.verticalfreq(1.)) < 10.**-4., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    return None

def test_interpsnapshotKeplerPotential_noc_normalize():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 4.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                          rgrid=(numpy.log(0.01),numpy.log(3.),201),
                                          zgrid=(0.,0.2,201),
                                          logR=True,
                                          interpPot=True,
                                          enable_c=False,
                                          zsym=True)
    #Currently unnormalized
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-6., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    # Normalize
    sp.normalize(R0=1.)
    assert numpy.fabs(sp.Rforce(1.,0.)+1.) < 10.**-6., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    # De normalize
    sp.denormalize()
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-6., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    # Also test when R0 =/= 1
    sp.normalize(R0=2.)
    assert numpy.fabs(sp.Rforce(1.,0.)+1.) < 10.**-6., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    # De normalize
    sp.denormalize()
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-6., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    return None

def test_interpsnapshotKeplerPotential_normalize_units():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 4.
    s['eps']= 0.
    s['pos'].units= 'kpc'
    s['vel'].units= 'km s**-1'
    sp= potential.InterpSnapshotRZPotential(s,
                                          rgrid=(0.01,3.,201),
                                          zgrid=(0.,0.2,201),
                                          logR=False,
                                          interpPot=True,
                                          zsym=True)
    #Currently unnormalized
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-7., "InterpSnapShotPotential that is assumed to be unnormalized doesn't behave as expected"
    # Normalize
    sp.normalize(R0=1.)
    assert numpy.fabs(sp.Rforce(1.,0.)+1.) < 10.**-7., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    # De normalize
    sp.denormalize()
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-7., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    # Also test when R0 =/= 1
    sp.normalize(R0=2.)
    assert numpy.fabs(sp.Rforce(1.,0.)+1.) < 10.**-7., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    # De normalize
    sp.denormalize()
    assert numpy.fabs(sp.Rforce(1.,0.)+4.) < 10.**-7., "InterpSnapShotPotential that is assumed to be normalized doesn't behave as expected"
    return None

def test_interpsnapshotKeplerPotential_epifreq():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 2.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                            rgrid=(0.01,2.,101),
                                            zgrid=(0.,0.2,101),
                                            logR=False,
                                            interpPot=True,
                                            interpepifreq=True,
                                            zsym=True)
    kp= potential.KeplerPotential(normalize=2.) #should be the same
    #This just tests on the grid
    rs= numpy.linspace(0.01,2.,21)[1:]
    for r in rs:
        assert numpy.fabs((sp.epifreq(r)-kp.epifreq(r))/kp.epifreq(r)) < 10.**-4., 'RZPot interpolation of epifreq w/ InterpSnapShotPotential of KeplerPotential fails at R = %g by %g' % (r,numpy.fabs((sp.epifreq(r)-kp.epifreq(r))/kp.epifreq(r)))
    #This tests within the grid
    rs= numpy.linspace(0.01,2.,10)[1:]
    for r in rs:
        assert numpy.fabs((sp.epifreq(r)-kp.epifreq(r))/kp.epifreq(r)) < 10.**-4., 'RZPot interpolation of epifreq w/ InterpSnapShotPotential of KeplerPotential fails at R = %g by %g' % (r,numpy.fabs((sp.epifreq(r)-kp.epifreq(r))/kp.epifreq(r)))
    return None

def test_interpsnapshotKeplerPotential_verticalfreq():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 2.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                            rgrid=(0.01,2.,101),
                                            zgrid=(0.,0.2,101),
                                            logR=False,
                                            interpPot=True,
                                            interpverticalfreq=True,
                                            zsym=True)
    kp= potential.KeplerPotential(normalize=2.) #should be the same
    #This just tests on the grid
    rs= numpy.linspace(0.01,2.,21)[1:]
    for r in rs:
        assert numpy.fabs((sp.verticalfreq(r)-kp.verticalfreq(r))/kp.verticalfreq(r)) < 10.**-4., 'RZPot interpolation of verticalfreq w/ InterpSnapShotPotential of KeplerPotential fails at R = %g by %g' % (r,numpy.fabs((sp.verticalfreq(r)-kp.verticalfreq(r))/kp.verticalfreq(r)))
    #This tests within the grid
    rs= numpy.linspace(0.01,2.,10)[1:]
    for r in rs:
        assert numpy.fabs((sp.verticalfreq(r)-kp.verticalfreq(r))/kp.verticalfreq(r)) < 10.**-4., 'RZPot interpolation of verticalfreq w/ InterpSnapShotPotential of KeplerPotential fails at R = %g by %g' % (r,numpy.fabs((sp.verticalfreq(r)-kp.verticalfreq(r))/kp.verticalfreq(r)))
    return None

def test_interpsnapshotKeplerPotential_R2deriv():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 2.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                            rgrid=(0.01,2.,101),
                                            zgrid=(0.,0.2,101),
                                            logR=False,
                                            interpPot=True,
                                            interpepifreq=True,
                                            zsym=True)
    kp= potential.KeplerPotential(amp=2.) #should be the same
    #This just tests on the grid
    rs= numpy.linspace(0.01,2.,21)[1:]
    zs= numpy.linspace(-0.2,0.2,41)
    for r in rs:
        for z in zs:
            assert numpy.fabs((sp.R2deriv(r,z)-kp.R2deriv(r,z))/kp.R2deriv(r,z)) < 10.**-4., 'RZPot interpolation of R2deriv w/ InterpSnapShotPotential of KeplerPotential fails at (R,z) = (%g,%g) by %g' % (r,z,numpy.fabs((sp.R2deriv(r,z)-kp.R2deriv(r,z))/kp.R2deriv(r,z)))
    #This tests within the grid
    rs= numpy.linspace(0.01,2.,10)[1:]
    zs= numpy.linspace(-0.2,0.2,20)
    for r in rs:
        for z in zs:
            assert numpy.fabs((sp.R2deriv(r,z)-kp.R2deriv(r,z))/kp.R2deriv(r,z)) < 10.**-4., 'RZPot interpolation of R2deriv w/ InterpSnapShotPotential of KeplerPotential fails at (R,z) = (%g,%g) by %g' % (r,z,numpy.fabs((sp.R2deriv(r,z)-kp.R2deriv(r,z))/kp.R2deriv(r,z)))
    return None

def test_interpsnapshotKeplerPotential_z2deriv():
    # Set up a snapshot with just one unit mass at the origin
    s= pynbody.new(star=1)
    s['mass']= 2.
    s['eps']= 0.
    sp= potential.InterpSnapshotRZPotential(s,
                                            rgrid=(0.01,2.,101),
                                            zgrid=(0.,0.2,101),
                                            logR=False,
                                            interpPot=True,
                                            interpverticalfreq=True,
                                            zsym=True)
    kp= potential.KeplerPotential(amp=2.) #should be the same
    #This just tests on the grid
    rs= numpy.linspace(0.01,2.,21)[1:]
    zs= numpy.linspace(-0.2,0.2,41)
    for r in rs:
        for z in zs:
            assert numpy.fabs((sp.z2deriv(r,z)-kp.z2deriv(r,z))/kp.z2deriv(r,z)) < 10.**-4., 'RZPot interpolation of z2deriv w/ InterpSnapShotPotential of KeplerPotential fails at (R,z) = (%g,%g) by %g' % (r,z,numpy.fabs((sp.z2deriv(r,z)-kp.z2deriv(r,z))/kp.z2deriv(r,z)))
    #This tests within the grid
    rs= numpy.linspace(0.01,2.,10)[1:]
    zs= numpy.linspace(-0.2,0.2,20)
    for r in rs:
        for z in zs:
            assert numpy.fabs((sp.z2deriv(r,z)-kp.z2deriv(r,z))/kp.z2deriv(r,z)) < 2.*10.**-4., 'RZPot interpolation of z2deriv w/ InterpSnapShotPotential of KeplerPotential fails at (R,z) = (%g,%g) by %g' % (r,z,numpy.fabs((sp.z2deriv(r,z)-kp.z2deriv(r,z))/kp.z2deriv(r,z)))
    return None

def test_snapshotrzpotential_nopynbody():
    # Test that if we cannot load pynbody, we get an ImportError
    from galpy.potential_src import SnapshotRZPotential
    SnapshotRZPotential._PYNBODY_LOADED= False
    try:
        sp= potential.SnapshotRZPotential(1.) #1. doesn't matter
    except ImportError: pass
    else:
        raise AssertionError("SnapshotRZPotential w/o pynbody should have raised an error, but didn't")
    return None

def test_interpsnapshotrzpotential_nopynbody():
    # Test that if we cannot load pynbody, we get an ImportError
    from galpy.potential_src import SnapshotRZPotential
    SnapshotRZPotential._PYNBODY_LOADED= False
    try:
        sp= potential.InterpSnapshotRZPotential(1.) #1. doesn't matter
    except ImportError: pass
    else:
        raise AssertionError("InterpSnapshotRZPotential w/o pynbody should have raised an error, but didn't")
    return None
