from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class DYNA4_TR2_BVRoutineIdentifierSignals:
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


class DYNA4_TR2_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    PowerVoltage = DiagMessage(0x1061, 'PowerVoltage', [1, 3, 4, 64], None, '', 4)
    PowerVoltage.add_parameter(DiagParameter('PowerSupplyVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('IGNswitch', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('12VHSD6', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('10VREF', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2][Miscellaneous][ ][2-41][D4-D6][L-S][raw][A5_T2][N][2]', False, False, False))

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
    AnalogInput.add_parameter(DiagParameter('AN_11', 11, 20, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN_12', 12, 22, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 65535, '[1][S2-S3-M1][Transmission][X19-B14][21-AN_12][D6][L-S][raw][A5_T2][Y_Y_Y][0_0_0]', False, False, False))

    DigitalInput_Read = DiagMessage(0x1063, 'DigitalInput_Read', [1, 3, 4, 64], None, '', 15)
    DigitalInput_Read.add_parameter(DiagParameter('FREQ_1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('FREQ_2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('FREQ_3', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_1', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S3-M1][PTO][X592][30-AN_1][D6][L-S][raw][A5_T2][Y_Y][0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_2', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2-S3-M1][Cab_commands][X726E-X726M][16-AN_2][D6][L-S][raw][A5_T2][Y_N_N][2_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_3', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S3-M1][Cab_commands][X604][31-AN_3][D6][L-S][raw][A5_T2][Y_Y][0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_4', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_5', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S3-M1][Cab_commands][X295][32-AN_5][D6][L-S][raw][A5_T2][Y_Y][0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_6', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2-S3-M1][Cab_commands][X66][18-AN_6][D6][L-S][raw][A5_T2][Y_Y_Y][2_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_7', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Braking_system][X618][33-AN_7][D4][L-S][raw][A5_T2][Y][0]#[1][S2-S3-M1][Cab_commands][X67][33-AN_7][D6][L-S][raw][A5_T2][Y_Y_Y][2_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_8', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_9', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_10', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_11', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2-S3-M1][Transmission][X494][35-AN_11][D6][L-S][raw][A5_T2][Y_Y_Y][1_0_0]', False, False, False))
    DigitalInput_Read.add_parameter(DiagParameter('AN_12', 15, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X726E][21-AN_12][D4][L-S][raw][A5_T2][Y][1]', False, False, False))

    FreqInput = DiagMessage(0x1064, 'FreqInput', [1, 3, 4, 64], None, '', 3)
    FreqInput.add_parameter(DiagParameter('FREQ_1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][S2][Transmission][X482-B9][38-FRQ_1][D4][L-S][raw][A5_T2][Y][1]#[1][S2-S3-M1][Transmission][X481-B30][38-FRQ_1][D6][L-S][raw][A5_T2][Y_Y_Y][0_0_0]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][S2][PTO][X777][37-FRQ_2][D4][L-S][raw][A5_T2][Y][0]#[1][S2][PTO][X776][37-FRQ_2][D6][L-S][raw][A5_T2][Y][2]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ_3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][S2][PTO][X776][36-FRQ_3][D4][L-S][raw][A5_T2][Y][1]#[1][S2-S3-M1][Transmission][X492-B49][36-FRQ_3][D6][L-S][raw][A5_T2][Y_Y_Y][0_0_0]', False, False, False))

    DigitalOutput_Read = DiagMessage(0x1065, 'DigitalOutput_Read', [1, 3, 4, 64], None, '', 12)
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_3', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X729][7-HSD_3][D4][L-S][raw][A5_T2][Y][0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_4', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X728][8-HSD_4][D4][L-S][raw][A5_T2][Y][0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_5', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X774][22-HSD_5][D6][L-S][raw][A5_T2][Y][0]#[1][S3-M1][PTO][X4][22-HSD_5][D6][L-S][raw][A5_T2][Y_Y][0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_6', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_7', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_8', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S3-M1][PTO][X778][24-HSD_8][D6][L-S][raw][A5_T2][Y_Y][0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_9', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2-S3-M1][Difflock][X6-Y1][11-HSD_9][D6][L-S][raw][A5_T2][Y_Y_Y][1_0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_10', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2-S3-M1][4WD][X5-Y3][25-HSD_10][D6][L-S][raw][A5_T2][Y_Y_Y][2_0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_11', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X775][12-HSD_11][D4][L-S][raw][A5_T2][Y][0]#[1][S3-M1][PTO][X774][12-HSD_11][D6][L-S][raw][A5_T2][Y_Y][0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_12', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X599][26-HSD_12][D6][L-S][raw][A5_T2][Y][1]#[1][S3-M1][PTO][X599][26-HSD_12][D6][L-S][raw][A5_T2][Y_Y][0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_13', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Miscellaneous][K15][13-HSD_13][D4][L-S][raw][A5_T2][Y][0]#[1][S2][PTO][X775][13-HSD_13][D6][L-S][raw][A5_T2][Y][1]#[1][S3-M1][PTO][X498][13-HSD_13][D6][L-S][raw][A5_T2][Y_Y][0_0]', False, False, False))
    DigitalOutput_Read.add_parameter(DiagParameter('HSD_14', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'ON': [0, 0], 'OFF': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Miscellaneous][K24][27-HSD_14][D4][L-S][raw][A5_T2][Y][2]#[1][S2-S3-M1][Miscellaneous][K24][27-HSD_14][D6][L-S][raw][A5_T2][Y_Y_Y][2_0_0]', False, False, False))

    AnalogOutput = DiagMessage(0x1066, 'AnalogOutput', [1, 3, 4, 64], None, '', 6)
    AnalogOutput.add_parameter(DiagParameter('HSD_1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2-S3-M1][Transmission][X478-Y76][5-HSD_1][D6][L-S][raw][A5_T2][Y_Y_Y][0_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2-S3-M1][Transmission][X479-Y77][6-HSD_2][D6][L-S][raw][A5_T2][Y_Y_Y][0_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_5', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_6', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '[1][S2][PTO][X16][23-HSD_6][D4][L-S][raw][A5_T2][Y][1]#[1][S2-S3-M1][Transmission][X480-Y84][23-HSD_6][D6][L-S][raw][A5_T2][Y_Y_Y][0_0_0]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_7', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD_8', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 65535, '', False, False, False))

    Fct_Pto = DiagMessage(0x1067, 'Fct_Pto', [1, 3, 4, 64], None, '', 20)
    Fct_Pto.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('pto_command_cabine', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('pto_command_stop', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('pto_command_fender_start', 7, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('ops', 8, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('EngineSpeed', 9, 9, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('pto_state', 10, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PTO_OFF': [0, 0], 'PTO_INIT': [1, 1], 'PTO_FILLING': [2, 2], 'PTO_START': [3, 3], 'PTO_PULSING': [4, 4], 'PTO_ON': [5, 5], 'PTO_SENSORS_OFF': [6, 6], 'PTO_ALARM': [7, 7], 'PTO_FENDER': [8, 8], 'STATE_PTO_EV_ON_OFF': [9, 9]}, 0, 9, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('pto_speed', 11, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '[1][S2][PTO][X777][37-FRQ_2][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('pto_energie', 12, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('Gspto_Switch', 13, 16, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X729][7-HSD_3][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('Gspto_Command', 14, 17, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Cab_commands][X726E][21-AN_12][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('EV_Gspto', 15, 18, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][S2][PTO][X728][8-HSD_4][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('VehicleSpeedWheel', 16, 19, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 65535, '[1][S2][Transmission][X482-B9][38-FRQ_1][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('PtoShaftSpeed', 17, 21, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 65535, '[1][S2][PTO][X776][36-FRQ_3][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('EV_brake', 18, 23, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][PTO][X775][12-HSD_11][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('Pto_pwm', 19, 24, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 65535, '[1][S2][PTO][X16][23-HSD_6][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_Pto.add_parameter(DiagParameter('ParkingBrakeSensor', 20, 25, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Braking_system][X618][33-AN_7][D4][L-S][conv][A5_T2][N][0]', False, False, False))

    Fct_HighPressurebrake = DiagMessage(0x1068, 'Fct_HighPressurebrake', [1, 3, 4, 64], None, '', 9)
    Fct_HighPressurebrake.add_parameter(DiagParameter('FunctionAvailable', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_HighPressurebrake.add_parameter(DiagParameter('EngineRunning', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_HighPressurebrake.add_parameter(DiagParameter('PowerSupplyVoltage', 3, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fct_HighPressurebrake.add_parameter(DiagParameter('TransOilPressure', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_HighPressurebrake.add_parameter(DiagParameter('EV_Brake', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_HighPressurebrake.add_parameter(DiagParameter('50kph_Sensor_secondary', 6, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'bar', 0, 65535, '', False, False, False))
    Fct_HighPressurebrake.add_parameter(DiagParameter('50kph_Sensor', 7, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'bar', 0, 65535, '', False, False, False))
    Fct_HighPressurebrake.add_parameter(DiagParameter('BrakeLights', 8, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Miscellaneous][K24][27-HSD_14][D4][L-S][conv][A5_T2][Y][0]', False, False, False))
    Fct_HighPressurebrake.add_parameter(DiagParameter('ReversingLight', 9, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '[1][S2][Miscellaneous][K15][13-HSD_13][D4][L-S][conv][A5_T2][Y][0]', False, False, False))

    Fct_Parklock = DiagMessage(0x1072, 'Fct_Parklock', [], None, '', 8)
    Fct_Parklock.add_parameter(DiagParameter('Switch_usure_PK1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Parklock.add_parameter(DiagParameter('Switch_onoff', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Parklock.add_parameter(DiagParameter('Command_PL', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Parklock.add_parameter(DiagParameter('EV_Road', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Parklock.add_parameter(DiagParameter('EV_Park', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'ERROR': [2, 2], 'NOT_AVAILABLE': [3, 3]}, 0, 3, '', False, False, False))
    Fct_Parklock.add_parameter(DiagParameter('ShuttleShiftStatus', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'FORWARD': [0, 0], 'NEUTRAL': [1, 1], 'REVERSE': [2, 2]}, 0, 2, '', False, False, False))
    Fct_Parklock.add_parameter(DiagParameter('TransOilTemperature', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -40.0, 1.0, '?C', 0, 200, '', False, False, False))
    Fct_Parklock.add_parameter(DiagParameter('VehicleSpeed', 8, 7, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'km/h', 0, 65535, '', False, False, False))

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


class DYNA4_TR2_BVWriteDataSignals:
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


class DYNA4_TR2_BVIOControlDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [4], [4], '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))


DYNA4_TR2_BVDTCSnapshotdDids = {
}


class DYNA4_TR2Client(ECUClient):
    class FlashData(Enum):
        pass

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0xA1, "DYNA4_TR2", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=5, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = DYNA4_TR2_BVReadDataSignals
        self.write_dids = DYNA4_TR2_BVWriteDataSignals
        self.routine_dids = DYNA4_TR2_BVRoutineIdentifierSignals
        self.io_dids = DYNA4_TR2_BVIOControlDataSignals
        self.dtc_snapshot_dids = DYNA4_TR2_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

