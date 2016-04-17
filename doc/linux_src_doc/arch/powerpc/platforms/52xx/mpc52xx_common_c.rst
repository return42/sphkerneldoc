.. -*- coding: utf-8; mode: rst -*-

================
mpc52xx_common.c
================


.. _`mpc52xx_declare_of_platform_devices`:

mpc52xx_declare_of_platform_devices
===================================

.. c:function:: void mpc52xx_declare_of_platform_devices ( void)

    :param void:
        no arguments



.. _`mpc52xx_declare_of_platform_devices.description`:

Description
-----------

of the localplus bus to the of_platform
bus.



.. _`mpc52xx_map_common_devices`:

mpc52xx_map_common_devices
==========================

.. c:function:: void mpc52xx_map_common_devices ( void)

    :param void:
        no arguments



.. _`mpc52xx_set_psc_clkdiv`:

mpc52xx_set_psc_clkdiv
======================

.. c:function:: int mpc52xx_set_psc_clkdiv (int psc_id, int clkdiv)

    :param int psc_id:
        id of psc port; must be 1,2,3 or 6

    :param int clkdiv:
        clock divider value to put into CDM PSC register.



.. _`mpc52xx_get_xtal_freq`:

mpc52xx_get_xtal_freq
=====================

.. c:function:: unsigned int mpc52xx_get_xtal_freq (struct device_node *node)

    Get SYS_XTAL_IN frequency for a device

    :param struct device_node \*node:
        device node



.. _`mpc52xx_get_xtal_freq.description`:

Description
-----------

Returns the frequency of the external oscillator clock connected
to the SYS_XTAL_IN pin, or 0 if it cannot be determined.



.. _`mpc52xx_restart`:

mpc52xx_restart
===============

.. c:function:: void mpc52xx_restart (char *cmd)

    >restart hook for mpc5200 using the watchdog timer

    :param char \*cmd:

        *undescribed*



.. _`mpc5200_psc_ac97_gpio_reset`:

mpc5200_psc_ac97_gpio_reset
===========================

.. c:function:: int mpc5200_psc_ac97_gpio_reset (int psc_number)

    :param int psc_number:

        *undescribed*

