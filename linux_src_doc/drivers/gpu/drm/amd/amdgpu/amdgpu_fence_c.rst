.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_fence.c

.. _`amdgpu_fence_write`:

amdgpu_fence_write
==================

.. c:function:: void amdgpu_fence_write(struct amdgpu_ring *ring, u32 seq)

    write a fence value

    :param ring:
        ring the fence is associated with
    :type ring: struct amdgpu_ring \*

    :param seq:
        sequence number to write
    :type seq: u32

.. _`amdgpu_fence_write.description`:

Description
-----------

Writes a fence value to memory (all asics).

.. _`amdgpu_fence_read`:

amdgpu_fence_read
=================

.. c:function:: u32 amdgpu_fence_read(struct amdgpu_ring *ring)

    read a fence value

    :param ring:
        ring the fence is associated with
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_fence_read.description`:

Description
-----------

Reads a fence value from memory (all asics).
Returns the value of the fence read from memory.

.. _`amdgpu_fence_emit`:

amdgpu_fence_emit
=================

.. c:function:: int amdgpu_fence_emit(struct amdgpu_ring *ring, struct dma_fence **f, unsigned flags)

    emit a fence on the requested ring

    :param ring:
        ring the fence is associated with
    :type ring: struct amdgpu_ring \*

    :param f:
        resulting fence object
    :type f: struct dma_fence \*\*

    :param flags:
        *undescribed*
    :type flags: unsigned

.. _`amdgpu_fence_emit.description`:

Description
-----------

Emits a fence command on the requested ring (all asics).
Returns 0 on success, -ENOMEM on failure.

.. _`amdgpu_fence_emit_polling`:

amdgpu_fence_emit_polling
=========================

.. c:function:: int amdgpu_fence_emit_polling(struct amdgpu_ring *ring, uint32_t *s)

    emit a fence on the requeste ring

    :param ring:
        ring the fence is associated with
    :type ring: struct amdgpu_ring \*

    :param s:
        resulting sequence number
    :type s: uint32_t \*

.. _`amdgpu_fence_emit_polling.description`:

Description
-----------

Emits a fence command on the requested ring (all asics).
Used For polling fence.
Returns 0 on success, -ENOMEM on failure.

.. _`amdgpu_fence_schedule_fallback`:

amdgpu_fence_schedule_fallback
==============================

.. c:function:: void amdgpu_fence_schedule_fallback(struct amdgpu_ring *ring)

    schedule fallback check

    :param ring:
        pointer to struct amdgpu_ring
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_fence_schedule_fallback.description`:

Description
-----------

Start a timer as fallback to our interrupts.

.. _`amdgpu_fence_process`:

amdgpu_fence_process
====================

.. c:function:: bool amdgpu_fence_process(struct amdgpu_ring *ring)

    check for fence activity

    :param ring:
        pointer to struct amdgpu_ring
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_fence_process.description`:

Description
-----------

Checks the current fence value and calculates the last
signalled fence value. Wakes the fence queue if the
sequence number has increased.

Returns true if fence was processed

.. _`amdgpu_fence_fallback`:

amdgpu_fence_fallback
=====================

.. c:function:: void amdgpu_fence_fallback(struct timer_list *t)

    fallback for hardware interrupts

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`amdgpu_fence_fallback.description`:

Description
-----------

Checks for fence activity.

.. _`amdgpu_fence_wait_empty`:

amdgpu_fence_wait_empty
=======================

.. c:function:: int amdgpu_fence_wait_empty(struct amdgpu_ring *ring)

    wait for all fences to signal

    :param ring:
        ring index the fence is associated with
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_fence_wait_empty.description`:

Description
-----------

Wait for all fences on the requested ring to signal (all asics).
Returns 0 if the fences have passed, error for all other cases.

.. _`amdgpu_fence_wait_polling`:

amdgpu_fence_wait_polling
=========================

.. c:function:: signed long amdgpu_fence_wait_polling(struct amdgpu_ring *ring, uint32_t wait_seq, signed long timeout)

    busy wait for givn sequence number

    :param ring:
        ring index the fence is associated with
    :type ring: struct amdgpu_ring \*

    :param wait_seq:
        sequence number to wait
    :type wait_seq: uint32_t

    :param timeout:
        the timeout for waiting in usecs
    :type timeout: signed long

.. _`amdgpu_fence_wait_polling.description`:

Description
-----------

Wait for all fences on the requested ring to signal (all asics).
Returns left time if no timeout, 0 or minus if timeout.

.. _`amdgpu_fence_count_emitted`:

amdgpu_fence_count_emitted
==========================

.. c:function:: unsigned amdgpu_fence_count_emitted(struct amdgpu_ring *ring)

    get the count of emitted fences

    :param ring:
        ring the fence is associated with
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_fence_count_emitted.description`:

Description
-----------

Get the number of fences emitted on the requested ring (all asics).
Returns the number of emitted fences on the ring.  Used by the
dynpm code to ring track activity.

.. _`amdgpu_fence_driver_start_ring`:

amdgpu_fence_driver_start_ring
==============================

.. c:function:: int amdgpu_fence_driver_start_ring(struct amdgpu_ring *ring, struct amdgpu_irq_src *irq_src, unsigned irq_type)

    make the fence driver ready for use on the requested ring.

    :param ring:
        ring to start the fence driver on
    :type ring: struct amdgpu_ring \*

    :param irq_src:
        interrupt source to use for this ring
    :type irq_src: struct amdgpu_irq_src \*

    :param irq_type:
        interrupt type to use for this ring
    :type irq_type: unsigned

.. _`amdgpu_fence_driver_start_ring.description`:

Description
-----------

Make the fence driver ready for processing (all asics).
Not all asics have all rings, so each asic will only
start the fence driver on the rings it has.
Returns 0 for success, errors for failure.

.. _`amdgpu_fence_driver_init_ring`:

amdgpu_fence_driver_init_ring
=============================

.. c:function:: int amdgpu_fence_driver_init_ring(struct amdgpu_ring *ring, unsigned num_hw_submission)

    init the fence driver for the requested ring.

    :param ring:
        ring to init the fence driver on
    :type ring: struct amdgpu_ring \*

    :param num_hw_submission:
        number of entries on the hardware queue
    :type num_hw_submission: unsigned

.. _`amdgpu_fence_driver_init_ring.description`:

Description
-----------

Init the fence driver for the requested ring (all asics).
Helper function for \ :c:func:`amdgpu_fence_driver_init`\ .

.. _`amdgpu_fence_driver_init`:

amdgpu_fence_driver_init
========================

.. c:function:: int amdgpu_fence_driver_init(struct amdgpu_device *adev)

    init the fence driver for all possible rings.

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_fence_driver_init.description`:

Description
-----------

Init the fence driver for all possible rings (all asics).
Not all asics have all rings, so each asic will only
start the fence driver on the rings it has using
\ :c:func:`amdgpu_fence_driver_start_ring`\ .
Returns 0 for success.

.. _`amdgpu_fence_driver_fini`:

amdgpu_fence_driver_fini
========================

.. c:function:: void amdgpu_fence_driver_fini(struct amdgpu_device *adev)

    tear down the fence driver for all possible rings.

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_fence_driver_fini.description`:

Description
-----------

Tear down the fence driver for all possible rings (all asics).

.. _`amdgpu_fence_driver_suspend`:

amdgpu_fence_driver_suspend
===========================

.. c:function:: void amdgpu_fence_driver_suspend(struct amdgpu_device *adev)

    suspend the fence driver for all possible rings.

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_fence_driver_suspend.description`:

Description
-----------

Suspend the fence driver for all possible rings (all asics).

.. _`amdgpu_fence_driver_resume`:

amdgpu_fence_driver_resume
==========================

.. c:function:: void amdgpu_fence_driver_resume(struct amdgpu_device *adev)

    resume the fence driver for all possible rings.

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_fence_driver_resume.description`:

Description
-----------

Resume the fence driver for all possible rings (all asics).
Not all asics have all rings, so each asic will only
start the fence driver on the rings it has using
\ :c:func:`amdgpu_fence_driver_start_ring`\ .
Returns 0 for success.

.. _`amdgpu_fence_driver_force_completion`:

amdgpu_fence_driver_force_completion
====================================

.. c:function:: void amdgpu_fence_driver_force_completion(struct amdgpu_ring *ring)

    force signal latest fence of ring

    :param ring:
        fence of the ring to signal
    :type ring: struct amdgpu_ring \*

.. _`amdgpu_fence_enable_signaling`:

amdgpu_fence_enable_signaling
=============================

.. c:function:: bool amdgpu_fence_enable_signaling(struct dma_fence *f)

    enable signalling on fence

    :param f:
        *undescribed*
    :type f: struct dma_fence \*

.. _`amdgpu_fence_enable_signaling.description`:

Description
-----------

This function is called with fence_queue lock held, and adds a callback
to fence_queue that checks if this fence is signaled, and if so it
signals the fence and removes itself.

.. _`amdgpu_fence_free`:

amdgpu_fence_free
=================

.. c:function:: void amdgpu_fence_free(struct rcu_head *rcu)

    free up the fence memory

    :param rcu:
        RCU callback head
    :type rcu: struct rcu_head \*

.. _`amdgpu_fence_free.description`:

Description
-----------

Free up the fence memory after the RCU grace period.

.. _`amdgpu_fence_release`:

amdgpu_fence_release
====================

.. c:function:: void amdgpu_fence_release(struct dma_fence *f)

    callback that fence can be freed

    :param f:
        *undescribed*
    :type f: struct dma_fence \*

.. _`amdgpu_fence_release.description`:

Description
-----------

This function is called when the reference count becomes zero.
It just RCU schedules freeing up the fence.

.. _`amdgpu_debugfs_gpu_recover`:

amdgpu_debugfs_gpu_recover
==========================

.. c:function:: int amdgpu_debugfs_gpu_recover(struct seq_file *m, void *data)

    manually trigger a gpu reset & recover

    :param m:
        *undescribed*
    :type m: struct seq_file \*

    :param data:
        *undescribed*
    :type data: void \*

.. _`amdgpu_debugfs_gpu_recover.description`:

Description
-----------

Manually trigger a gpu reset at the next fence wait.

.. This file was automatic generated / don't edit.

