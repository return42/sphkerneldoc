.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-pwm-device:

=================
struct pwm_device
=================

*man struct pwm_device(9)*

*4.6.0-rc5*

PWM channel object


Synopsis
========

.. code-block:: c

    struct pwm_device {
      const char * label;
      unsigned long flags;
      unsigned int hwpwm;
      unsigned int pwm;
      struct pwm_chip * chip;
      void * chip_data;
      struct mutex lock;
      unsigned int period;
      unsigned int duty_cycle;
      enum pwm_polarity polarity;
    };


Members
=======

label
    name of the PWM device

flags
    flags associated with the PWM device

hwpwm
    per-chip relative index of the PWM device

pwm
    global index of the PWM device

chip
    PWM chip providing this PWM device

chip_data
    chip-private data associated with the PWM device

lock
    used to serialize accesses to the PWM device where necessary

period
    period of the PWM signal (in nanoseconds)

duty_cycle
    duty cycle of the PWM signal (in nanoseconds)

polarity
    polarity of the PWM signal


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
