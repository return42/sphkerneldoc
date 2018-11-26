.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/serial/safe_serial.c

.. _`fcs_compute10`:

fcs_compute10
=============

.. c:function:: __u16 fcs_compute10(unsigned char *sp, int len, __u16 fcs)

    memcpy and calculate 10 bit CRC across buffer

    :param sp:
        pointer to buffer
    :type sp: unsigned char \*

    :param len:
        number of bytes
    :type len: int

    :param fcs:
        starting FCS
    :type fcs: __u16

.. _`fcs_compute10.description`:

Description
-----------

Perform a memcpy and calculate fcs using ppp 10bit CRC algorithm. Return
new 10 bit FCS.

.. This file was automatic generated / don't edit.

