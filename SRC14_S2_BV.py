from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class SRC14_S2_BVRoutineIdentifierSignals:
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

    ResultRequestRearHitchCalibrationRequest = DiagMessage(0x1201, 'ResultRequestRearHitchCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestRearHitchCalibrationResponse = DiagMessage(0x1201, 'ResultRequestRearHitchCalibrationResponse', [3, 64], [1, 4, 5], '', 0)

    StartRearHitchCalibrationRequest = DiagMessage(0x1201, 'StartRearHitchCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartRearHitchCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartRearHitchCalibrationResponse = DiagMessage(0x1201, 'StartRearHitchCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartRearHitchCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopRearHitchCalibrationRequest = DiagMessage(0x1201, 'StopRearHitchCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopRearHitchCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopRearHitchCalibrationResponse = DiagMessage(0x1201, 'StopRearHitchCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopRearHitchCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopRearHitchCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    ResultRequestClutchPedalCalibrationRequest = DiagMessage(0x1203, 'ResultRequestClutchPedalCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestClutchPedalCalibrationResponse = DiagMessage(0x1203, 'ResultRequestClutchPedalCalibrationResponse', [3, 64], [1, 4, 5], '', 0)

    StartClutchPedalCalibrationRequest = DiagMessage(0x1203, 'StartClutchPedalCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartClutchPedalCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartClutchPedalCalibrationResponse = DiagMessage(0x1203, 'StartClutchPedalCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartClutchPedalCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopClutchPedalCalibrationRequest = DiagMessage(0x1203, 'StopClutchPedalCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopClutchPedalCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopClutchPedalCalibrationResponse = DiagMessage(0x1203, 'StopClutchPedalCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopClutchPedalCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopClutchPedalCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    ResultRequestRadarCalibrationRequest = DiagMessage(0x1204, 'ResultRequestRadarCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestRadarCalibrationResponse = DiagMessage(0x1204, 'ResultRequestRadarCalibrationResponse', [3, 64], [1, 4, 5], '', 0)

    StartRadarCalibrationRequest = DiagMessage(0x1204, 'StartRadarCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartRadarCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartRadarCalibrationResponse = DiagMessage(0x1204, 'StartRadarCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartRadarCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopRadarCalibrationRequest = DiagMessage(0x1204, 'StopRadarCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopRadarCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopRadarCalibrationResponse = DiagMessage(0x1204, 'StopRadarCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopRadarCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopRadarCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    ResultRequestPVEDCalibrationRequest = DiagMessage(0x1206, 'ResultRequestPVEDCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestPVEDCalibrationResponse = DiagMessage(0x1206, 'ResultRequestPVEDCalibrationResponse', [3, 64], [1, 4, 5], '', 0)

    StartPVEDCalibrationRequest = DiagMessage(0x1206, 'StartPVEDCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartPVEDCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartPVEDCalibrationResponse = DiagMessage(0x1206, 'StartPVEDCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartPVEDCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopPVEDCalibrationRequest = DiagMessage(0x1206, 'StopPVEDCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopPVEDCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopPVEDCalibrationResponse = DiagMessage(0x1206, 'StopPVEDCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopPVEDCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopPVEDCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    ResultRequestWASRightLeftCalibrationRequest = DiagMessage(0x1207, 'ResultRequestWASRightLeftCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestWASRightLeftCalibrationResponse = DiagMessage(0x1207, 'ResultRequestWASRightLeftCalibrationResponse', [3, 64], [1, 4, 5], '', 0)

    StartWASRightLeftCalibrationRequest = DiagMessage(0x1207, 'StartWASRightLeftCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartWASRightLeftCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartWASRightLeftCalibrationResponse = DiagMessage(0x1207, 'StartWASRightLeftCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartWASRightLeftCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopWASRightLeftCalibrationRequest = DiagMessage(0x1207, 'StopWASRightLeftCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopWASRightLeftCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopWASRightLeftCalibrationResponse = DiagMessage(0x1207, 'StopWASRightLeftCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopWASRightLeftCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopWASRightLeftCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    ResultRequestWASCenterCalibrationRequest = DiagMessage(0x1208, 'ResultRequestWASCenterCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestWASCenterCalibrationResponse = DiagMessage(0x1208, 'ResultRequestWASCenterCalibrationResponse', [3, 64], [1, 4, 5], '', 0)
    ResultRequestWASCenterCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    ResultRequestWASCenterCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    StartWASCenterCalibrationRequest = DiagMessage(0x1208, 'StartWASCenterCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartWASCenterCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))
    StartWASCenterCalibrationRequest.add_parameter(DiagParameter('Monitoring_Type', 2, 1 , 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NU': [0, 0], 'ACHT': [1, 1]}, 0, 1, '', False, False, False))

    StartWASCenterCalibrationResponse = DiagMessage(0x1208, 'StartWASCenterCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartWASCenterCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))
    StartWASCenterCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    StopWASCenterCalibrationRequest = DiagMessage(0x1208, 'StopWASCenterCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopWASCenterCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopWASCenterCalibrationResponse = DiagMessage(0x1208, 'StopWASCenterCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopWASCenterCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopWASCenterCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

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


class SRC14_S2_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    RearHitchCalibrationState = DiagMessage(0x1101, 'RearHitchCalibrationState', [1, 3, 4, 64], None, '', 1)
    RearHitchCalibrationState.add_parameter(DiagParameter('RearHitchCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    ClutchPedalCalibrationState = DiagMessage(0x1103, 'ClutchPedalCalibrationState', [1, 3, 4, 64], None, '', 1)
    ClutchPedalCalibrationState.add_parameter(DiagParameter('ClutchPedalCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    RadarCalibrationState = DiagMessage(0x1104, 'RadarCalibrationState', [1, 3, 4, 64], None, '', 1)
    RadarCalibrationState.add_parameter(DiagParameter('RadarCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PVEDCalibrationState = DiagMessage(0x1106, 'PVEDCalibrationState', [1, 3, 4, 64], None, '', 1)
    PVEDCalibrationState.add_parameter(DiagParameter('PVEDCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    WASRightLeftCalibrationState = DiagMessage(0x1107, 'WASRightLeftCalibrationState', [1, 3, 4, 64], None, '', 1)
    WASRightLeftCalibrationState.add_parameter(DiagParameter('WASRightLeftCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    WASCenterCalibrationState = DiagMessage(0x1108, 'WASCenterCalibrationState', [1, 3, 4, 64], None, '', 1)
    WASCenterCalibrationState.add_parameter(DiagParameter('WASCenterCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    MaintenanceNextServiceHours = DiagMessage(0x1330, 'MaintenanceNextServiceHours', [1, 3, 4, 64], None, '', 1)
    MaintenanceNextServiceHours.add_parameter(DiagParameter('MaintenanceNSHs', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 4294967295, 'Next Maintenance Service Hours', False, False, False))

    TractorHoursOffset = DiagMessage(0x1331, 'TractorHoursOffset', [1, 3, 4, 64], None, '', 1)
    TractorHoursOffset.add_parameter(DiagParameter('TractorHoursOffset', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -2147483646, 2147483646, 'Tractor Hours Offset 0.1h', False, False, False))

    CurrentTractorWheelSize = DiagMessage(0x1332, 'CurrentTractorWheelSize', [1, 3, 4, 64], None, '', 1)
    CurrentTractorWheelSize.add_parameter(DiagParameter('CurrentTractorWhlSze', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 3000, 7500, 'Current Tractor WheelSize in mm', False, False, False))

    TractorWheelMaxSize = DiagMessage(0x1333, 'TractorWheelMaxSize', [1, 3, 4, 64], None, '', 1)
    TractorWheelMaxSize.add_parameter(DiagParameter('TractorWlMxSze', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 3000, 7500, 'Tractor Wheel Max Size in mm', False, False, False))

    EngineHoursMemo = DiagMessage(0x1334, 'EngineHoursMemo', [1, 3, 4, 64], None, '', 1)
    EngineHoursMemo.add_parameter(DiagParameter('HoursMemo', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 2147483646, '', False, False, False))

    UdsDiag_GetAntiStallStatus = DiagMessage(0xA701, 'UdsDiag_GetAntiStallStatus', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetAntiStallStatus.add_parameter(DiagParameter('AntiStallStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X635][250-DI_01][AMT-DCT-CVT][L-M-H][raw][SRC14][Y][0]#[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X2][250-DI_1][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))

    UdsDiag_GetPTOAutoState = DiagMessage(0xA702, 'UdsDiag_GetPTOAutoState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPTOAutoState.add_parameter(DiagParameter('PTOAutoState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetTractorSpeed = DiagMessage(0xA711, 'UdsDiag_GetTractorSpeed', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetTractorSpeed.add_parameter(DiagParameter('TractorActualSpeed', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '[1][S2-S3-M1][Transmission][ ][ ][D4-D6][L-S][conv][SRC14][N_N_N][0_0_0]#[1][S3-M1][Transmission][X10_Val][113-FI_02][CVT][S][conv][SRC14][N_N][0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    PIN_250_DI_01 = DiagMessage(0xA800, 'PIN_250_DI_01', [1, 3, 4, 64], None, '', 6)
    PIN_250_DI_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Miscellaneous][X990][250-DI_01][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X635][250-DI_01][AMT-DCT-CVT][L-M-H][raw][SRC14][Y][0]#[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X2][250-DI_1][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_236_DI_02 = DiagMessage(0xA801, 'PIN_236_DI_02', [1, 3, 4, 64], None, '', 6)
    PIN_236_DI_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][M2_19-M2_21-H2_22][Linkage][X636][236-DI_02][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][PTO][X94_A-X94_B][236-DI_02][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_209_DI_03 = DiagMessage(0xA802, 'PIN_209_DI_03', [1, 3, 4, 64], None, '', 6)
    PIN_209_DI_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Cab_commands][X717][209-DI_03][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X182][209-DI_03][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_147_DI_04 = DiagMessage(0xA803, 'PIN_147_DI_04', [1, 3, 4, 64], None, '', 6)
    PIN_147_DI_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X68][147-DI_04][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X68][147-DI_04][AMT-DCT-CVT][L-M-H][raw][SRC14][ ][0]#[1][M2_19-M2_21-H2_22][Linkage][X209][147-DI_04][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_223_DI_05 = DiagMessage(0xA804, 'PIN_223_DI_05', [1, 3, 4, 64], None, '', 6)
    PIN_223_DI_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Transmission][X19-B14][223-DI_05][CVT][S][raw][SRC14][N_N][0_0]#[1][M2][Cab_commands][X618][223-DI_05][ ][ ][raw][SRC14][Y][1]', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_148_DI_06 = DiagMessage(0xA805, 'PIN_148_DI_06', [1, 3, 4, 64], None, '', 6)
    PIN_148_DI_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X68][148-DI_06][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X68][148-DI_6][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_159_DI_07 = DiagMessage(0xA806, 'PIN_159_DI_07', [1, 3, 4, 64], None, '', 6)
    PIN_159_DI_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Transmission][X10_Dir][159-DI_07][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Light][X1050][159-DI_07][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_158_DI_08 = DiagMessage(0xA807, 'PIN_158_DI_08', [1, 3, 4, 64], None, '', 6)
    PIN_158_DI_08.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Transmission][X18][158-DI_08][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Light][X1050][158-DI_08][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_214_DI_09 = DiagMessage(0xA808, 'PIN_214_DI_09', [1, 3, 4, 64], None, '', 6)
    PIN_214_DI_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X56][214-DI_09][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X56][214-DI_09][AMT-DCT-CVT][L-M-H][raw][SRC14][ ][0]#[1][M2_19-M2_21-H2_22][Light][X138-X652][214-DI_09][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][2_0_0]', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_157_DI_10 = DiagMessage(0xA809, 'PIN_157_DI_10', [1, 3, 4, 64], None, '', 6)
    PIN_157_DI_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Transmission][X8_Dir][157-DI_10][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19][Auxiliary_hydraulic][X1017][157-DI_10][AMT-DCT][L-M-H][raw][SRC14][Y][0]', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_252_DI_11 = DiagMessage(0xA80A, 'PIN_252_DI_11', [1, 3, 4, 64], None, '', 6)
    PIN_252_DI_11.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][M2_19-M2_21-H2_22][Cab_commands][X404][252-DI_11][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X1017][252-DI_11][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_238_DI_12 = DiagMessage(0xA80B, 'PIN_238_DI_12', [1, 3, 4, 64], None, '', 6)
    PIN_238_DI_12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2][Linkage][X1118][238-DI_12][D4-D6][L-S][raw][SRC14][Y][1]', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_222_DI_13 = DiagMessage(0xA80C, 'PIN_222_DI_13', [1, 3, 4, 64], None, '', 6)
    PIN_222_DI_13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Cab_commands][X67][222-DI_13][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X67][222-DI_13][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_210_DI_14 = DiagMessage(0xA80D, 'PIN_210_DI_14', [1, 3, 4, 64], None, '', 6)
    PIN_210_DI_14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Cab_commands][X66][210-DI_14][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X66][210-DI_14][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_136_DI_15 = DiagMessage(0xA80E, 'PIN_136_DI_15', [1, 3, 4, 64], None, '', 6)
    PIN_136_DI_15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X56][136-DI_15][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_137_DI_16 = DiagMessage(0xA80F, 'PIN_137_DI_16', [1, 3, 4, 64], None, '', 6)
    PIN_137_DI_16.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2][Linkage][X1118][137-DI_16][D4-D6][L-S][raw][SRC14][Y][1]#[1][S3-M1][Cab_commands][X72][137-DI_16][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X739][137-DI_16][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_135_DI_17 = DiagMessage(0xA810, 'PIN_135_DI_17', [1, 3, 4, 64], None, '', 6)
    PIN_135_DI_17.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Steering_system][X23-S169][135-DI_17][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X184][135-DI_17][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_134_DI_18 = DiagMessage(0xA811, 'PIN_134_DI_18', [1, 3, 4, 64], None, '', 6)
    PIN_134_DI_18.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Transmission][X20][134-DI_18][CVT][S][raw][SRC14][N_N][0_0]#[1][M2][Braking_system][X1077][134-DI_18][ ][ ][raw][SRC14][Y][0]#[1][M2_19][Steering_system][X23][134-DI_18][AMT-DCT][L-M-H][raw][SRC14][Y][2]', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_211_DI_19 = DiagMessage(0xA812, 'PIN_211_DI_19', [1, 3, 4, 64], None, '', 6)
    PIN_211_DI_19.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X87-X97][211-DI_19][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X87-X97][211-DI_06][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_144_DI_20 = DiagMessage(0xA813, 'PIN_144_DI_20', [1, 3, 4, 64], None, '', 6)
    PIN_144_DI_20.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Braking_system][X996-S170][144-DI_20][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X72][144-DI_20][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_224_DI_21 = DiagMessage(0xA814, 'PIN_224_DI_21', [1, 3, 4, 64], None, '', 6)
    PIN_224_DI_21.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X664-X665][224-DI_21][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X87-X97][224][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_143_DI_22 = DiagMessage(0xA815, 'PIN_143_DI_22', [1, 3, 4, 64], None, '', 6)
    PIN_143_DI_22.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Braking_system][X618][143-DI_22][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_142_DI_23 = DiagMessage(0xA816, 'PIN_142_DI_23', [1, 3, 4, 64], None, '', 6)
    PIN_142_DI_23.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Braking_system][X984-X988][142-DI_23][D6-CVT][L-S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X984-X988][142-DI_23][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_235_DI_24 = DiagMessage(0xA817, 'PIN_235_DI_24', [1, 3, 4, 64], None, '', 6)
    PIN_235_DI_24.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X739][235-DI_24][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X990][235-DI_24][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_247_DI_25 = DiagMessage(0xA818, 'PIN_247_DI_25', [1, 3, 4, 64], None, '', 6)
    PIN_247_DI_25.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X363][247-DI_25][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21][Air_conditionning][X252-X318][247-DI_25][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N][1_0]', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_234_DI_26 = DiagMessage(0xA819, 'PIN_234_DI_26', [1, 3, 4, 64], None, '', 6)
    PIN_234_DI_26.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X363][234-DI_26][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_225_DI_27 = DiagMessage(0xA81A, 'PIN_225_DI_27', [1, 3, 4, 64], None, '', 6)
    PIN_225_DI_27.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S3-M1][Braking_system][X21][225-DI_27][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X277][225-DI_27][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_212_DI_28 = DiagMessage(0xA81B, 'PIN_212_DI_28', [1, 3, 4, 64], None, '', 6)
    PIN_212_DI_28.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X277][212-DI_28][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X277][212-DI_28][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_248_DI_29 = DiagMessage(0xA81C, 'PIN_248_DI_29', [1, 3, 4, 64], None, '', 6)
    PIN_248_DI_29.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Braking_system][X618][248-DI_29][D4-D6][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2][Braking_system][X683][248-DI_29][ ][ ][raw][SRC14][Y][2]', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_237_DI_30 = DiagMessage(0xA81D, 'PIN_237_DI_30', [1, 3, 4, 64], None, '', 6)
    PIN_237_DI_30.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X277][237-DI_30][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_239_DI_31 = DiagMessage(0xA81E, 'PIN_239_DI_31', [1, 3, 4, 64], None, '', 6)
    PIN_239_DI_31.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][S2-S3-M1][Cab_commands][X96][239-DI_31][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X95-X96][239-DI_31][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_251_DI_32 = DiagMessage(0xA81F, 'PIN_251_DI_32', [1, 3, 4, 64], None, '', 6)
    PIN_251_DI_32.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'32': [32, 32]}, 32, 32, '', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X95-X96][251-DI_32][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_256_DOH_01 = DiagMessage(0xA828, 'PIN_256_DOH_01', [1, 3, 4, 64], None, '', 4)
    PIN_256_DOH_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_256_DOH_01.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_256_DOH_01.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S3-M1][Transmission][X18][256-DOH_01][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Light][not_on_EFD][256-DOH_01][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19][Miscellaneous][ ][256-DOH_1][AMT-DCT][L-M-H][raw][SRC14][Y][0]', False, False, False))
    PIN_256_DOH_01.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_257_DOH_02 = DiagMessage(0xA829, 'PIN_257_DOH_02', [1, 3, 4, 64], None, '', 4)
    PIN_257_DOH_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_257_DOH_02.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_257_DOH_02.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands_state][X717][257-DOH_02][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X92-X77-X220-X1097(through_relay_K13)][257-DOH_02][AMT-DCT-CVT][L-M-H][raw][SRC14][ ][0]#[1][M2_19-M2_21-H2_22][Light][not_on_EFD][257-DOH_02][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_257_DOH_02.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_241_DOH_03 = DiagMessage(0xA82A, 'PIN_241_DOH_03', [1, 3, 4, 64], None, '', 4)
    PIN_241_DOH_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_241_DOH_03.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_241_DOH_03.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][X994][241-DOH_03][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Miscellaneous][X467B-X468B][241-DOH_3][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_241_DOH_03.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_242_DOH_04 = DiagMessage(0xA82B, 'PIN_242_DOH_04', [1, 3, 4, 64], None, '', 4)
    PIN_242_DOH_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_242_DOH_04.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_242_DOH_04.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Braking_system][X987_through_relay_X993-Y71][242-DOH_4][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Steering_system][X210-X236][242-DOH_4][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_242_DOH_04.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_114_DOH_05 = DiagMessage(0xA82C, 'PIN_114_DOH_05', [1, 3, 4, 64], None, '', 4)
    PIN_114_DOH_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_114_DOH_05.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_114_DOH_05.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][K7][114-DOH_05][D6-CVT][S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Miscellaneous][X151][114-DOH_5][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_114_DOH_05.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_244_DOH_07 = DiagMessage(0xA82D, 'PIN_244_DOH_07', [1, 3, 4, 64], None, '', 4)
    PIN_244_DOH_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_244_DOH_07.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_244_DOH_07.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][K28][244-DOH_07][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Light][X385-X386-X387-X388(through_K7R)][244-DOH_07][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Miscellaneous][X218-X1052(through_relay_K2I)][244-DOH_7][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_244_DOH_07.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_102_DOH_10 = DiagMessage(0xA82E, 'PIN_102_DOH_10', [1, 3, 4, 64], None, '', 4)
    PIN_102_DOH_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_102_DOH_10.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_102_DOH_10.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][ENG109][102-DOH_10][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Light][X379-X380-X381-X382(through_K9R)][102-DOH_10][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_102_DOH_10.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_103_DOH_12 = DiagMessage(0xA82F, 'PIN_103_DOH_12', [1, 3, 4, 64], None, '', 4)
    PIN_103_DOH_12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_103_DOH_12.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_103_DOH_12.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][ENG109][103-DOH_12][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Light][X405-X408(through_K10R)-X967(through_K14)][103-DOH_12][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_103_DOH_12.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_105_DOH_13 = DiagMessage(0xA830, 'PIN_105_DOH_13', [1, 3, 4, 64], None, '', 4)
    PIN_105_DOH_13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_105_DOH_13.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_105_DOH_13.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands_state][X717][105-DOH_13][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Light][X1102(through_K8)-X365(through_K11R)][105-DOH_13][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Light][X216-X1097(through_K12)][105-DOH_13][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][2_0_0]', False, False, False))
    PIN_105_DOH_13.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_128_DOH_14 = DiagMessage(0xA831, 'PIN_128_DOH_14', [1, 3, 4, 64], None, '', 4)
    PIN_128_DOH_14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_128_DOH_14.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_128_DOH_14.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][K8][128-DOH_14][D6-CVT][S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Light][X1029-X1030][128-DOH_14][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_128_DOH_14.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_127_DOH_15 = DiagMessage(0xA832, 'PIN_127_DOH_15', [1, 3, 4, 64], None, '', 4)
    PIN_127_DOH_15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_127_DOH_15.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_127_DOH_15.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S3-M1][Miscellaneous][K24][127-DOH_15][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Light][X223(through_K2T)-X93-X78(through_K13R)][127-DOH_15][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_127_DOH_15.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_106_DOH_16 = DiagMessage(0xA833, 'PIN_106_DOH_16', [1, 3, 4, 64], None, '', 4)
    PIN_106_DOH_16.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_106_DOH_16.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'12': [12, 12]}, 12, 12, '', False, False, False))
    PIN_106_DOH_16.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][X961][106-DOH_16][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][2_0_0]#[1][M2_19-M2_21-H2_22][Light][X1102(through_K15)-X409-X410(trhough_K12R)][106-DOH_16][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Miscellaneous][X218-X1052(through_relay_K1I)][106-DOH_16][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_106_DOH_16.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_119_AI_01 = DiagMessage(0xA850, 'PIN_119_AI_01', [1, 3, 4, 64], None, '', 5)
    PIN_119_AI_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_119_AI_01.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_119_AI_01.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_119_AI_01.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][M2_19-M2_21-H2_22][Braking_system][X1068][119-AI_01][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Light][X928][119-AI_01][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_119_AI_01.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_120_AI_02 = DiagMessage(0xA851, 'PIN_120_AI_02', [1, 3, 4, 64], None, '', 5)
    PIN_120_AI_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_120_AI_02.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_120_AI_02.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_120_AI_02.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][S2-S3-M1][Cab_commands][X56][120-AI_02][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X996][120-AI_2][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_120_AI_02.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_121_AI_03 = DiagMessage(0xA852, 'PIN_121_AI_03', [1, 3, 4, 64], None, '', 5)
    PIN_121_AI_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_121_AI_03.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_121_AI_03.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_121_AI_03.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][S2-S3-M1][Linkage][X30-B1E][121-AI_03][D4-D6][L-S][raw][SRC14][Y_N_N][1]#[1][S3-M1][Braking_system][X135][121-AI_03][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X21][121-AI_03][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_121_AI_03.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_116_AI_04 = DiagMessage(0xA853, 'PIN_116_AI_04', [1, 3, 4, 64], None, '', 5)
    PIN_116_AI_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_116_AI_04.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_116_AI_04.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_116_AI_04.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][S2-S3-M1][Linkage][X32-B2E][116-AI_04][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X32][116-AI_04(KMB)][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_116_AI_04.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_117_AI_05 = DiagMessage(0xA854, 'PIN_117_AI_05', [1, 3, 4, 64], None, '', 5)
    PIN_117_AI_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_117_AI_05.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_117_AI_05.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_117_AI_05.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][M2_19-M2_21-H2_22][Braking_system][X1067][117-AI_05][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_117_AI_05.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_118_AI_06 = DiagMessage(0xA855, 'PIN_118_AI_06', [1, 3, 4, 64], None, '', 5)
    PIN_118_AI_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_118_AI_06.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_118_AI_06.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_118_AI_06.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][M2_19-M2_21-H2_22][Cab_commands][X56][118-AI_06][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_118_AI_06.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_231_AI_07 = DiagMessage(0xA856, 'PIN_231_AI_07', [1, 3, 4, 64], None, '', 5)
    PIN_231_AI_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_231_AI_07.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_231_AI_07.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_231_AI_07.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][S2-S3-M1][Linkage][X31-B3E][231-AI_07][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X1078][231-AI_07][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X31][231-AI_07(KMB)][AMT_DCT_CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_231_AI_07.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_217_AI_08 = DiagMessage(0xA857, 'PIN_217_AI_08', [1, 3, 4, 64], None, '', 5)
    PIN_217_AI_08.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_217_AI_08.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_217_AI_08.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_217_AI_08.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][S3-M1][Braking_system][X35][217-AI_08][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_217_AI_08.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_213_AI_09 = DiagMessage(0xA858, 'PIN_213_AI_09', [1, 3, 4, 64], None, '', 5)
    PIN_213_AI_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_213_AI_09.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_213_AI_09.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_213_AI_09.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][S2-S3-M1][Cab_commands][X68][213-AI_09][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X68][213-AI_9][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_213_AI_09.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_226_AI_10 = DiagMessage(0xA859, 'PIN_226_AI_10', [1, 3, 4, 64], None, '', 5)
    PIN_226_AI_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_226_AI_10.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_226_AI_10.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_226_AI_10.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][S3-M1][Steering_system][X235][226-AI_10][D6-CVT][L-S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X71][226-AI_10][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_226_AI_10.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_228_AI_11 = DiagMessage(0xA85A, 'PIN_228_AI_11', [1, 3, 4, 64], None, '', 5)
    PIN_228_AI_11.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_228_AI_11.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_228_AI_11.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_228_AI_11.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][M2_19-M2_21-H2_22][Linkage][X1053][228-AI_11][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_228_AI_11.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_188_AI_12 = DiagMessage(0xA85B, 'PIN_188_AI_12', [1, 3, 4, 64], None, '', 5)
    PIN_188_AI_12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_188_AI_12.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_188_AI_12.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_188_AI_12.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '[1][S3-M1][Linkage][X211][188-AI_12][D6-CVT][L-S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X211][188-AI_12][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_188_AI_12.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_218_CI_03 = DiagMessage(0xA85C, 'PIN_218_CI_03', [1, 3, 4, 64], None, '', 5)
    PIN_218_CI_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_218_CI_03.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_218_CI_03.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_218_CI_03.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S2][Steering_system][X235-B2C][218-CI_03][D4-D6][L-S][raw][SRC14][Y][1]#[1][M2_19-M2_21-H2_22][Steering_system][X235][218-CI_03][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_218_CI_03.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_229_CI_04 = DiagMessage(0xA85D, 'PIN_229_CI_04', [1, 3, 4, 64], None, '', 5)
    PIN_229_CI_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_229_CI_04.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_229_CI_04.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_229_CI_04.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S3-M1][Linkage][X279][229-CI_04][D6-CVT][L-S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X279][229-CI_04][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_229_CI_04.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_171_CI_05 = DiagMessage(0xA85E, 'PIN_171_CI_05', [1, 3, 4, 64], None, '', 5)
    PIN_171_CI_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_171_CI_05.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_171_CI_05.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_171_CI_05.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S3-M1][Linkage][X30][171-CI_05][CVT][S][raw][SRC14][Y_Y][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X30][171-CI_05][AMT-DCT-CVT][L-M-H][raw][SRC14][ ][0_0_0]', False, False, False))
    PIN_171_CI_05.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_227_CI_06 = DiagMessage(0xA85F, 'PIN_227_CI_06', [1, 3, 4, 64], None, '', 5)
    PIN_227_CI_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_227_CI_06.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_227_CI_06.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_227_CI_06.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][M2_19-M2_21-H2_22][Front_axle_susp][X166][227-CI_06][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_227_CI_06.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_167_CI_07 = DiagMessage(0xA860, 'PIN_167_CI_07', [1, 3, 4, 64], None, '', 5)
    PIN_167_CI_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_167_CI_07.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_167_CI_07.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_167_CI_07.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S3-M1][Transmission][X9][167-CI_07][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_167_CI_07.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_170_CI_09 = DiagMessage(0xA861, 'PIN_170_CI_09', [1, 3, 4, 64], None, '', 5)
    PIN_170_CI_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_170_CI_09.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_170_CI_09.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_170_CI_09.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S3-M1][Transmission][X34][170-CI_09][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_170_CI_09.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_165_CI_10 = DiagMessage(0xA862, 'PIN_165_CI_10', [1, 3, 4, 64], None, '', 5)
    PIN_165_CI_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_165_CI_10.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_165_CI_10.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_165_CI_10.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S2][Braking_system][X1077-B51][165-CI_10][D4-D6][L-S][raw][SRC14][Y][2]', False, False, False))
    PIN_165_CI_10.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_230_CI_11 = DiagMessage(0xA863, 'PIN_230_CI_11', [1, 3, 4, 64], None, '', 5)
    PIN_230_CI_11.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_230_CI_11.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_230_CI_11.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_230_CI_11.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_230_CI_11.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_140_CI_12 = DiagMessage(0xA864, 'PIN_140_CI_12', [1, 3, 4, 64], None, '', 5)
    PIN_140_CI_12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_140_CI_12.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_140_CI_12.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_140_CI_12.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_140_CI_12.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_139_CI_13 = DiagMessage(0xA865, 'PIN_139_CI_13', [1, 3, 4, 64], None, '', 5)
    PIN_139_CI_13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_139_CI_13.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_139_CI_13.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_139_CI_13.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S3-M1][Transmission][X17][139-CI_13][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_139_CI_13.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_166_CI_14 = DiagMessage(0xA866, 'PIN_166_CI_14', [1, 3, 4, 64], None, '', 5)
    PIN_166_CI_14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_166_CI_14.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_166_CI_14.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_166_CI_14.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_166_CI_14.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_164_CI_15 = DiagMessage(0xA867, 'PIN_164_CI_15', [1, 3, 4, 64], None, '', 5)
    PIN_164_CI_15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_164_CI_15.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_164_CI_15.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_164_CI_15.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S2][Braking_system][X1078-B42][164-CI_15][D4-D6][L-S][raw][SRC14][Y][2]', False, False, False))
    PIN_164_CI_15.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_141_CI_16 = DiagMessage(0xA868, 'PIN_141_CI_16', [1, 3, 4, 64], None, '', 5)
    PIN_141_CI_16.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_141_CI_16.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'25': [25, 25]}, 25, 25, '', False, False, False))
    PIN_141_CI_16.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_141_CI_16.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][M2_19-M2_21-H2_22][Braking_system][X1063][141-CI_16][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_141_CI_16.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_221_AO_01 = DiagMessage(0xA878, 'PIN_221_AO_01', [1, 3, 4, 64], None, '', 5)
    PIN_221_AO_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_221_AO_01.add_parameter(DiagParameter('TotalNOfAO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 1, '', False, False, False))
    PIN_221_AO_01.add_parameter(DiagParameter('DigitalConversionAnalog', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'Digital to Analog Conversion value', False, False, False))
    PIN_221_AO_01.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '[1][S3-M1][Cab_commands][X175][221-AO_01][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_221_AO_01.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '', False, False, False))

    PIN_112_DFI_01 = DiagMessage(0xA8A0, 'PIN_112_DFI_01', [1, 3, 4, 64], None, '', 6)
    PIN_112_DFI_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'8': [8, 8]}, 8, 8, '', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '[1][S2-S3-M1][Transmission][X22-B25][112-FI_01][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Transmission][X22][112-FI_1][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_113_DFI_02 = DiagMessage(0xA8A1, 'PIN_113_DFI_02', [1, 3, 4, 64], None, '', 6)
    PIN_113_DFI_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'8': [8, 8]}, 8, 8, '', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '[1][S3-M1][Transmission][X10_Val][113-FI_02][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_110_DFI_03 = DiagMessage(0xA8A2, 'PIN_110_DFI_03', [1, 3, 4, 64], None, '', 6)
    PIN_110_DFI_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'8': [8, 8]}, 8, 8, '', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '[1][S3-M1][PTO][X16][110-FI_03][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_111_DFI_04 = DiagMessage(0xA8A3, 'PIN_111_DFI_04', [1, 3, 4, 64], None, '', 6)
    PIN_111_DFI_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'8': [8, 8]}, 8, 8, '', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '[1][S3-M1][Transmission][X25][111-FI_04][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_109_DFI_05 = DiagMessage(0xA8A4, 'PIN_109_DFI_05', [1, 3, 4, 64], None, '', 6)
    PIN_109_DFI_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'8': [8, 8]}, 8, 8, '', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '[1][S3-M1][Transmission][X8_Val][109-FI_05][CVT][S][raw][SRC14][Y_Y][0_0]', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_108_DFI_06 = DiagMessage(0xA8A5, 'PIN_108_DFI_06', [1, 3, 4, 64], None, '', 6)
    PIN_108_DFI_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'8': [8, 8]}, 8, 8, '', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_133_DFI_07 = DiagMessage(0xA8A6, 'PIN_133_DFI_07', [1, 3, 4, 64], None, '', 6)
    PIN_133_DFI_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'8': [8, 8]}, 8, 8, '', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '[1][S3-M1][PTO][X15][133-FI_07][CVT][S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_132_DFI_08 = DiagMessage(0xA8A7, 'PIN_132_DFI_08', [1, 3, 4, 64], None, '', 6)
    PIN_132_DFI_08.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'8': [8, 8]}, 8, 8, '', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_177_POH_02 = DiagMessage(0xA8C8, 'PIN_177_POH_02', [1, 3, 4, 64], None, '', 5)
    PIN_177_POH_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_177_POH_02.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_177_POH_02.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_177_POH_02.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][PTO][X7-Y2][177-POH_02][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X337][177-POH_02][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][PTO][X7][177-POH_02][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][2_0_0]', False, False, False))
    PIN_177_POH_02.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_186_POH_04 = DiagMessage(0xA8C9, 'PIN_186_POH_04', [1, 3, 4, 64], None, '', 5)
    PIN_186_POH_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_186_POH_04.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_186_POH_04.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_186_POH_04.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2-S3-M1][PTO][X281-Y9][186-POH_04][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19][Braking_system][X339][186-POH_04][AMT-DCT][L-M-H][raw][SRC14][ ][0]#[1][M2_19-M2_21-H2_22][PTO][X281][186-POH_04][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_186_POH_04.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_175_POH_06 = DiagMessage(0xA8CB, 'PIN_175_POH_06', [1, 3, 4, 64], None, '', 5)
    PIN_175_POH_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_175_POH_06.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_175_POH_06.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_175_POH_06.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Transmission][X11][175-POH_06][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19][Auxiliary_hydraulic][X727][175-POH_06][AMT-DCT][L-M-H][raw][SRC14][Y][0]', False, False, False))
    PIN_175_POH_06.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_152_POH_07 = DiagMessage(0xA8CC, 'PIN_152_POH_07', [1, 3, 4, 64], None, '', 5)
    PIN_152_POH_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_152_POH_07.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_152_POH_07.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_152_POH_07.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Braking_system][X38][152-POH_07][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X985][152-POH_07][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_152_POH_07.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_149_POH_09 = DiagMessage(0xA8CD, 'PIN_149_POH_09', [1, 3, 4, 64], None, '', 5)
    PIN_149_POH_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_149_POH_09.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_149_POH_09.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_149_POH_09.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Linkage][X27][149-POH_09][D6-CVT][L-S][raw][SRC14][N_N][0_0]#[1][M2_19][Linkage][X368][149-POH_09(EHR)][AMT-DCT][L-M-H][raw][SRC14][Y][0]', False, False, False))
    PIN_149_POH_09.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_173_POH_10 = DiagMessage(0xA8CE, 'PIN_173_POH_10', [1, 3, 4, 64], None, '', 5)
    PIN_173_POH_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_173_POH_10.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_173_POH_10.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_173_POH_10.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2][Braking_system][X1075-Y79][173-POH_10][D4-D6][L-S][raw][SRC14][Y][2]#[1][S3-M1][Linkage][X28][173-POH_10][D6-CVT][L-S][raw][SRC14][N_N][0_0]#[1][M2_19][Linkage][X368][173-POH_10(EHR)][AMT-DCT][L-M-H][raw][SRC14][Y][0]', False, False, False))
    PIN_173_POH_10.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_126_POH_17 = DiagMessage(0xA8CF, 'PIN_126_POH_17', [1, 3, 4, 64], None, '', 5)
    PIN_126_POH_17.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_126_POH_17.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_126_POH_17.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_126_POH_17.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2-S3-M1][Braking_system][X339-Y69][126-POH_17][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X39][126-POH_17][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_126_POH_17.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_190_PDOH_03 = DiagMessage(0xA8D0, 'PIN_190_PDOH_03', [1, 3, 4, 64], None, '', 5)
    PIN_190_PDOH_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_190_PDOH_03.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_190_PDOH_03.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_190_PDOH_03.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 100, '[1][S3-M1][Difflock][X6-Y1][190-PDOH_03][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Difflock][X6][190-PDOH_03][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Miscellaneous][X153][190-PDOH_3][AMT-DCT-CVT][L-M-H][raw][SRC14_IO][Y_N_N][0_0_0]', False, False, False))
    PIN_190_PDOH_03.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_189_PDOH_04 = DiagMessage(0xA8D1, 'PIN_189_PDOH_04', [1, 3, 4, 64], None, '', 5)
    PIN_189_PDOH_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_189_PDOH_04.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_189_PDOH_04.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_189_PDOH_04.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2][Miscellaneous][ ][189-PDOH_04][D4-D6][L-S][raw][SRC14][Y][0]#[1][S3-M1][4WD][X5][189-PDOH_04][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Front_axle_susp][X163][189-PDOH_04][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Miscellaneous][X153][189-PDOH_4][AMT-DCT-CVT][L-M-H][raw][SRC14_IO][Y_N_N][0_0_0]', False, False, False))
    PIN_189_PDOH_04.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_194_PDOH_05 = DiagMessage(0xA8D2, 'PIN_194_PDOH_05', [1, 3, 4, 64], None, '', 5)
    PIN_194_PDOH_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_194_PDOH_05.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_194_PDOH_05.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_194_PDOH_05.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Linkage][X727][194-PDOH_05][D4-D6][L-S][raw][SRC14][N_N][0_0]#[1][S3-M1][Transmission][X14][194-PDOH_05][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][PTO][X153][194-PDOH_05][AMT-DCT-CVT][L-M-H][raw][SRC14_IO][Y_N_N][0_0_0]', False, False, False))
    PIN_194_PDOH_05.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_193_PDOH_06 = DiagMessage(0xA8D3, 'PIN_193_PDOH_06', [1, 3, 4, 64], None, '', 5)
    PIN_193_PDOH_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_193_PDOH_06.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_193_PDOH_06.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_193_PDOH_06.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2][Braking_system][X1075-Y79][193-PDOH_06][D4-D6][L-S][raw][SRC14][Y][1]#[1][S3-M1][Transmission][X13][193-PDOH_06][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X153][193-PDOH_06][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_193_PDOH_06.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_187_PDOH_08 = DiagMessage(0xA8D4, 'PIN_187_PDOH_08', [1, 3, 4, 64], None, '', 5)
    PIN_187_PDOH_08.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_187_PDOH_08.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_187_PDOH_08.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_187_PDOH_08.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Braking_system][X337][187-PDOH_08][D6-CVT][L-S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X153][187-PDOH_08][AMT-DCt-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_187_PDOH_08.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_196_PDOH_09 = DiagMessage(0xA8D5, 'PIN_196_PDOH_09', [1, 3, 4, 64], None, '', 5)
    PIN_196_PDOH_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_196_PDOH_09.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_196_PDOH_09.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_196_PDOH_09.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Braking_system][X39][196-PDOH_09][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X38][196-PDOH_17][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X43][196-PDOH_09][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_196_PDOH_09.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_249_PDOH_10 = DiagMessage(0xA8D6, 'PIN_249_PDOH_10', [1, 3, 4, 64], None, '', 5)
    PIN_249_PDOH_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_249_PDOH_10.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_249_PDOH_10.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_249_PDOH_10.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 100, '[1][S3-M1][Braking_system][X37][249-PDOH_10][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X37][249-PDOH_10][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X44][249-PDOH_10][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_249_PDOH_10.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_153_PDOH_13 = DiagMessage(0xA8D7, 'PIN_153_PDOH_13', [1, 3, 4, 64], None, '', 5)
    PIN_153_PDOH_13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_153_PDOH_13.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_153_PDOH_13.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_153_PDOH_13.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2][Linkage][X43][153-PDOH_13][D4-D6][L-S][raw][SRC14][Y][1]#[1][S3-M1][PTO][X774][153-PDOH_13][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][PTO][X3][153-PDOH_13][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_153_PDOH_13.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_154_PDOH_14 = DiagMessage(0xA8D8, 'PIN_154_PDOH_14', [1, 3, 4, 64], None, '', 5)
    PIN_154_PDOH_14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_154_PDOH_14.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_154_PDOH_14.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_154_PDOH_14.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2][Linkage][X44][154-PDOH_14][D4-D6][L-S][raw][SRC14][Y][1]#[1][S3-M1][PTO][X892][154-PDOH_14][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][PTO][X892][154-PDOH_14][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_154_PDOH_14.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_176_PDOH_15 = DiagMessage(0xA8D9, 'PIN_176_PDOH_15', [1, 3, 4, 64], None, '', 5)
    PIN_176_PDOH_15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_176_PDOH_15.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_176_PDOH_15.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_176_PDOH_15.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][PTO][X4][176-PDOH_15][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][PTO][X599][176-PDOH_15][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_176_PDOH_15.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_129_PDOH_16 = DiagMessage(0xA8DA, 'PIN_129_PDOH_16', [1, 3, 4, 64], None, '', 5)
    PIN_129_PDOH_16.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_129_PDOH_16.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_129_PDOH_16.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_129_PDOH_16.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][PTO][X599][129-PDOH_16][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][PTO][X4][129-PDOH_16][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_129_PDOH_16.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_130_PDOH_17 = DiagMessage(0xA8DB, 'PIN_130_PDOH_17', [1, 3, 4, 64], None, '', 5)
    PIN_130_PDOH_17.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_130_PDOH_17.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_130_PDOH_17.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_130_PDOH_17.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Braking_system][X985_X1004][130-PDOH_17][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Front_axle_susp][X159][130-PDOH_17][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_130_PDOH_17.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_107_PDOH_18 = DiagMessage(0xA8DC, 'PIN_107_PDOH_18', [1, 3, 4, 64], None, '', 5)
    PIN_107_PDOH_18.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_107_PDOH_18.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_107_PDOH_18.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_107_PDOH_18.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Miscellaneous][K15][107-PDOH_18][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Front_axle_susp][X154][107-PDOH_18][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_107_PDOH_18.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_104_PDOH_19 = DiagMessage(0xA8DD, 'PIN_104_PDOH_19', [1, 3, 4, 64], None, '', 5)
    PIN_104_PDOH_19.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_104_PDOH_19.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_104_PDOH_19.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_104_PDOH_19.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2-S3-M1][Miscellaneous][X618-X739_Supply][104-PDOH_19][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Front_axle_susp][X161][104-PDOH_19][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_104_PDOH_19.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_115_PDOH_20 = DiagMessage(0xA8DE, 'PIN_115_PDOH_20', [1, 3, 4, 64], None, '', 5)
    PIN_115_PDOH_20.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_115_PDOH_20.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_115_PDOH_20.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_115_PDOH_20.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2-S3-M1][Auxiliary_hydraulic][X654-Y37][115-PDOH_20][D4-D6-CVT][S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X1075][115-PDOH_20][AMT-DCT-CVT][L-M-H][raw][SRC14][ ][0]#[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X654][115-PDOH_20][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_115_PDOH_20.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_243_PDOH_21 = DiagMessage(0xA8DF, 'PIN_243_PDOH_21', [1, 3, 4, 64], None, '', 5)
    PIN_243_PDOH_21.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_243_PDOH_21.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_243_PDOH_21.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_243_PDOH_21.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2-S3-M1][Steering_system][X372-Y1C3][243-PDOH_21][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X1075][243-PDOH_21][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Steering_system][X372][243-PDOH_21][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    PIN_243_PDOH_21.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_179_DOL_01 = DiagMessage(0xA8E0, 'PIN_179_DOL_01', [1, 3, 4, 64], None, '', 5)
    PIN_179_DOL_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_179_DOL_01.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_179_DOL_01.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_179_DOL_01.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_179_DOL_01.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_191_DOL_02 = DiagMessage(0xA8E1, 'PIN_191_DOL_02', [1, 3, 4, 64], None, '', 5)
    PIN_191_DOL_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_191_DOL_02.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_191_DOL_02.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_191_DOL_02.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_191_DOL_02.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_192_DOL_03 = DiagMessage(0xA8E2, 'PIN_192_DOL_03', [1, 3, 4, 64], None, '', 5)
    PIN_192_DOL_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_192_DOL_03.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_192_DOL_03.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_192_DOL_03.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_192_DOL_03.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_150_DOL_04 = DiagMessage(0xA8E3, 'PIN_150_DOL_04', [1, 3, 4, 64], None, '', 5)
    PIN_150_DOL_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_150_DOL_04.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_150_DOL_04.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_150_DOL_04.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_150_DOL_04.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_174_DOL_05 = DiagMessage(0xA8E4, 'PIN_174_DOL_05', [1, 3, 4, 64], None, '', 5)
    PIN_174_DOL_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_174_DOL_05.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_174_DOL_05.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_174_DOL_05.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_174_DOL_05.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_181_DOL_06 = DiagMessage(0xA8E5, 'PIN_181_DOL_06', [1, 3, 4, 64], None, '', 5)
    PIN_181_DOL_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_181_DOL_06.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_181_DOL_06.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_181_DOL_06.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 500, '', False, False, False))
    PIN_181_DOL_06.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_178_POL_01 = DiagMessage(0xA8E6, 'PIN_178_POL_01', [1, 3, 4, 64], None, '', 5)
    PIN_178_POL_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_178_POL_01.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_178_POL_01.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_178_POL_01.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][Linkage][X27-X28][178-POL_01][D6-CVT][L-S][raw][SRC14][N_N][0_0]', False, False, False))
    PIN_178_POL_01.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_184_POL_02 = DiagMessage(0xA8E7, 'PIN_184_POL_02', [1, 3, 4, 64], None, '', 5)
    PIN_184_POL_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_184_POL_02.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_184_POL_02.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_184_POL_02.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S2-S3-M1][PTO][X281-Y9][184-POL_02][D4-D6-CVT][L-S][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][PTO][X281][184-POL_02][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]', False, False, False))
    PIN_184_POL_02.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_185_POL_03 = DiagMessage(0xA8E8, 'PIN_185_POL_03', [1, 3, 4, 64], None, '', 5)
    PIN_185_POL_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_185_POL_03.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_185_POL_03.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_185_POL_03.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][S3-M1][PTO][X7][185-POL_03][CVT][S][raw][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Light][X350-X351-X353-X354(through_K7)][185-POL_03][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][PTO][X7][185-POL_03][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_185_POL_03.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_182_POL_04 = DiagMessage(0xA8E9, 'PIN_182_POL_04', [1, 3, 4, 64], None, '', 5)
    PIN_182_POL_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_182_POL_04.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_182_POL_04.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_182_POL_04.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_182_POL_04.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_183_POL_05 = DiagMessage(0xA8EA, 'PIN_183_POL_05', [1, 3, 4, 64], None, '', 5)
    PIN_183_POL_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_183_POL_05.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_183_POL_05.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_183_POL_05.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X654][183-POL_05][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Light][X258(through_K1R_K2R_through_K1)][183-POL_05][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_183_POL_05.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_180_POL_06 = DiagMessage(0xA8EB, 'PIN_180_POL_06', [1, 3, 4, 64], None, '', 5)
    PIN_180_POL_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_180_POL_06.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'36': [36, 36]}, 36, 36, '', False, False, False))
    PIN_180_POL_06.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_180_POL_06.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '[1][M2_19-M2_21-H2_22][Difflock][X6][180-POL_06][AMT-DCT-CVT][L-M-H][raw][SRC14][Y_N_N][1_0_0]', False, False, False))
    PIN_180_POL_06.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalInputs = DiagMessage(0xA8F0, 'DigitalInputs', [1, 3, 4, 64], None, '', 1)
    DigitalInputs.add_parameter(DiagParameter('AllDigitalInputs', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '', False, False, False))

    DigitalOutputs = DiagMessage(0xA8F3, 'DigitalOutputs', [1, 3, 4, 64], None, '', 1)
    DigitalOutputs.add_parameter(DiagParameter('AllDigitalOutputs', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '', False, False, False))

    PowerInput1 = DiagMessage(0xA8F5, 'PowerInput1', [1, 3, 4, 64], None, '', 1)
    PowerInput1.add_parameter(DiagParameter('AI_UBAT', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PowerInput2 = DiagMessage(0xA8F6, 'PowerInput2', [1, 3, 4, 64], None, '', 1)
    PowerInput2.add_parameter(DiagParameter('AI_VREF', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PowerInput3 = DiagMessage(0xA8F7, 'PowerInput3', [1, 3, 4, 64], None, '', 1)
    PowerInput3.add_parameter(DiagParameter('AI_5V_OUT', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PowerInput4 = DiagMessage(0xA8F8, 'PowerInput4', [1, 3, 4, 64], None, '', 1)
    PowerInput4.add_parameter(DiagParameter('AI_5V_TLE', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PowerOutput1 = DiagMessage(0xA8F9, 'PowerOutput1', [1, 3, 4, 64], None, '', 1)
    PowerOutput1.add_parameter(DiagParameter('DOPS_5V', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2][Miscellaneous][ ][145-219][D4-D6][L-S][raw][SRC14][Y][1]', False, False, False))

    PowerOutput2 = DiagMessage(0xA8FA, 'PowerOutput2', [1, 3, 4, 64], None, '', 1)
    PowerOutput2.add_parameter(DiagParameter('DOPS_8V5', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2][Miscellaneous][ ][146-232][D4-D6][L-S][raw][SRC14][Y][1]', False, False, False))

    UdsDiag_GetRearLinkageMode = DiagMessage(0xA8FB, 'UdsDiag_GetRearLinkageMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearLinkageMode.add_parameter(DiagParameter('RearLinkageMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [1, 1], 'WORK': [16, 16], 'TRANSPORT': [64, 64]}, 1, 64, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetFrontLinkageMode = DiagMessage(0xA8FC, 'UdsDiag_GetFrontLinkageMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontLinkageMode.add_parameter(DiagParameter('FrontLinkageMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'TRANSPORT': [1, 1], 'WORK': [2, 2], 'FLOAT': [3, 3], 'LOCKED': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetRearDualControlState = DiagMessage(0xA8FE, 'UdsDiag_GetRearDualControlState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearDualControlState.add_parameter(DiagParameter('RearDualControlState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N][1_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetFrontDualControlState = DiagMessage(0xA8FF, 'UdsDiag_GetFrontDualControlState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontDualControlState.add_parameter(DiagParameter('FrontDualControlState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N][1_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetRearPtoState = DiagMessage(0xA900, 'UdsDiag_GetRearPtoState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPtoState.add_parameter(DiagParameter('RearPtoState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetRearPtoSpeedSelected = DiagMessage(0xA901, 'UdsDiag_GetRearPtoSpeedSelected', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPtoSpeedSelected.add_parameter(DiagParameter('RearPtoSpeedSelected', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], '540': [1, 1], '540E': [2, 2], '1000': [3, 3], '1000E': [4, 4], 'ERROR': [5, 5]}, 0, 5, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetFrontPtoState = DiagMessage(0xA902, 'UdsDiag_GetFrontPtoState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontPtoState.add_parameter(DiagParameter('FrontPtoState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][ ][ ][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_Get4WDmode = DiagMessage(0xA903, 'UdsDiag_Get4WDmode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_Get4WDmode.add_parameter(DiagParameter('4WDmode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'MANU': [1, 1], 'AUTO': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_Get4WDstate = DiagMessage(0xA904, 'UdsDiag_Get4WDstate', [1, 3, 4, 64], None, '', 1)
    UdsDiag_Get4WDstate.add_parameter(DiagParameter('4WDstate', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetDifflockMode = DiagMessage(0xA905, 'UdsDiag_GetDifflockMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDifflockMode.add_parameter(DiagParameter('DifflockMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'MANU': [1, 1], 'AUTO': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetDifflockState = DiagMessage(0xA906, 'UdsDiag_GetDifflockState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDifflockState.add_parameter(DiagParameter('DifflockState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetFrontAxleSuspensionState = DiagMessage(0xA909, 'UdsDiag_GetFrontAxleSuspensionState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontAxleSuspensionState.add_parameter(DiagParameter('FrontAxleSuspensionState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][A5_RHS][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetAutoguideState = DiagMessage(0xA90A, 'UdsDiag_GetAutoguideState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetAutoguideState.add_parameter(DiagParameter('AutoguideState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))

    UdsDiag_GetHeadlandState = DiagMessage(0xA90D, 'UdsDiag_GetHeadlandState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHeadlandState.add_parameter(DiagParameter('HeadlandState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'HDL_STATE_OFF': [0, 0], 'HDL_STATE_RECORD': [1, 1], 'HDL_STATE_ON': [2, 2], 'HDL_STATE_PLAY_SEQ': [3, 3], 'HDL_STATE_PLAY_AUTO': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetMemoA_Value = DiagMessage(0xA90F, 'UdsDiag_GetMemoA_Value', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetMemoA_Value.add_parameter(DiagParameter('MemoA_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'rpm', 0, 5000, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetMemoSpeedState = DiagMessage(0xA910, 'UdsDiag_GetMemoSpeedState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetMemoSpeedState.add_parameter(DiagParameter('MemoSpeedState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'A': [1, 1], 'B': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetC1_Value = DiagMessage(0xA911, 'UdsDiag_GetC1_Value', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetC1_Value.add_parameter(DiagParameter('C1_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 8000, '[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetC1_Value.add_parameter(DiagParameter('C1_Value_D4D6', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1A': [0, 0], '1B': [1, 1], '1C': [2, 2], '1D': [3, 3], '1E': [4, 4], '1F': [5, 5], '2A': [6, 6], '2B': [7, 7], '2C': [8, 8], '2D': [9, 9], '2E': [10, 10], '2F': [11, 11], '3A': [12, 12], '3B': [13, 13], '3C': [14, 14], '3D': [15, 15], '3E': [16, 16], '3F': [17, 17], '4A': [18, 18], '4B': [19, 19], '4C': [20, 20], '4D': [21, 21], '4E': [22, 22], '4F': [23, 23]}, 0, 23, '[1][S2][Functions_state][ ][ ][D4-D6][L-S][conv][SRC14][N][0]', False, False, False))

    UdsDiag_GetC2_Value = DiagMessage(0xA912, 'UdsDiag_GetC2_Value', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetC2_Value.add_parameter(DiagParameter('C2_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 8000, '[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetC2_Value.add_parameter(DiagParameter('C2_Value_D4D6', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1A': [0, 0], '1B': [1, 1], '1C': [2, 2], '1D': [3, 3], '1E': [4, 4], '1F': [5, 5], '2A': [6, 6], '2B': [7, 7], '2C': [8, 8], '2D': [9, 9], '2E': [10, 10], '2F': [11, 11], '3A': [12, 12], '3B': [13, 13], '3C': [14, 14], '3D': [15, 15], '3E': [16, 16], '3F': [17, 17], '4A': [18, 18], '4B': [19, 19], '4C': [20, 20], '4D': [21, 21], '4E': [22, 22], '4F': [23, 23]}, 0, 23, '[1][S2][Functions_state][ ][ ][D4-D6][L-S][conv][SRC14][N][0]', False, False, False))

    UdsDiag_GetCruiseControlState = DiagMessage(0xA913, 'UdsDiag_GetCruiseControlState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetCruiseControlState.add_parameter(DiagParameter('CruiseControlState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CRUISE_CONTROL_DISABLED': [0, 0], 'CRUISE_CONTROL_1_SELECTED': [1, 1], 'CRUISE_CONTROL_2_SELECTED': [2, 2], 'CRUISE_CONTROL_1_ACTIVATED': [3, 3], 'CRUISE_CONTROL_2_ACTIVATED': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetPresetSpeedForwardMode1 = DiagMessage(0xA914, 'UdsDiag_GetPresetSpeedForwardMode1', [1, 3, 4, 64], None, '', 3)
    UdsDiag_GetPresetSpeedForwardMode1.add_parameter(DiagParameter('PresetSpeedForwardMode1_Auto', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))
    UdsDiag_GetPresetSpeedForwardMode1.add_parameter(DiagParameter('PresetSpeedForwardMode1_Manu_AMT', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1A': [1, 1], '1B': [2, 2], '1C': [3, 3], '1D': [4, 4], '1E': [5, 5], '1F': [6, 6], '1G': [7, 7], '2A': [8, 8], '2B': [9, 9], '2C': [10, 10], '2D': [11, 11], '2E': [12, 12], '2F': [13, 13], '2G': [14, 14], '3A': [15, 15], '3B': [16, 16], '3C': [17, 17], '3D': [18, 18], '3E': [19, 19], '3F': [20, 20], '3G': [21, 21], '4A': [22, 22], '4B': [23, 23], '4C': [24, 24], '4D': [25, 25], '4E': [26, 26], '4F': [27, 27], '4G': [28, 28]}, 1, 28, '', False, False, False))
    UdsDiag_GetPresetSpeedForwardMode1.add_parameter(DiagParameter('PresetSpeedForwardMode1_Manu_DCT', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    UdsDiag_GetPresetSpeedReverseMode1 = DiagMessage(0xA915, 'UdsDiag_GetPresetSpeedReverseMode1', [1, 3, 4, 64], None, '', 3)
    UdsDiag_GetPresetSpeedReverseMode1.add_parameter(DiagParameter('PresetSpeedReverseMode1_Auto', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))
    UdsDiag_GetPresetSpeedReverseMode1.add_parameter(DiagParameter('PresetSpeedReverseMode1_Manu_AMT', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1A': [1, 1], '1B': [2, 2], '1C': [3, 3], '1D': [4, 4], '1E': [5, 5], '1F': [6, 6], '1G': [7, 7], '2A': [8, 8], '2B': [9, 9], '2C': [10, 10], '2D': [11, 11], '2E': [12, 12], '2F': [13, 13], '2G': [14, 14], '3A': [15, 15], '3B': [16, 16], '3C': [17, 17], '3D': [18, 18], '3E': [19, 19], '3F': [20, 20], '3G': [21, 21], '4A': [22, 22], '4B': [23, 23], '4C': [24, 24], '4D': [25, 25], '4E': [26, 26], '4F': [27, 27], '4G': [28, 28]}, 1, 28, '', False, False, False))
    UdsDiag_GetPresetSpeedReverseMode1.add_parameter(DiagParameter('PresetSpeedReverseMode1_Manu_DCT', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    UdsDiag_GetPresetSpeedForwardMode2 = DiagMessage(0xA916, 'UdsDiag_GetPresetSpeedForwardMode2', [1, 3, 4, 64], None, '', 3)
    UdsDiag_GetPresetSpeedForwardMode2.add_parameter(DiagParameter('PresetSpeedForwardMode2_Auto', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))
    UdsDiag_GetPresetSpeedForwardMode2.add_parameter(DiagParameter('PresetSpeedForwardMode2_Manu_AMT', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1A': [1, 1], '1B': [2, 2], '1C': [3, 3], '1D': [4, 4], '1E': [5, 5], '1F': [6, 6], '1G': [7, 7], '2A': [8, 8], '2B': [9, 9], '2C': [10, 10], '2D': [11, 11], '2E': [12, 12], '2F': [13, 13], '2G': [14, 14], '3A': [15, 15], '3B': [16, 16], '3C': [17, 17], '3D': [18, 18], '3E': [19, 19], '3F': [20, 20], '3G': [21, 21], '4A': [22, 22], '4B': [23, 23], '4C': [24, 24], '4D': [25, 25], '4E': [26, 26], '4F': [27, 27], '4G': [28, 28]}, 1, 28, '', False, False, False))
    UdsDiag_GetPresetSpeedForwardMode2.add_parameter(DiagParameter('PresetSpeedForwardMode2_Manu_DCT', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    UdsDiag_GetPresetSpeedReverseMode2 = DiagMessage(0xA917, 'UdsDiag_GetPresetSpeedReverseMode2', [1, 3, 4, 64], None, '', 3)
    UdsDiag_GetPresetSpeedReverseMode2.add_parameter(DiagParameter('PresetSpeedReverseMode2_Auto', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))
    UdsDiag_GetPresetSpeedReverseMode2.add_parameter(DiagParameter('PresetSpeedReverseMode2_Manu_AMT', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'1A': [1, 1], '1B': [2, 2], '1C': [3, 3], '1D': [4, 4], '1E': [5, 5], '1F': [6, 6], '1G': [7, 7], '2A': [8, 8], '2B': [9, 9], '2C': [10, 10], '2D': [11, 11], '2E': [12, 12], '2F': [13, 13], '2G': [14, 14], '3A': [15, 15], '3B': [16, 16], '3C': [17, 17], '3D': [18, 18], '3E': [19, 19], '3F': [20, 20], '3G': [21, 21], '4A': [22, 22], '4B': [23, 23], '4C': [24, 24], '4D': [25, 25], '4E': [26, 26], '4F': [27, 27], '4G': [28, 28]}, 1, 28, '', False, False, False))
    UdsDiag_GetPresetSpeedReverseMode2.add_parameter(DiagParameter('PresetSpeedReverseMode2_Manu_DCT', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    UdsDiag_GetVistronicSpeedRequest = DiagMessage(0xA91B, 'UdsDiag_GetVistronicSpeedRequest', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetVistronicSpeedRequest.add_parameter(DiagParameter('VistronicSpeedRequest', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'rpm', 0, 5000, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetVistronicSpeedRequest.add_parameter(DiagParameter('ViscoSpeedRequestFiltered', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'rpm', 0, 5000, '', False, False, False))

    UdsDiag_GetViscoRegulationState = DiagMessage(0xA91C, 'UdsDiag_GetViscoRegulationState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetViscoRegulationState.add_parameter(DiagParameter('ViscoRegulationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NONE': [0, 0], 'COOLANT': [1, 1], 'INTAKEAIR': [2, 2], 'OILTRANS': [3, 3], 'AIRCONDITIONING ': [4, 4], 'SECUHYD': [5, 5], 'SECUTRANS': [6, 6], 'SECUFUEL': [7, 7], 'SECUENGINE': [8, 8], 'SECUCOMMUNICATION': [9, 9]}, 0, 9, '', False, False, False))

    UdsDiag_GetDriveMode = DiagMessage(0xA91D, 'UdsDiag_GetDriveMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDriveMode.add_parameter(DiagParameter('DriveMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'MANU': [0, 0], 'AUTO': [1, 1]}, 0, 1, '[1][S2-S3-M1][Functions_state][X124][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetSteeringSystemState = DiagMessage(0xA91E, 'UdsDiag_GetSteeringSystemState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteeringSystemState.add_parameter(DiagParameter('SteeringSystemState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_1 = DiagMessage(0xA921, 'UdsDiag_GetCommandSentToHydraulicValve_1', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_1.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_1.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_2 = DiagMessage(0xA922, 'UdsDiag_GetCommandSentToHydraulicValve_2', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_2.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_2.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_3 = DiagMessage(0xA923, 'UdsDiag_GetCommandSentToHydraulicValve_3', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_3.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_3.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_4 = DiagMessage(0xA924, 'UdsDiag_GetCommandSentToHydraulicValve_4', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_4.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_4.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_5 = DiagMessage(0xA925, 'UdsDiag_GetCommandSentToHydraulicValve_5', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_5.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_5.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_6 = DiagMessage(0xA926, 'UdsDiag_GetCommandSentToHydraulicValve_6', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_6.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_6.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_7 = DiagMessage(0xA927, 'UdsDiag_GetCommandSentToHydraulicValve_7', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_7.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_7.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_8 = DiagMessage(0xA928, 'UdsDiag_GetCommandSentToHydraulicValve_8', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_8.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_8.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_9 = DiagMessage(0xA929, 'UdsDiag_GetCommandSentToHydraulicValve_9', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_9.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][S2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][2]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y_N_N][2_0_0]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_9.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][2]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][2]', False, False, False))

    UdsDiag_GetLimitedEngineSpeedStatus = DiagMessage(0xA92D, 'UdsDiag_GetLimitedEngineSpeedStatus', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLimitedEngineSpeedStatus.add_parameter(DiagParameter('LimitedEngineSpeedStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetTrailerBrake_TrailerDetection_SW = DiagMessage(0xA969, 'UdsDiag_GetTrailerBrake_TrailerDetection_SW', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetTrailerBrake_TrailerDetection_SW.add_parameter(DiagParameter('TrailerBrake_TrailerDetection_SW', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Miscellaneous][X990][250-DI_01][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X990][235-DI_24][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetHydTrailerBrake_Safety_EV_SOL = DiagMessage(0xA96D, 'UdsDiag_GetHydTrailerBrake_Safety_EV_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydTrailerBrake_Safety_EV_SOL.add_parameter(DiagParameter('HydTrailerBrake_Safety_EV_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Braking_system][X339-Y69][126-POH_17][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Braking_system][X39][126-POH_17][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetPneumaticTrailerBrake_TankPressure2 = DiagMessage(0xA974, 'UdsDiag_GetPneumaticTrailerBrake_TankPressure2', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumaticTrailerBrake_TankPressure2.add_parameter(DiagParameter('PneumaticTrailerBrake_TankPressure2', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'bar', 0, 16000, '[1][S2][Braking_system][X1077-B51][165-CI_10][D4-D6][L-S][conv][SRC14][Y][1]#[1][M2_19-M2_21-H2_22][Braking_system][X1077][134-DI_18][AMT-DCT-CVT][L-M-H][conv][SRC14_IO][ ][0]', False, False, False))

    UdsDiag_GetPneumaticTrailerBrake_TankPressure = DiagMessage(0xA975, 'UdsDiag_GetPneumaticTrailerBrake_TankPressure', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumaticTrailerBrake_TankPressure.add_parameter(DiagParameter('PneumaticTrailerBrake_TankPressure', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'bar', 0, 16000, '[1][S2][Braking_system][X1078-B42][164-CI_15][D4-D6][L-S][conv][SRC14][Y][1]#[1][M2_19-M2_21-H2_22][Braking_system][X1078][231-AI_07][AMT-DCT-CVT][L-M-H][conv][SRC14_IO][Y][0]', False, False, False))

    UdsDiag_GetPneumatic_Drying_Governor_SOL = DiagMessage(0xA976, 'UdsDiag_GetPneumatic_Drying_Governor_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumatic_Drying_Governor_SOL.add_parameter(DiagParameter('Pneumatic_Drying_Governor_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][Braking_system][X1075-Y79][173-POH_10][D4-D6][L-S][conv][SRC14][Y][1]#[1][M2_19-M2_21-H2_22][Braking_system][X1075][115-PDOH_20][AMT-DCT-CVT][L-M-H][conv][SRC14_IO][ ][0]', False, False, False))

    UdsDiag_GetPneumatic_Drying_Regeneration_SOL = DiagMessage(0xA977, 'UdsDiag_GetPneumatic_Drying_Regeneration_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumatic_Drying_Regeneration_SOL.add_parameter(DiagParameter('Pneumatic_Drying_Regeneration_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][Braking_system][X1075-Y79][193-PDOH_06][D4-D6][L-S][conv][SRC14][Y][1]#[1][M2_19-M2_21-H2_22][Braking_system][X1075][243-PDOH_21][AMT-DCT-CVT][L-M-H][conv][SRC14_IO][ ][0]', False, False, False))

    UdsDiag_GetHitch_FenderUpSw = DiagMessage(0xA985, 'UdsDiag_GetHitch_FenderUpSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_FenderUpSw.add_parameter(DiagParameter('Hitch_FenderUpSw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X87-X97][211-DI_19][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X87-X97][211-DI_06][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]', False, False, False))

    UdsDiag_GetHitch_FenderDownSw = DiagMessage(0xA986, 'UdsDiag_GetHitch_FenderDownSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_FenderDownSw.add_parameter(DiagParameter('Hitch_FenderDownSw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X664-X665][224-DI_21][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X87-X97][224][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]', False, False, False))

    UdsDiag_GetFrontHitch_Extend_ExternalSw = DiagMessage(0xA987, 'UdsDiag_GetFrontHitch_Extend_ExternalSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontHitch_Extend_ExternalSw.add_parameter(DiagParameter('FrontHitch_Extend_ExternalSw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X277][237-DI_30][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X277][225-DI_27][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]', False, False, False))

    UdsDiag_GetFrontHitch_Retract_ExternalSw = DiagMessage(0xA988, 'UdsDiag_GetFrontHitch_Retract_ExternalSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontHitch_Retract_ExternalSw.add_parameter(DiagParameter('FrontHitch_Retract_ExternalSw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X277][212-DI_28][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X277][212-DI_28][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]', False, False, False))

    UdsDiag_GetHitch_LeftDraftSensor = DiagMessage(0xA989, 'UdsDiag_GetHitch_LeftDraftSensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_LeftDraftSensor.add_parameter(DiagParameter('Hitch_LeftDraftSensor_Degree', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'deg', -32768, 32767, '[1][S2-S3-M1][Linkage][X32-B2E][116-AI_04][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X32][116-AI_04(KMB)][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][2_0_0]', False, False, False))

    UdsDiag_GetHitch_RightDraftSensor = DiagMessage(0xA98A, 'UdsDiag_GetHitch_RightDraftSensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_RightDraftSensor.add_parameter(DiagParameter('Hitch_RightDraftSensor_Degree', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'deg', -32768, 32767, '[1][S2-S3-M1][Linkage][X31-B3E][231-AI_07][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X31][231-AI_07(KMB)][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][2_0_0]', False, False, False))

    UdsDiag_GetHitch_DualSensor = DiagMessage(0xA98B, 'UdsDiag_GetHitch_DualSensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_DualSensor.add_parameter(DiagParameter('Hitch_DualSensor', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'bar', 0, 255, '[1][S3-M1][Linkage][X211][188-AI_12][D6-CVT][L-S][conv][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X211][188-AI_12][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]', False, False, False))

    UdsDiag_GetHitch_Depth_Sensor = DiagMessage(0xA98C, 'UdsDiag_GetHitch_Depth_Sensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Depth_Sensor.add_parameter(DiagParameter('Hitch_Depth_Sensor_Degree', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Linkage][X30-B1E][121-AI_03][D4-D6][L-S][conv][SRC14][Y_N_N][2_0_0]#[1][S3-M1][Linkage][X30][171-CI_05][CVT][S][conv][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X30][171-CI_05][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_GetHitch_Radar_In = DiagMessage(0xA98D, 'UdsDiag_GetHitch_Radar_In', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Radar_In.add_parameter(DiagParameter('Hitch_Radar_In', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '[1][S2-S3-M1][Transmission][X22-B25][112-FI_01][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Linkage][X22][112-FI_01][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetHydraulic_RearFenderExtend_Sw = DiagMessage(0xA995, 'UdsDiag_GetHydraulic_RearFenderExtend_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_RearFenderExtend_Sw.add_parameter(DiagParameter('Hydraulic_RearFenderExtend_Sw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X96][239-DI_31][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X95-X96][239-DI_31][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]', False, False, False))

    UdsDiag_GetLOADER_KPAD_Lock_Status = DiagMessage(0xA9B6, 'UdsDiag_GetLOADER_KPAD_Lock_Status', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetLOADER_KPAD_Lock_Status.add_parameter(DiagParameter('LOADER_Lock_SwitchStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'Not_Available': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X1115_LockSw][LIN][D4-D6][L-S][conv][Keypad_Loader][N][0]#[1][M2_19-M2_21][LIN][ ][ ][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N][0_0]', False, False, False))
    UdsDiag_GetLOADER_KPAD_Lock_Status.add_parameter(DiagParameter('LOADER_Lock_LedStatus', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][Cab_commands_state][X1115_LockSt][LIN][D4-D6][L-S][conv][Keypad_Loader][N][0]', False, False, False))

    UdsDiag_GetLOADER_KPAD_BucketLock_Status = DiagMessage(0xA9B7, 'UdsDiag_GetLOADER_KPAD_BucketLock_Status', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetLOADER_KPAD_BucketLock_Status.add_parameter(DiagParameter('LOADER_BucketLock_SwitchStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'Not_Available': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X1115_LockBucketSw][LIN][D4-D6][L-S][conv][Keypad_Loader][N][0]#[1][M2_19-M2_21][LIN][ ][ ][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N][0_0]', False, False, False))
    UdsDiag_GetLOADER_KPAD_BucketLock_Status.add_parameter(DiagParameter('LOADER_BucketLock_LedStatus', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][Cab_commands_state][X1115_LockBucketSt][LIN][D4-D6][L-S][conv][Keypad_Loader][N][0]', False, False, False))

    UdsDiag_GetLOADER_KPAD_Susp_Status = DiagMessage(0xA9B8, 'UdsDiag_GetLOADER_KPAD_Susp_Status', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetLOADER_KPAD_Susp_Status.add_parameter(DiagParameter('LOADER_Susp_SwitchStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'Not_Available': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X1115_SuspSw][LIN][D4-D6][L-S][conv][Keypad_Loader][N][0]#[1][M2_19-M2_21][LIN][ ][ ][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N][0_0]', False, False, False))
    UdsDiag_GetLOADER_KPAD_Susp_Status.add_parameter(DiagParameter('LOADER_Susp_LedStatus', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][Cab_commands_state][X1115_SuspSt][LIN][D4-D6][L-S][conv][Keypad_Loader][N][0]', False, False, False))

    UdsDiag_GetSteering_PressureSw = DiagMessage(0xA9BA, 'UdsDiag_GetSteering_PressureSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteering_PressureSw.add_parameter(DiagParameter('Steering_PressureSw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Steering_system][X23-S169][135-DI_17][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19][Steering_system][X23][134-DI_18][AMT-DCT][L-M-H][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetSteering_WAS = DiagMessage(0xA9BB, 'UdsDiag_GetSteering_WAS', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteering_WAS.add_parameter(DiagParameter('Steering_WAS_Angle', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'deg', -90, 90, '[1][S2][Steering_system][X235-B2C][218-CI_03][D4-D6][L-S][conv][SRC14][Y][2]#[1][S3-M1][Steering_system][X235][226-AI_10][D6-CVT][L-S][conv][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Steering_system][X235][218-CI_03][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_GetSteering_SafetyValveSol = DiagMessage(0xA9BC, 'UdsDiag_GetSteering_SafetyValveSol', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteering_SafetyValveSol.add_parameter(DiagParameter('Steering_SafetyValveSolState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Steering_system][X372-Y1C3][243-PDOH_21][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][Steering_system][X372][243-PDOH_21][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_GetDrive_Toc_b = DiagMessage(0xA9BE, 'UdsDiag_GetDrive_Toc_b', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_Toc_b.add_parameter(DiagParameter('Drive_Toc_b', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X68][147-DI_04][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X68][147-DI_04][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetDrive_BOC_NO_b = DiagMessage(0xA9BF, 'UdsDiag_GetDrive_BOC_NO_b', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_BOC_NO_b.add_parameter(DiagParameter('Drive_BOC_NO_b', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X68][148-DI_06][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X68][148-DI_06][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetDrive_FNR_Neutral_NC = DiagMessage(0xA9C0, 'UdsDiag_GetDrive_FNR_Neutral_NC', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_FNR_Neutral_NC.add_parameter(DiagParameter('Drive_FNR_Neutral_NC', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X56][214-DI_09][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X56][214-DI_09][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetDrive_FNR_Neutral_NO = DiagMessage(0xA9C1, 'UdsDiag_GetDrive_FNR_Neutral_NO', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_FNR_Neutral_NO.add_parameter(DiagParameter('Drive_FNR_Neutral_NO', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X56][136-DI_15][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X56][118-AI_06][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetDrive_OPS = DiagMessage(0xA9C2, 'UdsDiag_GetDrive_OPS', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_OPS.add_parameter(DiagParameter('Drive_OPS', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X739][235-DI_24][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X739][137-DI_16][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetDrive_FNR_Position = DiagMessage(0xA9C3, 'UdsDiag_GetDrive_FNR_Position', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_FNR_Position.add_parameter(DiagParameter('Drive_FNR_Position', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 50, 4100, '[1][S2-S3-M1][Cab_commands][X56][120-AI_02][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X56][120-AI_2][AMT-DCT-CVT][L-M-H][raw][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetBrake_HandLever_sw = DiagMessage(0xA9C6, 'UdsDiag_GetBrake_HandLever_sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_HandLever_sw.add_parameter(DiagParameter('Brake_HandLever_sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Braking_system][X618][248-DI_29][D4-D6][L-S][conv][SRC14][Y_N_N][0_0_0]#[1][S3-M1][Braking_system][X618][143-DI_22][CVT][S][conv][SRC14][N_N][0_0]#[1][M2][Cab_commands][X618][223-DI_05][ ][ ][conv][SRC14][Y][2]', False, False, False))

    UdsDiag_GetBrake_CouplingPedals = DiagMessage(0xA9CA, 'UdsDiag_GetBrake_CouplingPedals', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_CouplingPedals.add_parameter(DiagParameter('Brake_CouplingPedals', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S3-M1][Braking_system][X984-X988][142-DI_23][D6-CVT][L-S][conv][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Cab_commands][X984-X988][142-DI_23][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetFrontPTO_SOL = DiagMessage(0xA9D0, 'UdsDiag_GetFrontPTO_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontPTO_SOL.add_parameter(DiagParameter('FrontPTO_SOL', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'mA', 0, 255, '[1][S2-S3-M1][PTO][X281-Y9][186-POH_04][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21-H2_22][PTO][X281][186-POH_04][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_GetFrontPTO_Gnd_SOL = DiagMessage(0xA9D5, 'UdsDiag_GetFrontPTO_Gnd_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontPTO_Gnd_SOL.add_parameter(DiagParameter('FrontPTO_Gnd_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][PTO][X281-Y9][184-POL_02][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]"[1][M2_19-M2_21-H2_22][PTO][X281][184-POL_02][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][2_0_0]', False, False, False))

    UdsDiag_GetDrive_ClutchPedal_PositionSen = DiagMessage(0xA9DA, 'UdsDiag_GetDrive_ClutchPedal_PositionSen', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_ClutchPedal_PositionSen.add_parameter(DiagParameter('Drive_ClutchPedalPositionSen', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2-S3-M1][Cab_commands][X68][213-AI_09][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2][Cab_commands][X68][213-AI_09][ ][ ][conv][SRC14][Y][0]', False, False, False))

    UdsDiag_GetInCabSocket_PowerSupply_relay = DiagMessage(0xA9E0, 'UdsDiag_GetInCabSocket_PowerSupply_relay', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetInCabSocket_PowerSupply_relay.add_parameter(DiagParameter('InCabSocket_PowerSupply_relay', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][M2_19-M2_21-H2_22][Miscellaneous][X151][114-DOH_05][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]#[1][S2][Miscellaneous][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetISO_Power_relay = DiagMessage(0xA9E1, 'UdsDiag_GetISO_Power_relay', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO_Power_relay.add_parameter(DiagParameter('ISO_Power_relay', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][M2_19-M2_21-H2_22][Miscellaneous][X218-X1052(through_relay_K2I)][244-DOH_07][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]#[1][S2][Miscellaneous][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetISO_ECU_Power_relay = DiagMessage(0xA9E2, 'UdsDiag_GetISO_ECU_Power_relay', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO_ECU_Power_relay.add_parameter(DiagParameter('ISO_ECU_Power_relay', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][M2_19-M2_21-H2_22][Miscellaneous][X218-X1052(through_relay_K1I)][106-DOH_06][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][0_0_0]#[1][S2][Miscellaneous][ ][ ][ ][ ][conv][SRC14][Y][1]', False, False, False))

    UdsDiag_GetOps_and_Park_brake_sensor = DiagMessage(0xA9EA, 'UdsDiag_GetOps_and_Park_brake_sensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetOps_and_Park_brake_sensor.add_parameter(DiagParameter('Ops_and_Park_brake_sensor', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Miscellaneous][X618-X739_Supply][104-PDOH_19][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))

    UdsDiag_GetPneumatic_trailer_braking_test = DiagMessage(0xA9EC, 'UdsDiag_GetPneumatic_trailer_braking_test', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumatic_trailer_braking_test.add_parameter(DiagParameter('Pneumatic_trailer_braking_test', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '[1][S2-S3-M1][Braking_system][X996-S170][144-DI_20][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))

    UdsDiag_GetPneumatic_trailer_brake_valve = DiagMessage(0xA9ED, 'UdsDiag_GetPneumatic_trailer_brake_valve', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumatic_trailer_brake_valve.add_parameter(DiagParameter('Pneumatic_trailer_brake_valve', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Braking_system][X987_through_relay_X993-Y71][242-DOH_4][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_GetSafety_solenoid_valve = DiagMessage(0xA9EF, 'UdsDiag_GetSafety_solenoid_valve', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSafety_solenoid_valve.add_parameter(DiagParameter('Safety_solenoid_valve', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Auxiliary_hydraulic][X654-Y37][115-PDOH_20][D4-D6-CVT][S][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_GetLight_diurne = DiagMessage(0xA9F0, 'UdsDiag_GetLight_diurne', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_diurne.add_parameter(DiagParameter('Light_diurne', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Miscellaneous][X994][241-DOH_03][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_Getslippage_rate = DiagMessage(0xA9F1, 'UdsDiag_Getslippage_rate', [1, 3, 4, 64], None, '', 1)
    UdsDiag_Getslippage_rate.add_parameter(DiagParameter('slippage_rate', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_GetSteering_spool_position = DiagMessage(0xAA17, 'UdsDiag_GetSteering_spool_position', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetSteering_spool_position.add_parameter(DiagParameter('SCT_Valve_State', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Blocked': [0, 0], 'Extend': [1, 1], 'Retract': [2, 2], 'ERROR_INDICATION': [14, 14]}, 0, 14, '[1][M2][Functions_state][ ][ ][ ][ ][conv][PVED-CC][Y][0]#[1][S2-S3-M1][X236-X237][CAN][D4-D6-CVT][L-S][raw][SRC14][N_N_N][0_0_0]', False, False, False))
    UdsDiag_GetSteering_spool_position.add_parameter(DiagParameter('SCT_Estimated_Flow_Percent', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][M2][Functions_state][ ][ ][ ][ ][conv][PVED-CC][Y][0]#[1][S2-S3-M1][X236-X237][CAN][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    Linkage_quick_soil_engagement_state = DiagMessage(0xAA22, 'Linkage_quick_soil_engagement_state', [1, 3, 4, 64], None, '', 1)
    Linkage_quick_soil_engagement_state.add_parameter(DiagParameter('Linkage_quick_soil_engagement_state', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2], 'test': [3, 3]}, 0, 3, '[1][S2][Functions_state][ ][ ][D4-D6][L-S][conv][SRC14][Y][2]', False, False, False))

    Brake_to_Neutral = DiagMessage(0xAA28, 'Brake_to_Neutral', [1, 3, 4, 64], None, '', 1)
    Brake_to_Neutral.add_parameter(DiagParameter('Brake_To_Neutral', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'Err': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))

    Command_Hitch_Valve_SB24 = DiagMessage(0xAA29, 'Command_Hitch_Valve_SB24', [1, 3, 4, 64], None, '', 2)
    Command_Hitch_Valve_SB24.add_parameter(DiagParameter('CommandToHitchRearValve_Direction', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Up': [0, 0], 'Down': [1, 1], 'Error': [2, 2], 'n.a.': [3, 3]}, 0, 3, '[1][S2][Linkage][X27-Y5E][CAN][D4-D6][L-S][raw][SRC14][Y][2]', False, False, False))
    Command_Hitch_Valve_SB24.add_parameter(DiagParameter('CommandToHitchRearValve_Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2][Linkage][X27-Y5E][CAN][D4-D6][L-S][conv][SRC14][Y][2]', False, False, False))

    UdsDiag_GetSASA_Sensor_Angle = DiagMessage(0xAA2A, 'UdsDiag_GetSASA_Sensor_Angle', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetSASA_Sensor_Angle.add_parameter(DiagParameter('SASA_Sensor_Angle', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'deg', -32768, 32767, '[1][S2-S3-M1][Steering_system][X210-B1C][CAN][D4-D6-CVT][L-S][conv][SASA][N_N_N][0_0_0]#[1][M2][Steering_system][X210][CAN][D4-D6-CVT][L-S][conv][SASA][Y][0]', False, False, False))
    UdsDiag_GetSASA_Sensor_Angle.add_parameter(DiagParameter('SASA_Sensor_Angle_raw', 2, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'V', 0, 65535, '[1][S2-S3-M1][Steering_system][X210-B1C][CAN][D4-D6-CVT][L-S][raw][SASA][N_N_N][0_0_0]#[1][M2][Steering_system][X210][CAN][D4-D6-CVT][L-S][raw][SASA][ ][0]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_10 = DiagMessage(0xAA32, 'UdsDiag_GetCommandSentToHydraulicValve_10', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_10.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]#[1][S2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_10.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]#[1][S2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_11 = DiagMessage(0xAA33, 'UdsDiag_GetCommandSentToHydraulicValve_11', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_11.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]#[1][S2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_11.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]#[1][S2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_12 = DiagMessage(0xAA34, 'UdsDiag_GetCommandSentToHydraulicValve_12', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_12.add_parameter(DiagParameter('Direction', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]#[1][S2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_12.add_parameter(DiagParameter('Position', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][M2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]#[1][S2][Functions_state][ ][ ][ ][ ][conv][SRC14][Y][0]', False, False, False))

    UdsDiag_GetInternalHitchSwitch = DiagMessage(0xAA38, 'UdsDiag_GetInternalHitchSwitch', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetInternalHitchSwitch.add_parameter(DiagParameter('Internal_Lifting_Linkage', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X363][247-DI_25][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]', False, False, False))
    UdsDiag_GetInternalHitchSwitch.add_parameter(DiagParameter('Internal_Lowering_Linkage', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][S2-S3-M1][Cab_commands][X363][234-DI_26][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]', False, False, False))

    UdsDiag_GetSupplyConverted = DiagMessage(0xAA48, 'UdsDiag_GetSupplyConverted', [1, 3, 4, 64], None, '', 8)
    UdsDiag_GetSupplyConverted.add_parameter(DiagParameter('External_connector_FrontLoaderLockingAcc_supply', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Miscellaneous][ENG109][102-DOH_10][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))
    UdsDiag_GetSupplyConverted.add_parameter(DiagParameter('External_connector_FrontLoaderSusp_supply', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Miscellaneous][ENG109][103-DOH_12][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))
    UdsDiag_GetSupplyConverted.add_parameter(DiagParameter('RelayK7_4thfunction_supply', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Miscellaneous][K7][114-DOH_05][D6-CVT][S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))
    UdsDiag_GetSupplyConverted.add_parameter(DiagParameter('RelayK8_3thfunction_supply', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Miscellaneous][K8][128-DOH_14][D6-CVT][S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))
    UdsDiag_GetSupplyConverted.add_parameter(DiagParameter('RelayK28_ext_isobus_supply', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Miscellaneous][K28][244-DOH_07][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))
    UdsDiag_GetSupplyConverted.add_parameter(DiagParameter('RelayK15_Reversinglight_supply', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S3-M1][Miscellaneous][K15][107-PDOH_18][CVT][S][conv][SRC14][N_N][0_0]', False, False, False))
    UdsDiag_GetSupplyConverted.add_parameter(DiagParameter('RelayK24_Brakelights_supply', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S3-M1][Miscellaneous][K24][127-DOH_15][CVT][S][conv][SRC14][N_N][0_0]', False, False, False))
    UdsDiag_GetSupplyConverted.add_parameter(DiagParameter('Relay_IsobusECUPower_supply', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2-S3-M1][Miscellaneous][X961][106-DOH_16][D4-D6-CVT][L-S][conv][SRC14][Y_N_N][2_0_0]', False, False, False))

    UdsDiag_GetFrontPowerLift = DiagMessage(0xAA52, 'UdsDiag_GetFrontPowerLift', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontPowerLift.add_parameter(DiagParameter('Position_sensor', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S3-M1][Linkage][X279][229-CI_04][D6-CVT][L-S][conv][SRC14][N_N][0_0]#[1][M2_19-M2_21-H2_22][Linkage][X279][229-CI_04][AMT-DCT-CVT][L-M-H][conv][SRC14][Y_N_N][1_0_0]', False, False, False))

    UdsDiag_GetPickUpHitch = DiagMessage(0xAA54, 'UdsDiag_GetPickUpHitch', [1, 3, 4, 64], None, '', 4)
    UdsDiag_GetPickUpHitch.add_parameter(DiagParameter('Extract_sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2][Linkage][X1118][238-DI_12][D4-D6][L-S][conv][SRC14][Y][2]', False, False, False))
    UdsDiag_GetPickUpHitch.add_parameter(DiagParameter('Retract_sw', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '[1][S2][Linkage][X1118][137-DI_16][D4-D6][L-S][conv][SRC14][Y][2]', False, False, False))
    UdsDiag_GetPickUpHitch.add_parameter(DiagParameter('Extract_EV', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2][Linkage][X43][153-PDOH_13][D4-D6][L-S][conv][SRC14][Y][2]', False, False, False))
    UdsDiag_GetPickUpHitch.add_parameter(DiagParameter('Retract_EV', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][S2][Linkage][X44][154-PDOH_14][D4-D6][L-S][conv][SRC14][Y][2]', False, False, False))

    BRAKE_TrailerPneumatic_AirDryingRegenerationCounter = DiagMessage(0xAA61, 'BRAKE_TrailerPneumatic_AirDryingRegenerationCounter', [1, 3, 4, 64], None, '', 1)
    BRAKE_TrailerPneumatic_AirDryingRegenerationCounter.add_parameter(DiagParameter('BRAKE_TrailerPneumatic_AirDryingRegenerationCounter', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21][Functions_state][ ][ ][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N][0_0]', False, False, False))

    HVAC_DensoMedium_States = DiagMessage(0xAB00, 'HVAC_DensoMedium_States', [1, 3, 4, 64], None, '', 8)
    HVAC_DensoMedium_States.add_parameter(DiagParameter('HVAC_Input_PresetTemperature', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.5, '?C', 0, 65535, '[1][S2-S3-M1][Air_conditionning][AC_ECU][CAN][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_States.add_parameter(DiagParameter('HVAC_State_AcSystem', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON_Cooling': [1, 1], 'ON_Heating': [2, 2], 'ON_Standard': [4, 4]}, 0, 4, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_States.add_parameter(DiagParameter('HVAC_State_CompressorRelay', 3, 2, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Air_conditionning][X439][26][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_States.add_parameter(DiagParameter('HVAC_State_RecyclingFlap', 4, 2, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Air_conditionning][X440][2][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_States.add_parameter(DiagParameter('HVAC_State_HeaterPumpRelay', 5, 2, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Air_conditionning][X453][23_blue][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_States.add_parameter(DiagParameter('HVAC_PowerSupply_DirectBattery', 6, 3, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Air_conditionning][X439][15][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_States.add_parameter(DiagParameter('HVAC_PowerSupply_Ignition', 7, 3, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Air_conditionning][X439][17][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_States.add_parameter(DiagParameter('HVAC_PowerSupply_Headlight', 8, 3, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2-S3-M1][Air_conditionning][X439][16][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))

    HVAC_DensoMedium_Sensors = DiagMessage(0xAB01, 'HVAC_DensoMedium_Sensors', [], None, '', 9)
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenTemperature_InsideCab_Ohm', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 166.0, 'ohm', 0, 65535, '[1][S2-S3-M1][Air_conditionning][X69][7][D4-D6-CVT][L-S][raw][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenTemperature_External_Ohm', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1000.0, 'ohm', 0, 65535, '[1][S2-S3-M1][Air_conditionning][X358][6][D4-D6-CVT][L-S][raw][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenTemperature_TreatedAir_Ohm', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1000.0, 'ohm', 0, 65535, '[1][S2-S3-M1][Air_conditionning][X439][22-23][D4-D6-CVT][L-S][raw][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenTemperature_Evaporator_Ohm', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'ohm', 0, 65535, '[1][S2-S3-M1][Air_conditionning][X439][24][D4-D6-CVT][L-S][raw][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenTemperature_InsideCab_Degree', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -128.0, 1.0, '?C', 0, 65535, '[1][S2-S3-M1][Air_conditionning][X69][7][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenTemperature_External_Degree', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 65535, '[1][S2-S3-M1][Air_conditionning][X358][6][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenSolar_Current', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '?A', 0, 255, '[1][S2-S3-M1][Air_conditionning][X70][21][D4-D6-CVT][L-S][raw][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenSpeed_VentilationRegulator_Percent', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.3921, '%', 0, 65535, '[1][S2-S3-M1][Air_conditionning][X440][5][D4-D6-CVT][L-S][conv][HVAC][N_N_N][0_0_0]', False, False, False))
    HVAC_DensoMedium_Sensors.add_parameter(DiagParameter('HVAC_SenPosition_HeatingValve', 9, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Air_conditionning][X440][14-18][D4-D6-CVT][L-S][raw][HVAC][N_N_N][2_0_0]', False, False, False))

    EEPROM_Parameters = DiagMessage(0xCF00, 'EEPROM_Parameters', [1, 3], None, '', 44)
    EEPROM_Parameters.add_parameter(DiagParameter('NUM_APPLI', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_NEUTRAL', 2, 2, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('DUAL_FLOW', 3, 2, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('CAB_SUSP', 4, 2, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('FAX_SUSP', 5, 2, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('REVERSE_FAN', 6, 2, 4, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('FOUR_WD', 7, 2, 5, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('NAO', 8, 2, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('VALVE_STEERING', 9, 2, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_540', 10, 3, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_540ECO', 11, 3, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_1000', 12, 3, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_1000ECO', 13, 3, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PORSHLIGHT_FEATURE', 14, 3, 4, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PORSHLIGHT_STATE', 15, 3, 5, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_1', 16, 3, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_2', 17, 3, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_FRONT_ROOF', 18, 4, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('BEACON', 19, 4, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_REAR_ROOF', 20, 4, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_REAR_FENDER', 21, 4, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_FRONT_HOOD', 22, 4, 4, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('BEAM_HANDRAIL', 23, 4, 5, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_01', 24, 4, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_02', 25, 4, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_03', 26, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('BEACON_AUTO', 27, 6, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_HANDRAIL', 28, 6, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('JAPON', 29, 6, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_HANDRAIL_2', 30, 6, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('CAB_SUSP_FEATURE', 31, 6, 4, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_05', 32, 6, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_06', 33, 6, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PLATFORM', 34, 7, 0, 4, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RHS_LEVER', 35, 7, 4, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_07', 36, 7, 6, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('REVERSE_LIGHT', 37, 8, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_08', 38, 8, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_09', 39, 8, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_10', 40, 8, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_11', 41, 8, 4, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_12', 42, 8, 5, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_13', 43, 8, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_14', 44, 8, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))

    EEP_CALIBRATION_AND_SETTING_CONTENT = DiagMessage(0xF100, 'EEP_CALIBRATION_AND_SETTING_CONTENT', [1, 2, 3, 4, 64, 65], None, '', 1)
    EEP_CALIBRATION_AND_SETTING_CONTENT.add_parameter(DiagParameter('EEP_CALIBRATION_AND_SETTING_CONTENT', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'EEP Calibration Setting content', False, False, False))

    EEP_tuning_content = DiagMessage(0xF102, 'EEP_tuning_content', [1, 2, 3, 4, 64, 65], None, '', 1)
    EEP_tuning_content.add_parameter(DiagParameter('EEP_tuning_content', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'EEP tuning content', False, False, False))

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

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [1, 2, 3, 4, 64], None, '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [1, 2, 3, 4, 64], None, '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [1, 2, 3, 4, 64], None, '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class SRC14_S2_BVWriteDataSignals:
    MaintenanceNextServiceHours = DiagMessage(0x1330, 'MaintenanceNextServiceHours', [3, 4, 64], [1, 3, 4, 5], '', 1)
    MaintenanceNextServiceHours.add_parameter(DiagParameter('MaintenanceNSHs', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 4294967295, 'Next Maintenance Service Hours', False, False, False))

    TractorHoursOffset = DiagMessage(0x1331, 'TractorHoursOffset', [3, 4, 64], [1, 3, 4, 5], '', 1)
    TractorHoursOffset.add_parameter(DiagParameter('TractorHoursOffset', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, '', -2147483646, 2147483646, 'Tractor Hours Offset 0.1h', False, False, False))

    CurrentTractorWheelSize = DiagMessage(0x1332, 'CurrentTractorWheelSize', [3, 4, 64], [1, 3, 4, 5], '', 1)
    CurrentTractorWheelSize.add_parameter(DiagParameter('CurrentTractorWhlSze', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 3000, 7500, 'Current Tractor WheelSize in mm', False, False, False))

    TractorWheelMaxSize = DiagMessage(0x1333, 'TractorWheelMaxSize', [3, 4, 64], [1, 3, 4, 5], '', 1)
    TractorWheelMaxSize.add_parameter(DiagParameter('TractorWlMxSze', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 3000, 7500, 'Tractor Wheel Max Size in mm', False, False, False))

    EngineHoursMemo = DiagMessage(0x1334, 'EngineHoursMemo', [3, 4, 64], [1, 3, 4, 5], '', 1)
    EngineHoursMemo.add_parameter(DiagParameter('HoursMemo', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 2147483646, '', False, False, False))

    BRAKE_TrailerPneumatic_AirDryingRegenerationCounter = DiagMessage(0xAA61, 'BRAKE_TrailerPneumatic_AirDryingRegenerationCounter', [3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    BRAKE_TrailerPneumatic_AirDryingRegenerationCounter.add_parameter(DiagParameter('BRAKE_TrailerPneumatic_AirDryingRegenerationCounter', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][S2-S3-M1][Functions_state][ ][ ][D4-D6-CVT][L-S][conv][SRC14][N_N_N][0_0_0]#[1][M2_19-M2_21][Functions_state][ ][ ][AMT-DCT-CVT][L-M-H][conv][SRC14][N_N][0_0]', False, False, False))

    EEPROM_Parameters = DiagMessage(0xCF00, 'EEPROM_Parameters', [], None, '', 44)
    EEPROM_Parameters.add_parameter(DiagParameter('NUM_APPLI', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_NEUTRAL', 2, 2, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('DUAL_FLOW', 3, 2, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('CAB_SUSP', 4, 2, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('FAX_SUSP', 5, 2, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('REVERSE_FAN', 6, 2, 4, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('FOUR_WD', 7, 2, 5, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('NAO', 8, 2, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('VALVE_STEERING', 9, 2, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_540', 10, 3, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_540ECO', 11, 3, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_1000', 12, 3, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PTO_ELEC_1000ECO', 13, 3, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PORSHLIGHT_FEATURE', 14, 3, 4, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PORSHLIGHT_STATE', 15, 3, 5, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_1', 16, 3, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_2', 17, 3, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_FRONT_ROOF', 18, 4, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('BEACON', 19, 4, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_REAR_ROOF', 20, 4, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_REAR_FENDER', 21, 4, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_FRONT_HOOD', 22, 4, 4, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('BEAM_HANDRAIL', 23, 4, 5, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_01', 24, 4, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_02', 25, 4, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_03', 26, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('BEACON_AUTO', 27, 6, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_HANDRAIL', 28, 6, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('JAPON', 29, 6, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('WORK_HANDRAIL_2', 30, 6, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('CAB_SUSP_FEATURE', 31, 6, 4, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_05', 32, 6, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_06', 33, 6, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('PLATFORM', 34, 7, 0, 4, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RHS_LEVER', 35, 7, 4, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_07', 36, 7, 6, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('REVERSE_LIGHT', 37, 8, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_08', 38, 8, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_09', 39, 8, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_10', 40, 8, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_11', 41, 8, 4, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_12', 42, 8, 5, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_13', 43, 8, 6, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))
    EEPROM_Parameters.add_parameter(DiagParameter('RESERVED_14', 44, 8, 7, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Enabled': [0, 0], 'Disabled': [1, 1]}, 0, 1, '', False, False, False))

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

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class SRC14_S2_BVIOControlDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [4], [4], '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))


SRC14_S2_BVDTCSnapshotdDids = {
}


class SRC14_S2Client(ECUClient):
    class FlashData(Enum):
        pass

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0x31, "SRC14_S2", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=6, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = SRC14_S2_BVReadDataSignals
        self.write_dids = SRC14_S2_BVWriteDataSignals
        self.routine_dids = SRC14_S2_BVRoutineIdentifierSignals
        self.io_dids = SRC14_S2_BVIOControlDataSignals
        self.dtc_snapshot_dids = SRC14_S2_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

