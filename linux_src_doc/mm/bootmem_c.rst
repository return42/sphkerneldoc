.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/bootmem.c

.. _`bootmem_bootmap_pages`:

bootmem_bootmap_pages
=====================

.. c:function:: unsigned long bootmem_bootmap_pages(unsigned long pages)

    calculate bitmap size in pages

    :param unsigned long pages:
        number of pages the bitmap has to represent

.. _`init_bootmem_node`:

init_bootmem_node
=================

.. c:function:: unsigned long init_bootmem_node(pg_data_t *pgdat, unsigned long freepfn, unsigned long startpfn, unsigned long endpfn)

    register a node as boot memory

    :param pg_data_t \*pgdat:
        node to register

    :param unsigned long freepfn:
        pfn where the bitmap for this node is to be placed

    :param unsigned long startpfn:
        first pfn on the node

    :param unsigned long endpfn:
        first pfn after the node

.. _`init_bootmem_node.description`:

Description
-----------

Returns the number of bytes needed to hold the bitmap for this node.

.. _`init_bootmem`:

init_bootmem
============

.. c:function:: unsigned long init_bootmem(unsigned long start, unsigned long pages)

    register boot memory

    :param unsigned long start:
        pfn where the bitmap is to be placed

    :param unsigned long pages:
        number of available physical pages

.. _`init_bootmem.description`:

Description
-----------

Returns the number of bytes needed to hold the bitmap.

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

.. c:function:: void free_bootmem(unsigned long physaddr, unsigned long size)

    mark a page range as usable

    :param unsigned long physaddr:
        starting physical address of the range

    :param unsigned long size:
        size of the range in bytes

.. _`free_bootmem.description`:

Description
-----------

Partial pages will be considered reserved and left as they are.

The range must be contiguous but may span node boundaries.

.. _`reserve_bootmem_node`:

reserve_bootmem_node
====================

.. c:function:: int reserve_bootmem_node(pg_data_t *pgdat, unsigned long physaddr, unsigned long size, int flags)

    mark a page range as reserved

    :param pg_data_t \*pgdat:
        node the range resides on

    :param unsigned long physaddr:
        starting address of the range

    :param unsigned long size:
        size of the range in bytes

    :param int flags:
        reservation flags (see linux/bootmem.h)

.. _`reserve_bootmem_node.description`:

Description
-----------

Partial pages will be reserved.

The range must reside completely on the specified node.

.. _`reserve_bootmem`:

reserve_bootmem
===============

.. c:function:: int reserve_bootmem(unsigned long addr, unsigned long size, int flags)

    mark a page range as reserved

    :param unsigned long addr:
        starting address of the range

    :param unsigned long size:
        size of the range in bytes

    :param int flags:
        reservation flags (see linux/bootmem.h)

.. _`reserve_bootmem.description`:

Description
-----------

Partial pages will be reserved.

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

