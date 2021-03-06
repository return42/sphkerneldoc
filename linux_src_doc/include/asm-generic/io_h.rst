.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/asm-generic/io.h

.. _`ioremap---and-ioremap_----variants`:

\ :c:func:`ioremap`\  and ioremap\_\*() variants
================================================

If you have an IOMMU your architecture is expected to have both \ :c:func:`ioremap`\ 
and \ :c:func:`iounmap`\  implemented otherwise the asm-generic helpers will provide a
direct mapping.

There are ioremap\_\*() call variants, if you have no IOMMU we naturally will
default to direct mapping for all of them, you can override these defaults.
If you have an IOMMU you are highly encouraged to provide your own
ioremap variant implementation as there currently is no safe architecture
agnostic default. To avoid possible improper behaviour default asm-generic
ioremap\_\*() variants all return NULL when an IOMMU is available. If you've
defined your own ioremap\_\*() variant you must then declare your own
ioremap\_\*() variant as defined to itself to avoid the default NULL return.

.. _`memset_io`:

memset_io
=========

.. c:function:: void memset_io(volatile void __iomem *addr, int value, size_t size)

    :param addr:
        The beginning of the I/O-memory range to set
    :type addr: volatile void __iomem \*

    :param value:
        *undescribed*
    :type value: int

    :param size:
        *undescribed*
    :type size: size_t

.. _`memset_io.description`:

Description
-----------

Set a range of I/O memory to a given value.

.. _`memcpy_fromio`:

memcpy_fromio
=============

.. c:function:: void memcpy_fromio(void *buffer, const volatile void __iomem *addr, size_t size)

    :param buffer:
        *undescribed*
    :type buffer: void \*

    :param addr:
        *undescribed*
    :type addr: const volatile void __iomem \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`memcpy_fromio.description`:

Description
-----------

Copy a block of data from I/O memory.

.. _`memcpy_toio`:

memcpy_toio
===========

.. c:function:: void memcpy_toio(volatile void __iomem *addr, const void *buffer, size_t size)

    :param addr:
        *undescribed*
    :type addr: volatile void __iomem \*

    :param buffer:
        *undescribed*
    :type buffer: const void \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`memcpy_toio.description`:

Description
-----------

Copy a block of data to I/O memory.

.. This file was automatic generated / don't edit.

