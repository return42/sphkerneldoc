.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/renesas/clk-div6.c

.. _`div6_clock`:

struct div6_clock
=================

.. c:type:: struct div6_clock

    CPG 6 bit divider clock

.. _`div6_clock.definition`:

Definition
----------

.. code-block:: c

    struct div6_clock {
        struct clk_hw hw;
        void __iomem *reg;
        unsigned int div;
        u32 src_shift;
        u32 src_width;
        u8 *parents;
        struct notifier_block nb;
    }

.. _`div6_clock.members`:

Members
-------

hw
    handle between common and hardware-specific interfaces

reg
    IO-remapped register

div
    divisor value (1-64)

src_shift
    Shift to access the register bits to select the parent clock

src_width
    Number of register bits to select the parent clock (may be 0)

parents
    Array to map from valid parent clocks indices to hardware indices

nb
    Notifier block to save/restore clock state for system resume

.. _`cpg_div6_register`:

cpg_div6_register
=================

.. c:function:: struct clk *cpg_div6_register(const char *name, unsigned int num_parents, const char **parent_names, void __iomem *reg, struct raw_notifier_head *notifiers)

    Register a DIV6 clock

    :param name:
        Name of the DIV6 clock
    :type name: const char \*

    :param num_parents:
        Number of parent clocks of the DIV6 clock (1, 4, or 8)
    :type num_parents: unsigned int

    :param parent_names:
        Array containing the names of the parent clocks
    :type parent_names: const char \*\*

    :param reg:
        Mapped register used to control the DIV6 clock
    :type reg: void __iomem \*

    :param notifiers:
        Optional notifier chain to save/restore state for system resume
    :type notifiers: struct raw_notifier_head \*

.. This file was automatic generated / don't edit.

