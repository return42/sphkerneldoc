.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/cgroup/rstat.c

.. _`cgroup_rstat_updated`:

cgroup_rstat_updated
====================

.. c:function:: void cgroup_rstat_updated(struct cgroup *cgrp, int cpu)

    keep track of updated rstat_cpu

    :param struct cgroup \*cgrp:
        target cgroup

    :param int cpu:
        cpu on which rstat_cpu was updated

.. _`cgroup_rstat_updated.description`:

Description
-----------

\ ``cgrp``\ 's rstat_cpu on \ ``cpu``\  was updated.  Put it on the parent's matching
rstat_cpu->updated_children list.  See the comment on top of
cgroup_rstat_cpu definition for details.

.. _`cgroup_rstat_cpu_pop_updated`:

cgroup_rstat_cpu_pop_updated
============================

.. c:function:: struct cgroup *cgroup_rstat_cpu_pop_updated(struct cgroup *pos, struct cgroup *root, int cpu)

    iterate and dismantle rstat_cpu updated tree

    :param struct cgroup \*pos:
        current position

    :param struct cgroup \*root:
        root of the tree to traversal

    :param int cpu:
        target cpu

.. _`cgroup_rstat_cpu_pop_updated.description`:

Description
-----------

Walks the udpated rstat_cpu tree on \ ``cpu``\  from \ ``root``\ .  \ ``NULL``\  \ ``pos``\  starts
the traversal and \ ``NULL``\  return indicates the end.  During traversal,
each returned cgroup is unlinked from the tree.  Must be called with the
matching cgroup_rstat_cpu_lock held.

The only ordering guarantee is that, for a parent and a child pair
covered by a given traversal, if a child is visited, its parent is
guaranteed to be visited afterwards.

.. _`cgroup_rstat_flush`:

cgroup_rstat_flush
==================

.. c:function:: void cgroup_rstat_flush(struct cgroup *cgrp)

    flush stats in \ ``cgrp``\ 's subtree

    :param struct cgroup \*cgrp:
        target cgroup

.. _`cgroup_rstat_flush.description`:

Description
-----------

Collect all per-cpu stats in \ ``cgrp``\ 's subtree into the global counters
and propagate them upwards.  After this function returns, all cgroups in
the subtree have up-to-date ->stat.

This also gets all cgroups in the subtree including \ ``cgrp``\  off the
->updated_children lists.

This function may block.

.. _`cgroup_rstat_flush_irqsafe`:

cgroup_rstat_flush_irqsafe
==========================

.. c:function:: void cgroup_rstat_flush_irqsafe(struct cgroup *cgrp)

    irqsafe version of \ :c:func:`cgroup_rstat_flush`\ 

    :param struct cgroup \*cgrp:
        target cgroup

.. _`cgroup_rstat_flush_irqsafe.description`:

Description
-----------

This function can be called from any context.

.. _`cgroup_rstat_flush_hold`:

cgroup_rstat_flush_hold
=======================

.. c:function:: void cgroup_rstat_flush_hold(struct cgroup *cgrp)

    flush stats in \ ``cgrp``\ 's subtree and hold

    :param struct cgroup \*cgrp:
        target cgroup

.. _`cgroup_rstat_flush_hold.description`:

Description
-----------

Flush stats in \ ``cgrp``\ 's subtree and prevent further flushes.  Must be
paired with \ :c:func:`cgroup_rstat_flush_release`\ .

This function may block.

.. _`cgroup_rstat_flush_release`:

cgroup_rstat_flush_release
==========================

.. c:function:: void cgroup_rstat_flush_release( void)

    release \ :c:func:`cgroup_rstat_flush_hold`\ 

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

