.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/timer.c

.. _`omap_get_timer_dt`:

omap_get_timer_dt
=================

.. c:function:: struct device_node *omap_get_timer_dt(const struct of_device_id *match, const char *property)

    get a timer using device-tree \ ``match``\        - device-tree match structure for matching a device type \ ``property``\     - optional timer property to match

    :param match:
        *undescribed*
    :type match: const struct of_device_id \*

    :param property:
        *undescribed*
    :type property: const char \*

.. _`omap_get_timer_dt.description`:

Description
-----------

Helper function to get a timer during early boot using device-tree for use
as kernel system timer. Optionally, the property argument can be used to
select a timer with a specific property. Once a timer is found then mark
the timer node in device-tree as disabled, to prevent the kernel from
registering this timer as a platform device and so no one else can use it.

.. _`omap_dmtimer_init`:

omap_dmtimer_init
=================

.. c:function:: void omap_dmtimer_init( void)

    initialisation function when device tree is used

    :param void:
        no arguments
    :type void: 

.. _`omap_dmtimer_init.description`:

Description
-----------

For secure OMAP3/DRA7xx devices, timers with device type "timer-secure"
cannot be used by the kernel as they are reserved. Therefore, to prevent the
kernel registering these devices remove them dynamically from the device
tree on boot.

.. _`omap_dm_timer_get_errata`:

omap_dm_timer_get_errata
========================

.. c:function:: u32 omap_dm_timer_get_errata( void)

    get errata flags for a timer

    :param void:
        no arguments
    :type void: 

.. _`omap_dm_timer_get_errata.description`:

Description
-----------

Get the timer errata flags that are specific to the OMAP device being used.

.. _`omap2_override_clocksource`:

omap2_override_clocksource
==========================

.. c:function:: int omap2_override_clocksource(char *str)

    clocksource override with user configuration

    :param str:
        *undescribed*
    :type str: char \*

.. _`omap2_override_clocksource.description`:

Description
-----------

Allows user to override default clocksource, using kernel parameter
clocksource="gp_timer"     (For all OMAP2PLUS architectures)

Note that, here we are using same standard kernel parameter "clocksource=",
and not introducing any OMAP specific interface.

.. This file was automatic generated / don't edit.

