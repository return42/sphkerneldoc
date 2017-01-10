.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_fence.c

.. _`radeon_fence_write`:

radeon_fence_write
==================

.. c:function:: void radeon_fence_write(struct radeon_device *rdev, u32 seq, int ring)

    write a fence value

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 seq:
        sequence number to write

    :param int ring:
        ring index the fence is associated with

.. _`radeon_fence_write.description`:

Description
-----------

Writes a fence value to memory or a scratch register (all asics).

.. _`radeon_fence_read`:

radeon_fence_read
=================

.. c:function:: u32 radeon_fence_read(struct radeon_device *rdev, int ring)

    read a fence value

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int ring:
        ring index the fence is associated with

.. _`radeon_fence_read.description`:

Description
-----------

Reads a fence value from memory or a scratch register (all asics).
Returns the value of the fence read from memory or register.

.. _`radeon_fence_schedule_check`:

radeon_fence_schedule_check
===========================

.. c:function:: void radeon_fence_schedule_check(struct radeon_device *rdev, int ring)

    schedule lockup check

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int ring:
        ring index we should work with

.. _`radeon_fence_schedule_check.description`:

Description
-----------

Queues a delayed work item to check for lockups.

.. _`radeon_fence_emit`:

radeon_fence_emit
=================

.. c:function:: int radeon_fence_emit(struct radeon_device *rdev, struct radeon_fence **fence, int ring)

    emit a fence on the requested ring

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_fence \*\*fence:
        radeon fence object

    :param int ring:
        ring index the fence is associated with

.. _`radeon_fence_emit.description`:

Description
-----------

Emits a fence command on the requested ring (all asics).
Returns 0 on success, -ENOMEM on failure.

.. _`radeon_fence_check_signaled`:

radeon_fence_check_signaled
===========================

.. c:function:: int radeon_fence_check_signaled(wait_queue_t *wait, unsigned mode, int flags, void *key)

    callback from fence_queue

    :param wait_queue_t \*wait:
        *undescribed*

    :param unsigned mode:
        *undescribed*

    :param int flags:
        *undescribed*

    :param void \*key:
        *undescribed*

.. _`radeon_fence_check_signaled.description`:

Description
-----------

this function is called with fence_queue lock held, which is also used
for the fence locking itself, so unlocked variants are used for
fence_signal, and remove_wait_queue.

.. _`radeon_fence_activity`:

radeon_fence_activity
=====================

.. c:function:: bool radeon_fence_activity(struct radeon_device *rdev, int ring)

    check for fence activity

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int ring:
        ring index the fence is associated with

.. _`radeon_fence_activity.description`:

Description
-----------

Checks the current fence value and calculates the last
signalled fence value. Returns true if activity occured
on the ring, and the fence_queue should be waken up.

.. _`radeon_fence_check_lockup`:

radeon_fence_check_lockup
=========================

.. c:function:: void radeon_fence_check_lockup(struct work_struct *work)

    check for hardware lockup

    :param struct work_struct \*work:
        delayed work item

.. _`radeon_fence_check_lockup.description`:

Description
-----------

Checks for fence activity and if there is none probe
the hardware if a lockup occured.

.. _`radeon_fence_process`:

radeon_fence_process
====================

.. c:function:: void radeon_fence_process(struct radeon_device *rdev, int ring)

    process a fence

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int ring:
        ring index the fence is associated with

.. _`radeon_fence_process.description`:

Description
-----------

Checks the current fence value and wakes the fence queue
if the sequence number has increased (all asics).

.. _`radeon_fence_seq_signaled`:

radeon_fence_seq_signaled
=========================

.. c:function:: bool radeon_fence_seq_signaled(struct radeon_device *rdev, u64 seq, unsigned ring)

    check if a fence sequence number has signaled

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param u64 seq:
        sequence number

    :param unsigned ring:
        ring index the fence is associated with

.. _`radeon_fence_seq_signaled.description`:

Description
-----------

Check if the last signaled fence sequnce number is >= the requested
sequence number (all asics).
Returns true if the fence has signaled (current fence value
is >= requested value) or false if it has not (current fence
value is < the requested value.  Helper function for
\ :c:func:`radeon_fence_signaled`\ .

.. _`radeon_fence_enable_signaling`:

radeon_fence_enable_signaling
=============================

.. c:function:: bool radeon_fence_enable_signaling(struct dma_fence *f)

    enable signalling on fence

    :param struct dma_fence \*f:
        *undescribed*

.. _`radeon_fence_enable_signaling.description`:

Description
-----------

This function is called with fence_queue lock held, and adds a callback
to fence_queue that checks if this fence is signaled, and if so it
signals the fence and removes itself.

.. _`radeon_fence_signaled`:

radeon_fence_signaled
=====================

.. c:function:: bool radeon_fence_signaled(struct radeon_fence *fence)

    check if a fence has signaled

    :param struct radeon_fence \*fence:
        radeon fence object

.. _`radeon_fence_signaled.description`:

Description
-----------

Check if the requested fence has signaled (all asics).
Returns true if the fence has signaled or false if it has not.

.. _`radeon_fence_any_seq_signaled`:

radeon_fence_any_seq_signaled
=============================

.. c:function:: bool radeon_fence_any_seq_signaled(struct radeon_device *rdev, u64 *seq)

    check if any sequence number is signaled

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param u64 \*seq:
        sequence numbers

.. _`radeon_fence_any_seq_signaled.description`:

Description
-----------

Check if the last signaled fence sequnce number is >= the requested
sequence number (all asics).
Returns true if any has signaled (current value is >= requested value)
or false if it has not. Helper function for radeon_fence_wait_seq.

.. _`radeon_fence_wait_seq_timeout`:

radeon_fence_wait_seq_timeout
=============================

.. c:function:: long radeon_fence_wait_seq_timeout(struct radeon_device *rdev, u64 *target_seq, bool intr, long timeout)

    wait for a specific sequence numbers

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param u64 \*target_seq:
        sequence number(s) we want to wait for

    :param bool intr:
        use interruptable sleep

    :param long timeout:
        maximum time to wait, or MAX_SCHEDULE_TIMEOUT for infinite wait

.. _`radeon_fence_wait_seq_timeout.description`:

Description
-----------

Wait for the requested sequence number(s) to be written by any ring
(all asics).  Sequnce number array is indexed by ring id.
\ ``intr``\  selects whether to use interruptable (true) or non-interruptable
(false) sleep when waiting for the sequence number.  Helper function
for radeon_fence_wait\_\*().
Returns remaining time if the sequence number has passed, 0 when
the wait timeout, or an error for all other cases.
-EDEADLK is returned when a GPU lockup has been detected.

.. _`radeon_fence_wait_timeout`:

radeon_fence_wait_timeout
=========================

.. c:function:: long radeon_fence_wait_timeout(struct radeon_fence *fence, bool intr, long timeout)

    wait for a fence to signal with timeout

    :param struct radeon_fence \*fence:
        radeon fence object

    :param bool intr:
        use interruptible sleep

    :param long timeout:
        maximum time to wait, or MAX_SCHEDULE_TIMEOUT for infinite wait
        Returns remaining time if the sequence number has passed, 0 when
        the wait timeout, or an error for all other cases.

.. _`radeon_fence_wait_timeout.description`:

Description
-----------

Wait for the requested fence to signal (all asics).
\ ``intr``\  selects whether to use interruptable (true) or non-interruptable
(false) sleep when waiting for the fence.

.. _`radeon_fence_wait`:

radeon_fence_wait
=================

.. c:function:: int radeon_fence_wait(struct radeon_fence *fence, bool intr)

    wait for a fence to signal

    :param struct radeon_fence \*fence:
        radeon fence object

    :param bool intr:
        use interruptible sleep

.. _`radeon_fence_wait.description`:

Description
-----------

Wait for the requested fence to signal (all asics).
\ ``intr``\  selects whether to use interruptable (true) or non-interruptable
(false) sleep when waiting for the fence.
Returns 0 if the fence has passed, error for all other cases.

.. _`radeon_fence_wait_any`:

radeon_fence_wait_any
=====================

.. c:function:: int radeon_fence_wait_any(struct radeon_device *rdev, struct radeon_fence **fences, bool intr)

    wait for a fence to signal on any ring

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param struct radeon_fence \*\*fences:
        radeon fence object(s)

    :param bool intr:
        use interruptable sleep

.. _`radeon_fence_wait_any.description`:

Description
-----------

Wait for any requested fence to signal (all asics).  Fence
array is indexed by ring id.  \ ``intr``\  selects whether to use
interruptable (true) or non-interruptable (false) sleep when
waiting for the fences. Used by the suballocator.
Returns 0 if any fence has passed, error for all other cases.

.. _`radeon_fence_wait_next`:

radeon_fence_wait_next
======================

.. c:function:: int radeon_fence_wait_next(struct radeon_device *rdev, int ring)

    wait for the next fence to signal

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        ring index the fence is associated with

.. _`radeon_fence_wait_next.description`:

Description
-----------

Wait for the next fence on the requested ring to signal (all asics).
Returns 0 if the next fence has passed, error for all other cases.
Caller must hold ring lock.

.. _`radeon_fence_wait_empty`:

radeon_fence_wait_empty
=======================

.. c:function:: int radeon_fence_wait_empty(struct radeon_device *rdev, int ring)

    wait for all fences to signal

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        ring index the fence is associated with

.. _`radeon_fence_wait_empty.description`:

Description
-----------

Wait for all fences on the requested ring to signal (all asics).
Returns 0 if the fences have passed, error for all other cases.
Caller must hold ring lock.

.. _`radeon_fence_ref`:

radeon_fence_ref
================

.. c:function:: struct radeon_fence *radeon_fence_ref(struct radeon_fence *fence)

    take a ref on a fence

    :param struct radeon_fence \*fence:
        radeon fence object

.. _`radeon_fence_ref.description`:

Description
-----------

Take a reference on a fence (all asics).
Returns the fence.

.. _`radeon_fence_unref`:

radeon_fence_unref
==================

.. c:function:: void radeon_fence_unref(struct radeon_fence **fence)

    remove a ref on a fence

    :param struct radeon_fence \*\*fence:
        radeon fence object

.. _`radeon_fence_unref.description`:

Description
-----------

Remove a reference on a fence (all asics).

.. _`radeon_fence_count_emitted`:

radeon_fence_count_emitted
==========================

.. c:function:: unsigned radeon_fence_count_emitted(struct radeon_device *rdev, int ring)

    get the count of emitted fences

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        ring index the fence is associated with

.. _`radeon_fence_count_emitted.description`:

Description
-----------

Get the number of fences emitted on the requested ring (all asics).
Returns the number of emitted fences on the ring.  Used by the
dynpm code to ring track activity.

.. _`radeon_fence_need_sync`:

radeon_fence_need_sync
======================

.. c:function:: bool radeon_fence_need_sync(struct radeon_fence *fence, int dst_ring)

    do we need a semaphore

    :param struct radeon_fence \*fence:
        radeon fence object

    :param int dst_ring:
        which ring to check against

.. _`radeon_fence_need_sync.description`:

Description
-----------

Check if the fence needs to be synced against another ring
(all asics).  If so, we need to emit a semaphore.
Returns true if we need to sync with another ring, false if
not.

.. _`radeon_fence_note_sync`:

radeon_fence_note_sync
======================

.. c:function:: void radeon_fence_note_sync(struct radeon_fence *fence, int dst_ring)

    record the sync point

    :param struct radeon_fence \*fence:
        radeon fence object

    :param int dst_ring:
        which ring to check against

.. _`radeon_fence_note_sync.description`:

Description
-----------

Note the sequence number at which point the fence will
be synced with the requested ring (all asics).

.. _`radeon_fence_driver_start_ring`:

radeon_fence_driver_start_ring
==============================

.. c:function:: int radeon_fence_driver_start_ring(struct radeon_device *rdev, int ring)

    make the fence driver ready for use on the requested ring.

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        ring index to start the fence driver on

.. _`radeon_fence_driver_start_ring.description`:

Description
-----------

Make the fence driver ready for processing (all asics).
Not all asics have all rings, so each asic will only
start the fence driver on the rings it has.
Returns 0 for success, errors for failure.

.. _`radeon_fence_driver_init_ring`:

radeon_fence_driver_init_ring
=============================

.. c:function:: void radeon_fence_driver_init_ring(struct radeon_device *rdev, int ring)

    init the fence driver for the requested ring.

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        ring index to start the fence driver on

.. _`radeon_fence_driver_init_ring.description`:

Description
-----------

Init the fence driver for the requested ring (all asics).
Helper function for \ :c:func:`radeon_fence_driver_init`\ .

.. _`radeon_fence_driver_init`:

radeon_fence_driver_init
========================

.. c:function:: int radeon_fence_driver_init(struct radeon_device *rdev)

    init the fence driver for all possible rings.

    :param struct radeon_device \*rdev:
        radeon device pointer

.. _`radeon_fence_driver_init.description`:

Description
-----------

Init the fence driver for all possible rings (all asics).
Not all asics have all rings, so each asic will only
start the fence driver on the rings it has using
\ :c:func:`radeon_fence_driver_start_ring`\ .
Returns 0 for success.

.. _`radeon_fence_driver_fini`:

radeon_fence_driver_fini
========================

.. c:function:: void radeon_fence_driver_fini(struct radeon_device *rdev)

    tear down the fence driver for all possible rings.

    :param struct radeon_device \*rdev:
        radeon device pointer

.. _`radeon_fence_driver_fini.description`:

Description
-----------

Tear down the fence driver for all possible rings (all asics).

.. _`radeon_fence_driver_force_completion`:

radeon_fence_driver_force_completion
====================================

.. c:function:: void radeon_fence_driver_force_completion(struct radeon_device *rdev, int ring)

    force all fence waiter to complete

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        the ring to complete

.. _`radeon_fence_driver_force_completion.description`:

Description
-----------

In case of GPU reset failure make sure no process keep waiting on fence
that will never complete.

.. _`radeon_debugfs_gpu_reset`:

radeon_debugfs_gpu_reset
========================

.. c:function:: int radeon_debugfs_gpu_reset(struct seq_file *m, void *data)

    manually trigger a gpu reset

    :param struct seq_file \*m:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`radeon_debugfs_gpu_reset.description`:

Description
-----------

Manually trigger a gpu reset at the next fence wait.

.. This file was automatic generated / don't edit.

