from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class A5_ISC_APP138_BVRoutineIdentifierSignals:
    CheckMemoryRequest = DiagMessage(0x0202, 'CheckMemoryRequest', [2], [1, 3, 4, 5], '', 0)

    CheckMemoryResponse = DiagMessage(0x0202, 'CheckMemoryResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckMemoryResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PASSED': [0, 0], 'FAILED': [1, 1]}, 0, 1, '', False, False, False))

    CheckProgrammingPreConditionsRequest = DiagMessage(0x0203, 'CheckProgrammingPreConditionsRequest', [3], None, '', 0)

    CheckProgrammingPreConditionsResponse = DiagMessage(0x0203, 'CheckProgrammingPreConditionsResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckProgrammingPreConditionsResponse.add_parameter(DiagParameter('ProgrammingPreConditionList', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGINE_SPEED_NOT_ZERO': [1, 1], 'IMMOBILIZER_NOT_UNLOCKED': [2, 2], 'TRANSMISSION_SPEED_IN_NOT_ZERO': [3, 3], 'TRANSMISSION_SPEED_OUT_NOT_ZERO': [4, 4], 'VEHICLE_SPEED_NOT_ZERO': [5, 5], 'CONTROLLING_ACTIVE': [6, 6], 'IGNITION_OFF_ON_NECESSARY': [7, 7], 'PROGRAMMING_VOLTAGE_TOO_LOW': [8, 8], 'IGNITION_NOT_ON': [9, 9], 'VEHICLE_VOLTAGE_TOO_LOW': [10, 10], 'TEMPERATURE_TOO_HIGH': [11, 11], 'TEMPERATURE_TOO_LOW': [12, 12], 'RESERVED_BY_HIS': [13, 127], 'VEHICLE_NOT_IN_SAFE_STATE': [128, 128], 'RESERVED_BY_MANUFACTURER': [129, 191], 'RESERVED_BY_SUPPLIER': [192, 255]}, 1, 255, 'for each wrong condition 1 byte is sent, if all conditions are meet 0 bytes are transmitted', False, True, False))

    ResultRequestIscCalibrationRequest = DiagMessage(0xF201, 'ResultRequestIscCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestIscCalibrationResponse = DiagMessage(0xF201, 'ResultRequestIscCalibrationResponse', [3, 4, 64], [1, 4, 5], '', 4)
    ResultRequestIscCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    ResultRequestIscCalibrationResponse.add_parameter(DiagParameter('ErrorCode', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ResultRequestIscCalibrationResponse.add_parameter(DiagParameter('ProgressValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))
    ResultRequestIscCalibrationResponse.add_parameter(DiagParameter('ResultValue', 4, 4, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -32768, 32767, '', False, False, False))

    StartIscCalibrationRequest = DiagMessage(0xF201, 'StartIscCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartIscCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartIscCalibrationResponse = DiagMessage(0xF201, 'StartIscCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StartIscCalibrationResponse.add_parameter(DiagParameter('State', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    StartIscCalibrationResponse.add_parameter(DiagParameter('Nb_Steps', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    StopIscCalibrationRequest = DiagMessage(0xF201, 'StopIscCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    StopIscCalibrationResponse = DiagMessage(0xF201, 'StopIscCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StopIscCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))

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


class A5_ISC_APP138_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    WorkingHour = DiagMessage(0x1011, 'WorkingHour', [], None, '', 1)
    WorkingHour.add_parameter(DiagParameter('WorkingHourModul', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 65535, '', False, False, False))

    PowerVoltage = DiagMessage(0x1061, 'PowerVoltage', [1, 2, 3], None, '', 4)
    PowerVoltage.add_parameter(DiagParameter('PowerSupplyVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][C3R_20-C3R_21][Cab_commands][ ][14-42][D4][Base][raw][A5_138][Y][1]', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('IGNSwitch', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('12VHSD6', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('10VREF', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C3R_20-C3R_21][Cab_commands][ ][2][D4][Base][raw][A5_138][Y][1]', False, False, False))

    AnalogInput = DiagMessage(0x1062, 'AnalogInput', [1, 2, 3], None, '', 12)
    AnalogInput.add_parameter(DiagParameter('AN1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN5', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN6', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN7', 7, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN8', 8, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN9', 9, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN10', 10, 18, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN11', 11, 20, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN12', 12, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 255, '[1][C3R_20-C3R_21][Transmission][X19][21-AN_12][D4][Base][raw][A5_138][Y][1]', False, False, False))

    DigitalInput = DiagMessage(0x1063, 'DigitalInput', [1, 2, 3], None, '', 15)
    DigitalInput.add_parameter(DiagParameter('FREQ1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ3', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN1', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X20][30-AN_1][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN2', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X493][16-AN_2][D4][Base][conv][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN3', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X66][31-AN_3][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN4', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X67][17-AN_4][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN5', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X488][32-AN_5][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN6', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X489][18-AN_6][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN7', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X490][33-AN_7][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN8', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X491][19-AN_8][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN9', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X494][34-AN_9][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN10', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X618][20-AN_10][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN11', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X603][35-AN_11][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN12', 15, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '', False, False, False))

    FreqInput = DiagMessage(0x1064, 'FreqInput', [1, 2, 3], None, '', 3)
    FreqInput.add_parameter(DiagParameter('FREQ1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X481][38-FRQ_1][D4][Base][raw][A5_138][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X483][37-FRQ_2][D4][Base][raw][A5_138][Y][1]', False, False, False))

    DigitalOutput = DiagMessage(0x1065, 'DigitalOutput', [1, 2, 3], None, '', 12)
    DigitalOutput.add_parameter(DiagParameter('HSD3', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Transmission][X484][7-HSD_3][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD4', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Transmission][X485][8-HSD_4][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD5', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Transmission][X486][22-HSD_5][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD6', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Transmission][X487][23-HSD_6][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD7', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Transmission][X772][10-HSD_7][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD8', 6, 5, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD9', 7, 6, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD10', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][4WD][X5][25-HSD_10][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD11', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][PTO][X599][12-HSD-11][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD12', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][PTO][X774][26-HSD_12][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD13', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Difflock][X6][13-HSD_13][D4][Base][raw][A5_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD14', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'off': [0, 0], 'on': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][C3R_20-C3R_21][Transmission][X773][27-HSD_14][D4][Base][raw][A5_138][Y][1]', False, False, False))

    AnalogOutput = DiagMessage(0x1066, 'AnalogOutput', [1, 2, 3], None, '', 6)
    AnalogOutput.add_parameter(DiagParameter('HSD1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X556][5-HSD_1][D4][Base][raw][A5_138][Y][1]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X557][6-HSD_2][D4][Base][raw][A5_138][Y][1]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD5', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD6', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD7', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD8', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))

    Fct4wd = DiagMessage(0x1067, 'Fct4wd', [1, 2, 3], None, '', 11)
    Fct4wd.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct4wd.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct4wd.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct4wd.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X494][34-AN_9][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct4wd.add_parameter(DiagParameter('FourWheelDriveDisengagementByCreeper', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct4wd.add_parameter(DiagParameter('FourWheelDriveCommand', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct4wd.add_parameter(DiagParameter('EVFourWheelDrive', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][4WD][X5][25-HSD_10][D4][L-S][conv][A5_T1][ ][0]#[1][S2-S3-M1][4WD][X5][25-HSD_10][D6][L-S][conv][A5_T2][ ][0]#[1][C3R_20-C3R_21][4WD][X5][25-HSD_10][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct4wd.add_parameter(DiagParameter('VehicleSpeedWheel', 8, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'kph', 0, 65535, '', False, False, False))
    Fct4wd.add_parameter(DiagParameter('LeftBrakePressed', 9, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X66][31-AN_3][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct4wd.add_parameter(DiagParameter('RightBrakePressed', 10, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X67][17-AN_4][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct4wd.add_parameter(DiagParameter('HandBrake', 11, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X618][20-AN_10][D4][Base][conv][A5_138][Y][2]', False, False, False))

    FctDifflock = DiagMessage(0x1068, 'FctDifflock', [1, 2, 3], None, '', 8)
    FctDifflock.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctDifflock.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctDifflock.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    FctDifflock.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'YES': [1, 1]}, 0, 1, '', False, False, False))
    FctDifflock.add_parameter(DiagParameter('DifflocklCommand', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctDifflock.add_parameter(DiagParameter('EVDofflock', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Difflock][X6][13-HSD_13][D4][Base][conv][A5_138][Y][1]', False, False, False))
    FctDifflock.add_parameter(DiagParameter('LeftBreakPressed', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctDifflock.add_parameter(DiagParameter('RightBreakPressed', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    FctHexashift = DiagMessage(0x1069, 'FctHexashift', [1, 2, 3], None, '', 12)
    FctHexashift.add_parameter(DiagParameter('EngineRunning', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('FunctionAvailable', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('TransOilTemperature', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?C', 0, 200, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('Gearbox7psPs1', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X478][24-HSD_8][D4][Base][conv][A5_138][Y][1]', False, False, False))
    FctHexashift.add_parameter(DiagParameter('Gearbox7psPs2', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X479][11-HSD_9][D4][Base][conv][A5_138][Y][1]', False, False, False))
    FctHexashift.add_parameter(DiagParameter('GearRangeUpSelect', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('GearRangeDownSelect', 9, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('GearRangeEngaged', 10, 10, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('PSRequest', 11, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'A': [0, 0], 'B': [1, 1], 'C': [2, 2], 'D': [3, 3]}, 0, 3, '', False, False, False))
    FctHexashift.add_parameter(DiagParameter('PSEngaged', 12, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'A': [0, 0], 'B': [1, 1], 'C': [2, 2], 'D': [3, 3]}, 0, 3, '', False, False, False))

    FctTransGeneral = DiagMessage(0x106A, 'FctTransGeneral', [1, 2, 3], None, '', 6)
    FctTransGeneral.add_parameter(DiagParameter('ClutchPedalPercent', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    FctTransGeneral.add_parameter(DiagParameter('ShuttleShiftStatus', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Forward': [0, 0], 'Neutral': [1, 1], 'Reverse': [2, 2], 'Up': [3, 3]}, 0, 3, '', False, False, False))
    FctTransGeneral.add_parameter(DiagParameter('EngineSpeed', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '[1][S2][Transmission][X481][38-FRQ_1][D4][L-S][conv][A5_T1][ ][0]#[1][S2-S3-M1][Transmission][X481][38-FRQ_1][D6][L-S][conv][A5_T2][ ][0]', False, False, False))
    FctTransGeneral.add_parameter(DiagParameter('TransOilTemperature', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', -40, 215, '[1][C3R_20-C3R_21][Transmission][X19][21-AN_12][D4][Base][conv][A5_138][Y][1]', False, False, False))
    FctTransGeneral.add_parameter(DiagParameter('VehiculeSpeed', 5, 5, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'kph', 0, 65535, '', False, False, False))
    FctTransGeneral.add_parameter(DiagParameter('Colmatage', 6, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Transmission][X20][30-AN_1][D4][Base][conv][A5_138][Y][1]', False, False, False))

    PowerBoost = DiagMessage(0x106B, 'PowerBoost', [1, 2, 3], None, '', 7)
    PowerBoost.add_parameter(DiagParameter('Phase', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    PowerBoost.add_parameter(DiagParameter('TorqueMeasuredOK', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    PowerBoost.add_parameter(DiagParameter('CdtionCalibrationOK', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    PowerBoost.add_parameter(DiagParameter('Torque', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    PowerBoost.add_parameter(DiagParameter('TransOilTemperature', 5, 6, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', -40, 215, '', False, False, False))
    PowerBoost.add_parameter(DiagParameter('speedTorqIN', 6, 7, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 200, '', False, False, False))
    PowerBoost.add_parameter(DiagParameter('speedTorqOut', 7, 9, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 200, '', False, False, False))

    SelectionPtoElectrohydrau = DiagMessage(0x106C, 'SelectionPtoElectrohydrau', [1, 2, 3], None, '', 15)
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('FonctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('PtoSpeed', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('RatioRequest', 5, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1000': [0, 0], '540': [1, 1], '750': [2, 2], '1000eco': [3, 3], 'Neutre': [4, 4]}, 0, 4, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('RatioEngaged', 6, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1000': [0, 0], '540': [1, 1], '750': [2, 2], '1000eco': [3, 3], 'Neutre': [4, 4]}, 0, 4, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('PtoBreakCommand', 7, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('PtoState', 8, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('EV750gpa50', 9, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][PTO][X774][26-HSD_12][D4][Base][conv][A5_138][Y][1]', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('EV540gpa50', 10, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][PTO][X599][12-HSD-11][D4][Base][conv][A5_138][Y][1]', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('EV540gpa20', 11, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('EV1000gpa20', 12, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('EVEcogpa20', 13, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('EVStdgpa20', 14, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    SelectionPtoElectrohydrau.add_parameter(DiagParameter('Switch5401000Gpa20', 15, 16, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    Fct_ShuttleShiftSelect = DiagMessage(0x106D, 'Fct_ShuttleShiftSelect', [1, 2, 3], None, '', 13)
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('FonctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'YES': [1, 1]}, 0, 1, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('IGNSw', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('ClutchPedalPercent', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('ShuttleShiftSelect', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Forward': [0, 0], 'Neutral': [1, 1], 'Reverse': [2, 2], 'Up': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxlscFwdCurrent', 8, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X556][4-HSD_1_cs][D4][Base][raw][A5_138][Y][1]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxlscRevCurrent', 9, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 2000, '[1][C3R_20-C3R_21][Transmission][X557][3-HSD_2_cs][D4][Base][raw][A5_138][Y][1]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('EngSpeed', 10, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X481][38-FRQ_1][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('InverterSpeedSensor', 11, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][C3R_20-C3R_21][Transmission][X483][37-FRQ_2][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxlscFwdSetPointCurrent', 12, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 2000, '[1][C3R_20-C3R_21][Transmission][X556][5-HSD_1][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxlscRevSetPointCurrent', 13, 18, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 2000, '[1][C3R_20-C3R_21][Transmission][X557][6-HSD_2][D4][Base][conv][A5_138][Y][1]', False, False, False))

    Fct_RangeCreeper = DiagMessage(0x106E, 'Fct_RangeCreeper', [1, 2, 3], None, '', 9)
    Fct_RangeCreeper.add_parameter(DiagParameter('FonctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeCreeper.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeCreeper.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_RangeCreeper.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeCreeper.add_parameter(DiagParameter('CreeperEngaged', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeCreeper.add_parameter(DiagParameter('CreeperCommand', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C3R_20-C3R_21][Cab_commands][X603][35-AN_11][D4][Base][conv][A5_138][Y][2]', False, False, False))
    Fct_RangeCreeper.add_parameter(DiagParameter('EVCreeperEngagement', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][Transmission][X772][10-HSD_7][D4][L-S][conv][A5_T1][ ][0]#[1][S2][Transmission][X772][27-HSD_14][D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X772][10-HSD_7][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeCreeper.add_parameter(DiagParameter('EVCreeperDisengagement', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][Transmission][X773][13-HSD_13][D6][L-S][conv][A5_T1][ ][0]#[1][S2][Transmission][X773][27-HSD_14][D4][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X773][27-HSD_14][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeCreeper.add_parameter(DiagParameter('VehicleSpeedWheel', 9, 9, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '', False, False, False))

    Fct_RangeSelect = DiagMessage(0x106F, 'Fct_RangeSelect', [1, 2, 3], None, '', 17)
    Fct_RangeSelect.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EVGear1', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Transmission][X484][7-HSD_3][D4-D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X484][7-HSD_3][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EVGear2', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Transmission][X485][8-HSD_4][D4-D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X485][8-HSD_4][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EVGear3', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Transmission][X486][22-HSD_5][D4-D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X486][22-HSD_5][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EVGear4', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][Transmission][X487][23-HSD_6][D4][L-S][conv][A5_T1][ ][0]#[1][S2-S3-M1][Transmission][X487][10-HSD_7][D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X487][23-HSD_6][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('SwitchGear1', 9, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2][Transmission][X488][32-AN_5][D4][L-S][conv][A5_T1][ ][0]#[1][S2-S3-M1][Transmission][X488][17-AN_4][D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X488][32-AN_5][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('SwitchGear2', 10, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2][Transmission][X489][18-AN_6][D4][L-S][conv][A5_T1][ ][0]#[1][S2-S3-M1][Transmission][X489][32-AN_5][D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X489][18-AN_6][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('SwitchGear3', 11, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2][Transmission][X490][33-AN_7][D4][L-S][conv][A5_T1][ ][0]#[1][S2-S3-M1][Transmission][X490][18-AN_6][D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X490][33-AN_7][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('SwitchGear4', 12, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2][Transmission][X491][19-AN_8][D4][L-S][conv][A5_T1][ ][0]#[1][S2-S3-M1][Transmission][X491][33-AN_7][D6][L-S][conv][A5_T1][ ][0]#[1][C3R_20-C3R_21][Transmission][X491][19-AN_8][D4][Base][conv][A5_138][Y][1]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('ShuttleShiftSelect', 13, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Forward': [0, 0], 'Neutral': [1, 1], 'Reverse': [2, 2], 'Up': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('CreeperEngagement', 14, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('RangeRequested', 15, 15, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('RangeEngaged', 16, 16, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('TransOilTemperature', 17, 17, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', -40, 215, '[1][S2][Transmission][X19][21-AN_12][D4][L-S][conv][A5_T1_T2][ ][0][A5_T1][ ][0]', False, False, False))

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

    ECU_SoftwareDetails = DiagMessage(0xF104, 'ECU_SoftwareDetails', [1, 2, 3], None, '', 6)
    ECU_SoftwareDetails.add_parameter(DiagParameter('CANdescVersion', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_1', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_2', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_3', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_4', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_5', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

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

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [1, 2, 3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [1, 2, 3, 4, 64], None, '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [1, 2, 3, 4, 64], None, '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))

    CalibrationState_ISC = DiagMessage(0xFE00, 'CalibrationState_ISC', [1, 3, 64], None, '', 1)
    CalibrationState_ISC.add_parameter(DiagParameter('CalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))


class A5_ISC_APP138_BVWriteDataSignals:
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


class A5_ISC_APP138_BVIOControlDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [4], [4], '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))


A5_ISC_APP138_BVDTCSnapshotdDids = {
}


class A5_ISC_APP138Client(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0xFC0000, 0x0, 32, 32, erase_address=0xFC0000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4000, 0x0, 32, 32, erase_address=0xFF4000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4980, 0x0, 32, 32, erase_address=0xFF4980, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF7E40, 0x0, 32, 32, erase_address=0xFF7E40, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xEC, "A5_ISC_APP138", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A5_ISC_APP138_BVReadDataSignals
        self.write_dids = A5_ISC_APP138_BVWriteDataSignals
        self.routine_dids = A5_ISC_APP138_BVRoutineIdentifierSignals
        self.io_dids = A5_ISC_APP138_BVIOControlDataSignals
        self.dtc_snapshot_dids = A5_ISC_APP138_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

class A5_DYNA4_APP167Client(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0xFC0000, 0x0, 32, 32, erase_address=0xFC0000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS1\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4000, 0x0, 32, 32, erase_address=0xFF4000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS1\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4740, 0x0, 32, 32, erase_address=0xFF4740, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS1\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF7E40, 0x0, 32, 32, erase_address=0xFF7E40, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS1\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xA0, "A5_DYNA4_APP167", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=2, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A5_ISC_APP138_BVReadDataSignals
        self.write_dids = A5_ISC_APP138_BVWriteDataSignals
        self.routine_dids = A5_ISC_APP138_BVRoutineIdentifierSignals
        self.io_dids = A5_ISC_APP138_BVIOControlDataSignals
        self.dtc_snapshot_dids = A5_ISC_APP138_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

class A5_DYNA4_APP168Client(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0xFC0000, 0x0, 32, 32, erase_address=0xFC0000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4000, 0x0, 32, 32, erase_address=0xFF4000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4980, 0x0, 32, 32, erase_address=0xFF4980, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF7E40, 0x0, 32, 32, erase_address=0xFF7E40, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D4_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xA1, "A5_DYNA4_APP168", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=2, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A5_ISC_APP138_BVReadDataSignals
        self.write_dids = A5_ISC_APP138_BVWriteDataSignals
        self.routine_dids = A5_ISC_APP138_BVRoutineIdentifierSignals
        self.io_dids = A5_ISC_APP138_BVIOControlDataSignals
        self.dtc_snapshot_dids = A5_ISC_APP138_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

class A5_DYNA6_APP177Client(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0xFC0000, 0x0, 32, 32, erase_address=0xFC0000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS1\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4000, 0x0, 32, 32, erase_address=0xFF4000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS1\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4A00, 0x0, 32, 32, erase_address=0xFF4980, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS1\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF7E40, 0x0, 32, 32, erase_address=0xFF7E40, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS1\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xAA, "A5_DYNA6_APP177", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=2, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A5_ISC_APP138_BVReadDataSignals
        self.write_dids = A5_ISC_APP138_BVWriteDataSignals
        self.routine_dids = A5_ISC_APP138_BVRoutineIdentifierSignals
        self.io_dids = A5_ISC_APP138_BVIOControlDataSignals
        self.dtc_snapshot_dids = A5_ISC_APP138_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

class A5_DYNA6_APP178Client(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0xFC0000, 0x0, 32, 32, erase_address=0xFC0000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4000, 0x0, 32, 32, erase_address=0xFF4000, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF4880, 0x0, 32, 32, erase_address=0xFF4980, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False), MemoryLocation(0xFF7E40, 0x0, 32, 32, erase_address=0xFF7E40, erase_size=None, path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS2\output.hex", ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL", did_read_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareIdentification), did_fingerprint_obj=deepcopy(A5_ISC_APP138_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xAB, "A5_DYNA6_APP178", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=2, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A5_ISC_APP138_BVReadDataSignals
        self.write_dids = A5_ISC_APP138_BVWriteDataSignals
        self.routine_dids = A5_ISC_APP138_BVRoutineIdentifierSignals
        self.io_dids = A5_ISC_APP138_BVIOControlDataSignals
        self.dtc_snapshot_dids = A5_ISC_APP138_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

