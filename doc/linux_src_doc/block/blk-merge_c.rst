.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-merge.c

.. _`blk_rq_set_mixed_merge`:

blk_rq_set_mixed_merge
======================

.. c:function:: void blk_rq_set_mixed_merge(struct request *rq)

    mark a request as mixed merge

    :param struct request \*rq:
        request to mark as mixed merge

.. _`blk_rq_set_mixed_merge.description`:

Description
-----------

\ ``rq``\  is about to be mixed merged.  Make sure the attributes
which can be mixed are set in each bio and mark \ ``rq``\  as mixed
merged.

.. This file was automatic generated / don't edit.

