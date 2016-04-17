.. -*- coding: utf-8; mode: rst -*-

===========
imx21-hcd.c
===========


.. _`copy_to_dmem`:

copy_to_dmem
============

.. c:function:: void copy_to_dmem (struct imx21 *imx21, int dmem_offset, void *src, int count)

    :param struct imx21 \*imx21:

        *undescribed*

    :param int dmem_offset:

        *undescribed*

    :param void \*src:

        *undescribed*

    :param int count:

        *undescribed*



.. _`copy_to_dmem.description`:

Description
-----------

We cannot use :c:func:`memcpy_toio` because the hardware requires 32bit writes

