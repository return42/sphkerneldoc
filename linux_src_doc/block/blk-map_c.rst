.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-map.c

.. _`blk_rq_map_user_iov`:

blk_rq_map_user_iov
===================

.. c:function:: int blk_rq_map_user_iov(struct request_queue *q, struct request *rq, struct rq_map_data *map_data, const struct iov_iter *iter, gfp_t gfp_mask)

    map user data to a request, for passthrough requests

    :param q:
        request queue where request should be inserted
    :type q: struct request_queue \*

    :param rq:
        request to map data to
    :type rq: struct request \*

    :param map_data:
        pointer to the rq_map_data holding pages (if necessary)
    :type map_data: struct rq_map_data \*

    :param iter:
        iovec iterator
    :type iter: const struct iov_iter \*

    :param gfp_mask:
        memory allocation flags
    :type gfp_mask: gfp_t

.. _`blk_rq_map_user_iov.description`:

Description
-----------

   Data will be mapped directly for zero copy I/O, if possible. Otherwise
   a kernel bounce buffer is used.

   A matching \ :c:func:`blk_rq_unmap_user`\  must be issued at the end of I/O, while
   still in process context.

.. _`blk_rq_map_user_iov.note`:

Note
----

The mapped bio may need to be bounced through \ :c:func:`blk_queue_bounce`\ 
   before being submitted to the device, as pages mapped may be out of
   reach. It's the callers responsibility to make sure this happens. The
   original bio must be passed back in to \ :c:func:`blk_rq_unmap_user`\  for proper
   unmapping.

.. _`blk_rq_unmap_user`:

blk_rq_unmap_user
=================

.. c:function:: int blk_rq_unmap_user(struct bio *bio)

    unmap a request with user data

    :param bio:
        start of bio list
    :type bio: struct bio \*

.. _`blk_rq_unmap_user.description`:

Description
-----------

   Unmap a rq previously mapped by \ :c:func:`blk_rq_map_user`\ . The caller must
   supply the original rq->bio from the \ :c:func:`blk_rq_map_user`\  return, since
   the I/O completion may have changed rq->bio.

.. _`blk_rq_map_kern`:

blk_rq_map_kern
===============

.. c:function:: int blk_rq_map_kern(struct request_queue *q, struct request *rq, void *kbuf, unsigned int len, gfp_t gfp_mask)

    map kernel data to a request, for passthrough requests

    :param q:
        request queue where request should be inserted
    :type q: struct request_queue \*

    :param rq:
        request to fill
    :type rq: struct request \*

    :param kbuf:
        the kernel buffer
    :type kbuf: void \*

    :param len:
        length of user data
    :type len: unsigned int

    :param gfp_mask:
        memory allocation flags
    :type gfp_mask: gfp_t

.. _`blk_rq_map_kern.description`:

Description
-----------

   Data will be mapped directly if possible. Otherwise a bounce
   buffer is used. Can be called multiple times to append multiple
   buffers.

.. This file was automatic generated / don't edit.

