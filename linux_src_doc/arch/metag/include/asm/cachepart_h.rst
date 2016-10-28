.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/metag/include/asm/cachepart.h

.. _`get_dcache_size`:

get_dcache_size
===============

.. c:function:: unsigned int get_dcache_size( void)

    Get size of data cache.

    :param  void:
        no arguments

.. _`get_icache_size`:

get_icache_size
===============

.. c:function:: unsigned int get_icache_size( void)

    Get size of code cache.

    :param  void:
        no arguments

.. _`get_global_dcache_size`:

get_global_dcache_size
======================

.. c:function:: unsigned int get_global_dcache_size( void)

    Get the thread's global dcache.

    :param  void:
        no arguments

.. _`get_global_dcache_size.description`:

Description
-----------

Returns the size of the current thread's global dcache partition.

.. _`get_global_icache_size`:

get_global_icache_size
======================

.. c:function:: unsigned int get_global_icache_size( void)

    Get the thread's global icache.

    :param  void:
        no arguments

.. _`get_global_icache_size.description`:

Description
-----------

Returns the size of the current thread's global icache partition.

.. _`check_for_cache_aliasing`:

check_for_cache_aliasing
========================

.. c:function:: void check_for_cache_aliasing(int thread_id)

    Ensure that the bootloader has configured the dache and icache properly to avoid aliasing

    :param int thread_id:
        Hardware thread ID

.. This file was automatic generated / don't edit.

