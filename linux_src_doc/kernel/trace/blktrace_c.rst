.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/blktrace.c

.. _`blk_trace_ioctl`:

blk_trace_ioctl
===============

.. c:function:: int blk_trace_ioctl(struct block_device *bdev, unsigned cmd, char __user *arg)

    - handle the ioctls associated with tracing

    :param bdev:
        the block device
    :type bdev: struct block_device \*

    :param cmd:
        the ioctl cmd
    :type cmd: unsigned

    :param arg:
        the argument data, if any
    :type arg: char __user \*

.. _`blk_trace_shutdown`:

blk_trace_shutdown
==================

.. c:function:: void blk_trace_shutdown(struct request_queue *q)

    - stop and cleanup trace structures

    :param q:
        the request queue associated with the device
    :type q: struct request_queue \*

.. _`blk_add_trace_rq`:

blk_add_trace_rq
================

.. c:function:: void blk_add_trace_rq(struct request *rq, int error, unsigned int nr_bytes, u32 what, union kernfs_node_id *cgid)

    Add a trace for a request oriented action

    :param rq:
        the source request
    :type rq: struct request \*

    :param error:
        return status to log
    :type error: int

    :param nr_bytes:
        number of completed bytes
    :type nr_bytes: unsigned int

    :param what:
        the action
    :type what: u32

    :param cgid:
        the cgroup info
    :type cgid: union kernfs_node_id \*

.. _`blk_add_trace_rq.description`:

Description
-----------

    Records an action against a request. Will log the bio offset + size.

.. _`blk_add_trace_bio`:

blk_add_trace_bio
=================

.. c:function:: void blk_add_trace_bio(struct request_queue *q, struct bio *bio, u32 what, int error)

    Add a trace for a bio oriented action

    :param q:
        queue the io is for
    :type q: struct request_queue \*

    :param bio:
        the source bio
    :type bio: struct bio \*

    :param what:
        the action
    :type what: u32

    :param error:
        error, if any
    :type error: int

.. _`blk_add_trace_bio.description`:

Description
-----------

    Records an action against a bio. Will log the bio offset + size.

.. _`blk_add_trace_bio_remap`:

blk_add_trace_bio_remap
=======================

.. c:function:: void blk_add_trace_bio_remap(void *ignore, struct request_queue *q, struct bio *bio, dev_t dev, sector_t from)

    Add a trace for a bio-remap operation

    :param ignore:
        trace callback data parameter (not used)
    :type ignore: void \*

    :param q:
        queue the io is for
    :type q: struct request_queue \*

    :param bio:
        the source bio
    :type bio: struct bio \*

    :param dev:
        target device
    :type dev: dev_t

    :param from:
        source sector
    :type from: sector_t

.. _`blk_add_trace_bio_remap.description`:

Description
-----------

    Device mapper or raid target sometimes need to split a bio because
    it spans a stripe (or similar). Add a trace for that action.

.. _`blk_add_trace_rq_remap`:

blk_add_trace_rq_remap
======================

.. c:function:: void blk_add_trace_rq_remap(void *ignore, struct request_queue *q, struct request *rq, dev_t dev, sector_t from)

    Add a trace for a request-remap operation

    :param ignore:
        trace callback data parameter (not used)
    :type ignore: void \*

    :param q:
        queue the io is for
    :type q: struct request_queue \*

    :param rq:
        the source request
    :type rq: struct request \*

    :param dev:
        target device
    :type dev: dev_t

    :param from:
        source sector
    :type from: sector_t

.. _`blk_add_trace_rq_remap.description`:

Description
-----------

    Device mapper remaps request to other devices.
    Add a trace for that action.

.. _`blk_add_driver_data`:

blk_add_driver_data
===================

.. c:function:: void blk_add_driver_data(struct request_queue *q, struct request *rq, void *data, size_t len)

    Add binary message with driver-specific data

    :param q:
        queue the io is for
    :type q: struct request_queue \*

    :param rq:
        io request
    :type rq: struct request \*

    :param data:
        driver-specific data
    :type data: void \*

    :param len:
        length of driver-specific data
    :type len: size_t

.. _`blk_add_driver_data.description`:

Description
-----------

    Some drivers might want to write driver-specific data per request.

.. This file was automatic generated / don't edit.

