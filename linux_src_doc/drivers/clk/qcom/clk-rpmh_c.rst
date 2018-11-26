.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/qcom/clk-rpmh.c

.. _`clk_rpmh`:

struct clk_rpmh
===============

.. c:type:: struct clk_rpmh

    individual rpmh clock data structure

.. _`clk_rpmh.definition`:

Definition
----------

.. code-block:: c

    struct clk_rpmh {
        struct clk_hw hw;
        const char *res_name;
        u8 div;
        u32 res_addr;
        u32 res_on_val;
        u32 state;
        u32 aggr_state;
        u32 last_sent_aggr_state;
        u32 valid_state_mask;
        struct device *dev;
        struct clk_rpmh *peer;
    }

.. _`clk_rpmh.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

res_name
    resource name for the rpmh clock

div
    clock divider to compute the clock rate

res_addr
    base address of the rpmh resource within the RPMh

res_on_val
    rpmh clock enable value

state
    rpmh clock requested state

aggr_state
    rpmh clock aggregated state

last_sent_aggr_state
    rpmh clock last aggr state sent to RPMh

valid_state_mask
    mask to determine the state of the rpmh clock

dev
    device to which it is attached

peer
    pointer to the clock rpmh sibling

.. This file was automatic generated / don't edit.

