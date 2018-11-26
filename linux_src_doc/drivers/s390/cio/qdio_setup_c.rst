.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/qdio_setup.c

.. _`qdio_free_buffers`:

qdio_free_buffers
=================

.. c:function:: void qdio_free_buffers(struct qdio_buffer **buf, unsigned int count)

    free qdio buffers

    :param buf:
        array of pointers to qdio buffers
    :type buf: struct qdio_buffer \*\*

    :param count:
        number of qdio buffers to free
    :type count: unsigned int

.. _`qdio_alloc_buffers`:

qdio_alloc_buffers
==================

.. c:function:: int qdio_alloc_buffers(struct qdio_buffer **buf, unsigned int count)

    allocate qdio buffers

    :param buf:
        array of pointers to qdio buffers
    :type buf: struct qdio_buffer \*\*

    :param count:
        number of qdio buffers to allocate
    :type count: unsigned int

.. _`qdio_reset_buffers`:

qdio_reset_buffers
==================

.. c:function:: void qdio_reset_buffers(struct qdio_buffer **buf, unsigned int count)

    reset qdio buffers

    :param buf:
        array of pointers to qdio buffers
    :type buf: struct qdio_buffer \*\*

    :param count:
        number of qdio buffers that will be zeroed
    :type count: unsigned int

.. This file was automatic generated / don't edit.

