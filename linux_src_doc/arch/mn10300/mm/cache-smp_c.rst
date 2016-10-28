.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mn10300/mm/cache-smp.c

.. _`smp_cache_interrupt`:

smp_cache_interrupt
===================

.. c:function:: void smp_cache_interrupt( void)

    Handle IPI request to flush caches.

    :param  void:
        no arguments

.. _`smp_cache_interrupt.description`:

Description
-----------

Handle a request delivered by IPI to flush the current CPU's
caches.  The parameters are stored in smp_cache\_\*.

.. _`smp_cache_call`:

smp_cache_call
==============

.. c:function:: void smp_cache_call(unsigned long opr_mask, unsigned long start, unsigned long end)

    Issue an IPI to request the other CPUs flush caches

    :param unsigned long opr_mask:
        Cache operation flags

    :param unsigned long start:
        Start address of request

    :param unsigned long end:
        End address of request

.. _`smp_cache_call.description`:

Description
-----------

Send cache flush IPI to other CPUs.  This invokes \ :c:func:`smp_cache_interrupt`\ 
above on those other CPUs and then waits for them to finish.

The caller must hold smp_cache_lock.

.. This file was automatic generated / don't edit.

