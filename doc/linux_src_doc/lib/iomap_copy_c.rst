.. -*- coding: utf-8; mode: rst -*-

============
iomap_copy.c
============


.. _`__iowrite32_copy`:

__iowrite32_copy
================

.. c:function:: void __iowrite32_copy (void __iomem *to, const void *from, size_t count)

    copy data to MMIO space, in 32-bit units

    :param void __iomem \*to:
        destination, in MMIO space (must be 32-bit aligned)

    :param const void \*from:
        source (must be 32-bit aligned)

    :param size_t count:
        number of 32-bit quantities to copy



.. _`__iowrite32_copy.description`:

Description
-----------

Copy data from kernel space to MMIO space, in units of 32 bits at a
time.  Order of access is not guaranteed, nor is a memory barrier
performed afterwards.



.. _`__ioread32_copy`:

__ioread32_copy
===============

.. c:function:: void __ioread32_copy (void *to, const void __iomem *from, size_t count)

    copy data from MMIO space, in 32-bit units

    :param void \*to:
        destination (must be 32-bit aligned)

    :param const void __iomem \*from:
        source, in MMIO space (must be 32-bit aligned)

    :param size_t count:
        number of 32-bit quantities to copy



.. _`__ioread32_copy.description`:

Description
-----------

Copy data from MMIO space to kernel space, in units of 32 bits at a
time.  Order of access is not guaranteed, nor is a memory barrier
performed afterwards.



.. _`__iowrite64_copy`:

__iowrite64_copy
================

.. c:function:: void __iowrite64_copy (void __iomem *to, const void *from, size_t count)

    copy data to MMIO space, in 64-bit or 32-bit units

    :param void __iomem \*to:
        destination, in MMIO space (must be 64-bit aligned)

    :param const void \*from:
        source (must be 64-bit aligned)

    :param size_t count:
        number of 64-bit quantities to copy



.. _`__iowrite64_copy.description`:

Description
-----------

Copy data from kernel space to MMIO space, in units of 32 or 64 bits at a
time.  Order of access is not guaranteed, nor is a memory barrier
performed afterwards.

