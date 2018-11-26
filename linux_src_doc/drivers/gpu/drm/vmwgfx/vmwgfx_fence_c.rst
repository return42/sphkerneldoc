.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_fence.c

.. _`vmw_event_fence_action`:

struct vmw_event_fence_action
=============================

.. c:type:: struct vmw_event_fence_action

    fence action that delivers a drm event.

.. _`vmw_event_fence_action.definition`:

Definition
----------

.. code-block:: c

    struct vmw_event_fence_action {
        struct vmw_fence_action action;
        struct drm_pending_event *event;
        struct vmw_fence_obj *fence;
        struct drm_device *dev;
        uint32_t *tv_sec;
        uint32_t *tv_usec;
    }

.. _`vmw_event_fence_action.members`:

Members
-------

action
    A struct vmw_fence_action to hook up to a fence.

event
    *undescribed*

fence
    A referenced pointer to the fence to keep it alive while \ ``action``\ 
    hangs on it.

dev
    Pointer to a struct drm_device so we can access the event stuff.

tv_sec
    If non-null, the variable pointed to will be assigned
    current time tv_sec val when the fence signals.

tv_usec
    Must be set if \ ``tv_sec``\  is set, and the variable pointed to will
    be assigned the current time tv_usec val when the fence signals.

.. _`vmw_fence_obj_destroy`:

vmw_fence_obj_destroy
=====================

.. c:function:: void vmw_fence_obj_destroy(struct dma_fence *f)

    Typically the vmw_fences_update function is called

    :param f:
        *undescribed*
    :type f: struct dma_fence \*

.. _`vmw_fence_obj_destroy.description`:

Description
-----------

a) When a new fence seqno has been submitted by the fifo code.
b) On-demand when we have waiters. Sleeping waiters will switch on the
ANY_FENCE irq and call vmw_fences_update function each time an ANY_FENCE
irq is received. When the last fence waiter is gone, that IRQ is masked
away.

In situations where there are no waiters and we don't submit any new fences,
fence objects may not be signaled. This is perfectly OK, since there are
no consumers of the signaled data, but that is NOT ok when there are fence
actions attached to a fence. The fencing subsystem then makes use of the
FENCE_GOAL irq and sets the fence goal seqno to that of the next fence
which has an action attached, and each time vmw_fences_update is called,
the subsystem makes sure the fence goal seqno is updated.

The fence goal seqno irq is on as long as there are unsignaled fence
objects with actions attached to them.

.. _`vmw_fence_work_func`:

vmw_fence_work_func
===================

.. c:function:: void vmw_fence_work_func(struct work_struct *work)

    This is done from a workqueue so we don't have to execute signal actions from atomic context.

    :param work:
        *undescribed*
    :type work: struct work_struct \*

.. _`vmw_fence_goal_new_locked`:

vmw_fence_goal_new_locked
=========================

.. c:function:: bool vmw_fence_goal_new_locked(struct vmw_fence_manager *fman, u32 passed_seqno)

    Figure out a new device fence goal seqno if needed.

    :param fman:
        Pointer to a fence manager.
    :type fman: struct vmw_fence_manager \*

    :param passed_seqno:
        The seqno the device currently signals as passed.
    :type passed_seqno: u32

.. _`vmw_fence_goal_new_locked.description`:

Description
-----------

This function should be called with the fence manager lock held.
It is typically called when we have a new passed_seqno, and
we might need to update the fence goal. It checks to see whether
the current fence goal has already passed, and, in that case,
scans through all unsignaled fences to get the next fence object with an
action attached, and sets the seqno of that fence as a new fence goal.

returns true if the device goal seqno was updated. False otherwise.

.. _`vmw_fence_goal_check_locked`:

vmw_fence_goal_check_locked
===========================

.. c:function:: bool vmw_fence_goal_check_locked(struct vmw_fence_obj *fence)

    Replace the device fence goal seqno if needed.

    :param fence:
        Pointer to a struct vmw_fence_obj the seqno of which should be
        considered as a device fence goal.
    :type fence: struct vmw_fence_obj \*

.. _`vmw_fence_goal_check_locked.description`:

Description
-----------

This function should be called with the fence manager lock held.
It is typically called when an action has been attached to a fence to
check whether the seqno of that fence should be used for a fence
goal interrupt. This is typically needed if the current fence goal is
invalid, or has a higher seqno than that of the current fence object.

returns true if the device goal seqno was updated. False otherwise.

.. _`vmw_wait_dma_fence`:

vmw_wait_dma_fence
==================

.. c:function:: int vmw_wait_dma_fence(struct vmw_fence_manager *fman, struct dma_fence *fence)

    Wait for a dma fence

    :param fman:
        pointer to a fence manager
    :type fman: struct vmw_fence_manager \*

    :param fence:
        DMA fence to wait on
    :type fence: struct dma_fence \*

.. _`vmw_wait_dma_fence.description`:

Description
-----------

This function handles the case when the fence is actually a fence
array.  If that's the case, it'll wait on each of the child fence

.. _`vmw_fence_fifo_down`:

vmw_fence_fifo_down
===================

.. c:function:: void vmw_fence_fifo_down(struct vmw_fence_manager *fman)

    signal all unsignaled fence objects.

    :param fman:
        *undescribed*
    :type fman: struct vmw_fence_manager \*

.. _`vmw_fence_obj_lookup`:

vmw_fence_obj_lookup
====================

.. c:function:: struct ttm_base_object *vmw_fence_obj_lookup(struct ttm_object_file *tfile, u32 handle)

    Look up a user-space fence object

    :param tfile:
        A struct ttm_object_file identifying the caller.
    :type tfile: struct ttm_object_file \*

    :param handle:
        A handle identifying the fence object.
    :type handle: u32

.. _`vmw_fence_obj_lookup.description`:

Description
-----------

The fence object is looked up and type-checked. The caller needs
to have opened the fence object first, but since that happens on
creation and fence objects aren't shareable, that's not an
issue currently.

.. _`vmw_event_fence_action_seq_passed`:

vmw_event_fence_action_seq_passed
=================================

.. c:function:: void vmw_event_fence_action_seq_passed(struct vmw_fence_action *action)

    :param action:
        The struct vmw_fence_action embedded in a struct
        vmw_event_fence_action.
    :type action: struct vmw_fence_action \*

.. _`vmw_event_fence_action_seq_passed.description`:

Description
-----------

This function is called when the seqno of the fence where \ ``action``\  is
attached has passed. It queues the event on the submitter's event list.
This function is always called from atomic context.

.. _`vmw_event_fence_action_cleanup`:

vmw_event_fence_action_cleanup
==============================

.. c:function:: void vmw_event_fence_action_cleanup(struct vmw_fence_action *action)

    :param action:
        The struct vmw_fence_action embedded in a struct
        vmw_event_fence_action.
    :type action: struct vmw_fence_action \*

.. _`vmw_event_fence_action_cleanup.description`:

Description
-----------

This function is the struct vmw_fence_action destructor. It's typically
called from a workqueue.

.. _`vmw_fence_obj_add_action`:

vmw_fence_obj_add_action
========================

.. c:function:: void vmw_fence_obj_add_action(struct vmw_fence_obj *fence, struct vmw_fence_action *action)

    Add an action to a fence object.

    :param fence:
        *undescribed*
    :type fence: struct vmw_fence_obj \*

    :param action:
        *undescribed*
    :type action: struct vmw_fence_action \*

.. _`vmw_fence_obj_add_action.description`:

Description
-----------

\ ``fence``\  - The fence object.
\ ``action``\  - The action to add.

Note that the action callbacks may be executed before this function
returns.

.. _`vmw_event_fence_action_queue`:

vmw_event_fence_action_queue
============================

.. c:function:: int vmw_event_fence_action_queue(struct drm_file *file_priv, struct vmw_fence_obj *fence, struct drm_pending_event *event, uint32_t *tv_sec, uint32_t *tv_usec, bool interruptible)

    Post an event for sending when a fence object seqno has passed.

    :param file_priv:
        The file connection on which the event should be posted.
    :type file_priv: struct drm_file \*

    :param fence:
        The fence object on which to post the event.
    :type fence: struct vmw_fence_obj \*

    :param event:
        Event to be posted. This event should've been alloced
        using k[mz]alloc, and should've been completely initialized.
    :type event: struct drm_pending_event \*

    :param tv_sec:
        *undescribed*
    :type tv_sec: uint32_t \*

    :param tv_usec:
        *undescribed*
    :type tv_usec: uint32_t \*

    :param interruptible:
        Interruptible waits if possible.
    :type interruptible: bool

.. _`vmw_event_fence_action_queue.description`:

Description
-----------

As a side effect, the object pointed to by \ ``event``\  may have been
freed when this function returns. If this function returns with
an error code, the caller needs to free that object.

.. This file was automatic generated / don't edit.

