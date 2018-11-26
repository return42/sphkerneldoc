.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk.h

.. _`rq_ioc`:

rq_ioc
======

.. c:function:: struct io_context *rq_ioc(struct bio *bio)

    determine io_context for request allocation

    :param bio:
        request being allocated is for this bio (can be \ ``NULL``\ )
    :type bio: struct bio \*

.. _`rq_ioc.description`:

Description
-----------

Determine io_context to use for request allocation for \ ``bio``\ .  May return
\ ``NULL``\  if \ ``current-``\ >io_context doesn't exist.

.. _`create_io_context`:

create_io_context
=================

.. c:function:: struct io_context *create_io_context(gfp_t gfp_mask, int node)

    try to create task->io_context

    :param gfp_mask:
        allocation mask
    :type gfp_mask: gfp_t

    :param node:
        allocation node
    :type node: int

.. _`create_io_context.description`:

Description
-----------

If \ ``current-``\ >io_context is \ ``NULL``\ , allocate a new io_context and install
it.  Returns the current \ ``current-``\ >io_context which may be \ ``NULL``\  if
allocation failed.

Note that this function can't be called with IRQ disabled because
task_lock which protects \ ``current-``\ >io_context is IRQ-unsafe.

.. This file was automatic generated / don't edit.

