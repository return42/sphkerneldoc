.. -*- coding: utf-8; mode: rst -*-

====================
sky81452-backlight.h
====================


.. _`sky81452_bl_platform_data`:

struct sky81452_bl_platform_data
================================

.. c:type:: sky81452_bl_platform_data

    


.. _`sky81452_bl_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct sky81452_bl_platform_data {
    const char * name;
    int gpio_enable;
    unsigned int enable;
    bool ignore_pwm;
    bool dpwm_mode;
    bool phase_shift;
    unsigned int boost_current_limit;
  };


.. _`sky81452_bl_platform_data.members`:

Members
-------

:``name``:
    backlight driver name.

:``gpio_enable``:
    GPIO number which control EN pin

:``enable``:
    Enable mask for current sink channel 1, 2, 3, 4, 5 and 6.

:``ignore_pwm``:
    true if DPWMI should be ignored.

:``dpwm_mode``:
    true is DPWM dimming mode, otherwise Analog dimming mode.

:``phase_shift``:
    true is phase shift mode.

:``boost_current_limit``:
    It should be one of 2300, 2750mA.


