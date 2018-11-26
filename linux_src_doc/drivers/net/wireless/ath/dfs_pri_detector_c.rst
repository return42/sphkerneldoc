.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/dfs_pri_detector.c

.. _`pulse_elem`:

struct pulse_elem
=================

.. c:type:: struct pulse_elem

    elements in pulse queue

.. _`pulse_elem.definition`:

Definition
----------

.. code-block:: c

    struct pulse_elem {
        struct list_head head;
        u64 ts;
    }

.. _`pulse_elem.members`:

Members
-------

head
    *undescribed*

ts
    time stamp in usecs

.. _`pde_get_multiple`:

pde_get_multiple
================

.. c:function:: u32 pde_get_multiple(u32 val, u32 fraction, u32 tolerance)

    get number of multiples considering a given tolerance \ ``return``\  factor if abs(val - factor\*fraction) <= tolerance, 0 otherwise

    :param val:
        *undescribed*
    :type val: u32

    :param fraction:
        *undescribed*
    :type fraction: u32

    :param tolerance:
        *undescribed*
    :type tolerance: u32

.. _`singleton-pulse-and-sequence-pools`:

Singleton Pulse and Sequence Pools
==================================

Instances of pri_sequence and pulse_elem are kept in singleton pools to
reduce the number of dynamic allocations. They are shared between all
instances and grow up to the peak number of simultaneously used objects.

Memory is freed after all references to the pools are released.

.. This file was automatic generated / don't edit.

