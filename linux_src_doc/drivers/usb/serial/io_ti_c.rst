.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/serial/io_ti.c

.. _`read_download_mem`:

read_download_mem
=================

.. c:function:: int read_download_mem(struct usb_device *dev, int start_address, int length, __u8 address_type, __u8 *buffer)

    Read edgeport memory from TI chip

    :param dev:
        usb device pointer
    :type dev: struct usb_device \*

    :param start_address:
        Device CPU address at which to read
    :type start_address: int

    :param length:
        Length of above data
    :type length: int

    :param address_type:
        Can read both XDATA and I2C
    :type address_type: __u8

    :param buffer:
        pointer to input data buffer
    :type buffer: __u8 \*

.. This file was automatic generated / don't edit.

