.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-tag.c

.. _`blk_queue_find_tag`:

blk_queue_find_tag
==================

.. c:function:: struct request *blk_queue_find_tag(struct request_queue *q, int tag)

    find a request by its tag and queue

    :param q:
        The request queue for the device
    :type q: struct request_queue \*

    :param tag:
        The tag of the request
    :type tag: int

.. _`blk_queue_find_tag.notes`:

Notes
-----

   Should be used when a device returns a tag and you want to match
   it with a request.

   no locks need be held.

.. _`blk_free_tags`:

blk_free_tags
=============

.. c:function:: void blk_free_tags(struct blk_queue_tag *bqt)

    release a given set of tag maintenance info

    :param bqt:
        the tag map to free
    :type bqt: struct blk_queue_tag \*

.. _`blk_free_tags.description`:

Description
-----------

Drop the reference count on \ ``bqt``\  and frees it when the last reference
is dropped.

.. _`__blk_queue_free_tags`:

__blk_queue_free_tags
=====================

.. c:function:: void __blk_queue_free_tags(struct request_queue *q)

    release tag maintenance info

    :param q:
        the request queue for the device
    :type q: struct request_queue \*

.. _`__blk_queue_free_tags.notes`:

Notes
-----

   \ :c:func:`blk_cleanup_queue`\  will take care of calling this function, if tagging
   has been used. So there's no need to call this directly.

.. _`blk_queue_free_tags`:

blk_queue_free_tags
===================

.. c:function:: void blk_queue_free_tags(struct request_queue *q)

    release tag maintenance info

    :param q:
        the request queue for the device
    :type q: struct request_queue \*

.. _`blk_queue_free_tags.notes`:

Notes
-----

     This is used to disable tagged queuing to a device, yet leave
     queue in function.

.. _`blk_init_tags`:

blk_init_tags
=============

.. c:function:: struct blk_queue_tag *blk_init_tags(int depth, int alloc_policy)

    initialize the tag info for an external tag map

    :param depth:
        the maximum queue depth supported
    :type depth: int

    :param alloc_policy:
        tag allocation policy
    :type alloc_policy: int

.. _`blk_queue_init_tags`:

blk_queue_init_tags
===================

.. c:function:: int blk_queue_init_tags(struct request_queue *q, int depth, struct blk_queue_tag *tags, int alloc_policy)

    initialize the queue tag info

    :param q:
        the request queue for the device
    :type q: struct request_queue \*

    :param depth:
        the maximum queue depth supported
    :type depth: int

    :param tags:
        the tag to use
    :type tags: struct blk_queue_tag \*

    :param alloc_policy:
        tag allocation policy
    :type alloc_policy: int

.. _`blk_queue_init_tags.description`:

Description
-----------

Queue lock must be held here if the function is called to resize an
existing map.

.. _`blk_queue_resize_tags`:

blk_queue_resize_tags
=====================

.. c:function:: int blk_queue_resize_tags(struct request_queue *q, int new_depth)

    change the queueing depth

    :param q:
        the request queue for the device
    :type q: struct request_queue \*

    :param new_depth:
        the new max command queueing depth
    :type new_depth: int

.. _`blk_queue_resize_tags.notes`:

Notes
-----

   Must be called with the queue lock held.

.. _`blk_queue_end_tag`:

blk_queue_end_tag
=================

.. c:function:: void blk_queue_end_tag(struct request_queue *q, struct request *rq)

    end tag operations for a request

    :param q:
        the request queue for the device
    :type q: struct request_queue \*

    :param rq:
        the request that has completed
    :type rq: struct request \*

.. _`blk_queue_end_tag.description`:

Description
-----------

   Typically called when \ :c:func:`end_that_request_first`\  returns \ ``0``\ , meaning
   all transfers have been done for a request. It's important to call
   this function before \ :c:func:`end_that_request_last`\ , as that will put the
   request back on the free list thus corrupting the internal tag list.

.. _`blk_queue_start_tag`:

blk_queue_start_tag
===================

.. c:function:: int blk_queue_start_tag(struct request_queue *q, struct request *rq)

    find a free tag and assign it

    :param q:
        the request queue for the device
    :type q: struct request_queue \*

    :param rq:
        the block request that needs tagging
    :type rq: struct request \*

.. _`blk_queue_start_tag.description`:

Description
-----------

   This can either be used as a stand-alone helper, or possibly be
   assigned as the queue \ :c:type:`struct prep_rq_fn <prep_rq_fn>`\  (in which case \ :c:type:`struct request <request>`\ 
   automagically gets a tag assigned). Note that this function
   assumes that any type of request can be queued! if this is not
   true for your device, you must check the request type before
   calling this function.  The request will also be removed from
   the request queue, so it's the drivers responsibility to readd
   it if it should need to be restarted for some reason.

.. This file was automatic generated / don't edit.

