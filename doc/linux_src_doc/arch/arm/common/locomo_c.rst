.. -*- coding: utf-8; mode: rst -*-

========
locomo.c
========


.. _`__locomo_probe`:

__locomo_probe
==============

.. c:function:: int __locomo_probe (struct device *me, struct resource *mem, int irq)

    probe for a single LoCoMo chip.

    :param struct device \*me:

        *undescribed*

    :param struct resource \*mem:

        *undescribed*

    :param int irq:

        *undescribed*



.. _`__locomo_probe.description`:

Description
-----------

Probe for a LoCoMo chip.  This must be called
before any other locomo-specific code.



.. _`__locomo_probe.returns`:

Returns
-------

``-ENODEV``        device not found.
``-EBUSY``                physical address already marked in-use.
``0``                successful.

