.. -*- coding: utf-8; mode: rst -*-

===========
gpio_vbus.h
===========


.. _`gpio_vbus_mach_info`:

struct gpio_vbus_mach_info
==========================

.. c:type:: gpio_vbus_mach_info

    configuration for gpio_vbus


.. _`gpio_vbus_mach_info.definition`:

Definition
----------

.. code-block:: c

  struct gpio_vbus_mach_info {
    int gpio_vbus;
    int gpio_pullup;
    bool gpio_vbus_inverted;
    bool gpio_pullup_inverted;
    bool wakeup;
  };


.. _`gpio_vbus_mach_info.members`:

Members
-------

:``gpio_vbus``:
    VBUS sensing GPIO

:``gpio_pullup``:
    optional D+ or D- pullup GPIO (else negative/invalid)

:``gpio_vbus_inverted``:
    true if gpio_vbus is active low

:``gpio_pullup_inverted``:
    true if gpio_pullup is active low

:``wakeup``:
    configure gpio_vbus as a wake-up source




.. _`gpio_vbus_mach_info.description`:

Description
-----------

The VBUS sensing GPIO should have a pulldown, which will normally be
part of a resistor ladder turning a 4.0V-5.25V level on VBUS into a
value the GPIO detects as active.  Some systems will use comparators.

