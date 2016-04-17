.. -*- coding: utf-8; mode: rst -*-

============
qdio_setup.c
============


.. _`qdio_free_buffers`:

qdio_free_buffers
=================

.. c:function:: void qdio_free_buffers (struct qdio_buffer **buf, unsigned int count)

    free qdio buffers

    :param struct qdio_buffer \*\*buf:
        array of pointers to qdio buffers

    :param unsigned int count:
        number of qdio buffers to free



.. _`qdio_alloc_buffers`:

qdio_alloc_buffers
==================

.. c:function:: int qdio_alloc_buffers (struct qdio_buffer **buf, unsigned int count)

    allocate qdio buffers

    :param struct qdio_buffer \*\*buf:
        array of pointers to qdio buffers

    :param unsigned int count:
        number of qdio buffers to allocate



.. _`qdio_reset_buffers`:

qdio_reset_buffers
==================

.. c:function:: void qdio_reset_buffers (struct qdio_buffer **buf, unsigned int count)

    reset qdio buffers

    :param struct qdio_buffer \*\*buf:
        array of pointers to qdio buffers

    :param unsigned int count:
        number of qdio buffers that will be zeroed

