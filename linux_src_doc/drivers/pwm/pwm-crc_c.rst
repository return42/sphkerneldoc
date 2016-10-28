.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pwm/pwm-crc.c

.. _`crystalcove_pwm`:

struct crystalcove_pwm
======================

.. c:type:: struct crystalcove_pwm

    Crystal Cove PWM controller

.. _`crystalcove_pwm.definition`:

Definition
----------

.. code-block:: c

    struct crystalcove_pwm {
        struct pwm_chip chip;
        struct regmap *regmap;
    }

.. _`crystalcove_pwm.members`:

Members
-------

chip
    the abstract pwm_chip structure.

regmap
    the regmap from the parent device.

.. This file was automatic generated / don't edit.

