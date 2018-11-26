.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/iomap_copy.c

.. _`__iowrite32_copy`:

\__iowrite32_copy
=================

.. c:function:: void __iowrite32_copy(void __iomem *to, const void *from, size_t count)

    copy data to MMIO space, in 32-bit units

    :param to:
        destination, in MMIO space (must be 32-bit aligned)
    :type to: void __iomem \*

    :param from:
        source (must be 32-bit aligned)
    :type from: const void \*

    :param count:
        number of 32-bit quantities to copy
    :type count: size_t

.. _`__iowrite32_copy.description`:

Description
-----------

Copy data from kernel space to MMIO space, in units of 32 bits at a
time.  Order of access is not guaranteed, nor is a memory barrier
performed afterwards.

.. _`__ioread32_copy`:

\__ioread32_copy
================

.. c:function:: void __ioread32_copy(void *to, const void __iomem *from, size_t count)

    copy data from MMIO space, in 32-bit units

    :param to:
        destination (must be 32-bit aligned)
    :type to: void \*

    :param from:
        source, in MMIO space (must be 32-bit aligned)
    :type from: const void __iomem \*

    :param count:
        number of 32-bit quantities to copy
    :type count: size_t

.. _`__ioread32_copy.description`:

Description
-----------

Copy data from MMIO space to kernel space, in units of 32 bits at a
time.  Order of access is not guaranteed, nor is a memory barrier
performed afterwards.

.. _`__iowrite64_copy`:

\__iowrite64_copy
=================

.. c:function:: void __iowrite64_copy(void __iomem *to, const void *from, size_t count)

    copy data to MMIO space, in 64-bit or 32-bit units

    :param to:
        destination, in MMIO space (must be 64-bit aligned)
    :type to: void __iomem \*

    :param from:
        source (must be 64-bit aligned)
    :type from: const void \*

    :param count:
        number of 64-bit quantities to copy
    :type count: size_t

.. _`__iowrite64_copy.description`:

Description
-----------

Copy data from kernel space to MMIO space, in units of 32 or 64 bits at a
time.  Order of access is not guaranteed, nor is a memory barrier
performed afterwards.

.. This file was automatic generated / don't edit.

