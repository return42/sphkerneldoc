.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/phy/mdio_bus.c

.. _`mdiobus_alloc_size`:

mdiobus_alloc_size
==================

.. c:function:: struct mii_bus *mdiobus_alloc_size(size_t size)

    allocate a mii_bus structure

    :param size:
        extra amount of memory to allocate for private storage.
        If non-zero, then bus->priv is points to that memory.
    :type size: size_t

.. _`mdiobus_alloc_size.description`:

Description
-----------

called by a bus driver to allocate an mii_bus
structure to fill in.

.. _`devm_mdiobus_alloc_size`:

devm_mdiobus_alloc_size
=======================

.. c:function:: struct mii_bus *devm_mdiobus_alloc_size(struct device *dev, int sizeof_priv)

    Resource-managed \ :c:func:`mdiobus_alloc_size`\ 

    :param dev:
        Device to allocate mii_bus for
    :type dev: struct device \*

    :param sizeof_priv:
        Space to allocate for private structure.
    :type sizeof_priv: int

.. _`devm_mdiobus_alloc_size.description`:

Description
-----------

Managed mdiobus_alloc_size. mii_bus allocated with this function is
automatically freed on driver detach.

If an mii_bus allocated with this function needs to be freed separately,
\ :c:func:`devm_mdiobus_free`\  must be used.

.. _`devm_mdiobus_alloc_size.return`:

Return
------

Pointer to allocated mii_bus on success, NULL on failure.

.. _`devm_mdiobus_free`:

devm_mdiobus_free
=================

.. c:function:: void devm_mdiobus_free(struct device *dev, struct mii_bus *bus)

    Resource-managed \ :c:func:`mdiobus_free`\ 

    :param dev:
        Device this mii_bus belongs to
    :type dev: struct device \*

    :param bus:
        the mii_bus associated with the device
    :type bus: struct mii_bus \*

.. _`devm_mdiobus_free.description`:

Description
-----------

Free mii_bus allocated with \ :c:func:`devm_mdiobus_alloc_size`\ .

.. _`mdiobus_release`:

mdiobus_release
===============

.. c:function:: void mdiobus_release(struct device *d)

    mii_bus device release callback

    :param d:
        the target struct device that contains the mii_bus
    :type d: struct device \*

.. _`mdiobus_release.description`:

Description
-----------

called when the last reference to an mii_bus is
dropped, to free the underlying memory.

.. _`of_mdio_find_bus`:

of_mdio_find_bus
================

.. c:function:: struct mii_bus *of_mdio_find_bus(struct device_node *mdio_bus_np)

    Given an mii_bus node, find the mii_bus.

    :param mdio_bus_np:
        Pointer to the mii_bus.
    :type mdio_bus_np: struct device_node \*

.. _`of_mdio_find_bus.description`:

Description
-----------

Returns a reference to the mii_bus, or NULL if none found.  The
embedded struct device will have its reference count incremented,
and this must be put once the bus is finished with.

Because the association of a device_node and mii_bus is made via
\ :c:func:`of_mdiobus_register`\ , the mii_bus cannot be found before it is
registered with \ :c:func:`of_mdiobus_register`\ .

.. _`mdiobus_create_device`:

mdiobus_create_device
=====================

.. c:function:: int mdiobus_create_device(struct mii_bus *bus, struct mdio_board_info *bi)

    create a full MDIO device given a mdio_board_info structure

    :param bus:
        MDIO bus to create the devices on
    :type bus: struct mii_bus \*

    :param bi:
        mdio_board_info structure describing the devices
    :type bi: struct mdio_board_info \*

.. _`mdiobus_create_device.description`:

Description
-----------

Returns 0 on success or < 0 on error.

.. _`__mdiobus_register`:

__mdiobus_register
==================

.. c:function:: int __mdiobus_register(struct mii_bus *bus, struct module *owner)

    bring up all the PHYs on a given bus and attach them to bus

    :param bus:
        target mii_bus
    :type bus: struct mii_bus \*

    :param owner:
        module containing bus accessor functions
    :type owner: struct module \*

.. _`__mdiobus_register.description`:

Description
-----------

Called by a bus driver to bring up all the PHYs
  on a given bus, and attach them to the bus. Drivers should use
  \ :c:func:`mdiobus_register`\  rather than \ :c:func:`__mdiobus_register`\  unless they
  need to pass a specific owner module. MDIO devices which are not
  PHYs will not be brought up by this function. They are expected to
  to be explicitly listed in DT and instantiated by \ :c:func:`of_mdiobus_register`\ .

Returns 0 on success or < 0 on error.

.. _`mdiobus_free`:

mdiobus_free
============

.. c:function:: void mdiobus_free(struct mii_bus *bus)

    free a struct mii_bus

    :param bus:
        mii_bus to free
    :type bus: struct mii_bus \*

.. _`mdiobus_free.description`:

Description
-----------

This function releases the reference to the underlying device
object in the mii_bus.  If this is the last reference, the mii_bus
will be freed.

.. _`mdiobus_scan`:

mdiobus_scan
============

.. c:function:: struct phy_device *mdiobus_scan(struct mii_bus *bus, int addr)

    scan a bus for MDIO devices.

    :param bus:
        mii_bus to scan
    :type bus: struct mii_bus \*

    :param addr:
        address on bus to scan
    :type addr: int

.. _`mdiobus_scan.description`:

Description
-----------

This function scans the MDIO bus, looking for devices which can be
identified using a vendor/product ID in registers 2 and 3. Not all
MDIO devices have such registers, but PHY devices typically
do. Hence this function assumes anything found is a PHY, or can be
treated as a PHY. Other MDIO devices, such as switches, will
probably not be found during the scan.

.. _`__mdiobus_read`:

__mdiobus_read
==============

.. c:function:: int __mdiobus_read(struct mii_bus *bus, int addr, u32 regnum)

    Unlocked version of the mdiobus_read function

    :param bus:
        the mii_bus struct
    :type bus: struct mii_bus \*

    :param addr:
        the phy address
    :type addr: int

    :param regnum:
        register number to read
    :type regnum: u32

.. _`__mdiobus_read.description`:

Description
-----------

Read a MDIO bus register. Caller must hold the mdio bus lock.

.. _`__mdiobus_read.note`:

NOTE
----

MUST NOT be called from interrupt context.

.. _`__mdiobus_write`:

__mdiobus_write
===============

.. c:function:: int __mdiobus_write(struct mii_bus *bus, int addr, u32 regnum, u16 val)

    Unlocked version of the mdiobus_write function

    :param bus:
        the mii_bus struct
    :type bus: struct mii_bus \*

    :param addr:
        the phy address
    :type addr: int

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        value to write to \ ``regnum``\ 
    :type val: u16

.. _`__mdiobus_write.description`:

Description
-----------

Write a MDIO bus register. Caller must hold the mdio bus lock.

.. _`__mdiobus_write.note`:

NOTE
----

MUST NOT be called from interrupt context.

.. _`mdiobus_read_nested`:

mdiobus_read_nested
===================

.. c:function:: int mdiobus_read_nested(struct mii_bus *bus, int addr, u32 regnum)

    Nested version of the mdiobus_read function

    :param bus:
        the mii_bus struct
    :type bus: struct mii_bus \*

    :param addr:
        the phy address
    :type addr: int

    :param regnum:
        register number to read
    :type regnum: u32

.. _`mdiobus_read_nested.description`:

Description
-----------

In case of nested MDIO bus access avoid lockdep false positives by
using \ :c:func:`mutex_lock_nested`\ .

.. _`mdiobus_read_nested.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`mdiobus_read`:

mdiobus_read
============

.. c:function:: int mdiobus_read(struct mii_bus *bus, int addr, u32 regnum)

    Convenience function for reading a given MII mgmt register

    :param bus:
        the mii_bus struct
    :type bus: struct mii_bus \*

    :param addr:
        the phy address
    :type addr: int

    :param regnum:
        register number to read
    :type regnum: u32

.. _`mdiobus_read.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`mdiobus_write_nested`:

mdiobus_write_nested
====================

.. c:function:: int mdiobus_write_nested(struct mii_bus *bus, int addr, u32 regnum, u16 val)

    Nested version of the mdiobus_write function

    :param bus:
        the mii_bus struct
    :type bus: struct mii_bus \*

    :param addr:
        the phy address
    :type addr: int

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        value to write to \ ``regnum``\ 
    :type val: u16

.. _`mdiobus_write_nested.description`:

Description
-----------

In case of nested MDIO bus access avoid lockdep false positives by
using \ :c:func:`mutex_lock_nested`\ .

.. _`mdiobus_write_nested.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`mdiobus_write`:

mdiobus_write
=============

.. c:function:: int mdiobus_write(struct mii_bus *bus, int addr, u32 regnum, u16 val)

    Convenience function for writing a given MII mgmt register

    :param bus:
        the mii_bus struct
    :type bus: struct mii_bus \*

    :param addr:
        the phy address
    :type addr: int

    :param regnum:
        register number to write
    :type regnum: u32

    :param val:
        value to write to \ ``regnum``\ 
    :type val: u16

.. _`mdiobus_write.note`:

NOTE
----

MUST NOT be called from interrupt context,
because the bus read/write functions may wait for an interrupt
to conclude the operation.

.. _`mdio_bus_match`:

mdio_bus_match
==============

.. c:function:: int mdio_bus_match(struct device *dev, struct device_driver *drv)

    determine if given MDIO driver supports the given MDIO device

    :param dev:
        target MDIO device
    :type dev: struct device \*

    :param drv:
        given MDIO driver
    :type drv: struct device_driver \*

.. _`mdio_bus_match.description`:

Description
-----------

Given a MDIO device, and a MDIO driver, return 1 if
  the driver supports the device.  Otherwise, return 0. This may
  require calling the devices own match function, since different classes
  of MDIO devices have different match criteria.

.. This file was automatic generated / don't edit.

