.. -*- coding: utf-8; mode: rst -*-

======
gpio.h
======


.. _`gpio`:

struct gpio
===========

.. c:type:: gpio

    a structure describing a GPIO with configuration


.. _`gpio.definition`:

Definition
----------

.. code-block:: c

  struct gpio {
    unsigned gpio;
    unsigned long flags;
    const char * label;
  };


.. _`gpio.members`:

Members
-------

:``gpio``:
    the GPIO number

:``flags``:
    GPIO configuration as specified by GPIOF\_\*

:``label``:
    a literal description string of this GPIO


