.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/scan.c

.. _`uwb_rc_scan`:

uwb_rc_scan
===========

.. c:function:: int uwb_rc_scan(struct uwb_rc *rc, unsigned channel, enum uwb_scan_type type, unsigned bpst_offset)

    :param struct uwb_rc \*rc:
        UWB Radio Controller

    :param unsigned channel:
        Channel to scan; encodings in WUSB1.0[Table 5.12]

    :param enum uwb_scan_type type:
        Type of scanning to do.

    :param unsigned bpst_offset:
        value at which to start scanning (if type ==
        UWB_SCAN_ONLY_STARTTIME)

.. _`uwb_rc_scan.description`:

Description
-----------

We put the command on kmalloc'ed memory as some arches cannot do
USB from the stack. The reply event is copied from an stage buffer,
so it can be in the stack. See WUSB1.0[8.6.2.4] for more details.

.. This file was automatic generated / don't edit.

