.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/qib/qib_pio_copy.c

.. _`qib_pio_copy`:

qib_pio_copy
============

.. c:function:: void qib_pio_copy(void __iomem *to, const void *from, size_t count)

    copy data to MMIO space, in multiples of 32-bits

    :param void __iomem \*to:
        destination, in MMIO space (must be 64-bit aligned)

    :param const void \*from:
        source (must be 64-bit aligned)

    :param size_t count:
        number of 32-bit quantities to copy

.. _`qib_pio_copy.description`:

Description
-----------

Copy data from kernel space to MMIO space, in multiples of 32 bits at a
time.  Order of access is not guaranteed, nor is a memory barrier
performed afterwards.

.. This file was automatic generated / don't edit.

