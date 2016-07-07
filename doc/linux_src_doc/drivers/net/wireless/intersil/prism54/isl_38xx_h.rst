.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/intersil/prism54/isl_38xx.h

.. _`isl38xx_w32_flush`:

isl38xx_w32_flush
=================

.. c:function:: void isl38xx_w32_flush(void __iomem *base, u32 val, unsigned long offset)

    PCI iomem write helper

    :param void __iomem \*base:
        (host) memory base address of the device

    :param u32 val:
        32bit value (host order) to write

    :param unsigned long offset:
        byte offset into \ ``base``\  to write value to

.. _`isl38xx_w32_flush.description`:

Description
-----------

This helper takes care of writing a 32bit datum to the
specified offset into the device's pci memory space, and making sure
the pci memory buffers get flushed by performing one harmless read
from the \ ``ISL38XX_PCI_POSTING_FLUSH``\  offset.

.. This file was automatic generated / don't edit.

