.. -*- coding: utf-8; mode: rst -*-

===============
c67x00-ll-hpi.c
===============


.. _`c67x00_ll_usb_clear_status`:

c67x00_ll_usb_clear_status
==========================

.. c:function:: void c67x00_ll_usb_clear_status (struct c67x00_sie *sie, u16 bits)

    clear the USB status bits

    :param struct c67x00_sie \*sie:

        *undescribed*

    :param u16 bits:

        *undescribed*



.. _`c67x00_ll_write_mem_le16`:

c67x00_ll_write_mem_le16
========================

.. c:function:: void c67x00_ll_write_mem_le16 (struct c67x00_device *dev, u16 addr, void *data, int len)

    write into c67x00 memory Only data is little endian, addr has cpu endianess.

    :param struct c67x00_device \*dev:

        *undescribed*

    :param u16 addr:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param int len:

        *undescribed*



.. _`c67x00_ll_read_mem_le16`:

c67x00_ll_read_mem_le16
=======================

.. c:function:: void c67x00_ll_read_mem_le16 (struct c67x00_device *dev, u16 addr, void *data, int len)

    read from c67x00 memory Only data is little endian, addr has cpu endianess.

    :param struct c67x00_device \*dev:

        *undescribed*

    :param u16 addr:

        *undescribed*

    :param void \*data:

        *undescribed*

    :param int len:

        *undescribed*

