.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fscache/operation.c

.. _`fscache_operation_init`:

fscache_operation_init
======================

.. c:function:: void fscache_operation_init(struct fscache_cookie *cookie, struct fscache_operation *op, fscache_operation_processor_t processor, fscache_operation_cancel_t cancel, fscache_operation_release_t release)

    Do basic initialisation of an operation

    :param cookie:
        *undescribed*
    :type cookie: struct fscache_cookie \*

    :param op:
        The operation to initialise
    :type op: struct fscache_operation \*

    :param processor:
        *undescribed*
    :type processor: fscache_operation_processor_t

    :param cancel:
        *undescribed*
    :type cancel: fscache_operation_cancel_t

    :param release:
        The release function to assign
    :type release: fscache_operation_release_t

.. _`fscache_operation_init.description`:

Description
-----------

Do basic initialisation of an operation.  The caller must still set flags,
object and processor if needed.

.. _`fscache_enqueue_operation`:

fscache_enqueue_operation
=========================

.. c:function:: void fscache_enqueue_operation(struct fscache_operation *op)

    Enqueue an operation for processing

    :param op:
        The operation to enqueue
    :type op: struct fscache_operation \*

.. _`fscache_enqueue_operation.description`:

Description
-----------

Enqueue an operation for processing by the FS-Cache thread pool.

This will get its own ref on the object.

.. This file was automatic generated / don't edit.

