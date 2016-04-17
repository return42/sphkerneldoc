.. -*- coding: utf-8; mode: rst -*-

=============
raspberrypi.c
=============


.. _`rpi_firmware_property_list`:

rpi_firmware_property_list
==========================

.. c:function:: int rpi_firmware_property_list (struct rpi_firmware *fw, void *data, size_t tag_size)

    Submit firmware property list

    :param struct rpi_firmware \*fw:
        Pointer to firmware structure from :c:func:`rpi_firmware_get`.

    :param void \*data:
        Buffer holding tags.

    :param size_t tag_size:
        Size of tags buffer.



.. _`rpi_firmware_property_list.description`:

Description
-----------

Submits a set of concatenated tags to the VPU firmware through the
mailbox property interface.

The buffer header and the ending tag are added by this function and
don't need to be supplied, just the actual tags for your operation.
See struct rpi_firmware_property_tag_header for the per-tag
structure.



.. _`rpi_firmware_property`:

rpi_firmware_property
=====================

.. c:function:: int rpi_firmware_property (struct rpi_firmware *fw, u32 tag, void *tag_data, size_t buf_size)

    Submit single firmware property

    :param struct rpi_firmware \*fw:
        Pointer to firmware structure from :c:func:`rpi_firmware_get`.

    :param u32 tag:
        One of enum_mbox_property_tag.

    :param void \*tag_data:
        Tag data buffer.

    :param size_t buf_size:
        Buffer size.



.. _`rpi_firmware_property.description`:

Description
-----------

Submits a single tag to the VPU firmware through the mailbox
property interface.

This is a convenience wrapper around
:c:func:`rpi_firmware_property_list` to avoid some of the
boilerplate in property calls.



.. _`rpi_firmware_get`:

rpi_firmware_get
================

.. c:function:: struct rpi_firmware *rpi_firmware_get (struct device_node *firmware_node)

    Get pointer to rpi_firmware structure.

    :param struct device_node \*firmware_node:
        Pointer to the firmware Device Tree node.



.. _`rpi_firmware_get.description`:

Description
-----------

Returns NULL is the firmware device is not ready.

