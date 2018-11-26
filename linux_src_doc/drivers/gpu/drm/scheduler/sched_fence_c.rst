.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/scheduler/sched_fence.c

.. _`drm_sched_fence_free`:

drm_sched_fence_free
====================

.. c:function:: void drm_sched_fence_free(struct rcu_head *rcu)

    free up the fence memory

    :param rcu:
        RCU callback head
    :type rcu: struct rcu_head \*

.. _`drm_sched_fence_free.description`:

Description
-----------

Free up the fence memory after the RCU grace period.

.. _`drm_sched_fence_release_scheduled`:

drm_sched_fence_release_scheduled
=================================

.. c:function:: void drm_sched_fence_release_scheduled(struct dma_fence *f)

    callback that fence can be freed

    :param f:
        *undescribed*
    :type f: struct dma_fence \*

.. _`drm_sched_fence_release_scheduled.description`:

Description
-----------

This function is called when the reference count becomes zero.
It just RCU schedules freeing up the fence.

.. _`drm_sched_fence_release_finished`:

drm_sched_fence_release_finished
================================

.. c:function:: void drm_sched_fence_release_finished(struct dma_fence *f)

    drop extra reference

    :param f:
        fence
    :type f: struct dma_fence \*

.. _`drm_sched_fence_release_finished.description`:

Description
-----------

Drop the extra reference from the scheduled fence to the base fence.

.. This file was automatic generated / don't edit.

