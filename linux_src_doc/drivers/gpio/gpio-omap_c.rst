.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-omap.c

.. _`omap2_set_gpio_debounce`:

omap2_set_gpio_debounce
=======================

.. c:function:: int omap2_set_gpio_debounce(struct gpio_bank *bank, unsigned offset, unsigned debounce)

    low level gpio debounce time

    :param struct gpio_bank \*bank:
        the gpio bank we're acting upon

    :param unsigned offset:
        the gpio number on this \ ``bank``\ 

    :param unsigned debounce:
        debounce time to use

.. _`omap2_set_gpio_debounce.description`:

Description
-----------

OMAP's debounce time is in 31us steps
<debounce time> = (GPIO_DEBOUNCINGTIME[7:0].DEBOUNCETIME + 1) x 31
so we need to convert and round up to the closest unit.

.. _`omap2_set_gpio_debounce.return`:

Return
------

0 on success, negative error otherwise.

.. _`omap_clear_gpio_debounce`:

omap_clear_gpio_debounce
========================

.. c:function:: void omap_clear_gpio_debounce(struct gpio_bank *bank, unsigned offset)

    clear debounce settings for a gpio

    :param struct gpio_bank \*bank:
        the gpio bank we're acting upon

    :param unsigned offset:
        the gpio number on this \ ``bank``\ 

.. _`omap_clear_gpio_debounce.description`:

Description
-----------

If a gpio is using debounce, then clear the debounce enable bit and if
this is the only gpio in this bank using debounce, then clear the debounce
time too. The debounce clock will also be disabled when calling this function
if this is the only gpio in the bank using debounce.

.. This file was automatic generated / don't edit.

