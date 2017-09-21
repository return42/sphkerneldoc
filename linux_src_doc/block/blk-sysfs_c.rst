.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-sysfs.c

.. _`__blk_release_queue`:

__blk_release_queue
===================

.. c:function:: void __blk_release_queue(struct work_struct *work)

    release a request queue when it is no longer needed

    :param struct work_struct \*work:
        pointer to the release_work member of the request queue to be released

.. _`__blk_release_queue.description`:

Description
-----------

    blk_release_queue is the counterpart of \ :c:func:`blk_init_queue`\ . It should be
    called when a request queue is being released; typically when a block
    device is being de-registered. Its primary task it to free the queue
    itself.

.. _`__blk_release_queue.notes`:

Notes
-----

    The low level driver must have finished any outstanding requests first
    via \ :c:func:`blk_cleanup_queue`\ .

    Although \ :c:func:`blk_release_queue`\  may be called with preemption disabled,
    \ :c:func:`__blk_release_queue`\  may sleep.

.. This file was automatic generated / don't edit.

