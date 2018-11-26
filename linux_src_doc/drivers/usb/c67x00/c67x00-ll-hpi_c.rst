.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/c67x00/c67x00-ll-hpi.c

.. _`c67x00_ll_usb_clear_status`:

c67x00_ll_usb_clear_status
==========================

.. c:function:: void c67x00_ll_usb_clear_status(struct c67x00_sie *sie, u16 bits)

    clear the USB status bits

    :param sie:
        *undescribed*
    :type sie: struct c67x00_sie \*

    :param bits:
        *undescribed*
    :type bits: u16

.. _`c67x00_ll_write_mem_le16`:

c67x00_ll_write_mem_le16
========================

.. c:function:: void c67x00_ll_write_mem_le16(struct c67x00_device *dev, u16 addr, void *data, int len)

    write into c67x00 memory Only data is little endian, addr has cpu endianess.

    :param dev:
        *undescribed*
    :type dev: struct c67x00_device \*

    :param addr:
        *undescribed*
    :type addr: u16

    :param data:
        *undescribed*
    :type data: void \*

    :param len:
        *undescribed*
    :type len: int

.. _`c67x00_ll_read_mem_le16`:

c67x00_ll_read_mem_le16
=======================

.. c:function:: void c67x00_ll_read_mem_le16(struct c67x00_device *dev, u16 addr, void *data, int len)

    read from c67x00 memory Only data is little endian, addr has cpu endianess.

    :param dev:
        *undescribed*
    :type dev: struct c67x00_device \*

    :param addr:
        *undescribed*
    :type addr: u16

    :param data:
        *undescribed*
    :type data: void \*

    :param len:
        *undescribed*
    :type len: int

.. This file was automatic generated / don't edit.

