from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class IC1_C3_BVRoutineIdentifierSignals:
    CheckMemoryRequest = DiagMessage(0x0202, 'CheckMemoryRequest', [2], [1, 3, 4, 5], '', 0)

    CheckMemoryResponse = DiagMessage(0x0202, 'CheckMemoryResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckMemoryResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PASSED': [0, 0], 'FAILED': [1, 1]}, 0, 1, '', False, False, False))

    CheckProgrammingPreConditionsRequest = DiagMessage(0x0203, 'CheckProgrammingPreConditionsRequest', [3], None, '', 0)

    CheckProgrammingPreConditionsResponse = DiagMessage(0x0203, 'CheckProgrammingPreConditionsResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckProgrammingPreConditionsResponse.add_parameter(DiagParameter('ProgrammingPreConditionList', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGINE_SPEED_NOT_ZERO': [1, 1], 'IMMOBILIZER_NOT_UNLOCKED': [2, 2], 'TRANSMISSION_SPEED_IN_NOT_ZERO': [3, 3], 'TRANSMISSION_SPEED_OUT_NOT_ZERO': [4, 4], 'VEHICLE_SPEED_NOT_ZERO': [5, 5], 'CONTROLLING_ACTIVE': [6, 6], 'IGNITION_OFF_ON_NECESSARY': [7, 7], 'PROGRAMMING_VOLTAGE_TOO_LOW': [8, 8], 'IGNITION_NOT_ON': [9, 9], 'VEHICLE_VOLTAGE_TOO_LOW': [10, 10], 'TEMPERATURE_TOO_HIGH': [11, 11], 'TEMPERATURE_TOO_LOW': [12, 12], 'RESERVED_BY_HIS': [13, 127], 'VEHICLE_NOT_IN_SAFE_STATE': [128, 128], 'RESERVED_BY_MANUFACTURER': [129, 191], 'RESERVED_BY_SUPPLIER': [192, 255]}, 1, 255, 'for each wrong condition 1 byte is sent, if all conditions are meet 0 bytes are transmitted', False, True, False))

    RequestCalibResult_ThrottlePedal = DiagMessage(0x1201, 'RequestCalibResult_ThrottlePedal', [3, 64], None, '', 0)

    RequestCalibResult_ThrottlePedal_Response = DiagMessage(0x1201, 'RequestCalibResult_ThrottlePedal_Response', [3, 64], None, '', 1)
    RequestCalibResult_ThrottlePedal_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StartCalib_ThrottlePedal = DiagMessage(0x1201, 'StartCalib_ThrottlePedal', [3, 64], None, '', 2)
    StartCalib_ThrottlePedal.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))
    StartCalib_ThrottlePedal.add_parameter(DiagParameter('Monitoring_Type', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Value monitoring off': [0, 0], 'Value monitoring on (ACHT result)': [1, 1], 'Progress monitoring on': [2, 2]}, 0, 2, '', False, False, False))

    StartCalib_ThrottlePedal_Response = DiagMessage(0x1201, 'StartCalib_ThrottlePedal_Response', [3, 64], None, '', 1)
    StartCalib_ThrottlePedal_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopCalib_ThrottlePedal = DiagMessage(0x1201, 'StopCalib_ThrottlePedal', [3, 64], None, '', 1)
    StopCalib_ThrottlePedal.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopCalib_ThrottlePedal_Response = DiagMessage(0x1201, 'StopCalib_ThrottlePedal_Response', [3, 64], None, '', 2)
    StopCalib_ThrottlePedal_Response.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopCalib_ThrottlePedal_Response.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    RequestCalibResult_ClutchPedal = DiagMessage(0x1202, 'RequestCalibResult_ClutchPedal', [3, 64], None, '', 0)

    RequestCalibResult_ClutchPedal_Response = DiagMessage(0x1202, 'RequestCalibResult_ClutchPedal_Response', [3, 64], None, '', 1)
    RequestCalibResult_ClutchPedal_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StartCalib_ClutchPedal = DiagMessage(0x1202, 'StartCalib_ClutchPedal', [3, 64], None, '', 2)
    StartCalib_ClutchPedal.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))
    StartCalib_ClutchPedal.add_parameter(DiagParameter('Monitoring_Type', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Value monitoring off': [0, 0], 'Value monitoring on (ACHT result)': [1, 1], 'Progress monitoring on': [2, 2]}, 0, 2, '', False, False, False))

    StartCalib_ClutchPedal_Response = DiagMessage(0x1202, 'StartCalib_ClutchPedal_Response', [3, 64], None, '', 1)
    StartCalib_ClutchPedal_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopCalib_ClutchPedal = DiagMessage(0x1202, 'StopCalib_ClutchPedal', [3, 64], None, '', 1)
    StopCalib_ClutchPedal.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopCalib_ClutchPedal_Response = DiagMessage(0x1202, 'StopCalib_ClutchPedal_Response', [3, 64], None, '', 2)
    StopCalib_ClutchPedal_Response.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopCalib_ClutchPedal_Response.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    RequestCalibResult_THandle = DiagMessage(0x1203, 'RequestCalibResult_THandle', [3, 64], None, '', 0)

    RequestCalibResult_THandle_Response = DiagMessage(0x1203, 'RequestCalibResult_THandle_Response', [3, 64], None, '', 1)
    RequestCalibResult_THandle_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StartCalib_THandle = DiagMessage(0x1203, 'StartCalib_THandle', [3, 64], None, '', 2)
    StartCalib_THandle.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))
    StartCalib_THandle.add_parameter(DiagParameter('Monitoring_Type', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Value monitoring off': [0, 0], 'Value monitoring on (ACHT result)': [1, 1], 'Progress monitoring on': [2, 2]}, 0, 2, '', False, False, False))

    StartCalib_THandle_Response = DiagMessage(0x1203, 'StartCalib_THandle_Response', [3, 64], None, '', 1)
    StartCalib_THandle_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopCalib_THandle = DiagMessage(0x1203, 'StopCalib_THandle', [3, 64], None, '', 1)
    StopCalib_THandle.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopCalib_THandle_Response = DiagMessage(0x1203, 'StopCalib_THandle_Response', [3, 64], None, '', 2)
    StopCalib_THandle_Response.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopCalib_THandle_Response.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    EraseMemoryRequest = DiagMessage(0xFF00, 'EraseMemoryRequest', [2], [1, 3, 4, 5], '', 4)
    EraseMemoryRequest.add_parameter(DiagParameter('NumberOfBytesOfMemoryAddressParameter', 1, 0, 0, 4, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 15, '', False, False, False))
    EraseMemoryRequest.add_parameter(DiagParameter('NumberOfBytesOfMemorySizeParameter', 2, 0, 4, 4, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 15, '', False, False, False))
    EraseMemoryRequest.add_parameter(DiagParameter('MemoryAddress', 3, 1, 0, 32, SignalByteOrder.Motorola, SignalType.BYTEFIELD, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, '', False, False, False))
    EraseMemoryRequest.add_parameter(DiagParameter('MemorySize', 4, 5, 0, 32, SignalByteOrder.Motorola, SignalType.BYTEFIELD, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, '', False, False, False))

    EraseMemoryResponse = DiagMessage(0xFF00, 'EraseMemoryResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    EraseMemoryResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PASSED': [0, 0], 'FAILED': [1, 1]}, 0, 1, '', False, False, False))

    CheckProgrammingDependenciesRequest = DiagMessage(0xFF01, 'CheckProgrammingDependenciesRequest', [2], [1, 3, 4, 5], '', 0)

    CheckProgrammingDependenciesResponse = DiagMessage(0xFF01, 'CheckProgrammingDependenciesResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckProgrammingDependenciesResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CORRECT_RESULT': [0, 0], 'INCORRECT_RESULT': [1, 1], 'INCORRECT_RESULT_ERROR_SW_HW': [2, 2], 'INCORRECT_RESULT_ERROR_SW_SW': [3, 3], 'INCORRECT_RESULT_ONE_OR_MORE_BLOCKS_NOT_PROGRAMMED': [4, 4]}, 0, 4, '', False, False, False))


class IC1_C3_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    FNR = DiagMessage(0x1100, 'FNR', [1, 2, 3, 4, 64], None, '', 2)
    FNR.add_parameter(DiagParameter('FNRVoltageRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 122.0, 'mV', 0, 65535, '', False, False, False))
    FNR.add_parameter(DiagParameter('FNRConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'FNRForwardPlus': [0, 0], 'FNRForward': [1, 1], 'FNRForwardMin': [2, 2], 'FNRNeutral': [3, 3], 'FNRReverseMin': [4, 4], 'FNRReverse': [5, 5], 'FNRReversePlus': [6, 6], 'OFF': [7, 7], 'OFFx1': [8, 8], 'ERROR': [9, 255]}, 0, 255, '[1][C3R_20-C3R_21][Cab_commands][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    FNRNormallyOpen = DiagMessage(0x1101, 'FNRNormallyOpen', [1, 2, 3, 4, 64], None, '', 2)
    FNRNormallyOpen.add_parameter(DiagParameter('FNRNormallyOpenRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][ ][ ][D4][Base][raw][IC1][Y_N][1_0]#[1][C3R_20-C3R_21][Cab_commands][ ][57-DI_X8][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    FNRNormallyOpen.add_parameter(DiagParameter('FNRNormallyOpenConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][ ][57-DI_X8][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    FNRNormallyClose = DiagMessage(0x1102, 'FNRNormallyClose', [1, 2, 3, 4, 64], None, '', 2)
    FNRNormallyClose.add_parameter(DiagParameter('FNRNormallyCloseRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][ ][58-DI_X9][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    FNRNormallyClose.add_parameter(DiagParameter('FNRNormallyCloseConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][ ][58-DI_X9][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    DotMatrixNavigationsKeys = DiagMessage(0x1103, 'DotMatrixNavigationsKeys', [1, 2, 3, 4, 64], None, '', 5)
    DotMatrixNavigationsKeys.add_parameter(DiagParameter('DotMatrixNavigationsKeysRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mV', 0, 65535, '[1][S2-S3-M1][Cab_commands][X57][11-AI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][11-AN_5][D4][Base][raw][IC1][Y_N][1_0]#[1][C3R_20-C3R_21][Cab_commands][X57][11-AN_5][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    DotMatrixNavigationsKeys.add_parameter(DiagParameter('DotMatrixUpSwitchConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X57_UP][11-AI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][11-AN_5][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))
    DotMatrixNavigationsKeys.add_parameter(DiagParameter('DotMatrixDownSwitchConvertedValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X57_DOWN][11-AI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][11-AN_5][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))
    DotMatrixNavigationsKeys.add_parameter(DiagParameter('DotMatrixLeftSwitchConvertedValue', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X57_LEFT][11-AI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][11-AN_5][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))
    DotMatrixNavigationsKeys.add_parameter(DiagParameter('DotMatrixRightSwitchConvertedValue', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X57_RIGHT][11-AI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][11-AN_5][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    DotMatrixHomeSwitch = DiagMessage(0x1104, 'DotMatrixHomeSwitch', [1, 2, 3, 4, 64], None, '', 2)
    DotMatrixHomeSwitch.add_parameter(DiagParameter('DotMatrixHomeSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Cab_commands][X57][8-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][8][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    DotMatrixHomeSwitch.add_parameter(DiagParameter('DotMatrixHomeSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X57][8-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][8][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    DotMatrixRefreshSwitch = DiagMessage(0x1105, 'DotMatrixRefreshSwitch', [1, 2, 3, 4, 64], None, '', 2)
    DotMatrixRefreshSwitch.add_parameter(DiagParameter('DotMatrixRefreshSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Cab_commands][X57][6-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][6][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    DotMatrixRefreshSwitch.add_parameter(DiagParameter('DotMatrixRefreshSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X57][6-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][6][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    DotMatrixOkSwitch = DiagMessage(0x1106, 'DotMatrixOkSwitch', [1, 2, 3, 4, 64], None, '', 2)
    DotMatrixOkSwitch.add_parameter(DiagParameter('DotMatrixOkSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Cab_commands][X57][66-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][66][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    DotMatrixOkSwitch.add_parameter(DiagParameter('DotMatrixOkSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X57][66-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X57][66][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    PedalsClutch = DiagMessage(0x1107, 'PedalsClutch', [1, 2, 3, 4, 64], None, '', 2)
    PedalsClutch.add_parameter(DiagParameter('PedalsClutchRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mV', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][X68][4-AN_0][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    PedalsClutch.add_parameter(DiagParameter('PedalsClutchConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '[1][C3R_20-C3R_21][Cab_commands][X68][4-AN_0][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    TOC = DiagMessage(0x1108, 'TOC', [1, 2, 3, 4, 64], None, '', 2)
    TOC.add_parameter(DiagParameter('TOCRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X68][20-DI_0][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    TOC.add_parameter(DiagParameter('TOCConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X68][20-DI_0][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    BOCNO = DiagMessage(0x1109, 'BOCNO', [1, 2, 3, 4, 64], None, '', 2)
    BOCNO.add_parameter(DiagParameter('BOCNORawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X68][19-DI_6][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    BOCNO.add_parameter(DiagParameter('BOCNOConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X68][19-DI_6][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    THandleMultipadPosition = DiagMessage(0x110A, 'THandleMultipadPosition', [1, 2, 3, 4, 64], None, '', 2)
    THandleMultipadPosition.add_parameter(DiagParameter('THandleMultipadPositionRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mV', 0, 65535, '[1][S2-S3-M1][Cab_commands][X106][7-AI][D4-D6][L][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X106][7-AN_2][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    THandleMultipadPosition.add_parameter(DiagParameter('THanleMultipadPositionConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PUSH': [0, 0], 'CENTER': [1, 1], 'PULLED': [2, 2], 'ERROR': [3, 3]}, 0, 3, '[1][S2-S3-M1][Cab_commands][X106][7-AI][D4-D6][L][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X106][7-AN_2][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    ThrottlePedalHand = DiagMessage(0x110B, 'ThrottlePedalHand', [1, 2, 3, 4, 64], None, '', 2)
    ThrottlePedalHand.add_parameter(DiagParameter('ThrottlePedalHandRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mV', 0, 65535, '[1][S2-S3-M1][Cab_commands][X71][10-AI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X122][10-AN_3][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    ThrottlePedalHand.add_parameter(DiagParameter('ThrottlePedalHandConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '[1][S2-S3-M1][Cab_commands][X71][10-AI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Cab_commands][X122][10-AN_3][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    DifflockSwitch = DiagMessage(0x110C, 'DifflockSwitch', [1, 2, 3, 4, 64], None, '', 2)
    DifflockSwitch.add_parameter(DiagParameter('DifflockSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X138][38-BIN][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    DifflockSwitch.add_parameter(DiagParameter('DifflockSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 1], 'CLOSE': [2, 2], 'OPENx1': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X138][38-BIN][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    i4WDSwitch = DiagMessage(0x110D, 'i4WDSwitch', [1, 2, 3, 4, 64], None, '', 2)
    i4WDSwitch.add_parameter(DiagParameter('4WDSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X137][13-DI_5][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    i4WDSwitch.add_parameter(DiagParameter('4WDSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 1], 'CLOSE': [2, 2], 'OPENx1': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X137][13-DI_5][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    SeatSwitch = DiagMessage(0x110E, 'SeatSwitch', [1, 2, 3, 4, 64], None, '', 2)
    SeatSwitch.add_parameter(DiagParameter('SeatSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X470][54-DI_X5][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    SeatSwitch.add_parameter(DiagParameter('SeatSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X470][54-DI_X5][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    HandBrakeSwitch = DiagMessage(0x110F, 'HandBrakeSwitch', [1, 2, 3, 4, 64], None, '', 2)
    HandBrakeSwitch.add_parameter(DiagParameter('HandBrakeSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X618][49-DI_4][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    HandBrakeSwitch.add_parameter(DiagParameter('HandBrakeSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X618][49-DI_4][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    THandleRangeSwitch = DiagMessage(0x1110, 'THandleRangeSwitch', [1, 2, 3, 4, 64], None, '', 2)
    THandleRangeSwitch.add_parameter(DiagParameter('THandleRangeSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X719][53-DI_X4][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    THandleRangeSwitch.add_parameter(DiagParameter('THandleRangeSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 1], 'CLOSE': [2, 2], 'OPENx1': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X719][53-DI_X4][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    IntermixPotentiometer = DiagMessage(0x1111, 'IntermixPotentiometer', [1, 2, 3, 4, 64], None, '', 2)
    IntermixPotentiometer.add_parameter(DiagParameter('IntermixPotentiometerRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'Pts', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][X750][9-AN_X13][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    IntermixPotentiometer.add_parameter(DiagParameter('IntermixPotentiometerConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X750][9-AN_X13][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    MaxHeightPotentiometer = DiagMessage(0x1112, 'MaxHeightPotentiometer', [1, 2, 3, 4, 64], None, '', 2)
    MaxHeightPotentiometer.add_parameter(DiagParameter('MaxHeightPotentiometerRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'Pts', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][X897][44-AN_1][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    MaxHeightPotentiometer.add_parameter(DiagParameter('MaxHeightPotentiometerConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X897][44-AN_1][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    DownShiftSpeedPotentiometer = DiagMessage(0x1113, 'DownShiftSpeedPotentiometer', [1, 2, 3, 4, 64], None, '', 3)
    DownShiftSpeedPotentiometer.add_parameter(DiagParameter('DownShiftSpeedPotentiometerRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'Pts', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][X898][15-AN_8][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    DownShiftSpeedPotentiometer.add_parameter(DiagParameter('DownShiftSpeedPotentiometerMode', 2, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'MANUAL': [0, 0], 'AUTO': [1, 1]}, 0, 1, '', False, False, False))
    DownShiftSpeedPotentiometer.add_parameter(DiagParameter('DownShiftSpeedPotentiometerConvertedValue', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X898][15-AN_8][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    PTOSpeedSelectionSwitch = DiagMessage(0x1114, 'PTOSpeedSelectionSwitch', [1, 2, 3, 4, 64], None, '', 2)
    PTOSpeedSelectionSwitch.add_parameter(DiagParameter('PTOSpeedSelectionSwitchRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mV', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][X914][60-AN_X0][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    PTOSpeedSelectionSwitch.add_parameter(DiagParameter('PTOSpeedSelectionSwitchConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ERROR': [0, 0], 'PTO 540': [1, 1], 'PTO 540E': [2, 2], 'PTO 1000': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X914][60-AN_X0][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    TransportModeSwitch = DiagMessage(0x1115, 'TransportModeSwitch', [1, 2, 3, 4, 64], None, '', 2)
    TransportModeSwitch.add_parameter(DiagParameter('TransportModeSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X933][48-DI_3][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    TransportModeSwitch.add_parameter(DiagParameter('TransportModeSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 1], 'CLOSE': [2, 2], 'OPENx1': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X933][48-DI_3][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    PneumaticTrailerBrakeCutOutSwitch = DiagMessage(0x1116, 'PneumaticTrailerBrakeCutOutSwitch', [1, 2, 3, 4, 64], None, '', 2)
    PneumaticTrailerBrakeCutOutSwitch.add_parameter(DiagParameter('PneumaticTrailerBrakeCutOutSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X1007][DI_X6][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    PneumaticTrailerBrakeCutOutSwitch.add_parameter(DiagParameter('PneumaticTrailerBrakeCutOutSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 1], 'CLOSE': [2, 2], 'OPENx1': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X1007][DI_X6][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    BrakeNeutralSwitch = DiagMessage(0x1117, 'BrakeNeutralSwitch', [1, 2, 3, 4, 64], None, '', 2)
    BrakeNeutralSwitch.add_parameter(DiagParameter('BrakeNeutralSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X1010][17-DI_X1][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    BrakeNeutralSwitch.add_parameter(DiagParameter('BrakeNeutralSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X1010][17-DI_X1][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    AutoDriveECOSwitch = DiagMessage(0x1118, 'AutoDriveECOSwitch', [1, 2, 3, 4, 64], None, '', 2)
    AutoDriveECOSwitch.add_parameter(DiagParameter('AutoDriveECOSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X1011][21-DI_7][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    AutoDriveECOSwitch.add_parameter(DiagParameter('AutodriveECOSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 1], 'CLOSE': [2, 2]}, 0, 2, '[1][C3R_20-C3R_21][Cab_commands][X1011][21-DI_7][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    AutoDrivePowerSwitch = DiagMessage(0x1119, 'AutoDrivePowerSwitch', [1, 2, 3, 4, 64], None, '', 2)
    AutoDrivePowerSwitch.add_parameter(DiagParameter('AutoDrivePowerSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][X1011][24-DI_8][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    AutoDrivePowerSwitch.add_parameter(DiagParameter('AutodrivePowerSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'OPENx1': [2, 2]}, 0, 2, '[1][C3R_20-C3R_21][Cab_commands][X1011][24-DI_8][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    LoaderOnOffSwitch = DiagMessage(0x111A, 'LoaderOnOffSwitch', [1, 2, 3, 4, 64], None, '', 2)
    LoaderOnOffSwitch.add_parameter(DiagParameter('LoaderOnOffSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][ ][46-DI_1][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    LoaderOnOffSwitch.add_parameter(DiagParameter('LoaderOnOffSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'ERROR': [1, 1], 'OFF': [2, 2]}, 0, 2, '[1][C3R_20-C3R_21][Cab_commands][ ][46-DI_1][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    LoaderSuspensionSwitch = DiagMessage(0x111B, 'LoaderSuspensionSwitch', [1, 2, 3, 4, 64], None, '', 2)
    LoaderSuspensionSwitch.add_parameter(DiagParameter('LoaderSuspensionSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][ ][47-DI_2][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    LoaderSuspensionSwitch.add_parameter(DiagParameter('LoaderSuspensionSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ERROR': [1, 1], 'ON': [2, 2]}, 0, 2, '[1][C3R_20-C3R_21][Cab_commands][ ][47-DI_2][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    LoaderBucketLockSwitch = DiagMessage(0x111C, 'LoaderBucketLockSwitch', [1, 2, 3, 4, 64], None, '', 2)
    LoaderBucketLockSwitch.add_parameter(DiagParameter('LoaderBucketLockSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Cab_commands][ ][50-DI_X0][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    LoaderBucketLockSwitch.add_parameter(DiagParameter('LoaderBucketLockSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 255]}, 0, 255, '[1][C3R_20-C3R_21][Cab_commands][ ][50-DI_X0][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))

    i4WDStateMode = DiagMessage(0x111D, 'i4WDStateMode', [1, 2, 3, 4, 64], None, '', 2)
    i4WDStateMode.add_parameter(DiagParameter('4WDStateModeRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'INIT': [0, 0], 'OFF': [1, 1], 'MANUAL': [2, 2], 'AUTO': [3, 3], 'AUTOx1': [4, 4]}, 0, 4, '', False, False, False))
    i4WDStateMode.add_parameter(DiagParameter('4WDStateModeConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGAGE': [1, 1], 'DISENGAGE': [2, 2]}, 1, 2, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    DifflockStateMode = DiagMessage(0x111E, 'DifflockStateMode', [1, 2, 3, 4, 64], None, '', 2)
    DifflockStateMode.add_parameter(DiagParameter('DifflockStateModeRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'INIT': [0, 0], 'OFF': [1, 1], 'MANUAL': [2, 2], 'MANUALx1': [3, 3]}, 0, 3, '', False, False, False))
    DifflockStateMode.add_parameter(DiagParameter('DifflockStateModeConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGAGE': [1, 1], 'DISENGAGE': [2, 2]}, 1, 2, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    MemoEngineSpeedValue = DiagMessage(0x111F, 'MemoEngineSpeedValue', [1, 2, 3, 4, 64], None, '', 1)
    MemoEngineSpeedValue.add_parameter(DiagParameter('MemoEngineSpeedValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'rpm', 0, 65535, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    MemoSpeedState = DiagMessage(0x1120, 'MemoSpeedState', [1, 2, 3, 4, 64], None, '', 1)
    MemoSpeedState.add_parameter(DiagParameter('MemoSpeedStateConvertedValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 2]}, 0, 2, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    PresetSpeedForwardTortoise = DiagMessage(0x1121, 'PresetSpeedForwardTortoise', [1, 2, 3, 4, 64], None, '', 1)
    PresetSpeedForwardTortoise.add_parameter(DiagParameter('PresetSpeedForwardTortoiseRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 65535, '', False, False, False))

    PresetSpeedReverseTortoise = DiagMessage(0x1123, 'PresetSpeedReverseTortoise', [1, 2, 3, 4, 64], None, '', 1)
    PresetSpeedReverseTortoise.add_parameter(DiagParameter('PresetSpeedReverseTortoiseRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AutodriveMode = DiagMessage(0x1124, 'AutodriveMode', [1, 2, 3, 4, 64], None, '', 1)
    AutodriveMode.add_parameter(DiagParameter('AutodriveModeConvertedValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO ACTION': [0, 0], 'DownShift': [1, 1], 'UpShift': [2, 2], 'ERROR': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    BrakeToNeutralState = DiagMessage(0x1125, 'BrakeToNeutralState', [1, 2, 3, 4, 64], None, '', 1)
    BrakeToNeutralState.add_parameter(DiagParameter('BrakeToNeutralStateConvertedValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'DISABLED': [2, 2]}, 0, 2, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    BrakeToNeutralRequest = DiagMessage(0x1126, 'BrakeToNeutralRequest', [1, 2, 3, 4, 64], None, '', 1)
    BrakeToNeutralRequest.add_parameter(DiagParameter('BrakeToNeutralRequestConvertedValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'OFFx1': [2, 2]}, 0, 2, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    BuzzerSignal = DiagMessage(0x1127, 'BuzzerSignal', [1, 2, 3, 4, 64], None, '', 1)
    BuzzerSignal.add_parameter(DiagParameter('BuzzerSignalConvertedValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][X73][22-DO][D4-D6-CVT][L-S][conv][IC1][Y_N][0_0]', False, False, False))

    AlternatorInput = DiagMessage(0x1128, 'AlternatorInput', [1, 2, 3, 4, 64], None, '', 2)
    AlternatorInput.add_parameter(DiagParameter('AlternatorInputRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Miscellaneous][X194][51][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    AlternatorInput.add_parameter(DiagParameter('AlternatorInputConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Miscellaneous][X194][51][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    FuelGauge = DiagMessage(0x1129, 'FuelGauge', [1, 2, 3, 4, 64], None, '', 2)
    FuelGauge.add_parameter(DiagParameter('FuelGaugeRawValue', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'ohm', 0, 65535, '[1][S2-S3-M1][Miscellaneous][X197-B2][12-AI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X197][12][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    FuelGauge.add_parameter(DiagParameter('FuelGaugeConvertedValue', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '[1][S2-S3-M1][Miscellaneous][X197-B2][12-AI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X197][12][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    AirFilter = DiagMessage(0x112A, 'AirFilter', [1, 2, 3, 4, 64], None, '', 2)
    AirFilter.add_parameter(DiagParameter('AirFilterConvertedValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Air_filter_Ok': [0, 0], 'Air_filter_clogged': [250, 250], 'Sensor_Error': [254, 254], 'Not_available': [255, 255]}, 0, 255, '[1][S3-M1][Miscellaneous][X253][36-DI][D4-D6][L-S][conv][IC1][N_N][0_0]#[1][C3R_20-C3R_21][Miscellaneous][X253][CAN][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    AirFilter.add_parameter(DiagParameter('AirFilterRawValue', 2, 1, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][S3-M1][Miscellaneous][X253][36-DI][D4-D6][L-S][raw][IC1][N_N][0_0]#[1][C3R_20-C3R_21][Miscellaneous][X253][CAN][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    LeftTurnLight = DiagMessage(0x112C, 'LeftTurnLight', [1, 2, 3, 4, 64], None, '', 2)
    LeftTurnLight.add_parameter(DiagParameter('LeftTurnLightRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Cab_commands][X652][26-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X652][26][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    LeftTurnLight.add_parameter(DiagParameter('LeftTurnLightConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X652][26-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X652][26][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    RightTurnLight = DiagMessage(0x112D, 'RightTurnLight', [1, 2, 3, 4, 64], None, '', 2)
    RightTurnLight.add_parameter(DiagParameter('RightTurnLightRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Cab_commands][X652][27-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X652][27][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    RightTurnLight.add_parameter(DiagParameter('RightTurnLightConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X652][27-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X652][27][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    Trailer1 = DiagMessage(0x112E, 'Trailer1', [1, 2, 3, 4, 64], None, '', 2)
    Trailer1.add_parameter(DiagParameter('Trailer1RawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Cab_commands][X652][28-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X652][28][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    Trailer1.add_parameter(DiagParameter('Trailer1ConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X652][28-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X652][28][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    Trailer2 = DiagMessage(0x112F, 'Trailer2', [1, 2, 3, 4, 64], None, '', 2)
    Trailer2.add_parameter(DiagParameter('Trailer2RawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Cab_commands][X652][29-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X652][29][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    Trailer2.add_parameter(DiagParameter('Trailer2ConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X652][29-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X652][29][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    ImplementStatus = DiagMessage(0x1130, 'ImplementStatus', [1, 2, 3, 4, 64], None, '', 2)
    ImplementStatus.add_parameter(DiagParameter('ImplementStatusRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Miscellaneous][X184][31-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X900][31-DI_X13][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    ImplementStatus.add_parameter(DiagParameter('ImplementStatusConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CLOSE': [0, 0], 'OPEN': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][X184][31-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X900][31-DI_X13][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    HighBeamLight = DiagMessage(0x1131, 'HighBeamLight', [1, 2, 3, 4, 64], None, '', 2)
    HighBeamLight.add_parameter(DiagParameter('HighBeamLightRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Cab_commands][X64][25-DI][D4-D6-CVT][L-S][raw][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X926][25][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    HighBeamLight.add_parameter(DiagParameter('HighBeamLightConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X64][25-DI][D4-D6-CVT][L-S][conv][IC1][Y_N_N][0_0_0]#[1][C3R_20-C3R_21][Miscellaneous][X926][25][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    MarkerLight = DiagMessage(0x1132, 'MarkerLight', [1, 2, 3, 4, 64], None, '', 2)
    MarkerLight.add_parameter(DiagParameter('MarkerLightRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Miscellaneous][X928][64-AN_X7][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    MarkerLight.add_parameter(DiagParameter('MarkerLightConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Miscellaneous][X928][64-AN_X7][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    BuzzerOnWarningActivated = DiagMessage(0x1134, 'BuzzerOnWarningActivated', [1, 2, 3, 4, 64], None, '', 2)
    BuzzerOnWarningActivated.add_parameter(DiagParameter('BuzzerOnWarningActivatedRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Miscellaneous][ ][ ][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    BuzzerOnWarningActivated.add_parameter(DiagParameter('BuzzerOnWarningActivatedConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Miscellaneous][ ][ ][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    StartInformationStarterSwitch = DiagMessage(0x1135, 'StartInformationStarterSwitch', [1, 2, 3, 4, 64], None, '', 2)
    StartInformationStarterSwitch.add_parameter(DiagParameter('StartInformationStarterSwitchRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Miscellaneous][ ][ ][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    StartInformationStarterSwitch.add_parameter(DiagParameter('StartInformationFromStarterSwitchConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Miscellaneous][ ][ ][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    PneumaticPressureSensor = DiagMessage(0x1136, 'PneumaticPressureSensor', [1, 2, 3, 4, 64], None, '', 2)
    PneumaticPressureSensor.add_parameter(DiagParameter('PneumaticPressureSensorRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S3-M1][Braking_system][X683][56-DI][CVT][S][raw][IC1][Y_N][0_0]#[1][C3R_20-C3R_21][Braking_system][X168][63-DI_X15][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    PneumaticPressureSensor.add_parameter(DiagParameter('PneumaticPressureSensorConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'NOT_Available': [255, 255]}, 0, 255, '[1][S3-M1][Braking_system][X683][56-DI][CVT][S][conv][IC1][Y_N][0_0]#[1][C3R_20-C3R_21][Braking_system][X168][63-DI_X15][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    PneumaticTrailerBrakeSolenoidValve = DiagMessage(0x1137, 'PneumaticTrailerBrakeSolenoidValve', [1, 2, 3, 4, 64], None, '', 1)
    PneumaticTrailerBrakeSolenoidValve.add_parameter(DiagParameter('PneumaticTrailerBreakeSolenoidValveConvertedValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Braking_system][X339][43-PWM_3][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    BrakeFluidLevel = DiagMessage(0x1138, 'BrakeFluidLevel', [1, 2, 3, 4, 64], None, '', 2)
    BrakeFluidLevel.add_parameter(DiagParameter('BrakeFluidLevelRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2][Braking_system][X894][56-DI][D4-D6][L-S][raw][IC1][Y][0]#[1][C3R_20-C3R_21][Braking_system][X894][56-DI_X7][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    BrakeFluidLevel.add_parameter(DiagParameter('BrakeFluidLevelConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2][Braking_system][X894][56-DI][D4-D6][L-S][conv][IC1][Y][0]#[1][C3R_20-C3R_21][Braking_system][X894][56-DI_X7][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    TrailerBrakeDefaultFromABS = DiagMessage(0x1139, 'TrailerBrakeDefaultFromABS', [1, 2, 3, 4, 64], None, '', 2)
    TrailerBrakeDefaultFromABS.add_parameter(DiagParameter('TrailerBrakeDefaultFromABSRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Braking_system][X990][30-DI_X11][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    TrailerBrakeDefaultFromABS.add_parameter(DiagParameter('TrailerBrakeDefaultFromABSConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Braking_system][X990][30-DI_X11][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    PneumaticTrailerBrakingTestSensor = DiagMessage(0x113A, 'PneumaticTrailerBrakingTestSensor', [1, 2, 3, 4, 64], None, '', 2)
    PneumaticTrailerBrakingTestSensor.add_parameter(DiagParameter('PneumaticTrailerBrakingTestSensorRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Braking_system][X198][63-DI][D4-D6-CVT][L-S][raw][IC1][N_N_N][0_0_0]#[1][C3R_20-C3R_21][Braking_system][X168][52-DI_X3][D4][Base][raw][IC1][Y_N][0_0]#[1][C3R_20-C3R_21][Braking_system][X996][52-DI_X3][D4][Base][raw][IC1][Y_N][1_0]', False, False, False))
    PneumaticTrailerBrakingTestSensor.add_parameter(DiagParameter('PneumaticTrailerBrakingTestSensorConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Braking_system][X198][63-DI][D4-D6-CVT][L-S][conv][IC1][N_N_N][0_0_0]#[1][C3R_20-C3R_21][Braking_system][X168][52-DI_X3][D4][Base][conv][IC1][Y_N][0_0]#[1][C3R_20-C3R_21][Braking_system][X996][52-DI_X3][D4][Base][conv][IC1][Y_N][1_0]', False, False, False))

    DisplayedSpeed = DiagMessage(0x113B, 'DisplayedSpeed', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    DisplayedSpeed.add_parameter(DiagParameter('DisplayedSpeed', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'km/h', 1, 65535, '', False, False, False))

    HydraulicPressureSensor = DiagMessage(0x1155, 'HydraulicPressureSensor', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 2)
    HydraulicPressureSensor.add_parameter(DiagParameter('HydraulicPressureSensorRawValue', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Braking_system][X1122][63-DI_X15][D4][Base][raw][IC1][Y_N][0_0]', False, False, False))
    HydraulicPressureSensor.add_parameter(DiagParameter('HydraulicPressureSensorConvertedValue', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'NOT_Available': [255, 255]}, 0, 255, '[1][C3R_20-C3R_21][Braking_system][X1122][63-DI_X15][D4][Base][conv][IC1][Y_N][0_0]', False, False, False))

    ThrottlePedalCalibrationState = DiagMessage(0x1201, 'ThrottlePedalCalibrationState', [1, 2, 3, 4, 64], None, '', 1)
    ThrottlePedalCalibrationState.add_parameter(DiagParameter('ThrottlePedalCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    ClutchPedalCalibrationState = DiagMessage(0x1202, 'ClutchPedalCalibrationState', [1, 2, 3, 4, 64], None, '', 1)
    ClutchPedalCalibrationState.add_parameter(DiagParameter('ClutchPedalCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    THandleCalibrationState = DiagMessage(0x1203, 'THandleCalibrationState', [1, 2, 3, 4, 64], None, '', 1)
    THandleCalibrationState.add_parameter(DiagParameter('THandlePedalCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    MaintenanceNextServiceHours = DiagMessage(0x1330, 'MaintenanceNextServiceHours', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    MaintenanceNextServiceHours.add_parameter(DiagParameter('ServiceHours', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    TractorHoursOffset = DiagMessage(0x1331, 'TractorHoursOffset', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    TractorHoursOffset.add_parameter(DiagParameter('HoursOffset', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -2147483648, 2147483647, '', False, False, False))

    EngineHoursMemo = DiagMessage(0x1332, 'EngineHoursMemo', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    EngineHoursMemo.add_parameter(DiagParameter('HoursMemo', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    TractorHoursSynchroStatus = DiagMessage(0xAA61, 'TractorHoursSynchroStatus', [1, 3, 4, 64], None, '', 1)
    TractorHoursSynchroStatus.add_parameter(DiagParameter('TractorHoursSynchroStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CNTR_STATUS_SYNCHRO_INIT': [0, 0], 'CNTR_STATUS_SYNCHRO_START': [1, 1], 'CNTR_STATUS_SYNCHRO_OK': [2, 2], 'CNTR_STATUS_SYNCHRO_UNDEF': [3, 3]}, 0, 3, '[1][C3][ ][ ][ ][ ][ ][Y][0)', False, False, False))

    Wheel_Circumference = DiagMessage(0xF039, 'Wheel_Circumference', [1, 2, 3, 4, 64], None, '', 1)
    Wheel_Circumference.add_parameter(DiagParameter('Circumference', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 1, 65535, '', False, False, False))

    BootSoftwareIdentification = DiagMessage(0xF180, 'BootSoftwareIdentification', [1, 2, 3, 4, 64, 65], None, '', 1)
    BootSoftwareIdentification.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 200 bytes allowed', False, False, False))

    ApplicationSoftwareIdentification = DiagMessage(0xF181, 'ApplicationSoftwareIdentification', [1, 2, 3, 4, 64, 65], None, '', 1)
    ApplicationSoftwareIdentification.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 200 bytes allowed', False, False, False))

    ApplicationDataIdentification = DiagMessage(0xF182, 'ApplicationDataIdentification', [1, 2, 3, 4, 64, 65], None, '', 1)
    ApplicationDataIdentification.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 200 bytes allowed', False, False, False))

    BootSoftwareFingerprint = DiagMessage(0xF183, 'BootSoftwareFingerprint', [1, 2, 3, 4, 64], None, '', 5)
    BootSoftwareFingerprint.add_parameter(DiagParameter('NumberOfFollowingFingerPrints', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 255, 'set to 0 if no valid fingerprints are stored, e.g at delivery status', False, False, False))
    BootSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingYear', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, 'SPN 964', False, True, False))
    BootSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, True, False))
    BootSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingDay', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, True, False))
    BootSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 5, 4, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, True, False))

    ApplicationSoftwareFingerprint = DiagMessage(0xF184, 'ApplicationSoftwareFingerprint', [1, 2, 3, 4, 64], None, '', 5)
    ApplicationSoftwareFingerprint.add_parameter(DiagParameter('NumberOfFollowingFingerPrints', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 255, 'set to 0 if no valid fingerprints are stored, e.g at delivery status', False, False, False))
    ApplicationSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingYear', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, 'SPN 964', False, True, False))
    ApplicationSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, True, False))
    ApplicationSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingDay', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, True, False))
    ApplicationSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 5, 4, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, True, False))

    ApplicationDataFingerprint = DiagMessage(0xF185, 'ApplicationDataFingerprint', [1, 2, 3, 4, 64], None, '', 5)
    ApplicationDataFingerprint.add_parameter(DiagParameter('NumberOfFollowingFingerPrints', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 255, 'set to 0 if no valid fingerprints are stored, e.g at delivery status', False, False, False))
    ApplicationDataFingerprint.add_parameter(DiagParameter('ProgrammingYear', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, 'SPN 964', False, True, False))
    ApplicationDataFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, True, False))
    ApplicationDataFingerprint.add_parameter(DiagParameter('ProgrammingDay', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, True, False))
    ApplicationDataFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 5, 4, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, True, False))

    ActiveDiagnosticSession = DiagMessage(0xF186, 'ActiveDiagnosticSession', [1, 2, 3, 4, 64, 65], None, '', 1)
    ActiveDiagnosticSession.add_parameter(DiagParameter('SessionNumber', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 65, '', False, False, False))

    VehicleManufacturerSparePartNumber = DiagMessage(0xF187, 'VehicleManufacturerSparePartNumber', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerSparePartNumber.add_parameter(DiagParameter('PartNumber', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Partnumber of the electronic board (mandatory, all 0xFF --> "INVALID")', False, False, False))

    EcuSerialNumber = DiagMessage(0xF18C, 'EcuSerialNumber', [1, 2, 3, 4, 64], None, '', 1)
    EcuSerialNumber.add_parameter(DiagParameter('SerialNumber', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 32 bytes allowed (all 0xFF --> "INVALID")', False, False, False))

    VehicleManufacturerKitAssemblyPartNumber = DiagMessage(0xF18E, 'VehicleManufacturerKitAssemblyPartNumber', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerKitAssemblyPartNumber.add_parameter(DiagParameter('AssemblyPartNumber', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Partnumber of a complete Assembly e.g. G-Nr (all 0xFF --> "INVALID")', False, False, False))

    VehicleIdentificationNumber = DiagMessage(0xF190, 'VehicleIdentificationNumber', [1, 2, 3, 4, 64, 65], None, '', 1)
    VehicleIdentificationNumber.add_parameter(DiagParameter('VinNumber', 1, 0, 0, 136, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '17 bytes fixed length (all 0xFF --> "INVALID")', False, False, False))

    VehicleManufacturerECUHardwareNumber = DiagMessage(0xF191, 'VehicleManufacturerECUHardwareNumber', [1, 2, 3, 4, 64, 65], None, '', 1)
    VehicleManufacturerECUHardwareNumber.add_parameter(DiagParameter('VirtualPartNumber', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 4293918720, 4294967295, 'Unique feature identifier (mandatory for compatibility check hardware/software at ECU programming) ', False, False, False))

    SystemSupplierECUHardwareVersionNumber = DiagMessage(0xF193, 'SystemSupplierECUHardwareVersionNumber', [1, 3, 4, 64], None, '', 1)
    SystemSupplierECUHardwareVersionNumber.add_parameter(DiagParameter('SystemSupplierHardwareVersion', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '(optional used by ECU supplier)', False, False, False))

    VehicleManufacturerEOLProgramInfoCode = DiagMessage(0xF1A3, 'VehicleManufacturerEOLProgramInfoCode', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerEOLProgramInfoCode.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Name of PROGRAMMING Tool', False, False, False))

    VehicleManufacturerEOLProgramVersionCode = DiagMessage(0xF1A4, 'VehicleManufacturerEOLProgramVersionCode', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerEOLProgramVersionCode.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Version of PROGRAMMING Tool', False, False, False))

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [1, 2, 3, 4, 64], None, '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))


class IC1_C3_BVWriteDataSignals:
    MaintenanceNextServiceHours = DiagMessage(0x1330, 'MaintenanceNextServiceHours', [64, 3, 4], [1, 2, 3, 4, 5], '', 1)
    MaintenanceNextServiceHours.add_parameter(DiagParameter('ServiceHours', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    TractorHoursOffset = DiagMessage(0x1331, 'TractorHoursOffset', [64, 3, 4], [1, 2, 3, 4, 5], '', 1)
    TractorHoursOffset.add_parameter(DiagParameter('HoursOffset', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -2147483648, 2147483647, '', False, False, False))

    EngineHoursMemo = DiagMessage(0x1332, 'EngineHoursMemo', [64, 3, 4], [1, 2, 3, 4, 5], '', 1)
    EngineHoursMemo.add_parameter(DiagParameter('HoursMemo', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    Wheel_Circumference = DiagMessage(0xF039, 'Wheel_Circumference', [3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    Wheel_Circumference.add_parameter(DiagParameter('Circumference', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 1, 65535, '', False, False, False))

    WriteFingerprint = DiagMessage(0xF15A, 'WriteFingerprint', [2], [1, 3, 4, 5], '', 4)
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 4, 3, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    VehicleManufacturerSparePartNumber = DiagMessage(0xF187, 'VehicleManufacturerSparePartNumber', [64], [5], '', 1)
    VehicleManufacturerSparePartNumber.add_parameter(DiagParameter('PartNumber', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Partnumber of the electronic board (mandatory, all 0xFF --> "INVALID")', False, False, False))

    EcuSerialNumber = DiagMessage(0xF18C, 'EcuSerialNumber', [64], [5], '', 1)
    EcuSerialNumber.add_parameter(DiagParameter('SerialNumber', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 32 bytes allowed (all 0xFF --> "INVALID")', False, False, False))

    VehicleManufacturerKitAssemblyPartNumber = DiagMessage(0xF18E, 'VehicleManufacturerKitAssemblyPartNumber', [64], [5], '', 1)
    VehicleManufacturerKitAssemblyPartNumber.add_parameter(DiagParameter('AssemblyPartNumber', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Partnumber of a complete Assembly e.g. G-Nr (all 0xFF --> "INVALID")', False, False, False))

    VehicleIdentificationNumber = DiagMessage(0xF190, 'VehicleIdentificationNumber', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleIdentificationNumber.add_parameter(DiagParameter('VinNumber', 1, 0, 0, 136, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '17 bytes fixed length (all 0xFF --> "INVALID")', False, False, False))

    VehicleManufacturerECUHardwareNumber = DiagMessage(0xF191, 'VehicleManufacturerECUHardwareNumber', [64], [5], '', 1)
    VehicleManufacturerECUHardwareNumber.add_parameter(DiagParameter('VirtualPartNumber', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 4293918720, 4294967295, 'Unique feature identifier (mandatory for compatibility check hardware/software at ECU programming) ', False, False, False))

    SystemSupplierECUHardwareVersionNumber = DiagMessage(0xF193, 'SystemSupplierECUHardwareVersionNumber', [64], [5], '', 1)
    SystemSupplierECUHardwareVersionNumber.add_parameter(DiagParameter('SystemSupplierHardwareVersion', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '(optional used by ECU supplier)', False, False, False))

    VehicleManufacturerEOLProgramInfoCode = DiagMessage(0xF1A3, 'VehicleManufacturerEOLProgramInfoCode', [64], [1, 3, 4], '', 1)
    VehicleManufacturerEOLProgramInfoCode.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Name of PROGRAMMING Tool', False, False, False))

    VehicleManufacturerEOLProgramVersionCode = DiagMessage(0xF1A4, 'VehicleManufacturerEOLProgramVersionCode', [64], [1, 3, 4], '', 1)
    VehicleManufacturerEOLProgramVersionCode.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Version of PROGRAMMING Tool', False, False, False))

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))


class IC1_C3_BVIOControlDataSignals:
    pass


IC1_C3_BVDTCSnapshotdDids = {
0x1100: IC1_C3_BVReadDataSignals.FNR,
0x1101: IC1_C3_BVReadDataSignals.FNRNormallyOpen,
0x1102: IC1_C3_BVReadDataSignals.FNRNormallyClose,
0x1107: IC1_C3_BVReadDataSignals.PedalsClutch,
0x1108: IC1_C3_BVReadDataSignals.TOC,
0x1109: IC1_C3_BVReadDataSignals.BOCNO,
0x110A: IC1_C3_BVReadDataSignals.THandleMultipadPosition,
0x110B: IC1_C3_BVReadDataSignals.ThrottlePedalHand,
0x110E: IC1_C3_BVReadDataSignals.SeatSwitch,
0x110F: IC1_C3_BVReadDataSignals.HandBrakeSwitch,
0x1111: IC1_C3_BVReadDataSignals.IntermixPotentiometer,
0x1112: IC1_C3_BVReadDataSignals.MaxHeightPotentiometer,
0x1113: IC1_C3_BVReadDataSignals.DownShiftSpeedPotentiometer,
0x1114: IC1_C3_BVReadDataSignals.PTOSpeedSelectionSwitch,
0x111D: IC1_C3_BVReadDataSignals.i4WDStateMode,
0x111E: IC1_C3_BVReadDataSignals.DifflockStateMode,
0x1136: IC1_C3_BVReadDataSignals.PneumaticPressureSensor,
0x1330: IC1_C3_BVReadDataSignals.MaintenanceNextServiceHours,
0x1331: IC1_C3_BVReadDataSignals.TractorHoursOffset,
0x1332: IC1_C3_BVReadDataSignals.EngineHoursMemo,
}


class IC1_C3Client(ECUClient):
    class FlashData(Enum):
        pass

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xFC, "IC1_C3", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = IC1_C3_BVReadDataSignals
        self.write_dids = IC1_C3_BVWriteDataSignals
        self.routine_dids = IC1_C3_BVRoutineIdentifierSignals
        self.io_dids = IC1_C3_BVIOControlDataSignals
        self.dtc_snapshot_dids = IC1_C3_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

