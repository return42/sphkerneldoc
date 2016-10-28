.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/iio/ring_hw.h

.. _`iio_hw_buffer`:

struct iio_hw_buffer
====================

.. c:type:: struct iio_hw_buffer

    hardware ring buffer

.. _`iio_hw_buffer.definition`:

Definition
----------

.. code-block:: c

    struct iio_hw_buffer {
        struct iio_buffer buf;
        void *private;
    }

.. _`iio_hw_buffer.members`:

Members
-------

buf
    generic ring buffer elements

private
    device specific data

.. This file was automatic generated / don't edit.

