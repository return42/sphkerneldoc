.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/rtl8723bs/hal/rtl8723b_phycfg.c

.. _`phy_calculatebitshift`:

phy_CalculateBitShift
=====================

.. c:function:: u32 phy_CalculateBitShift(u32 BitMask)

    phy_CalculateBitShift

    :param BitMask:
        *undescribed*
    :type BitMask: u32

.. _`phy_calculatebitshift.overview`:

OverView
--------

Get shifted position of the BitMask

.. _`phy_calculatebitshift.input`:

Input
-----

u32     BitMask,

.. _`phy_calculatebitshift.output`:

Output
------

none

.. _`phy_calculatebitshift.return`:

Return
------

u32     Return the shift bit bit position of the mask

.. _`phy_querybbreg_8723b`:

PHY_QueryBBReg_8723B
====================

.. c:function:: u32 PHY_QueryBBReg_8723B(struct adapter *Adapter, u32 RegAddr, u32 BitMask)

    PHY_QueryBBReg

    :param Adapter:
        *undescribed*
    :type Adapter: struct adapter \*

    :param RegAddr:
        *undescribed*
    :type RegAddr: u32

    :param BitMask:
        *undescribed*
    :type BitMask: u32

.. _`phy_querybbreg_8723b.overview`:

OverView
--------

Read "sepcific bits" from BB register

.. _`phy_querybbreg_8723b.input`:

Input
-----

struct adapter \*        Adapter,
u32             RegAddr,        The target address to be readback
u32             BitMask         The target bit position in the target address
to be readback

.. _`phy_querybbreg_8723b.output`:

Output
------

None

.. _`phy_querybbreg_8723b.return`:

Return
------

u32             Data            The readback register value

.. _`phy_querybbreg_8723b.note`:

Note
----

This function is equal to "GetRegSetting" in PHY programming guide

.. _`phy_setbbreg_8723b`:

PHY_SetBBReg_8723B
==================

.. c:function:: void PHY_SetBBReg_8723B(struct adapter *Adapter, u32 RegAddr, u32 BitMask, u32 Data)

    PHY_SetBBReg

    :param Adapter:
        *undescribed*
    :type Adapter: struct adapter \*

    :param RegAddr:
        *undescribed*
    :type RegAddr: u32

    :param BitMask:
        *undescribed*
    :type BitMask: u32

    :param Data:
        *undescribed*
    :type Data: u32

.. _`phy_setbbreg_8723b.overview`:

OverView
--------

Write "Specific bits" to BB register (page 8~)

.. _`phy_setbbreg_8723b.input`:

Input
-----

struct adapter \*        Adapter,
u32             RegAddr,        The target address to be modified
u32             BitMask         The target bit position in the target address
to be modified
u32             Data            The new register value in the target bit position
of the target address

.. _`phy_setbbreg_8723b.output`:

Output
------

None

.. _`phy_setbbreg_8723b.return`:

Return
------

None

.. _`phy_setbbreg_8723b.note`:

Note
----

This function is equal to "PutRegSetting" in PHY programming guide

.. _`phy_rfserialwrite_8723b`:

phy_RFSerialWrite_8723B
=======================

.. c:function:: void phy_RFSerialWrite_8723B(struct adapter *Adapter, enum RF_PATH eRFPath, u32 Offset, u32 Data)

    phy_RFSerialWrite_8723B

    :param Adapter:
        *undescribed*
    :type Adapter: struct adapter \*

    :param eRFPath:
        *undescribed*
    :type eRFPath: enum RF_PATH

    :param Offset:
        *undescribed*
    :type Offset: u32

    :param Data:
        *undescribed*
    :type Data: u32

.. _`phy_rfserialwrite_8723b.overview`:

OverView
--------

Write data to RF register (page 8~)

.. _`phy_rfserialwrite_8723b.input`:

Input
-----

struct adapter \*        Adapter,
RF_PATH                 eRFPath,        Radio path of A/B/C/D
u32             Offset,         The target address to be read
u32             Data            The new register Data in the target bit position
of the target to be read

.. _`phy_rfserialwrite_8723b.output`:

Output
------

None

.. _`phy_rfserialwrite_8723b.return`:

Return
------

None

.. _`phy_rfserialwrite_8723b.note`:

Note
----

Threre are three types of serial operations:
1. Software serial write
2. Hardware LSSI-Low Speed Serial Interface
3. Hardware HSSI-High speed
serial write. Driver need to implement (1) and (2).
This function is equal to the combination of \ :c:func:`RF_ReadReg`\  and  \ :c:func:`RFLSSIRead`\ 

For RF8256 only
The total count of RTL8256(Zebra4) register is around 36 bit it only employs
4-bit RF address. RTL8256 uses "register mode control bit" (Reg00[12], Reg00[10])
to access register address bigger than 0xf. See "Appendix-4 in PHY Configuration
programming guide" for more details.
Thus, we define a sub-finction for RTL8526 register address conversion
===========================================================
Register Mode          RegCTL[1]               RegCTL[0]               Note
(Reg00[12])             (Reg00[10])
===========================================================
Reg_Mode0                              0                               x                       Reg 0 ~15(0x0 ~ 0xf)
------------------------------------------------------------------
Reg_Mode1                              1                               0                       Reg 16 ~30(0x1 ~ 0xf)
------------------------------------------------------------------
Reg_Mode2                              1                               1                       Reg 31 ~ 45(0x1 ~ 0xf)
------------------------------------------------------------------

2008/09/02    MH      Add 92S RF definition

.. _`phy_queryrfreg_8723b`:

PHY_QueryRFReg_8723B
====================

.. c:function:: u32 PHY_QueryRFReg_8723B(struct adapter *Adapter, u8 eRFPath, u32 RegAddr, u32 BitMask)

    PHY_QueryRFReg

    :param Adapter:
        *undescribed*
    :type Adapter: struct adapter \*

    :param eRFPath:
        *undescribed*
    :type eRFPath: u8

    :param RegAddr:
        *undescribed*
    :type RegAddr: u32

    :param BitMask:
        *undescribed*
    :type BitMask: u32

.. _`phy_queryrfreg_8723b.overview`:

OverView
--------

Query "Specific bits" to RF register (page 8~)

.. _`phy_queryrfreg_8723b.input`:

Input
-----

struct adapter \*        Adapter,
RF_PATH                 eRFPath,        Radio path of A/B/C/D
u32             RegAddr,        The target address to be read
u32             BitMask         The target bit position in the target address
to be read

.. _`phy_queryrfreg_8723b.output`:

Output
------

None

.. _`phy_queryrfreg_8723b.return`:

Return
------

u32             Readback value

.. _`phy_queryrfreg_8723b.note`:

Note
----

This function is equal to "GetRFRegSetting" in PHY programming guide

.. _`phy_setrfreg_8723b`:

PHY_SetRFReg_8723B
==================

.. c:function:: void PHY_SetRFReg_8723B(struct adapter *Adapter, u8 eRFPath, u32 RegAddr, u32 BitMask, u32 Data)

    PHY_SetRFReg

    :param Adapter:
        *undescribed*
    :type Adapter: struct adapter \*

    :param eRFPath:
        *undescribed*
    :type eRFPath: u8

    :param RegAddr:
        *undescribed*
    :type RegAddr: u32

    :param BitMask:
        *undescribed*
    :type BitMask: u32

    :param Data:
        *undescribed*
    :type Data: u32

.. _`phy_setrfreg_8723b.overview`:

OverView
--------

Write "Specific bits" to RF register (page 8~)

.. _`phy_setrfreg_8723b.input`:

Input
-----

struct adapter \*        Adapter,
RF_PATH                 eRFPath,        Radio path of A/B/C/D
u32             RegAddr,        The target address to be modified
u32             BitMask         The target bit position in the target address
to be modified
u32             Data            The new register Data in the target bit position
of the target address

.. _`phy_setrfreg_8723b.output`:

Output
------

None

.. _`phy_setrfreg_8723b.return`:

Return
------

None

.. _`phy_setrfreg_8723b.note`:

Note
----

This function is equal to "PutRFRegSetting" in PHY programming guide

.. _`phy_initbbrfregisterdefinition`:

phy_InitBBRFRegisterDefinition
==============================

.. c:function:: void phy_InitBBRFRegisterDefinition(struct adapter *Adapter)

    phy_InitBBRFRegisterDefinition

    :param Adapter:
        *undescribed*
    :type Adapter: struct adapter \*

.. _`phy_initbbrfregisterdefinition.overview`:

OverView
--------

Initialize Register definition offset for Radio Path A/B/C/D

.. _`phy_initbbrfregisterdefinition.input`:

Input
-----

struct adapter \*        Adapter,

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

