.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/imx21-hcd.c

.. _`copy_to_dmem`:

copy_to_dmem
============

.. c:function:: void copy_to_dmem(struct imx21 *imx21, int dmem_offset, void *src, int count)

    We cannot use \ :c:func:`memcpy_toio`\  because the hardware requires 32bit writes

    :param imx21:
        *undescribed*
    :type imx21: struct imx21 \*

    :param dmem_offset:
        *undescribed*
    :type dmem_offset: int

    :param src:
        *undescribed*
    :type src: void \*

    :param count:
        *undescribed*
    :type count: int

.. This file was automatic generated / don't edit.

