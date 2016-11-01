.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/uapi/arch/icache.h

.. _`invalidate_icache`:

invalidate_icache
=================

.. c:function:: void invalidate_icache(const void*addr, unsigned long size, unsigned long page_size)

    :param const void\*addr:
        *undescribed*

    :param unsigned long size:
        *undescribed*

    :param unsigned long page_size:
        *undescribed*

.. _`invalidate_icache.description`:

Description
-----------

@param addr The start of memory to be invalidated.
\ ``param``\  size The number of bytes to be invalidated.
\ ``param``\  page_size The system's page size, e.g. \ :c:func:`getpagesize`\  in userspace.
This value must be a power of two no larger than the page containing
the code to be invalidated. If the value is smaller than the actual page
size, this function will still work, but may run slower than necessary.

.. This file was automatic generated / don't edit.

