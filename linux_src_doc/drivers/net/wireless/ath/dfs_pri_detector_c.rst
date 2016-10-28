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

    :param u32 val:
        *undescribed*

    :param u32 fraction:
        *undescribed*

    :param u32 tolerance:
        *undescribed*

.. This file was automatic generated / don't edit.

