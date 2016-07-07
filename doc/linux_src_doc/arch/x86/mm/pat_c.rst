.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/pat.c

.. _`pat_init`:

pat_init
========

.. c:function:: void pat_init( void)

    Initialize PAT MSR and PAT table

    :param  void:
        no arguments

.. _`pat_init.description`:

Description
-----------

This function initializes PAT MSR and PAT table with an OS-defined value
to enable additional cache attributes, WC and WT.

This function must be called on all CPUs using the specific sequence of
operations defined in Intel SDM. \ :c:func:`mtrr_rendezvous_handler`\  provides this
procedure for PAT.

.. _`lookup_memtype`:

lookup_memtype
==============

.. c:function:: enum page_cache_mode lookup_memtype(u64 paddr)

    Looksup the memory type for a physical address

    :param u64 paddr:
        physical address of which memory type needs to be looked up

.. _`lookup_memtype.description`:

Description
-----------

Only to be called when PAT is enabled

Returns \_PAGE_CACHE_MODE_WB, \_PAGE_CACHE_MODE_WC, \_PAGE_CACHE_MODE_UC_MINUS
or \_PAGE_CACHE_MODE_WT.

.. _`io_reserve_memtype`:

io_reserve_memtype
==================

.. c:function:: int io_reserve_memtype(resource_size_t start, resource_size_t end, enum page_cache_mode *type)

    Request a memory type mapping for a region of memory

    :param resource_size_t start:
        start (physical address) of the region

    :param resource_size_t end:
        end (physical address) of the region

    :param enum page_cache_mode \*type:
        A pointer to memtype, with requested type. On success, requested
        or any other compatible type that was available for the region is returned

.. _`io_reserve_memtype.description`:

Description
-----------

On success, returns 0
On failure, returns non-zero

.. _`io_free_memtype`:

io_free_memtype
===============

.. c:function:: void io_free_memtype(resource_size_t start, resource_size_t end)

    Release a memory type mapping for a region of memory

    :param resource_size_t start:
        start (physical address) of the region

    :param resource_size_t end:
        end (physical address) of the region

.. This file was automatic generated / don't edit.

