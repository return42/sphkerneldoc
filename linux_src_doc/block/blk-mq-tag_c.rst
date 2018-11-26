.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq-tag.c

.. _`bt_for_each`:

bt_for_each
===========

.. c:function:: void bt_for_each(struct blk_mq_hw_ctx *hctx, struct sbitmap_queue *bt, busy_iter_fn *fn, void *data, bool reserved)

    iterate over the requests associated with a hardware queue

    :param hctx:
        Hardware queue to examine.
    :type hctx: struct blk_mq_hw_ctx \*

    :param bt:
        sbitmap to examine. This is either the breserved_tags member
        or the bitmap_tags member of struct blk_mq_tags.
    :type bt: struct sbitmap_queue \*

    :param fn:
        Pointer to the function that will be called for each request
        associated with \ ``hctx``\  that has been assigned a driver tag.
        \ ``fn``\  will be called as follows: \ ``fn``\ (@hctx, rq, \ ``data``\ , \ ``reserved``\ )
        where rq is a pointer to a request.
    :type fn: busy_iter_fn \*

    :param data:
        Will be passed as third argument to \ ``fn``\ .
    :type data: void \*

    :param reserved:
        Indicates whether \ ``bt``\  is the breserved_tags member or the
        bitmap_tags member of struct blk_mq_tags.
    :type reserved: bool

.. _`bt_tags_for_each`:

bt_tags_for_each
================

.. c:function:: void bt_tags_for_each(struct blk_mq_tags *tags, struct sbitmap_queue *bt, busy_tag_iter_fn *fn, void *data, bool reserved)

    iterate over the requests in a tag map

    :param tags:
        Tag map to iterate over.
    :type tags: struct blk_mq_tags \*

    :param bt:
        sbitmap to examine. This is either the breserved_tags member
        or the bitmap_tags member of struct blk_mq_tags.
    :type bt: struct sbitmap_queue \*

    :param fn:
        Pointer to the function that will be called for each started
        request. \ ``fn``\  will be called as follows: \ ``fn``\ (rq, \ ``data``\ ,
        \ ``reserved``\ ) where rq is a pointer to a request.
    :type fn: busy_tag_iter_fn \*

    :param data:
        Will be passed as second argument to \ ``fn``\ .
    :type data: void \*

    :param reserved:
        Indicates whether \ ``bt``\  is the breserved_tags member or the
        bitmap_tags member of struct blk_mq_tags.
    :type reserved: bool

.. _`blk_mq_all_tag_busy_iter`:

blk_mq_all_tag_busy_iter
========================

.. c:function:: void blk_mq_all_tag_busy_iter(struct blk_mq_tags *tags, busy_tag_iter_fn *fn, void *priv)

    iterate over all started requests in a tag map

    :param tags:
        Tag map to iterate over.
    :type tags: struct blk_mq_tags \*

    :param fn:
        Pointer to the function that will be called for each started
        request. \ ``fn``\  will be called as follows: \ ``fn``\ (rq, \ ``priv``\ ,
        reserved) where rq is a pointer to a request. 'reserved'
        indicates whether or not \ ``rq``\  is a reserved request.
    :type fn: busy_tag_iter_fn \*

    :param priv:
        Will be passed as second argument to \ ``fn``\ .
    :type priv: void \*

.. _`blk_mq_tagset_busy_iter`:

blk_mq_tagset_busy_iter
=======================

.. c:function:: void blk_mq_tagset_busy_iter(struct blk_mq_tag_set *tagset, busy_tag_iter_fn *fn, void *priv)

    iterate over all started requests in a tag set

    :param tagset:
        Tag set to iterate over.
    :type tagset: struct blk_mq_tag_set \*

    :param fn:
        Pointer to the function that will be called for each started
        request. \ ``fn``\  will be called as follows: \ ``fn``\ (rq, \ ``priv``\ ,
        reserved) where rq is a pointer to a request. 'reserved'
        indicates whether or not \ ``rq``\  is a reserved request.
    :type fn: busy_tag_iter_fn \*

    :param priv:
        Will be passed as second argument to \ ``fn``\ .
    :type priv: void \*

.. _`blk_mq_queue_tag_busy_iter`:

blk_mq_queue_tag_busy_iter
==========================

.. c:function:: void blk_mq_queue_tag_busy_iter(struct request_queue *q, busy_iter_fn *fn, void *priv)

    iterate over all requests with a driver tag

    :param q:
        Request queue to examine.
    :type q: struct request_queue \*

    :param fn:
        Pointer to the function that will be called for each request
        on \ ``q``\ . \ ``fn``\  will be called as follows: \ ``fn``\ (hctx, rq, \ ``priv``\ ,
        reserved) where rq is a pointer to a request and hctx points
        to the hardware queue associated with the request. 'reserved'
        indicates whether or not \ ``rq``\  is a reserved request.
    :type fn: busy_iter_fn \*

    :param priv:
        Will be passed as third argument to \ ``fn``\ .
    :type priv: void \*

.. _`blk_mq_queue_tag_busy_iter.note`:

Note
----

if \ ``q->tag_set``\  is shared with other request queues then \ ``fn``\  will be
called for all requests on all queues that share that tag set and not only
for requests associated with \ ``q``\ .

.. _`blk_mq_unique_tag`:

blk_mq_unique_tag
=================

.. c:function:: u32 blk_mq_unique_tag(struct request *rq)

    return a tag that is unique queue-wide

    :param rq:
        request for which to compute a unique tag
    :type rq: struct request \*

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

.. This file was automatic generated / don't edit.

