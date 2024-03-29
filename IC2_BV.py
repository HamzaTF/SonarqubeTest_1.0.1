from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class IC2_BVRoutineIdentifierSignals:
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

    TFTCheckerboardResultRequest = DiagMessage(0x1200, 'TFTCheckerboardResultRequest', [], None, '', 0)

    TFTCheckerboardStartRequest = DiagMessage(0x1200, 'TFTCheckerboardStartRequest', [], None, '', 1)
    TFTCheckerboardStartRequest.add_parameter(DiagParameter('TFTScreenType', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Nothing': [0, 0], 'Checkerboard': [1, 1], 'Red': [2, 2], 'Green': [3, 3], 'Blue': [4, 4]}, 0, 4, '0: Nothing; 1: Checkerboard; 2: Red; 3: Green; 4: Blue', False, False, False))

    TFTCheckerboardStartResponse = DiagMessage(0x1200, 'TFTCheckerboardStartResponse', [1, 2, 3, 4, 64, 65], None, '', 0)

    TFTCheckerboardStopRequest = DiagMessage(0x1200, 'TFTCheckerboardStopRequest', [], None, '', 0)

    TFTCheckerboardStopResponse = DiagMessage(0x1200, 'TFTCheckerboardStopResponse', [1, 2, 3, 4, 64, 65], None, '', 0)

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


class IC2_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    DigitalInputRead = DiagMessage(0x1100, 'DigitalInputRead', [1, 3, 4, 64], None, '', 14)
    DigitalInputRead.add_parameter(DiagParameter('Battery', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('LightMarker', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2_19-M2_21-H2_22][Light][K2][18-DI_01][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][2_0_0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('RoadStatus', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2_19-M2_21][Light][X258][10-DI_02][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][2_0_0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('HighBeamStatus', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2_19-M2_21-H2_22][Light][X1050][1-DI_03][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][2_0_0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('LeftTurnStatus', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2_19-M2_21-H2_22][Light][X652][27-DI_04][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][2_0_0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('RightTurnStatus', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2_19-M2_21-H2_22][Light][X652][19-DI_05][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][2_0_0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('Blinker1Status', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2_19-M2_21][Light][X652][11-DI_06][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][2_0_0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('Blinker2Status', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2_19-M2_21-H2_22][Light][X652][2-DI_07][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][2_0_0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('BrakeHandLever', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('Dig13IGN', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2_19-M2_21-H2_22][Miscellaneous][ ][25-IGN_KL115][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][0_0_0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('ButtonOk', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2][Cab_commands][X57][20-DI_10][ ][ ][raw][DASHBOARD][Y][0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('ButtonEsc', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][M2][Cab_commands][X57][12-DI_11][ ][ ][raw][DASHBOARD][Y][0]', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('InDig18', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '', False, False, False))
    DigitalInputRead.add_parameter(DiagParameter('InDig19', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '', False, False, False))

    DigitalOutputRead = DiagMessage(0x1102, 'DigitalOutputRead', [1, 3, 4, 64], None, '', 3)
    DigitalOutputRead.add_parameter(DiagParameter('BuzzerPwm', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 255, '[1][M2_19-M2_21-H2_22][Miscellaneous][X73][8-DI_1][AMT-DCT-CVT][0_0_0][raw][DASHBOARD][Y_N_N][2_0_0]', False, False, False))
    DigitalOutputRead.add_parameter(DiagParameter('SUP_ANA_00', 2, 1, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '[1][M2_19-H2_22][Cab_commands][X57][6][AMT-DCT][L-M-H][raw][DASHBOARD][Y_N_N][0_0_0]', False, False, False))
    DigitalOutputRead.add_parameter(DiagParameter('Reserved', 3, 1, 1, 7, SignalByteOrder.Intel, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 127, '', False, False, False))

    AnalogInputRead = DiagMessage(0x1103, 'AnalogInputRead', [1, 3, 4, 64], None, '', 6)
    AnalogInputRead.add_parameter(DiagParameter('ANA_R_01', 1, 0, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'ohm', 0, 65535, '', False, False, False))
    AnalogInputRead.add_parameter(DiagParameter('ANA_R_02', 2, 2, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'ohm', 0, 65535, '', False, False, False))
    AnalogInputRead.add_parameter(DiagParameter('ANA_R_03', 3, 4, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'ohm', 0, 65535, '[1][M2_19-M2_21-H2_22][Auxiliary_hydraulic][X24][32(Dig_res_2][AMT-DCT-CVT][L-M-H][raw][DASHBOARD][Y_N_N][0_0_0]', False, False, False))
    AnalogInputRead.add_parameter(DiagParameter('ANA_R_04', 4, 6, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'ohm', 0, 65535, '', False, False, False))
    AnalogInputRead.add_parameter(DiagParameter('ANA_R_05', 5, 8, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'ohm', 0, 65535, '[1][M2_19-M2_21-H2_22][Cab_commands][X24][32_Dig_Res_2][CVT][L-M-H][raw][DASHBOARD][ ][0]', False, False, False))
    AnalogInputRead.add_parameter(DiagParameter('ANA_R_05', 6, 10, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'ohm', 0, 65535, '[1][M2][Cab_commands][X24][32_Dig_Res_2][ ][ ][raw][DASHBOARD][Y][0]', False, False, False))

    LightSensorRead = DiagMessage(0x1104, 'LightSensorRead', [], None, '', 1)
    LightSensorRead.add_parameter(DiagParameter('SensorValue', 1, 0, 0, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    TellTalesOutputs = DiagMessage(0x1105, 'TellTalesOutputs', [1, 3, 4, 64], None, '', 26)
    TellTalesOutputs.add_parameter(DiagParameter('LD01', 1, 0, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD02', 2, 0, 1, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD03', 3, 0, 2, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD04', 4, 0, 3, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD05', 5, 0, 4, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD06', 6, 0, 5, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD07', 7, 0, 6, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD08', 8, 0, 7, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD09', 9, 1, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD10', 10, 1, 1, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD11', 11, 1, 2, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD12', 12, 1, 3, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD13', 13, 1, 4, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD14', 14, 1, 5, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD15', 15, 1, 6, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD16', 16, 1, 7, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD17', 17, 2, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD18', 18, 2, 1, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD19', 19, 2, 2, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD20', 20, 2, 3, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD21', 21, 2, 4, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD22', 22, 2, 5, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD23', 23, 2, 6, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('LD24', 24, 2, 7, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('SLCD', 25, 3, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    TellTalesOutputs.add_parameter(DiagParameter('Reserved', 26, 3, 1, 7, SignalByteOrder.Intel, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 127, '', False, False, False))

    SLCDOutputs = DiagMessage(0x1106, 'SLCDOutputs', [1, 3, 4, 64], None, '', 57)
    SLCDOutputs.add_parameter(DiagParameter('5BC', 1, 0, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('5G', 2, 0, 1, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('am', 3, 0, 2, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('c', 4, 0, 3, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C1', 5, 0, 4, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C2', 6, 0, 5, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C3', 7, 0, 6, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C4', 8, 0, 7, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C5', 9, 1, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C6', 10, 1, 1, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C7', 11, 1, 2, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C8', 12, 1, 3, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C9', 13, 1, 4, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C10', 14, 1, 5, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C11', 15, 1, 6, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('C12', 16, 1, 7, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('COL1', 17, 2, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('D11', 18, 2, 1, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('F11', 19, 2, 2, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('G18', 20, 2, 3, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('E18', 21, 2, 4, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('DOT', 22, 2, 5, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('f', 23, 2, 6, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('KMH', 24, 2, 7, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('MPH', 25, 3, 0, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('pm', 26, 3, 1, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('RPM', 27, 3, 2, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('X1', 28, 3, 3, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('X2', 29, 3, 4, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('X3', 30, 3, 5, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('X4', 31, 3, 6, 1, SignalByteOrder.Intel, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0': [0, 0], '1': [1, 1]}, 0, 1, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char1', 32, 3, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char2', 33, 4, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char3', 34, 5, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char4', 35, 6, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char6', 36, 7, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char7', 37, 8, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char8', 38, 9, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char9', 39, 10, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char10', 40, 11, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char11', 41, 12, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char12', 42, 13, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char13', 43, 14, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Char14', 44, 15, 7, 8, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphFuelLevelStart', 45, 16, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphFuelLevelStop', 46, 18, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphGaugeInnerLevelStart', 47, 20, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphGaugeInnerLevelStop', 48, 22, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphGaugeLevelStart', 49, 24, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphGaugeLevelStop', 50, 26, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphTempStart', 51, 28, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphTempStop', 52, 30, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphUreaLevelStart', 53, 32, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphUreaLevelStop', 54, 34, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphBrakeStart', 55, 36, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('BargraphBrakeStop', 56, 38, 7, 16, SignalByteOrder.Intel, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    SLCDOutputs.add_parameter(DiagParameter('Reserved', 57, 40, 7, 1, SignalByteOrder.Intel, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 127, '', False, False, False))

    GravisSoftwareIdentification = DiagMessage(0xF100, 'GravisSoftwareIdentification', [1, 2, 3, 4, 64, 65], None, '', 1)
    GravisSoftwareIdentification.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 200 bytes allowed', False, False, False))

    GravisSoftwareFingerprint = DiagMessage(0xF101, 'GravisSoftwareFingerprint', [1, 2, 3, 4, 64], None, '', 5)
    GravisSoftwareFingerprint.add_parameter(DiagParameter('NumberOfFollowingFingerPrints', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 255, 'set to 0 if no valid fingerprints are stored, e.g at delivery status', False, False, False))
    GravisSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingYear', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, 'SPN 964', False, True, False))
    GravisSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, True, False))
    GravisSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingDay', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, True, False))
    GravisSoftwareFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 5, 4, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, True, False))

    GravisFontDataIdentification = DiagMessage(0xF102, 'GravisFontDataIdentification', [1, 2, 3, 4, 64, 65], None, '', 1)
    GravisFontDataIdentification.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 200 bytes allowed', False, False, False))

    GravisFontDataFingerprint = DiagMessage(0xF103, 'GravisFontDataFingerprint', [1, 2, 3, 4, 64], None, '', 5)
    GravisFontDataFingerprint.add_parameter(DiagParameter('NumberOfFollowingFingerPrints', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 255, 'set to 0 if no valid fingerprints are stored, e.g at delivery status', False, False, False))
    GravisFontDataFingerprint.add_parameter(DiagParameter('ProgrammingYear', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, 'SPN 964', False, True, False))
    GravisFontDataFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, True, False))
    GravisFontDataFingerprint.add_parameter(DiagParameter('ProgrammingDay', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, True, False))
    GravisFontDataFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 5, 4, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, True, False))

    GravisIconDataIdentification = DiagMessage(0xF104, 'GravisIconDataIdentification', [1, 2, 3, 4, 64, 65], None, '', 1)
    GravisIconDataIdentification.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 200 bytes allowed', False, False, False))

    GravisIconDataFingerprint = DiagMessage(0xF105, 'GravisIconDataFingerprint', [1, 2, 3, 4, 64], None, '', 5)
    GravisIconDataFingerprint.add_parameter(DiagParameter('NumberOfFollowingFingerPrints', 1, 0, 0, 8, SignalByteOrder.Intel, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 1, 255, 'set to 0 if no valid fingerprints are stored, e.g at delivery status', False, False, False))
    GravisIconDataFingerprint.add_parameter(DiagParameter('ProgrammingYear', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, 'SPN 964', False, True, False))
    GravisIconDataFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, True, False))
    GravisIconDataFingerprint.add_parameter(DiagParameter('ProgrammingDay', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, True, False))
    GravisIconDataFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 5, 4, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, True, False))

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

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [1, 2, 3, 4, 64], None, '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [1, 2, 3, 4, 64], None, '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class IC2_BVWriteDataSignals:
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

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class IC2_BVIOControlDataSignals:
    pass


IC2_BVDTCSnapshotdDids = {
}


class IC2Client(ECUClient):
    class FlashData(Enum):
        # FONT  1
        APPL = [MemoryLocation(0x41000000, 0x0, 32, 32, erase_address=0x41000000, erase_size=None,
                               path_to_file="IC2_.__GRVS.L.00.068.02.______.hex",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(IC2_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   IC2_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False),
        #ICON  2
            MemoryLocation(0x42000000, 0x0, 32, 32, erase_address=0x42000000, erase_size=None,
                           path_to_file="IC2_.__GRVS.I.00.068.02.______.hex",
                           ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                           did_read_obj=deepcopy(IC2_BVReadDataSignals.ApplicationSoftwareIdentification),
                           did_fingerprint_obj=deepcopy(
                               IC2_BVReadDataSignals.ApplicationSoftwareFingerprint),
                           did_dependency=None, consider_in_mdr=False),
                #SW1 3
                MemoryLocation(0x1A20000, 0x0, 32, 32, erase_address=0x1A20000, erase_size=None,
                               path_to_file="IC2_.17_SW1.F.00.068.02.______.hex",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(IC2_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   IC2_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False),
                #SW2  4
                MemoryLocation(0x1D00000, 0x0, 32, 32, erase_address=0x1D00000, erase_size=None,
                               path_to_file="IC2_.__GRVS.O.00.068.02.______.hex",
                               ecu_reset=True, wait_time_ecu_reset=0, area_name="APPL",
                               did_read_obj=deepcopy(IC2_BVReadDataSignals.ApplicationSoftwareIdentification),
                               did_fingerprint_obj=deepcopy(
                                   IC2_BVReadDataSignals.ApplicationSoftwareFingerprint),
                               did_dependency=None, consider_in_mdr=False)]

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0x17, "IC2", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=2, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = IC2_BVReadDataSignals
        self.write_dids = IC2_BVWriteDataSignals
        self.routine_dids = IC2_BVRoutineIdentifierSignals
        self.io_dids = IC2_BVIOControlDataSignals
        self.dtc_snapshot_dids = IC2_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

