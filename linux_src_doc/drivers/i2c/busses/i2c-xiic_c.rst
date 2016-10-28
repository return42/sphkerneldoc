.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-xiic.c

.. _`xiic_i2c`:

struct xiic_i2c
===============

.. c:type:: struct xiic_i2c

    Internal representation of the XIIC I2C bus

.. _`xiic_i2c.definition`:

Definition
----------

.. code-block:: c

    struct xiic_i2c {
        struct device *dev;
        void __iomem *base;
        wait_queue_head_t wait;
        struct i2c_adapter adap;
        struct i2c_msg *tx_msg;
        struct mutex lock;
        unsigned int tx_pos;
        unsigned int nmsgs;
        enum xilinx_i2c_state state;
        struct i2c_msg *rx_msg;
        int rx_pos;
        enum xiic_endian endianness;
        struct clk *clk;
    }

.. _`xiic_i2c.members`:

Members
-------

dev
    *undescribed*

base
    Memory base of the HW registers

wait
    Wait queue for callers

adap
    Kernel adapter representation

tx_msg
    Messages from above to be sent

lock
    Mutual exclusion

tx_pos
    Current pos in TX message

nmsgs
    Number of messages in tx_msg

state
    See STATE_

rx_msg
    Current RX message

rx_pos
    Position within current RX message

endianness
    big/little-endian byte order

clk
    *undescribed*

.. This file was automatic generated / don't edit.

