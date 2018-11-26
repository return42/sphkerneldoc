.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/scom.h

.. _`scom_init`:

scom_init
=========

.. c:function:: void scom_init(const struct scom_controller *controller)

    Initialize the SCOM backend, called by the platform

    :param controller:
        The platform SCOM controller
    :type controller: const struct scom_controller \*

.. _`scom_map_ok`:

scom_map_ok
===========

.. c:function:: int scom_map_ok(scom_map_t map)

    Test is a SCOM mapping is successful

    :param map:
        The result of scom_map to test
    :type map: scom_map_t

.. _`scom_map`:

scom_map
========

.. c:function:: scom_map_t scom_map(struct device_node *ctrl_dev, u64 reg, u64 count)

    Map a block of SCOM registers

    :param ctrl_dev:
        Device node of the SCOM controller
        some implementations allow NULL here
    :type ctrl_dev: struct device_node \*

    :param reg:
        first SCOM register to map
    :type reg: u64

    :param count:
        Number of SCOM registers to map
    :type count: u64

.. _`scom_find_parent`:

scom_find_parent
================

.. c:function:: struct device_node *scom_find_parent(struct device_node *dev)

    Find the SCOM controller for a device

    :param dev:
        OF node of the device
    :type dev: struct device_node \*

.. _`scom_find_parent.description`:

Description
-----------

This is not meant for general usage, but in combination with
\ :c:func:`scom_map`\  allows to map registers not represented by the
device own scom-reg property. Useful for applying HW workarounds
on things not properly represented in the device-tree for example.

.. _`scom_map_device`:

scom_map_device
===============

.. c:function:: scom_map_t scom_map_device(struct device_node *dev, int index)

    Map a device's block of SCOM registers

    :param dev:
        OF node of the device
    :type dev: struct device_node \*

    :param index:
        Register bank index (index in "scom-reg" property)
    :type index: int

.. _`scom_map_device.description`:

Description
-----------

This function will use the device-tree binding for SCOM which
is to follow "scom-parent" properties until it finds a node with
a "scom-controller" property to find the controller. It will then
use the "scom-reg" property which is made of reg/count pairs,
each of them having a size defined by the controller's #scom-cells
property

.. _`scom_unmap`:

scom_unmap
==========

.. c:function:: void scom_unmap(scom_map_t map)

    Unmap a block of SCOM registers

    :param map:
        Result of scom_map is to be unmapped
    :type map: scom_map_t

.. _`scom_read`:

scom_read
=========

.. c:function:: int scom_read(scom_map_t map, u64 reg, u64 *value)

    Read a SCOM register

    :param map:
        Result of scom_map
    :type map: scom_map_t

    :param reg:
        Register index within that map
    :type reg: u64

    :param value:
        Updated with the value read
    :type value: u64 \*

.. _`scom_read.description`:

Description
-----------

Returns 0 (success) or a negative error code

.. _`scom_write`:

scom_write
==========

.. c:function:: int scom_write(scom_map_t map, u64 reg, u64 value)

    Write to a SCOM register

    :param map:
        Result of scom_map
    :type map: scom_map_t

    :param reg:
        Register index within that map
    :type reg: u64

    :param value:
        Value to write
    :type value: u64

.. _`scom_write.description`:

Description
-----------

Returns 0 (success) or a negative error code

.. This file was automatic generated / don't edit.

