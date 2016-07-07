.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-omap2/timer.c

.. _`omap_get_timer_dt`:

omap_get_timer_dt
=================

.. c:function:: struct device_node *omap_get_timer_dt(const struct of_device_id *match, const char *property)

    get a timer using device-tree \ ``match``\        - device-tree match structure for matching a device type \ ``property``\     - optional timer property to match

    :param const struct of_device_id \*match:
        *undescribed*

    :param const char \*property:
        *undescribed*

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

    :param  void:
        no arguments

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

    :param  void:
        no arguments

.. _`omap_dm_timer_get_errata.description`:

Description
-----------

Get the timer errata flags that are specific to the OMAP device being used.

.. _`omap_timer_init`:

omap_timer_init
===============

.. c:function:: int omap_timer_init(struct omap_hwmod *oh, void *unused)

    build and register timer device with an associated timer hwmod

    :param struct omap_hwmod \*oh:
        timer hwmod pointer to be used to build timer device

    :param void \*unused:
        *undescribed*

.. _`omap_timer_init.description`:

Description
-----------

Called by omap_hwmod_for_each_by_class to register each of the timer
devices present in the system. The number of timer devices is known
by parsing through the hwmod database for a given class name. At the
end of function call memory is allocated for timer device and it is
registered to the framework ready to be proved by the driver.

.. _`omap2_dm_timer_init`:

omap2_dm_timer_init
===================

.. c:function:: int omap2_dm_timer_init( void)

    top level regular device initialization

    :param  void:
        no arguments

.. _`omap2_dm_timer_init.description`:

Description
-----------

Uses dedicated hwmod api to parse through hwmod database for
given class name and then build and register the timer device.

.. _`omap2_override_clocksource`:

omap2_override_clocksource
==========================

.. c:function:: int omap2_override_clocksource(char *str)

    clocksource override with user configuration

    :param char \*str:
        *undescribed*

.. _`omap2_override_clocksource.description`:

Description
-----------

Allows user to override default clocksource, using kernel parameter
clocksource="gp_timer"     (For all OMAP2PLUS architectures)

Note that, here we are using same standard kernel parameter "clocksource=",
and not introducing any OMAP specific interface.

.. This file was automatic generated / don't edit.

