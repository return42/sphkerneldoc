.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/reset/reset-simple.h

.. _`reset_simple_data`:

struct reset_simple_data
========================

.. c:type:: struct reset_simple_data

    driver data for simple reset controllers

.. _`reset_simple_data.definition`:

Definition
----------

.. code-block:: c

    struct reset_simple_data {
        spinlock_t lock;
        void __iomem *membase;
        struct reset_controller_dev rcdev;
        bool active_low;
        bool status_active_low;
    }

.. _`reset_simple_data.members`:

Members
-------

lock
    spinlock to protect registers during read-modify-write cycles

membase
    memory mapped I/O register range

rcdev
    reset controller device base structure

active_low
    if true, bits are cleared to assert the reset. Otherwise, bits
    are set to assert the reset. Note that this says nothing about
    the voltage level of the actual reset line.

status_active_low
    if true, bits read back as cleared while the reset is
    asserted. Otherwise, bits read back as set while the
    reset is asserted.

.. This file was automatic generated / don't edit.

