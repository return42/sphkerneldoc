.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/lnbh29.c

.. _`lnbh29_priv`:

struct lnbh29_priv
==================

.. c:type:: struct lnbh29_priv

    LNBH29 driver private data

.. _`lnbh29_priv.definition`:

Definition
----------

.. code-block:: c

    struct lnbh29_priv {
        struct i2c_adapter *i2c;
        u8 i2c_address;
        u8 config[2];
    }

.. _`lnbh29_priv.members`:

Members
-------

i2c
    Pointer to the I2C adapter structure

i2c_address
    I2C address of LNBH29 chip

config
    Registers configuration
    offset 0: 1st register address, always 0x01 (DATA)
    offset 1: DATA register value

.. This file was automatic generated / don't edit.

