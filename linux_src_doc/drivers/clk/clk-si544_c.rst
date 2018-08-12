.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-si544.c

.. _`clk_si544_muldiv`:

struct clk_si544_muldiv
=======================

.. c:type:: struct clk_si544_muldiv

    Multiplier/divider settings

.. _`clk_si544_muldiv.definition`:

Definition
----------

.. code-block:: c

    struct clk_si544_muldiv {
        u32 fb_div_frac;
        u16 fb_div_int;
        u16 hs_div;
        u8 ls_div_bits;
    }

.. _`clk_si544_muldiv.members`:

Members
-------

fb_div_frac
    integer part of feedback divider (32 bits)

fb_div_int
    fractional part of feedback divider (11 bits)

hs_div
    1st divider, 5..2046, must be even when >33

ls_div_bits
    2nd divider, as 2^x, range 0..5
    If ls_div_bits is non-zero, hs_div must be even

.. This file was automatic generated / don't edit.

