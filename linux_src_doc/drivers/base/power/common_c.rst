.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/common.c

.. _`dev_pm_get_subsys_data`:

dev_pm_get_subsys_data
======================

.. c:function:: int dev_pm_get_subsys_data(struct device *dev)

    Create or refcount power.subsys_data for device.

    :param struct device \*dev:
        Device to handle.

.. _`dev_pm_get_subsys_data.description`:

Description
-----------

If power.subsys_data is NULL, point it to a new object, otherwise increment
its reference counter.  Return 0 if new object has been created or refcount
increased, otherwise negative error code.

.. _`dev_pm_put_subsys_data`:

dev_pm_put_subsys_data
======================

.. c:function:: void dev_pm_put_subsys_data(struct device *dev)

    Drop reference to power.subsys_data.

    :param struct device \*dev:
        Device to handle.

.. _`dev_pm_put_subsys_data.description`:

Description
-----------

If the reference counter of power.subsys_data is zero after dropping the
reference, power.subsys_data is removed.

.. _`dev_pm_domain_attach`:

dev_pm_domain_attach
====================

.. c:function:: int dev_pm_domain_attach(struct device *dev, bool power_on)

    Attach a device to its PM domain.

    :param struct device \*dev:
        Device to attach.

    :param bool power_on:
        Used to indicate whether we should power on the device.

.. _`dev_pm_domain_attach.description`:

Description
-----------

The \ ``dev``\  may only be attached to a single PM domain. By iterating through
the available alternatives we try to find a valid PM domain for the device.
As attachment succeeds, the ->detach() callback in the struct dev_pm_domain
should be assigned by the corresponding attach function.

This function should typically be invoked from subsystem level code during
the probe phase. Especially for those that holds devices which requires
power management through PM domains.

Callers must ensure proper synchronization of this function with power
management callbacks.

Returns 0 on successfully attached PM domain, or when it is found that the
device doesn't need a PM domain, else a negative error code.

.. _`dev_pm_domain_attach_by_id`:

dev_pm_domain_attach_by_id
==========================

.. c:function:: struct device *dev_pm_domain_attach_by_id(struct device *dev, unsigned int index)

    Associate a device with one of its PM domains.

    :param struct device \*dev:
        The device used to lookup the PM domain.

    :param unsigned int index:
        The index of the PM domain.

.. _`dev_pm_domain_attach_by_id.description`:

Description
-----------

As \ ``dev``\  may only be attached to a single PM domain, the backend PM domain
provider creates a virtual device to attach instead. If attachment succeeds,
the ->detach() callback in the struct dev_pm_domain are assigned by the
corresponding backend attach function, as to deal with detaching of the
created virtual device.

This function should typically be invoked by a driver during the probe phase,
in case its device requires power management through multiple PM domains. The
driver may benefit from using the received device, to configure device-links
towards its original device. Depending on the use-case and if needed, the
links may be dynamically changed by the driver, which allows it to control
the power to the PM domains independently from each other.

Callers must ensure proper synchronization of this function with power
management callbacks.

Returns the virtual created device when successfully attached to its PM
domain, NULL in case \ ``dev``\  don't need a PM domain, else an \ :c:func:`ERR_PTR`\ .
Note that, to detach the returned virtual device, the driver shall call
\ :c:func:`dev_pm_domain_detach`\  on it, typically during the remove phase.

.. _`dev_pm_domain_detach`:

dev_pm_domain_detach
====================

.. c:function:: void dev_pm_domain_detach(struct device *dev, bool power_off)

    Detach a device from its PM domain.

    :param struct device \*dev:
        Device to detach.

    :param bool power_off:
        Used to indicate whether we should power off the device.

.. _`dev_pm_domain_detach.description`:

Description
-----------

This functions will reverse the actions from \ :c:func:`dev_pm_domain_attach`\  and
\ :c:func:`dev_pm_domain_attach_by_id`\ , thus it detaches \ ``dev``\  from its PM domain.
Typically it should be invoked during the remove phase, either from
subsystem level code or from drivers.

Callers must ensure proper synchronization of this function with power
management callbacks.

.. _`dev_pm_domain_set`:

dev_pm_domain_set
=================

.. c:function:: void dev_pm_domain_set(struct device *dev, struct dev_pm_domain *pd)

    Set PM domain of a device.

    :param struct device \*dev:
        Device whose PM domain is to be set.

    :param struct dev_pm_domain \*pd:
        PM domain to be set, or NULL.

.. _`dev_pm_domain_set.description`:

Description
-----------

Sets the PM domain the device belongs to. The PM domain of a device needs
to be set before its probe finishes (it's bound to a driver).

This function must be called with the device lock held.

.. This file was automatic generated / don't edit.

