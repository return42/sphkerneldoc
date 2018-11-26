.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/zynqmp/pll.c

.. _`zynqmp_pll`:

struct zynqmp_pll
=================

.. c:type:: struct zynqmp_pll

    PLL clock

.. _`zynqmp_pll.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_pll {
        struct clk_hw hw;
        u32 clk_id;
    }

.. _`zynqmp_pll.members`:

Members
-------

hw
    Handle between common and hardware-specific interfaces

clk_id
    PLL clock ID

.. _`zynqmp_pll_get_mode`:

zynqmp_pll_get_mode
===================

.. c:function:: enum pll_mode zynqmp_pll_get_mode(struct clk_hw *hw)

    Get mode of PLL

    :param hw:
        Handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

.. _`zynqmp_pll_get_mode.return`:

Return
------

Mode of PLL

.. _`zynqmp_pll_set_mode`:

zynqmp_pll_set_mode
===================

.. c:function:: void zynqmp_pll_set_mode(struct clk_hw *hw, bool on)

    Set the PLL mode

    :param hw:
        Handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

    :param on:
        Flag to determine the mode
    :type on: bool

.. _`zynqmp_pll_round_rate`:

zynqmp_pll_round_rate
=====================

.. c:function:: long zynqmp_pll_round_rate(struct clk_hw *hw, unsigned long rate, unsigned long *prate)

    Round a clock frequency

    :param hw:
        Handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

    :param rate:
        Desired clock frequency
    :type rate: unsigned long

    :param prate:
        Clock frequency of parent clock
    :type prate: unsigned long \*

.. _`zynqmp_pll_round_rate.return`:

Return
------

Frequency closest to \ ``rate``\  the hardware can generate

.. _`zynqmp_pll_recalc_rate`:

zynqmp_pll_recalc_rate
======================

.. c:function:: unsigned long zynqmp_pll_recalc_rate(struct clk_hw *hw, unsigned long parent_rate)

    Recalculate clock frequency

    :param hw:
        Handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

    :param parent_rate:
        Clock frequency of parent clock
    :type parent_rate: unsigned long

.. _`zynqmp_pll_recalc_rate.return`:

Return
------

Current clock frequency

.. _`zynqmp_pll_set_rate`:

zynqmp_pll_set_rate
===================

.. c:function:: int zynqmp_pll_set_rate(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate)

    Set rate of PLL

    :param hw:
        Handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

    :param rate:
        Frequency of clock to be set
    :type rate: unsigned long

    :param parent_rate:
        Clock frequency of parent clock
    :type parent_rate: unsigned long

.. _`zynqmp_pll_set_rate.description`:

Description
-----------

Set PLL divider to set desired rate.

.. _`zynqmp_pll_set_rate.return`:

Return
------

rate which is set on success else error code

.. _`zynqmp_pll_is_enabled`:

zynqmp_pll_is_enabled
=====================

.. c:function:: int zynqmp_pll_is_enabled(struct clk_hw *hw)

    Check if a clock is enabled

    :param hw:
        Handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

.. _`zynqmp_pll_is_enabled.return`:

Return
------

1 if the clock is enabled, 0 otherwise

.. _`zynqmp_pll_enable`:

zynqmp_pll_enable
=================

.. c:function:: int zynqmp_pll_enable(struct clk_hw *hw)

    Enable clock

    :param hw:
        Handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

.. _`zynqmp_pll_enable.return`:

Return
------

0 on success else error code

.. _`zynqmp_pll_disable`:

zynqmp_pll_disable
==================

.. c:function:: void zynqmp_pll_disable(struct clk_hw *hw)

    Disable clock

    :param hw:
        Handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

.. _`zynqmp_clk_register_pll`:

zynqmp_clk_register_pll
=======================

.. c:function:: struct clk_hw *zynqmp_clk_register_pll(const char *name, u32 clk_id, const char * const *parents, u8 num_parents, const struct clock_topology *nodes)

    Register PLL with the clock framework

    :param name:
        PLL name
    :type name: const char \*

    :param clk_id:
        Clock ID
    :type clk_id: u32

    :param parents:
        Name of this clock's parents
    :type parents: const char \* const \*

    :param num_parents:
        Number of parents
    :type num_parents: u8

    :param nodes:
        Clock topology node
    :type nodes: const struct clock_topology \*

.. _`zynqmp_clk_register_pll.return`:

Return
------

clock hardware to the registered clock

.. This file was automatic generated / don't edit.

