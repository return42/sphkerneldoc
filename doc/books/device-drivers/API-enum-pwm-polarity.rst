.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-pwm-polarity:

=================
enum pwm_polarity
=================

*man enum pwm_polarity(9)*

*4.6.0-rc5*

polarity of a PWM signal


Synopsis
========

.. code-block:: c

    enum pwm_polarity {
      PWM_POLARITY_NORMAL,
      PWM_POLARITY_INVERSED
    };


Constants
=========

PWM_POLARITY_NORMAL
    a high signal for the duration of the duty- cycle, followed by a low
    signal for the remainder of the pulse period

PWM_POLARITY_INVERSED
    a low signal for the duration of the duty- cycle, followed by a high
    signal for the remainder of the pulse period


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
