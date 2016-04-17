.. -*- coding: utf-8; mode: rst -*-

===========
gpio_tilt.h
===========


.. _`gpio_tilt_axis`:

struct gpio_tilt_axis
=====================

.. c:type:: gpio_tilt_axis

    Axis used by the tilt switch


.. _`gpio_tilt_axis.definition`:

Definition
----------

.. code-block:: c

  struct gpio_tilt_axis {
    int axis;
    int min;
    int max;
    int fuzz;
    int flat;
  };


.. _`gpio_tilt_axis.members`:

Members
-------

:``axis``:
    Constant describing the axis, e.g. ABS_X

:``min``:
    minimum value for abs_param

:``max``:
    maximum value for abs_param

:``fuzz``:
    fuzz value for abs_param

:``flat``:
    flat value for abs_param




.. _`gpio_tilt_state`:

struct gpio_tilt_state
======================

.. c:type:: gpio_tilt_state

    state description


.. _`gpio_tilt_state.definition`:

Definition
----------

.. code-block:: c

  struct gpio_tilt_state {
    int gpios;
    int * axes;
  };


.. _`gpio_tilt_state.members`:

Members
-------

:``gpios``:
    bitfield of gpio target-states for the value

:``axes``:
    array containing the axes settings for the gpio state
    The array indizes must correspond to the axes defined
    in platform_data




.. _`gpio_tilt_state.description`:

Description
-----------

This structure describes a supported axis settings
and the necessary gpio-state which represent it.

The n-th bit in the bitfield describes the state of the n-th GPIO
from the gpios-array defined in gpio_regulator_config below.



.. _`gpio_tilt_platform_data`:

struct gpio_tilt_platform_data
==============================

.. c:type:: gpio_tilt_platform_data

    


.. _`gpio_tilt_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct gpio_tilt_platform_data {
    struct gpio * gpios;
    int nr_gpios;
    struct gpio_tilt_axis * axes;
    int nr_axes;
    struct gpio_tilt_state * states;
    int nr_states;
    int debounce_interval;
    unsigned int poll_interval;
    int (* enable) (struct device *dev);
    void (* disable) (struct device *dev);
  };


.. _`gpio_tilt_platform_data.members`:

Members
-------

:``gpios``:
    Array containing the gpios determining the tilt state

:``nr_gpios``:
    Number of gpios

:``axes``:
    Array of gpio_tilt_axis descriptions

:``nr_axes``:
    Number of axes

:``states``:
    Array of gpio_tilt_state entries describing
    the gpio state for specific tilts

:``nr_states``:
    Number of states available

:``debounce_interval``:
    debounce ticks interval in msecs

:``poll_interval``:
    polling interval in msecs - for polling driver only

:``enable``:
    callback to enable the tilt switch

:``disable``:
    callback to disable the tilt switch




.. _`gpio_tilt_platform_data.description`:

Description
-----------

This structure contains gpio-tilt-switch configuration
information that must be passed by platform code to the
gpio-tilt input driver.

