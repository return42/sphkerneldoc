.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/lib/iomap_copy.c

.. _`__ioread64_copy`:

__ioread64_copy
===============

.. c:function:: void __ioread64_copy(void *to, const void __iomem *from, size_t count)

    copy data from MMIO space, in 64-bit units

    :param void \*to:
        destination (must be 64-bit aligned)

    :param const void __iomem \*from:
        source, in MMIO space (must be 64-bit aligned)

    :param size_t count:
        number of 64-bit quantities to copy

.. _`__ioread64_copy.description`:

Description
-----------

Copy data from MMIO space to kernel space, in units of 32 or 64 bits at a
time.  Order of access is not guaranteed, nor is a memory barrier
performed afterwards.

.. This file was automatic generated / don't edit.

