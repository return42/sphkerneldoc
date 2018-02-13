.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/nobootmem.c

.. _`free_all_bootmem`:

free_all_bootmem
================

.. c:function:: unsigned long free_all_bootmem( void)

    release free pages to the buddy allocator

    :param  void:
        no arguments

.. _`free_all_bootmem.description`:

Description
-----------

Returns the number of pages actually released.

.. _`free_bootmem_node`:

free_bootmem_node
=================

.. c:function:: void free_bootmem_node(pg_data_t *pgdat, unsigned long physaddr, unsigned long size)

    mark a page range as usable

    :param pg_data_t \*pgdat:
        node the range resides on

    :param unsigned long physaddr:
        starting address of the range

    :param unsigned long size:
        size of the range in bytes

.. _`free_bootmem_node.description`:

Description
-----------

Partial pages will be considered reserved and left as they are.

The range must reside completely on the specified node.

.. _`free_bootmem`:

free_bootmem
============

.. c:function:: void free_bootmem(unsigned long addr, unsigned long size)

    mark a page range as usable

    :param unsigned long addr:
        starting address of the range

    :param unsigned long size:
        size of the range in bytes

.. _`free_bootmem.description`:

Description
-----------

Partial pages will be considered reserved and left as they are.

The range must be contiguous but may span node boundaries.

.. _`__alloc_bootmem_nopanic`:

\__alloc_bootmem_nopanic
========================

.. c:function:: void *__alloc_bootmem_nopanic(unsigned long size, unsigned long align, unsigned long goal)

    allocate boot memory without panicking

    :param unsigned long size:
        size of the request in bytes

    :param unsigned long align:
        alignment of the region

    :param unsigned long goal:
        preferred starting address of the region

.. _`__alloc_bootmem_nopanic.description`:

Description
-----------

The goal is dropped if it can not be satisfied and the allocation will
fall back to memory below \ ``goal``\ .

Allocation may happen on any node in the system.

Returns NULL on failure.

.. _`__alloc_bootmem`:

\__alloc_bootmem
================

.. c:function:: void *__alloc_bootmem(unsigned long size, unsigned long align, unsigned long goal)

    allocate boot memory

    :param unsigned long size:
        size of the request in bytes

    :param unsigned long align:
        alignment of the region

    :param unsigned long goal:
        preferred starting address of the region

.. _`__alloc_bootmem.description`:

Description
-----------

The goal is dropped if it can not be satisfied and the allocation will
fall back to memory below \ ``goal``\ .

Allocation may happen on any node in the system.

The function panics if the request can not be satisfied.

.. _`__alloc_bootmem_node`:

\__alloc_bootmem_node
=====================

.. c:function:: void *__alloc_bootmem_node(pg_data_t *pgdat, unsigned long size, unsigned long align, unsigned long goal)

    allocate boot memory from a specific node

    :param pg_data_t \*pgdat:
        node to allocate from

    :param unsigned long size:
        size of the request in bytes

    :param unsigned long align:
        alignment of the region

    :param unsigned long goal:
        preferred starting address of the region

.. _`__alloc_bootmem_node.description`:

Description
-----------

The goal is dropped if it can not be satisfied and the allocation will
fall back to memory below \ ``goal``\ .

Allocation may fall back to any node in the system if the specified node
can not hold the requested memory.

The function panics if the request can not be satisfied.

.. _`__alloc_bootmem_low`:

\__alloc_bootmem_low
====================

.. c:function:: void *__alloc_bootmem_low(unsigned long size, unsigned long align, unsigned long goal)

    allocate low boot memory

    :param unsigned long size:
        size of the request in bytes

    :param unsigned long align:
        alignment of the region

    :param unsigned long goal:
        preferred starting address of the region

.. _`__alloc_bootmem_low.description`:

Description
-----------

The goal is dropped if it can not be satisfied and the allocation will
fall back to memory below \ ``goal``\ .

Allocation may happen on any node in the system.

The function panics if the request can not be satisfied.

.. _`__alloc_bootmem_low_node`:

\__alloc_bootmem_low_node
=========================

.. c:function:: void *__alloc_bootmem_low_node(pg_data_t *pgdat, unsigned long size, unsigned long align, unsigned long goal)

    allocate low boot memory from a specific node

    :param pg_data_t \*pgdat:
        node to allocate from

    :param unsigned long size:
        size of the request in bytes

    :param unsigned long align:
        alignment of the region

    :param unsigned long goal:
        preferred starting address of the region

.. _`__alloc_bootmem_low_node.description`:

Description
-----------

The goal is dropped if it can not be satisfied and the allocation will
fall back to memory below \ ``goal``\ .

Allocation may fall back to any node in the system if the specified node
can not hold the requested memory.

The function panics if the request can not be satisfied.

.. This file was automatic generated / don't edit.

