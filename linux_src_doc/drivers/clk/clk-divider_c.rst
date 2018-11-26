.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clk/clk-divider.c

.. _`clk_register_divider`:

clk_register_divider
====================

.. c:function:: struct clk *clk_register_divider(struct device *dev, const char *name, const char *parent_name, unsigned long flags, void __iomem *reg, u8 shift, u8 width, u8 clk_divider_flags, spinlock_t *lock)

    register a divider clock with the clock framework

    :param dev:
        device registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_name:
        name of clock's parent
    :type parent_name: const char \*

    :param flags:
        framework-specific flags
    :type flags: unsigned long

    :param reg:
        register address to adjust divider
    :type reg: void __iomem \*

    :param shift:
        number of bits to shift the bitfield
    :type shift: u8

    :param width:
        width of the bitfield
    :type width: u8

    :param clk_divider_flags:
        divider-specific flags for this clock
    :type clk_divider_flags: u8

    :param lock:
        shared register lock for this clock
    :type lock: spinlock_t \*

.. _`clk_hw_register_divider`:

clk_hw_register_divider
=======================

.. c:function:: struct clk_hw *clk_hw_register_divider(struct device *dev, const char *name, const char *parent_name, unsigned long flags, void __iomem *reg, u8 shift, u8 width, u8 clk_divider_flags, spinlock_t *lock)

    register a divider clock with the clock framework

    :param dev:
        device registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_name:
        name of clock's parent
    :type parent_name: const char \*

    :param flags:
        framework-specific flags
    :type flags: unsigned long

    :param reg:
        register address to adjust divider
    :type reg: void __iomem \*

    :param shift:
        number of bits to shift the bitfield
    :type shift: u8

    :param width:
        width of the bitfield
    :type width: u8

    :param clk_divider_flags:
        divider-specific flags for this clock
    :type clk_divider_flags: u8

    :param lock:
        shared register lock for this clock
    :type lock: spinlock_t \*

.. _`clk_register_divider_table`:

clk_register_divider_table
==========================

.. c:function:: struct clk *clk_register_divider_table(struct device *dev, const char *name, const char *parent_name, unsigned long flags, void __iomem *reg, u8 shift, u8 width, u8 clk_divider_flags, const struct clk_div_table *table, spinlock_t *lock)

    register a table based divider clock with the clock framework

    :param dev:
        device registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_name:
        name of clock's parent
    :type parent_name: const char \*

    :param flags:
        framework-specific flags
    :type flags: unsigned long

    :param reg:
        register address to adjust divider
    :type reg: void __iomem \*

    :param shift:
        number of bits to shift the bitfield
    :type shift: u8

    :param width:
        width of the bitfield
    :type width: u8

    :param clk_divider_flags:
        divider-specific flags for this clock
    :type clk_divider_flags: u8

    :param table:
        array of divider/value pairs ending with a div set to 0
    :type table: const struct clk_div_table \*

    :param lock:
        shared register lock for this clock
    :type lock: spinlock_t \*

.. _`clk_hw_register_divider_table`:

clk_hw_register_divider_table
=============================

.. c:function:: struct clk_hw *clk_hw_register_divider_table(struct device *dev, const char *name, const char *parent_name, unsigned long flags, void __iomem *reg, u8 shift, u8 width, u8 clk_divider_flags, const struct clk_div_table *table, spinlock_t *lock)

    register a table based divider clock with the clock framework

    :param dev:
        device registering this clock
    :type dev: struct device \*

    :param name:
        name of this clock
    :type name: const char \*

    :param parent_name:
        name of clock's parent
    :type parent_name: const char \*

    :param flags:
        framework-specific flags
    :type flags: unsigned long

    :param reg:
        register address to adjust divider
    :type reg: void __iomem \*

    :param shift:
        number of bits to shift the bitfield
    :type shift: u8

    :param width:
        width of the bitfield
    :type width: u8

    :param clk_divider_flags:
        divider-specific flags for this clock
    :type clk_divider_flags: u8

    :param table:
        array of divider/value pairs ending with a div set to 0
    :type table: const struct clk_div_table \*

    :param lock:
        shared register lock for this clock
    :type lock: spinlock_t \*

.. _`clk_hw_unregister_divider`:

clk_hw_unregister_divider
=========================

.. c:function:: void clk_hw_unregister_divider(struct clk_hw *hw)

    unregister a clk divider

    :param hw:
        hardware-specific clock data to unregister
    :type hw: struct clk_hw \*

.. This file was automatic generated / don't edit.

