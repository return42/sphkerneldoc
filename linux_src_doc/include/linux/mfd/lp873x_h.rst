.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/lp873x.h

.. _`lp873x`:

struct lp873x
=============

.. c:type:: struct lp873x

    state holder for the lp873x driver

.. _`lp873x.definition`:

Definition
----------

.. code-block:: c

    struct lp873x {
        struct device *dev;
        u8 rev;
        struct regmap *regmap;
    }

.. _`lp873x.members`:

Members
-------

dev
    struct device pointer for MFD device

rev
    revision of the lp873x

regmap
    register map of the lp873x PMIC

.. _`lp873x.description`:

Description
-----------

Device data may be used to access the LP873X chip

.. This file was automatic generated / don't edit.

