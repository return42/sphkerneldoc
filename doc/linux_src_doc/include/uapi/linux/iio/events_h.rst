.. -*- coding: utf-8; mode: rst -*-

========
events.h
========


.. _`iio_event_data`:

struct iio_event_data
=====================

.. c:type:: iio_event_data

    The actual event being pushed to userspace


.. _`iio_event_data.definition`:

Definition
----------

.. code-block:: c

  struct iio_event_data {
    __u64 id;
    __s64 timestamp;
  };


.. _`iio_event_data.members`:

Members
-------

:``id``:
    event identifier

:``timestamp``:
    best estimate of time of event occurrence (often from
    the interrupt handler)


