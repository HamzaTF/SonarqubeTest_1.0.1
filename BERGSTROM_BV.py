from agcolib.NetworkFunctions.can.client.uds_client import UDSConnection
from agcolib.NetworkFunctions.uds.client import ECUClient
from agcolib.NetworkFunctions.uds import DiagMessage, DiagParameter, MemoryLocation, SignalType, SignalConversion, SignalByteOrder, SignalScaleLinear, IntervalType, SignalTabIntp
from enum import Enum
from copy import deepcopy


class BERGSTROM_BVRoutineIdentifierSignals:
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
    EraseMemoryRequest.add_parameter(DiagParameter('MemoryAddress', 3, 1, 0, 24, SignalByteOrder.Motorola, SignalType.BYTEFIELD, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, '', False, False, False))
    EraseMemoryRequest.add_parameter(DiagParameter('MemorySize', 4, 4, 0, 24, SignalByteOrder.Motorola, SignalType.BYTEFIELD, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, '', False, False, False))

    EraseMemoryResponse = DiagMessage(0xFF00, 'EraseMemoryResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    EraseMemoryResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'PASSED': [0, 0], 'FAILED': [1, 1]}, 0, 1, '', False, False, False))

    CheckProgrammingDependenciesRequest = DiagMessage(0xFF01, 'CheckProgrammingDependenciesRequest', [2], [1, 3, 4, 5], '', 0)

    CheckProgrammingDependenciesResponse = DiagMessage(0xFF01, 'CheckProgrammingDependenciesResponse', [1, 2, 3, 4, 64, 65], None, '', 1)
    CheckProgrammingDependenciesResponse.add_parameter(DiagParameter('RoutineInfo', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'CORRECT_RESULT': [0, 0], 'INCORRECT_RESULT': [1, 1], 'INCORRECT_RESULT_ERROR_SW_HW': [2, 2], 'INCORRECT_RESULT_ERROR_SW_SW': [3, 3], 'INCORRECT_RESULT_ONE_OR_MORE_BLOCKS_NOT_PROGRAMMED': [4, 4]}, 0, 4, '', False, False, False))


class BERGSTROM_BVReadDataSignals:
    BatteryPotential = DiagMessage(0x0100, 'BatteryPotential', [1, 3, 4, 64], None, '', 1)
    BatteryPotential.add_parameter(DiagParameter('BatteryPotential', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.05, 'V', 0, 3212.75, '', False, False, False))

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

    VehicleManufacturerECUSoftwareNumber = DiagMessage(0xF188, 'VehicleManufacturerECUSoftwareNumber', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerECUSoftwareNumber.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    VehicleManufacturerECUSoftwareVersionNumber = DiagMessage(0xF189, 'VehicleManufacturerECUSoftwareVersionNumber', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerECUSoftwareVersionNumber.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    SystemSupplierIdentifierData = DiagMessage(0xF18A, 'SystemSupplierIdentifierData', [1, 3, 4, 64], None, '', 1)
    SystemSupplierIdentifierData.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'System Supplier Name', False, False, False))

    EcuManufacturingDate = DiagMessage(0xF18B, 'EcuManufacturingDate', [1, 3, 4, 64], None, '', 3)
    EcuManufacturingDate.add_parameter(DiagParameter('ManufacturingYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    EcuManufacturingDate.add_parameter(DiagParameter('ManufacturingMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    EcuManufacturingDate.add_parameter(DiagParameter('ManufacturingDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))

    EcuSerialNumber = DiagMessage(0xF18C, 'EcuSerialNumber', [1, 2, 3, 4, 64], None, '', 1)
    EcuSerialNumber.add_parameter(DiagParameter('SerialNumber', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 32 bytes allowed (all 0xFF --> "INVALID")', False, False, False))

    SupportedFunctionalUnits = DiagMessage(0xF18D, 'SupportedFunctionalUnits', [1, 3, 4, 64], None, '', 1)
    SupportedFunctionalUnits.add_parameter(DiagParameter('Number', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 4294967295, '', False, False, False))

    VehicleManufacturerKitAssemblyPartNumber = DiagMessage(0xF18E, 'VehicleManufacturerKitAssemblyPartNumber', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerKitAssemblyPartNumber.add_parameter(DiagParameter('AssemblyPartNumber', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Partnumber of a complete Assembly e.g. G-Nr (all 0xFF --> "INVALID")', False, False, False))

    VehicleIdentificationNumber = DiagMessage(0xF190, 'VehicleIdentificationNumber', [1, 2, 3, 4, 64, 65], None, '', 1)
    VehicleIdentificationNumber.add_parameter(DiagParameter('VinNumber', 1, 0, 0, 136, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '17 bytes fixed length (all 0xFF --> "INVALID")', False, False, False))

    VehicleManufacturerECUHardwareNumber = DiagMessage(0xF191, 'VehicleManufacturerECUHardwareNumber', [1, 2, 3, 4, 64, 65], None, '', 1)
    VehicleManufacturerECUHardwareNumber.add_parameter(DiagParameter('VirtualPartNumber', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 4293918720, 4294967295, 'Unique feature identifier (mandatory for compatibility check hardware/software at ECU programming) ', False, False, False))

    SystemSupplierECUHardwareNumber = DiagMessage(0xF192, 'SystemSupplierECUHardwareNumber', [1, 3, 4, 64], None, '', 1)
    SystemSupplierECUHardwareNumber.add_parameter(DiagParameter('HardwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    SystemSupplierECUHardwareVersionNumber = DiagMessage(0xF193, 'SystemSupplierECUHardwareVersionNumber', [1, 3, 4, 64], None, '', 1)
    SystemSupplierECUHardwareVersionNumber.add_parameter(DiagParameter('SystemSupplierHardwareVersion', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '(optional used by ECU supplier)', False, False, False))

    SystemSupplierECUSoftwareNumber = DiagMessage(0xF194, 'SystemSupplierECUSoftwareNumber', [1, 3, 4, 64], None, '', 1)
    SystemSupplierECUSoftwareNumber.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    SystemSupplierECUSoftwareVersionNumber = DiagMessage(0xF195, 'SystemSupplierECUSoftwareVersionNumber', [1, 3, 4, 64], None, '', 1)
    SystemSupplierECUSoftwareVersionNumber.add_parameter(DiagParameter('SystemSupplierSoftwareVersion', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    SystemNameOrEngineType = DiagMessage(0xF197, 'SystemNameOrEngineType', [1, 3, 4, 64], None, '', 1)
    SystemNameOrEngineType.add_parameter(DiagParameter('SystemName', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'e.g. "Infotainment"', False, False, False))

    RepairShopCodeOrTesterSerialNumber = DiagMessage(0xF198, 'RepairShopCodeOrTesterSerialNumber', [1, 3, 4, 64], None, '', 1)
    RepairShopCodeOrTesterSerialNumber.add_parameter(DiagParameter('TesterSerialNumber', 1, 0, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    ProgrammingDate = DiagMessage(0xF199, 'ProgrammingDate', [1, 3, 4, 64], None, '', 3)
    ProgrammingDate.add_parameter(DiagParameter('ProgrammingYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    ProgrammingDate.add_parameter(DiagParameter('ProgrammingMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    ProgrammingDate.add_parameter(DiagParameter('ProgrammingDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))

    CalibrationRepairShopCodeOrCalibrationEquipmentSerialNumber = DiagMessage(0xF19A, 'CalibrationRepairShopCodeOrCalibrationEquipmentSerialNumber', [], None, '', 1)
    CalibrationRepairShopCodeOrCalibrationEquipmentSerialNumber.add_parameter(DiagParameter('SerialNumber', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    CalibrationDate = DiagMessage(0xF19B, 'CalibrationDate', [], None, '', 3)
    CalibrationDate.add_parameter(DiagParameter('CalibrationYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    CalibrationDate.add_parameter(DiagParameter('CalibrationMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    CalibrationDate.add_parameter(DiagParameter('CalibrationDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))

    CalibrationEquipmentSoftwareNumber = DiagMessage(0xF19C, 'CalibrationEquipmentSoftwareNumber', [], None, '', 1)
    CalibrationEquipmentSoftwareNumber.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    EcuInstallationDate = DiagMessage(0xF19D, 'EcuInstallationDate', [], None, '', 3)
    EcuInstallationDate.add_parameter(DiagParameter('InstallationYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    EcuInstallationDate.add_parameter(DiagParameter('InstallationMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    EcuInstallationDate.add_parameter(DiagParameter('InstallationDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))

    OdxFile = DiagMessage(0xF19E, 'OdxFile', [1, 3, 4, 64], None, '', 1)
    OdxFile.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    VehicleManufacturerEOLProgramInfoCode = DiagMessage(0xF1A3, 'VehicleManufacturerEOLProgramInfoCode', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerEOLProgramInfoCode.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Name of PROGRAMMING Tool', False, False, False))

    VehicleManufacturerEOLProgramVersionCode = DiagMessage(0xF1A4, 'VehicleManufacturerEOLProgramVersionCode', [1, 3, 4, 64], None, '', 1)
    VehicleManufacturerEOLProgramVersionCode.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Version of PROGRAMMING Tool', False, False, False))

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [1, 2, 3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [1, 2, 3, 4, 64], None, '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))

    Software_Calibration_Identification = DiagMessage(0xF1A8, 'Software_Calibration_Identification', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    Software_Calibration_Identification.add_parameter(DiagParameter('Software_Calibration_Identification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, '', False, False, False))

    Assigned_Target_ECU_Name = DiagMessage(0xF1C1, 'Assigned_Target_ECU_Name', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    Assigned_Target_ECU_Name.add_parameter(DiagParameter('target_ECU_name', 1, 0, 0, 64, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, '', False, False, False))

    Internal_AGCO_Name = DiagMessage(0xF1C2, 'Internal_AGCO_Name', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    Internal_AGCO_Name.add_parameter(DiagParameter('InternalAGCO_Name', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, '', False, False, False))

    KP = DiagMessage(0xFD01, 'KP', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    KP.add_parameter(DiagParameter('KP', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    KI = DiagMessage(0xFD02, 'KI', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    KI.add_parameter(DiagParameter('KI', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    KD = DiagMessage(0xFD03, 'KD', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    KD.add_parameter(DiagParameter('KD', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    KP2 = DiagMessage(0xFD04, 'KP2', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    KP2.add_parameter(DiagParameter('KP2', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    KI2 = DiagMessage(0xFD05, 'KI2', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    KI2.add_parameter(DiagParameter('KI2', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    K_IntCapt = DiagMessage(0xFD06, 'K_IntCapt', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_IntCapt.add_parameter(DiagParameter('ActivateIntegral', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'6': [6, 6]}, 6, 6, '', False, False, False))

    K_PID_Time = DiagMessage(0xFD07, 'K_PID_Time', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_PID_Time.add_parameter(DiagParameter('PrimaryLoopSampleRate', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_TevapFreezeUpInit = DiagMessage(0xFD08, 'K_TevapFreezeUpInit', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_TevapFreezeUpInit.add_parameter(DiagParameter('K_TevapFreezeUpInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0x22': [34, 34]}, 34, 34, '', False, False, False))

    K_TevapHystInit = DiagMessage(0xFD09, 'K_TevapHystInit', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_TevapHystInit.add_parameter(DiagParameter('K_TevapHysInit', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'5': [5, 5]}, 5, 5, '', False, False, False))

    K_TimeAC2HeatInit = DiagMessage(0xFD0A, 'K_TimeAC2HeatInit', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_TimeAC2HeatInit.add_parameter(DiagParameter('K_TimeAC2HeatInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_TimeB4RampDownInit = DiagMessage(0xFD0B, 'K_TimeB4RampDownInit', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_TimeB4RampDownInit.add_parameter(DiagParameter('K_TimeB4RampDownInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_TimeB4RampUpInit = DiagMessage(0xFD0C, 'K_TimeB4RampUpInit', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_TimeB4RampUpInit.add_parameter(DiagParameter('K_TimeB4RampUpInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_TimeClutchOn2OnInit = DiagMessage(0xFD0D, 'K_TimeClutchOn2OnInit', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_TimeClutchOn2OnInit.add_parameter(DiagParameter('K_TimeClutchOn2OnInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_FsDebounceTime1 = DiagMessage(0xFD0E, 'K_FsDebounceTime1', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_FsDebounceTime1.add_parameter(DiagParameter('K_TimeFsDownHigh', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_FsDebounceTime2 = DiagMessage(0xFD0F, 'K_FsDebounceTime2', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_FsDebounceTime2.add_parameter(DiagParameter('K_TimeFsDownLow', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_MAX_AirOff = DiagMessage(0xFD10, 'K_MAX_AirOff', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_MAX_AirOff.add_parameter(DiagParameter('K_TimeFsUpHigh', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_TempcoolOffsetInit = DiagMessage(0xFD12, 'K_TempcoolOffsetInit', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_TempcoolOffsetInit.add_parameter(DiagParameter('K_TempcoolOffsetInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_TempAmbNoAC = DiagMessage(0xFD15, 'K_TempAmbNoAC', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_TempAmbNoAC.add_parameter(DiagParameter('K_TempAmbNoAC', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_FsAutoLowInit = DiagMessage(0xFD16, 'K_FsAutoLowInit', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_FsAutoLowInit.add_parameter(DiagParameter('K_FsAutoLowInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_LowBatteryThreshold = DiagMessage(0xFD17, 'K_LowBatteryThreshold', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_LowBatteryThreshold.add_parameter(DiagParameter('LowBatteryVoltage', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    K_HighBatteryThreshold = DiagMessage(0xFD18, 'K_HighBatteryThreshold', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_HighBatteryThreshold.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    WUP_Offset = DiagMessage(0xFD19, 'WUP_Offset', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    WUP_Offset.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_ClutchOffTime = DiagMessage(0xFD1A, 'K_ClutchOffTime', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_ClutchOffTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_AutoPrezOffTime = DiagMessage(0xFD1B, 'K_AutoPrezOffTime', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_AutoPrezOffTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_AutoPrezOnTime = DiagMessage(0xFD1C, 'K_AutoPrezOnTime', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_AutoPrezOnTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_PrezShortOffTime = DiagMessage(0xFD1D, 'K_PrezShortOffTime', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_PrezShortOffTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_PrezLongOnTime = DiagMessage(0xFD1E, 'K_PrezLongOnTime', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_PrezLongOnTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_PrezManOffTime = DiagMessage(0xFD1F, 'K_PrezManOffTime', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_PrezManOffTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_PrezManOnTime = DiagMessage(0xFD20, 'K_PrezManOnTime', [1, 2, 3, 4, 64], [1, 2, 3, 4, 5], '', 1)
    K_PrezManOnTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    CabinSensorRawValue = DiagMessage(0xFD21, 'CabinSensorRawValue', [], None, '', 1)
    CabinSensorRawValue.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.005, 'V', 0, 31981, '', False, False, False))

    OutletSensorRawValue = DiagMessage(0xFD22, 'OutletSensorRawValue', [], None, '', 1)
    OutletSensorRawValue.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.005, 'V', 0, 31981, '', False, False, False))

    EvapSensorRawValue = DiagMessage(0xFD23, 'EvapSensorRawValue', [], None, '', 1)
    EvapSensorRawValue.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.005, 'V', 0, 31981, '', False, False, False))

    PowerSupplyRawValue = DiagMessage(0xFD24, 'PowerSupplyRawValue', [], None, '', 1)
    PowerSupplyRawValue.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.005, 'V', 0, 31981, '', False, False, False))

    CabinTemp = DiagMessage(0xFD25, 'CabinTemp', [], None, '', 1)
    CabinTemp.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '?F', -200, 65335, '', False, False, False))

    OutletTemp = DiagMessage(0xFD26, 'OutletTemp', [], None, '', 1)
    OutletTemp.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '?F', -200, 65335, '', False, False, False))

    EvapTemp = DiagMessage(0xFD27, 'EvapTemp', [], None, '', 1)
    EvapTemp.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, '?F', -200, 65335, '', False, False, False))

    PowerSupplyValue = DiagMessage(0xFD28, 'PowerSupplyValue', [], None, '', 1)
    PowerSupplyValue.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.1, 'V', 0, 65535, '', False, False, False))

    WaterValveOutputCmd = DiagMessage(0xFD29, 'WaterValveOutputCmd', [], None, '', 1)
    WaterValveOutputCmd.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.4, '%', 0, 100, '', False, False, False))

    BlowerOutputCmd = DiagMessage(0xFD2A, 'BlowerOutputCmd', [], None, '', 1)
    BlowerOutputCmd.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.4, '%', 0, 100, '', False, False, False))

    ClutchOutputCmd = DiagMessage(0xFD2B, 'ClutchOutputCmd', [], None, '', 1)
    ClutchOutputCmd.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    RecircOutputCmd = DiagMessage(0xFD2C, 'RecircOutputCmd', [], None, '', 1)
    RecircOutputCmd.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.4, '%', 0, 100, '', False, False, False))

    AirDistributionOutputCmd = DiagMessage(0xFD2D, 'AirDistributionOutputCmd', [], None, '', 1)
    AirDistributionOutputCmd.add_parameter(DiagParameter('DataRecord', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.4, '%', 0, 100, '', False, False, False))

    UDSVersionDataIdentifier = DiagMessage(0xFF00, 'UDSVersionDataIdentifier', [1, 3, 4, 64], None, '', 4)
    UDSVersionDataIdentifier.add_parameter(DiagParameter('Major', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    UDSVersionDataIdentifier.add_parameter(DiagParameter('Minor', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    UDSVersionDataIdentifier.add_parameter(DiagParameter('Revision', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))
    UDSVersionDataIdentifier.add_parameter(DiagParameter('Build', 4, 3, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 255, '', False, False, False))


class BERGSTROM_BVWriteDataSignals:
    WriteFingerprint = DiagMessage(0xF15A, 'WriteFingerprint', [2], [1, 3, 4, 5], '', 4)
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))
    WriteFingerprint.add_parameter(DiagParameter('ProgrammingFingerprint', 4, 3, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    SystemSupplierIdentifierData = DiagMessage(0xF18A, 'SystemSupplierIdentifierData', [64], [5], '', 1)
    SystemSupplierIdentifierData.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'System Supplier Name', False, False, False))

    EcuManufacturingDate = DiagMessage(0xF18B, 'EcuManufacturingDate', [64], [5], '', 3)
    EcuManufacturingDate.add_parameter(DiagParameter('ManufacturingYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    EcuManufacturingDate.add_parameter(DiagParameter('ManufacturingMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    EcuManufacturingDate.add_parameter(DiagParameter('ManufacturingDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))

    EcuSerialNumber = DiagMessage(0xF18C, 'EcuSerialNumber', [64], [5], '', 1)
    EcuSerialNumber.add_parameter(DiagParameter('SerialNumber', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '1 to 32 bytes allowed (all 0xFF --> "INVALID")', False, False, False))

    SupportedFunctionalUnits = DiagMessage(0xF18D, 'SupportedFunctionalUnits', [64], [5], '', 1)
    SupportedFunctionalUnits.add_parameter(DiagParameter('Number', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 4294967295, '', False, False, False))

    VehicleManufacturerKitAssemblyPartNumber = DiagMessage(0xF18E, 'VehicleManufacturerKitAssemblyPartNumber', [64], [5], '', 1)
    VehicleManufacturerKitAssemblyPartNumber.add_parameter(DiagParameter('AssemblyPartNumber', 1, 0, 0, 160, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Partnumber of a complete Assembly e.g. G-Nr (all 0xFF --> "INVALID")', False, False, False))

    VehicleIdentificationNumber = DiagMessage(0xF190, 'VehicleIdentificationNumber', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleIdentificationNumber.add_parameter(DiagParameter('VinNumber', 1, 0, 0, 136, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '17 bytes fixed length (all 0xFF --> "INVALID")', False, False, False))

    VehicleManufacturerECUHardwareNumber = DiagMessage(0xF191, 'VehicleManufacturerECUHardwareNumber', [64], [5], '', 1)
    VehicleManufacturerECUHardwareNumber.add_parameter(DiagParameter('VirtualPartNumber', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 4293918720, 4294967295, 'Unique feature identifier (mandatory for compatibility check hardware/software at ECU programming) ', False, False, False))

    SystemSupplierECUHardwareNumber = DiagMessage(0xF192, 'SystemSupplierECUHardwareNumber', [64], [5], '', 1)
    SystemSupplierECUHardwareNumber.add_parameter(DiagParameter('HardwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    SystemSupplierECUHardwareVersionNumber = DiagMessage(0xF193, 'SystemSupplierECUHardwareVersionNumber', [64], [5], '', 1)
    SystemSupplierECUHardwareVersionNumber.add_parameter(DiagParameter('SystemSupplierHardwareVersion', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '(optional used by ECU supplier)', False, False, False))

    SystemSupplierECUSoftwareNumber = DiagMessage(0xF194, 'SystemSupplierECUSoftwareNumber', [64], [5], '', 1)
    SystemSupplierECUSoftwareNumber.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    SystemSupplierECUSoftwareVersionNumber = DiagMessage(0xF195, 'SystemSupplierECUSoftwareVersionNumber', [64], [5], '', 1)
    SystemSupplierECUSoftwareVersionNumber.add_parameter(DiagParameter('SystemSupplierSoftwareVersion', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    SystemNameOrEngineType = DiagMessage(0xF197, 'SystemNameOrEngineType', [64], [5], '', 1)
    SystemNameOrEngineType.add_parameter(DiagParameter('SystemName', 1, 0, 0, 256, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'e.g. "Infotainment"', False, False, False))

    RepairShopCodeOrTesterSerialNumber = DiagMessage(0xF198, 'RepairShopCodeOrTesterSerialNumber', [3, 4, 64], [1, 3, 4, 5], '', 1)
    RepairShopCodeOrTesterSerialNumber.add_parameter(DiagParameter('TesterSerialNumber', 1, 0, 0, 128, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    ProgrammingDate = DiagMessage(0xF199, 'ProgrammingDate', [64], [5], '', 3)
    ProgrammingDate.add_parameter(DiagParameter('ProgrammingYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    ProgrammingDate.add_parameter(DiagParameter('ProgrammingMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    ProgrammingDate.add_parameter(DiagParameter('ProgrammingDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))

    CalibrationRepairShopCodeOrCalibrationEquipmentSerialNumber = DiagMessage(0xF19A, 'CalibrationRepairShopCodeOrCalibrationEquipmentSerialNumber', [], None, '', 1)
    CalibrationRepairShopCodeOrCalibrationEquipmentSerialNumber.add_parameter(DiagParameter('SerialNumber', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    CalibrationDate = DiagMessage(0xF19B, 'CalibrationDate', [], None, '', 3)
    CalibrationDate.add_parameter(DiagParameter('CalibrationYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    CalibrationDate.add_parameter(DiagParameter('CalibrationMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    CalibrationDate.add_parameter(DiagParameter('CalibrationDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))

    CalibrationEquipmentSoftwareNumber = DiagMessage(0xF19C, 'CalibrationEquipmentSoftwareNumber', [], None, '', 1)
    CalibrationEquipmentSoftwareNumber.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    EcuInstallationDate = DiagMessage(0xF19D, 'EcuInstallationDate', [], None, '', 3)
    EcuInstallationDate.add_parameter(DiagParameter('InstallationYear', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 1985.0, 1.0, 'years', 0, 2235, '', False, False, False))
    EcuInstallationDate.add_parameter(DiagParameter('InstallationMonth', 2, 1, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, 'months', 1, 12, '', False, False, False))
    EcuInstallationDate.add_parameter(DiagParameter('InstallationDay', 3, 2, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 0.25, 'days', 0.25, 31.75, '', False, False, False))

    OdxFile = DiagMessage(0xF19E, 'OdxFile', [], [5], '', 1)
    OdxFile.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 1600, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, '', False, False, False))

    VehicleManufacturerEOLProgramInfoCode = DiagMessage(0xF1A3, 'VehicleManufacturerEOLProgramInfoCode', [64], [1, 3, 4], '', 1)
    VehicleManufacturerEOLProgramInfoCode.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Name of PROGRAMMING Tool', False, False, False))

    VehicleManufacturerEOLProgramVersionCode = DiagMessage(0xF1A4, 'VehicleManufacturerEOLProgramVersionCode', [64], [1, 3, 4], '', 1)
    VehicleManufacturerEOLProgramVersionCode.add_parameter(DiagParameter('SoftwareIdentification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, 'ASCII', 0, 255, 'Version of PROGRAMMING Tool', False, False, False))

    CommandedAddress = DiagMessage(0xF1A5, 'CommandedAddress', [3, 4, 64], None, '', 1)
    CommandedAddress.add_parameter(DiagParameter('NewSourceAddress', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT, SignalConversion.IDENTICAL, 0, 1, '', 0, 254, '', False, False, False))

    VehicleModel = DiagMessage(0xF1A7, 'VehicleModel', [2, 3, 4, 64], [1, 3, 4], '', 1)
    VehicleModel.add_parameter(DiagParameter('VehicleModel', 1, 0, 0, 80, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.MIN_MAX_LENGTH, 0, 1, '', 0, 255, 'e.g. "T760" (all 0xFF --> "INVALID")', False, False, False))

    Software_Calibration_Identification = DiagMessage(0xF1A8, 'Software_Calibration_Identification', [2, 3, 4, 64], [2, 3], '', 1)
    Software_Calibration_Identification.add_parameter(DiagParameter('Software_Calibration_Identification', 1, 0, 0, 240, SignalByteOrder.Motorola, SignalType.ASCIISTRING, SignalConversion.STANDARD_LENGTH, 0, 1, '', 0, 255, '', False, False, False))

    K_TevapFreezeUpInit = DiagMessage(0xFD08, 'K_TevapFreezeUpInit', [2, 3, 4, 64], [2, 3], '', 1)
    K_TevapFreezeUpInit.add_parameter(DiagParameter('K_TevapFreezeUpInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.LOOKUPTABLE, SignalConversion.IDENTICAL, 0, 1, {'0x22': [34, 34]}, 34, 34, '', False, False, False))

    K_TimeClutchOn2OnInit = DiagMessage(0xFD0D, 'K_TimeClutchOn2OnInit', [2, 3, 4, 64], [2, 3], '', 1)
    K_TimeClutchOn2OnInit.add_parameter(DiagParameter('K_TimeClutchOn2OnInit', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_MAX_AirOff = DiagMessage(0xFD10, 'K_MAX_AirOff', [2, 3, 4, 64], [2, 3], '', 1)
    K_MAX_AirOff.add_parameter(DiagParameter('K_TimeFsUpHigh', 1, 0, 0, 8, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 255, '', False, False, False))

    K_LowBatteryThreshold = DiagMessage(0xFD17, 'K_LowBatteryThreshold', [2, 3, 4, 64], [2, 3], '', 1)
    K_LowBatteryThreshold.add_parameter(DiagParameter('LowBatteryVoltage', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    K_HighBatteryThreshold = DiagMessage(0xFD18, 'K_HighBatteryThreshold', [2, 3, 4, 64], [2, 3], '', 1)
    K_HighBatteryThreshold.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 32, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 4294967296, '', False, False, False))

    K_AutoPrezOffTime = DiagMessage(0xFD1B, 'K_AutoPrezOffTime', [2, 3, 4, 64], [2, 3], '', 1)
    K_AutoPrezOffTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_AutoPrezOnTime = DiagMessage(0xFD1C, 'K_AutoPrezOnTime', [2, 3, 4, 64], [2, 3], '', 1)
    K_AutoPrezOnTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_PrezShortOffTime = DiagMessage(0xFD1D, 'K_PrezShortOffTime', [2, 3, 4, 64], [2, 3], '', 1)
    K_PrezShortOffTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_PrezLongOnTime = DiagMessage(0xFD1E, 'K_PrezLongOnTime', [2, 3, 4, 64], [2, 3], '', 1)
    K_PrezLongOnTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_PrezManOffTime = DiagMessage(0xFD1F, 'K_PrezManOffTime', [2, 3, 4, 64], [2, 3], '', 1)
    K_PrezManOffTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))

    K_PrezManOnTime = DiagMessage(0xFD20, 'K_PrezManOnTime', [2, 3, 4, 64], [2, 3], '', 1)
    K_PrezManOnTime.add_parameter(DiagParameter('HighBatteryVoltage', 1, 0, 0, 16, SignalByteOrder.Motorola, SignalType.UINT_LINEAR, SignalConversion.LINEAR_CALCULATION, 0.0, 1.0, '', 0, 65535, '', False, False, False))


class BERGSTROM_BVIOControlDataSignals:
    pass


BERGSTROM_BVDTCSnapshotdDids = {
}


class BERGSTROMClient(ECUClient):
    class FlashData(Enum):
        pass

    class ReadDIDs(Enum):
        pass

    def __init__(self, routing_over_dgw=False, can_channel=1, comparam=UDSConnection.default_com_parameter,
                 functional_addressing=None, **kwargs):
        hw_id = 0x0
        super().__init__(0x15, "BERGSTROM", True, [], hw_id, can_channel=can_channel,
                         routing_over_dgw=routing_over_dgw, comparam=comparam, baudrate=250000,
                         sec_vendor=b'Vendor=AGCO,', source_id=0xF9, j1939_prio=6, switch_session_wait_time=0.0,
                         boot_time_min=0.1, key_length=4, functional_adr=functional_addressing,
                         **kwargs)
        self.kl15_relay = 0
        self.kl30_relay = 0
        self.read_dids = BERGSTROM_BVReadDataSignals
        self.write_dids = BERGSTROM_BVWriteDataSignals
        self.routine_dids = BERGSTROM_BVRoutineIdentifierSignals
        self.io_dids = BERGSTROM_BVIOControlDataSignals
        self.dtc_snapshot_dids = BERGSTROM_BVDTCSnapshotdDids
        self.long_name = ""
        self.sysmon_sw_version_min_number_of_matches = 0
        self.sysmon_mask_active = False

