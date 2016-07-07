.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-si5351.h

.. _`si5351_variant`:

enum si5351_variant
===================

.. c:type:: enum si5351_variant

    SiLabs Si5351 chip variant

.. _`si5351_variant.definition`:

Definition
----------

.. code-block:: c

    enum si5351_variant {
        SI5351_VARIANT_A,
        SI5351_VARIANT_A3,
        SI5351_VARIANT_B,
        SI5351_VARIANT_C
    };

.. _`si5351_variant.constants`:

Constants
---------

SI5351_VARIANT_A
    Si5351A (8 output clocks, XTAL input)

SI5351_VARIANT_A3
    Si5351A MSOP10 (3 output clocks, XTAL input)

SI5351_VARIANT_B
    Si5351B (8 output clocks, XTAL/VXCO input)

SI5351_VARIANT_C
    Si5351C (8 output clocks, XTAL/CLKIN input)

.. This file was automatic generated / don't edit.

