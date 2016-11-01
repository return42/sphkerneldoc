.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-si570.c

.. _`clk_si570`:

struct clk_si570
================

.. c:type:: struct clk_si570


.. _`clk_si570.definition`:

Definition
----------

.. code-block:: c

    struct clk_si570 {
        struct clk_hw hw;
        struct regmap *regmap;
        unsigned int div_offset;
        u64 max_freq;
        u64 fxtal;
        unsigned int n1;
        unsigned int hs_div;
        u64 rfreq;
        u64 frequency;
        struct i2c_client *i2c_client;
    }

.. _`clk_si570.members`:

Members
-------

hw
    Clock hw struct

regmap
    Device's regmap

div_offset
    Rgister offset for dividers

max_freq
    Maximum frequency for this device

fxtal
    Factory xtal frequency

n1
    Clock divider N1

hs_div
    Clock divider HSDIV

rfreq
    Clock multiplier RFREQ

frequency
    Current output frequency

i2c_client
    I2C client pointer

.. _`si570_get_divs`:

si570_get_divs
==============

.. c:function:: int si570_get_divs(struct clk_si570 *data, u64 *rfreq, unsigned int *n1, unsigned int *hs_div)

    Read clock dividers from HW

    :param struct clk_si570 \*data:
        Pointer to struct clk_si570

    :param u64 \*rfreq:
        Fractional multiplier (output)

    :param unsigned int \*n1:
        Divider N1 (output)

    :param unsigned int \*hs_div:
        Divider HSDIV (output)
        Returns 0 on success, negative errno otherwise.

.. _`si570_get_divs.description`:

Description
-----------

Retrieve clock dividers and multipliers from the HW.

.. _`si570_get_defaults`:

si570_get_defaults
==================

.. c:function:: int si570_get_defaults(struct clk_si570 *data, u64 fout)

    Get default values

    :param struct clk_si570 \*data:
        Driver data structure

    :param u64 fout:
        Factory frequency output
        Returns 0 on success, negative errno otherwise.

.. _`si570_update_rfreq`:

si570_update_rfreq
==================

.. c:function:: int si570_update_rfreq(struct clk_si570 *data)

    Update clock multiplier

    :param struct clk_si570 \*data:
        Driver data structure
        Passes on \ :c:func:`regmap_bulk_write`\  return value.

.. _`si570_calc_divs`:

si570_calc_divs
===============

.. c:function:: int si570_calc_divs(unsigned long frequency, struct clk_si570 *data, u64 *out_rfreq, unsigned int *out_n1, unsigned int *out_hs_div)

    Caluclate clock dividers

    :param unsigned long frequency:
        Target frequency

    :param struct clk_si570 \*data:
        Driver data structure

    :param u64 \*out_rfreq:
        RFREG fractional multiplier (output)

    :param unsigned int \*out_n1:
        Clock divider N1 (output)

    :param unsigned int \*out_hs_div:
        Clock divider HSDIV (output)
        Returns 0 on success, negative errno otherwise.

.. _`si570_calc_divs.description`:

Description
-----------

Calculate the clock dividers (@out_hs_div, \ ``out_n1``\ ) and clock multiplier
(@out_rfreq) for a given target \ ``frequency``\ .

.. _`si570_set_frequency`:

si570_set_frequency
===================

.. c:function:: int si570_set_frequency(struct clk_si570 *data, unsigned long frequency)

    Adjust output frequency

    :param struct clk_si570 \*data:
        Driver data structure

    :param unsigned long frequency:
        Target frequency
        Returns 0 on success.

.. _`si570_set_frequency.description`:

Description
-----------

Update output frequency for big frequency changes (> 3,500 ppm).

.. _`si570_set_frequency_small`:

si570_set_frequency_small
=========================

.. c:function:: int si570_set_frequency_small(struct clk_si570 *data, unsigned long frequency)

    Adjust output frequency

    :param struct clk_si570 \*data:
        Driver data structure

    :param unsigned long frequency:
        Target frequency
        Returns 0 on success.

.. _`si570_set_frequency_small.description`:

Description
-----------

Update output frequency for small frequency changes (< 3,500 ppm).

.. This file was automatic generated / don't edit.

