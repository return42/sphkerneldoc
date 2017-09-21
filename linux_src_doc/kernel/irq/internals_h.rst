.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/internals.h

.. _`irq_timings`:

struct irq_timings
==================

.. c:type:: struct irq_timings

    irq timings storing structure

.. _`irq_timings.definition`:

Definition
----------

.. code-block:: c

    struct irq_timings {
        u64 values;
        int count;
    }

.. _`irq_timings.members`:

Members
-------

values
    a circular buffer of u64 encoded <timestamp,irq> values

count
    the number of elements in the array

.. This file was automatic generated / don't edit.

