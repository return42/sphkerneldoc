.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tty/tty_port.c

.. _`tty_port_link_device`:

tty_port_link_device
====================

.. c:function:: void tty_port_link_device(struct tty_port *port, struct tty_driver *driver, unsigned index)

    link tty and tty_port

    :param port:
        tty_port of the device
    :type port: struct tty_port \*

    :param driver:
        tty_driver for this device
    :type driver: struct tty_driver \*

    :param index:
        index of the tty
    :type index: unsigned

.. _`tty_port_link_device.description`:

Description
-----------

Provide the tty layer with a link from a tty (specified by \ ``index``\ ) to a
tty_port (@port). Use this only if neither tty_port_register_device nor
tty_port_install is used in the driver. If used, this has to be called before
tty_register_driver.

.. _`tty_port_register_device`:

tty_port_register_device
========================

.. c:function:: struct device *tty_port_register_device(struct tty_port *port, struct tty_driver *driver, unsigned index, struct device *device)

    register tty device

    :param port:
        tty_port of the device
    :type port: struct tty_port \*

    :param driver:
        tty_driver for this device
    :type driver: struct tty_driver \*

    :param index:
        index of the tty
    :type index: unsigned

    :param device:
        parent if exists, otherwise NULL
    :type device: struct device \*

.. _`tty_port_register_device.description`:

Description
-----------

It is the same as tty_register_device except the provided \ ``port``\  is linked to
a concrete tty specified by \ ``index``\ . Use this or tty_port_install (or both).
Call tty_port_link_device as a last resort.

.. _`tty_port_register_device_attr`:

tty_port_register_device_attr
=============================

.. c:function:: struct device *tty_port_register_device_attr(struct tty_port *port, struct tty_driver *driver, unsigned index, struct device *device, void *drvdata, const struct attribute_group **attr_grp)

    register tty device

    :param port:
        tty_port of the device
    :type port: struct tty_port \*

    :param driver:
        tty_driver for this device
    :type driver: struct tty_driver \*

    :param index:
        index of the tty
    :type index: unsigned

    :param device:
        parent if exists, otherwise NULL
    :type device: struct device \*

    :param drvdata:
        Driver data to be set to device.
    :type drvdata: void \*

    :param attr_grp:
        Attribute group to be set on device.
    :type attr_grp: const struct attribute_group \*\*

.. _`tty_port_register_device_attr.description`:

Description
-----------

It is the same as tty_register_device_attr except the provided \ ``port``\  is
linked to a concrete tty specified by \ ``index``\ . Use this or tty_port_install
(or both). Call tty_port_link_device as a last resort.

.. _`tty_port_register_device_attr_serdev`:

tty_port_register_device_attr_serdev
====================================

.. c:function:: struct device *tty_port_register_device_attr_serdev(struct tty_port *port, struct tty_driver *driver, unsigned index, struct device *device, void *drvdata, const struct attribute_group **attr_grp)

    register tty or serdev device

    :param port:
        tty_port of the device
    :type port: struct tty_port \*

    :param driver:
        tty_driver for this device
    :type driver: struct tty_driver \*

    :param index:
        index of the tty
    :type index: unsigned

    :param device:
        parent if exists, otherwise NULL
    :type device: struct device \*

    :param drvdata:
        driver data for the device
    :type drvdata: void \*

    :param attr_grp:
        attribute group for the device
    :type attr_grp: const struct attribute_group \*\*

.. _`tty_port_register_device_attr_serdev.description`:

Description
-----------

Register a serdev or tty device depending on if the parent device has any
defined serdev clients or not.

.. _`tty_port_register_device_serdev`:

tty_port_register_device_serdev
===============================

.. c:function:: struct device *tty_port_register_device_serdev(struct tty_port *port, struct tty_driver *driver, unsigned index, struct device *device)

    register tty or serdev device

    :param port:
        tty_port of the device
    :type port: struct tty_port \*

    :param driver:
        tty_driver for this device
    :type driver: struct tty_driver \*

    :param index:
        index of the tty
    :type index: unsigned

    :param device:
        parent if exists, otherwise NULL
    :type device: struct device \*

.. _`tty_port_register_device_serdev.description`:

Description
-----------

Register a serdev or tty device depending on if the parent device has any
defined serdev clients or not.

.. _`tty_port_unregister_device`:

tty_port_unregister_device
==========================

.. c:function:: void tty_port_unregister_device(struct tty_port *port, struct tty_driver *driver, unsigned index)

    deregister a tty or serdev device

    :param port:
        tty_port of the device
    :type port: struct tty_port \*

    :param driver:
        tty_driver for this device
    :type driver: struct tty_driver \*

    :param index:
        index of the tty
    :type index: unsigned

.. _`tty_port_unregister_device.description`:

Description
-----------

If a tty or serdev device is registered with a call to
\ :c:func:`tty_port_register_device_serdev`\  then this function must be called when
the device is gone.

.. _`tty_port_destroy`:

tty_port_destroy
================

.. c:function:: void tty_port_destroy(struct tty_port *port)

    - destroy inited port

    :param port:
        tty port to be destroyed
    :type port: struct tty_port \*

.. _`tty_port_destroy.description`:

Description
-----------

When a port was initialized using tty_port_init, one has to destroy the
port by this function. Either indirectly by using tty_port refcounting
(tty_port_put) or directly if refcounting is not used.

.. _`tty_port_tty_get`:

tty_port_tty_get
================

.. c:function:: struct tty_struct *tty_port_tty_get(struct tty_port *port)

    get a tty reference

    :param port:
        tty port
    :type port: struct tty_port \*

.. _`tty_port_tty_get.description`:

Description
-----------

Return a refcount protected tty instance or NULL if the port is not
associated with a tty (eg due to close or hangup)

.. _`tty_port_tty_set`:

tty_port_tty_set
================

.. c:function:: void tty_port_tty_set(struct tty_port *port, struct tty_struct *tty)

    set the tty of a port

    :param port:
        tty port
    :type port: struct tty_port \*

    :param tty:
        the tty
    :type tty: struct tty_struct \*

.. _`tty_port_tty_set.description`:

Description
-----------

Associate the port and tty pair. Manages any internal refcounts.
Pass NULL to deassociate a port

.. _`tty_port_hangup`:

tty_port_hangup
===============

.. c:function:: void tty_port_hangup(struct tty_port *port)

    hangup helper

    :param port:
        tty port
    :type port: struct tty_port \*

.. _`tty_port_hangup.description`:

Description
-----------

Perform port level tty hangup flag and count changes. Drop the tty
reference.

Caller holds tty lock.

.. _`tty_port_tty_hangup`:

tty_port_tty_hangup
===================

.. c:function:: void tty_port_tty_hangup(struct tty_port *port, bool check_clocal)

    helper to hang up a tty

    :param port:
        tty port
    :type port: struct tty_port \*

    :param check_clocal:
        hang only ttys with CLOCAL unset?
    :type check_clocal: bool

.. _`tty_port_tty_wakeup`:

tty_port_tty_wakeup
===================

.. c:function:: void tty_port_tty_wakeup(struct tty_port *port)

    helper to wake up a tty

    :param port:
        tty port
    :type port: struct tty_port \*

.. _`tty_port_carrier_raised`:

tty_port_carrier_raised
=======================

.. c:function:: int tty_port_carrier_raised(struct tty_port *port)

    carrier raised check

    :param port:
        tty port
    :type port: struct tty_port \*

.. _`tty_port_carrier_raised.description`:

Description
-----------

Wrapper for the carrier detect logic. For the moment this is used
to hide some internal details. This will eventually become entirely
internal to the tty port.

.. _`tty_port_raise_dtr_rts`:

tty_port_raise_dtr_rts
======================

.. c:function:: void tty_port_raise_dtr_rts(struct tty_port *port)

    Raise DTR/RTS

    :param port:
        tty port
    :type port: struct tty_port \*

.. _`tty_port_raise_dtr_rts.description`:

Description
-----------

Wrapper for the DTR/RTS raise logic. For the moment this is used
to hide some internal details. This will eventually become entirely
internal to the tty port.

.. _`tty_port_lower_dtr_rts`:

tty_port_lower_dtr_rts
======================

.. c:function:: void tty_port_lower_dtr_rts(struct tty_port *port)

    Lower DTR/RTS

    :param port:
        tty port
    :type port: struct tty_port \*

.. _`tty_port_lower_dtr_rts.description`:

Description
-----------

Wrapper for the DTR/RTS raise logic. For the moment this is used
to hide some internal details. This will eventually become entirely
internal to the tty port.

.. _`tty_port_block_til_ready`:

tty_port_block_til_ready
========================

.. c:function:: int tty_port_block_til_ready(struct tty_port *port, struct tty_struct *tty, struct file *filp)

    Waiting logic for tty open

    :param port:
        the tty port being opened
    :type port: struct tty_port \*

    :param tty:
        the tty device being bound
    :type tty: struct tty_struct \*

    :param filp:
        the file pointer of the opener or NULL
    :type filp: struct file \*

.. _`tty_port_block_til_ready.description`:

Description
-----------

Implement the core POSIX/SuS tty behaviour when opening a tty device.

.. _`tty_port_block_til_ready.handles`:

Handles
-------

- hangup (both before and during)
- non blocking open
- rts/dtr/dcd
- signals
- port flags and counts

The passed tty_port must implement the carrier_raised method if it can
do carrier detect and the dtr_rts method if it supports software
management of these lines. Note that the dtr/rts raise is done each
iteration as a hangup may have previously dropped them while we wait.

Caller holds tty lock.

NB: May drop and reacquire tty lock when blocking, so tty and tty_port
may have changed state (eg., may have been hung up).

.. _`tty_port_close`:

tty_port_close
==============

.. c:function:: void tty_port_close(struct tty_port *port, struct tty_struct *tty, struct file *filp)

    :param port:
        *undescribed*
    :type port: struct tty_port \*

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param filp:
        *undescribed*
    :type filp: struct file \*

.. _`tty_port_close.description`:

Description
-----------

Caller holds tty lock

.. _`tty_port_install`:

tty_port_install
================

.. c:function:: int tty_port_install(struct tty_port *port, struct tty_driver *driver, struct tty_struct *tty)

    generic tty->ops->install handler

    :param port:
        tty_port of the device
    :type port: struct tty_port \*

    :param driver:
        tty_driver for this device
    :type driver: struct tty_driver \*

    :param tty:
        tty to be installed
    :type tty: struct tty_struct \*

.. _`tty_port_install.description`:

Description
-----------

It is the same as tty_standard_install except the provided \ ``port``\  is linked
to a concrete tty specified by \ ``tty``\ . Use this or tty_port_register_device
(or both). Call tty_port_link_device as a last resort.

.. _`tty_port_open`:

tty_port_open
=============

.. c:function:: int tty_port_open(struct tty_port *port, struct tty_struct *tty, struct file *filp)

    :param port:
        *undescribed*
    :type port: struct tty_port \*

    :param tty:
        *undescribed*
    :type tty: struct tty_struct \*

    :param filp:
        *undescribed*
    :type filp: struct file \*

.. _`tty_port_open.description`:

Description
-----------

Caller holds tty lock.

NB: may drop and reacquire tty lock (in \ :c:func:`tty_port_block_til_ready`\ ) so
tty and tty_port may have changed state (eg., may be hung up now)

.. This file was automatic generated / don't edit.

