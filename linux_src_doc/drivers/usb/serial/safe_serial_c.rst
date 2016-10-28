.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/serial/safe_serial.c

.. _`fcs_compute10`:

fcs_compute10
=============

.. c:function:: __u16 __inline__ fcs_compute10(unsigned char *sp, int len, __u16 fcs)

    memcpy and calculate 10 bit CRC across buffer

    :param unsigned char \*sp:
        pointer to buffer

    :param int len:
        number of bytes

    :param __u16 fcs:
        starting FCS

.. _`fcs_compute10.description`:

Description
-----------

Perform a memcpy and calculate fcs using ppp 10bit CRC algorithm. Return
new 10 bit FCS.

.. This file was automatic generated / don't edit.

