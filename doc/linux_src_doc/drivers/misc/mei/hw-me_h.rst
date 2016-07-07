.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/hw-me.h

.. _`mei_me_hw`:

struct mei_me_hw
================

.. c:type:: struct mei_me_hw

    me hw specific data

.. _`mei_me_hw.definition`:

Definition
----------

.. code-block:: c

    struct mei_me_hw {
        const struct mei_cfg *cfg;
        void __iomem *mem_addr;
        u32 intr_source;
        enum mei_pg_state pg_state;
        bool d0i3_supported;
    }

.. _`mei_me_hw.members`:

Members
-------

cfg
    per device generation config and ops

mem_addr
    io memory address

intr_source
    interrupt source

pg_state
    power gating state

d0i3_supported
    di03 support

.. This file was automatic generated / don't edit.

