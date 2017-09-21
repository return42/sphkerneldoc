.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/domain_governor.c

.. _`default_suspend_ok`:

default_suspend_ok
==================

.. c:function:: bool default_suspend_ok(struct device *dev)

    Default PM domain governor routine to suspend devices.

    :param struct device \*dev:
        Device to check.

.. _`default_power_down_ok`:

default_power_down_ok
=====================

.. c:function:: bool default_power_down_ok(struct dev_pm_domain *pd)

    Default generic PM domain power off governor routine.

    :param struct dev_pm_domain \*pd:
        PM domain to check.

.. _`default_power_down_ok.description`:

Description
-----------

This routine must be executed under the PM domain's lock.

.. This file was automatic generated / don't edit.

