.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-replicator-qcom.c

.. _`replicator_state`:

struct replicator_state
=======================

.. c:type:: struct replicator_state

    specifics associated to a replicator component

.. _`replicator_state.definition`:

Definition
----------

.. code-block:: c

    struct replicator_state {
        void __iomem *base;
        struct device *dev;
        struct clk *atclk;
        struct coresight_device *csdev;
    }

.. _`replicator_state.members`:

Members
-------

base
    memory mapped base address for this component.

dev
    the device entity associated with this component

atclk
    optional clock for the core parts of the replicator.

csdev
    component vitals needed by the framework

.. This file was automatic generated / don't edit.

