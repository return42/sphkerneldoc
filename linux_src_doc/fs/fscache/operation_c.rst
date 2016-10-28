.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fscache/operation.c

.. _`fscache_operation_init`:

fscache_operation_init
======================

.. c:function:: void fscache_operation_init(struct fscache_operation *op, fscache_operation_processor_t processor, fscache_operation_cancel_t cancel, fscache_operation_release_t release)

    Do basic initialisation of an operation

    :param struct fscache_operation \*op:
        The operation to initialise

    :param fscache_operation_processor_t processor:
        *undescribed*

    :param fscache_operation_cancel_t cancel:
        *undescribed*

    :param fscache_operation_release_t release:
        The release function to assign

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

    :param struct fscache_operation \*op:
        The operation to enqueue

.. _`fscache_enqueue_operation.description`:

Description
-----------

Enqueue an operation for processing by the FS-Cache thread pool.

This will get its own ref on the object.

.. This file was automatic generated / don't edit.

