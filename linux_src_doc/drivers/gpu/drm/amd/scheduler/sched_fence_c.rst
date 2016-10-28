.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/scheduler/sched_fence.c

.. _`amd_sched_fence_free`:

amd_sched_fence_free
====================

.. c:function:: void amd_sched_fence_free(struct rcu_head *rcu)

    free up the fence memory

    :param struct rcu_head \*rcu:
        RCU callback head

.. _`amd_sched_fence_free.description`:

Description
-----------

Free up the fence memory after the RCU grace period.

.. _`amd_sched_fence_release`:

amd_sched_fence_release
=======================

.. c:function:: void amd_sched_fence_release(struct fence *f)

    callback that fence can be freed

    :param struct fence \*f:
        *undescribed*

.. _`amd_sched_fence_release.description`:

Description
-----------

This function is called when the reference count becomes zero.
It just RCU schedules freeing up the fence.

.. This file was automatic generated / don't edit.

