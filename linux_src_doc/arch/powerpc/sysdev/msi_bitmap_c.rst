.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/msi_bitmap.c

.. _`msi_bitmap_reserve_dt_hwirqs`:

msi_bitmap_reserve_dt_hwirqs
============================

.. c:function:: int msi_bitmap_reserve_dt_hwirqs(struct msi_bitmap *bmp)

    Reserve irqs specified in the device tree.

    :param bmp:
        pointer to the MSI bitmap.
    :type bmp: struct msi_bitmap \*

.. _`msi_bitmap_reserve_dt_hwirqs.description`:

Description
-----------

Looks in the device tree to see if there is a property specifying which
irqs can be used for MSI. If found those irqs reserved in the device tree
are reserved in the bitmap.

Returns 0 for success, < 0 if there was an error, and > 0 if no property
was found in the device tree.

.. This file was automatic generated / don't edit.

