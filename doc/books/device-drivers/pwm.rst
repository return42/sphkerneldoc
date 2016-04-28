.. -*- coding: utf-8; mode: rst -*-

.. _pwm:

============================
Pulse-Width Modulation (PWM)
============================

Pulse-width modulation is a modulation technique primarily used to
control power supplied to electrical devices.

The PWM framework provides an abstraction for providers and consumers of
PWM signals. A controller that provides one or more PWM signals is
registered as ``struct pwm_chip``. Providers are expected to embed this
structure in a driver-specific structure. This structure contains fields
that describe a particular chip.

A chip exposes one or more PWM signal sources, each of which exposed as
a ``struct pwm_device``. Operations can be performed on PWM devices to
control the period, duty cycle, polarity and active state of the signal.

Note that PWM devices are exclusive resources: they can always only be
used by one consumer at a time.


.. toctree::
    :maxdepth: 1

    API-enum-pwm-polarity
    API-struct-pwm-device
    API-struct-pwm-ops
    API-struct-pwm-chip
    API-pwm-set-chip-data
    API-pwm-get-chip-data
    API-pwmchip-add-with-polarity
    API-pwmchip-add
    API-pwmchip-remove
    API-pwm-request
    API-pwm-request-from-chip
    API-pwm-free
    API-pwm-config
    API-pwm-set-polarity
    API-pwm-enable
    API-pwm-disable
    API-of-pwm-get
    API-pwm-get
    API-pwm-put
    API-devm-pwm-get
    API-devm-of-pwm-get
    API-devm-pwm-put
    API-pwm-can-sleep




.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
