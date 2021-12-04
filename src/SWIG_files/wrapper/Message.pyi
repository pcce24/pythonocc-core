from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.OSD import *
from OCC.Core.TColStd import *

#the following typedef cannot be wrapped as is
Message_HArrayOfMsg = NewType('Message_HArrayOfMsg', Any)

class Message_ListOfAlert:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class Message_ListOfMsg:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> Message_Msg: ...
    def Last(self) -> Message_Msg: ...
    def Append(self, theItem: Message_Msg) -> Message_Msg: ...
    def Prepend(self, theItem: Message_Msg) -> Message_Msg: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> Message_Msg: ...
    def SetValue(self, theIndex: int, theValue: Message_Msg) -> None: ...

class Message_SequenceOfPrinters:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Length(self) -> int: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...
    def Value(self, theIndex: int) -> False: ...
    def SetValue(self, theIndex: int, theValue: False) -> None: ...

class Message_Status(IntEnum):
    Message_None: int = ...
    Message_Done1: int = ...
    Message_Done2: int = ...
    Message_Done3: int = ...
    Message_Done4: int = ...
    Message_Done5: int = ...
    Message_Done6: int = ...
    Message_Done7: int = ...
    Message_Done8: int = ...
    Message_Done9: int = ...
    Message_Done10: int = ...
    Message_Done11: int = ...
    Message_Done12: int = ...
    Message_Done13: int = ...
    Message_Done14: int = ...
    Message_Done15: int = ...
    Message_Done16: int = ...
    Message_Done17: int = ...
    Message_Done18: int = ...
    Message_Done19: int = ...
    Message_Done20: int = ...
    Message_Done21: int = ...
    Message_Done22: int = ...
    Message_Done23: int = ...
    Message_Done24: int = ...
    Message_Done25: int = ...
    Message_Done26: int = ...
    Message_Done27: int = ...
    Message_Done28: int = ...
    Message_Done29: int = ...
    Message_Done30: int = ...
    Message_Done31: int = ...
    Message_Done32: int = ...
    Message_Warn1: int = ...
    Message_Warn2: int = ...
    Message_Warn3: int = ...
    Message_Warn4: int = ...
    Message_Warn5: int = ...
    Message_Warn6: int = ...
    Message_Warn7: int = ...
    Message_Warn8: int = ...
    Message_Warn9: int = ...
    Message_Warn10: int = ...
    Message_Warn11: int = ...
    Message_Warn12: int = ...
    Message_Warn13: int = ...
    Message_Warn14: int = ...
    Message_Warn15: int = ...
    Message_Warn16: int = ...
    Message_Warn17: int = ...
    Message_Warn18: int = ...
    Message_Warn19: int = ...
    Message_Warn20: int = ...
    Message_Warn21: int = ...
    Message_Warn22: int = ...
    Message_Warn23: int = ...
    Message_Warn24: int = ...
    Message_Warn25: int = ...
    Message_Warn26: int = ...
    Message_Warn27: int = ...
    Message_Warn28: int = ...
    Message_Warn29: int = ...
    Message_Warn30: int = ...
    Message_Warn31: int = ...
    Message_Warn32: int = ...
    Message_Alarm1: int = ...
    Message_Alarm2: int = ...
    Message_Alarm3: int = ...
    Message_Alarm4: int = ...
    Message_Alarm5: int = ...
    Message_Alarm6: int = ...
    Message_Alarm7: int = ...
    Message_Alarm8: int = ...
    Message_Alarm9: int = ...
    Message_Alarm10: int = ...
    Message_Alarm11: int = ...
    Message_Alarm12: int = ...
    Message_Alarm13: int = ...
    Message_Alarm14: int = ...
    Message_Alarm15: int = ...
    Message_Alarm16: int = ...
    Message_Alarm17: int = ...
    Message_Alarm18: int = ...
    Message_Alarm19: int = ...
    Message_Alarm20: int = ...
    Message_Alarm21: int = ...
    Message_Alarm22: int = ...
    Message_Alarm23: int = ...
    Message_Alarm24: int = ...
    Message_Alarm25: int = ...
    Message_Alarm26: int = ...
    Message_Alarm27: int = ...
    Message_Alarm28: int = ...
    Message_Alarm29: int = ...
    Message_Alarm30: int = ...
    Message_Alarm31: int = ...
    Message_Alarm32: int = ...
    Message_Fail1: int = ...
    Message_Fail2: int = ...
    Message_Fail3: int = ...
    Message_Fail4: int = ...
    Message_Fail5: int = ...
    Message_Fail6: int = ...
    Message_Fail7: int = ...
    Message_Fail8: int = ...
    Message_Fail9: int = ...
    Message_Fail10: int = ...
    Message_Fail11: int = ...
    Message_Fail12: int = ...
    Message_Fail13: int = ...
    Message_Fail14: int = ...
    Message_Fail15: int = ...
    Message_Fail16: int = ...
    Message_Fail17: int = ...
    Message_Fail18: int = ...
    Message_Fail19: int = ...
    Message_Fail20: int = ...
    Message_Fail21: int = ...
    Message_Fail22: int = ...
    Message_Fail23: int = ...
    Message_Fail24: int = ...
    Message_Fail25: int = ...
    Message_Fail26: int = ...
    Message_Fail27: int = ...
    Message_Fail28: int = ...
    Message_Fail29: int = ...
    Message_Fail30: int = ...
    Message_Fail31: int = ...
    Message_Fail32: int = ...

Message_None = Message_Status.Message_None
Message_Done1 = Message_Status.Message_Done1
Message_Done2 = Message_Status.Message_Done2
Message_Done3 = Message_Status.Message_Done3
Message_Done4 = Message_Status.Message_Done4
Message_Done5 = Message_Status.Message_Done5
Message_Done6 = Message_Status.Message_Done6
Message_Done7 = Message_Status.Message_Done7
Message_Done8 = Message_Status.Message_Done8
Message_Done9 = Message_Status.Message_Done9
Message_Done10 = Message_Status.Message_Done10
Message_Done11 = Message_Status.Message_Done11
Message_Done12 = Message_Status.Message_Done12
Message_Done13 = Message_Status.Message_Done13
Message_Done14 = Message_Status.Message_Done14
Message_Done15 = Message_Status.Message_Done15
Message_Done16 = Message_Status.Message_Done16
Message_Done17 = Message_Status.Message_Done17
Message_Done18 = Message_Status.Message_Done18
Message_Done19 = Message_Status.Message_Done19
Message_Done20 = Message_Status.Message_Done20
Message_Done21 = Message_Status.Message_Done21
Message_Done22 = Message_Status.Message_Done22
Message_Done23 = Message_Status.Message_Done23
Message_Done24 = Message_Status.Message_Done24
Message_Done25 = Message_Status.Message_Done25
Message_Done26 = Message_Status.Message_Done26
Message_Done27 = Message_Status.Message_Done27
Message_Done28 = Message_Status.Message_Done28
Message_Done29 = Message_Status.Message_Done29
Message_Done30 = Message_Status.Message_Done30
Message_Done31 = Message_Status.Message_Done31
Message_Done32 = Message_Status.Message_Done32
Message_Warn1 = Message_Status.Message_Warn1
Message_Warn2 = Message_Status.Message_Warn2
Message_Warn3 = Message_Status.Message_Warn3
Message_Warn4 = Message_Status.Message_Warn4
Message_Warn5 = Message_Status.Message_Warn5
Message_Warn6 = Message_Status.Message_Warn6
Message_Warn7 = Message_Status.Message_Warn7
Message_Warn8 = Message_Status.Message_Warn8
Message_Warn9 = Message_Status.Message_Warn9
Message_Warn10 = Message_Status.Message_Warn10
Message_Warn11 = Message_Status.Message_Warn11
Message_Warn12 = Message_Status.Message_Warn12
Message_Warn13 = Message_Status.Message_Warn13
Message_Warn14 = Message_Status.Message_Warn14
Message_Warn15 = Message_Status.Message_Warn15
Message_Warn16 = Message_Status.Message_Warn16
Message_Warn17 = Message_Status.Message_Warn17
Message_Warn18 = Message_Status.Message_Warn18
Message_Warn19 = Message_Status.Message_Warn19
Message_Warn20 = Message_Status.Message_Warn20
Message_Warn21 = Message_Status.Message_Warn21
Message_Warn22 = Message_Status.Message_Warn22
Message_Warn23 = Message_Status.Message_Warn23
Message_Warn24 = Message_Status.Message_Warn24
Message_Warn25 = Message_Status.Message_Warn25
Message_Warn26 = Message_Status.Message_Warn26
Message_Warn27 = Message_Status.Message_Warn27
Message_Warn28 = Message_Status.Message_Warn28
Message_Warn29 = Message_Status.Message_Warn29
Message_Warn30 = Message_Status.Message_Warn30
Message_Warn31 = Message_Status.Message_Warn31
Message_Warn32 = Message_Status.Message_Warn32
Message_Alarm1 = Message_Status.Message_Alarm1
Message_Alarm2 = Message_Status.Message_Alarm2
Message_Alarm3 = Message_Status.Message_Alarm3
Message_Alarm4 = Message_Status.Message_Alarm4
Message_Alarm5 = Message_Status.Message_Alarm5
Message_Alarm6 = Message_Status.Message_Alarm6
Message_Alarm7 = Message_Status.Message_Alarm7
Message_Alarm8 = Message_Status.Message_Alarm8
Message_Alarm9 = Message_Status.Message_Alarm9
Message_Alarm10 = Message_Status.Message_Alarm10
Message_Alarm11 = Message_Status.Message_Alarm11
Message_Alarm12 = Message_Status.Message_Alarm12
Message_Alarm13 = Message_Status.Message_Alarm13
Message_Alarm14 = Message_Status.Message_Alarm14
Message_Alarm15 = Message_Status.Message_Alarm15
Message_Alarm16 = Message_Status.Message_Alarm16
Message_Alarm17 = Message_Status.Message_Alarm17
Message_Alarm18 = Message_Status.Message_Alarm18
Message_Alarm19 = Message_Status.Message_Alarm19
Message_Alarm20 = Message_Status.Message_Alarm20
Message_Alarm21 = Message_Status.Message_Alarm21
Message_Alarm22 = Message_Status.Message_Alarm22
Message_Alarm23 = Message_Status.Message_Alarm23
Message_Alarm24 = Message_Status.Message_Alarm24
Message_Alarm25 = Message_Status.Message_Alarm25
Message_Alarm26 = Message_Status.Message_Alarm26
Message_Alarm27 = Message_Status.Message_Alarm27
Message_Alarm28 = Message_Status.Message_Alarm28
Message_Alarm29 = Message_Status.Message_Alarm29
Message_Alarm30 = Message_Status.Message_Alarm30
Message_Alarm31 = Message_Status.Message_Alarm31
Message_Alarm32 = Message_Status.Message_Alarm32
Message_Fail1 = Message_Status.Message_Fail1
Message_Fail2 = Message_Status.Message_Fail2
Message_Fail3 = Message_Status.Message_Fail3
Message_Fail4 = Message_Status.Message_Fail4
Message_Fail5 = Message_Status.Message_Fail5
Message_Fail6 = Message_Status.Message_Fail6
Message_Fail7 = Message_Status.Message_Fail7
Message_Fail8 = Message_Status.Message_Fail8
Message_Fail9 = Message_Status.Message_Fail9
Message_Fail10 = Message_Status.Message_Fail10
Message_Fail11 = Message_Status.Message_Fail11
Message_Fail12 = Message_Status.Message_Fail12
Message_Fail13 = Message_Status.Message_Fail13
Message_Fail14 = Message_Status.Message_Fail14
Message_Fail15 = Message_Status.Message_Fail15
Message_Fail16 = Message_Status.Message_Fail16
Message_Fail17 = Message_Status.Message_Fail17
Message_Fail18 = Message_Status.Message_Fail18
Message_Fail19 = Message_Status.Message_Fail19
Message_Fail20 = Message_Status.Message_Fail20
Message_Fail21 = Message_Status.Message_Fail21
Message_Fail22 = Message_Status.Message_Fail22
Message_Fail23 = Message_Status.Message_Fail23
Message_Fail24 = Message_Status.Message_Fail24
Message_Fail25 = Message_Status.Message_Fail25
Message_Fail26 = Message_Status.Message_Fail26
Message_Fail27 = Message_Status.Message_Fail27
Message_Fail28 = Message_Status.Message_Fail28
Message_Fail29 = Message_Status.Message_Fail29
Message_Fail30 = Message_Status.Message_Fail30
Message_Fail31 = Message_Status.Message_Fail31
Message_Fail32 = Message_Status.Message_Fail32

class Message_ConsoleColor(IntEnum):
    Message_ConsoleColor_Default: int = ...
    Message_ConsoleColor_Black: int = ...
    Message_ConsoleColor_White: int = ...
    Message_ConsoleColor_Red: int = ...
    Message_ConsoleColor_Blue: int = ...
    Message_ConsoleColor_Green: int = ...
    Message_ConsoleColor_Yellow: int = ...
    Message_ConsoleColor_Cyan: int = ...
    Message_ConsoleColor_Magenta: int = ...

Message_ConsoleColor_Default = Message_ConsoleColor.Message_ConsoleColor_Default
Message_ConsoleColor_Black = Message_ConsoleColor.Message_ConsoleColor_Black
Message_ConsoleColor_White = Message_ConsoleColor.Message_ConsoleColor_White
Message_ConsoleColor_Red = Message_ConsoleColor.Message_ConsoleColor_Red
Message_ConsoleColor_Blue = Message_ConsoleColor.Message_ConsoleColor_Blue
Message_ConsoleColor_Green = Message_ConsoleColor.Message_ConsoleColor_Green
Message_ConsoleColor_Yellow = Message_ConsoleColor.Message_ConsoleColor_Yellow
Message_ConsoleColor_Cyan = Message_ConsoleColor.Message_ConsoleColor_Cyan
Message_ConsoleColor_Magenta = Message_ConsoleColor.Message_ConsoleColor_Magenta

class Message_Gravity(IntEnum):
    Message_Trace: int = ...
    Message_Info: int = ...
    Message_Warning: int = ...
    Message_Alarm: int = ...
    Message_Fail: int = ...

Message_Trace = Message_Gravity.Message_Trace
Message_Info = Message_Gravity.Message_Info
Message_Warning = Message_Gravity.Message_Warning
Message_Alarm = Message_Gravity.Message_Alarm
Message_Fail = Message_Gravity.Message_Fail

class Message_MetricType(IntEnum):
    Message_MetricType_None: int = ...
    Message_MetricType_ThreadCPUUserTime: int = ...
    Message_MetricType_ThreadCPUSystemTime: int = ...
    Message_MetricType_ProcessCPUUserTime: int = ...
    Message_MetricType_ProcessCPUSystemTime: int = ...
    Message_MetricType_MemPrivate: int = ...
    Message_MetricType_MemVirtual: int = ...
    Message_MetricType_MemWorkingSet: int = ...
    Message_MetricType_MemWorkingSetPeak: int = ...
    Message_MetricType_MemSwapUsage: int = ...
    Message_MetricType_MemSwapUsagePeak: int = ...
    Message_MetricType_MemHeapUsage: int = ...

Message_MetricType_None = Message_MetricType.Message_MetricType_None
Message_MetricType_ThreadCPUUserTime = Message_MetricType.Message_MetricType_ThreadCPUUserTime
Message_MetricType_ThreadCPUSystemTime = Message_MetricType.Message_MetricType_ThreadCPUSystemTime
Message_MetricType_ProcessCPUUserTime = Message_MetricType.Message_MetricType_ProcessCPUUserTime
Message_MetricType_ProcessCPUSystemTime = Message_MetricType.Message_MetricType_ProcessCPUSystemTime
Message_MetricType_MemPrivate = Message_MetricType.Message_MetricType_MemPrivate
Message_MetricType_MemVirtual = Message_MetricType.Message_MetricType_MemVirtual
Message_MetricType_MemWorkingSet = Message_MetricType.Message_MetricType_MemWorkingSet
Message_MetricType_MemWorkingSetPeak = Message_MetricType.Message_MetricType_MemWorkingSetPeak
Message_MetricType_MemSwapUsage = Message_MetricType.Message_MetricType_MemSwapUsage
Message_MetricType_MemSwapUsagePeak = Message_MetricType.Message_MetricType_MemSwapUsagePeak
Message_MetricType_MemHeapUsage = Message_MetricType.Message_MetricType_MemHeapUsage

class Message_StatusType(IntEnum):
    Message_DONE: int = ...
    Message_WARN: int = ...
    Message_ALARM: int = ...
    Message_FAIL: int = ...

Message_DONE = Message_StatusType.Message_DONE
Message_WARN = Message_StatusType.Message_WARN
Message_ALARM = Message_StatusType.Message_ALARM
Message_FAIL = Message_StatusType.Message_FAIL

class message:
    @staticmethod
    def DefaultMessenger() -> Message_Messenger: ...
    @staticmethod
    def DefaultReport(theToCreate: Optional[bool] = False) -> Message_Report: ...
    @staticmethod
    def FillTime(Hour: int, Minute: int, Second: float) -> TCollection_AsciiString: ...
    @overload
    @staticmethod
    def MetricFromString(theString: str) -> Tuple[bool, Message_MetricType]: ...
    @overload
    @staticmethod
    def MetricFromString(theString: str) -> Message_MetricType: ...
    @staticmethod
    def MetricToString(theType: Message_MetricType) -> str: ...

class Message_Alert(Standard_Transient):
    def GetMessageKey(self) -> str: ...
    def Merge(self, theTarget: Message_Alert) -> bool: ...
    def SupportsMerge(self) -> bool: ...

class Message_Algorithm(Standard_Transient):
    def __init__(self) -> None: ...
    @overload
    def AddStatus(self, theOther: Message_Algorithm) -> None: ...
    @overload
    def AddStatus(self, theStatus: Message_ExecStatus, theOther: Message_Algorithm) -> None: ...
    def ChangeStatus(self) -> Message_ExecStatus: ...
    def ClearStatus(self) -> None: ...
    def GetMessageNumbers(self, theStatus: Message_Status) -> TColStd_HPackedMapOfInteger: ...
    def GetMessageStrings(self, theStatus: Message_Status) -> TColStd_HSequenceOfHExtendedString: ...
    def GetMessenger(self) -> Message_Messenger: ...
    def GetStatus(self) -> Message_ExecStatus: ...
    @overload
    @staticmethod
    def PrepareReport(theError: TColStd_HPackedMapOfInteger, theMaxCount: int) -> TCollection_ExtendedString: ...
    @overload
    @staticmethod
    def PrepareReport(theReportSeq: TColStd_SequenceOfHExtendedString, theMaxCount: int) -> TCollection_ExtendedString: ...
    def SendMessages(self, theTraceLevel: Optional[Message_Gravity] = Message_Warning, theMaxCount: Optional[int] = 20) -> None: ...
    def SendStatusMessages(self, theFilter: Message_ExecStatus, theTraceLevel: Optional[Message_Gravity] = Message_Warning, theMaxCount: Optional[int] = 20) -> None: ...
    def SetMessenger(self, theMsgr: Message_Messenger) -> None: ...
    @overload
    def SetStatus(self, theStat: Message_Status) -> None: ...
    @overload
    def SetStatus(self, theStat: Message_Status, theInt: int) -> None: ...
    @overload
    def SetStatus(self, theStat: Message_Status, theStr: str, noRepetitions: Optional[bool] = True) -> None: ...
    @overload
    def SetStatus(self, theStat: Message_Status, theStr: TCollection_AsciiString, noRepetitions: Optional[bool] = True) -> None: ...
    @overload
    def SetStatus(self, theStat: Message_Status, theStr: TCollection_HAsciiString, noRepetitions: Optional[bool] = True) -> None: ...
    @overload
    def SetStatus(self, theStat: Message_Status, theStr: TCollection_ExtendedString, noRepetitions: Optional[bool] = True) -> None: ...
    @overload
    def SetStatus(self, theStat: Message_Status, theStr: TCollection_HExtendedString, noRepetitions: Optional[bool] = True) -> None: ...
    @overload
    def SetStatus(self, theStat: Message_Status, theMsg: Message_Msg) -> None: ...

class Message_Attribute(Standard_Transient):
    def __init__(self, theName: Optional[TCollection_AsciiString] = TCollection_AsciiString()) -> None: ...
    def GetMessageKey(self) -> str: ...
    def GetName(self) -> TCollection_AsciiString: ...
    def SetName(self, theName: TCollection_AsciiString) -> None: ...

class Message_CompositeAlerts(Standard_Transient):
    def __init__(self) -> None: ...
    def AddAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> bool: ...
    def Alerts(self, theGravity: Message_Gravity) -> Message_ListOfAlert: ...
    @overload
    def Clear(self) -> None: ...
    @overload
    def Clear(self, theGravity: Message_Gravity) -> None: ...
    @overload
    def Clear(self, theType: Standard_Type) -> None: ...
    @overload
    def HasAlert(self, theAlert: Message_Alert) -> bool: ...
    @overload
    def HasAlert(self, theType: Standard_Type, theGravity: Message_Gravity) -> bool: ...
    def RemoveAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> bool: ...

class Message_ExecStatus:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, status: Message_Status) -> None: ...
    def Add(self, theOther: Message_ExecStatus) -> None: ...
    def And(self, theOther: Message_ExecStatus) -> None: ...
    @overload
    def Clear(self, status: Message_Status) -> None: ...
    @overload
    def Clear(self) -> None: ...
    def ClearAllAlarm(self) -> None: ...
    def ClearAllDone(self) -> None: ...
    def ClearAllFail(self) -> None: ...
    def ClearAllWarn(self) -> None: ...
    def IsAlarm(self) -> bool: ...
    def IsDone(self) -> bool: ...
    def IsFail(self) -> bool: ...
    def IsSet(self, status: Message_Status) -> bool: ...
    def IsWarn(self) -> bool: ...
    @staticmethod
    def LocalStatusIndex(status: Message_Status) -> int: ...
    def Set(self, status: Message_Status) -> None: ...
    def SetAllAlarm(self) -> None: ...
    def SetAllDone(self) -> None: ...
    def SetAllFail(self) -> None: ...
    def SetAllWarn(self) -> None: ...
    @staticmethod
    def StatusByIndex(theIndex: int) -> Message_Status: ...
    @staticmethod
    def StatusIndex(status: Message_Status) -> int: ...
    @staticmethod
    def TypeOfStatus(status: Message_Status) -> Message_StatusType: ...

class Message_Level:
    def __init__(self, theName: Optional[TCollection_AsciiString] = TCollection_AsciiString()) -> None: ...
    def AddAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> bool: ...
    def RootAlert(self) -> Message_AlertExtended: ...
    def SetRootAlert(self, theAlert: Message_AlertExtended, isRequiredToStart: bool) -> None: ...

class Message_Messenger(Standard_Transient):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, thePrinter: Message_Printer) -> None: ...
    def AddPrinter(self, thePrinter: Message_Printer) -> bool: ...
    def ChangePrinters(self) -> Message_SequenceOfPrinters: ...
    def Printers(self) -> Message_SequenceOfPrinters: ...
    def RemovePrinter(self, thePrinter: Message_Printer) -> bool: ...
    def RemovePrinters(self, theType: Standard_Type) -> int: ...

class Message_Msg:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theMsg: Message_Msg) -> None: ...
    @overload
    def __init__(self, theKey: str) -> None: ...
    @overload
    def __init__(self, theKey: TCollection_ExtendedString) -> None: ...
    @overload
    def Arg(self, theString: str) -> Message_Msg: ...
    @overload
    def Arg(self, theString: TCollection_AsciiString) -> Message_Msg: ...
    @overload
    def Arg(self, theString: TCollection_HAsciiString) -> Message_Msg: ...
    @overload
    def Arg(self, theString: TCollection_ExtendedString) -> Message_Msg: ...
    @overload
    def Arg(self, theString: TCollection_HExtendedString) -> Message_Msg: ...
    @overload
    def Arg(self, theInt: int) -> Message_Msg: ...
    @overload
    def Arg(self, theReal: float) -> Message_Msg: ...
    def Get(self) -> TCollection_ExtendedString: ...
    def IsEdited(self) -> bool: ...
    def Original(self) -> TCollection_ExtendedString: ...
    @overload
    def Set(self, theMsg: str) -> None: ...
    @overload
    def Set(self, theMsg: TCollection_ExtendedString) -> None: ...
    def Value(self) -> TCollection_ExtendedString: ...

class Message_MsgFile:
    @staticmethod
    def AddMsg(key: TCollection_AsciiString, text: TCollection_ExtendedString) -> bool: ...
    @staticmethod
    def HasMsg(key: TCollection_AsciiString) -> bool: ...
    @staticmethod
    def Load(theDirName: str, theFileName: str) -> bool: ...
    @staticmethod
    def LoadFile(theFName: str) -> bool: ...
    @staticmethod
    def LoadFromEnv(theEnvName: str, theFileName: str, theLangExt: Optional[str] = "") -> bool: ...
    @staticmethod
    def LoadFromString(theContent: str, theLength: Optional[int] = -1) -> bool: ...
    @overload
    @staticmethod
    def Msg(key: str) -> TCollection_ExtendedString: ...
    @overload
    @staticmethod
    def Msg(key: TCollection_AsciiString) -> TCollection_ExtendedString: ...

class Message_Printer(Standard_Transient):
    def GetTraceLevel(self) -> Message_Gravity: ...
    @overload
    def Send(self, theString: TCollection_ExtendedString, theGravity: Message_Gravity) -> None: ...
    @overload
    def Send(self, theString: str, theGravity: Message_Gravity) -> None: ...
    @overload
    def Send(self, theString: TCollection_AsciiString, theGravity: Message_Gravity) -> None: ...
    def SendObject(self, theObject: Standard_Transient, theGravity: Message_Gravity) -> None: ...
    def SendStringStream(self, theStream: Standard_SStream, theGravity: Message_Gravity) -> None: ...
    def SetTraceLevel(self, theTraceLevel: Message_Gravity) -> None: ...

class Message_ProgressIndicator(Standard_Transient):
    def GetPosition(self) -> float: ...
    @overload
    def Start(self) -> Message_ProgressRange: ...
    @overload
    @staticmethod
    def Start(theProgress: Message_ProgressIndicator) -> Message_ProgressRange: ...

class Message_ProgressRange:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theOther: Message_ProgressRange) -> None: ...
    def Close(self) -> None: ...
    def IsActive(self) -> bool: ...
    def More(self) -> bool: ...
    def UserBreak(self) -> bool: ...

class Message_Report(Standard_Transient):
    def __init__(self) -> None: ...
    def ActivateInMessenger(self, toActivate: bool, theMessenger: Optional[Message_Messenger] = None) -> None: ...
    def ActiveMetrics(self) -> False: ...
    def AddAlert(self, theGravity: Message_Gravity, theAlert: Message_Alert) -> None: ...
    def AddLevel(self, theLevel: Message_Level, theName: TCollection_AsciiString) -> None: ...
    @overload
    def Clear(self) -> None: ...
    @overload
    def Clear(self, theGravity: Message_Gravity) -> None: ...
    @overload
    def Clear(self, theType: Standard_Type) -> None: ...
    def ClearMetrics(self) -> None: ...
    def GetAlerts(self, theGravity: Message_Gravity) -> Message_ListOfAlert: ...
    @overload
    def HasAlert(self, theType: Standard_Type) -> bool: ...
    @overload
    def HasAlert(self, theType: Standard_Type, theGravity: Message_Gravity) -> bool: ...
    def IsActiveInMessenger(self, theMessenger: Optional[Message_Messenger] = None) -> bool: ...
    def Limit(self) -> int: ...
    @overload
    def Merge(self, theOther: Message_Report) -> None: ...
    @overload
    def Merge(self, theOther: Message_Report, theGravity: Message_Gravity) -> None: ...
    def RemoveLevel(self, theLevel: Message_Level) -> None: ...
    @overload
    def SendMessages(self, theMessenger: Message_Messenger) -> None: ...
    @overload
    def SendMessages(self, theMessenger: Message_Messenger, theGravity: Message_Gravity) -> None: ...
    def SetActiveMetric(self, theMetricType: Message_MetricType, theActivate: bool) -> None: ...
    def SetLimit(self, theLimit: int) -> None: ...
    def UpdateActiveInMessenger(self, theMessenger: Optional[Message_Messenger] = None) -> None: ...

class Message_AlertExtended(Message_Alert):
    def __init__(self) -> None: ...
    @staticmethod
    def AddAlert(theReport: Message_Report, theAttribute: Message_Attribute, theGravity: Message_Gravity) -> Message_Alert: ...
    def Attribute(self) -> Message_Attribute: ...
    def CompositeAlerts(self, theToCreate: Optional[bool] = False) -> Message_CompositeAlerts: ...
    def GetMessageKey(self) -> str: ...
    def Merge(self, theTarget: Message_Alert) -> bool: ...
    def SetAttribute(self, theAttribute: Message_Attribute) -> None: ...
    def SupportsMerge(self) -> bool: ...

class Message_AttributeMeter(Message_Attribute):
    def __init__(self, theName: Optional[TCollection_AsciiString] = TCollection_AsciiString()) -> None: ...
    def HasMetric(self, theMetric: Message_MetricType) -> bool: ...
    def IsMetricValid(self, theMetric: Message_MetricType) -> bool: ...
    @staticmethod
    def SetAlertMetrics(theAlert: Message_AlertExtended, theStartValue: bool) -> None: ...
    def SetStartValue(self, theMetric: Message_MetricType, theValue: float) -> None: ...
    def SetStopValue(self, theMetric: Message_MetricType, theValue: float) -> None: ...
    @staticmethod
    def StartAlert(theAlert: Message_AlertExtended) -> None: ...
    def StartValue(self, theMetric: Message_MetricType) -> float: ...
    @staticmethod
    def StopAlert(theAlert: Message_AlertExtended) -> None: ...
    def StopValue(self, theMetric: Message_MetricType) -> float: ...
    @staticmethod
    def UndefinedMetricValue() -> float: ...

class Message_AttributeObject(Message_Attribute):
    def __init__(self, theObject: Standard_Transient, theName: Optional[TCollection_AsciiString] = TCollection_AsciiString()) -> None: ...
    def Object(self) -> Standard_Transient: ...
    def SetObject(self, theObject: Standard_Transient) -> None: ...

class Message_AttributeStream(Message_Attribute):
    def __init__(self, theStream: Standard_SStream, theName: Optional[TCollection_AsciiString] = TCollection_AsciiString()) -> None: ...
    def SetStream(self, theStream: Standard_SStream) -> None: ...
    def Stream(self) -> Standard_SStream: ...

class Message_PrinterOStream(Message_Printer):
    @overload
    def __init__(self, theTraceLevel: Optional[Message_Gravity] = Message_Info) -> None: ...
    @overload
    def __init__(self, theFileName: str, theDoAppend: bool, theTraceLevel: Optional[Message_Gravity] = Message_Info) -> None: ...
    def Close(self) -> None: ...
    def GetStream(self) -> Standard_OStream: ...
    def SetToColorize(self, theToColorize: bool) -> None: ...
    def ToColorize(self) -> bool: ...

class Message_PrinterSystemLog(Message_Printer):
    def __init__(self, theEventSourceName: TCollection_AsciiString, theTraceLevel: Optional[Message_Gravity] = Message_Info) -> None: ...

class Message_PrinterToReport(Message_Printer):
    def __init__(self) -> None: ...
    def Report(self) -> Message_Report: ...
    def SendObject(self, theObject: Standard_Transient, theGravity: Message_Gravity) -> None: ...
    def SendStringStream(self, theStream: Standard_SStream, theGravity: Message_Gravity) -> None: ...
    def SetReport(self, theReport: Message_Report) -> None: ...

class Message_ProgressSentry(Message_ProgressScope):
    def __init__(self, theRange: Message_ProgressRange, theName: str, theMin: float, theMax: float, theStep: float, theIsInf: Optional[bool] = False, theNewScopeSpan: Optional[float] = 0.0) -> None: ...
    def Relieve(self) -> None: ...

#classnotwrapped
class Message_ProgressScope: ...

# harray1 classes
# harray2 classes
# hsequence classes

message_DefaultMessenger = message.DefaultMessenger
message_DefaultReport = message.DefaultReport
message_FillTime = message.FillTime
message_MetricFromString = message.MetricFromString
message_MetricFromString = message.MetricFromString
message_MetricToString = message.MetricToString
message_ToMessageMetric = message.ToMessageMetric
message_ToOSDMetric = message.ToOSDMetric
Message_Algorithm_PrepareReport = Message_Algorithm.PrepareReport
Message_Algorithm_PrepareReport = Message_Algorithm.PrepareReport
Message_ExecStatus_LocalStatusIndex = Message_ExecStatus.LocalStatusIndex
Message_ExecStatus_StatusByIndex = Message_ExecStatus.StatusByIndex
Message_ExecStatus_StatusIndex = Message_ExecStatus.StatusIndex
Message_ExecStatus_TypeOfStatus = Message_ExecStatus.TypeOfStatus
Message_MsgFile_AddMsg = Message_MsgFile.AddMsg
Message_MsgFile_HasMsg = Message_MsgFile.HasMsg
Message_MsgFile_Load = Message_MsgFile.Load
Message_MsgFile_LoadFile = Message_MsgFile.LoadFile
Message_MsgFile_LoadFromEnv = Message_MsgFile.LoadFromEnv
Message_MsgFile_LoadFromString = Message_MsgFile.LoadFromString
Message_MsgFile_Msg = Message_MsgFile.Msg
Message_MsgFile_Msg = Message_MsgFile.Msg
Message_ProgressIndicator_Start = Message_ProgressIndicator.Start
Message_AlertExtended_AddAlert = Message_AlertExtended.AddAlert
Message_AttributeMeter_SetAlertMetrics = Message_AttributeMeter.SetAlertMetrics
Message_AttributeMeter_StartAlert = Message_AttributeMeter.StartAlert
Message_AttributeMeter_StopAlert = Message_AttributeMeter.StopAlert
Message_AttributeMeter_UndefinedMetricValue = Message_AttributeMeter.UndefinedMetricValue
Message_PrinterOStream_SetConsoleTextColor = Message_PrinterOStream.SetConsoleTextColor
