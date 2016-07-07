.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/pm-gpio.c

.. _`samsung_gpio_pm_2bit_resume`:

samsung_gpio_pm_2bit_resume
===========================

.. c:function:: void samsung_gpio_pm_2bit_resume(struct samsung_gpio_chip *chip)

    restore the given GPIO bank

    :param struct samsung_gpio_chip \*chip:
        The chip information to resume.

.. _`samsung_gpio_pm_2bit_resume.description`:

Description
-----------

Restore one of the GPIO banks that was saved during suspend. This is
not as simple as once thought, due to the possibility of glitches
from the order that the CON and DAT registers are set in.

The three states the pin can be are {IN,OUT,SFN} which gives us 9
combinations of changes to check. Three of these, if the pin stays
in the same configuration can be discounted. This leaves us with

.. _`samsung_gpio_pm_2bit_resume.the-following`:

the following
-------------


{ IN => OUT }  Change DAT first
{ IN => SFN }  Change CON first
{ OUT => SFN } Change CON first, so new data will not glitch
{ OUT => IN }  Change CON first, so new data will not glitch
{ SFN => IN }  Change CON first
{ SFN => OUT } Change DAT first, so new data will not glitch [1]

We do not currently deal with the UP registers as these control
weak resistors, so a small delay in change should not need to bring
these into the calculations.

[1] this assumes that writing to a pin DAT whilst in SFN will set the
state for when it is next output.

.. _`samsung_pm_save_gpio`:

samsung_pm_save_gpio
====================

.. c:function:: void samsung_pm_save_gpio(struct samsung_gpio_chip *ourchip)

    save gpio chip data for suspend

    :param struct samsung_gpio_chip \*ourchip:
        The chip for suspend.

.. _`samsung_pm_save_gpios`:

samsung_pm_save_gpios
=====================

.. c:function:: void samsung_pm_save_gpios( void)

    Save the state of the GPIO banks.

    :param  void:
        no arguments

.. _`samsung_pm_save_gpios.description`:

Description
-----------

For all the GPIO banks, save the state of each one ready for going
into a suspend mode.

.. _`samsung_pm_resume_gpio`:

samsung_pm_resume_gpio
======================

.. c:function:: void samsung_pm_resume_gpio(struct samsung_gpio_chip *ourchip)

    restore gpio chip data after suspend

    :param struct samsung_gpio_chip \*ourchip:
        The suspended chip.

.. This file was automatic generated / don't edit.

