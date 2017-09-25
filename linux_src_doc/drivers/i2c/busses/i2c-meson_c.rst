.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/i2c/busses/i2c-meson.c

.. _`meson_i2c`:

struct meson_i2c
================

.. c:type:: struct meson_i2c

    Meson I2C device private data

.. _`meson_i2c.definition`:

Definition
----------

.. code-block:: c

    struct meson_i2c {
        struct i2c_adapter adap;
        struct device *dev;
        void __iomem *regs;
        struct clk *clk;
        struct i2c_msg *msg;
        int state;
        bool last;
        int count;
        int pos;
        int error;
        spinlock_t lock;
        struct completion done;
        u32 tokens[2];
        int num_tokens;
    }

.. _`meson_i2c.members`:

Members
-------

adap
    I2C adapter instance

dev
    Pointer to device structure

regs
    Base address of the device memory mapped registers

clk
    Pointer to clock structure

msg
    Pointer to the current I2C message

state
    Current state in the driver state machine

last
    Flag set for the last message in the transfer

count
    Number of bytes to be sent/received in current transfer

pos
    Current position in the send/receive buffer

error
    Flag set when an error is received

lock
    To avoid race conditions between irq handler and xfer code

done
    Completion used to wait for transfer termination

tokens
    Sequence of tokens to be written to the device

num_tokens
    Number of tokens

.. This file was automatic generated / don't edit.

