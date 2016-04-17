.. -*- coding: utf-8; mode: rst -*-

=============
clk-divider.c
=============


.. _`clk_register_divider`:

clk_register_divider
====================

.. c:function:: struct clk *clk_register_divider (struct device *dev, const char *name, const char *parent_name, unsigned long flags, void __iomem *reg, u8 shift, u8 width, u8 clk_divider_flags, spinlock_t *lock)

    register a divider clock with the clock framework

    :param struct device \*dev:
        device registering this clock

    :param const char \*name:
        name of this clock

    :param const char \*parent_name:
        name of clock's parent

    :param unsigned long flags:
        framework-specific flags

    :param void __iomem \*reg:
        register address to adjust divider

    :param u8 shift:
        number of bits to shift the bitfield

    :param u8 width:
        width of the bitfield

    :param u8 clk_divider_flags:
        divider-specific flags for this clock

    :param spinlock_t \*lock:
        shared register lock for this clock



.. _`clk_register_divider_table`:

clk_register_divider_table
==========================

.. c:function:: struct clk *clk_register_divider_table (struct device *dev, const char *name, const char *parent_name, unsigned long flags, void __iomem *reg, u8 shift, u8 width, u8 clk_divider_flags, const struct clk_div_table *table, spinlock_t *lock)

    register a table based divider clock with the clock framework

    :param struct device \*dev:
        device registering this clock

    :param const char \*name:
        name of this clock

    :param const char \*parent_name:
        name of clock's parent

    :param unsigned long flags:
        framework-specific flags

    :param void __iomem \*reg:
        register address to adjust divider

    :param u8 shift:
        number of bits to shift the bitfield

    :param u8 width:
        width of the bitfield

    :param u8 clk_divider_flags:
        divider-specific flags for this clock

    :param const struct clk_div_table \*table:
        array of divider/value pairs ending with a div set to 0

    :param spinlock_t \*lock:
        shared register lock for this clock

