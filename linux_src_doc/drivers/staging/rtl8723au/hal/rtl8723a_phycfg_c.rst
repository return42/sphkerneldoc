.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8723au/hal/rtl8723a_phycfg.c

.. _`phy_calculatebitshift`:

phy_CalculateBitShift
=====================

.. c:function:: u32 phy_CalculateBitShift(u32 BitMask)

    phy_CalculateBitShift

    :param u32 BitMask:
        *undescribed*

.. _`phy_calculatebitshift.overview`:

OverView
--------

Get shifted position of the BitMask

.. _`phy_calculatebitshift.input`:

Input
-----

u32             BitMask,

.. _`phy_calculatebitshift.output`:

Output
------

none

.. _`phy_calculatebitshift.return`:

Return
------

u32             Return the shift bit bit position of the mask

.. _`phy_querybbreg`:

PHY_QueryBBReg
==============

.. c:function:: u32 PHY_QueryBBReg(struct rtw_adapter *Adapter, u32 RegAddr, u32 BitMask)

    PHY_QueryBBReg

    :param struct rtw_adapter \*Adapter:
        *undescribed*

    :param u32 RegAddr:
        *undescribed*

    :param u32 BitMask:
        *undescribed*

.. _`phy_querybbreg.overview`:

OverView
--------

Read "sepcific bits" from BB register

.. _`phy_querybbreg.input`:

Input
-----

struct rtw_adapter \*    Adapter,
u32                     RegAddr,        Target address to be readback
u32                     BitMask         Target bit position in the
target address to be readback

.. _`phy_querybbreg.output`:

Output
------

None

.. _`phy_querybbreg.return`:

Return
------

u32                     Data            The readback register value

.. _`phy_querybbreg.note`:

Note
----

This function is equal to "GetRegSetting" in PHY programming guide

.. _`phy_setbbreg`:

PHY_SetBBReg
============

.. c:function:: void PHY_SetBBReg(struct rtw_adapter *Adapter, u32 RegAddr, u32 BitMask, u32 Data)

    PHY_SetBBReg

    :param struct rtw_adapter \*Adapter:
        *undescribed*

    :param u32 RegAddr:
        *undescribed*

    :param u32 BitMask:
        *undescribed*

    :param u32 Data:
        *undescribed*

.. _`phy_setbbreg.overview`:

OverView
--------

Write "Specific bits" to BB register (page 8~)

.. _`phy_setbbreg.input`:

Input
-----

struct rtw_adapter \*    Adapter,
u32                     RegAddr,        Target address to be modified
u32                     BitMask         Target bit position in the
target address to be modified
u32                     Data            The new register value in the
target bit position of the
target address

.. _`phy_setbbreg.output`:

Output
------

None

.. _`phy_setbbreg.return`:

Return
------

None

.. _`phy_setbbreg.note`:

Note
----

This function is equal to "PutRegSetting" in PHY programming guide

.. _`phy_rfserialread`:

phy_RFSerialRead
================

.. c:function:: u32 phy_RFSerialRead(struct rtw_adapter *Adapter, enum RF_RADIO_PATH eRFPath, u32 Offset)

    phy_RFSerialRead

    :param struct rtw_adapter \*Adapter:
        *undescribed*

    :param enum RF_RADIO_PATH eRFPath:
        *undescribed*

    :param u32 Offset:
        *undescribed*

.. _`phy_rfserialread.overview`:

OverView
--------

Read regster from RF chips

.. _`phy_rfserialread.input`:

Input
-----

struct rtw_adapter \*            Adapter,
enum RF_RADIO_PATH      eRFPath,        Radio path of A/B/C/D
u32 Offset,                     The target address to be read

.. _`phy_rfserialread.output`:

Output
------

None

.. _`phy_rfserialread.return`:

Return
------

u32                     reback value

.. _`phy_rfserialread.note`:

Note
----

Threre are three types of serial operations:
1. Software serial write
2. Hardware LSSI-Low Speed Serial Interface
3. Hardware HSSI-High speed
serial write. Driver need to implement (1) and (2).
This function is equal to the combination of \ :c:func:`RF_ReadReg`\  and
\ :c:func:`RFLSSIRead`\ 

.. _`phy_rfserialwrite`:

phy_RFSerialWrite
=================

.. c:function:: void phy_RFSerialWrite(struct rtw_adapter *Adapter, enum RF_RADIO_PATH eRFPath, u32 Offset, u32 Data)

    phy_RFSerialWrite

    :param struct rtw_adapter \*Adapter:
        *undescribed*

    :param enum RF_RADIO_PATH eRFPath:
        *undescribed*

    :param u32 Offset:
        *undescribed*

    :param u32 Data:
        *undescribed*

.. _`phy_rfserialwrite.overview`:

OverView
--------

Write data to RF register (page 8~)

.. _`phy_rfserialwrite.input`:

Input
-----

struct rtw_adapter \*            Adapter,
enum RF_RADIO_PATH      eRFPath,        Radio path of A/B/C/D
u32 Offset,                     The target address to be read
u32 Data                        The new register Data in the target
bit position of the target to be read

.. _`phy_rfserialwrite.output`:

Output
------

None

.. _`phy_rfserialwrite.return`:

Return
------

None

.. _`phy_rfserialwrite.threre-are-three-types-of-serial-operations`:

Threre are three types of serial operations
-------------------------------------------

1. Software serial write
2. Hardware LSSI-Low Speed Serial Interface
3. Hardware HSSI-High speed
serial write. Driver need to implement (1) and (2).
This function is equal to the combination of \ :c:func:`RF_ReadReg`\  and
\ :c:func:`RFLSSIRead`\ 

.. _`phy_rfserialwrite.note`:

Note
----

For RF8256 only
The total count of RTL8256(Zebra4) register is around 36 bit it only employs
4-bit RF address. RTL8256 uses "register mode control bit"
(Reg00[12], Reg00[10]) to access register address bigger than 0xf.
See "Appendix-4 in PHY Configuration programming guide" for more details.
Thus, we define a sub-finction for RTL8526 register address conversion
===========================================================

.. _`phy_rfserialwrite.register-mode`:

Register Mode
-------------

RegCTL[1]       RegCTL[0]       Note
(Reg00[12])     (Reg00[10])
===========================================================
Reg_Mode0             0               x               Reg 0 ~15(0x0 ~ 0xf)
------------------------------------------------------------------
Reg_Mode1             1               0               Reg 16 ~30(0x1 ~ 0xf)
------------------------------------------------------------------
Reg_Mode2             1               1               Reg 31 ~ 45(0x1 ~ 0xf)
------------------------------------------------------------------

2008/09/02      MH      Add 92S RF definition

.. _`phy_queryrfreg`:

PHY_QueryRFReg
==============

.. c:function:: u32 PHY_QueryRFReg(struct rtw_adapter *Adapter, enum RF_RADIO_PATH eRFPath, u32 RegAddr, u32 BitMask)

    PHY_QueryRFReg

    :param struct rtw_adapter \*Adapter:
        *undescribed*

    :param enum RF_RADIO_PATH eRFPath:
        *undescribed*

    :param u32 RegAddr:
        *undescribed*

    :param u32 BitMask:
        *undescribed*

.. _`phy_queryrfreg.overview`:

OverView
--------

Query "Specific bits" to RF register (page 8~)

.. _`phy_queryrfreg.input`:

Input
-----

struct rtw_adapter \*            Adapter,
enum RF_RADIO_PATH      eRFPath,        Radio path of A/B/C/D
u32 RegAddr,                    The target address to be read
u32BitMask                      The target bit position in the target
address to be read

.. _`phy_queryrfreg.output`:

Output
------

None

.. _`phy_queryrfreg.return`:

Return
------

u32                             Readback value

.. _`phy_queryrfreg.note`:

Note
----

This function is equal to "GetRFRegSetting" in PHY programming guide

.. _`phy_setrfreg`:

PHY_SetRFReg
============

.. c:function:: void PHY_SetRFReg(struct rtw_adapter *Adapter, enum RF_RADIO_PATH eRFPath, u32 RegAddr, u32 BitMask, u32 Data)

    PHY_SetRFReg

    :param struct rtw_adapter \*Adapter:
        *undescribed*

    :param enum RF_RADIO_PATH eRFPath:
        *undescribed*

    :param u32 RegAddr:
        *undescribed*

    :param u32 BitMask:
        *undescribed*

    :param u32 Data:
        *undescribed*

.. _`phy_setrfreg.overview`:

OverView
--------

Write "Specific bits" to RF register (page 8~)

.. _`phy_setrfreg.input`:

Input
-----

struct rtw_adapter \*            Adapter,
enum RF_RADIO_PATH      eRFPath,        Radio path of A/B/C/D
u32 RegAddr,                    The target address to be modified
u32 BitMask                     The target bit position in the target
address to be modified
u32 Data                        The new register Data in the target
bit position of the target address

.. _`phy_setrfreg.output`:

Output
------

None

.. _`phy_setrfreg.return`:

Return
------

None

.. _`phy_setrfreg.note`:

Note
----

This function is equal to "PutRFRegSetting" in PHY programming guide

.. _`phy_initbbrfregisterdefinition`:

phy_InitBBRFRegisterDefinition
==============================

.. c:function:: void phy_InitBBRFRegisterDefinition(struct rtw_adapter *Adapter)

    phy_InitBBRFRegisterDefinition

    :param struct rtw_adapter \*Adapter:
        *undescribed*

.. _`phy_initbbrfregisterdefinition.overview`:

OverView
--------

Initialize Register definition offset for Radio Path A/B/C/D

.. _`phy_initbbrfregisterdefinition.input`:

Input
-----

struct rtw_adapter \*            Adapter,

.. _`phy_initbbrfregisterdefinition.output`:

Output
------

None

.. _`phy_initbbrfregisterdefinition.return`:

Return
------

None

.. _`phy_initbbrfregisterdefinition.note`:

Note
----

The initialization value is constant and it should never be changes

.. This file was automatic generated / don't edit.

