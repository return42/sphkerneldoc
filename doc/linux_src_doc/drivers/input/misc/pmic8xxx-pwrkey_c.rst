.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/misc/pmic8xxx-pwrkey.c

.. _`pmic8xxx_pwrkey`:

struct pmic8xxx_pwrkey
======================

.. c:type:: struct pmic8xxx_pwrkey

    pmic8xxx pwrkey information

.. _`pmic8xxx_pwrkey.definition`:

Definition
----------

.. code-block:: c

    struct pmic8xxx_pwrkey {
        int key_press_irq;
        struct regmap *regmap;
        int (*shutdown_fn)(struct pmic8xxx_pwrkey *, bool);
    }

.. _`pmic8xxx_pwrkey.members`:

Members
-------

key_press_irq
    key press irq number

regmap
    device regmap

shutdown_fn
    shutdown configuration function

.. This file was automatic generated / don't edit.

