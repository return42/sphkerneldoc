.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk.h

.. _`create_io_context`:

create_io_context
=================

.. c:function:: struct io_context *create_io_context(gfp_t gfp_mask, int node)

    try to create task->io_context

    :param gfp_t gfp_mask:
        allocation mask

    :param int node:
        allocation node

.. _`create_io_context.description`:

Description
-----------

If \ ``current-``\ >io_context is \ ``NULL``\ , allocate a new io_context and install
it.  Returns the current \ ``current-``\ >io_context which may be \ ``NULL``\  if
allocation failed.

Note that this function can't be called with IRQ disabled because
task_lock which protects \ ``current-``\ >io_context is IRQ-unsafe.

.. This file was automatic generated / don't edit.

