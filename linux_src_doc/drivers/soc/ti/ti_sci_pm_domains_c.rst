.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/ti/ti_sci_pm_domains.c

.. _`ti_sci_genpd_dev_data`:

struct ti_sci_genpd_dev_data
============================

.. c:type:: struct ti_sci_genpd_dev_data

    holds data needed for every device attached to this genpd

.. _`ti_sci_genpd_dev_data.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_genpd_dev_data {
        int idx;
    }

.. _`ti_sci_genpd_dev_data.members`:

Members
-------

idx
    index of the device that identifies it with the system
    control processor.

.. _`ti_sci_pm_domain`:

struct ti_sci_pm_domain
=======================

.. c:type:: struct ti_sci_pm_domain

    TI specific data needed for power domain

.. _`ti_sci_pm_domain.definition`:

Definition
----------

.. code-block:: c

    struct ti_sci_pm_domain {
        const struct ti_sci_handle *ti_sci;
        struct device *dev;
        struct generic_pm_domain pd;
    }

.. _`ti_sci_pm_domain.members`:

Members
-------

ti_sci
    handle to TI SCI protocol driver that provides ops to
    communicate with system control processor.

dev
    pointer to dev for the driver for devm allocs

pd
    generic_pm_domain for use with the genpd framework

.. _`ti_sci_dev_id`:

ti_sci_dev_id
=============

.. c:function:: int ti_sci_dev_id(struct device *dev)

    get prepopulated ti_sci id from struct dev

    :param dev:
        pointer to device associated with this genpd
    :type dev: struct device \*

.. _`ti_sci_dev_id.description`:

Description
-----------

Returns device_id stored from ti,sci_id property

.. _`ti_sci_dev_to_sci_handle`:

ti_sci_dev_to_sci_handle
========================

.. c:function:: const struct ti_sci_handle *ti_sci_dev_to_sci_handle(struct device *dev)

    get pointer to ti_sci_handle

    :param dev:
        pointer to device associated with this genpd
    :type dev: struct device \*

.. _`ti_sci_dev_to_sci_handle.description`:

Description
-----------

Returns ti_sci_handle to be used to communicate with system
control processor.

.. _`ti_sci_dev_start`:

ti_sci_dev_start
================

.. c:function:: int ti_sci_dev_start(struct device *dev)

    genpd device start hook called to turn device on

    :param dev:
        pointer to device associated with this genpd to be powered on
    :type dev: struct device \*

.. _`ti_sci_dev_stop`:

ti_sci_dev_stop
===============

.. c:function:: int ti_sci_dev_stop(struct device *dev)

    genpd device stop hook called to turn device off

    :param dev:
        pointer to device associated with this genpd to be powered off
    :type dev: struct device \*

.. This file was automatic generated / don't edit.

