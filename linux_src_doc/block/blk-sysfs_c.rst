.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-sysfs.c

.. _`__blk_release_queue`:

__blk_release_queue
===================

.. c:function:: void __blk_release_queue(struct work_struct *work)

    release a request queue when it is no longer needed

    :param work:
        pointer to the release_work member of the request queue to be released
    :type work: struct work_struct \*

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

.. _`blk_register_queue`:

blk_register_queue
==================

.. c:function:: int blk_register_queue(struct gendisk *disk)

    register a block layer queue with sysfs

    :param disk:
        Disk of which the request queue should be registered with sysfs.
    :type disk: struct gendisk \*

.. _`blk_unregister_queue`:

blk_unregister_queue
====================

.. c:function:: void blk_unregister_queue(struct gendisk *disk)

    counterpart of \ :c:func:`blk_register_queue`\ 

    :param disk:
        Disk of which the request queue should be unregistered from sysfs.
    :type disk: struct gendisk \*

.. _`blk_unregister_queue.note`:

Note
----

the caller is responsible for guaranteeing that this function is called
after \ :c:func:`blk_register_queue`\  has finished.

.. This file was automatic generated / don't edit.

