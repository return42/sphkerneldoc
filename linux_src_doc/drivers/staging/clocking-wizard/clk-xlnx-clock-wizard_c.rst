.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/clocking-wizard/clk-xlnx-clock-wizard.c

.. _`clk_wzrd`:

struct clk_wzrd
===============

.. c:type:: struct clk_wzrd


.. _`clk_wzrd.definition`:

Definition
----------

.. code-block:: c

    struct clk_wzrd {
        struct clk_onecell_data clk_data;
        struct notifier_block nb;
        void __iomem *base;
        struct clk *clk_in1;
        struct clk *axi_clk;
        struct clk *clks_internal[wzrd_clk_int_max];
        struct clk *clkout[WZRD_NUM_OUTPUTS];
        unsigned int speed_grade;
        bool suspended;
    }

.. _`clk_wzrd.members`:

Members
-------

clk_data
    Clock data

nb
    Notifier block

base
    Memory base

clk_in1
    Handle to input clock 'clk_in1'

axi_clk
    Handle to input clock 's_axi_aclk'

clks_internal
    Internal clocks

clkout
    Output clocks

speed_grade
    Speed grade of the device

suspended
    Flag indicating power state of the device

.. This file was automatic generated / don't edit.

