.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/at91/clk-generated.c

.. _`clk_generated_startup`:

clk_generated_startup
=====================

.. c:function:: void clk_generated_startup(struct clk_generated *gck)

    Initialize a given clock to its default parent and divisor parameter.

    :param struct clk_generated \*gck:
        Generated clock to set the startup parameters for.

.. _`clk_generated_startup.description`:

Description
-----------

Take parameters from the hardware and update local clock configuration
accordingly.

.. This file was automatic generated / don't edit.

