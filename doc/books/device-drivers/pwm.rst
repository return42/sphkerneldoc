.. -*- coding: utf-8; mode: rst -*-

.. _pwm:

****************************
Pulse-Width Modulation (PWM)
****************************

Pulse-width modulation is a modulation technique primarily used to
control power supplied to electrical devices.

The PWM framework provides an abstraction for providers and consumers of
PWM signals. A controller that provides one or more PWM signals is
registered as :c:type:`struct pwm_chip`. Providers are expected to
embed this structure in a driver-specific structure. This structure
contains fields that describe a particular chip.

A chip exposes one or more PWM signal sources, each of which exposed as
a :c:type:`struct pwm_device`. Operations can be performed on PWM
devices to control the period, duty cycle, polarity and active state of
the signal.

Note that PWM devices are exclusive resources: they can always only be
used by one consumer at a time.


.. kernel-doc:: include/linux/pwm.h
    :internal:

.. kernel-doc:: drivers/pwm/core.c
    :export:



.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
