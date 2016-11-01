.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pwm/pwm-cros-ec.c

.. _`cros_ec_pwm_device`:

struct cros_ec_pwm_device
=========================

.. c:type:: struct cros_ec_pwm_device

    Driver data for EC PWM

.. _`cros_ec_pwm_device.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_pwm_device {
        struct device *dev;
        struct cros_ec_device *ec;
        struct pwm_chip chip;
    }

.. _`cros_ec_pwm_device.members`:

Members
-------

dev
    Device node

ec
    Pointer to EC device

chip
    PWM controller chip

.. This file was automatic generated / don't edit.

