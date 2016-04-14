.. -*- coding: utf-8; mode: rst -*-

===============
input-polldev.h
===============

.. _`input_polled_dev`:

struct input_polled_dev
=======================

.. c:type:: struct input_polled_dev

    simple polled input device



Definition
----------

.. code-block:: c

  struct input_polled_dev {
    void * private;
    void (* open) (struct input_polled_dev *dev);
    void (* close) (struct input_polled_dev *dev);
    void (* poll) (struct input_polled_dev *dev);
    unsigned int poll_interval;
    unsigned int poll_interval_max;
    unsigned int poll_interval_min;
    struct input_dev * input;
  };



Members
-------

:``private``:
    private driver data.

:``open``:
    driver-supplied method that prepares device for polling
    (enabled the device and maybe flushes device state).

:``close``:
    driver-supplied method that is called when device is no
    longer being polled. Used to put device into low power mode.

:``poll``:
    driver-supplied method that polls the device and posts
    input events (mandatory).

:``poll_interval``:
    specifies how often the :c:func:`poll` method should be called.::

            Defaults to 500 msec unless overridden when registering the device.

:``poll_interval_max``:
    specifies upper bound for the poll interval.::

            Defaults to the initial value of ``poll_interval``\ .

:``poll_interval_min``:
    specifies lower bound for the poll interval.::

            Defaults to 0.

:``input``:
    input device structure associated with the polled device.::

            Must be properly initialized by the driver (id, name, phys, bits).



Description
-----------

Polled input device provides a skeleton for supporting simple input
devices that do not raise interrupts but have to be periodically
scanned or polled to detect changes in their state.

