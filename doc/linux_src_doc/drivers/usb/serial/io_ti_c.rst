.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/serial/io_ti.c

.. _`read_download_mem`:

read_download_mem
=================

.. c:function:: int read_download_mem(struct usb_device *dev, int start_address, int length, __u8 address_type, __u8 *buffer)

    Read edgeport memory from TI chip

    :param struct usb_device \*dev:
        usb device pointer

    :param int start_address:
        Device CPU address at which to read

    :param int length:
        Length of above data

    :param __u8 address_type:
        Can read both XDATA and I2C

    :param __u8 \*buffer:
        pointer to input data buffer

.. This file was automatic generated / don't edit.

