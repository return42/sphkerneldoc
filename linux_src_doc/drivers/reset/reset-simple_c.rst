.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/reset/reset-simple.c

.. _`reset_simple_devdata`:

struct reset_simple_devdata
===========================

.. c:type:: struct reset_simple_devdata

    simple reset controller properties

.. _`reset_simple_devdata.definition`:

Definition
----------

.. code-block:: c

    struct reset_simple_devdata {
        u32 reg_offset;
        u32 nr_resets;
        bool active_low;
        bool status_active_low;
    }

.. _`reset_simple_devdata.members`:

Members
-------

reg_offset
    offset between base address and first reset register.

nr_resets
    number of resets. If not set, default to resource size in bits.

active_low
    if true, bits are cleared to assert the reset. Otherwise, bits
    are set to assert the reset.

status_active_low
    if true, bits read back as cleared while the reset is
    asserted. Otherwise, bits read back as set while the
    reset is asserted.

.. This file was automatic generated / don't edit.

