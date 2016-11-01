.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/greybus/gpio.c

.. _`gb_gpio_irq_map`:

gb_gpio_irq_map
===============

.. c:function:: int gb_gpio_irq_map(struct irq_domain *domain, unsigned int irq, irq_hw_number_t hwirq)

    maps an IRQ into a GB gpio irqchip

    :param struct irq_domain \*domain:
        *undescribed*

    :param unsigned int irq:
        the global irq number used by this GB gpio irqchip irq

    :param irq_hw_number_t hwirq:
        the local IRQ/GPIO line offset on this GB gpio

.. _`gb_gpio_irq_map.description`:

Description
-----------

This function will set up the mapping for a certain IRQ line on a
GB gpio by assigning the GB gpio as chip data, and using the irqchip
stored inside the GB gpio.

.. _`gb_gpio_irqchip_remove`:

gb_gpio_irqchip_remove
======================

.. c:function:: void gb_gpio_irqchip_remove(struct gb_gpio_controller *ggc)

    removes an irqchip added to a gb_gpio_controller

    :param struct gb_gpio_controller \*ggc:
        the gb_gpio_controller to remove the irqchip from

.. _`gb_gpio_irqchip_remove.description`:

Description
-----------

This is called only from \ :c:func:`gb_gpio_remove`\ 

.. _`gb_gpio_irqchip_add`:

gb_gpio_irqchip_add
===================

.. c:function:: int gb_gpio_irqchip_add(struct gpio_chip *chip, struct irq_chip *irqchip, unsigned int first_irq, irq_flow_handler_t handler, unsigned int type)

    adds an irqchip to a gpio chip

    :param struct gpio_chip \*chip:
        the gpio chip to add the irqchip to

    :param struct irq_chip \*irqchip:
        the irqchip to add to the adapter

    :param unsigned int first_irq:
        if not dynamically assigned, the base (first) IRQ to
        allocate gpio irqs from

    :param irq_flow_handler_t handler:
        the irq handler to use (often a predefined irq core function)

    :param unsigned int type:
        the default type for IRQs on this irqchip, pass IRQ_TYPE_NONE
        to have the core avoid setting up any default type in the hardware.

.. _`gb_gpio_irqchip_add.description`:

Description
-----------

This function closely associates a certain irqchip with a certain
gpio chip, providing an irq domain to translate the local IRQs to
global irqs, and making sure that the gpio chip
is passed as chip data to all related functions. Driver callbacks
need to use \ :c:func:`container_of`\  to get their local state containers back
from the gpio chip passed as chip data. An irqdomain will be stored
in the gpio chip that shall be used by the driver to handle IRQ number
translation. The gpio chip will need to be initialized and registered
before calling this function.

.. This file was automatic generated / don't edit.

