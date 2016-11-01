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

.. _`amd_sched_fence_release_scheduled`:

amd_sched_fence_release_scheduled
=================================

.. c:function:: void amd_sched_fence_release_scheduled(struct fence *f)

    callback that fence can be freed

    :param struct fence \*f:
        *undescribed*

.. _`amd_sched_fence_release_scheduled.description`:

Description
-----------

This function is called when the reference count becomes zero.
It just RCU schedules freeing up the fence.

.. _`amd_sched_fence_release_finished`:

amd_sched_fence_release_finished
================================

.. c:function:: void amd_sched_fence_release_finished(struct fence *f)

    drop extra reference

    :param struct fence \*f:
        fence

.. _`amd_sched_fence_release_finished.description`:

Description
-----------

Drop the extra reference from the scheduled fence to the base fence.

.. This file was automatic generated / don't edit.

