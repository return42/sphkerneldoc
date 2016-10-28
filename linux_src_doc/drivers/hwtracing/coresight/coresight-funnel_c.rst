.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-funnel.c

.. _`funnel_drvdata`:

struct funnel_drvdata
=====================

.. c:type:: struct funnel_drvdata

    specifics associated to a funnel component

.. _`funnel_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct funnel_drvdata {
        void __iomem *base;
        struct device *dev;
        struct clk *atclk;
        struct coresight_device *csdev;
        unsigned long priority;
    }

.. _`funnel_drvdata.members`:

Members
-------

base
    memory mapped base address for this component.

dev
    the device entity associated to this component.

atclk
    optional clock for the core parts of the funnel.

csdev
    component vitals needed by the framework.

priority
    port selection order.

.. This file was automatic generated / don't edit.

