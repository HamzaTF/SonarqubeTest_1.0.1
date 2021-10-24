from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class A5_SUSP_Valtra_BVRoutineIdentifierSignals:
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

    RequestCalibResult_CabSusp = DiagMessage(0x1201, 'RequestCalibResult_CabSusp', [3, 64], [1, 4, 5], '', 0)

    RequestCalibResult_CabSusp_Response = DiagMessage(0x1201, 'RequestCalibResult_CabSusp_Response', [1, 2, 3, 4, 64, 65], None, '', 1)
    RequestCalibResult_CabSusp_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StartCalib_CabSusp = DiagMessage(0x1201, 'StartCalib_CabSusp', [3, 64], [1, 4, 5], '', 2)
    StartCalib_CabSusp.add_parameter(DiagParameter('Command', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Start calibration': [0, 0], 'Start next step': [1, 1]}, 0, 1, '', False, False, False))
    StartCalib_CabSusp.add_parameter(DiagParameter('Monitoring_Type', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Value monitoring off': [0, 0], 'Value monitoring on (ACHT result)': [1, 1], 'Progress monitoring on': [2, 2]}, 0, 2, '', False, False, False))

    StartCalib_CabSusp_Response = DiagMessage(0x1201, 'StartCalib_CabSusp_Response', [1, 2, 3, 4, 64, 65], None, '', 1)
    StartCalib_CabSusp_Response.add_parameter(DiagParameter('ResultState_Structure', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPERATION_OK': [0, 0], 'CALIBRATION_ERROR': [2, 2], 'CALIBRATION_STEP_NOT_READY': [3, 3], 'CALIBRATION_STEP_FINISHED': [4, 4], 'CALIBRATION_STEP_NOT_AVAILABLE': [5, 5], 'CALIBRATION_NOT_ALLOWED': [6, 6], 'CALIBRATION_SEQUENCE_ERROR': [7, 7], 'CALIBRATION_NOT_RUN': [8, 8], 'TIMEOUT': [9, 9], 'MEMORY_SAVING_ERROR': [10, 10]}, 0, 10, '', False, False, False))

    StopCalib_CabSusp = DiagMessage(0x1201, 'StopCalib_CabSusp', [3, 64], [1, 4, 5], '', 1)
    StopCalib_CabSusp.add_parameter(DiagParameter('RoutineControlOptionRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Fixed data value': [65535, 65535]}, 65535, 65535, '', False, False, False))

    StopCalib_CabSusp_Response = DiagMessage(0x1201, 'StopCalib_CabSusp_Response', [1, 2, 3, 4, 64, 65], None, '', 2)
    StopCalib_CabSusp_Response.add_parameter(DiagParameter('ResultState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Operation OK': [0, 0]}, 0, 0, '', False, False, False))
    StopCalib_CabSusp_Response.add_parameter(DiagParameter('NotUsed', 2, 1, 0, 32, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'NotUsed': [4294967295, 4294967295]}, 4294967295, 4294967295, '', False, False, False))

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


class A5_SUSP_Valtra_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    CABSUSP_SettingValue = DiagMessage(0x1101, 'CABSUSP_SettingValue', [1, 3, 4, 64], None, '', 1)
    CABSUSP_SettingValue.add_parameter(DiagParameter('CABSUSP_SettingValue', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Mode_Auto': [0, 0], 'Mode_Off': [1, 1], 'Mode_HighPosition': [2, 2], 'Mode_Calibration': [3, 3], 'Mode Fix': [4, 4]}, 0, 4, '', False, False, False))

    CABSUSP_ControlStatus = DiagMessage(0x1102, 'CABSUSP_ControlStatus', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ControlStatus.add_parameter(DiagParameter('CABSUSP_ControlStatus', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Mode_Auto': [0, 0], 'Mode_Off': [1, 1], 'Mode_HighPosition': [2, 2], 'Mode_Calibration': [3, 3], 'Mode Fix': [4, 4]}, 0, 4, '', False, False, False))

    FAXLESUSP_ControlStatus = DiagMessage(0x1103, 'FAXLESUSP_ControlStatus', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_ControlStatus.add_parameter(DiagParameter('FAXLESUSP_ControlStatus', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Mode_Block': [0, 0], 'Mode_Auto': [1, 1], 'Mode_Calibration': [2, 2], 'Mode_Off': [3, 3], 'Mode_Overload': [4, 4], 'Mode_Regulation': [5, 5], 'Mode_Manual (Only MF)': [6, 6]}, 0, 6, '', False, False, False))

    FAXLESUSP_Position = DiagMessage(0x1104, 'FAXLESUSP_Position', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_Position.add_parameter(DiagParameter('FAXLESUSP_Position', 1, 0, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    HW_AUTO5_APP18_125_LifeCycle = DiagMessage(0x1105, 'HW_AUTO5_APP18_125_LifeCycle', [1, 3, 4, 64], None, '', 1)
    HW_AUTO5_APP18_125_LifeCycle.add_parameter(DiagParameter('HW_AUTO5_APP18_125_LifeCycle', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Power Off': [0, 0], 'Starting': [1, 1], 'Active': [2, 2], 'Active-Sleep': [3, 3], 'Sleep': [4, 4]}, 0, 4, '', False, False, False))

    HW_AUTO5_APP18_125_SoftwareVers = DiagMessage(0x1106, 'HW_AUTO5_APP18_125_SoftwareVers', [1, 3, 4, 64], None, '', 1)
    HW_AUTO5_APP18_125_SoftwareVers.add_parameter(DiagParameter('HW_AUTO5_APP18_125_SoftwareVers', 1, 0, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    CABSUSP_PositionFrontLeft = DiagMessage(0x1107, 'CABSUSP_PositionFrontLeft', [1, 3, 4, 64], None, '', 1)
    CABSUSP_PositionFrontLeft.add_parameter(DiagParameter('CABSUSP_PositionFrontLeft', 1, 0, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    CABSUSP_PositionFrontRight = DiagMessage(0x1108, 'CABSUSP_PositionFrontRight', [1, 3, 4, 64], None, '', 1)
    CABSUSP_PositionFrontRight.add_parameter(DiagParameter('CABSUSP_PositionFrontRight', 1, 0, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    CABSUP_PositionRearLeft = DiagMessage(0x1109, 'CABSUP_PositionRearLeft', [1, 3, 4, 64], None, '', 1)
    CABSUP_PositionRearLeft.add_parameter(DiagParameter('CABSUP_PositionRearLeft', 1, 0, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    CABSUP_PositionRearRight = DiagMessage(0x110A, 'CABSUP_PositionRearRight', [1, 3, 4, 64], None, '', 1)
    CABSUP_PositionRearRight.add_parameter(DiagParameter('CABSUP_PositionRearRight', 1, 0, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    CABSUSP_ERR_15_77 = DiagMessage(0x110B, 'CABSUSP_ERR_15_77', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_77.add_parameter(DiagParameter('CABSUSP_ERR_15_77', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_78 = DiagMessage(0x110C, 'CABSUSP_ERR_15_78', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_78.add_parameter(DiagParameter('CABSUSP_ERR_15_78', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_79 = DiagMessage(0x110D, 'CABSUSP_ERR_15_79', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_79.add_parameter(DiagParameter('CABSUSP_ERR_15_79', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_7A = DiagMessage(0x110E, 'CABSUSP_ERR_15_7A', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_7A.add_parameter(DiagParameter('CABSUSP_ERR_15_7A', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_7B = DiagMessage(0x110F, 'CABSUSP_ERR_15_7B', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_7B.add_parameter(DiagParameter('CABSUSP_ERR_15_7B', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_7C = DiagMessage(0x1110, 'CABSUSP_ERR_15_7C', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_7C.add_parameter(DiagParameter('CABSUSP_ERR_15_7C', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_7D = DiagMessage(0x1111, 'CABSUSP_ERR_15_7D', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_7D.add_parameter(DiagParameter('CABSUSP_ERR_15_7D', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_7E = DiagMessage(0x1112, 'CABSUSP_ERR_15_7E', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_7E.add_parameter(DiagParameter('CABSUSP_ERR_15_7E', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_7F = DiagMessage(0x1113, 'CABSUSP_ERR_15_7F', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_7F.add_parameter(DiagParameter('CABSUSP_ERR_15_7F', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_8C = DiagMessage(0x1114, 'CABSUSP_ERR_15_8C', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_8C.add_parameter(DiagParameter('CABSUSP_ERR_15_8C', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_8D = DiagMessage(0x1115, 'CABSUSP_ERR_15_8D', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_8D.add_parameter(DiagParameter('CABSUSP_ERR_15_8D', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_8E = DiagMessage(0x1116, 'CABSUSP_ERR_15_8E', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_8E.add_parameter(DiagParameter('CABSUSP_ERR_15_8E', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    CABSUSP_ERR_15_8F = DiagMessage(0x1117, 'CABSUSP_ERR_15_8F', [1, 3, 4, 64], None, '', 1)
    CABSUSP_ERR_15_8F.add_parameter(DiagParameter('CABSUSP_ERR_15_8F', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    FAXLESUSP_ERR_11_81 = DiagMessage(0x1118, 'FAXLESUSP_ERR_11_81', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_ERR_11_81.add_parameter(DiagParameter('FAXLESUSP_ERR_11_81', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    FAXLESUSP_ERR_11_82 = DiagMessage(0x1119, 'FAXLESUSP_ERR_11_82', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_ERR_11_82.add_parameter(DiagParameter('FAXLESUSP_ERR_11_82', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    FAXLESUSP_ERR_11_83 = DiagMessage(0x111A, 'FAXLESUSP_ERR_11_83', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_ERR_11_83.add_parameter(DiagParameter('FAXLESUSP_ERR_11_83', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    FAXLESUSP_ERR_11_84 = DiagMessage(0x111B, 'FAXLESUSP_ERR_11_84', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_ERR_11_84.add_parameter(DiagParameter('FAXLESUSP_ERR_11_84', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    FAXLESUSP_ERR_11_85 = DiagMessage(0x111C, 'FAXLESUSP_ERR_11_85', [1, 3, 4, 64], None, '', 1)
    FAXLESUSP_ERR_11_85.add_parameter(DiagParameter('FAXLESUSP_ERR_11_85', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'No error': [0, 0], 'Error active': [1, 1], 'Not used': [2, 2], 'Not usedx1': [3, 3]}, 0, 3, '', False, False, False))

    FrontAxleCalibrationState = DiagMessage(0x111D, 'FrontAxleCalibrationState', [1, 3, 4, 64], None, '', 1)
    FrontAxleCalibrationState.add_parameter(DiagParameter('FrontAxleCalibrationState', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Calibration NOK': [0, 0], 'Calibration OK': [1, 1], 'Calibration not available': [5, 5]}, 0, 5, '', False, False, False))

    CabSuspCalibrationState = DiagMessage(0x111E, 'CabSuspCalibrationState', [1, 3, 4, 64], None, '', 1)
    CabSuspCalibrationState.add_parameter(DiagParameter('CabSuspCalibrationState', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Calibration NOK': [0, 0], 'Calibration OK': [1, 1], 'Calibration not available': [5, 5]}, 0, 5, '', False, False, False))

    DigitalInput1 = DiagMessage(0xA800, 'DigitalInput1', [1, 3, 4, 64], None, '', 6)
    DigitalInput1.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput1.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput1.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput1.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput1.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput1.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput2 = DiagMessage(0xA801, 'DigitalInput2', [1, 3, 4, 64], None, '', 6)
    DigitalInput2.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput2.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput2.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput2.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput2.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput2.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput3 = DiagMessage(0xA802, 'DigitalInput3', [1, 3, 4, 64], None, '', 6)
    DigitalInput3.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput3.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput3.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput3.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput3.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput3.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput4 = DiagMessage(0xA803, 'DigitalInput4', [1, 3, 4, 64], None, '', 6)
    DigitalInput4.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput4.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput4.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput4.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput4.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput4.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput5 = DiagMessage(0xA804, 'DigitalInput5', [1, 3, 4, 64], None, '', 6)
    DigitalInput5.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput5.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput5.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Selected Input Not Active': [0, 0], 'Selected Input Active': [1, 1]}, 0, 1, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput5.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput5.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput5.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput6 = DiagMessage(0xA805, 'DigitalInput6', [1, 3, 4, 64], None, '', 6)
    DigitalInput6.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput6.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput6.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput6.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput6.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput6.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput7 = DiagMessage(0xA806, 'DigitalInput7', [1, 3, 4, 64], None, '', 6)
    DigitalInput7.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput7.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput7.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput7.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput7.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput7.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput8 = DiagMessage(0xA807, 'DigitalInput8', [1, 3, 4, 64], None, '', 6)
    DigitalInput8.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput8.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput8.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput8.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput8.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput8.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput9 = DiagMessage(0xA808, 'DigitalInput9', [1, 3, 4, 64], None, '', 6)
    DigitalInput9.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput9.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput9.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput9.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput9.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput9.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput10 = DiagMessage(0xA809, 'DigitalInput10', [1, 3, 4, 64], None, '', 6)
    DigitalInput10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput10.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput10.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput10.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput10.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput10.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput11 = DiagMessage(0xA80A, 'DigitalInput11', [1, 3, 4, 64], None, '', 6)
    DigitalInput11.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput11.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput11.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput11.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput11.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput11.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput12 = DiagMessage(0xA80B, 'DigitalInput12', [1, 3, 4, 64], None, '', 6)
    DigitalInput12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput12.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput12.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput12.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput12.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput12.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput13 = DiagMessage(0xA80C, 'DigitalInput13', [1, 3, 4, 64], None, '', 6)
    DigitalInput13.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput13.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput13.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput13.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput13.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput13.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput14 = DiagMessage(0xA80D, 'DigitalInput14', [1, 3, 4, 64], None, '', 6)
    DigitalInput14.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput14.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput14.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput14.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput14.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput14.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalInput15 = DiagMessage(0xA80E, 'DigitalInput15', [1, 3, 4, 64], None, '', 6)
    DigitalInput15.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInput15.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInput15.add_parameter(DiagParameter('InputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected Input Not Active, 1=Selected InputActive', False, False, False))
    DigitalInput15.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    DigitalInput15.add_parameter(DiagParameter('InputVoltage', 5, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    DigitalInput15.add_parameter(DiagParameter('AnalogToDigitalConversion', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalOutput1 = DiagMessage(0xA828, 'DigitalOutput1', [1, 3, 4, 64], None, '', 4)
    DigitalOutput1.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutput1.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutput1.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    DigitalOutput1.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalOutput2 = DiagMessage(0xA829, 'DigitalOutput2', [1, 3, 4, 64], None, '', 4)
    DigitalOutput2.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutput2.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutput2.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    DigitalOutput2.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalOutput3 = DiagMessage(0xA82A, 'DigitalOutput3', [1, 3, 4, 64], None, '', 4)
    DigitalOutput3.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutput3.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutput3.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    DigitalOutput3.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalOutput4 = DiagMessage(0xA82B, 'DigitalOutput4', [1, 3, 4, 64], None, '', 4)
    DigitalOutput4.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutput4.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutput4.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    DigitalOutput4.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalOutput5 = DiagMessage(0xA82C, 'DigitalOutput5', [1, 3, 4, 64], None, '', 4)
    DigitalOutput5.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutput5.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutput5.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    DigitalOutput5.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalOutput6 = DiagMessage(0xA82D, 'DigitalOutput6', [1, 3, 4, 64], None, '', 4)
    DigitalOutput6.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutput6.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutput6.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    DigitalOutput6.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalOutput7 = DiagMessage(0xA82E, 'DigitalOutput7', [1, 3, 4, 64], None, '', 4)
    DigitalOutput7.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutput7.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutput7.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    DigitalOutput7.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalOutput8 = DiagMessage(0xA82F, 'DigitalOutput8', [1, 3, 4, 64], None, '', 4)
    DigitalOutput8.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutput8.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutput8.add_parameter(DiagParameter('OutputActive', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '0=Selected OUTput Not Active, 1=Selected OUTputActive', False, False, False))
    DigitalOutput8.add_parameter(DiagParameter('DiagData', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    AnalogInput1 = DiagMessage(0xA850, 'AnalogInput1', [1, 3, 4, 64], None, '', 5)
    AnalogInput1.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput1.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput1.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput1.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput1.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput2 = DiagMessage(0xA851, 'AnalogInput2', [1, 3, 4, 64], None, '', 5)
    AnalogInput2.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput2.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput2.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput2.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput2.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput3 = DiagMessage(0xA852, 'AnalogInput3', [1, 3, 4, 64], None, '', 5)
    AnalogInput3.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput3.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput3.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput3.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput3.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput4 = DiagMessage(0xA853, 'AnalogInput4', [1, 3, 4, 64], None, '', 5)
    AnalogInput4.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput4.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput4.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput4.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput4.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput5 = DiagMessage(0xA854, 'AnalogInput5', [1, 3, 4, 64], None, '', 5)
    AnalogInput5.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput5.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput5.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput5.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput5.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput6 = DiagMessage(0xA855, 'AnalogInput6', [1, 3, 4, 64], None, '', 5)
    AnalogInput6.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput6.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput6.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput6.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput6.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput7 = DiagMessage(0xA856, 'AnalogInput7', [1, 3, 4, 64], None, '', 5)
    AnalogInput7.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput7.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput7.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput7.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput7.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput8 = DiagMessage(0xA857, 'AnalogInput8', [1, 3, 4, 64], None, '', 5)
    AnalogInput8.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput8.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput8.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput8.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput8.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput9 = DiagMessage(0xA858, 'AnalogInput9', [1, 3, 4, 64], None, '', 5)
    AnalogInput9.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput9.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput9.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput9.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput9.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput10 = DiagMessage(0xA859, 'AnalogInput10', [1, 3, 4, 64], None, '', 5)
    AnalogInput10.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput10.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput10.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput10.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput10.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput11 = DiagMessage(0xA85A, 'AnalogInput11', [1, 3, 4, 64], None, '', 5)
    AnalogInput11.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput11.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput11.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput11.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput11.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    AnalogInput12 = DiagMessage(0xA85B, 'AnalogInput12', [1, 3, 4, 64], None, '', 5)
    AnalogInput12.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    AnalogInput12.add_parameter(DiagParameter('TotalNOfAI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    AnalogInput12.add_parameter(DiagParameter('DiagData', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    AnalogInput12.add_parameter(DiagParameter('InputVoltage', 4, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))
    AnalogInput12.add_parameter(DiagParameter('AnalogToDigitalConversion', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    FrequencyInput1 = DiagMessage(0xA8A0, 'FrequencyInput1', [1, 3, 4, 64], None, '', 6)
    FrequencyInput1.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    FrequencyInput1.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FrequencyInput1.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'Hz', 0, 255, '', False, False, False))
    FrequencyInput1.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FrequencyInput1.add_parameter(DiagParameter('DiagData', 5, 3, 2, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    FrequencyInput1.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))

    FrequencyInput2 = DiagMessage(0xA8A1, 'FrequencyInput2', [1, 3, 4, 64], None, '', 6)
    FrequencyInput2.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    FrequencyInput2.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FrequencyInput2.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'Hz', 0, 255, '', False, False, False))
    FrequencyInput2.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FrequencyInput2.add_parameter(DiagParameter('DiagData', 5, 3, 2, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    FrequencyInput2.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))

    FrequencyInput3 = DiagMessage(0xA8A2, 'FrequencyInput3', [1, 3, 4, 64], None, '', 6)
    FrequencyInput3.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    FrequencyInput3.add_parameter(DiagParameter('TotalNOfFI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FrequencyInput3.add_parameter(DiagParameter('Frequency', 3, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'Hz', 0, 255, '', False, False, False))
    FrequencyInput3.add_parameter(DiagParameter('Rotation', 4, 3, 0, 2, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    FrequencyInput3.add_parameter(DiagParameter('DiagData', 5, 3, 2, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))
    FrequencyInput3.add_parameter(DiagParameter('AnalogInputVoltage', 6, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mV', 0, 255, '', False, False, False))

    PWMOutput1 = DiagMessage(0xA8C8, 'PWMOutput1', [1, 3, 4, 64], None, '', 5)
    PWMOutput1.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PWMOutput1.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PWMOutput1.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '', False, False, False))
    PWMOutput1.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mA', 0, 255, '', False, False, False))
    PWMOutput1.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PWMOutput2 = DiagMessage(0xA8C9, 'PWMOutput2', [1, 3, 4, 64], None, '', 5)
    PWMOutput2.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PWMOutput2.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PWMOutput2.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '', False, False, False))
    PWMOutput2.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mA', 0, 255, '', False, False, False))
    PWMOutput2.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PWMOutput3 = DiagMessage(0xA8CA, 'PWMOutput3', [1, 3, 4, 64], None, '', 5)
    PWMOutput3.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PWMOutput3.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PWMOutput3.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '', False, False, False))
    PWMOutput3.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mA', 0, 255, '', False, False, False))
    PWMOutput3.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PWMOutput4 = DiagMessage(0xA8CB, 'PWMOutput4', [1, 3, 4, 64], None, '', 5)
    PWMOutput4.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PWMOutput4.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PWMOutput4.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '', False, False, False))
    PWMOutput4.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mA', 0, 255, '', False, False, False))
    PWMOutput4.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PWMOutput5 = DiagMessage(0xA8CC, 'PWMOutput5', [1, 3, 4, 64], None, '', 5)
    PWMOutput5.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PWMOutput5.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PWMOutput5.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '', False, False, False))
    PWMOutput5.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mA', 0, 255, '', False, False, False))
    PWMOutput5.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    PWMOutput6 = DiagMessage(0xA8CD, 'PWMOutput6', [1, 3, 4, 64], None, '', 5)
    PWMOutput6.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    PWMOutput6.add_parameter(DiagParameter('TotalNOfPWMO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    PWMOutput6.add_parameter(DiagParameter('PWMPuisse', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '', False, False, False))
    PWMOutput6.add_parameter(DiagParameter('PWMOutputCurrent', 4, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'mA', 0, 255, '', False, False, False))
    PWMOutput6.add_parameter(DiagParameter('DiagData', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OK': [0, 0], 'Open,there seems to be nothin outiside this IO': [1, 1], 'Short circuit to ground level': [2, 2], 'Short circuit to high voltage level': [4, 4]}, 0, 4, '', False, False, False))

    DigitalInputs = DiagMessage(0xA8F1, 'DigitalInputs', [1, 3, 4, 64], None, '', 7)
    DigitalInputs.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Input Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=input not available', False, False, False))
    DigitalInputs.add_parameter(DiagParameter('TotalNOfDI', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInputs.add_parameter(DiagParameter('DigitalInputs1_8', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInputs.add_parameter(DiagParameter('DigitalInputs9_16', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInputs.add_parameter(DiagParameter('DigitalInputs17_24', 5, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInputs.add_parameter(DiagParameter('DigitalInputs25_32', 6, 4, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalInputs.add_parameter(DiagParameter('DigitalInputs33_40', 7, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    DigitalOutputs = DiagMessage(0xA8F2, 'DigitalOutputs', [1, 3, 4, 64], None, '', 7)
    DigitalOutputs.add_parameter(DiagParameter('Answerstatus', 1, 0, 0, 2, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Read Fail': [0, 0], 'Read Success': [1, 1], 'Output Not Available': [3, 3]}, 0, 3, '0=Read fail,1=Read success,3=OUTput not available', False, False, False))
    DigitalOutputs.add_parameter(DiagParameter('TotalNOfDO', 2, 0, 2, 6, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutputs.add_parameter(DiagParameter('DigitalOutputs1_8', 3, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutputs.add_parameter(DiagParameter('DigitalOutputs9_16', 4, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutputs.add_parameter(DiagParameter('DigitalOutputs17_24', 5, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutputs.add_parameter(DiagParameter('DigitalOutputs25_32', 6, 4, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    DigitalOutputs.add_parameter(DiagParameter('DigitalOutputs33_40', 7, 5, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

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


class A5_SUSP_Valtra_BVWriteDataSignals:
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


class A5_SUSP_Valtra_BVIOControlDataSignals:
    pass


A5_SUSP_Valtra_BVDTCSnapshotdDids = {
}


class A5_SUSP_ValtraClient(ECUClient):
    class FlashData(Enum):
        pass

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xD0, "A5_SUSP_Valtra", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A5_SUSP_Valtra_BVReadDataSignals
        self.write_dids = A5_SUSP_Valtra_BVWriteDataSignals
        self.routine_dids = A5_SUSP_Valtra_BVRoutineIdentifierSignals
        self.io_dids = A5_SUSP_Valtra_BVIOControlDataSignals
        self.dtc_snapshot_dids = A5_SUSP_Valtra_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

