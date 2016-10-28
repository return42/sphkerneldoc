.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/tvp514x_regs.h

.. _`tvp514x_reg`:

struct tvp514x_reg
==================

.. c:type:: struct tvp514x_reg

    Structure for TVP5146/47 register initialization values

.. _`tvp514x_reg.definition`:

Definition
----------

.. code-block:: c

    struct tvp514x_reg {
        u8 token;
        u8 reg;
        u32 val;
    }

.. _`tvp514x_reg.members`:

Members
-------

token
    TOK_WRITE, TOK_TERM etc..
    \ ``reg``\  - Register offset
    \ ``val``\  - Register Value for TOK_WRITE or delay in ms for TOK_DELAY

reg
    *undescribed*

val
    *undescribed*

.. This file was automatic generated / don't edit.

