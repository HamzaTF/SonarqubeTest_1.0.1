from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class A5_REH_APP137_BVRoutineIdentifierSignals:
    CheckMemoryRequest = DiagMessage(0x0202, 'CheckMemoryRequest', [2], [1, 3, 4, 5], '', 0)

    CheckMemoryResponse = DiagMessage(0x0202, 'CheckMemoryResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckMemoryResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PASSED': [0, 0], 'FAILED': [1, 1]}, 0, 1, '', False, False, False))

    CheckProgrammingPreConditionsRequest = DiagMessage(0x0203, 'CheckProgrammingPreConditionsRequest', [3], None, '', 0)

    CheckProgrammingPreConditionsResponse = DiagMessage(0x0203, 'CheckProgrammingPreConditionsResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckProgrammingPreConditionsResponse.add_parameter(DiagParameter('ProgrammingPreConditionList', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGINE_SPEED_NOT_ZERO': [1, 1], 'IMMOBILIZER_NOT_UNLOCKED': [2, 2], 'TRANSMISSION_SPEED_IN_NOT_ZERO': [3, 3], 'TRANSMISSION_SPEED_OUT_NOT_ZERO': [4, 4], 'VEHICLE_SPEED_NOT_ZERO': [5, 5], 'CONTROLLING_ACTIVE': [6, 6], 'IGNITION_OFF_ON_NECESSARY': [7, 7], 'PROGRAMMING_VOLTAGE_TOO_LOW': [8, 8], 'IGNITION_NOT_ON': [9, 9], 'VEHICLE_VOLTAGE_TOO_LOW': [10, 10], 'TEMPERATURE_TOO_HIGH': [11, 11], 'TEMPERATURE_TOO_LOW': [12, 12], 'RESERVED_BY_HIS': [13, 127], 'VEHICLE_NOT_IN_SAFE_STATE': [128, 128], 'RESERVED_BY_MANUFACTURER': [129, 191], 'RESERVED_BY_SUPPLIER': [192, 255]}, 1, 255, 'for each wrong condition 1 byte is sent, if all conditions are meet 0 bytes are transmitted', False, True, False))

    ResultRequestREHCalibrationRequest = DiagMessage(0xF204, 'ResultRequestREHCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestREHCalibrationResponse = DiagMessage(0xF204, 'ResultRequestREHCalibrationResponse', [3, 4, 64], [1, 4, 5], '', 4)
    ResultRequestREHCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    ResultRequestREHCalibrationResponse.add_parameter(DiagParameter('ErrorCode', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ResultRequestREHCalibrationResponse.add_parameter(DiagParameter('ProgressValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))
    ResultRequestREHCalibrationResponse.add_parameter(DiagParameter('ResultValue', 4, 4, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -32768, 32767, '', False, False, False))

    StartREHCalibrationRequest = DiagMessage(0xF204, 'StartREHCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartREHCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartREHCalibrationResponse = DiagMessage(0xF204, 'StartREHCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StartREHCalibrationResponse.add_parameter(DiagParameter('State', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    StartREHCalibrationResponse.add_parameter(DiagParameter('Nb_Steps', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    StopREHCalibrationRequest = DiagMessage(0xF204, 'StopREHCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    StopREHCalibrationResponse = DiagMessage(0xF204, 'StopREHCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StopREHCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))

    ResultRequestLeverCalibrationRequest = DiagMessage(0xF205, 'ResultRequestLeverCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestLeverCalibrationResponse = DiagMessage(0xF205, 'ResultRequestLeverCalibrationResponse', [3, 4, 64], [1, 4, 5], '', 4)
    ResultRequestLeverCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    ResultRequestLeverCalibrationResponse.add_parameter(DiagParameter('ErrorCode', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ResultRequestLeverCalibrationResponse.add_parameter(DiagParameter('ProgressValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))
    ResultRequestLeverCalibrationResponse.add_parameter(DiagParameter('ResultValue', 4, 4, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -32768, 32767, '', False, False, False))

    StartLeverCalibrationRequest = DiagMessage(0xF205, 'StartLeverCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartLeverCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartLeverCalibrationResponse = DiagMessage(0xF205, 'StartLeverCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StartLeverCalibrationResponse.add_parameter(DiagParameter('State', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    StartLeverCalibrationResponse.add_parameter(DiagParameter('Nb_Steps', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    StopLeverCalibrationRequest = DiagMessage(0xF205, 'StopLeverCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    StopLeverCalibrationResponse = DiagMessage(0xF205, 'StopLeverCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StopLeverCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))

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


class A5_REH_APP137_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    PowerVoltage = DiagMessage(0x1061, 'PowerVoltage', [1, 2, 3], None, '', 4)
    PowerVoltage.add_parameter(DiagParameter('PowerSupplyVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][ ][14-42][D4][Base][raw][A5_137][Y][1]', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('IGNSwitch', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('12VHSD6', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('10VREF', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][ ][2][D4][Base][raw][A5_137][Y][1]', False, False, False))

    AnalogInput = DiagMessage(0x1062, 'AnalogInput', [1, 2, 3], None, '', 12)
    AnalogInput.add_parameter(DiagParameter('AN1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][C3R_20-C3R_21][Linkage][X30][30-AN_1][D4][Base][raw][A5_137][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][C3R_20-C3R_21][Linkage][X32][16-AN_2][D4][Base][raw][A5_137][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN5', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN6', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN7', 7, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][X97][20-AN_10][D4][Base][raw][A5_137][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN8', 8, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][X363][19-AN_8][D4][Base][raw][A5_137][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN9', 9, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][X751][34-AN_9][D4][Base][raw][A5_137][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN10', 10, 18, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN11', 11, 20, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN12', 12, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))

    DigitalInput = DiagMessage(0x1063, 'DigitalInput', [1, 2, 3], None, '', 15)
    DigitalInput.add_parameter(DiagParameter('FREQ1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ3', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN1', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN2', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN3', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN4', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN5', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X128][32-AN_5][D4][Base][raw][A5_137][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN6', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X128][18-AN_6][D4][Base][raw][A5_137][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN7', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X913][33-AN_7][D4][Base][raw][A5_137][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN8', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN9', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN10', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN11', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][X75][35-AN_11][D4][Base][raw][A5_137][Y][0]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN12', 15, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))

    FreqInput = DiagMessage(0x1064, 'FreqInput', [1, 2, 3], None, '', 3)
    FreqInput.add_parameter(DiagParameter('FREQ1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X482][38-FRQ_1][D4][Base][raw][A5_137][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][C3R_20-C3R_21][PTO][X777][37-FRQ_2][D4][Base][raw][A5_137][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][C3R_20-C3R_21][PTO][X776][36-FRQ_3][D4][Base][raw][A5_137][Y][1]', False, False, False))

    DigitalOutput = DiagMessage(0x1065, 'DigitalOutput', [1, 2, 3], None, '', 12)
    DigitalOutput.add_parameter(DiagParameter('HSD3', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands][ ][7-HSD_3][D4][Base][raw][A5_137][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD4', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD5', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD6', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD7', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD8', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD9', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Braking_system][X987][11-HSD_9][D4][Base][conv][A5_137][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD10', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands_state][X913][25-HSD_10][D4][Base][raw][A5_137][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD11', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][PTO][X498][12-HSD_11][D4][Base][raw][A5_137][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD12', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Linkage][X727][26-HSD_12][D4][Base][raw][A5_137][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD13', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Miscellaneous][K7][13-HSD_13][D4][Base][raw][A5_137][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD14', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Cab_commands_state][X934][27-HSD_14][D4][Base][raw][A5_137][Y][1]', False, False, False))

    AnalogOutput = DiagMessage(0x1066, 'AnalogOutput', [1, 2, 3], None, '', 6)
    AnalogOutput.add_parameter(DiagParameter('HSD1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][C3R_20-C3R_21][Linkage][X28][5-HSD_1][D4][Base][raw][A5_137][Y][1]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][C3R_20-C3R_21][Linkage][X27][6-HSD_2][D4][Base][raw][A5_137][Y][2]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD5', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD6', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][C3R_20-C3R_21][PTO][X16][23-HSD_6][D4][Base][raw][A5_137][Y][1]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD7', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD8', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))

    FnPto = DiagMessage(0x1067, 'FnPto', [1, 2, 3], None, '', 20)
    FnPto.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    FnPto.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoCommandCabin', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X128][18-AN_6][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoCommandStop', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X128][32-AN_5][D4][Base][conv][A5_137][Y][2]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoCommandFenderStart', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X75][35-AN_11][D4][Base][conv][A5_137][Y][0]', False, False, False))
    FnPto.add_parameter(DiagParameter('Ops', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('EngineSpeed', 9, 9, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoState', 10, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PTO_OFF': [0, 0], 'PTO_INIT': [1, 1], 'PTO_FILLING': [2, 2], 'PTO_START': [3, 3], 'PTO_PULSING': [4, 4], 'PTO_ON': [5, 5], 'PTO_SENSORS_OFF': [6, 6], 'PTO_ALARM': [7, 7], 'PTO_FENDER': [8, 8], 'STATE_PTO_EV_ON_OFF': [9, 9]}, 0, 9, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoSpeed', 11, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '[1][C3R_20-C3R_21][PTO][X777][37-FRQ_2][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoEnergy', 12, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    FnPto.add_parameter(DiagParameter('GsptoSwitch', 13, 16, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('GsptoCommand', 14, 17, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('EVGspto', 15, 18, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('VehicleSpeedWheel', 16, 19, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X482][38-FRQ_1][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoShaftSpeed', 17, 21, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '[1][C3R_20-C3R_21][PTO][X776][36-FRQ_3][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('EVBrake', 18, 23, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][PTO][X498][12-HSD_11][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoPwm', 19, 24, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoBrake', 20, 25, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    FctRearHitchCommand = DiagMessage(0x1069, 'FctRearHitchCommand', [1, 2, 3], None, '', 22)
    FctRearHitchCommand.add_parameter(DiagParameter('ProportionalValveSetPointCurrent', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][C3R_20-C3R_21][Linkage][X27][6-HSD_2][D4][Base][conv][A5_137][Y][2]', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('WheelSpeed', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'kph', 0, 60000, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('FunctionAvailable', 3, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('PowerSupplyVoltage', 4, 5, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 10000, 16000, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('EngineRunning', 5, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('ErrorActive', 6, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('LiftingCommand', 7, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('loweringCommand', 8, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X97][20-AN_10][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('ExternalCmd', 9, 11, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('IntCommand', 10, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'low': [1, 1], 'low to neutral': [2, 2], 'neutral to low': [3, 3], 'neutral': [4, 4], 'neutral to high': [5, 5], 'high to neutral': [6, 6], 'high': [7, 7]}, 1, 7, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('HitchRearPosActVal', 11, 13, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('SettingPosition', 12, 14, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('LoweringValveMeasureCurrent', 13, 15, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('LoweringValveMeasureCurrent', 14, 17, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 5000, '[1][C3R_20-C3R_21][Linkage][X27][3-HSD_2_cs][D4][Base][raw][A5_137][Y][1]', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('Command98L', 15, 19, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X913][33-AN_7][D4][Base][conv][A5_137][Y][2]', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('98LValveControl', 16, 20, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Linkage][X727][26-HSD_12][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('MeasureLeftDraft', 17, 21, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 2000, 8000, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('MeasureRightDraft', 18, 23, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 2000, 8000, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('SignalLeftDraftTonne', 19, 25, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -9.0, 0.001, 't', 0, 18000, '[1][C3R_20-C3R_21][Linkage][X32][16-AN_2][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('SignalRightDraftTonne', 20, 27, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -9.0, 0.001, 't', 0, 18000, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('EVLoweringHusco', 21, 29, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctRearHitchCommand.add_parameter(DiagParameter('LinkageMode', 22, 30, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C3R_20-C3R_21][Functions_state][ ][ ][D4][Base][conv][A5_137][Y][2]', False, False, False))

    FctHitchInput = DiagMessage(0x106A, 'FctHitchInput', [1, 2, 3], None, '', 9)
    FctHitchInput.add_parameter(DiagParameter('SettingPosition', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][C3R_20-C3R_21][Cab_commands][X751][34-AN_9][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FctHitchInput.add_parameter(DiagParameter('SettingDraftSensibility', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    FctHitchInput.add_parameter(DiagParameter('SettingUpperLimit', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 50, 100, '', False, False, False))
    FctHitchInput.add_parameter(DiagParameter('SettingLoweringSpeed', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    FctHitchInput.add_parameter(DiagParameter('Switch3Postion', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'low': [1, 1], 'low to neutral': [2, 2], 'neutral to low': [3, 3], 'neutral': [4, 4], 'neutral to high': [5, 5], 'high to neutral': [6, 6], 'high': [7, 7]}, 1, 7, '[1][C3R_20-C3R_21][Cab_commands][X363][19-AN_8][D4][Base][conv][A5_137][Y][2]', False, False, False))
    FctHitchInput.add_parameter(DiagParameter('DampingSwitch', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctHitchInput.add_parameter(DiagParameter('Command98L', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctHitchInput.add_parameter(DiagParameter('QuickSoilengagement', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Linkage][ ][ ][D4][Base][conv][A5_137][Y][1]', False, False, False))
    FctHitchInput.add_parameter(DiagParameter('SettingSlipage', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 50, '', False, False, False))

    FctEHS = DiagMessage(0x106B, 'FctEHS', [1, 2, 3], None, '', 14)
    FctEHS.add_parameter(DiagParameter('EhsMode0', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'VERROUILLE': [0, 0], 'PROPORTIONNEL': [1, 1], 'KICKOUT': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsSortie0', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsMode1', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'VERROUILLE': [0, 0], 'PROPORTIONNEL': [1, 1], 'KICKOUT': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsSortie1', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsMode2', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'VERROUILLE': [0, 0], 'PROPORTIONNEL': [1, 1], 'KICKOUT': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsSortie2', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsMode3', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'VERROUILLE': [0, 0], 'PROPORTIONNEL': [1, 1], 'KICKOUT': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsSortie3', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsMode4', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'VERROUILLE': [0, 0], 'PROPORTIONNEL': [1, 1], 'KICKOUT': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsSortie4', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsMode5', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'VERROUILLE': [0, 0], 'PROPORTIONNEL': [1, 1], 'KICKOUT': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsSortie5', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsMode6', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'VERROUILLE': [0, 0], 'PROPORTIONNEL': [1, 1], 'KICKOUT': [2, 2], 'FLOAT': [3, 3]}, 0, 3, '', False, False, False))
    FctEHS.add_parameter(DiagParameter('EhsSortie6', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    FnParklock = DiagMessage(0x1072, 'FnParklock', [1, 2, 3], None, '', 8)
    FnParklock.add_parameter(DiagParameter('Switch_Usure_PK1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnParklock.add_parameter(DiagParameter('Switch_onoff', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnParklock.add_parameter(DiagParameter('Command_PL', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnParklock.add_parameter(DiagParameter('EV_Road', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnParklock.add_parameter(DiagParameter('EV_Park', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnParklock.add_parameter(DiagParameter('ShuttleShiftStatus', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    FnParklock.add_parameter(DiagParameter('TransOilTemperature', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?C', 0, 200, '', False, False, False))
    FnParklock.add_parameter(DiagParameter('Vehicle_speed', 8, 7, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '', False, False, False))

    Test_Monitoring_DID = DiagMessage(0x1100, 'Test_Monitoring_DID', [], None, '', 2)
    Test_Monitoring_DID.add_parameter(DiagParameter('TestSignal1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -125.0, 1.0, '', -125, 125, '', False, False, False))
    Test_Monitoring_DID.add_parameter(DiagParameter('TestSignal2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -125.0, 1.0, '', -125, 125, '', False, False, False))

    RID_Example = DiagMessage(0x1200, 'RID_Example', [], None, '', 1)
    RID_Example.add_parameter(DiagParameter('RoutineOptionRecord', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DID_Example_Configuration = DiagMessage(0xCF00, 'DID_Example_Configuration', [], None, '', 1)
    DID_Example_Configuration.add_parameter(DiagParameter('Optional_Feature_1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'used for Configuration of a ECU', False, False, False))

    ECU_PIN = DiagMessage(0xF100, 'ECU_PIN', [1, 2, 3], None, '', 1)
    ECU_PIN.add_parameter(DiagParameter('Pin_number', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    ECU_Cheksum = DiagMessage(0xF101, 'ECU_Cheksum', [1, 2, 3], None, '', 2)
    ECU_Cheksum.add_parameter(DiagParameter('CurrentChecksum', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    ECU_Cheksum.add_parameter(DiagParameter('StoredChecksum', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    ECU_SoftwareIdentification = DiagMessage(0xF102, 'ECU_SoftwareIdentification', [1, 2, 3], None, '', 5)
    ECU_SoftwareIdentification.add_parameter(DiagParameter('SoftwareVersionOperatingSystem', 1, 0, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    ECU_SoftwareIdentification.add_parameter(DiagParameter('SoftwareVersionMicroControler', 2, 3, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    ECU_SoftwareIdentification.add_parameter(DiagParameter('SoftwareVersionLanguage', 3, 6, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    ECU_SoftwareIdentification.add_parameter(DiagParameter('SoftwareVersionFree3', 4, 9, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    ECU_SoftwareIdentification.add_parameter(DiagParameter('SoftwareVersionFree4', 5, 12, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    ECU_FbIQuestion = DiagMessage(0xF103, 'ECU_FbIQuestion', [1, 2, 3], None, '', 2)
    ECU_FbIQuestion.add_parameter(DiagParameter('FbIQuestion', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    ECU_FbIQuestion.add_parameter(DiagParameter('Reserved', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    ECU_SoftwareDetails = DiagMessage(0xF104, 'ECU_SoftwareDetails', [1, 2, 3], None, '', 5)
    ECU_SoftwareDetails.add_parameter(DiagParameter('CANdescVersion', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_2', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_3', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_4', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_5', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    SupplierCode = DiagMessage(0xF105, 'SupplierCode', [1, 2, 3], None, '', 1)
    SupplierCode.add_parameter(DiagParameter('SupplierCode', 1, 0, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

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

    ECUHardwareVersionNumber = DiagMessage(0xF193, 'ECUHardwareVersionNumber', [1, 2, 3], None, '', 2)
    ECUHardwareVersionNumber.add_parameter(DiagParameter('ECUHardwareVersionNumber', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    ECUHardwareVersionNumber.add_parameter(DiagParameter('New_Data_Object_8', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -125.0, 1.0, '', 0, 255, '', False, False, False))

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [1, 2, 3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [1, 2, 3, 4, 64], None, '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [1, 2, 3, 4, 64], None, '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))

    DID_Example_ECU_Identification = DiagMessage(0xF1B0, 'DID_Example_ECU_Identification', [], None, '', 1)
    DID_Example_ECU_Identification.add_parameter(DiagParameter('ECU_Identification_Test', 1, 0, 0, 88, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'used for additional ECU specific Identification ', False, False, False))

    CalibrationState_CabLeverHitchRear = DiagMessage(0xFE00, 'CalibrationState_CabLeverHitchRear', [1, 3, 4, 64], None, '', 1)
    CalibrationState_CabLeverHitchRear.add_parameter(DiagParameter('CalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    CalibrationState_HitchRear = DiagMessage(0xFE01, 'CalibrationState_HitchRear', [1, 3, 4, 64], None, '', 1)
    CalibrationState_HitchRear.add_parameter(DiagParameter('CalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))


class A5_REH_APP137_BVWriteDataSignals:
    WriteFingerprint = DiagMessage(0xF15A, 'WriteFingerprint', [2], [1, 3, 4, 5], '', 4)
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 4, 3, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    VehicleManufacturerSparePartNumber = DiagMessage(0xF187, 'VehicleManufacturerSparePartNumber', [64], [5], '', 1)
    VehicleManufacturerSparePartNumber.add_parameter(DiagParameter('PartNumber', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Partnumber of the electronic board (mandatory, all 0xFF --> "INVALID")', False, False, False))

    VehicleManufacturerKitAssemblyPartNumber = DiagMessage(0xF18E, 'VehicleManufacturerKitAssemblyPartNumber', [64], [5], '', 1)
    VehicleManufacturerKitAssemblyPartNumber.add_parameter(DiagParameter('AssemblyPartNumber', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Partnumber of a complete Assembly e.g. G-Nr (all 0xFF --> "INVALID")', False, False, False))

    VehicleIdentificationNumber = DiagMessage(0xF190, 'VehicleIdentificationNumber', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleIdentificationNumber.add_parameter(DiagParameter('VinNumber', 1, 0, 0, 136, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '17 bytes fixed length (all 0xFF --> "INVALID")', False, False, False))

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class A5_REH_APP137_BVIOControlDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [4], [4], '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))


A5_REH_APP137_BVDTCSnapshotdDids = {
}


class A5_REH_APP137Client(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0xFC0000, 0x0, 32, 32, erase_address=0xFC0000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_RHITCH\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_REH_APP137_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_REH_APP137_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4000, 0x0, 32, 32, erase_address=0xFF4000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_RHITCH\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_REH_APP137_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_REH_APP137_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4940, 0x0, 32, 32, erase_address=0xFF4940, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_RHITCH\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_REH_APP137_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_REH_APP137_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF7E40, 0x0, 32, 32, erase_address=0xFF7E40, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_RHITCH\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_REH_APP137_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_REH_APP137_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xEB, "A5_REH_APP137", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A5_REH_APP137_BVReadDataSignals
        self.write_dids = A5_REH_APP137_BVWriteDataSignals
        self.routine_dids = A5_REH_APP137_BVRoutineIdentifierSignals
        self.io_dids = A5_REH_APP137_BVIOControlDataSignals
        self.dtc_snapshot_dids = A5_REH_APP137_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

