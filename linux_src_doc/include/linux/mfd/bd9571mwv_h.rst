.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/bd9571mwv.h

.. _`bd9571mwv`:

struct bd9571mwv
================

.. c:type:: struct bd9571mwv

    state holder for the bd9571mwv driver

.. _`bd9571mwv.definition`:

Definition
----------

.. code-block:: c

    struct bd9571mwv {
        struct device *dev;
        struct regmap *regmap;
        int irq;
        struct regmap_irq_chip_data *irq_data;
    }

.. _`bd9571mwv.members`:

Members
-------

dev
    *undescribed*

regmap
    *undescribed*

irq
    *undescribed*

irq_data
    *undescribed*

.. _`bd9571mwv.description`:

Description
-----------

Device data may be used to access the BD9571MWV chip

.. This file was automatic generated / don't edit.

