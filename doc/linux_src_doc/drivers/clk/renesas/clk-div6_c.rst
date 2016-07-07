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
    *undescribed*

src_width
    *undescribed*

parents
    *undescribed*

.. _`cpg_div6_register`:

cpg_div6_register
=================

.. c:function:: struct clk *cpg_div6_register(const char *name, unsigned int num_parents, const char **parent_names, void __iomem *reg)

    Register a DIV6 clock

    :param const char \*name:
        Name of the DIV6 clock

    :param unsigned int num_parents:
        Number of parent clocks of the DIV6 clock (1, 4, or 8)

    :param const char \*\*parent_names:
        Array containing the names of the parent clocks

    :param void __iomem \*reg:
        Mapped register used to control the DIV6 clock

.. This file was automatic generated / don't edit.

