.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/swap_cgroup.c

.. _`swap_cgroup_cmpxchg`:

swap_cgroup_cmpxchg
===================

.. c:function:: unsigned short swap_cgroup_cmpxchg(swp_entry_t ent, unsigned short old, unsigned short new)

    cmpxchg mem_cgroup's id for this swp_entry.

    :param ent:
        swap entry to be cmpxchged
    :type ent: swp_entry_t

    :param old:
        old id
    :type old: unsigned short

    :param new:
        new id
    :type new: unsigned short

.. _`swap_cgroup_cmpxchg.description`:

Description
-----------

Returns old id at success, 0 at failure.
(There is no mem_cgroup using 0 as its id)

.. _`swap_cgroup_record`:

swap_cgroup_record
==================

.. c:function:: unsigned short swap_cgroup_record(swp_entry_t ent, unsigned short id, unsigned int nr_ents)

    record mem_cgroup for a set of swap entries

    :param ent:
        the first swap entry to be recorded into
    :type ent: swp_entry_t

    :param id:
        mem_cgroup to be recorded
    :type id: unsigned short

    :param nr_ents:
        number of swap entries to be recorded
    :type nr_ents: unsigned int

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

    :param ent:
        swap entry to be looked up.
    :type ent: swp_entry_t

.. _`lookup_swap_cgroup_id.description`:

Description
-----------

Returns ID of mem_cgroup at success. 0 at failure. (0 is invalid ID)

.. This file was automatic generated / don't edit.

