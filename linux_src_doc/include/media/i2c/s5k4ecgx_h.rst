.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/i2c/s5k4ecgx.h

.. _`s5k4ecgx_gpio`:

struct s5k4ecgx_gpio
====================

.. c:type:: struct s5k4ecgx_gpio

    data structure describing a GPIO

.. _`s5k4ecgx_gpio.definition`:

Definition
----------

.. code-block:: c

    struct s5k4ecgx_gpio {
        int gpio;
        int level;
    }

.. _`s5k4ecgx_gpio.members`:

Members
-------

gpio
    GPIO number

level
    indicates active state of the \ ``gpio``\ 

.. _`s5k4ecgx_platform_data`:

struct s5k4ecgx_platform_data
=============================

.. c:type:: struct s5k4ecgx_platform_data

    s5k4ecgx driver platform data

.. _`s5k4ecgx_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct s5k4ecgx_platform_data {
        struct s5k4ecgx_gpio gpio_reset;
        struct s5k4ecgx_gpio gpio_stby;
    }

.. _`s5k4ecgx_platform_data.members`:

Members
-------

gpio_reset
    GPIO driving RESET pin

gpio_stby
    GPIO driving STBY pin

.. This file was automatic generated / don't edit.

