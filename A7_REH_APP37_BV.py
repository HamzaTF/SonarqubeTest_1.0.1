from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class A7_REH_APP37_BVRoutineIdentifierSignals:
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


class A7_REH_APP37_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    WorkingHourModule = DiagMessage(0x1011, 'WorkingHourModule', [1, 2, 3], None, '', 1)
    WorkingHourModule.add_parameter(DiagParameter('WorkingHourModule', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4211081215, '', False, False, False))

    PowerVoltage = DiagMessage(0x1061, 'PowerVoltage', [1, 2, 3], None, '', 4)
    PowerVoltage.add_parameter(DiagParameter('PowerSupplyVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 64255, '[1][C2C3_20-C3_21][Miscellaneous][ ][E4_10CREF][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][Miscellaneous][ ][E4_10CREF][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('IGNSwitch', 2, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X68][G1-IGN_sw][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('12VHSD6', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '', False, False, False))
    PowerVoltage.add_parameter(DiagParameter('10VREF', 4, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 64255, '[1][C2C3_20-C3_21][Miscellaneous][ ][E4_10CREF][Meca][Base][conv][A7_137][Y][1]#[1][C2C3_20-C3_21][Miscellaneous][ ][E4_10CREF][Meca][Base][conv][A7_138][Y][1]', False, False, False))

    AnalogInput = DiagMessage(0x1062, 'AnalogInput', [1, 2, 3, 4], None, '', 9)
    AnalogInput.add_parameter(DiagParameter('AN1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Cab_commands][X68][B2-AN_1][Meca][Base][raw][A7_138][Y][1]#[1][C2C3_20-C3_21][Linkage][X30][B2-AN_1][Meca][Base][raw][A7_137][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Linkage][X31][A3-AN_2][Meca][Base][raw][A7_137][Y][0]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Cab_commands][X897][B3-AN_3][Meca][Base][raw][A7_137][Y][2]#[1][C2C3_20-C3_21][Cab_commands][X906][B3-AN_3][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Cab_commands][X898][B3-AN_4][Meca][Base][raw][A7_137][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN5', 5, 8, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Cab_commands][X751][A2-AN_5][Meca][Base][raw][A7_137][Y][2]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN6', 6, 10, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Cab_commands][X294][A4-AN_6][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN7', 7, 12, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Cab_commands][X750][B4-AN_7][Meca][Base][raw][A7_137][Y][2]#[1][C2C3_20-C3_21][Cab_commands][X913][B4-AN_7][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN8', 8, 14, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Cab_commands][X97][C1-AN_8][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][Cab_commands][X97][C1-AN_8][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][Cab_commands][X295][C1-AN_8][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    AnalogInput.add_parameter(DiagParameter('AN9', 9, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 0, 64255, '[1][C2C3_20-C3_21][Transmission][X19][A1-AN_9][Meca][Base][raw][A7_138][Y][1]', False, False, False))

    DigitalInput = DiagMessage(0x1063, 'DigitalInput', [1, 2, 3], None, '', 18)
    DigitalInput.add_parameter(DiagParameter('FREQ1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Transmission][X481][D1-FREQ_1][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][Transmission][X481][D1-FREQ_1][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('FREQ3', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Cab_commands][X1010][D3-FREQ_3][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN1', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN2', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN3', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN4', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Transmission][X1117][B1-AN_4][Meca][Base][raw][A7_138][Y][2]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN5', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Cab_commands][X128][A2-AN-5][Meca][Base][raw][A7_137][Y][2]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN6', 9, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN7', 10, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN8', 11, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('AN9', 12, 11, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CLOSE': [0, 0], 'OPEN': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Transmission][X752][A1-AN_9][Meca][Base][raw][A7_138][Y][2]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('BINARY_1', 13, 12, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Cab_commands][X67][C3-BIN_1][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][Cab_commands][X68][C3-BIN_1][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('BINARY_2', 14, 13, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CLOSE': [0, 0], 'OPEN': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Cab_commands][X66][C2-BIN_2][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][Transmission][X1084][C2-BIN_2][Meca][Base][raw][A7_138][Y][2]', False, False, False))
    DigitalInput.add_parameter(DiagParameter('HSD_AUX1', 15, 14, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('HSD_AUX2', 16, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('HSD_AUX3', 17, 16, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A.': [3, 3]}, 0, 3, '', False, False, False))
    DigitalInput.add_parameter(DiagParameter('HSD_AUX4', 18, 17, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A.': [3, 3]}, 0, 3, '', False, False, False))

    FreqInput = DiagMessage(0x1064, 'FreqInput', [1, 2, 3], None, '', 4)
    FreqInput.add_parameter(DiagParameter('FREQ1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 64225, '', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 64225, '[1][C2C3_20-C3_21][Transmission][X482][D2-FREQ_2][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][Transmission][X482][D2-FREQ_2][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ3', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 64225, '', False, False, False))
    FreqInput.add_parameter(DiagParameter('FREQ4', 4, 6, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 64225, '', False, False, False))

    DigitalOutput = DiagMessage(0x1065, 'DigitalOutput', [1, 2, 3], None, '', 5)
    DigitalOutput.add_parameter(DiagParameter('HSD_AUX_1', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Transmission][X772][F3-HSD_AUX_1][Meca][Base][raw][A7_138][Y][1]#[1][C2C3_20-C3_21][Transmission][X773][E1-HSD_AUX_1][Meca][Base][raw][A7_138][Y][1]#[1][C2C3_20-C3_21][4WD][X5][F3-HSD_AUX_1][Meca][Base][raw][A7_137][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_AUX_2', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Transmission][X1083][F2-HSD_AUX_2][Meca][Base][raw][A7_138][Y][1]#[1][C2C3_20-C3_21][Linkage][X727][F2-HSD_AUX_2][Meca][Base][raw][A7_137][Y][0]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_AUX_3', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Braking_system][X987][F1-HSD_AUX_3][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][PTO][X774][F1-HSD_AXU_3][Meca][Base][raw][A7_138][Y][1]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD_AUX_4', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '[1][C2C3_20-C3_21][Cab_commands][X128][E1-HSD_AUX_4][Meca][Base][raw][A7_137][Y][2]', False, False, False))
    DigitalOutput.add_parameter(DiagParameter('HSD6', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Off': [0, 0], 'On': [1, 1], 'Error': [2, 2], 'N.A': [3, 3]}, 0, 3, '', False, False, False))

    AnalogOutput = DiagMessage(0x1066, 'AnalogOutput', [1, 2, 3], None, '', 3)
    AnalogOutput.add_parameter(DiagParameter('HSD1', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 64255, '[1][C2C3_20-C3_21][Transmission][X556][G2-HSD_1][Meca][Base][raw][A7_138][Y][2]#[1][C2C3_20-C3_21][Linkage][X27][G2-HSD_1][Meca][Base][raw][A7_137][Y][2]#[1][C2C3_20-C3_21][Linkage][X27][G2-HSD_1_2_CURSEN][Meca][Base][raw][A7_137][Y][2]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD2', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 64255, '[1][C2C3_20-C3_21][Transmission][X557][G3-HSD_2][Meca][Base][raw][A7_138][Y][2]#[1][C2C3_20-C3_21][Linkage][X28][G3-HSD_2][Meca][Base][raw][A7_137][Y][2]', False, False, False))
    AnalogOutput.add_parameter(DiagParameter('HSD6', 3, 4, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '%', 0, 64255, '[1][C2C3_20-C3_21][PTO][X7][H2-HSD_6][Meca][Base][raw][A7_137][Y][1]#[1][C2C3_20-C3_21][PTO][X599][H2-HSD_6][Meca][Base][raw][A7_138][Y][1]', False, False, False))

    Fn4m = DiagMessage(0x1067, 'Fn4m', [1, 2, 3], None, '', 8)
    Fn4m.add_parameter(DiagParameter('EngineRunning', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fn4m.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    Fn4m.add_parameter(DiagParameter('FourWheelCommand', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    Fn4m.add_parameter(DiagParameter('EVFourWheelDrive', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][4WD][X5][F3-HSD_AUX_1][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    Fn4m.add_parameter(DiagParameter('VehicleSpeedWheel', 5, 5, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'km/h', 0, 64255, '[1][C2C3_20-C3_21][Transmission][X482][D2-FREQ_2][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    Fn4m.add_parameter(DiagParameter('LeftBrakePressed', 6, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X66][C2-BIN_2][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    Fn4m.add_parameter(DiagParameter('RightBrakePressed', 7, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X67][C3-BIN_1][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    Fn4m.add_parameter(DiagParameter('HandBrake', 8, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    FnDiffloc = DiagMessage(0x1068, 'FnDiffloc', [1, 2, 3], None, '', 6)
    FnDiffloc.add_parameter(DiagParameter('EngineRunning', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnDiffloc.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '[1][C2C3_20-C3_21][Difflock][X6][F2-HSD_AUX_2][Meca][Base][raw][A7_137][Y][1]', False, False, False))
    FnDiffloc.add_parameter(DiagParameter('DifflockCommand', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnDiffloc.add_parameter(DiagParameter('EVDifflock', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Difflock][X6][F2-HSD_AUX_2][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    FnDiffloc.add_parameter(DiagParameter('LeftBrakePressed', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnDiffloc.add_parameter(DiagParameter('RightBrakePressed', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    FnPto = DiagMessage(0x1069, 'FnPto', [1, 2, 3], None, '', 16)
    FnPto.add_parameter(DiagParameter('EngineRunning', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoCommandCabin', 3, 3, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X128][E1-HSD_AUX_4][Meca][Base][conv][A7_137][Y][2]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoCommandStop', 4, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][PTO][X776][D3-FREQ_3][Meca][Base][raw][A7_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoCommandFenderStart', 5, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnPto.add_parameter(DiagParameter('Ops', 6, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][PTO][X777][D4-FREQ_4][Meca][Base][raw][A7_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('EngineSpeed', 7, 7, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 64255, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoStateBo', 8, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'FILLING': [2, 2], 'START': [3, 3], 'PULSING': [4, 4], 'ONx1': [5, 5], 'SENSORS': [6, 6], 'ALARM': [7, 7], 'FENDER': [8, 8], 'STATE_PTO_EV_ON_OFF': [9, 9]}, 0, 9, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoStateBf', 9, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'FILLING': [2, 2], 'START': [3, 3], 'PULSING': [4, 4], 'ONx1': [5, 5], 'SENSORS': [6, 6], 'ALARM': [7, 7], 'FENDER': [8, 8], 'STATE_PTO_EV_ON_OFF': [9, 9]}, 0, 9, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoSpeed', 10, 11, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 64255, '[1][C2C3_20-C3_21][PTO][X777][D4-FREQ_4][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoEnergy', 11, 13, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))
    FnPto.add_parameter(DiagParameter('GsptoCommand', 12, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X726-M][H3-12_Vhsd_6][Meca][Base][conv][A7_137][Y][2]', False, False, False))
    FnPto.add_parameter(DiagParameter('VehicleSpeedWheel', 13, 16, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'Hz', 0, 64255, '', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoShaftSpeed', 14, 18, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 64255, '[1][C2C3_20-C3_21][PTO][X776][D3-FREQ_3][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    FnPto.add_parameter(DiagParameter('BrakePtoCmde', 15, 20, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X128][A2-AN-5][Meca][Base][conv][A7_137][Y][0]', False, False, False))
    FnPto.add_parameter(DiagParameter('PtoPwrn', 16, 21, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    FnRearHitchSettingInput = DiagMessage(0x106A, 'FnRearHitchSettingInput', [1, 2, 3], None, '', 8)
    FnRearHitchSettingInput.add_parameter(DiagParameter('FnRearHitchSettingInput', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))
    FnRearHitchSettingInput.add_parameter(DiagParameter('SettingDraftSensibility', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))
    FnRearHitchSettingInput.add_parameter(DiagParameter('SettingUpperLimit', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))
    FnRearHitchSettingInput.add_parameter(DiagParameter('SettingLoweringSpeed', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))
    FnRearHitchSettingInput.add_parameter(DiagParameter('Switch3Position', 5, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Downshift': [1, 1], 'Neutral': [2, 2], 'Downshiftx1': [3, 3], 'Neutralx1': [4, 4], 'Upshift': [5, 5], 'Neutralx2': [6, 6], 'Upshiftx1': [7, 7]}, 1, 7, '[1][C2C3_20-C3_21][Cab_commands][X363][A4-AN_6][Meca][Base][conv][A7_137][Y][2]', False, False, False))
    FnRearHitchSettingInput.add_parameter(DiagParameter('DampingSwitch', 6, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnRearHitchSettingInput.add_parameter(DiagParameter('Command98L', 7, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X363][A4-AN_6][Meca][Base][raw][A7_137][Y][1]', False, False, False))
    FnRearHitchSettingInput.add_parameter(DiagParameter('QuickSoilEngagement', 8, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    FnReadHitch = DiagMessage(0x106B, 'FnReadHitch', [1, 2, 3], None, '', 16)
    FnReadHitch.add_parameter(DiagParameter('ProportiornalValveSetpointCurrent', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 64255, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('WheelSpeed', 2, 2, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'kph', 0, 64255, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('FunctionAvailable', 3, 4, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('PowerSupplyVoltage', 4, 5, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('EngineRunning', 5, 7, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('LiftingCommand', 6, 8, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X97][C1-AN_8][Meca][Base][conv][A7_137][Y][2]', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('LoweringCommand', 7, 9, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X97][C1-AN_8][Meca][Base][conv][A7_137][Y][2]', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('ExternalCommand', 8, 10, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Low': [1, 1], 'Low to neutral': [2, 2], 'Neutral to low': [3, 3], 'Neutral': [4, 4], 'Neutral to high': [5, 5], 'High to neutral': [6, 6], 'High': [7, 7]}, 1, 7, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('HitchRearPosActVal', 9, 11, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '[1][C2C3_20-C3_21][Linkage][X30][B2-AN_1][Meca][Base][conv][A7_137][Y][2]', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('SettingPosition', 10, 12, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 255, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('HitchValveCurrent', 11, 13, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mA', 0, 64255, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('Command98L', 12, 15, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('MeasureLeftDraft', 13, 16, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, -50.0, 1.0, '%', 0, 64255, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('SignalLeftDraftTonne', 14, 17, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.01, 't', 0, 18000, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('EVLoweringHusco', 15, 19, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'entry0': [0, 0], 'entry1': [1, 1]}, 0, 1, '', False, False, False))
    FnReadHitch.add_parameter(DiagParameter('LinkageMode', 16, 20, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'Error': [0, 0], 'Transport': [1, 1], 'Suspension': [2, 2], 'Work': [3, 3], 'Neutral': [4, 4], 'Calibration': [5, 5], 'QuickSoilEngagement': [6, 6]}, 0, 6, '', False, False, False))

    FnGeneral = DiagMessage(0x106C, 'FnGeneral', [1, 2, 3], None, '', 5)
    FnGeneral.add_parameter(DiagParameter('EngineRunning', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))
    FnGeneral.add_parameter(DiagParameter('PowerSupplyVoltage', 2, 1, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.001, 'V', 8000, 16000, '', False, False, False))
    FnGeneral.add_parameter(DiagParameter('EngineSpeed', 3, 3, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'rpm', 0, 64255, '[1][C2C3_20-C3_21][Transmission][X481][D1-FREQ_1][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    FnGeneral.add_parameter(DiagParameter('TrailerBrakeCommand', 4, 5, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Braking_system][X987][F1-HSD_AUX_3][Meca][Base][conv][A7_137][Y][1]', False, False, False))
    FnGeneral.add_parameter(DiagParameter('ReverseLight', 5, 6, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    CalibrationFingerprint = DiagMessage(0xD201, 'CalibrationFingerprint', [1, 2, 3], None, '', 8)
    CalibrationFingerprint.add_parameter(DiagParameter('UserID_0', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    CalibrationFingerprint.add_parameter(DiagParameter('Timestamp_0', 2, 4, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    CalibrationFingerprint.add_parameter(DiagParameter('UserID_1', 3, 8, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    CalibrationFingerprint.add_parameter(DiagParameter('Timestamp_1', 4, 12, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    CalibrationFingerprint.add_parameter(DiagParameter('UserID_2', 5, 16, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    CalibrationFingerprint.add_parameter(DiagParameter('Timestamp_2', 6, 20, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    CalibrationFingerprint.add_parameter(DiagParameter('UserID_3', 7, 24, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    CalibrationFingerprint.add_parameter(DiagParameter('Timestamp_3', 8, 28, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))

    ConfigurationFingerprint = DiagMessage(0xD202, 'ConfigurationFingerprint', [1, 2, 3], None, '', 8)
    ConfigurationFingerprint.add_parameter(DiagParameter('UserID_0', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ConfigurationFingerprint.add_parameter(DiagParameter('Timestamp_0', 2, 4, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ConfigurationFingerprint.add_parameter(DiagParameter('UserID_1', 3, 8, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ConfigurationFingerprint.add_parameter(DiagParameter('Timestamp_1', 4, 12, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ConfigurationFingerprint.add_parameter(DiagParameter('UserID_2', 5, 16, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ConfigurationFingerprint.add_parameter(DiagParameter('Timestamp_2', 6, 20, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ConfigurationFingerprint.add_parameter(DiagParameter('UserID_3', 7, 24, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ConfigurationFingerprint.add_parameter(DiagParameter('Timestamp_3', 8, 28, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))

    ParametrizationFingerprint = DiagMessage(0xD203, 'ParametrizationFingerprint', [1, 2, 3], None, '', 8)
    ParametrizationFingerprint.add_parameter(DiagParameter('UserID_0', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ParametrizationFingerprint.add_parameter(DiagParameter('Timestamp_0', 2, 4, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ParametrizationFingerprint.add_parameter(DiagParameter('UserID_1', 3, 8, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ParametrizationFingerprint.add_parameter(DiagParameter('Timestamp_1', 4, 12, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ParametrizationFingerprint.add_parameter(DiagParameter('UserID_2', 5, 16, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ParametrizationFingerprint.add_parameter(DiagParameter('Timestamp_2', 6, 20, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ParametrizationFingerprint.add_parameter(DiagParameter('UserID_3', 7, 24, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    ParametrizationFingerprint.add_parameter(DiagParameter('Timestamp_3', 8, 28, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))

    DownloadFingerprint = DiagMessage(0xD204, 'DownloadFingerprint', [1, 2, 3], None, '', 8)
    DownloadFingerprint.add_parameter(DiagParameter('UserID_0', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    DownloadFingerprint.add_parameter(DiagParameter('Timestamp_0', 2, 4, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    DownloadFingerprint.add_parameter(DiagParameter('UserID_1', 3, 8, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    DownloadFingerprint.add_parameter(DiagParameter('Timestamp_1', 4, 12, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    DownloadFingerprint.add_parameter(DiagParameter('UserID_2', 5, 16, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    DownloadFingerprint.add_parameter(DiagParameter('Timestamp_2', 6, 20, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    DownloadFingerprint.add_parameter(DiagParameter('UserID_3', 7, 24, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))
    DownloadFingerprint.add_parameter(DiagParameter('Timestamp_3', 8, 28, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967295, '', False, False, False))

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


class A7_REH_APP37_BVWriteDataSignals:
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


class A7_REH_APP37_BVIOControlDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [4], [4], '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))


A7_REH_APP37_BVDTCSnapshotdDids = {
}


class A7_REH_APP37Client(ECUClient):
    class FlashData(Enum):
        pass

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0x7, "A7_REH_APP37", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=6, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = A7_REH_APP37_BVReadDataSignals
        self.write_dids = A7_REH_APP37_BVWriteDataSignals
        self.routine_dids = A7_REH_APP37_BVRoutineIdentifierSignals
        self.io_dids = A7_REH_APP37_BVIOControlDataSignals
        self.dtc_snapshot_dids = A7_REH_APP37_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

