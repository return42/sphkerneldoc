.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/include/asm/outercache.h

.. _`outer_inv_range`:

outer_inv_range
===============

.. c:function:: void outer_inv_range(phys_addr_t start, phys_addr_t end)

    invalidate range of outer cache lines

    :param phys_addr_t start:
        starting physical address, inclusive

    :param phys_addr_t end:
        end physical address, exclusive

.. _`outer_clean_range`:

outer_clean_range
=================

.. c:function:: void outer_clean_range(phys_addr_t start, phys_addr_t end)

    clean dirty outer cache lines

    :param phys_addr_t start:
        starting physical address, inclusive

    :param phys_addr_t end:
        end physical address, exclusive

.. _`outer_flush_range`:

outer_flush_range
=================

.. c:function:: void outer_flush_range(phys_addr_t start, phys_addr_t end)

    clean and invalidate outer cache lines

    :param phys_addr_t start:
        starting physical address, inclusive

    :param phys_addr_t end:
        end physical address, exclusive

.. _`outer_flush_all`:

outer_flush_all
===============

.. c:function:: void outer_flush_all( void)

    clean and invalidate all cache lines in the outer cache

    :param  void:
        no arguments

.. _`outer_flush_all.note`:

Note
----

depending on implementation, this may not be atomic - it must
only be called with interrupts disabled and no other active outer
cache masters.

It is intended that this function is only used by implementations
needing to override the outer_cache.disable() method due to security.
(Some implementations perform this as a clean followed by an invalidate.)

.. _`outer_disable`:

outer_disable
=============

.. c:function:: void outer_disable( void)

    clean, invalidate and disable the outer cache

    :param  void:
        no arguments

.. _`outer_disable.description`:

Description
-----------

Disable the outer cache, ensuring that any data contained in the outer
cache is pushed out to lower levels of system memory.  The note and
conditions above concerning \ :c:func:`outer_flush_all`\  applies here.

.. _`outer_resume`:

outer_resume
============

.. c:function:: void outer_resume( void)

    restore the cache configuration and re-enable outer cache

    :param  void:
        no arguments

.. _`outer_resume.description`:

Description
-----------

Restore any configuration that the cache had when previously enabled,
and re-enable the outer cache.

.. This file was automatic generated / don't edit.

