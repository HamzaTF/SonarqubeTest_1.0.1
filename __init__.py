from . import A5_ADD_BV, A5_ARM_BV, A5_ISC_APP138_BV, A5_REH_APP137_BV, A5_SUSP_MF_BV, A5_SUSP_Valtra_BV, A5_VRG_BV, A7_ISC_APP38_BV, A7_REH_APP37_BV, A7_VRG_BV, A11_TRANS_BV, A11V_BV, ADV_JOYSTICK_BV, Armrest_BV, Auto5_RHS_BV, BERGSTROM_BV, CLIM_PANEL_AUTO_BV, CLIM_PANEL_MANU_BV, CLUSTER_BV, DGW_BV, DYNA4_TR1_BV, DYNA4_TR2_BV, FRONT_LOADER_BV, IC1_C3_BV, IC2_BV, MULTIPAD_BV, NT03_BV, SANT03_BV, SRC14_34IO_BV, SRC14_34M_BV, SRC14_34V_BV, SRC14_H2_S3_M1_21_BV, SRC14_S2_BV, SRCIO_BV, SRCM_BV, SRCV_BV
from enum import Enum, IntEnum


def get_odx_version():
    return '2021-03-26'


def default_verbund_path():
    return r''


class IPAdressRelay(Enum):
    relay_1 = "192.168.0.21"
    relay_2 = "192.168.0.22"
    relay_3 = "192.168.0.24"
    relay_4 = "192.168.0.25"
    relay_5 = "192.168.0.26"


class GenerallyRelay(IntEnum):
    KL15_all_ECUs = 38
    KL30_all_ECUs = 37
    OBD_power = 27


class ECUs(Enum):
    A5_ADD = A5_ADD_BV.A5_ADDClient
    A5_ARM = A5_ARM_BV.A5_ARMClient
    A5_ISC_APP138 = A5_ISC_APP138_BV.A5_ISC_APP138Client
    A5_DYNA4_APP167 = A5_ISC_APP138_BV.A5_DYNA4_APP167Client
    A5_DYNA4_APP168 = A5_ISC_APP138_BV.A5_DYNA4_APP168Client
    A5_DYNA6_APP177 = A5_ISC_APP138_BV.A5_DYNA6_APP177Client
    A5_DYNA6_APP178 = A5_ISC_APP138_BV.A5_DYNA6_APP178Client
    A5_REH_APP137 = A5_REH_APP137_BV.A5_REH_APP137Client
    A5_SUSP_MF = A5_SUSP_MF_BV.A5_SUSP_MFClient
    A5_SUSP_Valtra = A5_SUSP_Valtra_BV.A5_SUSP_ValtraClient
    A5_VRG = A5_VRG_BV.A5_VRGClient
    A7_ISC_APP38 = A7_ISC_APP38_BV.A7_ISC_APP38Client
    A7_REH_APP37 = A7_REH_APP37_BV.A7_REH_APP37Client
    A7_VRG = A7_VRG_BV.A7_VRGClient
    A11_TRANS = A11_TRANS_BV.A11_TRANSClient
    A11V = A11V_BV.A11VClient
    ADV_JOYSTICK = ADV_JOYSTICK_BV.ADV_JOYSTICKClient
    Armrest = Armrest_BV.ArmrestClient
    Auto5_RHS = Auto5_RHS_BV.Auto5_RHSClient
    BERGSTROM = BERGSTROM_BV.BERGSTROMClient
    CLIM_PANEL_AUTO = CLIM_PANEL_AUTO_BV.CLIM_PANEL_AUTOClient
    CLIM_PANEL_MANU = CLIM_PANEL_MANU_BV.CLIM_PANEL_MANUClient
    CLUSTER = CLUSTER_BV.CLUSTERClient
    DGW = DGW_BV.DGWClient
    DYNA4_TR1 = DYNA4_TR1_BV.DYNA4_TR1Client
    DYNA4_TR2 = DYNA4_TR2_BV.DYNA4_TR2Client
    FRONT_LOADER = FRONT_LOADER_BV.FRONT_LOADERClient
    IC1_C3 = IC1_C3_BV.IC1_C3Client
    IC2 = IC2_BV.IC2Client
    MULTIPAD = MULTIPAD_BV.MULTIPADClient
    NT03 = NT03_BV.NT03Client
    SANT03 = SANT03_BV.SANT03Client
    SRC14_34IO = SRC14_34IO_BV.SRC14_34IOClient
    SRC14_34M = SRC14_34M_BV.SRC14_34MClient
    SRC14_34V = SRC14_34V_BV.SRC14_34VClient
    SRC14_H2_S3_M1_21 = SRC14_H2_S3_M1_21_BV.SRC14_H2_S3_M1_21Client
    SRC14_S2 = SRC14_S2_BV.SRC14_S2Client
    SRCIO = SRCIO_BV.SRCIOClient
    SRCM = SRCM_BV.SRCMClient
    SRCV = SRCV_BV.SRCVClient


class OnlyForTestPurposesECUs(Enum):
    pass

class FlashArea(Enum):
    APPL = "APPL"
    BOOT = "BOOT"
    DATA = "DATA"
    MCF = "MCF"


class DiagnosticSessions(IntEnum):
    DEFAULT = 1
    PROGRAMMING = 2
    EXTENDED = 3
    SAFETY = 4
    EOL = 0x40
    DEFAULT_PROGRAMMING = 0x41


class SecurityLevel(IntEnum):
    SERVICE = 1
    SERVICE_REMOTE = 2
    MANUFACTURER = 3
    DEVELOPMENT = 4
    SUPPLIER = 5


