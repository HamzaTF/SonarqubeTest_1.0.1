from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class SRCM_BVRoutineIdentifierSignals:
    CheckMemoryRequest = DiagMessage(0x0202, 'CheckMemoryRequest', [2], [1, 3, 4, 5], '', 0)

    CheckMemoryResponse = DiagMessage(0x0202, 'CheckMemoryResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckMemoryResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PASSED': [0, 0], 'FAILED': [1, 1]}, 0, 1, '', False, False, False))

    CheckProgrammingPreConditionsRequest = DiagMessage(0x0203, 'CheckProgrammingPreConditionsRequest', [3], None, '', 0)

    CheckProgrammingPreConditionsResponse = DiagMessage(0x0203, 'CheckProgrammingPreConditionsResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckProgrammingPreConditionsResponse.add_parameter(DiagParameter('ProgrammingPreConditionList', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGINE_SPEED_NOT_ZERO': [1, 1], 'IMMOBILIZER_NOT_UNLOCKED': [2, 2], 'TRANSMISSION_SPEED_IN_NOT_ZERO': [3, 3], 'TRANSMISSION_SPEED_OUT_NOT_ZERO': [4, 4], 'VEHICLE_SPEED_NOT_ZERO': [5, 5], 'CONTROLLING_ACTIVE': [6, 6], 'IGNITION_OFF_ON_NECESSARY': [7, 7], 'PROGRAMMING_VOLTAGE_TOO_LOW': [8, 8], 'IGNITION_NOT_ON': [9, 9], 'VEHICLE_VOLTAGE_TOO_LOW': [10, 10], 'TEMPERATURE_TOO_HIGH': [11, 11], 'TEMPERATURE_TOO_LOW': [12, 12], 'RESERVED_BY_HIS': [13, 127], 'VEHICLE_NOT_IN_SAFE_STATE': [128, 128], 'RESERVED_BY_MANUFACTURER': [129, 191], 'RESERVED_BY_SUPPLIER': [192, 255]}, 1, 255, 'for each wrong condition 1 byte is sent, if all conditions are meet 0 bytes are transmitted', False, True, False))

    ResultRequestFrontAxleCalibrationRequest = DiagMessage(0x1200, 'ResultRequestFrontAxleCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestFrontAxleCalibrationResponse = DiagMessage(0x1200, 'ResultRequestFrontAxleCalibrationResponse', [3, 4, 64], [1, 4, 5], '', 0)

    StartFrontAxleCalibrationRequest = DiagMessage(0x1200, 'StartFrontAxleCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartFrontAxleCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartFrontAxleCalibrationResponse = DiagMessage(0x1200, 'StartFrontAxleCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartFrontAxleCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopFrontAxleCalibrationRequest = DiagMessage(0x1200, 'StopFrontAxleCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopFrontAxleCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopFrontAxleCalibrationResponse = DiagMessage(0x1200, 'StopFrontAxleCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopFrontAxleCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopFrontAxleCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

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

    ResultRequestFrontHitchCalibrationRequest = DiagMessage(0x1202, 'ResultRequestFrontHitchCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestFrontHitchCalibrationResponse = DiagMessage(0x1202, 'ResultRequestFrontHitchCalibrationResponse', [3, 64], [1, 4, 5], '', 0)

    StartFrontHitchCalibrationRequest = DiagMessage(0x1202, 'StartFrontHitchCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartFrontHitchCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartFrontHitchCalibrationResponse = DiagMessage(0x1202, 'StartFrontHitchCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartFrontHitchCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopFrontHitchCalibrationRequest = DiagMessage(0x1202, 'StopFrontHitchCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopFrontHitchCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopFrontHitchCalibrationResponse = DiagMessage(0x1202, 'StopFrontHitchCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopFrontHitchCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopFrontHitchCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

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

    ResultRequestRearPtoCalibrationRequest = DiagMessage(0x1205, 'ResultRequestRearPtoCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestRearPtoCalibrationResponse = DiagMessage(0x1205, 'ResultRequestRearPtoCalibrationResponse', [3, 64], [1, 4, 5], '', 0)

    StartRearPtoCalibrationRequest = DiagMessage(0x1205, 'StartRearPtoCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartRearPtoCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartRearPtoCalibrationResponse = DiagMessage(0x1205, 'StartRearPtoCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartRearPtoCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopRearPtoCalibrationRequest = DiagMessage(0x1205, 'StopRearPtoCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopRearPtoCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopRearPtoCalibrationResponse = DiagMessage(0x1205, 'StopRearPtoCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopRearPtoCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopRearPtoCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

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

    StartWASCenterCalibrationRequest = DiagMessage(0x1208, 'StartWASCenterCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartWASCenterCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartWASCenterCalibrationResponse = DiagMessage(0x1208, 'StartWASCenterCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartWASCenterCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopWASCenterCalibrationRequest = DiagMessage(0x1208, 'StopWASCenterCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopWASCenterCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopWASCenterCalibrationResponse = DiagMessage(0x1208, 'StopWASCenterCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopWASCenterCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopWASCenterCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

    ResultRequestThrottlePedalCalibrationRequest = DiagMessage(0x1209, 'ResultRequestThrottlePedalCalibrationRequest', [3, 64], [1, 4, 5], '', 0)

    ResultRequestThrottlePedalCalibrationResponse = DiagMessage(0x1209, 'ResultRequestThrottlePedalCalibrationResponse', [3, 64], [1, 4, 5], '', 0)

    StartThrottlePedalCalibrationRequest = DiagMessage(0x1209, 'StartThrottlePedalCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StartThrottlePedalCalibrationRequest.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))

    StartThrottlePedalCalibrationResponse = DiagMessage(0x1209, 'StartThrottlePedalCalibrationResponse', [3, 64], [1, 4, 5], '', 1)
    StartThrottlePedalCalibrationResponse.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopThrottlePedalCalibrationRequest = DiagMessage(0x1209, 'StopThrottlePedalCalibrationRequest', [3, 64], [1, 4, 5], '', 1)
    StopThrottlePedalCalibrationRequest.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopThrottlePedalCalibrationResponse = DiagMessage(0x1209, 'StopThrottlePedalCalibrationResponse', [3, 64], [1, 4, 5], '', 2)
    StopThrottlePedalCalibrationResponse.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopThrottlePedalCalibrationResponse.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

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


class SRCM_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    FrontAxleCalibrationState = DiagMessage(0x1100, 'FrontAxleCalibrationState', [1, 3, 4, 64], None, '', 1)
    FrontAxleCalibrationState.add_parameter(DiagParameter('FrontAxleCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    RearHitchCalibrationState = DiagMessage(0x1101, 'RearHitchCalibrationState', [1, 3, 4, 64], None, '', 1)
    RearHitchCalibrationState.add_parameter(DiagParameter('RearHitchCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    FrontHitchCalibrationState = DiagMessage(0x1102, 'FrontHitchCalibrationState', [1, 3, 4, 64], None, '', 1)
    FrontHitchCalibrationState.add_parameter(DiagParameter('FrontHitchCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    ClutchPedalCalibrationState = DiagMessage(0x1103, 'ClutchPedalCalibrationState', [1, 3, 4, 64], None, '', 1)
    ClutchPedalCalibrationState.add_parameter(DiagParameter('ClutchPedalCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    RadarCalibrationState = DiagMessage(0x1104, 'RadarCalibrationState', [1, 3, 4, 64], None, '', 1)
    RadarCalibrationState.add_parameter(DiagParameter('RadarCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    RearPtoCalibrationState = DiagMessage(0x1105, 'RearPtoCalibrationState', [1, 3, 4, 64], None, '', 1)
    RearPtoCalibrationState.add_parameter(DiagParameter('RearPtoCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PVEDCalibrationState = DiagMessage(0x1106, 'PVEDCalibrationState', [1, 3, 4, 64], None, '', 1)
    PVEDCalibrationState.add_parameter(DiagParameter('PVEDCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    WASRightLeftCalibrationState = DiagMessage(0x1107, 'WASRightLeftCalibrationState', [1, 3, 4, 64], None, '', 1)
    WASRightLeftCalibrationState.add_parameter(DiagParameter('WASRightLeftCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    WASCenterCalibrationState = DiagMessage(0x1108, 'WASCenterCalibrationState', [1, 3, 4, 64], None, '', 1)
    WASCenterCalibrationState.add_parameter(DiagParameter('WASCenterCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    ThrottlePedalCalibrationState = DiagMessage(0x1109, 'ThrottlePedalCalibrationState', [1, 3, 4, 64], None, '', 1)
    ThrottlePedalCalibrationState.add_parameter(DiagParameter('ThrottlePedalCalibrationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    MaintenanceNextServiceHours = DiagMessage(0x1330, 'MaintenanceNextServiceHours', [1, 2, 3, 4, 64], None, '', 1)
    MaintenanceNextServiceHours.add_parameter(DiagParameter('MaintenanceNSHs', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 4294967295, 'Next Maintenance Service Hours', False, False, False))

    TractorHoursOffset = DiagMessage(0x1331, 'TractorHoursOffset', [1, 2, 3, 4, 64], None, '', 1)
    TractorHoursOffset.add_parameter(DiagParameter('TractorHoursOffset', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', -2147483646, 2147483646, 'Tractor Hours Offset 0.1h', False, False, False))

    CurrentTractorWheelSize = DiagMessage(0x1332, 'CurrentTractorWheelSize', [1, 2, 3, 4, 64], None, '', 1)
    CurrentTractorWheelSize.add_parameter(DiagParameter('CurrentTractorWhlSze', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 3000, 7500, 'Current Tractor WheelSize in mm', False, False, False))

    TractorWheelMaxSize = DiagMessage(0x1333, 'TractorWheelMaxSize', [1, 2, 3, 4, 64], None, '', 1)
    TractorWheelMaxSize.add_parameter(DiagParameter('TractorWlMxSze', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 3000, 7500, 'Tractor Wheel Max Size in mm', False, False, False))

    UdsDiag_GetAntiStallProgress = DiagMessage(0xA700, 'UdsDiag_GetAntiStallProgress', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetAntiStallProgress.add_parameter(DiagParameter('AntiStallProgress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetAntiStallStatus = DiagMessage(0xA701, 'UdsDiag_GetAntiStallStatus', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetAntiStallStatus.add_parameter(DiagParameter('AntiStallStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetPTOAutoState = DiagMessage(0xA702, 'UdsDiag_GetPTOAutoState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPTOAutoState.add_parameter(DiagParameter('PTOAutoState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetSpeedPreset = DiagMessage(0xA703, 'UdsDiag_GetSpeedPreset', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSpeedPreset.add_parameter(DiagParameter('SpeedPreset', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'MODE_1': [0, 0], 'MODE_2': [1, 1], 'NOT_VALID': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetTractorSpeedLimit = DiagMessage(0xA710, 'UdsDiag_GetTractorSpeedLimit', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetTractorSpeedLimit.add_parameter(DiagParameter('BrakeCouplingSpeedLimit', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '', False, False, False))

    UdsDiag_GetTractorSpeed = DiagMessage(0xA711, 'UdsDiag_GetTractorSpeed', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetTractorSpeed.add_parameter(DiagParameter('TractorActualSpeed', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '', False, False, False))

    PIN_250_DI_01 = DiagMessage(0xA800, 'PIN_250_DI_01', [1, 3, 4, 64], None, '', 6)
    PIN_250_DI_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_250_DI_01.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_236_DI_02 = DiagMessage(0xA801, 'PIN_236_DI_02', [1, 3, 4, 64], None, '', 6)
    PIN_236_DI_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_236_DI_02.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_209_DI_03 = DiagMessage(0xA802, 'PIN_209_DI_03', [1, 3, 4, 64], None, '', 6)
    PIN_209_DI_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_209_DI_03.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_147_DI_04 = DiagMessage(0xA803, 'PIN_147_DI_04', [1, 3, 4, 64], None, '', 6)
    PIN_147_DI_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_147_DI_04.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_223_DI_05 = DiagMessage(0xA804, 'PIN_223_DI_05', [1, 3, 4, 64], None, '', 6)
    PIN_223_DI_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_223_DI_05.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_148_DI_06 = DiagMessage(0xA805, 'PIN_148_DI_06', [1, 3, 4, 64], None, '', 6)
    PIN_148_DI_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_148_DI_06.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_159_DI_07 = DiagMessage(0xA806, 'PIN_159_DI_07', [1, 3, 4, 64], None, '', 6)
    PIN_159_DI_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_159_DI_07.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_158_DI_08 = DiagMessage(0xA807, 'PIN_158_DI_08', [1, 3, 4, 64], None, '', 6)
    PIN_158_DI_08.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_158_DI_08.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_214_DI_09 = DiagMessage(0xA808, 'PIN_214_DI_09', [1, 3, 4, 64], None, '', 6)
    PIN_214_DI_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_214_DI_09.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_157_DI_10 = DiagMessage(0xA809, 'PIN_157_DI_10', [1, 3, 4, 64], None, '', 6)
    PIN_157_DI_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_157_DI_10.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_252_DI_11 = DiagMessage(0xA80A, 'PIN_252_DI_11', [1, 3, 4, 64], None, '', 6)
    PIN_252_DI_11.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_252_DI_11.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_238_DI_12 = DiagMessage(0xA80B, 'PIN_238_DI_12', [1, 3, 4, 64], None, '', 6)
    PIN_238_DI_12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_238_DI_12.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_222_DI_13 = DiagMessage(0xA80C, 'PIN_222_DI_13', [1, 3, 4, 64], None, '', 6)
    PIN_222_DI_13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_222_DI_13.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_210_DI_14 = DiagMessage(0xA80D, 'PIN_210_DI_14', [1, 3, 4, 64], None, '', 6)
    PIN_210_DI_14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_210_DI_14.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_136_DI_15 = DiagMessage(0xA80E, 'PIN_136_DI_15', [1, 3, 4, 64], None, '', 6)
    PIN_136_DI_15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_136_DI_15.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_137_DI_16 = DiagMessage(0xA80F, 'PIN_137_DI_16', [1, 3, 4, 64], None, '', 6)
    PIN_137_DI_16.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_137_DI_16.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_135_DI_17 = DiagMessage(0xA810, 'PIN_135_DI_17', [1, 3, 4, 64], None, '', 6)
    PIN_135_DI_17.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_135_DI_17.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_134_DI_18 = DiagMessage(0xA811, 'PIN_134_DI_18', [1, 3, 4, 64], None, '', 6)
    PIN_134_DI_18.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_134_DI_18.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_211_DI_19 = DiagMessage(0xA812, 'PIN_211_DI_19', [1, 3, 4, 64], None, '', 6)
    PIN_211_DI_19.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_211_DI_19.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_144_DI_20 = DiagMessage(0xA813, 'PIN_144_DI_20', [1, 3, 4, 64], None, '', 6)
    PIN_144_DI_20.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_144_DI_20.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_224_DI_21 = DiagMessage(0xA814, 'PIN_224_DI_21', [1, 3, 4, 64], None, '', 6)
    PIN_224_DI_21.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_224_DI_21.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_143_DI_22 = DiagMessage(0xA815, 'PIN_143_DI_22', [1, 3, 4, 64], None, '', 6)
    PIN_143_DI_22.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_143_DI_22.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_142_DI_23 = DiagMessage(0xA816, 'PIN_142_DI_23', [1, 3, 4, 64], None, '', 6)
    PIN_142_DI_23.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_142_DI_23.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_235_DI_24 = DiagMessage(0xA817, 'PIN_235_DI_24', [1, 3, 4, 64], None, '', 6)
    PIN_235_DI_24.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_235_DI_24.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_247_DI_25 = DiagMessage(0xA818, 'PIN_247_DI_25', [1, 3, 4, 64], None, '', 6)
    PIN_247_DI_25.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_247_DI_25.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_234_DI_26 = DiagMessage(0xA819, 'PIN_234_DI_26', [1, 3, 4, 64], None, '', 6)
    PIN_234_DI_26.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_234_DI_26.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_225_DI_27 = DiagMessage(0xA81A, 'PIN_225_DI_27', [1, 3, 4, 64], None, '', 6)
    PIN_225_DI_27.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_225_DI_27.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_212_DI_28 = DiagMessage(0xA81B, 'PIN_212_DI_28', [1, 3, 4, 64], None, '', 6)
    PIN_212_DI_28.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_212_DI_28.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_248_DI_29 = DiagMessage(0xA81C, 'PIN_248_DI_29', [1, 3, 4, 64], None, '', 6)
    PIN_248_DI_29.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_248_DI_29.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_237_DI_30 = DiagMessage(0xA81D, 'PIN_237_DI_30', [1, 3, 4, 64], None, '', 6)
    PIN_237_DI_30.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_237_DI_30.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_239_DI_31 = DiagMessage(0xA81E, 'PIN_239_DI_31', [1, 3, 4, 64], None, '', 6)
    PIN_239_DI_31.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_239_DI_31.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_251_DI_32 = DiagMessage(0xA81F, 'PIN_251_DI_32', [1, 3, 4, 64], None, '', 6)
    PIN_251_DI_32.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [32, 32]}, 32, 32, '', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))
    PIN_251_DI_32.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_256_DOH_01 = DiagMessage(0xA828, 'PIN_256_DOH_01', [1, 3, 4, 64], None, '', 4)
    PIN_256_DOH_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_256_DOH_01.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_256_DOH_01.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_256_DOH_01.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_257_DOH_02 = DiagMessage(0xA829, 'PIN_257_DOH_02', [1, 3, 4, 64], None, '', 4)
    PIN_257_DOH_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_257_DOH_02.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_257_DOH_02.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_257_DOH_02.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_241_DOH_03 = DiagMessage(0xA82A, 'PIN_241_DOH_03', [1, 3, 4, 64], None, '', 4)
    PIN_241_DOH_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_241_DOH_03.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_241_DOH_03.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_241_DOH_03.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_242_DOH_04 = DiagMessage(0xA82B, 'PIN_242_DOH_04', [1, 3, 4, 64], None, '', 4)
    PIN_242_DOH_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_242_DOH_04.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_242_DOH_04.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_242_DOH_04.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_114_DOH_05 = DiagMessage(0xA82C, 'PIN_114_DOH_05', [1, 3, 4, 64], None, '', 4)
    PIN_114_DOH_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_114_DOH_05.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_114_DOH_05.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_114_DOH_05.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_244_DOH_07 = DiagMessage(0xA82D, 'PIN_244_DOH_07', [1, 3, 4, 64], None, '', 4)
    PIN_244_DOH_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_244_DOH_07.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_244_DOH_07.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_244_DOH_07.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_102_DOH_10 = DiagMessage(0xA82E, 'PIN_102_DOH_10', [1, 3, 4, 64], None, '', 4)
    PIN_102_DOH_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_102_DOH_10.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_102_DOH_10.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_102_DOH_10.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_103_DOH_12 = DiagMessage(0xA82F, 'PIN_103_DOH_12', [1, 3, 4, 64], None, '', 4)
    PIN_103_DOH_12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_103_DOH_12.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_103_DOH_12.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_103_DOH_12.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_105_DOH_13 = DiagMessage(0xA830, 'PIN_105_DOH_13', [1, 3, 4, 64], None, '', 4)
    PIN_105_DOH_13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_105_DOH_13.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_105_DOH_13.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_105_DOH_13.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_128_DOH_14 = DiagMessage(0xA831, 'PIN_128_DOH_14', [1, 3, 4, 64], None, '', 4)
    PIN_128_DOH_14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_128_DOH_14.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_128_DOH_14.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_128_DOH_14.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_127_DOH_15 = DiagMessage(0xA832, 'PIN_127_DOH_15', [1, 3, 4, 64], None, '', 4)
    PIN_127_DOH_15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_127_DOH_15.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_127_DOH_15.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_127_DOH_15.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_106_DOH_16 = DiagMessage(0xA833, 'PIN_106_DOH_16', [1, 3, 4, 64], None, '', 4)
    PIN_106_DOH_16.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_106_DOH_16.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [12, 12]}, 12, 12, '', False, False, False))
    PIN_106_DOH_16.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected OUTput Not Active': [0, 0], 'Selected OUTput Active': [1, 1]}, 0, 1, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    PIN_106_DOH_16.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_119_AI_01 = DiagMessage(0xA850, 'PIN_119_AI_01', [1, 3, 4, 64], None, '', 5)
    PIN_119_AI_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_119_AI_01.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_119_AI_01.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_119_AI_01.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_119_AI_01.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_120_AI_02 = DiagMessage(0xA851, 'PIN_120_AI_02', [1, 3, 4, 64], None, '', 5)
    PIN_120_AI_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_120_AI_02.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_120_AI_02.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_120_AI_02.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_120_AI_02.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_121_AI_03 = DiagMessage(0xA852, 'PIN_121_AI_03', [1, 3, 4, 64], None, '', 5)
    PIN_121_AI_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_121_AI_03.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_121_AI_03.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_121_AI_03.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_121_AI_03.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_116_AI_04 = DiagMessage(0xA853, 'PIN_116_AI_04', [1, 3, 4, 64], None, '', 5)
    PIN_116_AI_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_116_AI_04.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_116_AI_04.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_116_AI_04.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_116_AI_04.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_117_AI_05 = DiagMessage(0xA854, 'PIN_117_AI_05', [1, 3, 4, 64], None, '', 5)
    PIN_117_AI_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_117_AI_05.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_117_AI_05.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_117_AI_05.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_117_AI_05.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_118_AI_06 = DiagMessage(0xA855, 'PIN_118_AI_06', [1, 3, 4, 64], None, '', 5)
    PIN_118_AI_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_118_AI_06.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_118_AI_06.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_118_AI_06.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_118_AI_06.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_231_AI_07 = DiagMessage(0xA856, 'PIN_231_AI_07', [1, 3, 4, 64], None, '', 5)
    PIN_231_AI_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_231_AI_07.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_231_AI_07.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_231_AI_07.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_231_AI_07.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_217_AI_08 = DiagMessage(0xA857, 'PIN_217_AI_08', [1, 3, 4, 64], None, '', 5)
    PIN_217_AI_08.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_217_AI_08.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_217_AI_08.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_217_AI_08.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_217_AI_08.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_213_AI_09 = DiagMessage(0xA858, 'PIN_213_AI_09', [1, 3, 4, 64], None, '', 5)
    PIN_213_AI_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_213_AI_09.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_213_AI_09.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_213_AI_09.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_213_AI_09.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_226_AI_10 = DiagMessage(0xA859, 'PIN_226_AI_10', [1, 3, 4, 64], None, '', 5)
    PIN_226_AI_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_226_AI_10.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_226_AI_10.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_226_AI_10.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_226_AI_10.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_228_AI_11 = DiagMessage(0xA85A, 'PIN_228_AI_11', [1, 3, 4, 64], None, '', 5)
    PIN_228_AI_11.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_228_AI_11.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_228_AI_11.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_228_AI_11.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_228_AI_11.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_188_AI_12 = DiagMessage(0xA85B, 'PIN_188_AI_12', [1, 3, 4, 64], None, '', 5)
    PIN_188_AI_12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_188_AI_12.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_188_AI_12.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_188_AI_12.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 8500, '', False, False, False))
    PIN_188_AI_12.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_218_CI_03 = DiagMessage(0xA85C, 'PIN_218_CI_03', [1, 3, 4, 64], None, '', 5)
    PIN_218_CI_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_218_CI_03.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_218_CI_03.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_218_CI_03.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_218_CI_03.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_229_CI_04 = DiagMessage(0xA85D, 'PIN_229_CI_04', [1, 3, 4, 64], None, '', 5)
    PIN_229_CI_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_229_CI_04.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_229_CI_04.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_229_CI_04.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_229_CI_04.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_171_CI_05 = DiagMessage(0xA85E, 'PIN_171_CI_05', [1, 3, 4, 64], None, '', 5)
    PIN_171_CI_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_171_CI_05.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_171_CI_05.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_171_CI_05.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_171_CI_05.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_227_CI_06 = DiagMessage(0xA85F, 'PIN_227_CI_06', [1, 3, 4, 64], None, '', 5)
    PIN_227_CI_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_227_CI_06.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_227_CI_06.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_227_CI_06.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_227_CI_06.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_167_CI_07 = DiagMessage(0xA860, 'PIN_167_CI_07', [1, 3, 4, 64], None, '', 5)
    PIN_167_CI_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_167_CI_07.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_167_CI_07.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_167_CI_07.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_167_CI_07.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_170_CI_09 = DiagMessage(0xA861, 'PIN_170_CI_09', [1, 3, 4, 64], None, '', 5)
    PIN_170_CI_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_170_CI_09.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_170_CI_09.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_170_CI_09.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_170_CI_09.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_165_CI_10 = DiagMessage(0xA862, 'PIN_165_CI_10', [1, 3, 4, 64], None, '', 5)
    PIN_165_CI_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_165_CI_10.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_165_CI_10.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_165_CI_10.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_165_CI_10.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_230_CI_11 = DiagMessage(0xA863, 'PIN_230_CI_11', [1, 3, 4, 64], None, '', 5)
    PIN_230_CI_11.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_230_CI_11.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_230_CI_11.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_230_CI_11.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_230_CI_11.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_140_CI_12 = DiagMessage(0xA864, 'PIN_140_CI_12', [1, 3, 4, 64], None, '', 5)
    PIN_140_CI_12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_140_CI_12.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_140_CI_12.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_140_CI_12.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_140_CI_12.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_139_CI_13 = DiagMessage(0xA865, 'PIN_139_CI_13', [1, 3, 4, 64], None, '', 5)
    PIN_139_CI_13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_139_CI_13.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_139_CI_13.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_139_CI_13.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_139_CI_13.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_166_CI_14 = DiagMessage(0xA866, 'PIN_166_CI_14', [1, 3, 4, 64], None, '', 5)
    PIN_166_CI_14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_166_CI_14.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_166_CI_14.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_166_CI_14.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_166_CI_14.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_164_CI_15 = DiagMessage(0xA867, 'PIN_164_CI_15', [1, 3, 4, 64], None, '', 5)
    PIN_164_CI_15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_164_CI_15.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_164_CI_15.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_164_CI_15.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_164_CI_15.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_141_CI_16 = DiagMessage(0xA868, 'PIN_141_CI_16', [1, 3, 4, 64], None, '', 5)
    PIN_141_CI_16.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_141_CI_16.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [25, 25]}, 25, 25, '', False, False, False))
    PIN_141_CI_16.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_141_CI_16.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_141_CI_16.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_221_AO_01 = DiagMessage(0xA878, 'PIN_221_AO_01', [1, 3, 4, 64], None, '', 5)
    PIN_221_AO_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_221_AO_01.add_parameter(DiagParameter('TotalNOfAO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 1, '', False, False, False))
    PIN_221_AO_01.add_parameter(DiagParameter('DigitalConversionAnalog', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'Digital to Analog Conversion value', False, False, False))
    PIN_221_AO_01.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?A', 4000, 20000, '', False, False, False))
    PIN_221_AO_01.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))

    PIN_112_DFI_01 = DiagMessage(0xA8A0, 'PIN_112_DFI_01', [1, 3, 4, 64], None, '', 6)
    PIN_112_DFI_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [8, 8]}, 8, 8, '', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_112_DFI_01.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_113_DFI_02 = DiagMessage(0xA8A1, 'PIN_113_DFI_02', [1, 3, 4, 64], None, '', 6)
    PIN_113_DFI_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [8, 8]}, 8, 8, '', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_113_DFI_02.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_110_DFI_03 = DiagMessage(0xA8A2, 'PIN_110_DFI_03', [1, 3, 4, 64], None, '', 6)
    PIN_110_DFI_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [8, 8]}, 8, 8, '', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_110_DFI_03.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_111_DFI_04 = DiagMessage(0xA8A3, 'PIN_111_DFI_04', [1, 3, 4, 64], None, '', 6)
    PIN_111_DFI_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [8, 8]}, 8, 8, '', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_111_DFI_04.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_109_DFI_05 = DiagMessage(0xA8A4, 'PIN_109_DFI_05', [1, 3, 4, 64], None, '', 6)
    PIN_109_DFI_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [8, 8]}, 8, 8, '', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_109_DFI_05.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_108_DFI_06 = DiagMessage(0xA8A5, 'PIN_108_DFI_06', [1, 3, 4, 64], None, '', 6)
    PIN_108_DFI_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [8, 8]}, 8, 8, '', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_108_DFI_06.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_133_DFI_07 = DiagMessage(0xA8A6, 'PIN_133_DFI_07', [1, 3, 4, 64], None, '', 6)
    PIN_133_DFI_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [8, 8]}, 8, 8, '', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_133_DFI_07.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_132_DFI_08 = DiagMessage(0xA8A7, 'PIN_132_DFI_08', [1, 3, 4, 64], None, '', 6)
    PIN_132_DFI_08.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [8, 8]}, 8, 8, '', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 1.4, 10000, '', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('DiagData', 5, 3, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    PIN_132_DFI_08.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 7500, '', False, False, False))

    PIN_177_POH_02 = DiagMessage(0xA8C8, 'PIN_177_POH_02', [1, 3, 4, 64], None, '', 5)
    PIN_177_POH_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_177_POH_02.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_177_POH_02.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_177_POH_02.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_177_POH_02.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_186_POH_04 = DiagMessage(0xA8C9, 'PIN_186_POH_04', [1, 3, 4, 64], None, '', 5)
    PIN_186_POH_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_186_POH_04.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_186_POH_04.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_186_POH_04.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_186_POH_04.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_151_POH_05 = DiagMessage(0xA8CA, 'PIN_151_POH_05', [1, 3, 4, 64], None, '', 5)
    PIN_151_POH_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_151_POH_05.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_151_POH_05.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_151_POH_05.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_151_POH_05.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_175_POH_06 = DiagMessage(0xA8CB, 'PIN_175_POH_06', [1, 3, 4, 64], None, '', 5)
    PIN_175_POH_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_175_POH_06.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_175_POH_06.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_175_POH_06.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_175_POH_06.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_152_POH_07 = DiagMessage(0xA8CC, 'PIN_152_POH_07', [1, 3, 4, 64], None, '', 5)
    PIN_152_POH_07.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_152_POH_07.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_152_POH_07.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_152_POH_07.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_152_POH_07.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_149_POH_09 = DiagMessage(0xA8CD, 'PIN_149_POH_09', [1, 3, 4, 64], None, '', 5)
    PIN_149_POH_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_149_POH_09.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_149_POH_09.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_149_POH_09.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_149_POH_09.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_173_POH_10 = DiagMessage(0xA8CE, 'PIN_173_POH_10', [1, 3, 4, 64], None, '', 5)
    PIN_173_POH_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_173_POH_10.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_173_POH_10.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_173_POH_10.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_173_POH_10.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_126_POH_17 = DiagMessage(0xA8CF, 'PIN_126_POH_17', [1, 3, 4, 64], None, '', 5)
    PIN_126_POH_17.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_126_POH_17.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_126_POH_17.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_126_POH_17.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_126_POH_17.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_190_PDOH_03 = DiagMessage(0xA8D0, 'PIN_190_PDOH_03', [1, 3, 4, 64], None, '', 5)
    PIN_190_PDOH_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_190_PDOH_03.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_190_PDOH_03.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_190_PDOH_03.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 100, '', False, False, False))
    PIN_190_PDOH_03.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_189_PDOH_04 = DiagMessage(0xA8D1, 'PIN_189_PDOH_04', [1, 3, 4, 64], None, '', 5)
    PIN_189_PDOH_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_189_PDOH_04.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_189_PDOH_04.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_189_PDOH_04.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_189_PDOH_04.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_194_PDOH_05 = DiagMessage(0xA8D2, 'PIN_194_PDOH_05', [1, 3, 4, 64], None, '', 5)
    PIN_194_PDOH_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_194_PDOH_05.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_194_PDOH_05.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_194_PDOH_05.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_194_PDOH_05.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_193_PDOH_06 = DiagMessage(0xA8D3, 'PIN_193_PDOH_06', [1, 3, 4, 64], None, '', 5)
    PIN_193_PDOH_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_193_PDOH_06.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_193_PDOH_06.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_193_PDOH_06.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_193_PDOH_06.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_187_PDOH_08 = DiagMessage(0xA8D4, 'PIN_187_PDOH_08', [1, 3, 4, 64], None, '', 5)
    PIN_187_PDOH_08.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_187_PDOH_08.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_187_PDOH_08.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_187_PDOH_08.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_187_PDOH_08.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_196_PDOH_09 = DiagMessage(0xA8D5, 'PIN_196_PDOH_09', [1, 3, 4, 64], None, '', 5)
    PIN_196_PDOH_09.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_196_PDOH_09.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_196_PDOH_09.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_196_PDOH_09.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_196_PDOH_09.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_249_PDOH_10 = DiagMessage(0xA8D6, 'PIN_249_PDOH_10', [1, 3, 4, 64], None, '', 5)
    PIN_249_PDOH_10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_249_PDOH_10.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_249_PDOH_10.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_249_PDOH_10.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 100, '', False, False, False))
    PIN_249_PDOH_10.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_153_PDOH_13 = DiagMessage(0xA8D7, 'PIN_153_PDOH_13', [1, 3, 4, 64], None, '', 5)
    PIN_153_PDOH_13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_153_PDOH_13.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_153_PDOH_13.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_153_PDOH_13.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_153_PDOH_13.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_154_PDOH_14 = DiagMessage(0xA8D8, 'PIN_154_PDOH_14', [1, 3, 4, 64], None, '', 5)
    PIN_154_PDOH_14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_154_PDOH_14.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_154_PDOH_14.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_154_PDOH_14.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_154_PDOH_14.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_176_PDOH_15 = DiagMessage(0xA8D9, 'PIN_176_PDOH_15', [1, 3, 4, 64], None, '', 5)
    PIN_176_PDOH_15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_176_PDOH_15.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_176_PDOH_15.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_176_PDOH_15.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_176_PDOH_15.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_129_PDOH_16 = DiagMessage(0xA8DA, 'PIN_129_PDOH_16', [1, 3, 4, 64], None, '', 5)
    PIN_129_PDOH_16.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_129_PDOH_16.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_129_PDOH_16.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_129_PDOH_16.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_129_PDOH_16.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_130_PDOH_17 = DiagMessage(0xA8DB, 'PIN_130_PDOH_17', [1, 3, 4, 64], None, '', 5)
    PIN_130_PDOH_17.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_130_PDOH_17.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_130_PDOH_17.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_130_PDOH_17.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_130_PDOH_17.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_107_PDOH_18 = DiagMessage(0xA8DC, 'PIN_107_PDOH_18', [1, 3, 4, 64], None, '', 5)
    PIN_107_PDOH_18.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_107_PDOH_18.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_107_PDOH_18.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_107_PDOH_18.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_107_PDOH_18.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_104_PDOH_19 = DiagMessage(0xA8DD, 'PIN_104_PDOH_19', [1, 3, 4, 64], None, '', 5)
    PIN_104_PDOH_19.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_104_PDOH_19.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_104_PDOH_19.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_104_PDOH_19.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_104_PDOH_19.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_115_PDOH_20 = DiagMessage(0xA8DE, 'PIN_115_PDOH_20', [1, 3, 4, 64], None, '', 5)
    PIN_115_PDOH_20.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_115_PDOH_20.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_115_PDOH_20.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_115_PDOH_20.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_115_PDOH_20.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_243_PDOH_21 = DiagMessage(0xA8DF, 'PIN_243_PDOH_21', [1, 3, 4, 64], None, '', 5)
    PIN_243_PDOH_21.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_243_PDOH_21.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_243_PDOH_21.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_243_PDOH_21.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_243_PDOH_21.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_179_DOL_01 = DiagMessage(0xA8E0, 'PIN_179_DOL_01', [1, 3, 4, 64], None, '', 5)
    PIN_179_DOL_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_179_DOL_01.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_179_DOL_01.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_179_DOL_01.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_179_DOL_01.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_191_DOL_02 = DiagMessage(0xA8E1, 'PIN_191_DOL_02', [1, 3, 4, 64], None, '', 5)
    PIN_191_DOL_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_191_DOL_02.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_191_DOL_02.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_191_DOL_02.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_191_DOL_02.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_192_DOL_03 = DiagMessage(0xA8E2, 'PIN_192_DOL_03', [1, 3, 4, 64], None, '', 5)
    PIN_192_DOL_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_192_DOL_03.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_192_DOL_03.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_192_DOL_03.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_192_DOL_03.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_150_DOL_04 = DiagMessage(0xA8E3, 'PIN_150_DOL_04', [1, 3, 4, 64], None, '', 5)
    PIN_150_DOL_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_150_DOL_04.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_150_DOL_04.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_150_DOL_04.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_150_DOL_04.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_174_DOL_05 = DiagMessage(0xA8E4, 'PIN_174_DOL_05', [1, 3, 4, 64], None, '', 5)
    PIN_174_DOL_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_174_DOL_05.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_174_DOL_05.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_174_DOL_05.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 10, '', False, False, False))
    PIN_174_DOL_05.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_181_DOL_06 = DiagMessage(0xA8E5, 'PIN_181_DOL_06', [1, 3, 4, 64], None, '', 5)
    PIN_181_DOL_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_181_DOL_06.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_181_DOL_06.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_181_DOL_06.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 500, '', False, False, False))
    PIN_181_DOL_06.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_178_POL_01 = DiagMessage(0xA8E6, 'PIN_178_POL_01', [1, 3, 4, 64], None, '', 5)
    PIN_178_POL_01.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_178_POL_01.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_178_POL_01.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_178_POL_01.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_178_POL_01.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_184_POL_02 = DiagMessage(0xA8E7, 'PIN_184_POL_02', [1, 3, 4, 64], None, '', 5)
    PIN_184_POL_02.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_184_POL_02.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_184_POL_02.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_184_POL_02.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_184_POL_02.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_185_POL_03 = DiagMessage(0xA8E8, 'PIN_185_POL_03', [1, 3, 4, 64], None, '', 5)
    PIN_185_POL_03.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_185_POL_03.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_185_POL_03.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_185_POL_03.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_185_POL_03.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_182_POL_04 = DiagMessage(0xA8E9, 'PIN_182_POL_04', [1, 3, 4, 64], None, '', 5)
    PIN_182_POL_04.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_182_POL_04.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_182_POL_04.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_182_POL_04.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_182_POL_04.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_183_POL_05 = DiagMessage(0xA8EA, 'PIN_183_POL_05', [1, 3, 4, 64], None, '', 5)
    PIN_183_POL_05.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_183_POL_05.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_183_POL_05.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_183_POL_05.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_183_POL_05.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PIN_180_POL_06 = DiagMessage(0xA8EB, 'PIN_180_POL_06', [1, 3, 4, 64], None, '', 5)
    PIN_180_POL_06.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PIN_180_POL_06.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry1': [36, 36]}, 36, 36, '', False, False, False))
    PIN_180_POL_06.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 100, '', False, False, False))
    PIN_180_POL_06.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 3000, '', False, False, False))
    PIN_180_POL_06.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothing outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

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
    PowerOutput1.add_parameter(DiagParameter('DOPS_5V', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    PowerOutput2 = DiagMessage(0xA8FA, 'PowerOutput2', [1, 3, 4, 64], None, '', 1)
    PowerOutput2.add_parameter(DiagParameter('DOPS_8V5', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    UdsDiag_GetRearLinkageMode = DiagMessage(0xA8FB, 'UdsDiag_GetRearLinkageMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearLinkageMode.add_parameter(DiagParameter('RearLinkageMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [1, 1], 'TRANSPORT': [2, 2], 'WORK': [3, 3], 'QUICK SOIL': [4, 4], 'FLOAT': [5, 5], 'CALIBRATION': [6, 6], 'EXTERNAL': [7, 7], 'LOCKED': [8, 8]}, 1, 8, '', False, False, False))

    UdsDiag_GetFrontLinkageMode = DiagMessage(0xA8FC, 'UdsDiag_GetFrontLinkageMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontLinkageMode.add_parameter(DiagParameter('FrontLinkageMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'TRANSPORT': [1, 1], 'WORK': [2, 2], 'FLOAT': [3, 3], 'LOCKED': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetDampingState = DiagMessage(0xA8FD, 'UdsDiag_GetDampingState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDampingState.add_parameter(DiagParameter('DampingState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetRearDualControlState = DiagMessage(0xA8FE, 'UdsDiag_GetRearDualControlState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearDualControlState.add_parameter(DiagParameter('RearDualControlState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetFrontDualControlState = DiagMessage(0xA8FF, 'UdsDiag_GetFrontDualControlState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontDualControlState.add_parameter(DiagParameter('FrontDualControlState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetRearPtoState = DiagMessage(0xA900, 'UdsDiag_GetRearPtoState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPtoState.add_parameter(DiagParameter('RearPtoState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetRearPtoSpeedSelected = DiagMessage(0xA901, 'UdsDiag_GetRearPtoSpeedSelected', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPtoSpeedSelected.add_parameter(DiagParameter('RearPtoSpeedSelected', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], '540': [1, 1], '540E': [2, 2], '1000': [3, 3], '1000E': [4, 4], 'ERROR': [5, 5]}, 0, 5, '', False, False, False))

    UdsDiag_GetFrontPtoState = DiagMessage(0xA902, 'UdsDiag_GetFrontPtoState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontPtoState.add_parameter(DiagParameter('FrontPtoState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_Get4WDmode = DiagMessage(0xA903, 'UdsDiag_Get4WDmode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_Get4WDmode.add_parameter(DiagParameter('4WDmode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'MANU': [1, 1], 'AUTO': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_Get4WDstate = DiagMessage(0xA904, 'UdsDiag_Get4WDstate', [1, 3, 4, 64], None, '', 1)
    UdsDiag_Get4WDstate.add_parameter(DiagParameter('4WDstate', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetDifflockMode = DiagMessage(0xA905, 'UdsDiag_GetDifflockMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDifflockMode.add_parameter(DiagParameter('DifflockMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'MANU': [1, 1], 'AUTO': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetDifflockState = DiagMessage(0xA906, 'UdsDiag_GetDifflockState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDifflockState.add_parameter(DiagParameter('DifflockState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetCabSuspensionState = DiagMessage(0xA907, 'UdsDiag_GetCabSuspensionState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetCabSuspensionState.add_parameter(DiagParameter('CabSuspensionState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetCabSuspensionMode = DiagMessage(0xA908, 'UdsDiag_GetCabSuspensionMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetCabSuspensionMode.add_parameter(DiagParameter('CabSuspensionMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'SOFT': [1, 1], 'AUTO': [2, 2], 'TOUGH': [3, 3]}, 1, 3, '', False, False, False))

    UdsDiag_GetFrontAxleSuspensionState = DiagMessage(0xA909, 'UdsDiag_GetFrontAxleSuspensionState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontAxleSuspensionState.add_parameter(DiagParameter('FrontAxleSuspensionState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetAutoguideState = DiagMessage(0xA90A, 'UdsDiag_GetAutoguideState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetAutoguideState.add_parameter(DiagParameter('AutoguideState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetHVACmode = DiagMessage(0xA90B, 'UdsDiag_GetHVACmode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHVACmode.add_parameter(DiagParameter('HVACmode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'MANU': [0, 0], 'AUTO': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetACstate = DiagMessage(0xA90C, 'UdsDiag_GetACstate', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetACstate.add_parameter(DiagParameter('ACstate', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetHeadlandState = DiagMessage(0xA90D, 'UdsDiag_GetHeadlandState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHeadlandState.add_parameter(DiagParameter('HeadlandState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'HDL_STATE_OFF': [0, 0], 'HDL_STATE_RECORD': [1, 1], 'HDL_STATE_ON': [2, 2], 'HDL_STATE_PLAY_SEQ': [3, 3], 'HDL_STATE_PLAY_AUTO': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetDTMstate = DiagMessage(0xA90E, 'UdsDiag_GetDTMstate', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDTMstate.add_parameter(DiagParameter('DTMstate', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetMemoA_Value = DiagMessage(0xA90F, 'UdsDiag_GetMemoA_Value', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetMemoA_Value.add_parameter(DiagParameter('MemoA_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'rpm', 0, 255, '', False, False, False))

    UdsDiag_GetMemoSpeedState = DiagMessage(0xA910, 'UdsDiag_GetMemoSpeedState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetMemoSpeedState.add_parameter(DiagParameter('MemoSpeedState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'A': [1, 1], 'B': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetC1_Value = DiagMessage(0xA911, 'UdsDiag_GetC1_Value', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetC1_Value.add_parameter(DiagParameter('C1_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '', False, False, False))

    UdsDiag_GetC2_Value = DiagMessage(0xA912, 'UdsDiag_GetC2_Value', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetC2_Value.add_parameter(DiagParameter('C2_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '', False, False, False))

    UdsDiag_GetCruiseControlState = DiagMessage(0xA913, 'UdsDiag_GetCruiseControlState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetCruiseControlState.add_parameter(DiagParameter('CruiseControlState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CRUISE_CONTROL_DISABLED': [0, 0], 'CRUISE_CONTROL_1_SELECTED': [1, 1], 'CRUISE_CONTROL_2_SELECTED': [2, 2], 'CRUISE_CONTROL_1_ACTIVATED': [3, 3], 'CRUISE_CONTROL_2_ACTIVATED': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetPresetSpeedForwardMode1 = DiagMessage(0xA914, 'UdsDiag_GetPresetSpeedForwardMode1', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPresetSpeedForwardMode1.add_parameter(DiagParameter('PresetSpeedForwardMode1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'km/h', 0, 255, '', False, False, False))

    UdsDiag_GetPresetSpeedReverseMode1 = DiagMessage(0xA915, 'UdsDiag_GetPresetSpeedReverseMode1', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPresetSpeedReverseMode1.add_parameter(DiagParameter('PresetSpeedReverseMode1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'km/h', 0, 255, '', False, False, False))

    UdsDiag_GetPresetSpeedForwardMode2 = DiagMessage(0xA916, 'UdsDiag_GetPresetSpeedForwardMode2', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPresetSpeedForwardMode2.add_parameter(DiagParameter('PresetSpeedForwardMode2', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'km/h', 0, 255, '', False, False, False))

    UdsDiag_GetPresetSpeedReverseMode2 = DiagMessage(0xA917, 'UdsDiag_GetPresetSpeedReverseMode2', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPresetSpeedReverseMode2.add_parameter(DiagParameter('PresetSpeedReverseMode2', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'km/h', 0, 255, '', False, False, False))

    UdsDiag_GetParklockStatus = DiagMessage(0xA918, 'UdsDiag_GetParklockStatus', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetParklockStatus.add_parameter(DiagParameter('ParklockStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ENGAGED': [0, 0], 'DISENGAGED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetParklockPreDisengagement = DiagMessage(0xA919, 'UdsDiag_GetParklockPreDisengagement', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetParklockPreDisengagement.add_parameter(DiagParameter('ParklockPreDisengagement', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetSlippageRate = DiagMessage(0xA91A, 'UdsDiag_GetSlippageRate', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSlippageRate.add_parameter(DiagParameter('SlippageRate', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))

    UdsDiag_GetVistronicSpeedRequest = DiagMessage(0xA91B, 'UdsDiag_GetVistronicSpeedRequest', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetVistronicSpeedRequest.add_parameter(DiagParameter('VistronicSpeedRequest', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'rpm', 0, 255, '', False, False, False))
    UdsDiag_GetVistronicSpeedRequest.add_parameter(DiagParameter('ViscoSpeedRequestFiltered', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'rpm', 0, 255, '', False, False, False))

    UdsDiag_GetViscoRegulationState = DiagMessage(0xA91C, 'UdsDiag_GetViscoRegulationState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetViscoRegulationState.add_parameter(DiagParameter('ViscoRegulationState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NONE': [0, 0], 'COOLANT': [1, 1], 'INTAKEAIR': [2, 2], 'OILTRANS': [3, 3], 'AIRCONDITIONING ': [4, 4], 'SECUHYD': [5, 5], 'SECUTRANS': [6, 6], 'SECUFUEL': [7, 7], 'SECUENGINE': [8, 8], 'SECUCOMMUNICATION': [9, 9]}, 0, 9, '', False, False, False))

    UdsDiag_GetDriveMode = DiagMessage(0xA91D, 'UdsDiag_GetDriveMode', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDriveMode.add_parameter(DiagParameter('DriveMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'MANU': [0, 0], 'AUTO': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetSteeringSystemState = DiagMessage(0xA91E, 'UdsDiag_GetSteeringSystemState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteeringSystemState.add_parameter(DiagParameter('SteeringSystemState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetBrakeToNeutralState = DiagMessage(0xA91F, 'UdsDiag_GetBrakeToNeutralState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrakeToNeutralState.add_parameter(DiagParameter('BrakeToNeutralState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetCurrentGear = DiagMessage(0xA920, 'UdsDiag_GetCurrentGear', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetCurrentGear.add_parameter(DiagParameter('CurrentGear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_1 = DiagMessage(0xA921, 'UdsDiag_GetCommandSentToHydraulicValve_1', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_1.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_1.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_2 = DiagMessage(0xA922, 'UdsDiag_GetCommandSentToHydraulicValve_2', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_2.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_2.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_3 = DiagMessage(0xA923, 'UdsDiag_GetCommandSentToHydraulicValve_3', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_3.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_3.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_4 = DiagMessage(0xA924, 'UdsDiag_GetCommandSentToHydraulicValve_4', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_4.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_4.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_5 = DiagMessage(0xA925, 'UdsDiag_GetCommandSentToHydraulicValve_5', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_5.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_5.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_6 = DiagMessage(0xA926, 'UdsDiag_GetCommandSentToHydraulicValve_6', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_6.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_6.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_7 = DiagMessage(0xA927, 'UdsDiag_GetCommandSentToHydraulicValve_7', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_7.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_7.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_8 = DiagMessage(0xA928, 'UdsDiag_GetCommandSentToHydraulicValve_8', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_8.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_8.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetCommandSentToHydraulicValve_9 = DiagMessage(0xA929, 'UdsDiag_GetCommandSentToHydraulicValve_9', [1, 3, 4, 64], None, '', 2)
    UdsDiag_GetCommandSentToHydraulicValve_9.add_parameter(DiagParameter('Position', 1, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 100, '', False, False, False))
    UdsDiag_GetCommandSentToHydraulicValve_9.add_parameter(DiagParameter('Direction', 2, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NEUTRAL': [0, 0], 'PLUS': [1, 1], 'MINUS': [2, 2], 'FLOAT': [3, 3], 'ERROR': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetLoaderFunctionSelectorSwitchState = DiagMessage(0xA92A, 'UdsDiag_GetLoaderFunctionSelectorSwitchState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLoaderFunctionSelectorSwitchState.add_parameter(DiagParameter('LoaderFunctionSelectorSwitchState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetFaxRequestedPosition = DiagMessage(0xA92B, 'UdsDiag_GetFaxRequestedPosition', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFaxRequestedPosition.add_parameter(DiagParameter('FaxRequestedPosition', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))

    UdsDiag_GetRearLinkageHydraulicPriority = DiagMessage(0xA92C, 'UdsDiag_GetRearLinkageHydraulicPriority', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearLinkageHydraulicPriority.add_parameter(DiagParameter('RearLinkageHydraulicPriority', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))

    UdsDiag_GetLimitedEngineSpeedStatus = DiagMessage(0xA92D, 'UdsDiag_GetLimitedEngineSpeedStatus', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLimitedEngineSpeedStatus.add_parameter(DiagParameter('LimitedEngineSpeedStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetBrake_MainPressostat = DiagMessage(0xA965, 'UdsDiag_GetBrake_MainPressostat', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_MainPressostat.add_parameter(DiagParameter('Brake_MainPressostat', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 255, '', False, False, False))

    UdsDiag_GetBrake_LeftPedalPressure = DiagMessage(0xA966, 'UdsDiag_GetBrake_LeftPedalPressure', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_LeftPedalPressure.add_parameter(DiagParameter('Brake_LeftPedalPressure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'bar', 0, 255, '', False, False, False))

    UdsDiag_GetBrake_RightPedalPressure = DiagMessage(0xA967, 'UdsDiag_GetBrake_RightPedalPressure', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_RightPedalPressure.add_parameter(DiagParameter('Brake_RightPedalPressure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'bar', 0, 255, '', False, False, False))

    UdsDiag_GetBrake_StopLamp = DiagMessage(0xA968, 'UdsDiag_GetBrake_StopLamp', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_StopLamp.add_parameter(DiagParameter('Brake_StopLamp', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetTrailerBrake_TrailerDetection_SW = DiagMessage(0xA969, 'UdsDiag_GetTrailerBrake_TrailerDetection_SW', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetTrailerBrake_TrailerDetection_SW.add_parameter(DiagParameter('TrailerBrake_TrailerDetection_SW', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetParklock_State_Sensor = DiagMessage(0xA96A, 'UdsDiag_GetParklock_State_Sensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetParklock_State_Sensor.add_parameter(DiagParameter('Parklock_State_Sensor_Bar', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'bar', 0, 255, '', False, False, False))

    UdsDiag_GetTrailerBrake_ParkHandLever_ana = DiagMessage(0xA96B, 'UdsDiag_GetTrailerBrake_ParkHandLever_ana', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetTrailerBrake_ParkHandLever_ana.add_parameter(DiagParameter('TrailerBrake_ParkHandLever_ana', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 255, '', False, False, False))

    UdsDiag_GetParklock_Disengage_SOL = DiagMessage(0xA96C, 'UdsDiag_GetParklock_Disengage_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetParklock_Disengage_SOL.add_parameter(DiagParameter('Parklock_Disengage_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetHydTrailerBrake_Safety_EV_SOL = DiagMessage(0xA96D, 'UdsDiag_GetHydTrailerBrake_Safety_EV_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydTrailerBrake_Safety_EV_SOL.add_parameter(DiagParameter('HydTrailerBrake_Safety_EV_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetHydTrailerBrake_EV_SOL = DiagMessage(0xA96E, 'UdsDiag_GetHydTrailerBrake_EV_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydTrailerBrake_EV_SOL.add_parameter(DiagParameter('HydTrailerBrake_EV_SOL', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, '%', 0, 255, '', False, False, False))

    UdsDiag_GetParklock_ReversePressure_SOL = DiagMessage(0xA96F, 'UdsDiag_GetParklock_ReversePressure_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetParklock_ReversePressure_SOL.add_parameter(DiagParameter('Parklock_ReversePressure_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetHitch_FenderUpSw = DiagMessage(0xA985, 'UdsDiag_GetHitch_FenderUpSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_FenderUpSw.add_parameter(DiagParameter('Hitch_FenderUpSw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHitch_FenderDownSw = DiagMessage(0xA986, 'UdsDiag_GetHitch_FenderDownSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_FenderDownSw.add_parameter(DiagParameter('Hitch_FenderDownSw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetFrontHitch_Extend_ExternalSw = DiagMessage(0xA987, 'UdsDiag_GetFrontHitch_Extend_ExternalSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontHitch_Extend_ExternalSw.add_parameter(DiagParameter('FrontHitch_Extend_ExternalSw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetFrontHitch_Retract_ExternalSw = DiagMessage(0xA988, 'UdsDiag_GetFrontHitch_Retract_ExternalSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontHitch_Retract_ExternalSw.add_parameter(DiagParameter('FrontHitch_Retract_ExternalSw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHitch_LeftDraftSensor = DiagMessage(0xA989, 'UdsDiag_GetHitch_LeftDraftSensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_LeftDraftSensor.add_parameter(DiagParameter('Hitch_LeftDraftSensor_Degree', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))

    UdsDiag_GetHitch_RightDraftSensor = DiagMessage(0xA98A, 'UdsDiag_GetHitch_RightDraftSensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_RightDraftSensor.add_parameter(DiagParameter('Hitch_RightDraftSensor_Degree', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))

    UdsDiag_GetHitch_DualSensor = DiagMessage(0xA98B, 'UdsDiag_GetHitch_DualSensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_DualSensor.add_parameter(DiagParameter('Hitch_DualSensor', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'bar', 0, 255, '', False, False, False))

    UdsDiag_GetHitch_Depth_Sensor = DiagMessage(0xA98C, 'UdsDiag_GetHitch_Depth_Sensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Depth_Sensor.add_parameter(DiagParameter('Hitch_Depth_Sensor_Degree', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))

    UdsDiag_GetHitch_Radar_In = DiagMessage(0xA98D, 'UdsDiag_GetHitch_Radar_In', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Radar_In.add_parameter(DiagParameter('Hitch_Radar_In', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'km/h', 0, 255, '', False, False, False))

    UdsDiag_GetFrontHitch_SE_DE_Pressure_Sen = DiagMessage(0xA98E, 'UdsDiag_GetFrontHitch_SE_DE_Pressure_Sen', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontHitch_SE_DE_Pressure_Sen.add_parameter(DiagParameter('FrontHitch_SE_DE_Pressure_Sen', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'bar', 0, 255, '', False, False, False))

    UdsDiag_GetFrontHitch_PositionSensor = DiagMessage(0xA98F, 'UdsDiag_GetFrontHitch_PositionSensor', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontHitch_PositionSensor.add_parameter(DiagParameter('FrontHitch_PositionSensor_Degree', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '%', 0, 255, '', False, False, False))

    UdsDiag_GetLoader_Susp_SOL = DiagMessage(0xA990, 'UdsDiag_GetLoader_Susp_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLoader_Susp_SOL.add_parameter(DiagParameter('Loader_Susp_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetLoader_BucketLock_SOL = DiagMessage(0xA991, 'UdsDiag_GetLoader_BucketLock_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLoader_BucketLock_SOL.add_parameter(DiagParameter('Loader_BucketLock_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetCloggingFilterStatus = DiagMessage(0xA992, 'UdsDiag_GetCloggingFilterStatus', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetCloggingFilterStatus.add_parameter(DiagParameter('CloggingFilterStatus', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHydraulic_FrontExternalExtend_Sw = DiagMessage(0xA993, 'UdsDiag_GetHydraulic_FrontExternalExtend_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_FrontExternalExtend_Sw.add_parameter(DiagParameter('Hydraulic_FrontExternalExtend_Sw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHydraulic_FrontExternalRetract_Sw = DiagMessage(0xA994, 'UdsDiag_GetHydraulic_FrontExternalRetract_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_FrontExternalRetract_Sw.add_parameter(DiagParameter('Hydraulic_FrontExternalRetract_Sw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHydraulic_RearFenderExtend_Sw = DiagMessage(0xA995, 'UdsDiag_GetHydraulic_RearFenderExtend_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_RearFenderExtend_Sw.add_parameter(DiagParameter('Hydraulic_RearFenderExtend_Sw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHydraulic_RearFenderRetract_Sw = DiagMessage(0xA996, 'UdsDiag_GetHydraulic_RearFenderRetract_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_RearFenderRetract_Sw.add_parameter(DiagParameter('Hydraulic_RearFenderRetract_Sw_OnOff', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHydraulic_Auxilliary_Temp_ana = DiagMessage(0xA997, 'UdsDiag_GetHydraulic_Auxilliary_Temp_ana', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_Auxilliary_Temp_ana.add_parameter(DiagParameter('Hydraulic_Auxilliary_Temp_ana_Degree_C', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '?C', 0, 255, '', False, False, False))

    UdsDiag_GetHydraulic_Safety_SOL = DiagMessage(0xA998, 'UdsDiag_GetHydraulic_Safety_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_Safety_SOL.add_parameter(DiagParameter('Hydraulic_Safety_SOL', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))

    UdsDiag_GetHydraulic_H4_Command = DiagMessage(0xA999, 'UdsDiag_GetHydraulic_H4_Command', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_H4_Command.add_parameter(DiagParameter('Hydraulic_H4_Relay', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetHydraulic_H3_Command = DiagMessage(0xA99A, 'UdsDiag_GetHydraulic_H3_Command', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_H3_Command.add_parameter(DiagParameter('Hydraulic_H3_Relay', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetHydraulic_Safety_Ground_SOL = DiagMessage(0xA99B, 'UdsDiag_GetHydraulic_Safety_Ground_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHydraulic_Safety_Ground_SOL.add_parameter(DiagParameter('Hydraulic_Safety_Ground_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetDualPump_SOL = DiagMessage(0xA99C, 'UdsDiag_GetDualPump_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDualPump_SOL.add_parameter(DiagParameter('DualPump_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetLight_ReverseLamp = DiagMessage(0xA9B2, 'UdsDiag_GetLight_ReverseLamp', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_ReverseLamp.add_parameter(DiagParameter('Light_ReverseLamp', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetSteering_PressureSw = DiagMessage(0xA9BA, 'UdsDiag_GetSteering_PressureSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteering_PressureSw.add_parameter(DiagParameter('Steering_PressureSw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetSteering_WAS = DiagMessage(0xA9BB, 'UdsDiag_GetSteering_WAS', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteering_WAS.add_parameter(DiagParameter('Steering_WAS_Angle', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.INT, SignalConversion.STANDARD_LENGTH, 0, 1, 'deg', 0, 255, '', False, False, False))

    UdsDiag_GetSteering_SafetyValveSol = DiagMessage(0xA9BC, 'UdsDiag_GetSteering_SafetyValveSol', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteering_SafetyValveSol.add_parameter(DiagParameter('Steering_SafetyValveSolState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetSteering_ValvePowerSol = DiagMessage(0xA9BD, 'UdsDiag_GetSteering_ValvePowerSol', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetSteering_ValvePowerSol.add_parameter(DiagParameter('Steering_ValvePowerSolState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetDrive_Toc_b = DiagMessage(0xA9BE, 'UdsDiag_GetDrive_Toc_b', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_Toc_b.add_parameter(DiagParameter('Drive_Toc_b', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetDrive_BOC_NO_b = DiagMessage(0xA9BF, 'UdsDiag_GetDrive_BOC_NO_b', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_BOC_NO_b.add_parameter(DiagParameter('Drive_BOC_NO_b', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetDrive_FNR_Neutral_NC = DiagMessage(0xA9C0, 'UdsDiag_GetDrive_FNR_Neutral_NC', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_FNR_Neutral_NC.add_parameter(DiagParameter('Drive_FNR_Neutral_NC', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetDrive_FNR_Neutral_NO = DiagMessage(0xA9C1, 'UdsDiag_GetDrive_FNR_Neutral_NO', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_FNR_Neutral_NO.add_parameter(DiagParameter('Drive_FNR_Neutral_NO', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetDrive_OPS = DiagMessage(0xA9C2, 'UdsDiag_GetDrive_OPS', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_OPS.add_parameter(DiagParameter('Drive_OPS', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetDrive_FNR_Position = DiagMessage(0xA9C3, 'UdsDiag_GetDrive_FNR_Position', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_FNR_Position.add_parameter(DiagParameter('Drive_FNR_Position', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 255, '', False, False, False))

    UdsDiag_GetDrive_ClutchPedalPositionSen = DiagMessage(0xA9C4, 'UdsDiag_GetDrive_ClutchPedalPositionSen', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDrive_ClutchPedalPositionSen.add_parameter(DiagParameter('Drive_ClutchPedalPositionSen', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 255, '', False, False, False))

    UdsDiag_GetEngine_FootThrottle = DiagMessage(0xA9C5, 'UdsDiag_GetEngine_FootThrottle', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetEngine_FootThrottle.add_parameter(DiagParameter('Engine_FootThrottle', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 255, '', False, False, False))

    UdsDiag_GetBrake_HandLever_sw = DiagMessage(0xA9C6, 'UdsDiag_GetBrake_HandLever_sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_HandLever_sw.add_parameter(DiagParameter('Brake_HandLever_sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetImplementStatus_sw = DiagMessage(0xA9C7, 'UdsDiag_GetImplementStatus_sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetImplementStatus_sw.add_parameter(DiagParameter('ImplementStatus_sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetBrake_RightPedal_SEN_NF = DiagMessage(0xA9C8, 'UdsDiag_GetBrake_RightPedal_SEN_NF', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_RightPedal_SEN_NF.add_parameter(DiagParameter('Brake_RightPedal_SEN_NF', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetBrake_LeftPedal_SEN_NF = DiagMessage(0xA9C9, 'UdsDiag_GetBrake_LeftPedal_SEN_NF', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_LeftPedal_SEN_NF.add_parameter(DiagParameter('Brake_LeftPedal_SEN_NF', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetBrake_CouplingPedals = DiagMessage(0xA9CA, 'UdsDiag_GetBrake_CouplingPedals', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetBrake_CouplingPedals.add_parameter(DiagParameter('Brake_CouplingPedals', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetParklock_FNR_Sw = DiagMessage(0xA9CB, 'UdsDiag_GetParklock_FNR_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetParklock_FNR_Sw.add_parameter(DiagParameter('Parklock_FNR_Sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetRearPTO_FenderSw = DiagMessage(0xA9CC, 'UdsDiag_GetRearPTO_FenderSw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_FenderSw.add_parameter(DiagParameter('RearPTO_FenderSw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSED': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetRearPTO_OutputSpeed = DiagMessage(0xA9CD, 'UdsDiag_GetRearPTO_OutputSpeed', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_OutputSpeed.add_parameter(DiagParameter('RearPTO_OutputSpeed', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'Hz', 0, 255, '', False, False, False))

    UdsDiag_GetRearPTO_ClutchSpeed = DiagMessage(0xA9CE, 'UdsDiag_GetRearPTO_ClutchSpeed', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_ClutchSpeed.add_parameter(DiagParameter('RearPTO_ClutchSpeed', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 'Hz', 0, 255, '', False, False, False))

    UdsDiag_GetRearPTO_SOL = DiagMessage(0xA9CF, 'UdsDiag_GetRearPTO_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_SOL.add_parameter(DiagParameter('RearPTO_SOL', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 255, '', False, False, False))

    UdsDiag_GetFrontPTO_SOL = DiagMessage(0xA9D0, 'UdsDiag_GetFrontPTO_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontPTO_SOL.add_parameter(DiagParameter('FrontPTO_SOL', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 255, '', False, False, False))

    UdsDiag_GetRearPTO_ECO_SOL = DiagMessage(0xA9D1, 'UdsDiag_GetRearPTO_ECO_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_ECO_SOL.add_parameter(DiagParameter('RearPTO_ECO_SOL', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 255, '', False, False, False))

    UdsDiag_GetRearPTO_Std_SOL = DiagMessage(0xA9D2, 'UdsDiag_GetRearPTO_Std_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_Std_SOL.add_parameter(DiagParameter('RearPTO_Std_SOL', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 255, '', False, False, False))

    UdsDiag_GetRearPTO_540_SOL = DiagMessage(0xA9D3, 'UdsDiag_GetRearPTO_540_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_540_SOL.add_parameter(DiagParameter('RearPTO_540_SOL', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 255, '', False, False, False))

    UdsDiag_GetRearPTO_1000_SOL = DiagMessage(0xA9D4, 'UdsDiag_GetRearPTO_1000_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_1000_SOL.add_parameter(DiagParameter('RearPTO_1000_SOL', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 255, '', False, False, False))

    UdsDiag_GetFrontPTO_Gnd_SOL = DiagMessage(0xA9D5, 'UdsDiag_GetFrontPTO_Gnd_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFrontPTO_Gnd_SOL.add_parameter(DiagParameter('FrontPTO_Gnd_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetRearPTO_Gnd_SOL = DiagMessage(0xA9D6, 'UdsDiag_GetRearPTO_Gnd_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetRearPTO_Gnd_SOL.add_parameter(DiagParameter('RearPTO_Gnd_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetDifflock_SOL = DiagMessage(0xA9D7, 'UdsDiag_GetDifflock_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDifflock_SOL.add_parameter(DiagParameter('Difflock_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetDifflock_Gnd_SOL = DiagMessage(0xA9D8, 'UdsDiag_GetDifflock_Gnd_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetDifflock_Gnd_SOL.add_parameter(DiagParameter('Difflock_Gnd_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetVisco_ClimCompressorState = DiagMessage(0xA9D9, 'UdsDiag_GetVisco_ClimCompressorState', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetVisco_ClimCompressorState.add_parameter(DiagParameter('Visco_ClimCompressorState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetExternalMiror_Defrost = DiagMessage(0xA9DF, 'UdsDiag_GetExternalMiror_Defrost', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetExternalMiror_Defrost.add_parameter(DiagParameter('ExternalMiror_Defrost', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetInCabSocket_PowerSupply_relay = DiagMessage(0xA9E0, 'UdsDiag_GetInCabSocket_PowerSupply_relay', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetInCabSocket_PowerSupply_relay.add_parameter(DiagParameter('InCabSocket_PowerSupply_relay', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetISO_Power_relay = DiagMessage(0xA9E1, 'UdsDiag_GetISO_Power_relay', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO_Power_relay.add_parameter(DiagParameter('ISO_Power_relay', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetISO_ECU_Power_relay = DiagMessage(0xA9E2, 'UdsDiag_GetISO_ECU_Power_relay', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO_ECU_Power_relay.add_parameter(DiagParameter('ISO_ECU_Power_relay', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

    UdsDiag_GetFNR_DriveISC_EV_Shunt = DiagMessage(0xA9E3, 'UdsDiag_GetFNR_DriveISC_EV_Shunt', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetFNR_DriveISC_EV_Shunt.add_parameter(DiagParameter('FNR_DriveISC_EV_Shunt', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2]}, 0, 2, '', False, False, False))

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
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'INVALID': [48, 48], 'FELLA': [65, 65], 'CHALLENGER': [67, 67], 'FENDT': [70, 70], 'LAVERDA': [76, 76], 'MASSEY_FERGUSON': [77, 77], 'VALTRA': [86, 86], 'LELY': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class SRCM_BVWriteDataSignals:
    MaintenanceNextServiceHours = DiagMessage(0x1330, 'MaintenanceNextServiceHours', [2, 3, 4, 64], None, '', 1)
    MaintenanceNextServiceHours.add_parameter(DiagParameter('MaintenanceNSHs', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 4294967295, 'Next Maintenance Service Hours', False, False, False))

    TractorHoursOffset = DiagMessage(0x1331, 'TractorHoursOffset', [2, 3, 4, 64], None, '', 1)
    TractorHoursOffset.add_parameter(DiagParameter('TractorHoursOffset', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', -2147483646, 2147483646, 'Tractor Hours Offset 0.1h', False, False, False))

    CurrentTractorWheelSize = DiagMessage(0x1332, 'CurrentTractorWheelSize', [2, 3, 64], None, '', 1)
    CurrentTractorWheelSize.add_parameter(DiagParameter('CurrentTractorWhlSze', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 3000, 7500, 'Current Tractor WheelSize in mm', False, False, False))

    TractorWheelMaxSize = DiagMessage(0x1333, 'TractorWheelMaxSize', [2, 3, 4, 64], None, '', 1)
    TractorWheelMaxSize.add_parameter(DiagParameter('TractorWlMxSze', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'mm', 3000, 7500, 'Tractor Wheel Max Size in mm', False, False, False))

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

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [2, 3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'INVALID': [48, 48], 'FELLA': [65, 65], 'CHALLENGER': [67, 67], 'FENDT': [70, 70], 'LAVERDA': [76, 76], 'MASSEY_FERGUSON': [77, 77], 'VALTRA': [86, 86], 'LELY': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class SRCM_BVIOControlDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [4], [4], '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))


SRCM_BVDTCSnapshotdDids = {
}

class SRCMClient(ECUClient):
    class FlashData(Enum):
        BOOT= [MemoryLocation(0x80040000, 0x0, 32, 32, erase_address=0x80040000, erase_size=None,
                               path_to_file="^DGW_[.]__MOD_[.]F[.][0-9a-fA-F]{2}[.][0-9a-fA-F]{3}[.][0-9a-fA-F]{2}[.].{6}[.](HEX|hex)$",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(SRCM_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(SRCM_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False)]

        APPL = [MemoryLocation(0x80040000, 0x0, 32, 32, erase_address=0x80040000, erase_size=None,
                               path_to_file="^DGW_[.]__MOD_[.]F[.][0-9a-fA-F]{2}[.][0-9a-fA-F]{3}[.][0-9a-fA-F]{2}[.].{6}[.](HEX|hex)$",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(SRCM_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(SRCM_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False),

                MemoryLocation(0x80820000, 0x0, 32, 32, erase_address=0x80820000, erase_size=None,
                               path_to_file="^DGW_[.]__MOD_[.]F[.][0-9a-fA-F]{2}[.][0-9a-fA-F]{3}[.][0-9a-fA-F]{2}[.].{6}[.](HEX|hex)$",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(SRCM_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(SRCM_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0x31, "SRCM", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=6, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = SRCM_BVReadDataSignals
        self.write_dids = SRCM_BVWriteDataSignals
        self.routine_dids = SRCM_BVRoutineIdentifierSignals
        self.io_dids = SRCM_BVIOControlDataSignals
        self.dtc_snapshot_dids = SRCM_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

