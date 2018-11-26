.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/dsa/mv88e6xxx/global2_scratch.c

.. _`mv88e6xxx_g2_scratch_get_bit`:

mv88e6xxx_g2_scratch_get_bit
============================

.. c:function:: int mv88e6xxx_g2_scratch_get_bit(struct mv88e6xxx_chip *chip, int base_reg, unsigned int offset, int *set)

    get a bit

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param base_reg:
        *undescribed*
    :type base_reg: int

    :param offset:
        *undescribed*
    :type offset: unsigned int

    :param set:
        is bit set?
    :type set: int \*

.. _`mv88e6xxx_g2_scratch_set_bit`:

mv88e6xxx_g2_scratch_set_bit
============================

.. c:function:: int mv88e6xxx_g2_scratch_set_bit(struct mv88e6xxx_chip *chip, int base_reg, unsigned int offset, int set)

    set (or clear) a bit

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param base_reg:
        *undescribed*
    :type base_reg: int

    :param offset:
        *undescribed*
    :type offset: unsigned int

    :param set:
        set if true, clear if false
    :type set: int

.. _`mv88e6xxx_g2_scratch_set_bit.description`:

Description
-----------

Helper function for dealing with the direction and data registers.

.. _`mv88e6352_g2_scratch_gpio_get_data`:

mv88e6352_g2_scratch_gpio_get_data
==================================

.. c:function:: int mv88e6352_g2_scratch_gpio_get_data(struct mv88e6xxx_chip *chip, unsigned int pin)

    get data on gpio pin

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param pin:
        gpio index
    :type pin: unsigned int

.. _`mv88e6352_g2_scratch_gpio_get_data.return`:

Return
------

0 for low, 1 for high, negative error

.. _`mv88e6352_g2_scratch_gpio_set_data`:

mv88e6352_g2_scratch_gpio_set_data
==================================

.. c:function:: int mv88e6352_g2_scratch_gpio_set_data(struct mv88e6xxx_chip *chip, unsigned int pin, int value)

    set data on gpio pin

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param pin:
        gpio index
    :type pin: unsigned int

    :param value:
        value to set
    :type value: int

.. _`mv88e6352_g2_scratch_gpio_get_dir`:

mv88e6352_g2_scratch_gpio_get_dir
=================================

.. c:function:: int mv88e6352_g2_scratch_gpio_get_dir(struct mv88e6xxx_chip *chip, unsigned int pin)

    get direction of gpio pin

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param pin:
        gpio index
    :type pin: unsigned int

.. _`mv88e6352_g2_scratch_gpio_get_dir.return`:

Return
------

0 for output, 1 for input (same as GPIOF_DIR_XXX).

.. _`mv88e6352_g2_scratch_gpio_set_dir`:

mv88e6352_g2_scratch_gpio_set_dir
=================================

.. c:function:: int mv88e6352_g2_scratch_gpio_set_dir(struct mv88e6xxx_chip *chip, unsigned int pin, bool input)

    set direction of gpio pin

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param pin:
        gpio index
    :type pin: unsigned int

    :param input:
        *undescribed*
    :type input: bool

.. _`mv88e6352_g2_scratch_gpio_get_pctl`:

mv88e6352_g2_scratch_gpio_get_pctl
==================================

.. c:function:: int mv88e6352_g2_scratch_gpio_get_pctl(struct mv88e6xxx_chip *chip, unsigned int pin, int *func)

    get pin control setting

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param pin:
        gpio index
    :type pin: unsigned int

    :param func:
        function number
    :type func: int \*

.. _`mv88e6352_g2_scratch_gpio_get_pctl.description`:

Description
-----------

Note that the function numbers themselves may vary by chipset.

.. _`mv88e6352_g2_scratch_gpio_set_pctl`:

mv88e6352_g2_scratch_gpio_set_pctl
==================================

.. c:function:: int mv88e6352_g2_scratch_gpio_set_pctl(struct mv88e6xxx_chip *chip, unsigned int pin, int func)

    set pin control setting

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param pin:
        gpio index
    :type pin: unsigned int

    :param func:
        function number
    :type func: int

.. _`mv88e6xxx_g2_scratch_gpio_set_smi`:

mv88e6xxx_g2_scratch_gpio_set_smi
=================================

.. c:function:: int mv88e6xxx_g2_scratch_gpio_set_smi(struct mv88e6xxx_chip *chip, bool external)

    set gpio muxing for external smi

    :param chip:
        chip private data
    :type chip: struct mv88e6xxx_chip \*

    :param external:
        set mux for external smi, or free for gpio usage
    :type external: bool

.. _`mv88e6xxx_g2_scratch_gpio_set_smi.description`:

Description
-----------

Some mv88e6xxx models have GPIO pins that may be configured as
an external SMI interface, or they may be made free for other
GPIO uses.

.. This file was automatic generated / don't edit.

