.. -*- coding: utf-8; mode: rst -*-

============
blk-mq-tag.c
============


.. _`blk_mq_unique_tag`:

blk_mq_unique_tag
=================

.. c:function:: u32 blk_mq_unique_tag (struct request *rq)

    return a tag that is unique queue-wide

    :param struct request \*rq:
        request for which to compute a unique tag



.. _`blk_mq_unique_tag.description`:

Description
-----------

The tag field in struct request is unique per hardware queue but not over
all hardware queues. Hence this function that returns a tag with the
hardware context index in the upper bits and the per hardware queue tag in
the lower bits.



.. _`blk_mq_unique_tag.note`:

Note
----

When called for a request that is queued on a non-multiqueue request
queue, the hardware context index is set to zero.

