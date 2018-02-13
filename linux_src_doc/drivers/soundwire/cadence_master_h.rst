.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soundwire/cadence_master.h

.. _`sdw_cdns`:

struct sdw_cdns
===============

.. c:type:: struct sdw_cdns

    Cadence driver context

.. _`sdw_cdns.definition`:

Definition
----------

.. code-block:: c

    struct sdw_cdns {
        struct device *dev;
        struct sdw_bus bus;
        unsigned int instance;
        u32 response_buf[0x80];
        struct completion tx_complete;
        struct sdw_defer *defer;
        void __iomem *registers;
        bool link_up;
        unsigned int msg_count;
    }

.. _`sdw_cdns.members`:

Members
-------

dev
    Linux device

bus
    Bus handle

instance
    instance number

response_buf
    SoundWire response buffer

tx_complete
    Tx completion

defer
    Defer pointer

registers
    Cadence registers

link_up
    Link status

msg_count
    Messages sent on bus

.. This file was automatic generated / don't edit.

