from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class Auto5_RHS_BVRoutineIdentifierSignals:
    CheckMemoryRequest = DiagMessage(0x0202, 'CheckMemoryRequest', [2], [1, 3, 4, 5], '', 0)

    CheckMemoryResponse = DiagMessage(0x0202, 'CheckMemoryResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckMemoryResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PASSED': [0, 0], 'FAILED': [1, 1]}, 0, 1, '', False, False, False))

    CheckProgrammingPreConditionsRequest = DiagMessage(0x0203, 'CheckProgrammingPreConditionsRequest', [3], None, '', 0)

    CheckProgrammingPreConditionsResponse = DiagMessage(0x0203, 'CheckProgrammingPreConditionsResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckProgrammingPreConditionsResponse.add_parameter(DiagParameter('ProgrammingPreConditionList', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGINE_SPEED_NOT_ZERO': [1, 1], 'IMMOBILIZER_NOT_UNLOCKED': [2, 2], 'TRANSMISSION_SPEED_IN_NOT_ZERO': [3, 3], 'TRANSMISSION_SPEED_OUT_NOT_ZERO': [4, 4], 'VEHICLE_SPEED_NOT_ZERO': [5, 5], 'CONTROLLING_ACTIVE': [6, 6], 'IGNITION_OFF_ON_NECESSARY': [7, 7], 'PROGRAMMING_VOLTAGE_TOO_LOW': [8, 8], 'IGNITION_NOT_ON': [9, 9], 'VEHICLE_VOLTAGE_TOO_LOW': [10, 10], 'TEMPERATURE_TOO_HIGH': [11, 11], 'TEMPERATURE_TOO_LOW': [12, 12], 'RESERVED_BY_HIS': [13, 127], 'VEHICLE_NOT_IN_SAFE_STATE': [128, 128], 'RESERVED_BY_MANUFACTURER': [129, 191], 'RESERVED_BY_SUPPLIER': [192, 255]}, 1, 255, 'for each wrong condition 1 byte is sent, if all conditions are meet 0 bytes are transmitted', False, True, False))

    RequestCalibResult_FrontAxle = DiagMessage(0x1200, 'RequestCalibResult_FrontAxle', [3, 64], [1, 4, 5], '', 0)

    RequestCalibResult_FrontAxle_Response = DiagMessage(0x1200, 'RequestCalibResult_FrontAxle_Response', [1, 2, 3, 4, 64, 65], None, '', 1)
    RequestCalibResult_FrontAxle_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StartCalib_FrontAxle = DiagMessage(0x1200, 'StartCalib_FrontAxle', [3, 64], [1, 4, 5], '', 2)
    StartCalib_FrontAxle.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))
    StartCalib_FrontAxle.add_parameter(DiagParameter('Monitoring_Type', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Value monitoring off': [0, 0], 'Value monitoring on (ACHT result)': [1, 1], 'Progress monitoring on': [2, 2]}, 0, 2, '', False, False, False))

    StartCalib_FrontAxle_Response = DiagMessage(0x1200, 'StartCalib_FrontAxle_Response', [1, 2, 3, 4, 64, 65], None, '', 1)
    StartCalib_FrontAxle_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopCalib_FrontAxle = DiagMessage(0x1200, 'StopCalib_FrontAxle', [3, 64], [1, 4, 5], '', 1)
    StopCalib_FrontAxle.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopCalib_FrontAxle_Response = DiagMessage(0x1200, 'StopCalib_FrontAxle_Response', [1, 2, 3, 4, 64, 65], None, '', 2)
    StopCalib_FrontAxle_Response.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopCalib_FrontAxle_Response.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    RequestCalibResult_FingerTips = DiagMessage(0x1201, 'RequestCalibResult_FingerTips', [3, 64], [1, 4, 5], '', 0)

    RequestCalibResult_FingerTips_Response = DiagMessage(0x1201, 'RequestCalibResult_FingerTips_Response', [1, 2, 3, 4, 64, 65], None, '', 1)
    RequestCalibResult_FingerTips_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StartCalib_FingerTips = DiagMessage(0x1201, 'StartCalib_FingerTips', [3, 64], [1, 4, 5], '', 2)
    StartCalib_FingerTips.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))
    StartCalib_FingerTips.add_parameter(DiagParameter('Monitoring_Type', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Value monitoring off': [0, 0], 'Value monitoring on (ACHT result)': [1, 1], 'Progress monitoring on': [2, 2]}, 0, 2, '', False, False, False))

    StartCalib_FingerTips_Response = DiagMessage(0x1201, 'StartCalib_FingerTips_Response', [1, 2, 3, 4, 64, 65], None, '', 1)
    StartCalib_FingerTips_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopCalib_FingerTips = DiagMessage(0x1201, 'StopCalib_FingerTips', [3, 64], [1, 4, 5], '', 1)
    StopCalib_FingerTips.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopCalib_FingerTips_Response = DiagMessage(0x1201, 'StopCalib_FingerTips_Response', [1, 2, 3, 4, 64, 65], None, '', 2)
    StopCalib_FingerTips_Response.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopCalib_FingerTips_Response.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

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


class Auto5_RHS_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    PowerVoltage = DiagMessage(0x1061, 'PowerVoltage', [1, 2, 3], None, '', 5)
    PowerVoltage.add_parameter(DiagParameter('PowerSupplyVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('IGNSwitch', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('12VHSD6', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('10VREF', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2-S3-M1][Miscellaneous][ ][2-41][D4-D6-CVT][L-S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('5VREF', 5, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))

    AnalogInput = DiagMessage(0x1062, 'AnalogInput', [1, 2, 3], None, '', 12)
    AnalogInput.add_parameter(DiagParameter('AN1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2-S3-M1][Front_axle_susp][X166-B1F][16-AN_2][D4-D6-CVT][L-S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2-S3-M1][Cab_commands][X587][31-AN_3][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2-S3-M1][Cab_commands][X119][17-AN_4][D4-D6][L][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN5', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2-S3-M1][Cab_commands][X588][32-AN_5][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN6', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN7', 7, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN8', 8, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN9', 9, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN10', 10, 18, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2-S3-M1][Cab_commands][X121][20-AN_10][D4-D6][L][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN11', 11, 20, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN12', 12, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))

    DigitalInput = DiagMessage(0x1063, 'DigitalInput', [1, 2, 3], None, '', 15)
    DigitalInput.add_parameter(DiagParameter('FREQ1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '[1][S2-S3-M1][Cab_commands][X723][38-FRQ_1][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '[1][S3-M1][Cab_commands][X884][37-FRQ_2][D6-CVT][L-S][raw][A5_RHS][N_N][0_0]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ3', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '[1][S2-S3-M1][Cab_commands][X704][36-FRQ_3][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN1', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN2', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN3', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN4', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN5', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN6', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN7', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN8', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '[1][S3-M1][Cab_commands][X650][19-AN_8][D6-CVT][S][raw][A5_RHS][N_N][0_0]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN9', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '[1][S3-M1][Cab_commands][X650][34-AN_9][D6-CVT][S][raw][A5_RHS][N_N][0_0]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN10', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN11', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN12', 15, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NA': [3, 3]}, 0, 3, '', False, False, False))

    DigitalOutput = DiagMessage(0x1065, 'DigitalOutput', [1, 2, 3], None, '', 12)
    DigitalOutput.add_parameter(DiagParameter('HSD3', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD4', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][X153][8-HSD_4][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD5', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD6', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD7', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '[1][S2-S3-M1][Front_axle_susp][X154-Y5F][10-HSD_7][D4-D6-CVT][L-S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD8', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '[1][S2-S3-M1][Front_axle_susp][X159-Y4F][24-HSD_8][D4-D6-CVT][L-S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD9', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD10', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD11', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '[1][S2-S3-M1][Front_axle_susp][X161-Y2F][12-HSD_11][D4-D6-CVT][L-S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD12', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands_state][X918][26-HSD_12][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD13', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands_state][X704][13-HSD_13][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD14', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '', False, False, False))

    AnalogOutput = DiagMessage(0x1066, 'AnalogOutput', [1, 2, 3], None, '', 6)
    AnalogOutput.add_parameter(DiagParameter('HSD1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2-S3-M1][Miscellaneous][X153][5-HSD_1][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2-S3-M1][Miscellaneous][X153][6-HSD_2][D4-D6-CVT][L-S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD5', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2-S3-M1][Miscellaneous][X153][22-HSD_5][D4-D6-CVT][L-S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD6', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2-S3-M1][Miscellaneous][X153][23-HSD_6][D4-D6-CVT][S][raw][A5_RHS][N_N_N][0_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD7', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD8', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))

    FrontAxleCalibrationState = DiagMessage(0x1100, 'FrontAxleCalibrationState', [1, 3, 4, 64], None, '', 1)
    FrontAxleCalibrationState.add_parameter(DiagParameter('FrontAxleCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    FingerTipsCalibrationState = DiagMessage(0x1101, 'FingerTipsCalibrationState', [1, 3, 4, 64], None, '', 1)
    FingerTipsCalibrationState.add_parameter(DiagParameter('FingerTipsCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    HYD_SwitchActivation = DiagMessage(0x1102, 'HYD_SwitchActivation', [1, 3, 4, 64], None, '', 1)
    HYD_SwitchActivation.add_parameter(DiagParameter('HYD_SwitchActivation', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[Y]', False, False, False))

    HYD_SwitchFrontRear = DiagMessage(0x1103, 'HYD_SwitchFrontRear', [1, 3, 4, 64], None, '', 1)
    HYD_SwitchFrontRear.add_parameter(DiagParameter('HYD_SwitchFrontRear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[Y]', False, False, False))

    HYD_LevierFT3Status = DiagMessage(0x1104, 'HYD_LevierFT3Status', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT3Status.add_parameter(DiagParameter('HYD_LevierFT3Status', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'EXTEND': [0, 0], 'RETRACT': [1, 1], 'NEUTRAL': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '[1][S2-S3-M1][Cab_commands][X587][31-AN_3][D4-D6-CVT][S][conv][A5_RHS][Y_N_N][2_0_0]', False, False, False))

    HITCH_SwitchUpNeuDown = DiagMessage(0x1105, 'HITCH_SwitchUpNeuDown', [1, 2, 3, 4, 64], None, '', 1)
    HITCH_SwitchUpNeuDown.add_parameter(DiagParameter('HITCH_SwitchUpNeuDown', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'UP': [0, 0], 'NEUTRAL': [1, 1], 'DOWN': [2, 2]}, 0, 2, '[Y]', False, False, False))

    HYD_LevierFT4Status = DiagMessage(0x1106, 'HYD_LevierFT4Status', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT4Status.add_parameter(DiagParameter('HYD_LevierFT4Status', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'EXTEND': [0, 0], 'RETRACT': [1, 1], 'NEUTRAL': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '[1][S2-S3-M1][Cab_commands][X588][32-AN_5][D4-D6-CVT][S][conv][A5_RHS][Y_N_N][2_0_0]', False, False, False))

    HITCH_DepthPotentiometer = DiagMessage(0x1107, 'HITCH_DepthPotentiometer', [1, 3, 4, 64], None, '', 1)
    HITCH_DepthPotentiometer.add_parameter(DiagParameter('HITCH_DepthPotentiometer', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[Y]', False, False, False))

    LOADER_SwitchActivation = DiagMessage(0x1108, 'LOADER_SwitchActivation', [1, 3, 4, 64], None, '', 1)
    LOADER_SwitchActivation.add_parameter(DiagParameter('LOADER_SwitchActivation', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S3-M1][Functions_state][ ][ ][D6-CVT][L-S][raw][A5_RHS][Y_N][0_0]', False, False, False))

    HYD_LevierFT6Status = DiagMessage(0x1109, 'HYD_LevierFT6Status', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT6Status.add_parameter(DiagParameter('HYD_LevierFT6Status', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'EXTEND': [0, 0], 'RETRACT': [1, 1], 'NEUTRAL': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '[1][S3-M1][Cab_commands][X110][18-AN_6][D6-CVT][L-S][conv][A5_RHS][Y_N][0_0]', False, False, False))

    HYD_LevierFT3Percent = DiagMessage(0x110A, 'HYD_LevierFT3Percent', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT3Percent.add_parameter(DiagParameter('HYD_LevierFT3Percent', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Cab_commands][X587][31-AN_3][D4-D6-CVT][S][conv][A5_RHS][Y_N_N][1_0_0]', False, False, False))

    HYD_LevierFT4Percent = DiagMessage(0x110B, 'HYD_LevierFT4Percent', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT4Percent.add_parameter(DiagParameter('HYD_LevierFT4Percent', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Cab_commands][X588][32-AN_5][D4-D6-CVT][S][conv][A5_RHS][Y_N_N][1_0_0]', False, False, False))

    HYD_LevierFT6Percent = DiagMessage(0x110C, 'HYD_LevierFT6Percent', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT6Percent.add_parameter(DiagParameter('HYD_LevierFT6Percent', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S3-M1][Cab_commands][X110][18-AN_6][D6-CVT][L-S][conv][A5_RHS][Y_N][0_0]', False, False, False))

    HYD_LevierFT8Status = DiagMessage(0x110D, 'HYD_LevierFT8Status', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT8Status.add_parameter(DiagParameter('HYD_LevierFT8Status', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'EXTEND': [0, 0], 'RETRACT': [1, 1], 'NEUTRAL': [2, 2], 'FLOAT': [4, 4]}, 0, 4, '[1][S3-M1][Cab_commands][X883][35-AN_11][D6-CVT][L-S][conv][A5_RHS][Y_N][0_0]', False, False, False))

    HYD_LevierFT7Status = DiagMessage(0x110E, 'HYD_LevierFT7Status', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT7Status.add_parameter(DiagParameter('HYD_LevierFT7Status', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'EXTEND': [0, 0], 'RETRACT': [1, 1], 'NEUTRAL': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '[1][S3-M1][Cab_commands][X882][33-AN_7][D6-CVT][L-S][conv][A5_RHS][Y_N][0_0]', False, False, False))

    HYD_SwitchMemorizationStep = DiagMessage(0x110F, 'HYD_SwitchMemorizationStep', [1, 3, 4, 64], None, '', 1)
    HYD_SwitchMemorizationStep.add_parameter(DiagParameter('HYD_SwitchMemorizationStep', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[Y]', False, False, False))

    HYD_SwitchMemorizationInst = DiagMessage(0x1110, 'HYD_SwitchMemorizationInst', [1, 3, 4, 64], None, '', 1)
    HYD_SwitchMemorizationInst.add_parameter(DiagParameter('HYD_SwitchMemorizationInst', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[Y]', False, False, False))

    HYD_LevierFT7Percent = DiagMessage(0x1111, 'HYD_LevierFT7Percent', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT7Percent.add_parameter(DiagParameter('HYD_LevierFT7Percent', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S3-M1][Cab_commands][X882][33-AN_7][D6-CVT][L-S][conv][A5_RHS][Y_N][0_0]', False, False, False))

    HYD_LevierFT8Percent = DiagMessage(0x1112, 'HYD_LevierFT8Percent', [1, 3, 4, 64], None, '', 1)
    HYD_LevierFT8Percent.add_parameter(DiagParameter('HYD_LevierFT8Percent', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S3-M1][Cab_commands][X883][35-AN_11][D6-CVT][L-S][conv][A5_RHS][Y_N][0_0]', False, False, False))

    FAXLESUSP_DisplayFrontAxleSusp = DiagMessage(0x1113, 'FAXLESUSP_DisplayFrontAxleSusp', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_DisplayFrontAxleSusp.add_parameter(DiagParameter('FAXLESUSP_DisplayFrontAxleSusp', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[Y]', False, False, False))

    FAXLESUSP_Height = DiagMessage(0x1114, 'FAXLESUSP_Height', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_Height.add_parameter(DiagParameter('FAXLESUSP_Height', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[Y]', False, False, False))

    FAXLESUSP_ControlStatus = DiagMessage(0x1115, 'FAXLESUSP_ControlStatus', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_ControlStatus.add_parameter(DiagParameter('FAXLESUSP_ControlStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[Y]', False, False, False))

    FAXLESUSP_Position = DiagMessage(0x1116, 'FAXLESUSP_Position', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_Position.add_parameter(DiagParameter('FAXLESUSP_Position', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Front_axle_susp][X166-B1F][16-AN_2][D4-D6-CVT][L-S][conv][A5_RHS][Y_N_N][1_0_0]', False, False, False))

    REAR_PowerLift = DiagMessage(0x1118, 'REAR_PowerLift', [1, 3, 4, 64], None, '', 2)
    REAR_PowerLift.add_parameter(DiagParameter('Lifting_Lowering_sw', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 65535, '[1][S2-S3-M1][Cab_commands][X119][17-AN_4][D4-D6][L][conv][A5_RHS][Y_N_N][2_0_0]', False, False, False))
    REAR_PowerLift.add_parameter(DiagParameter('Height_Depth_ajustement_thumb', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Cab_commands][X121][20-AN_10][D4-D6][L][conv][A5_RHS][N_N_N][2_0_0]', False, False, False))

    HYD_FlowRateMemo_sw = DiagMessage(0x1119, 'HYD_FlowRateMemo_sw', [1, 3, 4, 64], None, '', 2)
    HYD_FlowRateMemo_sw.add_parameter(DiagParameter('Switch_1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S3-M1][Cab_commands][X650][19-AN_8][D6-CVT][S][conv][A5_RHS][N_N][0_0]', False, False, False))
    HYD_FlowRateMemo_sw.add_parameter(DiagParameter('Switch_2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S3-M1][Cab_commands][X650][34-AN_9][D6-CVT][S][conv][A5_RHS][N_N][0_0]', False, False, False))

    HYD_auxiliary_locking_sw = DiagMessage(0x111A, 'HYD_auxiliary_locking_sw', [1, 3, 4, 64], None, '', 1)
    HYD_auxiliary_locking_sw.add_parameter(DiagParameter('Auxiliary_locking_sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X704][36-FRQ_3][D4-D6-CVT][S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))

    LOADER_function_selector_sw = DiagMessage(0x111B, 'LOADER_function_selector_sw', [1, 3, 4, 64], None, '', 1)
    LOADER_function_selector_sw.add_parameter(DiagParameter('Function_selector_sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X723][38-FRQ_1][D4-D6-CVT][S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))

    HYD_SpoolValve_Control_sw = DiagMessage(0x111C, 'HYD_SpoolValve_Control_sw', [1, 3, 4, 64], None, '', 1)
    HYD_SpoolValve_Control_sw.add_parameter(DiagParameter('SpoolValve_Control_sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S3-M1][Cab_commands][X884][37-FRQ_2][D6-CVT][L-S][conv][A5_RHS][N_N][0_0]', False, False, False))

    NON_ISOBUS_Socket = DiagMessage(0x111D, 'NON_ISOBUS_Socket', [1, 3, 4, 64], None, '', 5)
    NON_ISOBUS_Socket.add_parameter(DiagParameter('Rear_linkage_position_signal', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Miscellaneous][X153][5-HSD_1][D4-D6-CVT][S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))
    NON_ISOBUS_Socket.add_parameter(DiagParameter('Theorical_speed', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'km/h', 0, 255, '[1][S2-S3-M1][Miscellaneous][X153][6-HSD_2][D4-D6-CVT][L-S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))
    NON_ISOBUS_Socket.add_parameter(DiagParameter('Rear_Linkage_signal', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'TRANSPORT_POSITION': [0, 0], 'WORK_POSITION': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][X153][8-HSD_4][D4-D6-CVT][S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))
    NON_ISOBUS_Socket.add_parameter(DiagParameter('Actual_speed', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'km/h', 0, 255, '[1][S2-S3-M1][Miscellaneous][X153][22-HSD_5][D4-D6-CVT][L-S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))
    NON_ISOBUS_Socket.add_parameter(DiagParameter('RearPTO_rotational_speed_signal', 5, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'rpm', 0, 65535, '[1][S2-S3-M1][Miscellaneous][X153][23-HSD_6][D4-D6-CVT][S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))

    FAXLESUSP_Suspension = DiagMessage(0x1120, 'FAXLESUSP_Suspension', [1, 3, 4, 64], None, '', 3)
    FAXLESUSP_Suspension.add_parameter(DiagParameter('Lock_EV', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Front_axle_susp][X154-Y5F][10-HSD_7][D4-D6-CVT][L-S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))
    FAXLESUSP_Suspension.add_parameter(DiagParameter('Lowering_EV', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Front_axle_susp][X159-Y4F][24-HSD_8][D4-D6-CVT][L-S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))
    FAXLESUSP_Suspension.add_parameter(DiagParameter('Lifting_EV', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Front_axle_susp][X161-Y2F][12-HSD_11][D4-D6-CVT][L-S][conv][A5_RHS][N_N_N][0_0_0]', False, False, False))

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

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [1, 2, 3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [1, 2, 3, 4, 64], None, '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [1, 2, 3, 4, 64], None, '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class Auto5_RHS_BVWriteDataSignals:
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

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class Auto5_RHS_BVIOControlDataSignals:
    pass


Auto5_RHS_BVDTCSnapshotdDids = {
}


class Auto5_RHSClient(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0x00FC0000, 00, 32, 32, erase_address=0x00FC0000, erase_size=None,
                               path_to_file="C:\Python38\Lib\site-packages\agco_diagnostic\massey\ecus_uds\output.hex",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(Auto5_RHS_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   Auto5_RHS_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False),

                MemoryLocation(0x00FD0000, 00, 32, 32, erase_address=0x00FD0000, erase_size=None,
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(Auto5_RHS_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   Auto5_RHS_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False),

                MemoryLocation(0x00FF4000, 00, 32, 32, erase_address=0x00FF4000, erase_size=None,
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(Auto5_RHS_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   Auto5_RHS_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False),

                MemoryLocation(0x00FF7E40, 00, 32, 32, erase_address=0x00FF7E40, erase_size=None,
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(Auto5_RHS_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   Auto5_RHS_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xDD, "Auto5_RHS", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=2, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = Auto5_RHS_BVReadDataSignals
        self.write_dids = Auto5_RHS_BVWriteDataSignals
        self.routine_dids = Auto5_RHS_BVRoutineIdentifierSignals
        self.io_dids = Auto5_RHS_BVIOControlDataSignals
        self.dtc_snapshot_dids = Auto5_RHS_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

