#!/usr/bin/env python3
# Automatically generated file. 
# Format:    Python script code
# McStas <http://www.mcstas.org>
# Instrument: Ni_TAS.instr (Ni_TAS)
# Date:       Wed Sep  6 07:18:55 2023
# File:       Ni_TAS_generated.py

import mcstasscript as ms

# Python McStas instrument description
instr = ms.McStas_instr("Ni_TAS_generated", author = "McCode Py-Generator", origin = "ESS DMSC")

# Add collected DEPENDENCY strings
instr.set_dependency(' -I@MCCODE_LIB@/share/ -DFUNNEL ')

# *****************************************************************************
# * Start of instrument 'Ni_TAS' generated code
# *****************************************************************************
# MCSTAS system dir is "/Users/pkwi/McStas/mcstas/3.x-dev/"


# *****************************************************************************
# * instrument 'Ni_TAS' and components DECLARE
# *****************************************************************************

# Instrument parameters:

EI = instr.add_parameter('double', 'EI', value=40, comment='Parameter type (double) added by McCode py-generator')
EF = instr.add_parameter('double', 'EF', value=40, comment='Parameter type (double) added by McCode py-generator')
QHK = instr.add_parameter('double', 'QHK', value=1, comment='Parameter type (double) added by McCode py-generator')
QL = instr.add_parameter('double', 'QL', value=1, comment='Parameter type (double) added by McCode py-generator')
Temperature_K = instr.add_parameter('double', 'Temperature_K', value=70, comment='Parameter type (double) added by McCode py-generator')

component_definition_metadata = {
}
instr.append_declare(r'''
// Hardcoded variables
double KI=0;
double KF=0;
double QH; // Need to be set to QHK in initialize;
double QK;
double EN=0, QM=0, KFIX=0, FX=0;
double L1=9, L2=2.1, L3=1.5, L4=0.7;
double SM=1, SS=-1, SA=1;
double DM=3.3539, DA=3.3539;
double RMV=-1, RMH=0, RAV=0, RAH=-1;
double ETAM=30, ETAA=30;
double ALF1=60, ALF2=60, ALF3=60, ALF4=60;
double BET1=120, BET2=120, BET3=120, BET4=120;
//double BET1=120, BET2=60, BET3=60, BET4=120;
double AS=3.5238, BS=3.5238, CS=3.5238;
double AA=90, BB=90, CC=90;
double AX=1, AY=1, AZ=0;
double BX=0, BY=0, BZ=1;
double verbose=1;
double A1=0,A2=0,A3=0,A4=0,A5=0,A6=0;
double NHM=1, NVM=9, WM=0.10, HM=0.12;
double NHA=9, NVA=1, WA=0.10, HA=0.12;
double radius=0.012, thickness=0.005, height=0.05;


  struct sample_struct {
    double as, bs, cs;
    double aa, bb, cc;
    double ax, ay, az;
    double bx, by, bz;
  } sample;

  struct machine_hkl_struct {
    double dm, da;
    double l1, l2, l3, l4;
    double sm, ss, sa;
    double etam, etaa, kfix, fx;
    double alf1, alf2, alf3, alf4;
    double bet1, bet2, bet3, bet4;
    double ki, kf, ei, ef;
    double qh, qk, ql, en;
  } machine_hkl;

  struct machine_real_struct {
    double a1,a2,a3,a4,a5,a6;
    double rmh, rmv, rah, rav;
    double qm, qs, qt[3];
    char   message[256];
  } machine_real;

  struct machine_real_struct qhkl2angles(
    struct sample_struct      sample,
    struct machine_hkl_struct machine_hkl,
    struct machine_real_struct machine_real) {

      /* code from TASMAD/t_rlp.F:SETRLP */
      double qhkl[3];
      double alpha[3];
      double a[3];
      double aspv[3][2];
      double cosa[3], sina[3];
      double cosb[3], sinb[3];
      double b[3], c[3], s[4][4];
      double vv[3][3], bb[3][3];
      double arg, cc;
      int i,j,k,l,m,n;
      char liquid_case=1;
      /* transfer parameters to local arrays */
      qhkl[0]   = machine_hkl.qh; /* HKL target */
      qhkl[1]   = machine_hkl.qk;
      qhkl[2]   = machine_hkl.ql;
      alpha[0]  = sample.aa; /* cell angles */
      alpha[1]  = sample.bb;
      alpha[2]  = sample.cc;
      a[0]      = sample.as; /* cell parameters */
      a[1]      = sample.bs;
      a[2]      = sample.cs;
      aspv[0][0]= sample.ax; /* cell axis A */
      aspv[1][0]= sample.ay;
      aspv[2][0]= sample.az;
      aspv[0][1]= sample.bx; /* cell axis B */
      aspv[1][1]= sample.by;
      aspv[2][1]= sample.bz;

      /* default return values */
      strcpy(machine_real.message, "");
      machine_real.a3 = machine_real.a4 = 0;
      machine_real.a1 = machine_real.a5 = 0;

      /* if using HKL positioning in crystal (QM = 0) */
      if (machine_real.qm <= 0) {
        liquid_case = 0;
        /* compute reciprocal cell */
        for (i=0; i< 3; i++)
          if (a[i] <=0) sprintf(machine_real.message, "Lattice parameters a[%i]=%g", i, a[i]);
          else {
            a[i]    /= 2*PI;
            alpha[i]*= DEG2RAD;
            cosa[i]  = cos(alpha[i]);
            sina[i]  = sin(alpha[i]);
          }
        cc = cosa[0]*cosa[0]+cosa[1]*cosa[1]+cosa[2]*cosa[2]; /* norm */
        cc = 1 + 2*cosa[0]*cosa[1]*cosa[2] - cc;
        if (cc <= 0) sprintf(machine_real.message, "Lattice angles (AA,BB,CC) cc=%g", cc);
        else cc = sqrt(cc);

        if (strlen(machine_real.message)) return machine_real;

        /* compute bb */
        j=1; k=2;
        for (i=0; i<3; i++) {
          b[i] = sina[i]/(a[i]*cc);
          cosb[i] = (cosa[j]*cosa[k] - cosa[i])/(sina[j]*sina[k]);
          sinb[i] = sqrt(1 - cosb[i]*cosb[i]);
          j=k; k=i;
        }

        bb[0][0] = b[0];
        bb[1][0] = 0;
        bb[2][0] = 0;
        bb[0][1] = b[1]*cosb[2];
        bb[1][1] = b[1]*sinb[2];
        bb[2][1] = 0;
        bb[0][2] = b[2]*cosb[1];
        bb[1][2] =-b[2]*sinb[1]*cosa[0];
        bb[2][2] = 1/a[2];

        /* compute vv */
        for (k=0; k< 3; k++)
          for (i=0; i< 3; i++) vv[k][i] = 0;

        for (k=0; k< 2; k++)
          for (i=0; i< 3; i++)
            for (j=0; j< 3; j++)
              vv[k][i] += bb[i][j]*aspv[j][k];

        for (m=2; m>=1; m--)
          for (n=0; n<3; n++) {
            i = (int)fmod(m+1,3); j= (int)fmod(m+2,3);
            k = (int)fmod(n+1,3); l= (int)fmod(n+2,3);
            vv[m][n]=vv[i][k]*vv[j][l]-vv[i][l]*vv[j][k];
          }

        for (i=0; i< 3; i++) { /* compute norm(vv) */
          c[i]=0;
          for (j=0; j< 3; j++)
            c[i] += vv[i][j]*vv[i][j];
          if (c[i]>0) c[i] =  sqrt(c[i]);
          else {
            sprintf(machine_real.message, "Vectors A and B, c[%i]=%g", i, c[i]);
            return machine_real;
          }
        }

        for (i=0; i< 3; i++) /* normalize vv */
          for (j=0; j< 3; j++)
            vv[j][i] /= c[j];

        for (i=0; i< 3; i++) /* compute S */
          for (j=0; j< 3; j++) {
            s[i][j] = 0;
            for (k=0; k< 3; k++)
              s[i][j] += vv[i][k]*bb[k][j];
          }
        s[3][3]=1;
        for (i=0;  i< 3;  i++)  s[3][i]=s[i][3]=0;

        /* compute q modulus and transverse component */
        machine_real.qs = 0;
        for (i=0; i< 3; i++) {
          machine_real.qt[i] = 0;
          for (j=0; j< 3; j++) machine_real.qt[i] += qhkl[j]*s[i][j];
          machine_real.qs += machine_real.qt[i]*machine_real.qt[i];
        }
        if (machine_real.qs > 0) machine_real.qm = sqrt(machine_real.qs);
        else sprintf(machine_real.message, "Q modulus too small QM^2=%g", machine_real.qs);
      } else {
        machine_real.qs = machine_real.qm*machine_real.qm;
      }
      /* end if  qm <= 0 ********************************************* */

      /* positioning of monochromator and analyser */
      arg = PI/machine_hkl.dm/machine_hkl.ki;
      if (fabs(arg > 1))
        sprintf(machine_real.message, "Monochromator can not reach this KI. arg=%g", arg);
      else {
        if (machine_hkl.dm <= 0 || machine_hkl.ki <= 0)
          strcpy(machine_real.message, "Monochromator DM=0 or KI=0.");
        else
          machine_real.a1 = asin(arg)*RAD2DEG;
        machine_real.a1 *= machine_hkl.sm;
      }
      machine_real.a2=2*machine_real.a1;

      arg = PI/machine_hkl.da/machine_hkl.kf;
      if (fabs(arg > 1))
        sprintf(machine_real.message, "Analyzer can not reach this KF. arg=%g",arg);
      else {
        if (machine_hkl.da <= 0 || machine_hkl.kf <= 0)
          strcpy(machine_real.message, "Analyzer DA=0 or KF=0.");
        else
          machine_real.a5 = asin(arg)*RAD2DEG;
        machine_real.a5 *= machine_hkl.sa;
      }
      machine_real.a6=2*machine_real.a5;
      if (strlen(machine_real.message)) return machine_real;


      /* code from TASMAD/t_conv.F:SAM_CASE */
      arg = (machine_hkl.ki*machine_hkl.ki + machine_hkl.kf*machine_hkl.kf - machine_real.qs)
          / (2*machine_hkl.ki*machine_hkl.kf);
      if (fabs(arg) < 1)
        machine_real.a4 = RAD2DEG*acos(arg);
      else
        sprintf(machine_real.message, "Q modulus too big. Can not close triangle. arg=%g", arg);
      machine_real.a4 *= machine_hkl.ss;

      if (!liquid_case) { /* compute a3 in crystals */
        machine_real.a3 =
            -atan2(machine_real.qt[1],machine_real.qt[0])
            -acos( (machine_hkl.kf*machine_hkl.kf-machine_real.qs-machine_hkl.ki*machine_hkl.ki)
                  /(-2*machine_real.qm*machine_hkl.ki) );
        machine_real.a3 *= RAD2DEG*(machine_real.a4 > 0 ? 1 : -1 );
    }

    return machine_real;
  } /* qhkl2angles */
''')


instr.append_initialize(r'''

QH=QHK;
QK=QHK;

double Vi, Vf;
char   anglemode = 0;
printf("* Incoming beam: EI=%.4g [meV] KI=%.4g [Angs-1] Vi=%g [m/s]\n", EI, KI, Vi);
printf("* Outgoing beam: EF=%.4g [meV] KF=%.4g [Angs-1] Vf=%g [m/s]\n", EF, KF, Vf);

if (KFIX && FX) {
  if      (FX == 1) KI = KFIX;
  else if (FX == 2) KF = KFIX;
}

if (EI && EF && !EN)
  EN = EI - EF;

/* determine neutron energy from input */
if (KI && !EI) {
  Vi = K2V*fabs(KI);
  EI = VS2E*Vi*Vi;
}
if (KF && !EF) {
  Vf = K2V*fabs(KF);
  EF = VS2E*Vf*Vf;
}

machine_real.a1 = A1;
machine_real.a2 = A2;
machine_real.a3 = A3;
machine_real.a4 = A4;
machine_real.a5 = A5;
machine_real.a6 = A6;

printf("* Incoming beam: EI=%.4g [meV] KI=%.4g [Angs-1] Vi=%g [m/s]\n", EI, KI, Vi);
printf("* Outgoing beam: EF=%.4g [meV] KF=%.4g [Angs-1] Vf=%g [m/s]\n", EF, KF, Vf);

if (A1 || A2 || A3 || A4 || A5 || A6) anglemode=1;

if (!anglemode) {
  if (!EI && !EF)
      exit(fprintf(stderr,
        "Ni_TAS: ERROR: neutron beam energy is not defined (EI, EF, KI, KF)\n"));


  /* energy conservation */
  if (EI)
    EF = EI - EN;
  else if (EF)
    EI = EF + EN;

  /* determine remaining neutron energies */
  if (!KI && EI) {
    Vi = SE2V*sqrt(EI);
    KI = V2K*Vi;
  }
  if (!KF && EF) {
    Vf = SE2V*sqrt(EF);
    KF = V2K*Vf;
  }

  if (!QM && !QH && !QK && !QL)
    exit(fprintf(stderr,
      "Ni_TAS: ERROR: No Q transfer defined (QM, QH, QK, QL)\n"));
    
  
    
} else {
  /* compute KI, KF if angles are consistent */
  if (!KI && fabs(A2-2*A1) < 0.01) {
    KI  = PI/DM/fabs(sin(DEG2RAD*A1*SM));
  }
  if (!KF && fabs(A6-2*A5) < 0.01) {
    KF  = PI/DA/fabs(sin(DEG2RAD*A5*SA));
  }
  double qs=(KI*KI + KF*KF - cos(A4*DEG2RAD*SS)*(2*KI*KF));
  if (!QM && qs>=0) QM = sqrt(qs);
  else fprintf(stderr,
      "Ni_TAS: Warning: Can not compute Q-modulus from A4=%g [deg].\n",A4);
}

/* transfer sample parameters */
sample.aa = AA;
sample.bb = BB;
sample.cc = CC;
sample.as = AS;
sample.bs = BS;
sample.cs = CS;
sample.ax = AX;
sample.ay = AY;
sample.az = AZ;
sample.bx = BX;
sample.by = BY;
sample.bz = BZ;

/* transfer target parameters */
machine_hkl.ki = KI;
machine_hkl.kf = KF;
machine_hkl.ei = EI;
machine_hkl.ef = EF;
machine_hkl.qh = QH;
machine_hkl.qk = QK;
machine_hkl.ql = QL;
machine_hkl.en = EN;
machine_real.qm = QM;

if (verbose) {
  printf("Ni_TAS: Detailed TAS configuration\n");
  printf("* Incoming beam: EI=%.4g [meV] KI=%.4g [Angs-1] Vi=%g [m/s]\n", EI, KI, Vi);
  printf("* Outgoing beam: EF=%.4g [meV] KF=%.4g [Angs-1] Vf=%g [m/s]\n", EF, KF, Vf);
}

/* transfer machine parameters */
machine_hkl.l1 = L1;
machine_hkl.l2 = L2;
machine_hkl.l3 = L3;
machine_hkl.l4 = L4;
machine_hkl.sm = SM;
machine_hkl.ss = SS;
machine_hkl.sa = SA;
machine_hkl.dm = DM;
machine_hkl.da = DA;
machine_real.rmv= RMV;
machine_real.rmh= RMH;
machine_real.rav= RAV;
machine_real.rah= RAH;
machine_hkl.etam= ETAM;
machine_hkl.etaa= ETAA;
machine_hkl.alf1= ALF1;
machine_hkl.alf2= ALF2;
machine_hkl.alf3= ALF3;
machine_hkl.alf4= ALF4;
machine_hkl.bet1= BET1;
machine_hkl.bet2= BET2;
machine_hkl.bet3= BET3;
machine_hkl.bet4= BET4;

/* geometry tests w/r to collimator lengths */
if (machine_hkl.l1 <= 1)
  fprintf(stderr, "Ni_TAS: Warning: L1 too short. Min=1\n");

if (machine_hkl.l2 <= 0.35)
  exit(fprintf(stderr, "Ni_TAS: ERROR: L2 too short. Min=0.35\n"));

if (machine_hkl.l3 <= 0.40)
  exit(fprintf(stderr, "Ni_TAS: ERROR: L3 too short. Min=0.40\n"));

if (machine_hkl.l4 <= 0.24)
  exit(fprintf(stderr, "Ni_TAS: ERROR: L4 too short. Min=0.24\n"));

if (!anglemode) {
  machine_real = qhkl2angles(sample, machine_hkl, machine_real);
  if (strlen(machine_real.message))
    exit(fprintf(stderr, "Ni_TAS: ERROR: %s [qhkl2angles]\n", machine_real.message));
}

/* compute optimal curvatures */
double L;
L = 1/(1/L1+1/L2);
if (RMV < 0) machine_real.rmv = fabs(2*L*sin(DEG2RAD*machine_real.a1));
if (RMH < 0) machine_real.rmh = fabs(2*L/sin(DEG2RAD*machine_real.a1));
L = 1/(1/L3+1/L4);
if (RAV < 0) machine_real.rav = fabs(2*L*sin(DEG2RAD*machine_real.a5));
if (RAH < 0) machine_real.rah = fabs(2*L/sin(DEG2RAD*machine_real.a5));

if (verbose) {
  printf("* Transfer:     EN=%g [meV] QM=%g [Angs-1]\n", EN, machine_real.qm);
  printf("Angles: A1=%.4g A2=%.4g A3=%.4g A4=%.4g A5=%.4g A6=%.4g [deg]\n",
    machine_real.a1, machine_real.a2,
    machine_real.a3, machine_real.a4,
    machine_real.a5, machine_real.a6);
  printf("Monochromator: DM=%.4g [Angs] RMH=%.4g [m] RMV=%.4g [m] %s\n",
    machine_hkl.dm, machine_real.rmh, machine_real.rmv,
    (!machine_real.rmh && !machine_real.rmv ? "flat" : "curved"));
  printf("Analyzer:      DA=%.4g [Angs] RAH=%.4g [m] RAV=%.4g [m] %s\n",
    machine_hkl.da, machine_real.rah, machine_real.rav,
    (!machine_real.rah && !machine_real.rav ? "flat" : "curved"));
   
  /*
  printf("Sample:        ");
    if (strcmp(Sqw_coh, "NULL") && !strstr(Sqw_coh, ".laz") && !strstr(Sqw_coh, ".lau"))
      printf("Isotropic (liquid/polymer) %s\n", Sqw_coh);
    if (!strcmp(Sqw_coh, "NULL"))
      printf("Incoherent\n");
    if (strstr(Sqw_coh, ".laz") || strstr(Sqw_coh, ".lau"))
      printf("Powder %s\n", Sqw_coh);
   */
}

machine_real.rmv = fabs(machine_real.rmv)*machine_hkl.sm;
machine_real.rmh = fabs(machine_real.rmh)*machine_hkl.sm;
machine_real.rav = fabs(machine_real.rav)*machine_hkl.sa;
machine_real.rah = fabs(machine_real.rah)*machine_hkl.sa;

''')


uv_n_scattering_events = instr.add_user_var("int ", "n_scattering_events", comment="USERVAR added by McCode py-generator")
# *****************************************************************************
# * instrument 'Ni_TAS' TRACE
# *****************************************************************************

# Comp instance init, placement and parameters
init = instr.add_component('init','Union_init')


# Comp instance Ni_Incoherent, placement and parameters
Ni_Incoherent = instr.add_component('Ni_Incoherent','Incoherent_process')

Ni_Incoherent.sigma = '20.79999'
Ni_Incoherent.f_QE = '0'
Ni_Incoherent.gamma = '0'
Ni_Incoherent.packing_factor = '1'
Ni_Incoherent.unit_cell_volume = '43.75561'
Ni_Incoherent.interact_fraction = '0.2'
Ni_Incoherent.init = '"init"'

# Comp instance Ni_Phonon_L, placement and parameters
Ni_Phonon_L = instr.add_component('Ni_Phonon_L','PhononSimple_process', AT=['0', '0', '0'], ROTATED=['45', '0', '0'])

Ni_Phonon_L.packing_factor = '1'
Ni_Phonon_L.unit_cell_volume = '13.8'
Ni_Phonon_L.interact_fraction = '0.2'
Ni_Phonon_L.a = '3.52380'
Ni_Phonon_L.c = '33.8'
Ni_Phonon_L.M = '58.6934'
Ni_Phonon_L.b = '10.3'
Ni_Phonon_L.T = 'Temperature_K'
Ni_Phonon_L.DW = '1'
Ni_Phonon_L.longitudinal = '1'
Ni_Phonon_L.transverse = '0'
Ni_Phonon_L.init = '"init"'

# Comp instance Ni_Phonon_T, placement and parameters
Ni_Phonon_T = instr.add_component('Ni_Phonon_T','PhononSimple_process', AT=['0', '0', '0'], ROTATED=['45', '0', '0'])

Ni_Phonon_T.packing_factor = '1'
Ni_Phonon_T.unit_cell_volume = '13.8'
Ni_Phonon_T.interact_fraction = '0.2'
Ni_Phonon_T.a = '3.52380'
Ni_Phonon_T.c = '23.7'
Ni_Phonon_T.M = '58.6934'
Ni_Phonon_T.b = '10.3'
Ni_Phonon_T.T = 'Temperature_K'
Ni_Phonon_T.DW = '1'
Ni_Phonon_T.longitudinal = '0'
Ni_Phonon_T.transverse = '1'
Ni_Phonon_T.init = '"init"'

# Comp instance Ni_Single_crystal, placement and parameters
Ni_Single_crystal = instr.add_component('Ni_Single_crystal','Single_crystal_process', AT=['0', '0', '0'], ROTATED=['45', '0', '0'])

Ni_Single_crystal.reflections = '"Ni.lau"'
Ni_Single_crystal.delta_d_d = '1e-4'
Ni_Single_crystal.mosaic = '30'
Ni_Single_crystal.mosaic_a = '-1'
Ni_Single_crystal.mosaic_b = '-1'
Ni_Single_crystal.mosaic_c = '-1'
Ni_Single_crystal.mosaic_AB = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
Ni_Single_crystal.recip_cell = '0'
Ni_Single_crystal.barns = '0'
Ni_Single_crystal.ax = '3.52380'
Ni_Single_crystal.ay = '0'
Ni_Single_crystal.az = '0'
Ni_Single_crystal.bx = '0'
Ni_Single_crystal.by = '3.52380'
Ni_Single_crystal.bz = '0'
Ni_Single_crystal.cx = '0'
Ni_Single_crystal.cy = '0'
Ni_Single_crystal.cz = '3.52380'
Ni_Single_crystal.aa = '0'
Ni_Single_crystal.bb = '0'
Ni_Single_crystal.cc = '0'
Ni_Single_crystal.order = '0'
Ni_Single_crystal.RX = '0'
Ni_Single_crystal.RY = '0'
Ni_Single_crystal.RZ = '0'
Ni_Single_crystal.powder = '0'
Ni_Single_crystal.PG = '0'
Ni_Single_crystal.interact_fraction = '-1'
Ni_Single_crystal.packing_factor = '1'
Ni_Single_crystal.init = '"init"'

# Comp instance Ni, placement and parameters
Ni = instr.add_component('Ni','Union_make_material')

Ni.process_string = '"Ni_Incoherent,Ni_Phonon_L,Ni_Phonon_T,Ni_Single_crystal"'
Ni.my_absorption = '17.96000 * 100 / 43.75561'
Ni.absorber = '0'
Ni.init = '"init"'

# Comp instance Origin, placement and parameters
Origin = instr.add_component('Origin','Progress_bar')

Origin.profile = '"NULL"'
Origin.percent = '10'
Origin.flag_save = '0'
Origin.minutes = '0'

# Comp instance Source, placement and parameters
Source = instr.add_component('Source','Source_gen')

Source.flux_file = '"NULL"'
Source.xdiv_file = '"NULL"'
Source.ydiv_file = '"NULL"'
Source.radius = '0.10'
Source.dist = 'machine_hkl . l1'
Source.focus_xw = 'fabs ( WM * sin ( machine_real . a1 * DEG2RAD ) )'
Source.focus_yh = 'HM'
Source.focus_aw = '0'
Source.focus_ah = '0'
Source.E0 = 'machine_hkl . ei'
Source.dE = 'machine_hkl . ei * 0.03'
Source.lambda0 = '0'
Source.dlambda = '0'
Source.I1 = '0.5874e13'
Source.yheight = '0.1'
Source.xwidth = '0.1'
Source.verbose = '0'
Source.T1 = '683.7'
Source.flux_file_perAA = '0'
Source.flux_file_log = '0'
Source.Lmin = '0'
Source.Lmax = '0'
Source.Emin = '0'
Source.Emax = '0'
Source.T2 = '257.7'
Source.I2 = '2.5094e13'
Source.T3 = '16.7'
Source.I3 = '0.10343e13'
Source.zdepth = '0'
Source.target_index = '+ 1'

# Comp instance SC1, placement and parameters
SC1 = instr.add_component('SC1','Collimator_linear', AT=['0', '0', 'machine_hkl . l1 / 4'])
# WHEN ( ALF1 && BET1 ) at SC1
SC1.set_WHEN('( ALF1 && BET1 )')

SC1.xmin = '- WM / 2'
SC1.xmax = 'WM / 2'
SC1.ymin = '- HM / 2'
SC1.ymax = 'HM / 2'
SC1.xwidth = '0'
SC1.yheight = '0'
SC1.length = 'machine_hkl . l1 / 2'
SC1.divergence = 'ALF1'
SC1.transmission = '1'
SC1.divergenceV = 'BET1'

# Comp instance Guide_out, placement and parameters
Guide_out = instr.add_component('Guide_out','Arm', AT=['0', '0', 'machine_hkl . l1 -0.2'])


# Comp instance Mono_Cradle, placement and parameters
Mono_Cradle = instr.add_component('Mono_Cradle','Arm', AT=['0', '0', '0.2'], AT_RELATIVE='Guide_out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Guide_out')


# Comp instance PG1Xtal, placement and parameters
PG1Xtal = instr.add_component('PG1Xtal','Monochromator_curved', AT=['0', '0', '0'], AT_RELATIVE='Mono_Cradle', ROTATED=['0', 'machine_real . a1', '0'], ROTATED_RELATIVE='Mono_Cradle')

PG1Xtal.reflect = '( fabs ( machine_hkl . dm -3.355 ) < 0.2 ? "HOPG.rfl" : "" )'
PG1Xtal.transmit = '"NULL"'
PG1Xtal.zwidth = '0.01'
PG1Xtal.yheight = '0.01'
PG1Xtal.gap = '0.0005'
PG1Xtal.NH = 'NHM'
PG1Xtal.NV = 'NVM'
PG1Xtal.mosaich = 'machine_hkl . etam'
PG1Xtal.mosaicv = 'machine_hkl . etam'
PG1Xtal.r0 = '( fabs ( machine_hkl . dm -3.355 ) < 0.2 ? 1 : 0.7 )'
PG1Xtal.t0 = '1.0'
PG1Xtal.Q = '1.8734'
PG1Xtal.RV = 'machine_real . rmv'
PG1Xtal.RH = 'machine_real . rmh'
PG1Xtal.DM = 'machine_hkl . dm'
PG1Xtal.mosaic = '0'
PG1Xtal.width = 'WM'
PG1Xtal.height = 'HM'
PG1Xtal.verbose = '0'
PG1Xtal.order = '0'

# Comp instance Mono_Out, placement and parameters
Mono_Out = instr.add_component('Mono_Out','Arm', AT=['0', '0', '0'], AT_RELATIVE='Mono_Cradle', ROTATED=['0', 'machine_real . a2', '0'], ROTATED_RELATIVE='Mono_Cradle')


# Comp instance SC2, placement and parameters
SC2 = instr.add_component('SC2','Collimator_linear', AT=['0', '0', '( machine_hkl . l2 -0.35 ) / 2'], AT_RELATIVE='Mono_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Mono_Out')
# WHEN ( ALF2 && BET2 ) at SC2
SC2.set_WHEN('( ALF2 && BET2 )')

SC2.xmin = '-0.04 / 2'
SC2.xmax = '0.04 / 2'
SC2.ymin = '-0.07 / 2'
SC2.ymax = '0.07 / 2'
SC2.xwidth = '0'
SC2.yheight = '0'
SC2.length = '0.35'
SC2.divergence = 'ALF2'
SC2.transmission = '1'
SC2.divergenceV = 'BET2'

# Comp instance before_sample, placement and parameters
before_sample = instr.add_component('before_sample','Monitor_nD', AT=['0', '0', 'machine_hkl . l2'], AT_RELATIVE='Mono_Out', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='Mono_Out')

before_sample.user1 = '""'
before_sample.user2 = '""'
before_sample.user3 = '""'
before_sample.xwidth = '0.02'
before_sample.yheight = '0.02'
before_sample.zdepth = '0'
before_sample.xmin = '0'
before_sample.xmax = '0'
before_sample.ymin = '0'
before_sample.ymax = '0'
before_sample.zmin = '0'
before_sample.zmax = '0'
before_sample.bins = '0'
before_sample.min = '-1e40'
before_sample.max = '1e40'
before_sample.restore_neutron = '1'
before_sample.radius = '0'
before_sample.options = '"per cm2"'
before_sample.filename = '"before_sample.dat"'
before_sample.geometry = '"NULL"'
before_sample.nowritefile = '0'
before_sample.username1 = '"NULL"'
before_sample.username2 = '"NULL"'
before_sample.username3 = '"NULL"'

# Comp instance Sample_Cradle_2, placement and parameters
Sample_Cradle_2 = instr.add_component('Sample_Cradle_2','Arm', AT=['0', '0', '0'], AT_RELATIVE='before_sample', ROTATED=['0', 'machine_real . a3', '0'], ROTATED_RELATIVE='before_sample')


# Comp instance Sample, placement and parameters
Sample = instr.add_component('Sample','Union_cylinder', AT=['0', '0', '0'], AT_RELATIVE='Sample_Cradle_2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample_Cradle_2')

Sample.material_string = '"Ni"'
Sample.priority = '1'
Sample.radius = 'radius'
Sample.yheight = 'height'
Sample.visualize = '1'
Sample.target_index = '4'
Sample.target_x = '0'
Sample.target_y = '0'
Sample.target_z = '0'
Sample.focus_aw = '0'
Sample.focus_ah = '0'
Sample.focus_xw = '2 * WA'
Sample.focus_xh = 'HA'
Sample.focus_r = '0'
Sample.p_interact = '0'
Sample.mask_string = '0'
Sample.mask_setting = '0'
Sample.number_of_activations = '1'
Sample.init = '"init"'

# Comp instance Master, placement and parameters
Master = instr.add_component('Master','Union_master', AT=['0', '0', '0'], AT_RELATIVE='Sample_Cradle_2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample_Cradle_2')
# EXTEND at Master
Master.append_EXTEND(r'''
n_scattering_events = number_of_scattering_events;
''')



Master.verbal = '1'
Master.list_verbal = '0'
Master.finally_verbal = '0'
Master.allow_inside_start = '0'
Master.enable_tagging = '0'
Master.history_limit = '300000'
Master.enable_conditionals = '1'
Master.inherit_number_of_scattering_events = '0'
Master.init = '"init"'

# Comp instance Stop, placement and parameters
Stop = instr.add_component('Stop','Union_stop', AT=['0', '0', '0'], AT_RELATIVE='Sample_Cradle_2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample_Cradle_2')


# Comp instance Sample_Out, placement and parameters
Sample_Out = instr.add_component('Sample_Out','Arm', AT=['0', '0', '0'], AT_RELATIVE='before_sample', ROTATED=['0', 'machine_real . a4', '0'], ROTATED_RELATIVE='before_sample')


# Comp instance SC3, placement and parameters
SC3 = instr.add_component('SC3','Collimator_linear', AT=['0', '0', '( machine_hkl . l3 -0.40 ) / 2'], AT_RELATIVE='Sample_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample_Out')
# WHEN ( ALF3 && BET3 ) at SC3
SC3.set_WHEN('( ALF3 && BET3 )')

SC3.xmin = '-0.06 / 2'
SC3.xmax = '0.06 / 2'
SC3.ymin = '-0.12 / 2'
SC3.ymax = '0.12 / 2'
SC3.xwidth = '0'
SC3.yheight = '0'
SC3.length = '0.40'
SC3.divergence = 'ALF3'
SC3.transmission = '1'
SC3.divergenceV = 'BET3'

# Comp instance Ana_Cradle, placement and parameters
Ana_Cradle = instr.add_component('Ana_Cradle','Arm', AT=['0', '0', 'machine_hkl . l3'], AT_RELATIVE='Sample_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample_Out')


# Comp instance PG2Xtal, placement and parameters
PG2Xtal = instr.add_component('PG2Xtal','Monochromator_curved', AT=['0', '0', '0'], AT_RELATIVE='Ana_Cradle', ROTATED=['0', 'machine_real . a5', '0'], ROTATED_RELATIVE='Ana_Cradle')

PG2Xtal.reflect = '( fabs ( machine_hkl . dm -3.355 ) < 0.2 ? "HOPG.rfl" : "" )'
PG2Xtal.transmit = '"NULL"'
PG2Xtal.zwidth = '0.01'
PG2Xtal.yheight = '0.01'
PG2Xtal.gap = '0.0005'
PG2Xtal.NH = 'NHA'
PG2Xtal.NV = 'NVA'
PG2Xtal.mosaich = 'machine_hkl . etaa'
PG2Xtal.mosaicv = 'machine_hkl . etaa'
PG2Xtal.r0 = '( fabs ( machine_hkl . dm -3.355 ) < 0.2 ? 1 : 0.7 )'
PG2Xtal.t0 = '1.0'
PG2Xtal.Q = '1.8734'
PG2Xtal.RV = 'machine_real . rav'
PG2Xtal.RH = 'machine_real . rah'
PG2Xtal.DM = 'machine_hkl . da'
PG2Xtal.mosaic = '0'
PG2Xtal.width = 'WA'
PG2Xtal.height = 'HA'
PG2Xtal.verbose = '0'
PG2Xtal.order = '0'

# Comp instance Ana_Out, placement and parameters
Ana_Out = instr.add_component('Ana_Out','Arm', AT=['0', '0', '0'], AT_RELATIVE='Ana_Cradle', ROTATED=['0', 'machine_real . a6', '0'], ROTATED_RELATIVE='Ana_Cradle')


# Comp instance SC4, placement and parameters
SC4 = instr.add_component('SC4','Collimator_linear', AT=['0', '0', '( machine_hkl . l4 -0.24 ) / 2'], AT_RELATIVE='Ana_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Ana_Out')
# WHEN ( ALF4 && BET4 ) at SC4
SC4.set_WHEN('( ALF4 && BET4 )')

SC4.xmin = '-0.06 / 2'
SC4.xmax = '0.06 / 2'
SC4.ymin = '-0.12 / 2'
SC4.ymax = '0.12 / 2'
SC4.xwidth = '0'
SC4.yheight = '0'
SC4.length = '0.24'
SC4.divergence = 'ALF4'
SC4.transmission = '1'
SC4.divergenceV = 'BET4'

# Comp instance He3H, placement and parameters
He3H = instr.add_component('He3H','PSD_monitor', AT=['0', '0', 'machine_hkl . l4'], AT_RELATIVE='Ana_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Ana_Out')

He3H.nx = '20'
He3H.ny = '20'
He3H.filename = '"He3H.psd"'
He3H.xmin = '-0.025400'
He3H.xmax = '0.025400'
He3H.ymin = '-0.042850'
He3H.ymax = '0.042850'
He3H.xwidth = '0'
He3H.yheight = '0'
He3H.restore_neutron = '1'
He3H.nowritefile = '0'

# Comp instance Mono_shielding, placement and parameters
Mono_shielding = instr.add_component('Mono_shielding','Shape', AT=['0', '-0.3', '0'], AT_RELATIVE='PG1Xtal', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='Guide_out')

Mono_shielding.geometry = '0'
Mono_shielding.radius = '0.5'
Mono_shielding.xwidth = '0'
Mono_shielding.yheight = '1.4'
Mono_shielding.zdepth = '0'
Mono_shielding.thickness = '0'
Mono_shielding.center = '1'

# Comp instance Collimator_shelf, placement and parameters
Collimator_shelf = instr.add_component('Collimator_shelf','Shape', AT=['0', '0', '0.37 + ( ( machine_hkl . l2 -0.35 ) / 2 ) / 2'], AT_RELATIVE='Mono_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Mono_Out')

Collimator_shelf.geometry = '0'
Collimator_shelf.radius = '0'
Collimator_shelf.xwidth = '0.06'
Collimator_shelf.yheight = '0.08'
Collimator_shelf.zdepth = '( ( machine_hkl . l2 -0.35 ) / 2 )'
Collimator_shelf.thickness = '0'
Collimator_shelf.center = '1'

# Comp instance Collimator_shelf_2, placement and parameters
Collimator_shelf_2 = instr.add_component('Collimator_shelf_2','Shape', AT=['0', '-0.18', '0.37 + ( ( machine_hkl . l2 -0.35 ) / 2 ) / 2 -0.2'], AT_RELATIVE='Mono_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Mono_Out')

Collimator_shelf_2.geometry = '0'
Collimator_shelf_2.radius = '0'
Collimator_shelf_2.xwidth = '0.09'
Collimator_shelf_2.yheight = '0.45'
Collimator_shelf_2.zdepth = '( ( machine_hkl . l2 -0.35 ) / 2 ) * 0.5'
Collimator_shelf_2.thickness = '0'
Collimator_shelf_2.center = '1'

# Comp instance mono_connect, placement and parameters
mono_connect = instr.add_component('mono_connect','Shape', AT=['0', '-0.4', 'machine_hkl . l2 * 0.5 + 0.3'], AT_RELATIVE='Mono_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Mono_Out')

mono_connect.geometry = '0'
mono_connect.radius = '0'
mono_connect.xwidth = '0.20'
mono_connect.yheight = '0.03'
mono_connect.zdepth = 'machine_hkl . l2 -0.2'
mono_connect.thickness = '0'
mono_connect.center = '1'

# Comp instance Sample_table, placement and parameters
Sample_table = instr.add_component('Sample_table','Shape', AT=['0', '-0.06', '0'], AT_RELATIVE='Sample', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample')

Sample_table.geometry = '0'
Sample_table.radius = '0'
Sample_table.xwidth = '0.15'
Sample_table.yheight = '0.02'
Sample_table.zdepth = '0.15'
Sample_table.thickness = '0'
Sample_table.center = '1'

# Comp instance Sample_table_holder, placement and parameters
Sample_table_holder = instr.add_component('Sample_table_holder','Shape', AT=['0', '-0.155 + 0.02', '0'], AT_RELATIVE='Sample', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample')

Sample_table_holder.geometry = '0'
Sample_table_holder.radius = '0'
Sample_table_holder.xwidth = '0.06'
Sample_table_holder.yheight = '0.14'
Sample_table_holder.zdepth = '0.06'
Sample_table_holder.thickness = '0'
Sample_table_holder.center = '1'

# Comp instance Sample_table_holder_cylinder, placement and parameters
Sample_table_holder_cylinder = instr.add_component('Sample_table_holder_cylinder','Shape', AT=['0', '-1 + 0.80 * 0.5', '0'], AT_RELATIVE='Sample', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample')

Sample_table_holder_cylinder.geometry = '0'
Sample_table_holder_cylinder.radius = '0.1'
Sample_table_holder_cylinder.xwidth = '0'
Sample_table_holder_cylinder.yheight = '0.80'
Sample_table_holder_cylinder.zdepth = '0'
Sample_table_holder_cylinder.thickness = '0'
Sample_table_holder_cylinder.center = '1'

# Comp instance Sample_table_foot, placement and parameters
Sample_table_foot = instr.add_component('Sample_table_foot','Shape', AT=['0', '-0.98', '0'], AT_RELATIVE='Sample', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample')

Sample_table_foot.geometry = '0'
Sample_table_foot.radius = '0'
Sample_table_foot.xwidth = '0.5'
Sample_table_foot.yheight = '0.04'
Sample_table_foot.zdepth = '0.5'
Sample_table_foot.thickness = '0'
Sample_table_foot.center = '1'

# Comp instance Outer_cryostat_shell, placement and parameters
Outer_cryostat_shell = instr.add_component('Outer_cryostat_shell','Shape', AT=['0', '0', '0'], AT_RELATIVE='Sample', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample')

Outer_cryostat_shell.geometry = '0'
Outer_cryostat_shell.radius = '0.08'
Outer_cryostat_shell.xwidth = '0'
Outer_cryostat_shell.yheight = '0.11'
Outer_cryostat_shell.zdepth = '0'
Outer_cryostat_shell.thickness = '0'
Outer_cryostat_shell.center = '1'

# Comp instance Cryostat_drum, placement and parameters
Cryostat_drum = instr.add_component('Cryostat_drum','Shape', AT=['0', '0.11 * 0.5 + 0.5 * 0.5', '0'], AT_RELATIVE='Sample', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample')

Cryostat_drum.geometry = '0'
Cryostat_drum.radius = '0.2'
Cryostat_drum.xwidth = '0'
Cryostat_drum.yheight = '0.5'
Cryostat_drum.zdepth = '0'
Cryostat_drum.thickness = '0'
Cryostat_drum.center = '1'

# Comp instance center_volume, placement and parameters
center_volume = instr.add_component('center_volume','Shape', AT=['0', '-0.06 + 0.7 * 0.5 + 0.015', '0'], AT_RELATIVE='Sample', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample')

center_volume.geometry = '0'
center_volume.radius = '0.04'
center_volume.xwidth = '0'
center_volume.yheight = '0.7'
center_volume.zdepth = '0'
center_volume.thickness = '0'
center_volume.center = '1'

# Comp instance analyzer_connect, placement and parameters
analyzer_connect = instr.add_component('analyzer_connect','Shape', AT=['0', '-0.35', 'machine_hkl . l3 * 0.5 -0.15'], AT_RELATIVE='Sample_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample_Out')

analyzer_connect.geometry = '0'
analyzer_connect.radius = '0'
analyzer_connect.xwidth = '0.22'
analyzer_connect.yheight = '0.03'
analyzer_connect.zdepth = 'machine_hkl . l3'
analyzer_connect.thickness = '0'
analyzer_connect.center = '1'

# Comp instance analyzer_col_shelf, placement and parameters
analyzer_col_shelf = instr.add_component('analyzer_col_shelf','Shape', AT=['0', '-0.13', 'machine_hkl . l3 * 0.6'], AT_RELATIVE='Sample_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample_Out')

analyzer_col_shelf.geometry = '0'
analyzer_col_shelf.radius = '0'
analyzer_col_shelf.xwidth = '0.1'
analyzer_col_shelf.yheight = '0.4'
analyzer_col_shelf.zdepth = '0.8'
analyzer_col_shelf.thickness = '0'
analyzer_col_shelf.center = '1'

# Comp instance Analyzer_shielding, placement and parameters
Analyzer_shielding = instr.add_component('Analyzer_shielding','Shape', AT=['0', '-0.3', '0'], AT_RELATIVE='PG2Xtal', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='Guide_out')

Analyzer_shielding.geometry = '0'
Analyzer_shielding.radius = '0.25'
Analyzer_shielding.xwidth = '0'
Analyzer_shielding.yheight = '1.4'
Analyzer_shielding.zdepth = '0'
Analyzer_shielding.thickness = '0'
Analyzer_shielding.center = '1'

# Comp instance detector_connect, placement and parameters
detector_connect = instr.add_component('detector_connect','Shape', AT=['0', '-0.15', 'machine_hkl . l4 * 0.5 + 0.05'], AT_RELATIVE='Ana_Out', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Ana_Out')

detector_connect.geometry = '0'
detector_connect.radius = '0'
detector_connect.xwidth = '0.16'
detector_connect.yheight = '0.03'
detector_connect.zdepth = 'machine_hkl . l4 * 0.6'
detector_connect.thickness = '0'
detector_connect.center = '1'

# Comp instance detector_tank, placement and parameters
detector_tank = instr.add_component('detector_tank','Shape', AT=['0', '0', '0.05'], AT_RELATIVE='He3H', ROTATED=['90', '0', '0'], ROTATED_RELATIVE='He3H')

detector_tank.geometry = '0'
detector_tank.radius = '0.25'
detector_tank.xwidth = '0'
detector_tank.yheight = '0.3'
detector_tank.zdepth = '0'
detector_tank.thickness = '0'
detector_tank.center = '1'

# Comp instance detector_tank_stand_1, placement and parameters
detector_tank_stand_1 = instr.add_component('detector_tank_stand_1','Shape', AT=['0', '-1 + 0.8 * 0.5', '-0.05'], AT_RELATIVE='He3H', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='He3H')

detector_tank_stand_1.geometry = '0'
detector_tank_stand_1.radius = '0'
detector_tank_stand_1.xwidth = '0.02'
detector_tank_stand_1.yheight = '0.8'
detector_tank_stand_1.zdepth = '0.02'
detector_tank_stand_1.thickness = '0'
detector_tank_stand_1.center = '1'

# Comp instance detector_tank_stand_2, placement and parameters
detector_tank_stand_2 = instr.add_component('detector_tank_stand_2','Shape', AT=['0', '-1 + 0.8 * 0.5', '0.15'], AT_RELATIVE='He3H', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='He3H')

detector_tank_stand_2.geometry = '0'
detector_tank_stand_2.radius = '0'
detector_tank_stand_2.xwidth = '0.02'
detector_tank_stand_2.yheight = '0.8'
detector_tank_stand_2.zdepth = '0.02'
detector_tank_stand_2.thickness = '0'
detector_tank_stand_2.center = '1'

# Comp instance detector_tank_stand_foot, placement and parameters
detector_tank_stand_foot = instr.add_component('detector_tank_stand_foot','Shape', AT=['0', '-1 + 0.03 * 0.5', '0.05'], AT_RELATIVE='He3H', ROTATED=['0', '0', '0'], ROTATED_RELATIVE='He3H')

detector_tank_stand_foot.geometry = '0'
detector_tank_stand_foot.radius = '0'
detector_tank_stand_foot.xwidth = '0.4'
detector_tank_stand_foot.yheight = '0.03'
detector_tank_stand_foot.zdepth = '0.4'
detector_tank_stand_foot.thickness = '0'
detector_tank_stand_foot.center = '1'

# Instruct McStasscript not to 'check everythng'
instr.settings(checks=False)
# (also, this is where one can add e.g. seed=1000, ncount=1e7, mpi=8, openacc=True, force_compile=False etc.)


# Visualise with default parameters.
instr.show_instrument()


# Generate a dataset with default parameters.
data = instr.backengine()

# Overview plot:
ms.make_sub_plot(data)


# Other useful commands follow...

# One plot pr. window
#ms.make_plot(data)

# Load another dataset
#data2 = ms.load_data('some_other_folder')

# Adjusting a specific plot
#ms.name_plot_options("PSD_4PI", data, log=1, colormap="hot", orders_of_mag=5)


# Bring up the 'interface' - only relevant in Jupyter
#%matplotlib widget
#import mcstasscript.jb_interface as ms_widget
#ms_widget.show(data)


# Bring up the simulation 'interface' - only relevant in Jupyter
#%matplotlib widget
#import mcstasscript.jb_interface as ms_widget
#sim_widget = ms_widget.SimInterface(instr)
#sim_widget.show_interface()
#data = sim_widget.get_data()


# end of generated Python code Ni_TAS_generated.py 
