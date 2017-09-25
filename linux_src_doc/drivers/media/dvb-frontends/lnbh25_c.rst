.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/dvb-frontends/lnbh25.c

.. _`lnbh25_priv`:

struct lnbh25_priv
==================

.. c:type:: struct lnbh25_priv

    LNBH25 driver private data

.. _`lnbh25_priv.definition`:

Definition
----------

.. code-block:: c

    struct lnbh25_priv {
        struct i2c_adapter *i2c;
        u8 i2c_address;
        u8 config[3];
    }

.. _`lnbh25_priv.members`:

Members
-------

i2c
    pointer to the I2C adapter structure

i2c_address
    I2C address of LNBH25 SEC chip

config
    Registers configuration:
    offset 0: 1st register address, always 0x02 (DATA1)
    offset 1: DATA1 register value
    offset 2: DATA2 register value

.. This file was automatic generated / don't edit.

