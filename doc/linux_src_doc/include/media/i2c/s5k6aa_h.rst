.. -*- coding: utf-8; mode: rst -*-

========
s5k6aa.h
========


.. _`s5k6aa_gpio`:

struct s5k6aa_gpio
==================

.. c:type:: s5k6aa_gpio

    data structure describing a GPIO


.. _`s5k6aa_gpio.definition`:

Definition
----------

.. code-block:: c

  struct s5k6aa_gpio {
    int gpio;
    int level;
  };


.. _`s5k6aa_gpio.members`:

Members
-------

:``gpio``:
    GPIO number

:``level``:
    indicates active state of the ``gpio``




.. _`s5k6aa_platform_data`:

struct s5k6aa_platform_data
===========================

.. c:type:: s5k6aa_platform_data

    s5k6aa driver platform data


.. _`s5k6aa_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct s5k6aa_platform_data {
    int (* set_power) (int enable);
    unsigned long mclk_frequency;
    struct s5k6aa_gpio gpio_reset;
    struct s5k6aa_gpio gpio_stby;
    u8 nlanes;
    u8 horiz_flip;
    u8 vert_flip;
  };


.. _`s5k6aa_platform_data.members`:

Members
-------

:``set_power``:
    an additional callback to the board code, called
    after enabling the regulators and before switching
    the sensor off

:``mclk_frequency``:
    sensor's master clock frequency in Hz

:``gpio_reset``:
    GPIO driving RESET pin

:``gpio_stby``:
    GPIO driving STBY pin

:``nlanes``:
    maximum number of MIPI-CSI lanes used

:``horiz_flip``:
    default horizontal image flip value, non zero to enable

:``vert_flip``:
    default vertical image flip value, non zero to enable


