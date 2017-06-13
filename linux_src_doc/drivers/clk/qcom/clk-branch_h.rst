.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/clk-branch.h

.. _`clk_branch`:

struct clk_branch
=================

.. c:type:: struct clk_branch

    gating clock with status bit and dynamic hardware gating

.. _`clk_branch.definition`:

Definition
----------

.. code-block:: c

    struct clk_branch {
        u32 hwcg_reg;
        u32 halt_reg;
        u8 hwcg_bit;
        u8 halt_bit;
        u8 halt_check;
    #define BRANCH_VOTED BIT(7)
    #define BRANCH_HALT 0
    #define BRANCH_HALT_VOTED (BRANCH_HALT | BRANCH_VOTED)
    #define BRANCH_HALT_ENABLE 1
    #define BRANCH_HALT_ENABLE_VOTED (BRANCH_HALT_ENABLE | BRANCH_VOTED)
    #define BRANCH_HALT_DELAY 2
        struct clk_regmap clkr;
    }

.. _`clk_branch.members`:

Members
-------

hwcg_reg
    dynamic hardware clock gating register

halt_reg
    halt register

hwcg_bit
    ORed with \ ``hwcg_reg``\  to enable dynamic hardware clock gating

halt_bit
    ANDed with \ ``halt_reg``\  to test for clock halted

halt_check
    type of halt checking to perform

clkr
    handle between common and hardware-specific interfaces

.. _`clk_branch.description`:

Description
-----------

Clock which can gate its output.

.. This file was automatic generated / don't edit.

