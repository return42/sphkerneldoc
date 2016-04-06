.. -*- coding: utf-8; mode: rst -*-

===========
blk-sysfs.c
===========



.. _xref_blk_release_queue:

blk_release_queue
=================

.. c:function:: void blk_release_queue (struct kobject * kobj)

    release a \\\amp;struct request_queue when it is no longer needed

    :param struct kobject * kobj:
        the kobj belonging to the request queue to be released



Description
-----------

    blk_release_queue is the pair to :c:func:`blk_init_queue` or
    :c:func:`blk_queue_make_request`.  It should be called when a request queue is
    being released; typically when a block device is being de-registered.
    Currently, its primary task it to free all the :c:type:`struct request <request>`
    structures that were allocated to the queue and the queue itself.



Note
----

    The low level driver must have finished any outstanding requests first
    via :c:func:`blk_cleanup_queue`.


