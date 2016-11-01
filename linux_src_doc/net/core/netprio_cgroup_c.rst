.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/core/netprio_cgroup.c

.. _`netprio_prio`:

netprio_prio
============

.. c:function:: u32 netprio_prio(struct cgroup_subsys_state *css, struct net_device *dev)

    return the effective netprio of a cgroup-net_device pair

    :param struct cgroup_subsys_state \*css:
        css part of the target pair

    :param struct net_device \*dev:
        net_device part of the target pair

.. _`netprio_prio.description`:

Description
-----------

Should be called under RCU read or rtnl lock.

.. _`netprio_set_prio`:

netprio_set_prio
================

.. c:function:: int netprio_set_prio(struct cgroup_subsys_state *css, struct net_device *dev, u32 prio)

    set netprio on a cgroup-net_device pair

    :param struct cgroup_subsys_state \*css:
        css part of the target pair

    :param struct net_device \*dev:
        net_device part of the target pair

    :param u32 prio:
        prio to set

.. _`netprio_set_prio.description`:

Description
-----------

Set netprio to \ ``prio``\  on \ ``css``\ -@dev pair.  Should be called under rtnl
lock and may fail under memory pressure for non-zero \ ``prio``\ .

.. This file was automatic generated / don't edit.

