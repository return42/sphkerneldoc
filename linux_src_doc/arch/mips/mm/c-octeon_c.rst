.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/mm/c-octeon.c

.. _`octeon_flush_data_cache_page`:

octeon_flush_data_cache_page
============================

.. c:function:: void octeon_flush_data_cache_page(unsigned long addr)

    from Linux's viewpoint it acts much like a physically tagged cache. No flushing is needed

    :param addr:
        *undescribed*
    :type addr: unsigned long

.. _`octeon_flush_icache_all_cores`:

octeon_flush_icache_all_cores
=============================

.. c:function:: void octeon_flush_icache_all_cores(struct vm_area_struct *vma)

    vma. If no vma is supplied, all cores are flushed.

    :param vma:
        VMA to flush or NULL to flush all icaches.
    :type vma: struct vm_area_struct \*

.. _`octeon_flush_icache_all`:

octeon_flush_icache_all
=======================

.. c:function:: void octeon_flush_icache_all( void)

    :param void:
        no arguments
    :type void: 

.. _`octeon_flush_cache_mm`:

octeon_flush_cache_mm
=====================

.. c:function:: void octeon_flush_cache_mm(struct mm_struct *mm)

    context.

    :param mm:
        Memory context to flush
    :type mm: struct mm_struct \*

.. _`octeon_flush_icache_range`:

octeon_flush_icache_range
=========================

.. c:function:: void octeon_flush_icache_range(unsigned long start, unsigned long end)

    :param start:
        *undescribed*
    :type start: unsigned long

    :param end:
        *undescribed*
    :type end: unsigned long

.. _`octeon_flush_cache_sigtramp`:

octeon_flush_cache_sigtramp
===========================

.. c:function:: void octeon_flush_cache_sigtramp(unsigned long addr)

    and exception hooking.

    :param addr:
        Address to flush
    :type addr: unsigned long

.. _`octeon_flush_cache_range`:

octeon_flush_cache_range
========================

.. c:function:: void octeon_flush_cache_range(struct vm_area_struct *vma, unsigned long start, unsigned long end)

    :param vma:
        VMA to flush
    :type vma: struct vm_area_struct \*

    :param start:
        *undescribed*
    :type start: unsigned long

    :param end:
        *undescribed*
    :type end: unsigned long

.. _`octeon_flush_cache_page`:

octeon_flush_cache_page
=======================

.. c:function:: void octeon_flush_cache_page(struct vm_area_struct *vma, unsigned long page, unsigned long pfn)

    :param vma:
        VMA to flush page for
    :type vma: struct vm_area_struct \*

    :param page:
        Page to flush
    :type page: unsigned long

    :param pfn:
        *undescribed*
    :type pfn: unsigned long

.. _`probe_octeon`:

probe_octeon
============

.. c:function:: void probe_octeon( void)

    :param void:
        no arguments
    :type void: 

.. _`octeon_cache_init`:

octeon_cache_init
=================

.. c:function:: void octeon_cache_init( void)

    :param void:
        no arguments
    :type void: 

.. _`cache_parity_error_octeon_non_recoverable`:

cache_parity_error_octeon_non_recoverable
=========================================

.. c:function:: void cache_parity_error_octeon_non_recoverable( void)

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

