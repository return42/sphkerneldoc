.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hda_bus_type.c

.. _`hdac_get_device_id`:

hdac_get_device_id
==================

.. c:function:: const struct hda_device_id *hdac_get_device_id(struct hdac_device *hdev, struct hdac_driver *drv)

    gets the hdac device id entry

    :param hdev:
        HD-audio core device
    :type hdev: struct hdac_device \*

    :param drv:
        HD-audio codec driver
    :type drv: struct hdac_driver \*

.. _`hdac_get_device_id.description`:

Description
-----------

Compares the hdac device vendor_id and revision_id to the hdac_device
driver id_table and returns the matching device id entry.

.. This file was automatic generated / don't edit.

