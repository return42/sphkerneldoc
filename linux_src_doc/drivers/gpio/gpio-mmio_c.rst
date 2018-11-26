.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-mmio.c

.. _`bgpio_init`:

bgpio_init
==========

.. c:function:: int bgpio_init(struct gpio_chip *gc, struct device *dev, unsigned long sz, void __iomem *dat, void __iomem *set, void __iomem *clr, void __iomem *dirout, void __iomem *dirin, unsigned long flags)

    Initialize generic GPIO accessor functions

    :param gc:
        the GPIO chip to set up
    :type gc: struct gpio_chip \*

    :param dev:
        the parent device of the new GPIO chip (compulsory)
    :type dev: struct device \*

    :param sz:
        the size (width) of the MMIO registers in bytes, typically 1, 2 or 4
    :type sz: unsigned long

    :param dat:
        MMIO address for the register to READ the value of the GPIO lines, it
        is expected that a 1 in the corresponding bit in this register means the
        line is asserted
    :type dat: void __iomem \*

    :param set:
        MMIO address for the register to SET the value of the GPIO lines, it is
        expected that we write the line with 1 in this register to drive the GPIO line
        high.
    :type set: void __iomem \*

    :param clr:
        MMIO address for the register to CLEAR the value of the GPIO lines, it is
        expected that we write the line with 1 in this register to drive the GPIO line
        low. It is allowed to leave this address as NULL, in that case the SET register
        will be assumed to also clear the GPIO lines, by actively writing the line
        with 0.
    :type clr: void __iomem \*

    :param dirout:
        MMIO address for the register to set the line as OUTPUT. It is assumed
        that setting a line to 1 in this register will turn that line into an
        output line. Conversely, setting the line to 0 will turn that line into
        an input. Either this or \ ``dirin``\  can be defined, but never both.
    :type dirout: void __iomem \*

    :param dirin:
        MMIO address for the register to set this line as INPUT. It is assumed
        that setting a line to 1 in this register will turn that line into an
        input line. Conversely, setting the line to 0 will turn that line into
        an output. Either this or \ ``dirout``\  can be defined, but never both.
    :type dirin: void __iomem \*

    :param flags:
        Different flags that will affect the behaviour of the device, such as
        endianness etc.
    :type flags: unsigned long

.. This file was automatic generated / don't edit.

