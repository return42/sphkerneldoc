.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hwtracing/coresight/coresight-replicator.c

.. _`replicator_drvdata`:

struct replicator_drvdata
=========================

.. c:type:: struct replicator_drvdata

    specifics associated to a replicator component

.. _`replicator_drvdata.definition`:

Definition
----------

.. code-block:: c

    struct replicator_drvdata {
        struct device *dev;
        struct clk *atclk;
        struct coresight_device *csdev;
    }

.. _`replicator_drvdata.members`:

Members
-------

dev
    the device entity associated with this component

atclk
    optional clock for the core parts of the replicator.

csdev
    component vitals needed by the framework

.. This file was automatic generated / don't edit.

