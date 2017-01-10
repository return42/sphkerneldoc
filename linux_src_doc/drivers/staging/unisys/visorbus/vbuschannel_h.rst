.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/unisys/visorbus/vbuschannel.h

.. _`vbuschannel_print_devinfo`:

vbuschannel_print_devinfo
=========================

.. c:function:: void vbuschannel_print_devinfo(struct ultra_vbus_deviceinfo *devinfo, struct seq_file *seq, int devix)

    format a struct ultra_vbus_deviceinfo and write it to a seq_file

    :param struct ultra_vbus_deviceinfo \*devinfo:
        the struct ultra_vbus_deviceinfo to format

    :param struct seq_file \*seq:
        seq_file to write to

    :param int devix:
        the device index to be included in the output data, or -1 if no
        device index is to be included

.. _`vbuschannel_print_devinfo.description`:

Description
-----------

Reads \ ``devInfo``\ , and writes it in human-readable notation to \ ``seq``\ .

.. This file was automatic generated / don't edit.

