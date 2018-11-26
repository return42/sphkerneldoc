.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/regulator/tps65090-regulator.c

.. _`tps65090_regulator`:

struct tps65090_regulator
=========================

.. c:type:: struct tps65090_regulator

    Per-regulator data for a tps65090 regulator

.. _`tps65090_regulator.definition`:

Definition
----------

.. code-block:: c

    struct tps65090_regulator {
        struct device *dev;
        struct regulator_desc *desc;
        struct regulator_dev *rdev;
        bool overcurrent_wait_valid;
        int overcurrent_wait;
    }

.. _`tps65090_regulator.members`:

Members
-------

dev
    Pointer to our device.

desc
    The struct regulator_desc for the regulator.

rdev
    The struct regulator_dev for the regulator.

overcurrent_wait_valid
    True if overcurrent_wait is valid.

overcurrent_wait
    For FETs, the value to put in the WTFET bitfield.

.. _`tps65090_reg_set_overcurrent_wait`:

tps65090_reg_set_overcurrent_wait
=================================

.. c:function:: int tps65090_reg_set_overcurrent_wait(struct tps65090_regulator *ri, struct regulator_dev *rdev)

    Setup overcurrent wait

    :param ri:
        Overall regulator data
    :type ri: struct tps65090_regulator \*

    :param rdev:
        Regulator device
    :type rdev: struct regulator_dev \*

.. _`tps65090_reg_set_overcurrent_wait.description`:

Description
-----------

This will set the overcurrent wait time based on what's in the regulator
info.

.. _`tps65090_reg_set_overcurrent_wait.return`:

Return
------

0 if no error, non-zero if there was an error writing the register.

.. _`tps65090_try_enable_fet`:

tps65090_try_enable_fet
=======================

.. c:function:: int tps65090_try_enable_fet(struct regulator_dev *rdev)

    Try to enable a FET

    :param rdev:
        Regulator device
    :type rdev: struct regulator_dev \*

.. _`tps65090_try_enable_fet.return`:

Return
------

0 if ok, -ENOTRECOVERABLE if the FET power good bit did not get
set, or some other -ve value if another error occurred (e.g. i2c error)

.. _`tps65090_fet_enable`:

tps65090_fet_enable
===================

.. c:function:: int tps65090_fet_enable(struct regulator_dev *rdev)

    Enable a FET, trying a few times if it fails

    :param rdev:
        Regulator device
    :type rdev: struct regulator_dev \*

.. _`tps65090_fet_enable.description`:

Description
-----------

Some versions of the tps65090 have issues when turning on the FETs.
This function goes through several steps to ensure the best chance of the
FET going on.  Specifically:
- We'll make sure that we bump the "overcurrent wait" to the maximum, which
increases the chances that we'll turn on properly.
- We'll retry turning the FET on multiple times (turning off in between).

.. _`tps65090_fet_enable.return`:

Return
------

0 if ok, non-zero if it fails.

.. This file was automatic generated / don't edit.

