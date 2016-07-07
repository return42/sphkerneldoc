.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/trigger_consumer.h

.. _`iio_poll_func`:

struct iio_poll_func
====================

.. c:type:: struct iio_poll_func

    poll function pair

.. _`iio_poll_func.definition`:

Definition
----------

.. code-block:: c

    struct iio_poll_func {
        struct iio_dev *indio_dev;
        irqreturn_t (* h) (int irq, void *p);
        irqreturn_t (* thread) (int irq, void *p);
        int type;
        char *name;
        int irq;
        s64 timestamp;
    }

.. _`iio_poll_func.members`:

Members
-------

indio_dev
    data specific to device (passed into poll func)

h
    the function that is actually run on trigger

thread
    threaded interrupt part

type
    the type of interrupt (basically if oneshot)

name
    name used to identify the trigger consumer.

irq
    the corresponding irq as allocated from the
    trigger pool

timestamp
    some devices need a timestamp grabbed as soon
    as possible after the trigger - hence handler
    passes it via here.

.. This file was automatic generated / don't edit.

