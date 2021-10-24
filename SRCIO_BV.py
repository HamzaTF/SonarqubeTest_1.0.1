from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class SRCIO_BVRoutineIdentifierSignals:
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


class SRCIO_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    UdsDiag_GetPneumatic_AirDryer_State = DiagMessage(0xA704, 'UdsDiag_GetPneumatic_AirDryer_State', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumatic_AirDryer_State.add_parameter(DiagParameter('Pneumatic_AirDryer_State', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'DRY_INIT': [0, 0], 'DRY_ENGINE_OFF': [1, 1], 'DRY_IDLE': [2, 2], 'DRY_PUMPING': [3, 3], 'DRY_START': [4, 4], 'DRY_DELAY': [5, 5], 'DRY_REGENERATE': [6, 6], 'DRY_STOP': [7, 7]}, 0, 7, '', False, False, False))

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

    UdsDiag_GetPneumaticTrailerBrake_Park_SOL = DiagMessage(0xA970, 'UdsDiag_GetPneumaticTrailerBrake_Park_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumaticTrailerBrake_Park_SOL.add_parameter(DiagParameter('PneumaticTrailerBrake_Park_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetPneumaticTrailerBrake_PROP_SOL = DiagMessage(0xA971, 'UdsDiag_GetPneumaticTrailerBrake_PROP_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumaticTrailerBrake_PROP_SOL.add_parameter(DiagParameter('PneumaticTrailerBrake_PROP_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetPneumaticTrailerBrake_CutOutValve_Rel = DiagMessage(0xA972, 'UdsDiag_GetPneumaticTrailerBrake_CutOutValve_Rel', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumaticTrailerBrake_CutOutValve_Rel.add_parameter(DiagParameter('PneumaticTrailerBrake_CutOutValve_Rel', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetPneumaticTrailerBrake_CutOutValvePressureContact = DiagMessage(0xA973, 'UdsDiag_GetPneumaticTrailerBrake_CutOutValvePressureContact', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumaticTrailerBrake_CutOutValvePressureContact.add_parameter(DiagParameter('PneumaticTrailerBrake_CutOutValvePressureContact', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 255, '', False, False, False))

    UdsDiag_GetPneumaticTrailerBrake_TankPressure2 = DiagMessage(0xA974, 'UdsDiag_GetPneumaticTrailerBrake_TankPressure2', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumaticTrailerBrake_TankPressure2.add_parameter(DiagParameter('PneumaticTrailerBrake_TankPressure2', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.001, 1.0, 'bar', 0, 255, '', False, False, False))

    UdsDiag_GetPneumaticTrailerBrake_TankPressure = DiagMessage(0xA975, 'UdsDiag_GetPneumaticTrailerBrake_TankPressure', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumaticTrailerBrake_TankPressure.add_parameter(DiagParameter('PneumaticTrailerBrake_TankPressure', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.001, 1.0, 'bar', 0, 255, '', False, False, False))

    UdsDiag_GetPneumatic_Drying_Governor_SOL = DiagMessage(0xA976, 'UdsDiag_GetPneumatic_Drying_Governor_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumatic_Drying_Governor_SOL.add_parameter(DiagParameter('Pneumatic_Drying_Governor_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetPneumatic_Drying_Regeneration_SOL = DiagMessage(0xA977, 'UdsDiag_GetPneumatic_Drying_Regeneration_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetPneumatic_Drying_Regeneration_SOL.add_parameter(DiagParameter('Pneumatic_Drying_Regeneration_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHitch_Dromone_Extend_Sw = DiagMessage(0xA97D, 'UdsDiag_GetHitch_Dromone_Extend_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Dromone_Extend_Sw.add_parameter(DiagParameter('Hitch_Dromone_Extend_Sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHitch_Dromone_Retract_Sw = DiagMessage(0xA97E, 'UdsDiag_GetHitch_Dromone_Retract_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Dromone_Retract_Sw.add_parameter(DiagParameter('Hitch_Dromone_Retract_Sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHitch_Dromone_Up_Sw = DiagMessage(0xA97F, 'UdsDiag_GetHitch_Dromone_Up_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Dromone_Up_Sw.add_parameter(DiagParameter('Hitch_Dromone_Up_Sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHitch_Dromone_Down_Sw = DiagMessage(0xA980, 'UdsDiag_GetHitch_Dromone_Down_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Dromone_Down_Sw.add_parameter(DiagParameter('Hitch_Dromone_Down_Sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHitch_Dromone_Extend_SOL = DiagMessage(0xA981, 'UdsDiag_GetHitch_Dromone_Extend_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Dromone_Extend_SOL.add_parameter(DiagParameter('Hitch_Dromone_Extend_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetHitch_Dromone_Retract_SOL = DiagMessage(0xA982, 'UdsDiag_GetHitch_Dromone_Retract_SOL', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetHitch_Dromone_Retract_SOL.add_parameter(DiagParameter('Hitch_Dromone_Retract_SOL', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetISO11786_HitchPosition = DiagMessage(0xA983, 'UdsDiag_GetISO11786_HitchPosition', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO11786_HitchPosition.add_parameter(DiagParameter('ISO11786_HitchPosition', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'mV', 0, 255, '', False, False, False))

    UdsDiag_GetISO11786_DiscretHitchPosition = DiagMessage(0xA984, 'UdsDiag_GetISO11786_DiscretHitchPosition', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO11786_DiscretHitchPosition.add_parameter(DiagParameter('ISO11786_DiscretHitchPosition', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_LeftBlinker_Input = DiagMessage(0xA99F, 'UdsDiag_GetLight_LeftBlinker_Input', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_LeftBlinker_Input.add_parameter(DiagParameter('Light_LeftBlinker_InputState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_RightBlinker_Input = DiagMessage(0xA9A0, 'UdsDiag_GetLight_RightBlinker_Input', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_RightBlinker_Input.add_parameter(DiagParameter('Light_RightBlinker_InputState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_RotarySw_Ana = DiagMessage(0xA9A2, 'UdsDiag_GetLight_RotarySw_Ana', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_RotarySw_Ana.add_parameter(DiagParameter('Light_RotarySw_AnaState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'SWITCH_OFF': [0, 0], 'SWITCH_PORCHLIGHT': [1, 1], 'SWITCH_TAIL_LIGHT': [2, 2], 'SWITCH_FULL_LIGHT': [3, 3], 'SWITCH_ROAD_LIGHT_AUTO': [4, 4]}, 0, 4, '', False, False, False))

    UdsDiag_GetLight_RightBlinker_Out = DiagMessage(0xA9A3, 'UdsDiag_GetLight_RightBlinker_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_RightBlinker_Out.add_parameter(DiagParameter('Light_RightBlinker_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_LeftBlinker_Out = DiagMessage(0xA9A4, 'UdsDiag_GetLight_LeftBlinker_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_LeftBlinker_Out.add_parameter(DiagParameter('Light_LeftBlinker_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_RearRoof_Out = DiagMessage(0xA9A8, 'UdsDiag_GetLight_RearRoof_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_RearRoof_Out.add_parameter(DiagParameter('Light_RearRoof_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_FrontRoof_Out = DiagMessage(0xA9A9, 'UdsDiag_GetLight_FrontRoof_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_FrontRoof_Out.add_parameter(DiagParameter('Light_FrontRoof_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_Step_Out = DiagMessage(0xA9AA, 'UdsDiag_GetLight_Step_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_Step_Out.add_parameter(DiagParameter('Light_Step_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_HandRail_Out = DiagMessage(0xA9AB, 'UdsDiag_GetLight_HandRail_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_HandRail_Out.add_parameter(DiagParameter('Light_HandRail_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_diurne_Out = DiagMessage(0xA9AC, 'UdsDiag_GetLight_diurne_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_diurne_Out.add_parameter(DiagParameter('Light_diurne_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_Fender_Out = DiagMessage(0xA9AD, 'UdsDiag_GetLight_Fender_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_Fender_Out.add_parameter(DiagParameter('Light_Fender_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_Beacon_Out = DiagMessage(0xA9AE, 'UdsDiag_GetLight_Beacon_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_Beacon_Out.add_parameter(DiagParameter('Light_Beacon_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_Hood_Out = DiagMessage(0xA9AF, 'UdsDiag_GetLight_Hood_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_Hood_Out.add_parameter(DiagParameter('Light_Hood_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_RoadHandRail_Out = DiagMessage(0xA9B0, 'UdsDiag_GetLight_RoadHandRail_Out', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_RoadHandRail_Out.add_parameter(DiagParameter('Light_RoadHandRail_OutState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetCab_DoorOpened_Sw = DiagMessage(0xA9DA, 'UdsDiag_GetCab_DoorOpened_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetCab_DoorOpened_Sw.add_parameter(DiagParameter('Cab_DoorOpened_Sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetLight_Warning_Input_Sw = DiagMessage(0xA9DB, 'UdsDiag_GetLight_Warning_Input_Sw', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetLight_Warning_Input_Sw.add_parameter(DiagParameter('Light_Warning_Input_Sw', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '', False, False, False))

    UdsDiag_GetISO11786_PTOspeed = DiagMessage(0xA9DC, 'UdsDiag_GetISO11786_PTOspeed', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO11786_PTOspeed.add_parameter(DiagParameter('ISO11786_PTOspeed', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'rpm', 0, 255, '', False, False, False))

    UdsDiag_GetISO11786_TheoricalSpeed = DiagMessage(0xA9DD, 'UdsDiag_GetISO11786_TheoricalSpeed', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO11786_TheoricalSpeed.add_parameter(DiagParameter('SO11786_TheoricalSpeed', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'm/s', 0, 255, '', False, False, False))

    UdsDiag_GetISO11786_RealSpeed = DiagMessage(0xA9DE, 'UdsDiag_GetISO11786_RealSpeed', [1, 3, 4, 64], None, '', 1)
    UdsDiag_GetISO11786_RealSpeed.add_parameter(DiagParameter('ISO11786_RealSpeed', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, 'm/s', 0, 255, '', False, False, False))

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

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [1, 2, 3, 4, 64], None, '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [1, 2, 3, 4, 64], None, '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [1, 2, 3, 4, 64], None, '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'INVALID': [48, 48], 'FELLA': [65, 65], 'CHALLENGER': [67, 67], 'FENDT': [70, 70], 'LAVERDA': [76, 76], 'MASSEY_FERGUSON': [77, 77], 'VALTRA': [86, 86], 'LELY': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class SRCIO_BVWriteDataSignals:
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

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [2, 3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'INVALID': [48, 48], 'FELLA': [65, 65], 'CHALLENGER': [67, 67], 'FENDT': [70, 70], 'LAVERDA': [76, 76], 'MASSEY_FERGUSON': [77, 77], 'VALTRA': [86, 86], 'LELY': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class SRCIO_BVIOControlDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [4], [4], '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))


SRCIO_BVDTCSnapshotdDids = {
}


class SRCIOClient(ECUClient):
    class FlashData(Enum):
        pass

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0x32, "SRCIO", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=6, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = SRCIO_BVReadDataSignals
        self.write_dids = SRCIO_BVWriteDataSignals
        self.routine_dids = SRCIO_BVRoutineIdentifierSignals
        self.io_dids = SRCIO_BVIOControlDataSignals
        self.dtc_snapshot_dids = SRCIO_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

