.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cgroup/stat.c

.. _`cgroup_cpu_stat_updated`:

cgroup_cpu_stat_updated
=======================

.. c:function:: void cgroup_cpu_stat_updated(struct cgroup *cgrp, int cpu)

    keep track of updated cpu_stat

    :param struct cgroup \*cgrp:
        target cgroup

    :param int cpu:
        cpu on which cpu_stat was updated

.. _`cgroup_cpu_stat_updated.description`:

Description
-----------

@cgrp's cpu_stat on \ ``cpu``\  was updated.  Put it on the parent's matching
cpu_stat->updated_children list.  See the comment on top of
cgroup_cpu_stat definition for details.

.. _`cgroup_cpu_stat_pop_updated`:

cgroup_cpu_stat_pop_updated
===========================

.. c:function:: struct cgroup *cgroup_cpu_stat_pop_updated(struct cgroup *pos, struct cgroup *root, int cpu)

    iterate and dismantle cpu_stat updated tree

    :param struct cgroup \*pos:
        current position

    :param struct cgroup \*root:
        root of the tree to traversal

    :param int cpu:
        target cpu

.. _`cgroup_cpu_stat_pop_updated.description`:

Description
-----------

Walks the udpated cpu_stat tree on \ ``cpu``\  from \ ``root``\ .  \ ``NULL``\  \ ``pos``\  starts
the traversal and \ ``NULL``\  return indicates the end.  During traversal,
each returned cgroup is unlinked from the tree.  Must be called with the
matching cgroup_cpu_stat_lock held.

The only ordering guarantee is that, for a parent and a child pair
covered by a given traversal, if a child is visited, its parent is
guaranteed to be visited afterwards.

.. _`cgroup_stat_flush`:

cgroup_stat_flush
=================

.. c:function:: void cgroup_stat_flush(struct cgroup *cgrp)

    flush stats in \ ``cgrp``\ 's subtree

    :param struct cgroup \*cgrp:
        target cgroup

.. _`cgroup_stat_flush.description`:

Description
-----------

Collect all per-cpu stats in \ ``cgrp``\ 's subtree into the global counters
and propagate them upwards.  After this function returns, all cgroups in
the subtree have up-to-date ->stat.

This also gets all cgroups in the subtree including \ ``cgrp``\  off the
->updated_children lists.

.. This file was automatic generated / don't edit.

