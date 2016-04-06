
.. _API-enum-pwm-polarity:

=================
enum pwm_polarity
=================

*man enum pwm_polarity(9)*

*4.6.0-rc1*

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
    a high signal for the duration of the duty- cycle, followed by a low signal for the remainder of the pulse period

PWM_POLARITY_INVERSED
    a low signal for the duration of the duty- cycle, followed by a high signal for the remainder of the pulse period
