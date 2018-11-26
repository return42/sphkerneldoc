.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-kye.c

.. _`kye_tablet_enable`:

kye_tablet_enable
=================

.. c:function:: int kye_tablet_enable(struct hid_device *hdev)

    functional tablet mode by setting a special feature report.

    :param hdev:
        HID device
    :type hdev: struct hid_device \*

.. _`kye_tablet_enable.description`:

Description
-----------

The specific report ID and data were discovered by sniffing the
Windows driver traffic.

.. This file was automatic generated / don't edit.

