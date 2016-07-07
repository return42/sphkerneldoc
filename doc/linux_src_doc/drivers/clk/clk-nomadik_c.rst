.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-nomadik.c

.. _`clk_pll`:

struct clk_pll
==============

.. c:type:: struct clk_pll

    Nomadik PLL1 clock

.. _`clk_pll.definition`:

Definition
----------

.. code-block:: c

    struct clk_pll {
        struct clk_hw hw;
        int id;
    }

.. _`clk_pll.members`:

Members
-------

hw
    corresponding clock hardware entry

id
    PLL instance: 1 or 2

.. _`clk_src`:

struct clk_src
==============

.. c:type:: struct clk_src

    Nomadik src clock

.. _`clk_src.definition`:

Definition
----------

.. code-block:: c

    struct clk_src {
        struct clk_hw hw;
        int id;
        bool group1;
        u32 clkbit;
    }

.. _`clk_src.members`:

Members
-------

hw
    corresponding clock hardware entry

id
    the clock ID

group1
    true if the clock is in group1, else it is in group0

clkbit
    bit 0...31 corresponding to the clock in each clock register

.. This file was automatic generated / don't edit.

