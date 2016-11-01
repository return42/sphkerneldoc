.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/altera-a10sr.h

.. _`altr_a10sr`:

struct altr_a10sr
=================

.. c:type:: struct altr_a10sr

    Altera Max5 MFD device private data structure

.. _`altr_a10sr.definition`:

Definition
----------

.. code-block:: c

    struct altr_a10sr {
        struct device *dev;
        struct regmap *regmap;
    }

.. _`altr_a10sr.members`:

Members
-------

dev
    : this device

regmap
    the regmap assigned to the parent device.

.. This file was automatic generated / don't edit.

