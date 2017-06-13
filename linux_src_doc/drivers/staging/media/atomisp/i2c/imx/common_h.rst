.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/atomisp/i2c/imx/common.h

.. _`imx_reg`:

struct imx_reg
==============

.. c:type:: struct imx_reg

    MI sensor  register format

.. _`imx_reg.definition`:

Definition
----------

.. code-block:: c

    struct imx_reg {
        enum imx_tok_type type;
        u16 sreg;
        u32 val;
    }

.. _`imx_reg.members`:

Members
-------

type
    type of the register

sreg
    *undescribed*

val
    8/16/32-bit register value

.. _`imx_reg.description`:

Description
-----------

Define a structure for sensor register initialization values

.. This file was automatic generated / don't edit.

