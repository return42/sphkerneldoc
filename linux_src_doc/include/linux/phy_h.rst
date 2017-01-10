.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/phy.h

.. _`phy_supported_speeds`:

phy_supported_speeds
====================

.. c:function:: unsigned int phy_supported_speeds(struct phy_device *phy, unsigned int *speeds, unsigned int size)

    return all speeds currently supported by a phy device

    :param struct phy_device \*phy:
        The phy device to return supported speeds of.

    :param unsigned int \*speeds:
        buffer to store supported speeds in.

    :param unsigned int size:
        size of speeds buffer.

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

    :param phy_interface_t interface:
        *undescribed*

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

    :param struct phy_device \*phydev:
        The phy_device struct

    :param int devad:
        The MMD to read from

    :param u32 regnum:
        The register on the MMD to read

.. _`phy_read_mmd.description`:

Description
-----------

Same rules as for \ :c:func:`phy_read`\ ;

.. _`phy_read_mmd_indirect`:

phy_read_mmd_indirect
=====================

.. c:function:: int phy_read_mmd_indirect(struct phy_device *phydev, int prtad, int devad)

    reads data from the MMD registers

    :param struct phy_device \*phydev:
        The PHY device bus

    :param int prtad:
        MMD Address

    :param int devad:
        *undescribed*

.. _`phy_read_mmd_indirect.description`:

Description
-----------

it reads data from the MMD registers (clause 22 to access to
clause 45) of the specified phy address.

.. _`phy_read`:

phy_read
========

.. c:function:: int phy_read(struct phy_device *phydev, u32 regnum)

    Convenience function for reading a given PHY register

    :param struct phy_device \*phydev:
        the phy_device struct

    :param u32 regnum:
        register number to read

.. _`phy_read.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`phy_write`:

phy_write
=========

.. c:function:: int phy_write(struct phy_device *phydev, u32 regnum, u16 val)

    Convenience function for writing a given PHY register

    :param struct phy_device \*phydev:
        the phy_device struct

    :param u32 regnum:
        register number to write

    :param u16 val:
        value to write to \ ``regnum``\ 

.. _`phy_write.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`phy_interrupt_is_valid`:

phy_interrupt_is_valid
======================

.. c:function:: bool phy_interrupt_is_valid(struct phy_device *phydev)

    Convenience function for testing a given PHY irq

    :param struct phy_device \*phydev:
        the phy_device struct

.. _`phy_interrupt_is_valid.note`:

NOTE
----

must be kept in sync with addition/removal of PHY_POLL and
PHY_IGNORE_INTERRUPT

.. _`phy_is_internal`:

phy_is_internal
===============

.. c:function:: bool phy_is_internal(struct phy_device *phydev)

    Convenience function for testing if a PHY is internal

    :param struct phy_device \*phydev:
        the phy_device struct

.. _`phy_interface_is_rgmii`:

phy_interface_is_rgmii
======================

.. c:function:: bool phy_interface_is_rgmii(struct phy_device *phydev)

    Convenience function for testing if a PHY interface is RGMII (all variants)

    :param struct phy_device \*phydev:
        the phy_device struct

.. _`phy_write_mmd`:

phy_write_mmd
=============

.. c:function:: int phy_write_mmd(struct phy_device *phydev, int devad, u32 regnum, u16 val)

    Convenience function for writing a register on an MMD on a given PHY.

    :param struct phy_device \*phydev:
        The phy_device struct

    :param int devad:
        The MMD to read from

    :param u32 regnum:
        The register on the MMD to read

    :param u16 val:
        value to write to \ ``regnum``\ 

.. _`phy_write_mmd.description`:

Description
-----------

Same rules as for \ :c:func:`phy_write`\ ;

.. _`phy_write_mmd_indirect`:

phy_write_mmd_indirect
======================

.. c:function:: void phy_write_mmd_indirect(struct phy_device *phydev, int prtad, int devad, u32 data)

    writes data to the MMD registers

    :param struct phy_device \*phydev:
        The PHY device

    :param int prtad:
        MMD Address

    :param int devad:
        MMD DEVAD

    :param u32 data:
        data to write in the MMD register

.. _`phy_write_mmd_indirect.description`:

Description
-----------

Write data from the MMD registers of the specified
phy address.

.. _`phy_module_driver`:

phy_module_driver
=================

.. c:function::  phy_module_driver( __phy_drivers,  __count)

    Helper macro for registering PHY drivers

    :param  __phy_drivers:
        array of PHY drivers to register

    :param  __count:
        *undescribed*

.. _`phy_module_driver.description`:

Description
-----------

Helper macro for PHY drivers which do not do anything special in module
init/exit. Each module may only use this macro once, and calling it
replaces \ :c:func:`module_init`\  and \ :c:func:`module_exit`\ .

.. This file was automatic generated / don't edit.

