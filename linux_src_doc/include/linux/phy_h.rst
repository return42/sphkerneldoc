.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/phy.h

.. _`phy_supported_speeds`:

phy_supported_speeds
====================

.. c:function:: unsigned int phy_supported_speeds(struct phy_device *phy, unsigned int *speeds, unsigned int size)

    return all speeds currently supported by a phy device

    :param phy:
        The phy device to return supported speeds of.
    :type phy: struct phy_device \*

    :param speeds:
        buffer to store supported speeds in.
    :type speeds: unsigned int \*

    :param size:
        size of speeds buffer.
    :type size: unsigned int

.. _`phy_supported_speeds.description`:

Description
-----------

Returns the number of supported speeds, and
fills the speeds \* buffer with the supported speeds. If speeds buffer is
too small to contain \* all currently supported speeds, will return as
many speeds as can fit.

.. _`phy_modes`:

phy_modes
=========

.. c:function:: const char *phy_modes(phy_interface_t interface)

    into the device tree binding of 'phy-mode', so that Ethernet device driver can get phy interface from device tree.

    :param interface:
        *undescribed*
    :type interface: phy_interface_t

.. _`phy_c45_device_ids`:

struct phy_c45_device_ids
=========================

.. c:type:: struct phy_c45_device_ids

    802.3-c45 Device Identifiers

.. _`phy_c45_device_ids.definition`:

Definition
----------

.. code-block:: c

    struct phy_c45_device_ids {
        u32 devices_in_package;
        u32 device_ids[8];
    }

.. _`phy_c45_device_ids.members`:

Members
-------

devices_in_package
    Bit vector of devices present.

device_ids
    The device identifer for each present device.

.. _`phy_read_mmd`:

phy_read_mmd
============

.. c:function:: int phy_read_mmd(struct phy_device *phydev, int devad, u32 regnum)

    Convenience function for reading a register from an MMD on a given PHY.

    :param phydev:
        The phy_device struct
    :type phydev: struct phy_device \*

    :param devad:
        The MMD to read from
    :type devad: int

    :param regnum:
        The register on the MMD to read
    :type regnum: u32

.. _`phy_read_mmd.description`:

Description
-----------

Same rules as for \ :c:func:`phy_read`\ ;

.. _`phy_read`:

phy_read
========

.. c:function:: int phy_read(struct phy_device *phydev, u32 regnum)

    Convenience function for reading a given PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to read
    :type regnum: u32

.. _`phy_read.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`__phy_read`:

\__phy_read
===========

.. c:function:: int __phy_read(struct phy_device *phydev, u32 regnum)

    convenience function for reading a given PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to read
    :type regnum: u32

.. _`__phy_read.description`:

Description
-----------

The caller must have taken the MDIO bus lock.

.. _`phy_write`:

phy_write
=========

.. c:function:: int phy_write(struct phy_device *phydev, u32 regnum, u16 val)

    Convenience function for writing a given PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        value to write to \ ``regnum``\ 
    :type val: u16

.. _`phy_write.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`__phy_write`:

\__phy_write
============

.. c:function:: int __phy_write(struct phy_device *phydev, u32 regnum, u16 val)

    Convenience function for writing a given PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        value to write to \ ``regnum``\ 
    :type val: u16

.. _`__phy_write.description`:

Description
-----------

The caller must have taken the MDIO bus lock.

.. _`__phy_set_bits`:

\__phy_set_bits
===============

.. c:function:: int __phy_set_bits(struct phy_device *phydev, u32 regnum, u16 val)

    Convenience function for setting bits in a PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        bits to set
    :type val: u16

.. _`__phy_set_bits.description`:

Description
-----------

The caller must have taken the MDIO bus lock.

.. _`__phy_clear_bits`:

\__phy_clear_bits
=================

.. c:function:: int __phy_clear_bits(struct phy_device *phydev, u32 regnum, u16 val)

    Convenience function for clearing bits in a PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        bits to clear
    :type val: u16

.. _`__phy_clear_bits.description`:

Description
-----------

The caller must have taken the MDIO bus lock.

.. _`phy_set_bits`:

phy_set_bits
============

.. c:function:: int phy_set_bits(struct phy_device *phydev, u32 regnum, u16 val)

    Convenience function for setting bits in a PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        bits to set
    :type val: u16

.. _`phy_clear_bits`:

phy_clear_bits
==============

.. c:function:: int phy_clear_bits(struct phy_device *phydev, u32 regnum, u16 val)

    Convenience function for clearing bits in a PHY register

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        bits to clear
    :type val: u16

.. _`phy_interrupt_is_valid`:

phy_interrupt_is_valid
======================

.. c:function:: bool phy_interrupt_is_valid(struct phy_device *phydev)

    Convenience function for testing a given PHY irq

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

.. _`phy_interrupt_is_valid.note`:

NOTE
----

must be kept in sync with addition/removal of PHY_POLL and
PHY_IGNORE_INTERRUPT

.. _`phy_polling_mode`:

phy_polling_mode
================

.. c:function:: bool phy_polling_mode(struct phy_device *phydev)

    Convenience function for testing whether polling is used to detect PHY status changes

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

.. _`phy_is_internal`:

phy_is_internal
===============

.. c:function:: bool phy_is_internal(struct phy_device *phydev)

    Convenience function for testing if a PHY is internal

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

.. _`phy_interface_mode_is_rgmii`:

phy_interface_mode_is_rgmii
===========================

.. c:function:: bool phy_interface_mode_is_rgmii(phy_interface_t mode)

    Convenience function for testing if a PHY interface mode is RGMII (all variants)

    :param mode:
        the phy_interface_t enum
    :type mode: phy_interface_t

.. _`phy_interface_mode_is_8023z`:

phy_interface_mode_is_8023z
===========================

.. c:function:: bool phy_interface_mode_is_8023z(phy_interface_t mode)

    does the phy interface mode use 802.3z negotiation

    :param mode:
        one of \ :c:type:`enum phy_interface_t <phy_interface_t>`\ 
    :type mode: phy_interface_t

.. _`phy_interface_mode_is_8023z.description`:

Description
-----------

Returns true if the phy interface mode uses the 16-bit negotiation
word as defined in 802.3z. (See 802.3-2015 37.2.1 Config_Reg encoding)

.. _`phy_interface_is_rgmii`:

phy_interface_is_rgmii
======================

.. c:function:: bool phy_interface_is_rgmii(struct phy_device *phydev)

    Convenience function for testing if a PHY interface is RGMII (all variants)

    :param phydev:
        the phy_device struct
    :type phydev: struct phy_device \*

.. _`phy_write_mmd`:

phy_write_mmd
=============

.. c:function:: int phy_write_mmd(struct phy_device *phydev, int devad, u32 regnum, u16 val)

    Convenience function for writing a register on an MMD on a given PHY.

    :param phydev:
        The phy_device struct
    :type phydev: struct phy_device \*

    :param devad:
        The MMD to read from
    :type devad: int

    :param regnum:
        The register on the MMD to read
    :type regnum: u32

    :param val:
        value to write to \ ``regnum``\ 
    :type val: u16

.. _`phy_write_mmd.description`:

Description
-----------

Same rules as for \ :c:func:`phy_write`\ ;

.. _`phy_module_driver`:

phy_module_driver
=================

.. c:function::  phy_module_driver( __phy_drivers,  __count)

    Helper macro for registering PHY drivers

    :param __phy_drivers:
        array of PHY drivers to register
    :type __phy_drivers: 

    :param __count:
        *undescribed*
    :type __count: 

.. _`phy_module_driver.description`:

Description
-----------

Helper macro for PHY drivers which do not do anything special in module
init/exit. Each module may only use this macro once, and calling it
replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ .

.. This file was automatic generated / don't edit.

