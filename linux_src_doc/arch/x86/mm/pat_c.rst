.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/pat.c

.. _`pat_init`:

pat_init
========

.. c:function:: void pat_init( void)

    Initialize PAT MSR and PAT table

    :param void:
        no arguments
    :type void: 

.. _`pat_init.description`:

Description
-----------

This function initializes PAT MSR and PAT table with an OS-defined value
to enable additional cache attributes, WC, WT and WP.

This function must be called on all CPUs using the specific sequence of
operations defined in Intel SDM. \ :c:func:`mtrr_rendezvous_handler`\  provides this
procedure for PAT.

.. _`lookup_memtype`:

lookup_memtype
==============

.. c:function:: enum page_cache_mode lookup_memtype(u64 paddr)

    Looksup the memory type for a physical address

    :param paddr:
        physical address of which memory type needs to be looked up
    :type paddr: u64

.. _`lookup_memtype.description`:

Description
-----------

Only to be called when PAT is enabled

Returns \_PAGE_CACHE_MODE_WB, \_PAGE_CACHE_MODE_WC, \_PAGE_CACHE_MODE_UC_MINUS
or \_PAGE_CACHE_MODE_WT.

.. _`pat_pfn_immune_to_uc_mtrr`:

pat_pfn_immune_to_uc_mtrr
=========================

.. c:function:: bool pat_pfn_immune_to_uc_mtrr(unsigned long pfn)

    Check whether the PAT memory type of \ ``pfn``\  cannot be overridden by UC MTRR memory type.

    :param pfn:
        *undescribed*
    :type pfn: unsigned long

.. _`pat_pfn_immune_to_uc_mtrr.description`:

Description
-----------

Only to be called when PAT is enabled.

Returns true, if the PAT memory type of \ ``pfn``\  is UC, UC-, or WC.
Returns false in other cases.

.. _`io_reserve_memtype`:

io_reserve_memtype
==================

.. c:function:: int io_reserve_memtype(resource_size_t start, resource_size_t end, enum page_cache_mode *type)

    Request a memory type mapping for a region of memory

    :param start:
        start (physical address) of the region
    :type start: resource_size_t

    :param end:
        end (physical address) of the region
    :type end: resource_size_t

    :param type:
        A pointer to memtype, with requested type. On success, requested
        or any other compatible type that was available for the region is returned
    :type type: enum page_cache_mode \*

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

    :param start:
        start (physical address) of the region
    :type start: resource_size_t

    :param end:
        end (physical address) of the region
    :type end: resource_size_t

.. This file was automatic generated / don't edit.

