.. -*- coding: utf-8; mode: rst -*-

==========
blktrace.c
==========

.. _`blk_trace_ioctl`:

blk_trace_ioctl
===============

.. c:function:: int blk_trace_ioctl (struct block_device *bdev, unsigned cmd, char __user *arg)

    handle the ioctls associated with tracing

    :param struct block_device \*bdev:
        the block device

    :param unsigned cmd:
        the ioctl cmd

    :param char __user \*arg:
        the argument data, if any


.. _`blk_trace_shutdown`:

blk_trace_shutdown
==================

.. c:function:: void blk_trace_shutdown (struct request_queue *q)

    stop and cleanup trace structures

    :param struct request_queue \*q:
        the request queue associated with the device


.. _`blk_add_trace_rq`:

blk_add_trace_rq
================

.. c:function:: void blk_add_trace_rq (struct request_queue *q, struct request *rq, unsigned int nr_bytes, u32 what)

    Add a trace for a request oriented action

    :param struct request_queue \*q:
        queue the io is for

    :param struct request \*rq:
        the source request

    :param unsigned int nr_bytes:
        number of completed bytes

    :param u32 what:
        the action


.. _`blk_add_trace_rq.description`:

Description
-----------

Description::

    Records an action against a request. Will log the bio offset + size.


.. _`blk_add_trace_bio`:

blk_add_trace_bio
=================

.. c:function:: void blk_add_trace_bio (struct request_queue *q, struct bio *bio, u32 what, int error)

    Add a trace for a bio oriented action

    :param struct request_queue \*q:
        queue the io is for

    :param struct bio \*bio:
        the source bio

    :param u32 what:
        the action

    :param int error:
        error, if any


.. _`blk_add_trace_bio.description`:

Description
-----------

Description::

    Records an action against a bio. Will log the bio offset + size.


.. _`blk_add_trace_bio_remap`:

blk_add_trace_bio_remap
=======================

.. c:function:: void blk_add_trace_bio_remap (void *ignore, struct request_queue *q, struct bio *bio, dev_t dev, sector_t from)

    Add a trace for a bio-remap operation

    :param void \*ignore:
        trace callback data parameter (not used)

    :param struct request_queue \*q:
        queue the io is for

    :param struct bio \*bio:
        the source bio

    :param dev_t dev:
        target device

    :param sector_t from:
        source sector


.. _`blk_add_trace_bio_remap.description`:

Description
-----------

Description::

    Device mapper or raid target sometimes need to split a bio because
    it spans a stripe (or similar). Add a trace for that action.


.. _`blk_add_trace_rq_remap`:

blk_add_trace_rq_remap
======================

.. c:function:: void blk_add_trace_rq_remap (void *ignore, struct request_queue *q, struct request *rq, dev_t dev, sector_t from)

    Add a trace for a request-remap operation

    :param void \*ignore:
        trace callback data parameter (not used)

    :param struct request_queue \*q:
        queue the io is for

    :param struct request \*rq:
        the source request

    :param dev_t dev:
        target device

    :param sector_t from:
        source sector


.. _`blk_add_trace_rq_remap.description`:

Description
-----------

Description::

    Device mapper remaps request to other devices.
    Add a trace for that action.


.. _`blk_add_driver_data`:

blk_add_driver_data
===================

.. c:function:: void blk_add_driver_data (struct request_queue *q, struct request *rq, void *data, size_t len)

    Add binary message with driver-specific data

    :param struct request_queue \*q:
        queue the io is for

    :param struct request \*rq:
        io request

    :param void \*data:
        driver-specific data

    :param size_t len:
        length of driver-specific data


.. _`blk_add_driver_data.description`:

Description
-----------

Description::

    Some drivers might want to write driver-specific data per request.

