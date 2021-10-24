from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class CLUSTER_BVRoutineIdentifierSignals:
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


class CLUSTER_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

    TransactionID = DiagMessage(0x1100, 'TransactionID', [1, 3, 4, 64], None, '', 1)
    TransactionID.add_parameter(DiagParameter('TransactionID', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 4294967295, '', False, False, False))

    RID_StartSwitchIgnition = DiagMessage(0x1103, 'RID_StartSwitchIgnition', [1, 3, 4, 64], None, '', 1)
    RID_StartSwitchIgnition.add_parameter(DiagParameter('StartSwitchIgnition', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X152][3][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_AlternatorInput = DiagMessage(0x1106, 'RID_AlternatorInput', [1, 3, 4, 64], None, '', 1)
    RID_AlternatorInput.add_parameter(DiagParameter('AlternatorInput', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CHARGING': [0, 0], 'NOT_CHARGING': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X194][6][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_FuelGauge_Raw = DiagMessage(0x1107, 'RID_FuelGauge_Raw', [1, 3, 4, 64], None, '', 1)
    RID_FuelGauge_Raw.add_parameter(DiagParameter('FuelGauge_Raw', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'ohm', 0, 255, '[1][C2C3_20-C3_21][Miscellaneous][X197][7][Meca][Base][raw][DCC_CONTI][Y][1]', False, False, False))

    RID_EngineTemperatureSensor_Raw = DiagMessage(0x1108, 'RID_EngineTemperatureSensor_Raw', [1, 3, 4, 64], None, '', 1)
    RID_EngineTemperatureSensor_Raw.add_parameter(DiagParameter('EngineTemperatureSensor_Raw', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'ohm', 0, 255, '', False, False, False))

    RID_PowershuttleResponsePotentiometer_Raw = DiagMessage(0x1109, 'RID_PowershuttleResponsePotentiometer_Raw', [1, 3, 4, 64], None, '', 1)
    RID_PowershuttleResponsePotentiometer_Raw.add_parameter(DiagParameter('PowershuttleResponsePotentiometer_Raw', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))

    RID_TransportModeSwitch = DiagMessage(0x110A, 'RID_TransportModeSwitch', [1, 3, 4, 64], None, '', 1)
    RID_TransportModeSwitch.add_parameter(DiagParameter('TransportModeSwitch', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X933][10-IN-DIG_1][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_External_RearPTOSwitch = DiagMessage(0x110B, 'RID_External_RearPTOSwitch', [1, 3, 4, 64], None, '', 1)
    RID_External_RearPTOSwitch.add_parameter(DiagParameter('External_RearPTOSwitch', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X94][11-IN_DIG_2][Meca][Base][conv][DCC_CONTI][Y][2]', False, False, False))

    RID_Navigation_Switch = DiagMessage(0x110C, 'RID_Navigation_Switch', [1, 3, 4, 64], None, '', 4)
    RID_Navigation_Switch.add_parameter(DiagParameter('NavigationSwitchPlus', 1, 0, 0, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X743][12-IN_DIG_3][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))
    RID_Navigation_Switch.add_parameter(DiagParameter('NavigationSwitchMinus', 2, 0, 1, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X743][13-IN_DIG_4][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))
    RID_Navigation_Switch.add_parameter(DiagParameter('NavigationSwitchUp', 3, 0, 2, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X744][14-IN_DIG_5][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))
    RID_Navigation_Switch.add_parameter(DiagParameter('NavigationSwitchDown', 4, 0, 3, 1, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X744][15-IN_DIG_6][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_FuelGauge__Converted = DiagMessage(0x110D, 'RID_FuelGauge__Converted', [1, 3, 4, 64], None, '', 1)
    RID_FuelGauge__Converted.add_parameter(DiagParameter('FuelGauge_Converted', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '%', 0, 100, '[1][C2C3_20-C3_21][Miscellaneous][X197][7][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_EngineTemperatureSensor_Converted = DiagMessage(0x110E, 'RID_EngineTemperatureSensor_Converted', [1, 3, 4, 64], None, '', 1)
    RID_EngineTemperatureSensor_Converted.add_parameter(DiagParameter('EngineTemperatureSensor_Converted', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '?C', 0, 255, '[1][C2C3_20-C3_21][Miscellaneous][X799][8-IN_ANA_5][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_PowershuttleResponsePotentiometer_Converted = DiagMessage(0x110F, 'RID_PowershuttleResponsePotentiometer_Converted', [1, 3, 4, 64], None, '', 1)
    RID_PowershuttleResponsePotentiometer_Converted.add_parameter(DiagParameter('PowershuttleResponsePotentiometer_Converted', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '[1][C2C3_20-C3_21][Cab_commands][X747][9-IN_ANA_6][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_TrailerBrakeDefaultFromABS = DiagMessage(0x1110, 'RID_TrailerBrakeDefaultFromABS', [1, 3, 4, 64], None, '', 1)
    RID_TrailerBrakeDefaultFromABS.add_parameter(DiagParameter('TrailerBrakeDefaultFromABS', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Braking_system][X990][16-IN_DIG_21][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_RearHandSideLight_BrakeLightAndDirectionIndicator = DiagMessage(0x1111, 'RID_RearHandSideLight_BrakeLightAndDirectionIndicator', [1, 3, 4, 64], None, '', 1)
    RID_RearHandSideLight_BrakeLightAndDirectionIndicator.add_parameter(DiagParameter('RearHandSideLight_BrakeLightAndDirectionIndicator', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X77][17][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_AudibleAlarmControl = DiagMessage(0x1113, 'RID_AudibleAlarmControl', [1, 3, 4, 64], None, '', 1)
    RID_AudibleAlarmControl.add_parameter(DiagParameter('AudibleAlarmControl', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X73][19][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_4WDSwitch = DiagMessage(0x1114, 'RID_4WDSwitch', [1, 3, 4, 64], None, '', 1)
    RID_4WDSwitch.add_parameter(DiagParameter('4WDSwitch', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X137][20-IN_DIG_8][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_DifflockSwitch = DiagMessage(0x1115, 'RID_DifflockSwitch', [1, 3, 4, 64], None, '', 1)
    RID_DifflockSwitch.add_parameter(DiagParameter('DifflockSwitch', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X136][21-IN_DIG_9][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_PneumaticTrailerBrakingTestSensor = DiagMessage(0x1116, 'RID_PneumaticTrailerBrakingTestSensor', [1, 3, 4, 64], None, '', 1)
    RID_PneumaticTrailerBrakingTestSensor.add_parameter(DiagParameter('PneumaticTrailerBrakingTestSensor', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Braking_system][X996][22-IN_DIG_22][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_TransmissionOilFilterSensor = DiagMessage(0x1117, 'RID_TransmissionOilFilterSensor', [1, 3, 4, 64], None, '', 1)
    RID_TransmissionOilFilterSensor.add_parameter(DiagParameter('TransmissionOilFilterSensor', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Transmission][X20][23-IN_DIG_10][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_AirFilter = DiagMessage(0x1118, 'RID_AirFilter', [1, 3, 4, 64], None, '', 1)
    RID_AirFilter.add_parameter(DiagParameter('AirFilter', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CLEAN': [0, 0], 'CLOGGED': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X253][24-IN_DIG_23][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_Lubrication5b_Switch17Bar = DiagMessage(0x1119, 'RID_Lubrication5b_Switch17Bar', [1, 3, 4, 64], None, '', 1)
    RID_Lubrication5b_Switch17Bar.add_parameter(DiagParameter('Lubrication5b_Switch17Bar', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Transmission][X493][25-IN_DIG_11][Meca][Base][conv][DCC_CONTI][Y][1]#[1][C2C3_20-C3_21][Transmission][X494][25-IN_DIG_11][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_HandBrakeSwitch = DiagMessage(0x111A, 'RID_HandBrakeSwitch', [1, 3, 4, 64], None, '', 1)
    RID_HandBrakeSwitch.add_parameter(DiagParameter('HandBrakeSwitch', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X618][26-IN_DIG_12][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_SeatSwitch = DiagMessage(0x111B, 'RID_SeatSwitch', [1, 3, 4, 64], None, '', 1)
    RID_SeatSwitch.add_parameter(DiagParameter('SeatSwitch', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X470][27-IN_DIG_13][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_PneumaticPressureSensor = DiagMessage(0x111C, 'RID_PneumaticPressureSensor', [1, 3, 4, 64], None, '', 1)
    RID_PneumaticPressureSensor.add_parameter(DiagParameter('PneumaticPressureSensor', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Braking_system][X168][28-IN_DIG_14][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_LeftTurnLight = DiagMessage(0x111D, 'RID_LeftTurnLight', [1, 3, 4, 64], None, '', 1)
    RID_LeftTurnLight.add_parameter(DiagParameter('LeftTurnLight', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X652][29-IN_DIG_15][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_RightTurnLight = DiagMessage(0x111E, 'RID_RightTurnLight', [1, 3, 4, 64], None, '', 1)
    RID_RightTurnLight.add_parameter(DiagParameter('RightTurnLight', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X652][30-IN_DIG_16][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_HighBeamLight = DiagMessage(0x111F, 'RID_HighBeamLight', [1, 3, 4, 64], None, '', 1)
    RID_HighBeamLight.add_parameter(DiagParameter('HighBeamLight', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X926][31-IN_DIG_17][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_PneumaticTrailerBrakeCutOutSwitch = DiagMessage(0x1120, 'RID_PneumaticTrailerBrakeCutOutSwitch', [1, 3, 4, 64], None, '', 1)
    RID_PneumaticTrailerBrakeCutOutSwitch.add_parameter(DiagParameter('PneumaticTrailerBrakeCutOutSwitch', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X1007][32-IN-DIG_18][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_Trailer = DiagMessage(0x1121, 'RID_Trailer', [1, 3, 4, 64], None, '', 1)
    RID_Trailer.add_parameter(DiagParameter('Trailer', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Miscellaneous][X652][33-IN_DIG_19][Meca][Base][conv][DCC_CONTI][Y][2]', False, False, False))

    RID_CreeperSwitch = DiagMessage(0x1122, 'RID_CreeperSwitch', [1, 3, 4, 64], None, '', 1)
    RID_CreeperSwitch.add_parameter(DiagParameter('CreeperSwitch', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OPEN': [0, 0], 'CLOSE': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Cab_commands][X603-E][34-IN_DIG_20][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_FourWD = DiagMessage(0x112A, 'RID_FourWD', [1, 3, 4, 64], None, '', 1)
    RID_FourWD.add_parameter(DiagParameter('4WDStateMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [1, 1], 'MANUAL': [2, 2], 'AUTO': [3, 3], 'OVERSPEED': [4, 4], 'ERROR': [5, 5]}, 1, 5, '[1][C2C3_20-C3_21][Functions_state][ ][ ][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_Difflock = DiagMessage(0x112B, 'RID_Difflock', [1, 3, 4, 64], None, '', 1)
    RID_Difflock.add_parameter(DiagParameter('DifflockStateMode', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [1, 1], 'MANUAL': [2, 2], 'ERROR': [3, 3]}, 1, 3, '[1][C2C3_20-C3_21][Functions_state][ ][ ][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_Brake_State = DiagMessage(0x112C, 'RID_Brake_State', [1, 3, 4, 64], None, '', 1)
    RID_Brake_State.add_parameter(DiagParameter('BrakeToNeutralState', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1], 'DISABLED': [2, 2], 'NOTPRESENT': [255, 255]}, 0, 255, '[1][C2C3_20-C3_21][Functions_state][ ][ ][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    RID_Brake_Rqst = DiagMessage(0x112D, 'RID_Brake_Rqst', [1, 3, 4, 64], None, '', 1)
    RID_Brake_Rqst.add_parameter(DiagParameter('BrakeToNeutralRqst', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'OFF': [0, 0], 'ON': [1, 1]}, 0, 1, '[1][C2C3_20-C3_21][Functions_state][ ][ ][Meca][Base][conv][DCC_CONTI][Y][1]', False, False, False))

    EngineHours = DiagMessage(0x13DE, 'EngineHours', [], None, '', 1)
    EngineHours.add_parameter(DiagParameter('EngineHours', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 65535, '', False, False, False))

    NextMaintenance = DiagMessage(0x13E1, 'NextMaintenance', [], None, '', 1)
    NextMaintenance.add_parameter(DiagParameter('NextMaintenance', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 65535, '', False, False, False))

    NextMaintenanceInterval = DiagMessage(0x13E2, 'NextMaintenanceInterval', [], None, '', 1)
    NextMaintenanceInterval.add_parameter(DiagParameter('NextMaintenanceInterval', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 65535, '', False, False, False))

    HYDRAULIC_PUMP_CAPACITY = DiagMessage(0xF010, 'HYDRAULIC_PUMP_CAPACITY', [], None, '', 1)
    HYDRAULIC_PUMP_CAPACITY.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    PIN_SENSING_CAPACITY = DiagMessage(0xF011, 'PIN_SENSING_CAPACITY', [], None, '', 1)
    PIN_SENSING_CAPACITY.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    NB_EFFORT_BAR = DiagMessage(0xF012, 'NB_EFFORT_BAR', [], None, '', 1)
    NB_EFFORT_BAR.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    POT_INTERMIX_SETPOINT = DiagMessage(0xF013, 'POT_INTERMIX_SETPOINT', [], None, '', 1)
    POT_INTERMIX_SETPOINT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    DIAMETER_CYLINDER = DiagMessage(0xF014, 'DIAMETER_CYLINDER', [], None, '', 1)
    DIAMETER_CYLINDER.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    DRAFT_CTRL_SENSORS = DiagMessage(0xF015, 'DRAFT_CTRL_SENSORS', [], None, '', 1)
    DRAFT_CTRL_SENSORS.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    GPA_TYPE = DiagMessage(0xF016, 'GPA_TYPE', [], None, '', 1)
    GPA_TYPE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    FOUR_WD = DiagMessage(0xF017, 'FOUR_WD', [], None, '', 1)
    FOUR_WD.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    DAMPING_SWITCH_ATC = DiagMessage(0xF018, 'DAMPING_SWITCH_ATC', [], None, '', 1)
    DAMPING_SWITCH_ATC.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    POT_HIGH_POSITION_SETPOINT = DiagMessage(0xF019, 'POT_HIGH_POSITION_SETPOINT', [], None, '', 1)
    POT_HIGH_POSITION_SETPOINT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    POT_SINK_SPEED_SETPOINT = DiagMessage(0xF01A, 'POT_SINK_SPEED_SETPOINT', [], None, '', 1)
    POT_SINK_SPEED_SETPOINT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    SWITCH_3P_HITCHING = DiagMessage(0xF01B, 'SWITCH_3P_HITCHING', [], None, '', 1)
    SWITCH_3P_HITCHING.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    TYPE_INTERMIX = DiagMessage(0xF01C, 'TYPE_INTERMIX', [], None, '', 1)
    TYPE_INTERMIX.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    GB_TAXLE = DiagMessage(0xF01D, 'GB_TAXLE', [], None, '', 1)
    GB_TAXLE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    EXT_CMD_BUTTONS = DiagMessage(0xF01E, 'EXT_CMD_BUTTONS', [], None, '', 1)
    EXT_CMD_BUTTONS.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    PTO_REAR_GSPTO = DiagMessage(0xF01F, 'PTO_REAR_GSPTO', [], None, '', 1)
    PTO_REAR_GSPTO.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'F', False, False, False))

    MOTHER_REGULATION = DiagMessage(0xF020, 'MOTHER_REGULATION', [], None, '', 1)
    MOTHER_REGULATION.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    PTO_REAR_540 = DiagMessage(0xF021, 'PTO_REAR_540', [], None, '', 1)
    PTO_REAR_540.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'F', False, False, False))

    PTO_REAR_540E = DiagMessage(0xF022, 'PTO_REAR_540E', [], None, '', 1)
    PTO_REAR_540E.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'F', False, False, False))

    PTO_REAR_1000 = DiagMessage(0xF023, 'PTO_REAR_1000', [], None, '', 1)
    PTO_REAR_1000.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'F', False, False, False))

    PTO_SETTING = DiagMessage(0xF024, 'PTO_SETTING', [], None, '', 1)
    PTO_SETTING.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    PTO_TYPE = DiagMessage(0xF025, 'PTO_TYPE', [], None, '', 1)
    PTO_TYPE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    NB_TEETH_GEAR_WHEEL = DiagMessage(0xF026, 'NB_TEETH_GEAR_WHEEL', [], None, '', 1)
    NB_TEETH_GEAR_WHEEL.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    PTO_MODE = DiagMessage(0xF027, 'PTO_MODE', [], None, '', 1)
    PTO_MODE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    NB_TEETH_ISC = DiagMessage(0xF028, 'NB_TEETH_ISC', [], None, '', 1)
    NB_TEETH_ISC.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    ABSENCE_ISC = DiagMessage(0xF029, 'ABSENCE_ISC', [], None, '', 1)
    ABSENCE_ISC.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    FNR_BRAND = DiagMessage(0xF02A, 'FNR_BRAND', [], None, '', 1)
    FNR_BRAND.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    CREEPER = DiagMessage(0xF02B, 'CREEPER', [], None, '', 1)
    CREEPER.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    FINAL_REDUCTION = DiagMessage(0xF02C, 'FINAL_REDUCTION', [], None, '', 1)
    FINAL_REDUCTION.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    BRAKE_TO_NEUTRAL = DiagMessage(0xF02D, 'BRAKE_TO_NEUTRAL', [], None, '', 1)
    BRAKE_TO_NEUTRAL.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    ENGINE_EMISSION_LEVEL = DiagMessage(0xF02E, 'ENGINE_EMISSION_LEVEL', [], None, '', 1)
    ENGINE_EMISSION_LEVEL.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'F', False, False, False))

    FOUR_WHEEL_DRIVE_MODE_US = DiagMessage(0xF02F, 'FOUR_WHEEL_DRIVE_MODE_US', [], None, '', 1)
    FOUR_WHEEL_DRIVE_MODE_US.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    MAXIMUM_VEHICLE_SPEED = DiagMessage(0xF030, 'MAXIMUM_VEHICLE_SPEED', [], None, '', 1)
    MAXIMUM_VEHICLE_SPEED.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'F,M', False, False, False))

    WITH_CABIN = DiagMessage(0xF031, 'WITH_CABIN', [], None, '', 1)
    WITH_CABIN.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    POWERSHUTTLE = DiagMessage(0xF032, 'POWERSHUTTLE', [], None, '', 1)
    POWERSHUTTLE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    UNIT_VOLUME_MF = DiagMessage(0xF033, 'UNIT_VOLUME_MF', [], None, '', 1)
    UNIT_VOLUME_MF.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    HYD_TRAILER_BRAKE = DiagMessage(0xF034, 'HYD_TRAILER_BRAKE', [], None, '', 1)
    HYD_TRAILER_BRAKE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    PNEU_TRAILER_BRAKE = DiagMessage(0xF035, 'PNEU_TRAILER_BRAKE', [], None, '', 1)
    PNEU_TRAILER_BRAKE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    ENGINE_SPEED_MEMORY = DiagMessage(0xF036, 'ENGINE_SPEED_MEMORY', [], None, '', 1)
    ENGINE_SPEED_MEMORY.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    ENGINE_CURVE_STRATEGY = DiagMessage(0xF037, 'ENGINE_CURVE_STRATEGY', [], None, '', 1)
    ENGINE_CURVE_STRATEGY.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    HELP_DATA1_LANGUAGE = DiagMessage(0xF038, 'HELP_DATA1_LANGUAGE', [], None, '', 1)
    HELP_DATA1_LANGUAGE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'F', False, False, False))

    WHEEL_CIRCUMFERENCE_SPECIAL = DiagMessage(0xF039, 'WHEEL_CIRCUMFERENCE_SPECIAL', [], None, '', 1)
    WHEEL_CIRCUMFERENCE_SPECIAL.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 65535, 'M,V', False, False, False))

    MAX_WHEEL_CIRCUMFERENCE = DiagMessage(0xF03A, 'MAX_WHEEL_CIRCUMFERENCE', [], None, '', 1)
    MAX_WHEEL_CIRCUMFERENCE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 65535, 'F', False, False, False))

    TWO_PS_OPTION = DiagMessage(0xF03B, 'TWO_PS_OPTION', [], None, '', 1)
    TWO_PS_OPTION.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    SPEED_OFFSET_ACTIVATION = DiagMessage(0xF03C, 'SPEED_OFFSET_ACTIVATION', [], None, '', 1)
    SPEED_OFFSET_ACTIVATION.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    PTO_REAR_SPTO_TYPE = DiagMessage(0xF03D, 'PTO_REAR_SPTO_TYPE', [], None, '', 1)
    PTO_REAR_SPTO_TYPE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    PTO_REAR_1000E = DiagMessage(0xF03E, 'PTO_REAR_1000E', [], None, '', 1)
    PTO_REAR_1000E.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    THREE_PT_REAR_FENDER_SW_LEFT = DiagMessage(0xF03F, 'THREE_PT_REAR_FENDER_SW_LEFT', [], None, '', 1)
    THREE_PT_REAR_FENDER_SW_LEFT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    THREE_PT_REAR_FENDER_SW_RIGHT = DiagMessage(0xF040, 'THREE_PT_REAR_FENDER_SW_RIGHT', [], None, '', 1)
    THREE_PT_REAR_FENDER_SW_RIGHT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M, V', False, False, False))

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

    ExhaustRegulationOrTypeApprovalNumber = DiagMessage(0xF196, 'ExhaustRegulationOrTypeApprovalNumber', [], None, '', 1)
    ExhaustRegulationOrTypeApprovalNumber.add_parameter(DiagParameter('tbd', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '(all 0xFF --> "INVALID")', False, False, False))

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
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))

    UDSVersionDataIdentifier = DiagMessage(0xFF00, 'UDSVersionDataIdentifier', [1, 3, 4, 64], None, '', 4)
    UDSVersionDataIdentifier.add_parameter(DiagParameter('Major', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    UDSVersionDataIdentifier.add_parameter(DiagParameter('Minor', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    UDSVersionDataIdentifier.add_parameter(DiagParameter('Revision', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    UDSVersionDataIdentifier.add_parameter(DiagParameter('Build', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))


class CLUSTER_BVWriteDataSignals:
    TransactionID = DiagMessage(0x1100, 'TransactionID', [], None, '', 1)
    TransactionID.add_parameter(DiagParameter('TransactionID', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 4294967295, '', False, False, False))

    EngineHours = DiagMessage(0x13DE, 'EngineHours', [], None, '', 1)
    EngineHours.add_parameter(DiagParameter('EngineHours', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 65535, '', False, False, False))

    NextMaintenance = DiagMessage(0x13E1, 'NextMaintenance', [], None, '', 1)
    NextMaintenance.add_parameter(DiagParameter('NextMaintenance', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 65535, '', False, False, False))

    NextMaintenanceInterval = DiagMessage(0x13E2, 'NextMaintenanceInterval', [], None, '', 1)
    NextMaintenanceInterval.add_parameter(DiagParameter('NextMaintenanceInterval', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'h', 0, 65535, '', False, False, False))

    HYDRAULIC_PUMP_CAPACITY = DiagMessage(0xF010, 'HYDRAULIC_PUMP_CAPACITY', [], None, '', 1)
    HYDRAULIC_PUMP_CAPACITY.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    PIN_SENSING_CAPACITY = DiagMessage(0xF011, 'PIN_SENSING_CAPACITY', [], None, '', 1)
    PIN_SENSING_CAPACITY.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    NB_EFFORT_BAR = DiagMessage(0xF012, 'NB_EFFORT_BAR', [], None, '', 1)
    NB_EFFORT_BAR.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    POT_INTERMIX_SETPOINT = DiagMessage(0xF013, 'POT_INTERMIX_SETPOINT', [], None, '', 1)
    POT_INTERMIX_SETPOINT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    DIAMETER_CYLINDER = DiagMessage(0xF014, 'DIAMETER_CYLINDER', [], None, '', 1)
    DIAMETER_CYLINDER.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    DRAFT_CTRL_SENSORS = DiagMessage(0xF015, 'DRAFT_CTRL_SENSORS', [], None, '', 1)
    DRAFT_CTRL_SENSORS.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    GPA_TYPE = DiagMessage(0xF016, 'GPA_TYPE', [], None, '', 1)
    GPA_TYPE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    FOUR_WD = DiagMessage(0xF017, 'FOUR_WD', [], None, '', 1)
    FOUR_WD.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    DAMPING_SWITCH_ATC = DiagMessage(0xF018, 'DAMPING_SWITCH_ATC', [], None, '', 1)
    DAMPING_SWITCH_ATC.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    POT_HIGH_POSITION_SETPOINT = DiagMessage(0xF019, 'POT_HIGH_POSITION_SETPOINT', [], None, '', 1)
    POT_HIGH_POSITION_SETPOINT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    POT_SINK_SPEED_SETPOINT = DiagMessage(0xF01A, 'POT_SINK_SPEED_SETPOINT', [], None, '', 1)
    POT_SINK_SPEED_SETPOINT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    SWITCH_3P_HITCHING = DiagMessage(0xF01B, 'SWITCH_3P_HITCHING', [], None, '', 1)
    SWITCH_3P_HITCHING.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    TYPE_INTERMIX = DiagMessage(0xF01C, 'TYPE_INTERMIX', [], None, '', 1)
    TYPE_INTERMIX.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    GB_TAXLE = DiagMessage(0xF01D, 'GB_TAXLE', [], None, '', 1)
    GB_TAXLE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    EXT_CMD_BUTTONS = DiagMessage(0xF01E, 'EXT_CMD_BUTTONS', [], None, '', 1)
    EXT_CMD_BUTTONS.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    PTO_REAR_GSPTO = DiagMessage(0xF01F, 'PTO_REAR_GSPTO', [], None, '', 1)
    PTO_REAR_GSPTO.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'F', False, False, False))

    MOTHER_REGULATION = DiagMessage(0xF020, 'MOTHER_REGULATION', [], None, '', 1)
    MOTHER_REGULATION.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    PTO_REAR_540 = DiagMessage(0xF021, 'PTO_REAR_540', [], None, '', 1)
    PTO_REAR_540.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'F', False, False, False))

    PTO_REAR_540E = DiagMessage(0xF022, 'PTO_REAR_540E', [], None, '', 1)
    PTO_REAR_540E.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'F', False, False, False))

    PTO_REAR_1000 = DiagMessage(0xF023, 'PTO_REAR_1000', [], None, '', 1)
    PTO_REAR_1000.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'F', False, False, False))

    PTO_SETTING = DiagMessage(0xF024, 'PTO_SETTING', [], None, '', 1)
    PTO_SETTING.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    PTO_TYPE = DiagMessage(0xF025, 'PTO_TYPE', [], None, '', 1)
    PTO_TYPE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    NB_TEETH_GEAR_WHEEL = DiagMessage(0xF026, 'NB_TEETH_GEAR_WHEEL', [], None, '', 1)
    NB_TEETH_GEAR_WHEEL.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    PTO_MODE = DiagMessage(0xF027, 'PTO_MODE', [], None, '', 1)
    PTO_MODE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    NB_TEETH_ISC = DiagMessage(0xF028, 'NB_TEETH_ISC', [], None, '', 1)
    NB_TEETH_ISC.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    ABSENCE_ISC = DiagMessage(0xF029, 'ABSENCE_ISC', [], None, '', 1)
    ABSENCE_ISC.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    FNR_BRAND = DiagMessage(0xF02A, 'FNR_BRAND', [], None, '', 1)
    FNR_BRAND.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    CREEPER = DiagMessage(0xF02B, 'CREEPER', [], None, '', 1)
    CREEPER.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    FINAL_REDUCTION = DiagMessage(0xF02C, 'FINAL_REDUCTION', [], None, '', 1)
    FINAL_REDUCTION.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    BRAKE_TO_NEUTRAL = DiagMessage(0xF02D, 'BRAKE_TO_NEUTRAL', [], None, '', 1)
    BRAKE_TO_NEUTRAL.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    ENGINE_EMISSION_LEVEL = DiagMessage(0xF02E, 'ENGINE_EMISSION_LEVEL', [], None, '', 1)
    ENGINE_EMISSION_LEVEL.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'F', False, False, False))

    FOUR_WHEEL_DRIVE_MODE_US = DiagMessage(0xF02F, 'FOUR_WHEEL_DRIVE_MODE_US', [], None, '', 1)
    FOUR_WHEEL_DRIVE_MODE_US.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    MAXIMUM_VEHICLE_SPEED = DiagMessage(0xF030, 'MAXIMUM_VEHICLE_SPEED', [], None, '', 1)
    MAXIMUM_VEHICLE_SPEED.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'F,M', False, False, False))

    WITH_CABIN = DiagMessage(0xF031, 'WITH_CABIN', [], None, '', 1)
    WITH_CABIN.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    POWERSHUTTLE = DiagMessage(0xF032, 'POWERSHUTTLE', [], None, '', 1)
    POWERSHUTTLE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    UNIT_VOLUME_MF = DiagMessage(0xF033, 'UNIT_VOLUME_MF', [], None, '', 1)
    UNIT_VOLUME_MF.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    HYD_TRAILER_BRAKE = DiagMessage(0xF034, 'HYD_TRAILER_BRAKE', [], None, '', 1)
    HYD_TRAILER_BRAKE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    PNEU_TRAILER_BRAKE = DiagMessage(0xF035, 'PNEU_TRAILER_BRAKE', [], None, '', 1)
    PNEU_TRAILER_BRAKE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M,V', False, False, False))

    ENGINE_SPEED_MEMORY = DiagMessage(0xF036, 'ENGINE_SPEED_MEMORY', [], None, '', 1)
    ENGINE_SPEED_MEMORY.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M', False, False, False))

    ENGINE_CURVE_STRATEGY = DiagMessage(0xF037, 'ENGINE_CURVE_STRATEGY', [], None, '', 1)
    ENGINE_CURVE_STRATEGY.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, 'M', False, False, False))

    HELP_DATA1_LANGUAGE = DiagMessage(0xF038, 'HELP_DATA1_LANGUAGE', [], None, '', 1)
    HELP_DATA1_LANGUAGE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'F', False, False, False))

    WHEEL_CIRCUMFERENCE_SPECIAL = DiagMessage(0xF039, 'WHEEL_CIRCUMFERENCE_SPECIAL', [], None, '', 1)
    WHEEL_CIRCUMFERENCE_SPECIAL.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 65535, 'M,V', False, False, False))

    MAX_WHEEL_CIRCUMFERENCE = DiagMessage(0xF03A, 'MAX_WHEEL_CIRCUMFERENCE', [], None, '', 1)
    MAX_WHEEL_CIRCUMFERENCE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 65535, 'F', False, False, False))

    TWO_PS_OPTION = DiagMessage(0xF03B, 'TWO_PS_OPTION', [], None, '', 1)
    TWO_PS_OPTION.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    SPEED_OFFSET_ACTIVATION = DiagMessage(0xF03C, 'SPEED_OFFSET_ACTIVATION', [], None, '', 1)
    SPEED_OFFSET_ACTIVATION.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    PTO_REAR_SPTO_TYPE = DiagMessage(0xF03D, 'PTO_REAR_SPTO_TYPE', [], None, '', 1)
    PTO_REAR_SPTO_TYPE.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    PTO_REAR_1000E = DiagMessage(0xF03E, 'PTO_REAR_1000E', [], None, '', 1)
    PTO_REAR_1000E.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    THREE_PT_REAR_FENDER_SW_LEFT = DiagMessage(0xF03F, 'THREE_PT_REAR_FENDER_SW_LEFT', [], None, '', 1)
    THREE_PT_REAR_FENDER_SW_LEFT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M,V', False, False, False))

    THREE_PT_REAR_FENDER_SW_RIGHT = DiagMessage(0xF040, 'THREE_PT_REAR_FENDER_SW_RIGHT', [], None, '', 1)
    THREE_PT_REAR_FENDER_SW_RIGHT.add_parameter(DiagParameter('Feature_Value', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 1, 'M, V', False, False, False))

    DeleteFeature = DiagMessage(0xF0FF, 'DeleteFeature', [], None, '', 1)
    DeleteFeature.add_parameter(DiagParameter('DeleteFeature', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 4294967295, '', False, False, False))

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

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))

    VehiclePlatform = DiagMessage(0xF1A9, 'VehiclePlatform', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehiclePlatform.add_parameter(DiagParameter('VehiclePlatform', 1, 0, 0, 40, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, 'e.g. "M219P" (all 0xFF --> "INVAL")', False, False, False))

    VehicleBrand = DiagMessage(0xF1AA, 'VehicleBrand', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleBrand.add_parameter(DiagParameter('VehicleBrand', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'-': [48, 48], 'A': [65, 65], 'C': [67, 67], 'F': [70, 70], 'L': [76, 76], 'M': [77, 77], 'V': [86, 86], 'Y': [89, 89]}, 48, 89, '1 Ascii Char: "F" = Fendt, "M" = Massey, "V" = Valtra, etc ("0" (Ascii 0x30) --> invalid Brand)', False, False, False))


class CLUSTER_BVIOControlDataSignals:
    pass


CLUSTER_BVDTCSnapshotdDids = {
}


class CLUSTERClient(ECUClient):
    class FlashData(Enum):
        pass

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0x18, "CLUSTER", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=6, switch_session_wait_time=0.0,
                         boot_time_min=0, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = CLUSTER_BVReadDataSignals
        self.write_dids = CLUSTER_BVWriteDataSignals
        self.routine_dids = CLUSTER_BVRoutineIdentifierSignals
        self.io_dids = CLUSTER_BVIOControlDataSignals
        self.dtc_snapshot_dids = CLUSTER_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

