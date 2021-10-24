from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class DYNA4_TR1_BVRoutineIdentifierSignals:
    CheckMemoryRequest = DiagMessage(0x0202, 'CheckMemoryRequest', [2], [1, 3, 4, 5], '', 0)

    CheckMemoryResponse = DiagMessage(0x0202, 'CheckMemoryResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckMemoryResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PASSED': [0, 0], 'FAILED': [1, 1]}, 0, 1, '', False, False, False))

    CheckProgrammingPreConditionsRequest = DiagMessage(0x0203, 'CheckProgrammingPreConditionsRequest', [3], None, '', 0)

    CheckProgrammingPreConditionsResponse = DiagMessage(0x0203, 'CheckProgrammingPreConditionsResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckProgrammingPreConditionsResponse.add_parameter(DiagParameter('ProgrammingPreConditionList', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGINE_SPEED_NOT_ZERO': [1, 1], 'IMMOBILIZER_NOT_UNLOCKED': [2, 2], 'TRANSMISSION_SPEED_IN_NOT_ZERO': [3, 3], 'TRANSMISSION_SPEED_OUT_NOT_ZERO': [4, 4], 'VEHICLE_SPEED_NOT_ZERO': [5, 5], 'CONTROLLING_ACTIVE': [6, 6], 'IGNITION_OFF_ON_NECESSARY': [7, 7], 'PROGRAMMING_VOLTAGE_TOO_LOW': [8, 8], 'IGNITION_NOT_ON': [9, 9], 'VEHICLE_VOLTAGE_TOO_LOW': [10, 10], 'TEMPERATURE_TOO_HIGH': [11, 11], 'TEMPERATURE_TOO_LOW': [12, 12], 'RESERVED_BY_HIS': [13, 127], 'VEHICLE_NOT_IN_SAFE_STATE': [128, 128], 'RESERVED_BY_MANUFACTURER': [129, 191], 'RESERVED_BY_SUPPLIER': [192, 255]}, 1, 255, 'for each wrong condition 1 byte is sent, if all conditions are meet 0 bytes are transmitted', False, True, False))

    TestRoutine = DiagMessage(0x0203, 'TestRoutine', [3, 4, 64], None, '', 1)
    TestRoutine.add_parameter(DiagParameter('TestSignal', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'remove this routine from the BV/EV, its just a place holder', False, False, False))

    TestRoutine = DiagMessage(0x0203, 'TestRoutine', [3, 4, 64], None, '', 1)
    TestRoutine.add_parameter(DiagParameter('TestSignal', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'remove this routine from the BV/EV, its just a place holder', False, False, False))

    TestRoutine = DiagMessage(0x0203, 'TestRoutine', [3, 4, 64], None, '', 1)
    TestRoutine.add_parameter(DiagParameter('TestSignal', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'remove this routine from the BV/EV, its just a place holder', False, False, False))

    TestRoutine = DiagMessage(0x0203, 'TestRoutine', [3, 4, 64], None, '', 1)
    TestRoutine.add_parameter(DiagParameter('TestSignal', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'remove this routine from the BV/EV, its just a place holder', False, False, False))

    IscCalibrationResultRequest = DiagMessage(0xF201, 'IscCalibrationResultRequest', [1, 2, 3, 4, 64], [1, 3, 4, 5], '', 0)

    IscCalibrationResultResponse = DiagMessage(0xF201, 'IscCalibrationResultResponse', [3, 4, 64], [1, 3, 4, 5], '', 4)
    IscCalibrationResultResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))
    IscCalibrationResultResponse.add_parameter(DiagParameter('ErrorCode', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO_ERROR': [0, 0], 'INITIAL CONDITION ERROR': [255, 255], 'CALIBRATION RESULT ERROR': [256, 256], 'CALIBRATION STEP ERROR': [257, 257]}, 0, 257, '', False, False, False))
    IscCalibrationResultResponse.add_parameter(DiagParameter('ProgressValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))
    IscCalibrationResultResponse.add_parameter(DiagParameter('ResultValue', 4, 4, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ERROR_CODE_NOT_AVAILABLE': [0, 4294967295]}, 0, 4294967295, '', False, False, False))

    IscCalibrationStartRequest = DiagMessage(0xF201, 'IscCalibrationStartRequest', [1, 2, 3, 4, 64], [1, 3, 4, 5], '', 1)
    IscCalibrationStartRequest.add_parameter(DiagParameter('CalibrationCommand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'START_CALIBRATION': [0, 0], 'START_NEXT_STEP': [1, 1]}, 0, 1, '', False, False, False))

    IscCalibrationStartResponse = DiagMessage(0xF201, 'IscCalibrationStartResponse', [1, 2, 3, 4, 64, 65], None, '', 2)
    IscCalibrationStartResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))
    IscCalibrationStartResponse.add_parameter(DiagParameter('NumberOfSteps', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    IscCalibrationStopRequest = DiagMessage(0xF201, 'IscCalibrationStopRequest', [1, 2, 3, 4, 64], [1, 3, 4, 5], '', 0)

    IscCalibrationStopResponse = DiagMessage(0xF201, 'IscCalibrationStopResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    IscCalibrationStopResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))

    PowerBoost2CalibrationResultRequest = DiagMessage(0xF203, 'PowerBoost2CalibrationResultRequest', [1, 2, 3, 4, 64], [1, 3, 4, 5], '', 0)

    PowerBoost2CalibrationResultResponse = DiagMessage(0xF203, 'PowerBoost2CalibrationResultResponse', [3, 4, 64], [1, 3, 4, 5], '', 4)
    PowerBoost2CalibrationResultResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))
    PowerBoost2CalibrationResultResponse.add_parameter(DiagParameter('ErrorCode', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO_ERROR': [0, 0], 'INITIAL CONDITION ERROR': [255, 255], 'CALIBRATION RESULT ERROR': [256, 256], 'CALIBRATION STEP ERROR': [257, 257]}, 0, 257, '', False, False, False))
    PowerBoost2CalibrationResultResponse.add_parameter(DiagParameter('ProgressValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))
    PowerBoost2CalibrationResultResponse.add_parameter(DiagParameter('ResultValue', 4, 4, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ERROR_CODE_NOT_AVAILABLE': [0, 4294967295]}, 0, 4294967295, '', False, False, False))

    PowerBoost2CalibrationStartRequest = DiagMessage(0xF203, 'PowerBoost2CalibrationStartRequest', [1, 2, 3, 4, 64], [1, 3, 4, 5], '', 1)
    PowerBoost2CalibrationStartRequest.add_parameter(DiagParameter('CalibrationCommand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'START_CALIBRATION': [0, 0], 'START_NEXT_STEP': [1, 1]}, 0, 1, '', False, False, False))

    PowerBoost2CalibrationStartResponse = DiagMessage(0xF203, 'PowerBoost2CalibrationStartResponse', [1, 2, 3, 4, 64, 65], None, '', 2)
    PowerBoost2CalibrationStartResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))
    PowerBoost2CalibrationStartResponse.add_parameter(DiagParameter('NumberOfSteps', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PowerBoost2CalibrationStopRequest = DiagMessage(0xF203, 'PowerBoost2CalibrationStopRequest', [1, 2, 3, 4, 64], [1, 3, 4, 5], '', 0)

    PowerBoost2CalibrationStopResponse = DiagMessage(0xF203, 'PowerBoost2CalibrationStopResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    PowerBoost2CalibrationStopResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))

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


class DYNA4_TR1_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    PowerVoltage = DiagMessage(0x1061, 'PowerVoltage', [1, 3, 4, 64], None, '', 4)
    PowerVoltage.add_parameter(DiagParameter('PowerSupplyVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('IGNswitch', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('12VHSD6', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('5VREF', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[0][S2][Miscellaneous][ ][2-41][D4-D6][L-S][raw][A5_T2][N][2]', False, False, False))

    AnalogInput = DiagMessage(0x1062, 'AnalogInput', [1, 3, 4, 64], None, '', 12)
    AnalogInput.add_parameter(DiagParameter('AN_1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_5', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_6', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_7', 7, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_8', 8, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_9', 9, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_10', 10, 18, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_11', 11, 20, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S3-M1][Braking_system][X135][35-AN_11][D6][L-S][raw][A5_T1][Y_Y][0_0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_12', 12, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2][Transmission][X19-B14][21-AN_12][D4][L-S][raw][A5_T1][Y][0]#[1][S2-S3-M1][Transmission][ ][21-AN_12][D6][L-S][raw][A5_T1][Y_Y_Y][0_0_0]', False, False, False))

    DigitalInput_Read = DiagMessage(0x1063, 'DigitalInput_Read', [1, 3, 4, 64], None, '', 15)
    DigitalInput_Read.add_parameter(DiagParameter('FREQ_1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('FREQ_2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('FREQ_3', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_1', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CLOSE': [0, 0], 'OPEN': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X20-S155][30-AN_1][D4][L-S][raw][A5_T1][Y][0]#[1][S2-S3-M1][Cab_commands][X603M-X603E][30-AN_1][D6][L-S][raw][A5_T1][Y_N_N][1_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_2', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X493][16-AN_2][D4][L-S][raw][A5_T1][Y][2]#[1][S2][PTO][X729][16-AN_2][D6][L-S][raw][A5_T1][Y][0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_3', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X66][31-AN_3][D4][L-S][raw][A5_T1][Y][0]#[1][S2-S3-M1][Transmission][X493][31-AN_3][D6][L-S][raw][A5_T1][Y_Y_Y][1_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_4', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X67][17-AN_4][D4][L-S][raw][A5_T1][Y][0]#[1][S2-S3-M1][Transmission][X488-S171][17-AN_4][D6][L-S][raw][A5_T1][Y_Y_Y][0_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_5', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X488-S171][32-AN_5][D4][L-S][raw][A5_T1][Y][0]#[1][S2-S3-M1][Transmission][X489-S172][32-AN_5][D6][L-S][raw][A5_T1][Y_Y_Y][2_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_6', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X489-S172][18-AN_6][D4][L-S][raw][A5_T1][Y][0]#[1][S2-S3-M1][Transmission][X490-S173][18-AN_6][D6][L-S][raw][A5_T1][Y_Y_Y][2_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_7', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X490-S173][33-AN_7][D4][L-S][raw][A5_T1][Y][0]#[1][S2-S3-M1][Transmission][X491-S174][33-AN_7][D6][L-S][raw][A5_T1][Y_Y_Y][2_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_8', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X491-S174][19-AN_8][D4][L-S][raw][A5_T1][Y][0]#[1][S3-M1][Braking_system][X618][19-AN_8][D6][L-S][raw][A5_T1][Y][0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_9', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X494-S182][34-AN_9][D4][L-S][raw][A5_T1][Y][0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_10', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2-S3-M1][Cab_commands][X56][20-AN_10][D6][L-S][raw][A5_T1][Y_N_N][1_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_11', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X603E][35-AN_11][D4][L-S][raw][A5_T1][Y][0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_12', 15, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))

    FreqInput = DiagMessage(0x1064, 'FreqInput', [1, 3, 4, 64], None, '', 3)
    FreqInput.add_parameter(DiagParameter('FREQ_1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][S2][Transmission][X481-B30][38-FRQ_1][D4][L-S][raw][A5_T1][Y][0]#[1][S2-S3-M1][Transmission][X483-B45][38-FRQ_1][D6][L-S][raw][A5_T1][Y_Y_Y][1_0_0]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][S2][Transmission][X483-B45][37-FRQ_2][D4][L-S][raw][A5_T1][Y][1]#[1][S2-S3-M1][Transmission][X482-B9][37-FRQ_2][D6][L-S][raw][A5_T1][Y_Y_Y][0_0_0]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][S2][Transmission][X492-B49][36-FRQ_3][D4][L-S][raw][A5_T1][Y][0]#[1][S2][PTO][X777][36-FRQ_3][D6][L-S][raw][A5_T1][Y][0]#[1][S3-M1][PTO][X16][36-FRQ_3][D6][L-S][raw][A5_T1][Y_Y][0_0]', False, False, False))

    DigitalOutput_Read = DiagMessage(0x1065, 'DigitalOutput_Read', [1, 3, 4, 64], None, '', 12)
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_3', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X484-Y72][7-HSD_3][D4][L-S][raw][A5_T1][Y][2]#[1][S2-S3-M1][Transmission][X484-Y72][7-HSD_3][D6][L-S][raw][A5_T1][Y_N_N][2_0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_4', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X485-Y73][8-HSD_4][D4][L-S][raw][A5_T1][Y][2]#[1][S2-S3-M1][Transmission][X485-Y73][8-HSD_4][D6][L-S][raw][A5_T1][Y_N_N][2_0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_5', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X486-Y74][22-HSD_5][D4][L-S][raw][A5_T1][Y][2]#[1][S2-S3-M1][Transmission][X486-Y74][22-HSD_5][D6][L-S][raw][A5_T1][Y_N_N][2_0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_6', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X487-Y75][23-HSD_6][D4][L-S][raw][A5_T1][Y][0]#[1][S2][PTO][X16][23-HSD_6][D6][L-S][raw][A5_T1][Y][2]#[1][S3-M1][PTO][X7][23-HSD_6][D6][L-S][raw][A5_T1][Y_Y][0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_7', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X772][10-HSD_7][D4][L-S][raw][A5_T1][Y][1]#[1][S2-S3-M1][Transmission][X487-Y75][10-HSD_7][D6][L-S][raw][A5_T1][Y_Y_Y][0_0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_8', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X478-Y76][24-HSD_8][D4][L-S][raw][A5_T1][Y][0]#[1][S2][PTO][X728][24-HSD_8][D6][L-S][raw][A5_T1][Y][2]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_9', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X479-Y77][11-HSD_9][D4][L-S][raw][A5_T1][Y][1]#[1][S2-S3-M1][Miscellaneous][K15][11-HSD_9][D6][L-S][raw][A5_T1][Y_Y_Y][0_0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_10', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][4WD][X5-Y3][25-HSD_10][D4][L-S][raw][A5_T1][Y][0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_11', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X774][12-HSD_11][D4][L-S][raw][A5_T1][Y][0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_12', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X599][26-HSD_12][D4][L-S][raw][A5_T1][Y][0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_13', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Difflock][X6-Y1][13-HSD_13][D4][L-S][raw][A5_T1][Y][0]#[1][S2][Transmission][X773][13-HSD_13][D6][L-S][raw][A5_T1][Y][2]#[1][S3-M1][Braking_system][X496][13-HSD_13][D6][L-S][raw][A5_T1][Y_Y][0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_14', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X773][27-HSD_14][D4][L-S][raw][A5_T1][Y][2]#[1][S2][Transmission][X772][27-HSD_14][D6][L-S][raw][A5_T1][Y][0]', False, False, False))

    AnalogOutput = DiagMessage(0x1066, 'AnalogOutput', [1, 3, 4, 64], None, '', 6)
    AnalogOutput.add_parameter(DiagParameter('HSD_1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2][Transmission][X556-Y11][5-HSD_1][D4][L-S][raw][A5_T1][Y][1]#[1][S2-S3-M1][Transmission][X556-Y11][5-HSD_1][D6][L-S][raw][A5_T1][Y_Y_Y][1_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2][Transmission][X557-Y12][6-HSD_2][D4][L-S][raw][A5_T1][Y][1]#[1][S2-S3-M1][Transmission][X557-Y12][6-HSD_2][D6][L-S][raw][A5_T1][Y_Y_Y][1_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_5', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_6', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_7', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_8', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))

    Fct_4wd = DiagMessage(0x1067, 'Fct_4wd', [1, 3, 4, 64], None, '', 11)
    Fct_4wd.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X494-S182][34-AN_9][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('FourWheelDrive_disengage', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('FourWheelCommand', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('EV_FourWheelDrive', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1]}, 0, 1, '[1][S2][4WD][X5-Y3][25-HSD_10][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('VehicleSpeedWheel', 8, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'km/h', 20000, 64255, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('LeftBrakePressed', 9, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X66][31-AN_3][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('RightBrakePressed', 10, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X67][17-AN_4][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('HandBrake', 11, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))

    Fct_Difflock = DiagMessage(0x1068, 'Fct_Difflock', [1, 3, 4, 64], None, '', 8)
    Fct_Difflock.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Difflock.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Difflock.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_Difflock.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Difflock.add_parameter(DiagParameter('DifflocklCommand', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Difflock.add_parameter(DiagParameter('EV_Difflock', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Difflock][X6-Y1][13-HSD_13][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_Difflock.add_parameter(DiagParameter('LeftBrakePressed', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Difflock.add_parameter(DiagParameter('RightBrakePressed', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))

    Fct_Hexashift = DiagMessage(0x1069, 'Fct_Hexashift', [1, 3, 4, 64], None, '', 12)
    Fct_Hexashift.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('TransOilTemperature', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 200, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('GearBox7psPs1', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X478-Y76][24-HSD_8][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('GearBox7psPs2', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X479-Y77][11-HSD_9][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('GearRangeUpSelect', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('GearRangeDownSelect', 9, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('GearRangeEngaged', 10, 10, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 7, '[1][S2][Transmission][RangeEng][][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('PS_Requested', 11, 11, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('PS_Engaged', 12, 12, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2][Transmission][PsEng][][D4][L-S][conv][A5_T1][Y][0]', False, False, False))

    Fct_TransGeneral = DiagMessage(0x106A, 'Fct_TransGeneral', [1, 3, 4, 64], None, '', 7)
    Fct_TransGeneral.add_parameter(DiagParameter('ClutchPedalPercent', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    Fct_TransGeneral.add_parameter(DiagParameter('ShuttleShiftStatus', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'FORWARD': [0, 0], 'NEUTRAL': [1, 1], 'REVERSE': [2, 2]}, 0, 2, '', False, False, False))
    Fct_TransGeneral.add_parameter(DiagParameter('EngineSpeed', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '[1][S2][Transmission][X481-B30][38-FRQ_1][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_TransGeneral.add_parameter(DiagParameter('TransOilTemperature', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 200, '', False, False, False))
    Fct_TransGeneral.add_parameter(DiagParameter('Vehicle_speed', 5, 5, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'km/h', 0, 65535, '', False, False, False))
    Fct_TransGeneral.add_parameter(DiagParameter('TransFilterBlockage', 6, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X20-S155][30-AN_1][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_TransGeneral.add_parameter(DiagParameter('LubSwitch', 7, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X493][16-AN_2][D4][L-S][conv][A5_T1][N][0]', False, False, False))

    Powerboost = DiagMessage(0x106B, 'Powerboost', [1, 3, 4, 64], None, '', 7)
    Powerboost.add_parameter(DiagParameter('Phase', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Powerboost.add_parameter(DiagParameter('Torque_Measured', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Powerboost.add_parameter(DiagParameter('Cdtion_Calibration', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Powerboost.add_parameter(DiagParameter('Torque', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Powerboost.add_parameter(DiagParameter('TransOilTemperature', 5, 6, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 200, '', False, False, False))
    Powerboost.add_parameter(DiagParameter('speed_Torq_In', 6, 7, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 200, '[1][S2][Transmission][X492-B49][36-FRQ_3][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Powerboost.add_parameter(DiagParameter('speed_Torq_Out', 7, 9, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 200, '', False, False, False))

    Selection_pto_electrohydrau = DiagMessage(0x106C, 'Selection_pto_electrohydrau', [1, 3, 4, 64], None, '', 15)
    Selection_pto_electrohydrau.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('PtoSpeed', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('RatioRequested', 5, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1000': [0, 0], '540': [1, 1], '750': [2, 2], '1000ECO': [3, 3], 'NEUTRE': [4, 4]}, 0, 4, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('RatioEngaged', 6, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1000': [0, 0], '540': [1, 1], '750': [2, 2], '1000ECO': [3, 3], 'NEUTRE': [4, 4]}, 0, 4, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('PtoBrakeCommand', 7, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('PtoState', 8, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PTO_OFF': [0, 0], 'PTO_INIT': [1, 1], 'PTO_FILLING': [2, 2], 'PTO_START': [3, 3], 'PTO_PULSING': [4, 4], 'PTO_ON': [5, 5], 'PTO_SENSORS_OFF': [6, 6], 'PTO_ALARM': [7, 7], 'PTO_FENDER': [8, 8], 'STATE_PTO_EV_ON_OFF': [9, 9]}, 0, 9, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('EV750_gpa50', 9, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X774][12-HSD_11][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('EV540_gpa50', 10, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X599][26-HSD_12][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('EV540_gpa20', 11, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('EV1000_gpa20', 12, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('EVEco_gpa20', 13, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('EVStd_gpa20', 14, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Selection_pto_electrohydrau.add_parameter(DiagParameter('Switch_540_1000_gpa20', 15, 16, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))

    Fct_ShuttleShiftSelect = DiagMessage(0x106D, 'Fct_ShuttleShiftSelect', [1, 3, 4, 64], None, '', 13)
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('IGNSw', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('ClutchPedalPercent', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('ShuttleShiftSelect', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'FORWARD': [0, 0], 'NEUTRAL': [1, 1], 'REVERSE': [2, 2], 'UP': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxIscFwdCurrent', 8, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 2000, '[1][S2][Transmission][X556][4-HSD_1cs][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxIscRevCurrent', 9, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 2000, '[1][S2][Transmission][X557][3-HSD_2cs][D4][L-S][conv][A5_T1][N][2]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('EngSpeed', 10, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 64255, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('InverterSpeedSensor', 11, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][S2][Transmission][X483-B45][37-FRQ_2][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearBoxIscFwdSetPointCurrent', 12, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 65535, '[1][S2][Transmission][X556-Y11][5-HSD_1][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxIscRevSetPointCurrent', 13, 18, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 65535, '[1][S2][Transmission][X557-Y12][6-HSD_2][D4][L-S][conv][A5_T1][N][2]', False, False, False))

    Fct_Creeper = DiagMessage(0x106E, 'Fct_Creeper', [1, 3, 4, 64], None, '', 9)
    Fct_Creeper.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Creeper.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Creeper.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_Creeper.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Creeper.add_parameter(DiagParameter('CreeperEngaged', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Creeper.add_parameter(DiagParameter('CreeperCommand', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X603E][35-AN_11][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_Creeper.add_parameter(DiagParameter('EV_CreeperEngagement', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X772][10-HSD_7][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_Creeper.add_parameter(DiagParameter('EV_CreeperDisengagement', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X773][27-HSD_14][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_Creeper.add_parameter(DiagParameter('VehicleSpeedWheel', 9, 9, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 64255, '', False, False, False))

    Fct_RangeSelect = DiagMessage(0x106F, 'Fct_RangeSelect', [1, 3, 4, 64], None, '', 17)
    Fct_RangeSelect.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EV_Gear1', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X484-Y72][7-HSD_3][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EV_Gear2', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X485-Y73][8-HSD_4][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EV_Gear3', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X486-Y74][22-HSD_5][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('EV_Gear4', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X487-Y75][23-HSD_6][D4][L-S][conv][A5_T1][N][0]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('SwitchGear1', 9, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X488-S171][32-AN_5][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('SwitchGear2', 10, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X489-S172][18-AN_6][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('SwitchGear3', 11, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X490-S173][33-AN_7][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('SwitchGear4', 12, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Transmission][X491-S174][19-AN_8][D4][L-S][conv][A5_T1][Y][0]', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('ShuttleShiftSelect', 13, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'FORWARD': [0, 0], 'NEUTRAL': [1, 1], 'REVERSE': [2, 2], 'UP': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('CreeperEngagement', 14, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('Range_Requested', 15, 15, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('Range_Engaged', 16, 16, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Fct_RangeSelect.add_parameter(DiagParameter('TransOilTemperature', 17, 17, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 65535, '[1][S2][Transmission][X19-B14][21-AN_12][D4][L-S][conv][A5_T1][N][0]', False, False, False))

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

    CalibrationState_ISC = DiagMessage(0xFE00, 'CalibrationState_ISC', [1, 3, 4, 64], None, '', 1)
    CalibrationState_ISC.add_parameter(DiagParameter('CalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    CalibrationState_PowerBoostMultipleSpeed = DiagMessage(0xFE02, 'CalibrationState_PowerBoostMultipleSpeed', [1, 3, 4, 64], None, '', 1)
    CalibrationState_PowerBoostMultipleSpeed.add_parameter(DiagParameter('CalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))


class DYNA4_TR1_BVWriteDataSignals:
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

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class DYNA4_TR1_BVIOControlDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [4], [4], '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))


DYNA4_TR1_BVDTCSnapshotdDids = {
}


class DYNA4_TR1Client(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0xFC0000, 0x0, 32, 32, erase_address=0xFC0000, erase_size=None,
                               path_to_file="C:\ProgramData\AGCO Corporation\TechConnectDiagnostics\dev\Content\Flashfiles\LL_UDS_A5_D6_TRANS1\output.hex",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(DYNA4_TR1_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(DYNA4_TR1_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None,
                               consider_in_mdr=False),
                MemoryLocation(0xFF4000, 0x0, 32, 32, erase_address=0xFF4000, erase_size=None,
                               path_to_file="",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(DYNA4_TR1_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   DYNA4_TR1_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None,
                               consider_in_mdr=False),
                MemoryLocation(0xFF4A00, 0x0, 32, 32, erase_address=0xFF4980, erase_size=None,
                               path_to_file="",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(DYNA4_TR1_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   DYNA4_TR1_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None,
                               consider_in_mdr=False),
                MemoryLocation(0xFF7E40, 0x0, 32, 32, erase_address=0xFF7E40, erase_size=None,
                               path_to_file="",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(DYNA4_TR1_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   DYNA4_TR1_BVReadDataSignals.ApplicationSoftwareFingerprint), did_dependency=None,
                               consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xA0, "DYNA4_TR1", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = DYNA4_TR1_BVReadDataSignals
        self.write_dids = DYNA4_TR1_BVWriteDataSignals
        self.routine_dids = DYNA4_TR1_BVRoutineIdentifierSignals
        self.io_dids = DYNA4_TR1_BVIOControlDataSignals
        self.dtc_snapshot_dids = DYNA4_TR1_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

