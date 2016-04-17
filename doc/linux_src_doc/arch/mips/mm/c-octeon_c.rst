.. -*- coding: utf-8; mode: rst -*-

==========
c-octeon.c
==========


.. _`octeon_flush_data_cache_page`:

octeon_flush_data_cache_page
============================

.. c:function:: void octeon_flush_data_cache_page (unsigned long addr)

    :param unsigned long addr:

        *undescribed*



.. _`octeon_flush_data_cache_page.description`:

Description
-----------

from Linux's viewpoint it acts much like a physically
tagged cache. No flushing is needed



.. _`octeon_flush_icache_all_cores`:

octeon_flush_icache_all_cores
=============================

.. c:function:: void octeon_flush_icache_all_cores (struct vm_area_struct *vma)

    :param struct vm_area_struct \*vma:
        VMA to flush or NULL to flush all icaches.



.. _`octeon_flush_icache_all_cores.description`:

Description
-----------

vma. If no vma is supplied, all cores are flushed.



.. _`octeon_flush_icache_all`:

octeon_flush_icache_all
=======================

.. c:function:: void octeon_flush_icache_all ( void)

    :param void:
        no arguments



.. _`octeon_flush_cache_mm`:

octeon_flush_cache_mm
=====================

.. c:function:: void octeon_flush_cache_mm (struct mm_struct *mm)

    :param struct mm_struct \*mm:
        Memory context to flush



.. _`octeon_flush_cache_mm.description`:

Description
-----------

context.



.. _`octeon_flush_icache_range`:

octeon_flush_icache_range
=========================

.. c:function:: void octeon_flush_icache_range (unsigned long start, unsigned long end)

    :param unsigned long start:

        *undescribed*

    :param unsigned long end:

        *undescribed*



.. _`octeon_flush_cache_sigtramp`:

octeon_flush_cache_sigtramp
===========================

.. c:function:: void octeon_flush_cache_sigtramp (unsigned long addr)

    :param unsigned long addr:
        Address to flush



.. _`octeon_flush_cache_sigtramp.description`:

Description
-----------


and exception hooking.



.. _`octeon_flush_cache_range`:

octeon_flush_cache_range
========================

.. c:function:: void octeon_flush_cache_range (struct vm_area_struct *vma, unsigned long start, unsigned long end)

    :param struct vm_area_struct \*vma:
        VMA to flush

    :param unsigned long start:

        *undescribed*

    :param unsigned long end:

        *undescribed*



.. _`octeon_flush_cache_page`:

octeon_flush_cache_page
=======================

.. c:function:: void octeon_flush_cache_page (struct vm_area_struct *vma, unsigned long page, unsigned long pfn)

    :param struct vm_area_struct \*vma:
        VMA to flush page for

    :param unsigned long page:
        Page to flush

    :param unsigned long pfn:

        *undescribed*



.. _`probe_octeon`:

probe_octeon
============

.. c:function:: void probe_octeon ( void)

    :param void:
        no arguments



.. _`octeon_cache_init`:

octeon_cache_init
=================

.. c:function:: void octeon_cache_init ( void)

    :param void:
        no arguments



.. _`cache_parity_error_octeon_non_recoverable`:

cache_parity_error_octeon_non_recoverable
=========================================

.. c:function:: void cache_parity_error_octeon_non_recoverable ( void)

    :param void:
        no arguments

