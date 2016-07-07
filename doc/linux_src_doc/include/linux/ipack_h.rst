.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ipack.h

.. _`ipack_device`:

struct ipack_device
===================

.. c:type:: struct ipack_device


.. _`ipack_device.definition`:

Definition
----------

.. code-block:: c

    struct ipack_device {
        unsigned int slot;
        struct ipack_bus_device *bus;
        struct device dev;
        void (* release) (struct ipack_device *dev);
        struct ipack_region region[IPACK_SPACE_COUNT];
        u8 *id;
        size_t id_avail;
        u32 id_vendor;
        u32 id_device;
        u8 id_format;
        unsigned int id_crc_correct:1;
        unsigned int speed_8mhz:1;
        unsigned int speed_32mhz:1;
    }

.. _`ipack_device.members`:

Members
-------

slot
    Slot where the device is plugged in the carrier board

bus
    ipack_bus_device where the device is plugged to.

dev
    device in kernel representation.

release
    *undescribed*

id
    *undescribed*

id_avail
    *undescribed*

id_vendor
    *undescribed*

id_device
    *undescribed*

id_format
    *undescribed*

id_crc_correct
    *undescribed*

speed_8mhz
    *undescribed*

speed_32mhz
    *undescribed*

.. _`ipack_device.warning`:

Warning
-------

Direct access to mapped memory is possible but the endianness
is not the same with PCI carrier or VME carrier. The endianness is managed
by the carrier board throught bus->ops.

.. _`ipack_driver_ops`:

struct ipack_driver_ops
=======================

.. c:type:: struct ipack_driver_ops

    - Callbacks to IPack device driver

.. _`ipack_driver_ops.definition`:

Definition
----------

.. code-block:: c

    struct ipack_driver_ops {
        int (* probe) (struct ipack_device *dev);
        void (* remove) (struct ipack_device *dev);
    }

.. _`ipack_driver_ops.members`:

Members
-------

probe
    Probe function

remove
    Prepare imminent removal of the device.  Services provided by the
    device should be revoked.

.. _`ipack_driver`:

struct ipack_driver
===================

.. c:type:: struct ipack_driver

    - Specific data to each ipack device driver

.. _`ipack_driver.definition`:

Definition
----------

.. code-block:: c

    struct ipack_driver {
        struct device_driver driver;
        const struct ipack_device_id *id_table;
        const struct ipack_driver_ops *ops;
    }

.. _`ipack_driver.members`:

Members
-------

driver
    Device driver kernel representation

id_table
    *undescribed*

ops
    Callbacks provided by the IPack device driver

.. _`ipack_bus_ops`:

struct ipack_bus_ops
====================

.. c:type:: struct ipack_bus_ops

    available operations on a bridge module

.. _`ipack_bus_ops.definition`:

Definition
----------

.. code-block:: c

    struct ipack_bus_ops {
        int (* request_irq) (struct ipack_device *dev,irqreturn_t (*handler);
        int (* free_irq) (struct ipack_device *dev);
        int (* get_clockrate) (struct ipack_device *dev);
        int (* set_clockrate) (struct ipack_device *dev, int mherz);
        int (* get_error) (struct ipack_device *dev);
        int (* get_timeout) (struct ipack_device *dev);
        int (* reset_timeout) (struct ipack_device *dev);
    }

.. _`ipack_bus_ops.members`:

Members
-------

request_irq
    request IRQ

free_irq
    free IRQ

get_clockrate
    Returns the clockrate the carrier is currently
    communicating with the device at.

set_clockrate
    Sets the clock-rate for carrier / module communication.
    Should return -EINVAL if the requested speed is not supported.

get_error
    Returns the error state for the slot the device is attached
    to.

get_timeout
    Returns 1 if the communication with the device has
    previously timed out.

reset_timeout
    Resets the state returned by get_timeout.

.. _`ipack_bus_device`:

struct ipack_bus_device
=======================

.. c:type:: struct ipack_bus_device


.. _`ipack_bus_device.definition`:

Definition
----------

.. code-block:: c

    struct ipack_bus_device {
        struct module *owner;
        struct device *parent;
        int slots;
        int bus_nr;
        const struct ipack_bus_ops *ops;
    }

.. _`ipack_bus_device.members`:

Members
-------

owner
    *undescribed*

parent
    *undescribed*

slots
    number of slots available

bus_nr
    ipack bus number

ops
    bus operations for the mezzanine drivers

.. _`ipack_bus_register`:

ipack_bus_register
==================

.. c:function:: struct ipack_bus_device *ipack_bus_register(struct device *parent, int slots, const struct ipack_bus_ops *ops, struct module *owner)

    - register a new ipack bus

    :param struct device \*parent:
        pointer to the parent device, if any.

    :param int slots:
        number of slots available in the bus device.

    :param const struct ipack_bus_ops \*ops:
        bus operations for the mezzanine drivers.

    :param struct module \*owner:
        *undescribed*

.. _`ipack_bus_register.description`:

Description
-----------

The carrier board device should call this function to register itself as
available bus device in ipack.

.. _`ipack_bus_unregister`:

ipack_bus_unregister
====================

.. c:function:: int ipack_bus_unregister(struct ipack_bus_device *bus)

    - unregister an ipack bus

    :param struct ipack_bus_device \*bus:
        *undescribed*

.. _`ipack_driver_register`:

ipack_driver_register
=====================

.. c:function:: int ipack_driver_register(struct ipack_driver *edrv, struct module *owner, const char *name)

    - Register a new ipack device driver

    :param struct ipack_driver \*edrv:
        *undescribed*

    :param struct module \*owner:
        *undescribed*

    :param const char \*name:
        *undescribed*

.. _`ipack_driver_register.description`:

Description
-----------

Called by a ipack driver to register itself as a driver
that can manage ipack devices.

.. _`ipack_device_init`:

ipack_device_init
=================

.. c:function:: int ipack_device_init(struct ipack_device *dev)

    - initialize an IPack device

    :param struct ipack_device \*dev:
        the new device to initialize.

.. _`ipack_device_init.description`:

Description
-----------

Initialize a new IPack device ("module" in IndustryPack jargon). The call
is done by the carrier driver.  The carrier should populate the fields
bus and slot as well as the region array of \ ``dev``\  prior to calling this
function.  The rest of the fields will be allocated and populated
during initalization.

Return zero on success or error code on failure.

.. _`ipack_device_init.note`:

NOTE
----

_Never\_ directly free \ ``dev``\  after calling this function, even
if it returned an error! Always use \ :c:func:`ipack_put_device`\  to give up the
reference initialized in this function instead.

.. _`ipack_device_add`:

ipack_device_add
================

.. c:function:: int ipack_device_add(struct ipack_device *dev)

    - Add an IPack device

    :param struct ipack_device \*dev:
        the new device to add.

.. _`ipack_device_add.description`:

Description
-----------

Add a new IPack device. The call is done by the carrier driver
after calling \ :c:func:`ipack_device_init`\ .

Return zero on success or error code on failure.

.. _`ipack_device_add.note`:

NOTE
----

_Never\_ directly free \ ``dev``\  after calling this function, even
if it returned an error! Always use \ :c:func:`ipack_put_device`\  to give up the
reference initialized in this function instead.

.. _`define_ipack_device_table`:

DEFINE_IPACK_DEVICE_TABLE
=========================

.. c:function::  DEFINE_IPACK_DEVICE_TABLE( _table)

    macro used to describe a IndustryPack table

    :param  _table:
        device table name

.. _`define_ipack_device_table.description`:

Description
-----------

This macro is used to create a struct ipack_device_id array (a device table)
in a generic manner.

.. _`ipack_device`:

IPACK_DEVICE
============

.. c:function::  IPACK_DEVICE( _format,  vend,  dev)

    macro used to describe a specific IndustryPack device

    :param  _format:
        the format version (currently either 1 or 2, 8 bit value)

    :param  vend:
        the 8 or 24 bit IndustryPack Vendor ID

    :param  dev:
        the 8 or 16  bit IndustryPack Device ID

.. _`ipack_device.description`:

Description
-----------

This macro is used to create a struct ipack_device_id that matches a specific
device.

.. _`ipack_get_carrier`:

ipack_get_carrier
=================

.. c:function:: int ipack_get_carrier(struct ipack_device *dev)

    it increase the carrier ref. counter of the carrier module

    :param struct ipack_device \*dev:
        mezzanine device which wants to get the carrier

.. _`ipack_put_carrier`:

ipack_put_carrier
=================

.. c:function:: void ipack_put_carrier(struct ipack_device *dev)

    it decrease the carrier ref. counter of the carrier module

    :param struct ipack_device \*dev:
        mezzanine device which wants to get the carrier

.. This file was automatic generated / don't edit.

