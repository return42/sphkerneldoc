.. -*- coding: utf-8; mode: rst -*-

========
lnbh25.c
========



.. _xref_struct_lnbh25_priv:

struct lnbh25_priv
==================

.. c:type:: struct lnbh25_priv

    LNBH25 driver private data



Definition
----------

.. code-block:: c

  struct lnbh25_priv {
    struct i2c_adapter * i2c;
    u8 i2c_address;
    u8 config[3];
  };



Members
-------

:``struct i2c_adapter * i2c``:
    pointer to the I2C adapter structure

:``u8 i2c_address``:
    I2C address of LNBH25 SEC chip

:``u8 config[3]``:
    Registers configuration:




offset 0
--------

1st register address, always 0x02 (DATA1)



offset 1
--------

DATA1 register value



offset 2
--------

DATA2 register value


