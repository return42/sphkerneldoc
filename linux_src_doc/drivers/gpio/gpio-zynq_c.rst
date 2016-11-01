.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-zynq.c

.. _`zynq_gpio`:

struct zynq_gpio
================

.. c:type:: struct zynq_gpio

    gpio device private data structure

.. _`zynq_gpio.definition`:

Definition
----------

.. code-block:: c

    struct zynq_gpio {
        struct gpio_chip chip;
        void __iomem *base_addr;
        struct clk *clk;
        int irq;
        const struct zynq_platform_data *p_data;
    }

.. _`zynq_gpio.members`:

Members
-------

chip
    instance of the gpio_chip

base_addr
    base address of the GPIO device

clk
    clock resource for this controller

irq
    interrupt for the GPIO device

p_data
    pointer to platform data

.. _`zynq_platform_data`:

struct zynq_platform_data
=========================

.. c:type:: struct zynq_platform_data

    zynq gpio platform data structure

.. _`zynq_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct zynq_platform_data {
        const char *label;
        u32 quirks;
        u16 ngpio;
        int max_bank;
        int bank_min[ZYNQMP_GPIO_MAX_BANK];
        int bank_max[ZYNQMP_GPIO_MAX_BANK];
    }

.. _`zynq_platform_data.members`:

Members
-------

label
    string to store in gpio->label

quirks
    *undescribed*

ngpio
    max number of gpio pins

max_bank
    maximum number of gpio banks

bank_min
    this array represents bank's min pin

bank_max
    this array represents bank's max pin

.. _`zynq_gpio_get_bank_pin`:

zynq_gpio_get_bank_pin
======================

.. c:function:: void zynq_gpio_get_bank_pin(unsigned int pin_num, unsigned int *bank_num, unsigned int *bank_pin_num, struct zynq_gpio *gpio)

    Get the bank number and pin number within that bank for a given pin in the GPIO device

    :param unsigned int pin_num:
        gpio pin number within the device

    :param unsigned int \*bank_num:
        an output parameter used to return the bank number of the gpio
        pin

    :param unsigned int \*bank_pin_num:
        an output parameter used to return pin number within a bank
        for the given gpio pin

    :param struct zynq_gpio \*gpio:
        *undescribed*

.. _`zynq_gpio_get_bank_pin.description`:

Description
-----------

Returns the bank number and pin offset within the bank.

.. _`zynq_gpio_get_value`:

zynq_gpio_get_value
===================

.. c:function:: int zynq_gpio_get_value(struct gpio_chip *chip, unsigned int pin)

    Get the state of the specified pin of GPIO device

    :param struct gpio_chip \*chip:
        gpio_chip instance to be worked on

    :param unsigned int pin:
        gpio pin number within the device

.. _`zynq_gpio_get_value.description`:

Description
-----------

This function reads the state of the specified pin of the GPIO device.

.. _`zynq_gpio_get_value.return`:

Return
------

0 if the pin is low, 1 if pin is high.

.. _`zynq_gpio_set_value`:

zynq_gpio_set_value
===================

.. c:function:: void zynq_gpio_set_value(struct gpio_chip *chip, unsigned int pin, int state)

    Modify the state of the pin with specified value

    :param struct gpio_chip \*chip:
        gpio_chip instance to be worked on

    :param unsigned int pin:
        gpio pin number within the device

    :param int state:
        value used to modify the state of the specified pin

.. _`zynq_gpio_set_value.description`:

Description
-----------

This function calculates the register offset (i.e to lower 16 bits or
upper 16 bits) based on the given pin number and sets the state of a
gpio pin to the specified value. The state is either 0 or non-zero.

.. _`zynq_gpio_dir_in`:

zynq_gpio_dir_in
================

.. c:function:: int zynq_gpio_dir_in(struct gpio_chip *chip, unsigned int pin)

    Set the direction of the specified GPIO pin as input

    :param struct gpio_chip \*chip:
        gpio_chip instance to be worked on

    :param unsigned int pin:
        gpio pin number within the device

.. _`zynq_gpio_dir_in.description`:

Description
-----------

This function uses the read-modify-write sequence to set the direction of
the gpio pin as input.

.. _`zynq_gpio_dir_in.return`:

Return
------

0 always

.. _`zynq_gpio_dir_out`:

zynq_gpio_dir_out
=================

.. c:function:: int zynq_gpio_dir_out(struct gpio_chip *chip, unsigned int pin, int state)

    Set the direction of the specified GPIO pin as output

    :param struct gpio_chip \*chip:
        gpio_chip instance to be worked on

    :param unsigned int pin:
        gpio pin number within the device

    :param int state:
        value to be written to specified pin

.. _`zynq_gpio_dir_out.description`:

Description
-----------

This function sets the direction of specified GPIO pin as output, configures
the Output Enable register for the pin and uses zynq_gpio_set to set
the state of the pin to the value specified.

.. _`zynq_gpio_dir_out.return`:

Return
------

0 always

.. _`zynq_gpio_irq_mask`:

zynq_gpio_irq_mask
==================

.. c:function:: void zynq_gpio_irq_mask(struct irq_data *irq_data)

    Disable the interrupts for a gpio pin

    :param struct irq_data \*irq_data:
        per irq and chip data passed down to chip functions

.. _`zynq_gpio_irq_mask.description`:

Description
-----------

This function calculates gpio pin number from irq number and sets the
bit in the Interrupt Disable register of the corresponding bank to disable
interrupts for that pin.

.. _`zynq_gpio_irq_unmask`:

zynq_gpio_irq_unmask
====================

.. c:function:: void zynq_gpio_irq_unmask(struct irq_data *irq_data)

    Enable the interrupts for a gpio pin

    :param struct irq_data \*irq_data:
        irq data containing irq number of gpio pin for the interrupt
        to enable

.. _`zynq_gpio_irq_unmask.description`:

Description
-----------

This function calculates the gpio pin number from irq number and sets the
bit in the Interrupt Enable register of the corresponding bank to enable
interrupts for that pin.

.. _`zynq_gpio_irq_ack`:

zynq_gpio_irq_ack
=================

.. c:function:: void zynq_gpio_irq_ack(struct irq_data *irq_data)

    Acknowledge the interrupt of a gpio pin

    :param struct irq_data \*irq_data:
        irq data containing irq number of gpio pin for the interrupt
        to ack

.. _`zynq_gpio_irq_ack.description`:

Description
-----------

This function calculates gpio pin number from irq number and sets the bit
in the Interrupt Status Register of the corresponding bank, to ACK the irq.

.. _`zynq_gpio_irq_enable`:

zynq_gpio_irq_enable
====================

.. c:function:: void zynq_gpio_irq_enable(struct irq_data *irq_data)

    Enable the interrupts for a gpio pin

    :param struct irq_data \*irq_data:
        irq data containing irq number of gpio pin for the interrupt
        to enable

.. _`zynq_gpio_irq_enable.description`:

Description
-----------

Clears the INTSTS bit and unmasks the given interrupt.

.. _`zynq_gpio_set_irq_type`:

zynq_gpio_set_irq_type
======================

.. c:function:: int zynq_gpio_set_irq_type(struct irq_data *irq_data, unsigned int type)

    Set the irq type for a gpio pin

    :param struct irq_data \*irq_data:
        irq data containing irq number of gpio pin

    :param unsigned int type:
        interrupt type that is to be set for the gpio pin

.. _`zynq_gpio_set_irq_type.description`:

Description
-----------

This function gets the gpio pin number and its bank from the gpio pin number
and configures the INT_TYPE, INT_POLARITY and INT_ANY registers.

.. _`zynq_gpio_set_irq_type.return`:

Return
------

0, negative error otherwise.
TYPE-EDGE_RISING,  INT_TYPE - 1, INT_POLARITY - 1,  INT_ANY - 0;
TYPE-EDGE_FALLING, INT_TYPE - 1, INT_POLARITY - 0,  INT_ANY - 0;
TYPE-EDGE_BOTH,    INT_TYPE - 1, INT_POLARITY - NA, INT_ANY - 1;
TYPE-LEVEL_HIGH,   INT_TYPE - 0, INT_POLARITY - 1,  INT_ANY - NA;
TYPE-LEVEL_LOW,    INT_TYPE - 0, INT_POLARITY - 0,  INT_ANY - NA

.. _`zynq_gpio_irqhandler`:

zynq_gpio_irqhandler
====================

.. c:function:: void zynq_gpio_irqhandler(struct irq_desc *desc)

    IRQ handler for the gpio banks of a gpio device

    :param struct irq_desc \*desc:
        irq descriptor instance of the 'irq'

.. _`zynq_gpio_irqhandler.description`:

Description
-----------

This function reads the Interrupt Status Register of each bank to get the
gpio pin number which has triggered an interrupt. It then acks the triggered
interrupt and calls the pin specific handler set by the higher layer
application for that pin.

.. _`zynq_gpio_irqhandler.note`:

Note
----

A bug is reported if no handler is set for the gpio pin.

.. _`zynq_gpio_probe`:

zynq_gpio_probe
===============

.. c:function:: int zynq_gpio_probe(struct platform_device *pdev)

    Initialization method for a zynq_gpio device

    :param struct platform_device \*pdev:
        platform device instance

.. _`zynq_gpio_probe.description`:

Description
-----------

This function allocates memory resources for the gpio device and registers
all the banks of the device. It will also set up interrupts for the gpio
pins.

.. _`zynq_gpio_probe.note`:

Note
----

Interrupts are disabled for all the banks during initialization.

.. _`zynq_gpio_probe.return`:

Return
------

0 on success, negative error otherwise.

.. _`zynq_gpio_remove`:

zynq_gpio_remove
================

.. c:function:: int zynq_gpio_remove(struct platform_device *pdev)

    Driver removal function

    :param struct platform_device \*pdev:
        platform device instance

.. _`zynq_gpio_remove.return`:

Return
------

0 always

.. _`zynq_gpio_init`:

zynq_gpio_init
==============

.. c:function:: int zynq_gpio_init( void)

    Initial driver registration call

    :param  void:
        no arguments

.. _`zynq_gpio_init.return`:

Return
------

value from platform_driver_register

.. This file was automatic generated / don't edit.

