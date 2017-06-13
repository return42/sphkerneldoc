.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/dummy/iio_dummy_evgen.c

.. _`iio_eventgen_no`:

IIO_EVENTGEN_NO
===============

.. c:function::  IIO_EVENTGEN_NO()

.. _`iio_eventgen_no.description`:

Description
-----------

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License version 2 as published by
the Free Software Foundation.

Companion module to the iio simple dummy example driver.
The purpose of this is to generate 'fake' event interrupts thus
allowing that driver's code to be as close as possible to that of
a normal driver talking to hardware.  The approach used here
is not intended to be general and just happens to work for this
particular use case.

.. _`iio_dummy_handle_irq`:

struct iio_dummy_handle_irq
===========================

.. c:type:: struct iio_dummy_handle_irq

    helper struct to simulate interrupt generation

.. _`iio_dummy_handle_irq.definition`:

Definition
----------

.. code-block:: c

    struct iio_dummy_handle_irq {
        struct irq_work work;
        int irq;
    }

.. _`iio_dummy_handle_irq.members`:

Members
-------

work
    irq_work used to run handlers from hardirq context

irq
    fake irq line number to trigger an interrupt

.. _`iio_dummy_eventgen`:

struct iio_dummy_eventgen
=========================

.. c:type:: struct iio_dummy_eventgen

    evgen state

.. _`iio_dummy_eventgen.definition`:

Definition
----------

.. code-block:: c

    struct iio_dummy_eventgen {
        struct irq_chip chip;
        int base;
        bool enabled;
        bool inuse;
        struct iio_dummy_regs regs;
        struct mutex lock;
        struct iio_dummy_handle_irq handler;
    }

.. _`iio_dummy_eventgen.members`:

Members
-------

chip
    irq chip we are faking

base
    base of irq range

enabled
    mask of which irqs are enabled

inuse
    mask of which irqs are connected

regs
    irq regs we are faking

lock
    protect the evgen state

handler
    helper for a 'hardware-like' interrupt simulation

.. _`iio_dummy_evgen_get_irq`:

iio_dummy_evgen_get_irq
=======================

.. c:function:: int iio_dummy_evgen_get_irq( void)

    get an evgen provided irq for a device

    :param  void:
        no arguments

.. _`iio_dummy_evgen_get_irq.description`:

Description
-----------

This function will give a free allocated irq to a client device.
That irq can then be caused to 'fire' by using the associated sysfs file.

.. _`iio_dummy_evgen_release_irq`:

iio_dummy_evgen_release_irq
===========================

.. c:function:: void iio_dummy_evgen_release_irq(int irq)

    give the irq back.

    :param int irq:
        irq being returned to the pool

.. _`iio_dummy_evgen_release_irq.description`:

Description
-----------

Used by client driver instances to give the irqs back when they disconnect

.. This file was automatic generated / don't edit.

