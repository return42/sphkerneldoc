.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/sh/maple/maple.c

.. _`maple_driver_register`:

maple_driver_register
=====================

.. c:function:: int maple_driver_register(struct maple_driver *drv)

    register a maple driver

    :param drv:
        maple driver to be registered.
    :type drv: struct maple_driver \*

.. _`maple_driver_register.description`:

Description
-----------

Registers the passed in \ ``drv``\ , while updating the bus type.
Devices with matching function IDs will be automatically probed.

.. _`maple_driver_unregister`:

maple_driver_unregister
=======================

.. c:function:: void maple_driver_unregister(struct maple_driver *drv)

    unregister a maple driver.

    :param drv:
        maple driver to unregister.
    :type drv: struct maple_driver \*

.. _`maple_driver_unregister.description`:

Description
-----------

Cleans up after \ :c:func:`maple_driver_register`\ . To be invoked in the exit
path of any module drivers.

.. _`maple_getcond_callback`:

maple_getcond_callback
======================

.. c:function:: void maple_getcond_callback(struct maple_device *dev, void (*callback)(struct mapleq *mq), unsigned long interval, unsigned long function)

    setup handling MAPLE_COMMAND_GETCOND

    :param dev:
        device responding
    :type dev: struct maple_device \*

    :param void (\*callback)(struct mapleq \*mq):
        handler callback

    :param interval:
        interval in jiffies between callbacks
    :type interval: unsigned long

    :param function:
        the function code for the device
    :type function: unsigned long

.. _`maple_add_packet`:

maple_add_packet
================

.. c:function:: int maple_add_packet(struct maple_device *mdev, u32 function, u32 command, size_t length, void *data)

    add a single instruction to the maple bus queue

    :param mdev:
        maple device
    :type mdev: struct maple_device \*

    :param function:
        function on device being queried
    :type function: u32

    :param command:
        maple command to add
    :type command: u32

    :param length:
        length of command string (in 32 bit words)
    :type length: size_t

    :param data:
        remainder of command string
    :type data: void \*

.. This file was automatic generated / don't edit.

