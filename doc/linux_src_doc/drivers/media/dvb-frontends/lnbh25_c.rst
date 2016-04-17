.. -*- coding: utf-8; mode: rst -*-

========
lnbh25.c
========


.. _`lnbh25_priv`:

struct lnbh25_priv
==================

.. c:type:: lnbh25_priv

    LNBH25 driver private data


.. _`lnbh25_priv.definition`:

Definition
----------

.. code-block:: c

  struct lnbh25_priv {
    struct i2c_adapter * i2c;
    u8 i2c_address;
    u8 config[3];
  };


.. _`lnbh25_priv.members`:

Members
-------

:``i2c``:
    pointer to the I2C adapter structure

:``i2c_address``:
    I2C address of LNBH25 SEC chip

:``config[3]``:
    Registers configuration:




.. _`lnbh25_priv.offset-0`:

offset 0
--------

1st register address, always 0x02 (DATA1)



.. _`lnbh25_priv.offset-1`:

offset 1
--------

DATA1 register value



.. _`lnbh25_priv.offset-2`:

offset 2
--------

DATA2 register value

