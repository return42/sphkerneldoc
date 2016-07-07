.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-ioc.c

.. _`get_io_context`:

get_io_context
==============

.. c:function:: void get_io_context(struct io_context *ioc)

    increment reference count to io_context

    :param struct io_context \*ioc:
        io_context to get

.. _`get_io_context.description`:

Description
-----------

Increment reference count to \ ``ioc``\ .

.. _`put_io_context`:

put_io_context
==============

.. c:function:: void put_io_context(struct io_context *ioc)

    put a reference of io_context

    :param struct io_context \*ioc:
        io_context to put

.. _`put_io_context.description`:

Description
-----------

Decrement reference count of \ ``ioc``\  and release it if the count reaches
zero.

.. _`put_io_context_active`:

put_io_context_active
=====================

.. c:function:: void put_io_context_active(struct io_context *ioc)

    put active reference on ioc

    :param struct io_context \*ioc:
        ioc of interest

.. _`put_io_context_active.description`:

Description
-----------

Undo \ :c:func:`get_io_context_active`\ .  If active reference reaches zero after
put, \ ``ioc``\  can never issue further IOs and ioscheds are notified.

.. _`ioc_clear_queue`:

ioc_clear_queue
===============

.. c:function:: void ioc_clear_queue(struct request_queue *q)

    break any ioc association with the specified queue

    :param struct request_queue \*q:
        request_queue being cleared

.. _`ioc_clear_queue.description`:

Description
-----------

Walk \ ``q``\ ->icq_list and exit all io_cq's.  Must be called with \ ``q``\  locked.

.. _`get_task_io_context`:

get_task_io_context
===================

.. c:function:: struct io_context *get_task_io_context(struct task_struct *task, gfp_t gfp_flags, int node)

    get io_context of a task

    :param struct task_struct \*task:
        task of interest

    :param gfp_t gfp_flags:
        allocation flags, used if allocation is necessary

    :param int node:
        allocation node, used if allocation is necessary

.. _`get_task_io_context.description`:

Description
-----------

Return io_context of \ ``task``\ .  If it doesn't exist, it is created with
\ ``gfp_flags``\  and \ ``node``\ .  The returned io_context has its reference count
incremented.

This function always goes through \ :c:func:`task_lock`\  and it's better to use
\ ``current-``\ >io_context + \ :c:func:`get_io_context`\  for \ ``current``\ .

.. _`ioc_lookup_icq`:

ioc_lookup_icq
==============

.. c:function:: struct io_cq *ioc_lookup_icq(struct io_context *ioc, struct request_queue *q)

    lookup io_cq from ioc

    :param struct io_context \*ioc:
        the associated io_context

    :param struct request_queue \*q:
        the associated request_queue

.. _`ioc_lookup_icq.description`:

Description
-----------

Look up io_cq associated with \ ``ioc``\  - \ ``q``\  pair from \ ``ioc``\ .  Must be called
with \ ``q``\ ->queue_lock held.

.. _`ioc_create_icq`:

ioc_create_icq
==============

.. c:function:: struct io_cq *ioc_create_icq(struct io_context *ioc, struct request_queue *q, gfp_t gfp_mask)

    create and link io_cq

    :param struct io_context \*ioc:
        io_context of interest

    :param struct request_queue \*q:
        request_queue of interest

    :param gfp_t gfp_mask:
        allocation mask

.. _`ioc_create_icq.description`:

Description
-----------

Make sure io_cq linking \ ``ioc``\  and \ ``q``\  exists.  If icq doesn't exist, they
will be created using \ ``gfp_mask``\ .

The caller is responsible for ensuring \ ``ioc``\  won't go away and \ ``q``\  is
alive and will stay alive until this function returns.

.. This file was automatic generated / don't edit.

