.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/swap_cgroup.c

.. _`swap_cgroup_cmpxchg`:

swap_cgroup_cmpxchg
===================

.. c:function:: unsigned short swap_cgroup_cmpxchg(swp_entry_t ent, unsigned short old, unsigned short new)

    cmpxchg mem_cgroup's id for this swp_entry.

    :param swp_entry_t ent:
        swap entry to be cmpxchged

    :param unsigned short old:
        old id

    :param unsigned short new:
        new id

.. _`swap_cgroup_cmpxchg.description`:

Description
-----------

Returns old id at success, 0 at failure.
(There is no mem_cgroup using 0 as its id)

.. _`swap_cgroup_record`:

swap_cgroup_record
==================

.. c:function:: unsigned short swap_cgroup_record(swp_entry_t ent, unsigned short id)

    record mem_cgroup for this swp_entry.

    :param swp_entry_t ent:
        swap entry to be recorded into

    :param unsigned short id:
        mem_cgroup to be recorded

.. _`swap_cgroup_record.description`:

Description
-----------

Returns old value at success, 0 at failure.
(Of course, old value can be 0.)

.. _`lookup_swap_cgroup_id`:

lookup_swap_cgroup_id
=====================

.. c:function:: unsigned short lookup_swap_cgroup_id(swp_entry_t ent)

    lookup mem_cgroup id tied to swap entry

    :param swp_entry_t ent:
        swap entry to be looked up.

.. _`lookup_swap_cgroup_id.description`:

Description
-----------

Returns ID of mem_cgroup at success. 0 at failure. (0 is invalid ID)

.. This file was automatic generated / don't edit.
