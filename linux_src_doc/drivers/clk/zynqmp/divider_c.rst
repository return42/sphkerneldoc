.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/zynqmp/divider.c

.. _`zynqmp_clk_divider`:

struct zynqmp_clk_divider
=========================

.. c:type:: struct zynqmp_clk_divider

    adjustable divider clock

.. _`zynqmp_clk_divider.definition`:

Definition
----------

.. code-block:: c

    struct zynqmp_clk_divider {
        struct clk_hw hw;
        u8 flags;
        u32 clk_id;
        u32 div_type;
    }

.. _`zynqmp_clk_divider.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

flags
    Hardware specific flags

clk_id
    Id of clock

div_type
    divisor type (TYPE_DIV1 or TYPE_DIV2)

.. _`zynqmp_clk_divider_recalc_rate`:

zynqmp_clk_divider_recalc_rate
==============================

.. c:function:: unsigned long zynqmp_clk_divider_recalc_rate(struct clk_hw *hw, unsigned long parent_rate)

    Recalc rate of divider clock

    :param hw:
        handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

    :param parent_rate:
        rate of parent clock
    :type parent_rate: unsigned long

.. _`zynqmp_clk_divider_recalc_rate.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_clk_divider_round_rate`:

zynqmp_clk_divider_round_rate
=============================

.. c:function:: long zynqmp_clk_divider_round_rate(struct clk_hw *hw, unsigned long rate, unsigned long *prate)

    Round rate of divider clock

    :param hw:
        handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

    :param rate:
        rate of clock to be set
    :type rate: unsigned long

    :param prate:
        rate of parent clock
    :type prate: unsigned long \*

.. _`zynqmp_clk_divider_round_rate.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_clk_divider_set_rate`:

zynqmp_clk_divider_set_rate
===========================

.. c:function:: int zynqmp_clk_divider_set_rate(struct clk_hw *hw, unsigned long rate, unsigned long parent_rate)

    Set rate of divider clock

    :param hw:
        handle between common and hardware-specific interfaces
    :type hw: struct clk_hw \*

    :param rate:
        rate of clock to be set
    :type rate: unsigned long

    :param parent_rate:
        rate of parent clock
    :type parent_rate: unsigned long

.. _`zynqmp_clk_divider_set_rate.return`:

Return
------

0 on success else error+reason

.. _`zynqmp_clk_register_divider`:

zynqmp_clk_register_divider
===========================

.. c:function:: struct clk_hw *zynqmp_clk_register_divider(const char *name, u32 clk_id, const char * const *parents, u8 num_parents, const struct clock_topology *nodes)

    Register a divider clock

    :param name:
        Name of this clock
    :type name: const char \*

    :param clk_id:
        Id of clock
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

.. _`zynqmp_clk_register_divider.return`:

Return
------

clock hardware to registered clock divider

.. This file was automatic generated / don't edit.

