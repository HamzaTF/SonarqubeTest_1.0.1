from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class A11_TRANS_BVRoutineIdentifierSignals:
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

    ResultRequestRangeCalibrationRequest = DiagMessage(0xF214, 'ResultRequestRangeCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestRangeCalibrationResponse = DiagMessage(0xF214, 'ResultRequestRangeCalibrationResponse', [3, 4, 64], [1, 4, 5], '', 4)
    ResultRequestRangeCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    ResultRequestRangeCalibrationResponse.add_parameter(DiagParameter('ErrorCode', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ResultRequestRangeCalibrationResponse.add_parameter(DiagParameter('ProgressValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))
    ResultRequestRangeCalibrationResponse.add_parameter(DiagParameter('ResultValue', 4, 4, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -32768, 32767, '', False, False, False))

    StartRangeCalibrationRequest = DiagMessage(0xF214, 'StartRangeCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartRangeCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartRangeCalibrationResponse = DiagMessage(0xF214, 'StartRangeCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StartRangeCalibrationResponse.add_parameter(DiagParameter('State', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    StartRangeCalibrationResponse.add_parameter(DiagParameter('Nb_Steps', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    StopRangeCalibrationRequest = DiagMessage(0xF214, 'StopRangeCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    StopRangeCalibrationResponse = DiagMessage(0xF214, 'StopRangeCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StopRangeCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))

    ResultRequestClutchesCalibrationRequest = DiagMessage(0xF215, 'ResultRequestClutchesCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestClutchesCalibrationResponse = DiagMessage(0xF215, 'ResultRequestClutchesCalibrationResponse', [3, 4, 64], [1, 4, 5], '', 4)
    ResultRequestClutchesCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    ResultRequestClutchesCalibrationResponse.add_parameter(DiagParameter('ErrorCode', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ResultRequestClutchesCalibrationResponse.add_parameter(DiagParameter('ProgressValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))
    ResultRequestClutchesCalibrationResponse.add_parameter(DiagParameter('ResultValue', 4, 4, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -32768, 32767, '', False, False, False))

    StartClutchesCalibrationRequest = DiagMessage(0xF215, 'StartClutchesCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartClutchesCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartClutchesCalibrationResponse = DiagMessage(0xF215, 'StartClutchesCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StartClutchesCalibrationResponse.add_parameter(DiagParameter('State', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    StartClutchesCalibrationResponse.add_parameter(DiagParameter('Nb_Steps', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    StopClutchesCalibrationRequest = DiagMessage(0xF215, 'StopClutchesCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    StopClutchesCalibrationResponse = DiagMessage(0xF215, 'StopClutchesCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StopClutchesCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))

    ResultRequestPowerBoostCalibrationRequest = DiagMessage(0xF216, 'ResultRequestPowerBoostCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestPowerBoostCalibrationResponse = DiagMessage(0xF216, 'ResultRequestPowerBoostCalibrationResponse', [3, 4, 64], [1, 4, 5], '', 4)
    ResultRequestPowerBoostCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    ResultRequestPowerBoostCalibrationResponse.add_parameter(DiagParameter('ErrorCode', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    ResultRequestPowerBoostCalibrationResponse.add_parameter(DiagParameter('ProgressValue', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))
    ResultRequestPowerBoostCalibrationResponse.add_parameter(DiagParameter('ResultValue', 4, 4, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -32768, 32767, '', False, False, False))

    StartPowerBoostCalibrationRequest = DiagMessage(0xF216, 'StartPowerBoostCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartPowerBoostCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartPowerBoostCalibrationResponse = DiagMessage(0xF216, 'StartPowerBoostCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StartPowerBoostCalibrationResponse.add_parameter(DiagParameter('State', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    StartPowerBoostCalibrationResponse.add_parameter(DiagParameter('Nb_Steps', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    StopPowerBoostCalibrationRequest = DiagMessage(0xF216, 'StopPowerBoostCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    StopPowerBoostCalibrationResponse = DiagMessage(0xF216, 'StopPowerBoostCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StopPowerBoostCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10], 'INVALID_USER_LEVEL': [11, 11], 'WRONG_OPERATION_MODE': [12, 12], 'NOT_READ': [255, 255]}, 0, 255, '', False, False, False))

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


class A11_TRANS_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    WorkingHour = DiagMessage(0x1011, 'WorkingHour', [1, 3, 4, 64], None, '', 1)
    WorkingHour.add_parameter(DiagParameter('WorkingHourModul', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 's', 0, 0, '', False, False, False))

    ProcessData = DiagMessage(0x1060, 'ProcessData', [1, 3, 4, 64], None, '', 4)
    ProcessData.add_parameter(DiagParameter('InverterValveFwdSetPointCurrent', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 4000, '', False, False, False))
    ProcessData.add_parameter(DiagParameter('InverterValveRevSetPointCurrent', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 4000, '', False, False, False))
    ProcessData.add_parameter(DiagParameter('InverterValveFwdMeasureCurrent', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 4000, '', False, False, False))
    ProcessData.add_parameter(DiagParameter('InverterValveRevMeasureCurrent', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 4000, '', False, False, False))

    PowerVoltage = DiagMessage(0x1061, 'PowerVoltage', [1, 3, 4, 64], None, '', 8)
    PowerVoltage.add_parameter(DiagParameter('PowerSupplyVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 16000, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('IGNswitch', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('HDS_SW1', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('HDS_SW2', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('HDS_SW3', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('HDS_SW4', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('5Vref', 7, 7, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 5000, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('10VRef', 8, 9, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 10000, '[1][M2][Transmission][X1031.11-X1032.11-X20-X494][C2-F3][ ][ ][raw][A11][Y][2]', False, False, False))

    AnalogInput = DiagMessage(0x1062, 'AnalogInput', [1, 3, 4, 64], None, '', 17)
    AnalogInput.add_parameter(DiagParameter('AN1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][X66][CC-A1-AN_1][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][X67][CC-A3-AN_3][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN5', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN6', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN7', 7, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN8', 8, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][G14][C2-B4-AN_8][ ][ ][raw][A11][Y][0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN9', 9, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][G34_DCT][C2-C1-AN_9][ ][ ][raw][A11][Y][2]#[1][M2][Transmission][G44_AMT][C2-C1-AN_9][ ][ ][raw][A11][Y][0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN10', 10, 18, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][G33_DCT][C2-C2-AN_10][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN11', 11, 20, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][X494][C2-C3-AN_11][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN12', 12, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][G13][C2-C4-AN_12][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN13', 13, 24, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][X20][C2-D1-AN_13][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN14', 14, 26, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][G35_DCT][C2-D2-AN_14][ ][ ][raw][A11][Y][2]#[1][M2][Transmission][G45_AMT][C2-D2-AN_14][ ][ ][raw][A11][Y][0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN15', 15, 28, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN16', 16, 30, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][X19][C2-D4-AN_16][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN17', 17, 32, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))

    DigitalInput = DiagMessage(0x1063, 'DigitalInput', [1, 3, 4, 64], None, '', 9)
    DigitalInput.add_parameter(DiagParameter('FREQ_1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ_2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ_3', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ_4', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ_5', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ_6', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ_7', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ_8', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ_9', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))

    FreqInput = DiagMessage(0x1064, 'FreqInput', [1, 3, 4, 64], None, '', 9)
    FreqInput.add_parameter(DiagParameter('FREQ_1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][M2][Transmission][G47-G37][C2-F4-FRQ_1][ ][ ][raw][A11][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][M2][Transmission][G9][C2-G1-FRQ_2][ ][ ][raw][A11][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][M2][Transmission][G10][C2-G2-FRQ_3][ ][ ][raw][A11][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][M2][Transmission][G11][C2-G3-FRQ_4][ ][ ][raw][A11][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_5', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][M2][Transmission][G11][C2-G4-FRQ_5][ ][ ][raw][A11][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_6', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][M2][Transmission][G48-G38][C2-H1-FRQ_6][ ][ ][raw][A11][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_7', 7, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][M2][Transmission][G12][C2-H2-FRQ_7][ ][ ][raw][A11][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_8', 8, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_9', 9, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '', False, False, False))

    DigitalOutput = DiagMessage(0x1065, 'DigitalOutput', [1, 3, 4, 64], None, '', 26)
    DigitalOutput.add_parameter(DiagParameter('HSD_5', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G46-G36][C1-A2-HSD_5][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_6', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G26_DCT][C1-A3-HSD_6][ ][ ][raw][A11][Y][2]#[1][M2][Transmission][G41_AMT][C1-A3-HSD_6][ ][ ][raw][A11][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_7', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G27_DCT][C1-B1-HSD_7][ ][ ][raw][A11][Y][2]#[1][M2][Transmission][G42_AMT][C1-B1-HSD_7][ ][ ][raw][A11][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_8', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G30_DCT][C1-B1-HSD_8][ ][ ][raw][A11][Y][0]#[1][M2][Transmission][G43_AMT][C1-B2-HSD_8][ ][ ][raw][A11][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_9', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G25_DCT][C1-B4-HSD_9][ ][ ][raw][A11][Y][2]#[1][M2][Transmission][G40_AMT][C1-B4-HSD_9][ ][ ][raw][A11][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_10', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G29_DCT][C1-C1-HSD_10][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_11', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G28_DTC][C1-A3-HSD_11][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_12', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G3][C1-C4-HSD_12][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_13', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G1][C1-D2-HSD_13][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_14', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G6][C1-D3-HSD_14][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_15', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G7][C1-E1-HSD_15][ ][ ][raw][A11][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_16', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G4][C1-E2-HSD_16][ ][ ][raw][A11][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_17', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_18', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_19', 15, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_20', 16, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_21', 17, 16, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_22', 18, 17, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_23', 19, 18, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_24', 20, 19, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('LSD_1', 21, 20, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G8][C1-M1-LSD_1][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('LSD_2', 22, 21, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G5][C1-M2-LSD_2][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('LSD_3', 23, 22, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G32_DCT][C1-M3-LSD_3][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('LSD_4', 24, 23, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G31_DCT][C1-M4-LSD_4][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('LSD_5', 25, 24, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G46-G36][C1-H1-LSD_5][ ][ ][raw][A11][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('LSD_6', 26, 25, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))

    AnalogOutput = DiagMessage(0x1066, 'AnalogOutput', [1, 3, 4, 64], None, '', 4)
    AnalogOutput.add_parameter(DiagParameter('HSD_1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '[1][M2][Transmission][G8][C1-L1-HSD_1][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '[1][M2][Transmission][G5][C1-L2-HSD_2][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '[1][M2][Transmission][G32_DCT][C1-L3-HSD_3][ ][ ][raw][A11][Y][2]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '[1][M2][Transmission][G31_DCT][C1-L4-HSD_4][ ][ ][raw][A11][Y][2]', False, False, False))

    Fct_ShuttleShiftSelect = DiagMessage(0x1067, 'Fct_ShuttleShiftSelect', [1, 3, 4, 64], None, '', 16)
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('EngineRunning', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('ShuttleShiftSelect', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Forward': [0, 0], 'Neutral': [1, 1], 'Reverse': [2, 2], 'Up': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxlscFwdMeasureCurrent', 5, 5, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 2000, '[1][M2][Transmission][G8][C1-M1-LSD_1][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearboxlscRevMeasureCurrent', 6, 7, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'A', 0, 2000, '[1][M2][Transmission][G5][C1-M2-LSD_2][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('Slippage_Reverser', 7, 9, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('Energy_Reveser', 8, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'kW', 0, 65535, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('TransOilPressure', 9, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GearRangeEngagedTerm', 10, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1': [0, 0], '2': [1, 1], '3': [2, 2], '4': [3, 3], 'P': [6, 6]}, 0, 6, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('TransNotInNeutral', 11, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('CabEngineTransmittedMaxTorqRqst', 12, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('IGNSw', 13, 18, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('ShuttleShiftRqst', 14, 19, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Forward': [0, 0], 'Neutral': [1, 1], 'Reverse': [2, 2], 'Up': [3, 3]}, 0, 3, '', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('EngSpeed', 15, 20, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 64255, '[1][M2][Transmission][G48-G38][C2-H-FRQ_6][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_ShuttleShiftSelect.add_parameter(DiagParameter('GroundSpeedSensor', 16, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '', False, False, False))

    Fct_RangeSelect_amt = DiagMessage(0x1068, 'Fct_RangeSelect_amt', [1, 3, 4, 64], None, '', 58)
    Fct_RangeSelect_amt.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('EngineRunning', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Sync_Snd_12', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Sync_Prim_24', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Sync_Prim_13', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Sync_Snd_34', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('GearRangeEngagedTerm', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1': [0, 0], '2': [1, 1], '3': [2, 2], '4': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('RangePassedWell', 9, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('ShuttleShiftSelect', 10, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Forward': [0, 0], 'Neutral': [1, 1], 'Reverse': [2, 2], 'Up': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('EngagedGear', 11, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'gear 1': [1, 1], 'gear 2': [2, 2], 'gear 3': [3, 3], 'gear 4': [4, 4], 'gear 5': [5, 5], 'gear 6': [6, 6], 'gear 7': [7, 7], 'gear 8': [8, 8], 'gear 9': [9, 9], 'gear 10': [10, 10], 'gear 11': [11, 11], 'gear 12': [12, 12], 'gear 13': [13, 13], 'gear 14': [14, 14], 'gear 15': [15, 15], 'gear 16': [16, 16], 'gear 17': [17, 17], 'gear 18': [18, 18], 'gear 19': [19, 19], 'gear 20': [20, 20], 'gear 21': [21, 21], 'gear 22': [22, 22], 'gear 23': [23, 23], 'gear 24': [24, 24], 'gear 25': [25, 25], 'gear 26': [26, 26], 'gear 27': [27, 27], 'gear 28': [28, 28]}, 1, 28, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('GearToEngage', 12, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'gear 1': [1, 1], 'gear 2': [2, 2], 'gear 3': [3, 3], 'gear 4': [4, 4], 'gear 5': [5, 5], 'gear 6': [6, 6], 'gear 7': [7, 7], 'gear 8': [8, 8], 'gear 9': [9, 9], 'gear 10': [10, 10], 'gear 11': [11, 11], 'gear 12': [12, 12], 'gear 13': [13, 13], 'gear 14': [14, 14], 'gear 15': [15, 15], 'gear 16': [16, 16], 'gear 17': [17, 17], 'gear 18': [18, 18], 'gear 19': [19, 19], 'gear 20': [20, 20], 'gear 21': [21, 21], 'gear 22': [22, 22], 'gear 23': [23, 23], 'gear 24': [24, 24], 'gear 25': [25, 25], 'gear 26': [26, 26], 'gear 27': [27, 27], 'gear 28': [28, 28]}, 1, 28, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('CreeperEngagement', 13, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('TransNotInNeutral', 14, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('TransOilPressure', 15, 15, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('TransLubOilPressure', 16, 17, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][G13][C2-C4-AN_12][ ][ ][conv][A11][Y][0]', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('TransOilFilterClogging', 17, 19, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][M2][Transmission][X20][C2-D1-AN_13][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('TransOilTempreature', 18, 21, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 200, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Range_SyncPrim_Pos_mV', 19, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 0, '[1][M2][Transmission][G45_AMT][C2-D2-AN_14][ ][ ][conv][A11][Y][0]', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Range_SyncSnd_Pos_mV', 20, 24, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 0, '[1][M2][Transmission][G44_AMT][C2-C1-AN_9][ ][ ][conv][A11][Y][0]', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Range_Creeper_Pos_mV', 21, 26, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 0, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear1_Allowed', 22, 28, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear2_Allowed', 23, 29, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear3_Allowed', 24, 30, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear4_Allowed', 25, 31, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear5_Allowed', 26, 32, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear6_Allowed', 27, 33, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear7_Allowed', 28, 34, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear8_Allowed', 29, 35, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear9_Allowed', 30, 36, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear10_Allowed', 31, 37, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear11_Allowed', 32, 38, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear12_Allowed', 33, 39, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear13_Allowed', 34, 40, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear14_Allowed', 35, 41, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear15_Allowed', 36, 42, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear16_Allowed', 37, 43, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear17_Allowed', 38, 44, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear18_Allowed', 39, 45, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear19_Allowed', 40, 46, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear20_Allowed', 41, 47, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear21_Allowed', 42, 48, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear22_Allowed', 43, 49, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear23_Allowed', 44, 50, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear24_Allowed', 45, 51, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear25_Allowed', 46, 52, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear26_Allowed', 47, 53, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear27_Allowed', 48, 54, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Gear28_Allowed', 49, 55, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('RangeSyncPrim_Pos_State', 50, 56, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Reached': [0, 0], 'Adjust': [1, 1], 'Error': [2, 2]}, 0, 2, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('RangeSyncSnd_Pos_State', 51, 57, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Reached': [0, 0], 'Adjust': [1, 1], 'Error': [2, 2]}, 0, 2, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('RangeCreeper_Pos_State', 52, 58, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Reached': [0, 0], 'Adjust': [1, 1], 'Error': [2, 2]}, 0, 2, '[1][M2][Transmission][G14][C2-B4-AN_8][ ][ ][conv][A11][Y][0]', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('RangeSyncPrim_Pos_Traget', 53, 59, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'POS_RANGE_1': [0, 0], 'POS_RANGE_2': [1, 1], 'POS_RANGE_3': [2, 2], 'POS_RANGE_4': [3, 3], 'POS_RANGE_NEUTRAL_13': [4, 4], 'POS_RANGE_NEUTRAL_24': [5, 5], 'POS_PRIM_13': [6, 6], 'POS_PRIM_24': [7, 7], 'POS_Neutral_PRIM': [8, 8], 'POS_SND_12': [9, 9], 'POS_SND_34': [10, 10], 'POS_NEUTRAL_SND': [11, 11], 'POS_STOP_PRIM_13': [12, 12], 'POS_STOP_PRIM_24': [13, 13], 'POS_STOP_SND_12': [14, 14], 'POS_STOP_SND_34': [15, 15], 'POS_STOP_RANGE_1': [16, 16], 'POS_STOP_RANGE_2': [17, 17], 'POS_STOP_RANGE_3': [18, 18], 'POS_STOP_RANGE_3x1': [19, 19], 'POS_STOP_RANGE_4': [20, 20], 'POS_COUPLING_12': [21, 21], 'POS_DECOUPLING_12': [22, 22], 'POS_STOP_CREEPER_ENGAGED': [23, 23], 'POS_STOP_CREEPER_DIENGAGED': [24, 24], 'POS_SYNCHRO_MAX': [25, 25], 'POS_SYNCHRO_UNDEF': [26, 26]}, 0, 26, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('RangeSyncSnd_Pos_Traget', 54, 60, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'POS_RANGE_1': [0, 0], 'POS_RANGE_2': [1, 1], 'POS_RANGE_3': [2, 2], 'POS_RANGE_4': [3, 3], 'POS_RANGE_NEUTRAL_13': [4, 4], 'POS_RANGE_NEUTRAL_24': [5, 5], 'POS_PRIM_13': [6, 6], 'POS_PRIM_24': [7, 7], 'POS_Neutral_PRIM': [8, 8], 'POS_SND_12': [9, 9], 'POS_SND_34': [10, 10], 'POS_NEUTRAL_SND': [11, 11], 'POS_STOP_PRIM_13': [12, 12], 'POS_STOP_PRIM_24': [13, 13], 'POS_STOP_SND_12': [14, 14], 'POS_STOP_SND_34': [15, 15], 'POS_STOP_RANGE_1': [16, 16], 'POS_STOP_RANGE_2': [17, 17], 'POS_STOP_RANGE_3': [18, 18], 'POS_STOP_RANGE_3x1': [19, 19], 'POS_STOP_RANGE_4': [20, 20], 'POS_COUPLING_12': [21, 21], 'POS_DECOUPLING_12': [22, 22], 'POS_STOP_CREEPER_ENGAGED': [23, 23], 'POS_STOP_CREEPER_DIENGAGED': [24, 24], 'POS_SYNCHRO_MAX': [25, 25], 'POS_SYNCHRO_UNDEF': [26, 26]}, 0, 26, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('RangeCreeper_Pos_Traget', 55, 61, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'POS_RANGE_1': [0, 0], 'POS_RANGE_2': [1, 1], 'POS_RANGE_3': [2, 2], 'POS_RANGE_4': [3, 3], 'POS_RANGE_NEUTRAL_13': [4, 4], 'POS_RANGE_NEUTRAL_24': [5, 5], 'POS_PRIM_13': [6, 6], 'POS_PRIM_24': [7, 7], 'POS_Neutral_PRIM': [8, 8], 'POS_SND_12': [9, 9], 'POS_SND_34': [10, 10], 'POS_NEUTRAL_SND': [11, 11], 'POS_STOP_PRIM_13': [12, 12], 'POS_STOP_PRIM_24': [13, 13], 'POS_STOP_SND_12': [14, 14], 'POS_STOP_SND_34': [15, 15], 'POS_STOP_RANGE_1': [16, 16], 'POS_STOP_RANGE_2': [17, 17], 'POS_STOP_RANGE_3': [18, 18], 'POS_STOP_RANGE_3x1': [19, 19], 'POS_STOP_RANGE_4': [20, 20], 'POS_COUPLING_12': [21, 21], 'POS_DECOUPLING_12': [22, 22], 'POS_STOP_CREEPER_ENGAGED': [23, 23], 'POS_STOP_CREEPER_DIENGAGED': [24, 24], 'POS_SYNCHRO_MAX': [25, 25], 'POS_SYNCHRO_UNDEF': [26, 26]}, 0, 26, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Engine_Control_Mode_Rqst', 56, 62, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGINE_NO_CONTROL': [0, 0], 'ENGINE_SPEED_CONTROL': [1, 1], 'ENGINE_TORQ_CONTROL': [2, 2]}, 0, 2, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Troq_Offset_Rqst_Nm', 57, 63, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Nm', 0, 65535, '', False, False, False))
    Fct_RangeSelect_amt.add_parameter(DiagParameter('Speed_Rqst_rpm', 58, 65, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 6425, '', False, False, False))

    Fct_4wd = DiagMessage(0x106A, 'Fct_4wd', [1, 3, 4, 64], None, '', 20)
    Fct_4wd.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('ErrorActive', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('EngineRunning', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('4wdEngagement', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('4wdSpoolValve', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][M2][Transmission][G46-G36][C1-A2-HSD_5][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('FourWheelDriveStatusActVal', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'auto': [2, 2], 'Error': [14, 14], 'NotAvailable': [15, 15]}, 0, 15, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('PowerSupplyVoltage', 7, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('TransOilPressure', 8, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('FourWheelDriveRequested', 9, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('VehicleSpeedWheel', 10, 11, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'km/h', 0, 64255, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('LeftBrakePressed', 11, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CLOSE': [0, 0], 'OPEN': [1, 1]}, 0, 1, '[1][M2][Transmission][X66][CC-A1-AN_1][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('RightBrakePressed', 12, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CLOSE': [0, 0], 'OPEN': [1, 1]}, 0, 1, '[1][M2][Transmission][X67][CC-A3-AN_3][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('LeftBrakeComp', 13, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('RightBrakeComp', 14, 16, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('GearboxIscSpeedSensorRPM', 15, 17, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'rpm', 0, 625335, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('Energy_4WD', 16, 19, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('RearBrakeState', 17, 21, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CLOSE': [0, 0], 'OPEN': [1, 1], 'NA': [2, 2]}, 0, 2, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('4WDNaoActivation', 18, 22, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('4WDSpeedRPM', 19, 23, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'rpm', 0, 65535, '', False, False, False))
    Fct_4wd.add_parameter(DiagParameter('4WDSpeedQuadraRPM', 20, 25, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'rpm', 0, 65535, '', False, False, False))

    Fct_Hexashift = DiagMessage(0x106B, 'Fct_Hexashift', [1, 3, 4, 64], None, '', 15)
    Fct_Hexashift.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('EngineRunning', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('Gearbox7psPs1', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][M2][Transmission][G1][C1-D2-HSD_13][ ][ ][conv][A11][Y][1]', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('Gearbox7psPs2', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][M2][Transmission][G6][C1-D3-HSD_14][ ][ ][conv][A11][Y][1]', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('Gearbox7psOverDrive', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][M2][Transmission][G3][C1-C4-HSD_12][ ][ ][conv][A11][Y][1]', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('GearShiftEngagedTerm', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'A': [0, 0], 'B': [1, 1], 'C': [2, 2], 'D': [3, 3], 'D_Comp': [4, 4], 'E': [5, 5], 'F': [6, 6], 'G': [7, 7], 'H': [8, 8]}, 0, 8, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('TransOilPressure', 8, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('ShuttleShiftStatus', 9, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Forward': [0, 0], 'Neutral': [1, 1], 'Reverse': [2, 2], 'Up': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('TransOilTempreature', 10, 11, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 200, '[1][M2][Transmission][X19][C2-D4-AN_16][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('TransNotInNeutral', 11, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('TransOilTempAllowedShiftSelection', 12, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('EngagedGear', 13, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'gear 1': [1, 1], 'gear 2': [2, 2], 'gear 3': [3, 3], 'gear 4': [4, 4], 'gear 5': [5, 5], 'gear 6': [6, 6], 'gear 7': [7, 7], 'gear 8': [8, 8], 'gear 9': [9, 9], 'gear 10': [10, 10], 'gear 11': [11, 11], 'gear 12': [12, 12], 'gear 13': [13, 13], 'gear 14': [14, 14], 'gear 15': [15, 15], 'gear 16': [16, 16], 'gear 17': [17, 17], 'gear 18': [18, 18], 'gear 19': [19, 19], 'gear 20': [20, 20], 'gear 21': [21, 21], 'gear 22': [22, 22], 'gear 23': [23, 23], 'gear 24': [24, 24], 'gear 25': [25, 25], 'gear 26': [26, 26], 'gear 27': [27, 27], 'gear 28': [28, 28]}, 1, 28, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('GearToEngage', 14, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'gear 1': [1, 1], 'gear 2': [2, 2], 'gear 3': [3, 3], 'gear 4': [4, 4], 'gear 5': [5, 5], 'gear 6': [6, 6], 'gear 7': [7, 7], 'gear 8': [8, 8], 'gear 9': [9, 9], 'gear 10': [10, 10], 'gear 11': [11, 11], 'gear 12': [12, 12], 'gear 13': [13, 13], 'gear 14': [14, 14], 'gear 15': [15, 15], 'gear 16': [16, 16], 'gear 17': [17, 17], 'gear 18': [18, 18], 'gear 19': [19, 19], 'gear 20': [20, 20], 'gear 21': [21, 21], 'gear 22': [22, 22], 'gear 23': [23, 23], 'gear 24': [24, 24], 'gear 25': [25, 25], 'gear 26': [26, 26], 'gear 27': [27, 27], 'gear 28': [28, 28]}, 1, 28, '', False, False, False))
    Fct_Hexashift.add_parameter(DiagParameter('Ratio_ps', 15, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, '', 0, 65535, '', False, False, False))

    Fct_TransProtection = DiagMessage(0x106C, 'Fct_TransProtection', [1, 3, 4, 64], None, '', 11)
    Fct_TransProtection.add_parameter(DiagParameter('EngineRunning', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('TransProtection', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('GearboxBoostOutSpeed', 5, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 200, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('EngineSpeed', 6, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 200, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('MeasureTorque', 7, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Nm', 0, 1000, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('CalibrationPowerBoostAllowed', 8, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('TorquePowerBoostMeasuredAvailable', 9, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('PowerBoostPhase', 10, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 0, '', False, False, False))
    Fct_TransProtection.add_parameter(DiagParameter('GearboxBoostOutSpeedRPM', 11, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'rpm', 0, 65535, '', False, False, False))

    Fct_AllowingCalibration = DiagMessage(0x106D, 'Fct_AllowingCalibration', [1, 3, 4, 64], None, '', 14)
    Fct_AllowingCalibration.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('CalibrationClutchsAllowed', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('CalibrationRangesAllowed', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('TransOilPressure', 5, 5, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('TransOilTempreature', 6, 7, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 200, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('InCabEngineTransmittedMaxTorqPer100', 7, 8, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('EngRqedSpeed_SpeedLimit', 8, 9, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 23500, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('FourWheelDriveSetSwitch', 9, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('ShuttleShiftForward', 10, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('ShuttleShiftNeutral', 11, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('TransNotInNeutral', 12, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('TransOilTempAllowedShiftSelection', 13, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_AllowingCalibration.add_parameter(DiagParameter('GearboxIscSpeedSensor', 14, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '', False, False, False))

    Fct_RangeSelect_dct = DiagMessage(0x106E, 'Fct_RangeSelect_dct', [1, 3, 4, 64], None, '', 58)
    Fct_RangeSelect_dct.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('EngineRunning', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('GearRange3to1', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][M2][Transmission][G30_DCT][C1-B2-HSD_8][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('GearRange4to2', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][M2][Transmission][G26_DCT][C1-A3-HSD_6][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('GearRange1to3', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][M2][Transmission][G25_DCT][C1-B4-HSD_9][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('GearRange2to4', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][M2][Transmission][G27_DCT][C1-B1-HSD_7][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('GearRangeEngagedTerm', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1': [0, 0], '2': [1, 1], '3': [2, 2], '4': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('RangePassedWell', 9, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('ShuttleShiftSelect', 10, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Forward': [0, 0], 'Neutral': [1, 1], 'Reverse': [2, 2], 'Up': [3, 3]}, 0, 3, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('EngagedGear', 11, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'gear 1': [1, 1], 'gear 2': [2, 2], 'gear 3': [3, 3], 'gear 4': [4, 4], 'gear 5': [5, 5], 'gear 6': [6, 6], 'gear 7': [7, 7], 'gear 8': [8, 8], 'gear 9': [9, 9], 'gear 10': [10, 10], 'gear 11': [11, 11], 'gear 12': [12, 12], 'gear 13': [13, 13], 'gear 14': [14, 14], 'gear 15': [15, 15], 'gear 16': [16, 16], 'gear 17': [17, 17], 'gear 18': [18, 18], 'gear 19': [19, 19], 'gear 20': [20, 20], 'gear 21': [21, 21], 'gear 22': [22, 22], 'gear 23': [23, 23], 'gear 24': [24, 24], 'gear 25': [25, 25], 'gear 26': [26, 26], 'gear 27': [27, 27], 'gear 28': [28, 28]}, 1, 28, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('GearToEngage', 12, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'gear 1': [1, 1], 'gear 2': [2, 2], 'gear 3': [3, 3], 'gear 4': [4, 4], 'gear 5': [5, 5], 'gear 6': [6, 6], 'gear 7': [7, 7], 'gear 8': [8, 8], 'gear 9': [9, 9], 'gear 10': [10, 10], 'gear 11': [11, 11], 'gear 12': [12, 12], 'gear 13': [13, 13], 'gear 14': [14, 14], 'gear 15': [15, 15], 'gear 16': [16, 16], 'gear 17': [17, 17], 'gear 18': [18, 18], 'gear 19': [19, 19], 'gear 20': [20, 20], 'gear 21': [21, 21], 'gear 22': [22, 22], 'gear 23': [23, 23], 'gear 24': [24, 24], 'gear 25': [25, 25], 'gear 26': [26, 26], 'gear 27': [27, 27], 'gear 28': [28, 28]}, 1, 28, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('CreeperEngagement', 13, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('TransNotInNeutral', 14, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NO': [0, 0], 'Yes': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('TransOilPressure', 15, 15, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('TransLubOilPressure', 16, 17, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('TransOilFilterClogging', 17, 19, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('TransOilTempreature', 18, 21, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 200, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Range_Sync13_Pos_mV', 19, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 0, '[1][M2][Transmission][G35_DCT][C2-D2-AN_14][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Range_Sync24_Pos_mV', 20, 24, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 0, '[1][M2][Transmission][G34_DCT][C2-C1-AN_9][ ][ ][conv][A11][Y][2]', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Range_Creeper_Pos_mV', 21, 26, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 0, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear1_Allowed', 22, 28, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear2_Allowed', 23, 29, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear3_Allowed', 24, 30, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear4_Allowed', 25, 31, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear5_Allowed', 26, 32, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear6_Allowed', 27, 33, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear7_Allowed', 28, 34, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear8_Allowed', 29, 35, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear9_Allowed', 30, 36, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear10_Allowed', 31, 37, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear11_Allowed', 32, 38, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear12_Allowed', 33, 39, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear13_Allowed', 34, 40, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear14_Allowed', 35, 41, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear15_Allowed', 36, 42, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear16_Allowed', 37, 43, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear17_Allowed', 38, 44, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear18_Allowed', 39, 45, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear19_Allowed', 40, 46, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear20_Allowed', 41, 47, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear21_Allowed', 42, 48, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear22_Allowed', 43, 49, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear23_Allowed', 44, 50, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear24_Allowed', 45, 51, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear25_Allowed', 46, 52, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear26_Allowed', 47, 53, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear27_Allowed', 48, 54, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Gear28_Allowed', 49, 55, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('RangeSync13_Pos_Sate', 50, 56, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Reached': [0, 0], 'Adjust': [1, 1], 'Error': [2, 2]}, 0, 2, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('RangeSync24_Pos_State', 51, 57, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Reached': [0, 0], 'Adjust': [1, 1], 'Error': [2, 2]}, 0, 2, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('RangeCreeper_Pos_State', 52, 58, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Reached': [0, 0], 'Adjust': [1, 1], 'Error': [2, 2]}, 0, 2, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Rangesync13_Pos_Traget', 53, 59, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'POS_RANGE_1': [0, 0], 'POS_RANGE_2': [1, 1], 'POS_RANGE_3': [2, 2], 'POS_RANGE_4': [3, 3], 'POS_RANGE_NEUTRAL_13': [4, 4], 'POS_RANGE_NEUTRAL_24': [5, 5], 'POS_PRIM_13': [6, 6], 'POS_PRIM_24': [7, 7], 'POS_Neutral_PRIM': [8, 8], 'POS_SND_12': [9, 9], 'POS_SND_34': [10, 10], 'POS_NEUTRAL_SND': [11, 11], 'POS_STOP_PRIM_13': [12, 12], 'POS_STOP_PRIM_24': [13, 13], 'POS_STOP_SND_12': [14, 14], 'POS_STOP_SND_34': [15, 15], 'POS_STOP_RANGE_1': [16, 16], 'POS_STOP_RANGE_2': [17, 17], 'POS_STOP_RANGE_3': [18, 18], 'POS_STOP_RANGE_3x1': [19, 19], 'POS_STOP_RANGE_4': [20, 20], 'POS_COUPLING_12': [21, 21], 'POS_DECOUPLING_12': [22, 22], 'POS_STOP_CREEPER_ENGAGED': [23, 23], 'POS_STOP_CREEPER_DIENGAGED': [24, 24], 'POS_SYNCHRO_MAX': [25, 25], 'POS_SYNCHRO_UNDEF': [26, 26]}, 0, 26, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Rangesync24_Pos_Traget', 54, 60, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'POS_RANGE_1': [0, 0], 'POS_RANGE_2': [1, 1], 'POS_RANGE_3': [2, 2], 'POS_RANGE_4': [3, 3], 'POS_RANGE_NEUTRAL_13': [4, 4], 'POS_RANGE_NEUTRAL_24': [5, 5], 'POS_PRIM_13': [6, 6], 'POS_PRIM_24': [7, 7], 'POS_Neutral_PRIM': [8, 8], 'POS_SND_12': [9, 9], 'POS_SND_34': [10, 10], 'POS_NEUTRAL_SND': [11, 11], 'POS_STOP_PRIM_13': [12, 12], 'POS_STOP_PRIM_24': [13, 13], 'POS_STOP_SND_12': [14, 14], 'POS_STOP_SND_34': [15, 15], 'POS_STOP_RANGE_1': [16, 16], 'POS_STOP_RANGE_2': [17, 17], 'POS_STOP_RANGE_3': [18, 18], 'POS_STOP_RANGE_3x1': [19, 19], 'POS_STOP_RANGE_4': [20, 20], 'POS_COUPLING_12': [21, 21], 'POS_DECOUPLING_12': [22, 22], 'POS_STOP_CREEPER_ENGAGED': [23, 23], 'POS_STOP_CREEPER_DIENGAGED': [24, 24], 'POS_SYNCHRO_MAX': [25, 25], 'POS_SYNCHRO_UNDEF': [26, 26]}, 0, 26, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('RangeCreeper_Pos_Traget', 55, 61, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'POS_RANGE_1': [0, 0], 'POS_RANGE_2': [1, 1], 'POS_RANGE_3': [2, 2], 'POS_RANGE_4': [3, 3], 'POS_RANGE_NEUTRAL_13': [4, 4], 'POS_RANGE_NEUTRAL_24': [5, 5], 'POS_PRIM_13': [6, 6], 'POS_PRIM_24': [7, 7], 'POS_Neutral_PRIM': [8, 8], 'POS_SND_12': [9, 9], 'POS_SND_34': [10, 10], 'POS_NEUTRAL_SND': [11, 11], 'POS_STOP_PRIM_13': [12, 12], 'POS_STOP_PRIM_24': [13, 13], 'POS_STOP_SND_12': [14, 14], 'POS_STOP_SND_34': [15, 15], 'POS_STOP_RANGE_1': [16, 16], 'POS_STOP_RANGE_2': [17, 17], 'POS_STOP_RANGE_3': [18, 18], 'POS_STOP_RANGE_3x1': [19, 19], 'POS_STOP_RANGE_4': [20, 20], 'POS_COUPLING_12': [21, 21], 'POS_DECOUPLING_12': [22, 22], 'POS_STOP_CREEPER_ENGAGED': [23, 23], 'POS_STOP_CREEPER_DIENGAGED': [24, 24], 'POS_SYNCHRO_MAX': [25, 25], 'POS_SYNCHRO_UNDEF': [26, 26]}, 0, 26, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Engine_Control_Mode_Rqst', 56, 62, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGINE_NO_CONTROL': [0, 0], 'ENGINE_SPEED_CONTROL': [1, 1], 'ENGINE_TORQ_CONTROL': [2, 2]}, 0, 2, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Troq_Offset_Rqst_Nm', 57, 63, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Nm', 0, 0, '', False, False, False))
    Fct_RangeSelect_dct.add_parameter(DiagParameter('Speed_Rqst_rpm', 58, 65, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 6425, '', False, False, False))

    RID_Example = DiagMessage(0x1200, 'RID_Example', [], None, '', 1)
    RID_Example.add_parameter(DiagParameter('RoutineOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DummyParameterization = DiagMessage(0x30BD, 'DummyParameterization', [1, 2, 3], None, '', 1)
    DummyParameterization.add_parameter(DiagParameter('DummyParam', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    Parameter_ModuleExchange = DiagMessage(0x30BE, 'Parameter_ModuleExchange', [1, 2, 3], None, '', 1)
    Parameter_ModuleExchange.add_parameter(DiagParameter('ParamModelExchange', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    Parameter_ECUDefaultSetting = DiagMessage(0x30BF, 'Parameter_ECUDefaultSetting', [1, 2, 3], None, '', 1)
    Parameter_ECUDefaultSetting.add_parameter(DiagParameter('PAramECUDefault', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    ECU_PIN = DiagMessage(0xF100, 'ECU_PIN', [], None, '', 1)
    ECU_PIN.add_parameter(DiagParameter('Pin_number', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [38928387, 38928387]}, 38928387, 38928387, '', False, False, False))

    ECU_Cheksum = DiagMessage(0xF101, 'ECU_Cheksum', [1, 2, 3], None, '', 2)
    ECU_Cheksum.add_parameter(DiagParameter('CurrentChecksum', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_Cheksum.add_parameter(DiagParameter('StoredChecksum', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))

    ECU_SoftwareOperatingSystem = DiagMessage(0xF102, 'ECU_SoftwareOperatingSystem', [1, 3, 4, 64], None, '', 5)
    ECU_SoftwareOperatingSystem.add_parameter(DiagParameter('SoftwareVersionOperatingSystem', 1, 0, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_SoftwareOperatingSystem.add_parameter(DiagParameter('SoftwareVersionMicroControler', 2, 3, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_SoftwareOperatingSystem.add_parameter(DiagParameter('SoftwareVersionLanguage', 3, 6, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_SoftwareOperatingSystem.add_parameter(DiagParameter('SoftwareVersionFree3', 4, 9, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_SoftwareOperatingSystem.add_parameter(DiagParameter('SoftwareVersionFree4', 5, 12, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))

    EcuFbIQuestion = DiagMessage(0xF103, 'EcuFbIQuestion', [], None, '', 2)
    EcuFbIQuestion.add_parameter(DiagParameter('FbIQuestion', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    EcuFbIQuestion.add_parameter(DiagParameter('Reserved', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    ECU_SoftwareDetails = DiagMessage(0xF104, 'ECU_SoftwareDetails', [1, 3, 4, 64], None, '', 5)
    ECU_SoftwareDetails.add_parameter(DiagParameter('CANdescVersion', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_2', 2, 2, 0, 1, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_3', 3, 3, 0, 1, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_4', 4, 4, 0, 1, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))
    ECU_SoftwareDetails.add_parameter(DiagParameter('Reserved_5', 5, 5, 0, 1, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))

    SupplierCode = DiagMessage(0xF105, 'SupplierCode', [1, 3, 4, 64], None, '', 1)
    SupplierCode.add_parameter(DiagParameter('SupplierCode', 1, 0, 0, 24, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 0, '', False, False, False))

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

    RangeCalibrationState = DiagMessage(0xFE00, 'RangeCalibrationState', [1, 3, 4, 64], None, '', 1)
    RangeCalibrationState.add_parameter(DiagParameter('CalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    ClutchesCalibrationState = DiagMessage(0xFE01, 'ClutchesCalibrationState', [1, 3, 4, 64], None, '', 1)
    ClutchesCalibrationState.add_parameter(DiagParameter('CalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PowerboostCalibrationState = DiagMessage(0xFE02, 'PowerboostCalibrationState', [1, 3, 4, 64], None, '', 1)
    PowerboostCalibrationState.add_parameter(DiagParameter('CalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    Fct_GearRatio = DiagMessage(0xFE10, 'Fct_GearRatio', [1, 3, 64], None, '', 7)
    Fct_GearRatio.add_parameter(DiagParameter('PS_GearToEngage', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'A': [0, 0], 'B': [1, 1], 'C': [2, 2], 'D': [3, 3], 'D_COMP': [4, 4], 'E': [5, 5], 'F': [6, 6], 'G': [7, 7], 'NULL': [8, 8]}, 0, 8, '', False, False, False))
    Fct_GearRatio.add_parameter(DiagParameter('Range_GearToEngage', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1': [0, 0], '2': [1, 1], '3': [2, 2], '4': [3, 3], 'NEUTRAL_13': [4, 4], 'NEUTRAL_24': [5, 5], 'NEUTRAL': [6, 6], 'UNDEF': [7, 7]}, 0, 7, '', False, False, False))
    Fct_GearRatio.add_parameter(DiagParameter('ISC_Ratio', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, '', 0, 65535, '', False, False, False))
    Fct_GearRatio.add_parameter(DiagParameter('Range_Ratio', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, '', 0, 65535, '', False, False, False))
    Fct_GearRatio.add_parameter(DiagParameter('PS_Ratio', 5, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, '', 0, 65535, '', False, False, False))
    Fct_GearRatio.add_parameter(DiagParameter('GearBox_Ratio', 6, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, '', 0, 65535, '', False, False, False))
    Fct_GearRatio.add_parameter(DiagParameter('PowerShiftSpeedRPM', 7, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'rpm', 0, 65535, '', False, False, False))


class A11_TRANS_BVWriteDataSignals:
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


class A11_TRANS_BVIOControlDataSignals:
    pass


A11_TRANS_BVDTCSnapshotdDids = {
}


class A11_TRANSClient(ECUClient):
    class FlashData(Enum):
        APPL = [MemoryLocation(0x00078000, 0x0, 32, 32, erase_address=0x00078000, erase_size=None,
                               path_to_file="^DGW_[.]__MOD_[.]F[.][0-9a-fA-F]{2}[.][0-9a-fA-F]{3}[.][0-9a-fA-F]{2}[.].{6}[.](HEX|hex)$",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(A11_TRANS_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(A11_TRANS_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False),

                MemoryLocation(0x000FFC00, 0x0, 32, 32, erase_address=0x000FFC00, erase_size=None,
                               path_to_file="^DGW_[.]__MOD_[.]F[.][0-9a-fA-F]{2}[.][0-9a-fA-F]{3}[.][0-9a-fA-F]{2}[.].{6}[.](HEX|hex)$",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(A11_TRANS_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(A11_TRANS_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False),

                MemoryLocation(0x0017FF80, 0x0, 32, 32, erase_address=0x000FFC00, erase_size=None,
                               path_to_file="^DGW_[.]__MOD_[.]F[.][0-9a-fA-F]{2}[.][0-9a-fA-F]{3}[.][0-9a-fA-F]{2}[.].{6}[.](HEX|hex)$",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(A11_TRANS_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(A11_TRANS_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0x3, "A11_TRANS", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A11_TRANS_BVReadDataSignals
        self.write_dids = A11_TRANS_BVWriteDataSignals
        self.routine_dids = A11_TRANS_BVRoutineIdentifierSignals
        self.io_dids = A11_TRANS_BVIOControlDataSignals
        self.dtc_snapshot_dids = A11_TRANS_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

