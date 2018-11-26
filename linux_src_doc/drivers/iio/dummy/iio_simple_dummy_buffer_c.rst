.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dummy/iio_simple_dummy_buffer.c

.. _`iio_simple_dummy_trigger_h`:

iio_simple_dummy_trigger_h
==========================

.. c:function:: irqreturn_t iio_simple_dummy_trigger_h(int irq, void *p)

    the trigger handler function

    :param irq:
        the interrupt number
    :type irq: int

    :param p:
        private data - always a pointer to the poll func.
    :type p: void \*

.. _`iio_simple_dummy_trigger_h.description`:

Description
-----------

This is the guts of buffered capture. On a trigger event occurring,
if the pollfunc is attached then this handler is called as a threaded
interrupt (and hence may sleep). It is responsible for grabbing data
from the device and pushing it into the associated buffer.

.. _`iio_simple_dummy_unconfigure_buffer`:

iio_simple_dummy_unconfigure_buffer
===================================

.. c:function:: void iio_simple_dummy_unconfigure_buffer(struct iio_dev *indio_dev)

    release buffer resources

    :param indio_dev:
        *undescribed*
    :type indio_dev: struct iio_dev \*

.. This file was automatic generated / don't edit.

