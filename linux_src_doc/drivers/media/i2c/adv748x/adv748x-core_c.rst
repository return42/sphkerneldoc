.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/adv748x/adv748x-core.c

.. _`adv748x_reg_value`:

struct adv748x_reg_value
========================

.. c:type:: struct adv748x_reg_value

    Register write instruction

.. _`adv748x_reg_value.definition`:

Definition
----------

.. code-block:: c

    struct adv748x_reg_value {
        u8 page;
        u8 reg;
        u8 value;
    }

.. _`adv748x_reg_value.members`:

Members
-------

page
    Regmap page identifier

reg
    I2C register

value
    value to write to \ ``page``\  at \ ``reg``\ 

.. This file was automatic generated / don't edit.

