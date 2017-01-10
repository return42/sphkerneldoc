.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/domain.c

.. _`genpd_queue_power_off_work`:

genpd_queue_power_off_work
==========================

.. c:function:: void genpd_queue_power_off_work(struct generic_pm_domain *genpd)

    Queue up the execution of \ :c:func:`genpd_poweroff`\ .

    :param struct generic_pm_domain \*genpd:
        PM domain to power off.

.. _`genpd_queue_power_off_work.description`:

Description
-----------

Queue up the execution of \ :c:func:`genpd_poweroff`\  unless it's already been done
before.

.. _`genpd_poweron`:

genpd_poweron
=============

.. c:function:: int genpd_poweron(struct generic_pm_domain *genpd, unsigned int depth)

    Restore power to a given PM domain and its masters.

    :param struct generic_pm_domain \*genpd:
        PM domain to power up.

    :param unsigned int depth:
        nesting count for lockdep.

.. _`genpd_poweron.description`:

Description
-----------

Restore power to \ ``genpd``\  and all of its masters so that it is possible to
resume a device belonging to it.

.. _`genpd_poweroff`:

genpd_poweroff
==============

.. c:function:: int genpd_poweroff(struct generic_pm_domain *genpd, bool is_async)

    Remove power from a given PM domain.

    :param struct generic_pm_domain \*genpd:
        PM domain to power down.

    :param bool is_async:
        PM domain is powered down from a scheduled work

.. _`genpd_poweroff.description`:

Description
-----------

If all of the \ ``genpd``\ 's devices have been suspended and all of its subdomains
have been powered down, remove power from \ ``genpd``\ .

.. _`genpd_power_off_work_fn`:

genpd_power_off_work_fn
=======================

.. c:function:: void genpd_power_off_work_fn(struct work_struct *work)

    Power off PM domain whose subdomain count is 0.

    :param struct work_struct \*work:
        Work structure used for scheduling the execution of this function.

.. _`__genpd_runtime_suspend`:

__genpd_runtime_suspend
=======================

.. c:function:: int __genpd_runtime_suspend(struct device *dev)

    walk the hierarchy of ->runtime_suspend() callbacks

    :param struct device \*dev:
        Device to handle.

.. _`__genpd_runtime_resume`:

__genpd_runtime_resume
======================

.. c:function:: int __genpd_runtime_resume(struct device *dev)

    walk the hierarchy of ->runtime_resume() callbacks

    :param struct device \*dev:
        Device to handle.

.. _`genpd_runtime_suspend`:

genpd_runtime_suspend
=====================

.. c:function:: int genpd_runtime_suspend(struct device *dev)

    Suspend a device belonging to I/O PM domain.

    :param struct device \*dev:
        Device to suspend.

.. _`genpd_runtime_suspend.description`:

Description
-----------

Carry out a runtime suspend of a device under the assumption that its
pm_domain field points to the domain member of an object of type
struct generic_pm_domain representing a PM domain consisting of I/O devices.

.. _`genpd_runtime_resume`:

genpd_runtime_resume
====================

.. c:function:: int genpd_runtime_resume(struct device *dev)

    Resume a device belonging to I/O PM domain.

    :param struct device \*dev:
        Device to resume.

.. _`genpd_runtime_resume.description`:

Description
-----------

Carry out a runtime resume of a device under the assumption that its
pm_domain field points to the domain member of an object of type
struct generic_pm_domain representing a PM domain consisting of I/O devices.

.. _`genpd_poweroff_unused`:

genpd_poweroff_unused
=====================

.. c:function:: int genpd_poweroff_unused( void)

    Power off all PM domains with no devices in use.

    :param  void:
        no arguments

.. _`pm_genpd_present`:

pm_genpd_present
================

.. c:function:: bool pm_genpd_present(const struct generic_pm_domain *genpd)

    Check if the given PM domain has been initialized.

    :param const struct generic_pm_domain \*genpd:
        PM domain to check.

.. _`genpd_sync_poweroff`:

genpd_sync_poweroff
===================

.. c:function:: void genpd_sync_poweroff(struct generic_pm_domain *genpd)

    Synchronously power off a PM domain and its masters.

    :param struct generic_pm_domain \*genpd:
        PM domain to power off, if possible.

.. _`genpd_sync_poweroff.description`:

Description
-----------

Check if the given PM domain can be powered off (during system suspend or
hibernation) and do that if so.  Also, in that case propagate to its masters.

This function is only called in "noirq" and "syscore" stages of system power
transitions, so it need not acquire locks (all of the "noirq" callbacks are
executed sequentially, so it is guaranteed that it will never run twice in
parallel).

.. _`genpd_sync_poweron`:

genpd_sync_poweron
==================

.. c:function:: void genpd_sync_poweron(struct generic_pm_domain *genpd)

    Synchronously power on a PM domain and its masters.

    :param struct generic_pm_domain \*genpd:
        PM domain to power on.

.. _`genpd_sync_poweron.description`:

Description
-----------

This function is only called in "noirq" and "syscore" stages of system power
transitions, so it need not acquire locks (all of the "noirq" callbacks are
executed sequentially, so it is guaranteed that it will never run twice in
parallel).

.. _`resume_needed`:

resume_needed
=============

.. c:function:: bool resume_needed(struct device *dev, struct generic_pm_domain *genpd)

    Check whether to resume a device before system suspend.

    :param struct device \*dev:
        Device to check.

    :param struct generic_pm_domain \*genpd:
        PM domain the device belongs to.

.. _`resume_needed.description`:

Description
-----------

There are two cases in which a device that can wake up the system from sleep
states should be resumed by \ :c:func:`pm_genpd_prepare`\ : (1) if the device is enabled
to wake up the system and it has to remain active for this purpose while the
system is in the sleep state and (2) if the device is not enabled to wake up
the system from sleep states and it generally doesn't generate wakeup signals
by itself (those signals are generated on its behalf by other parts of the
system).  In the latter case it may be necessary to reconfigure the device's
wakeup settings during system suspend, because it may have been set up to
signal remote wakeup from the system's working state as needed by runtime PM.
Return 'true' in either of the above cases.

.. _`pm_genpd_prepare`:

pm_genpd_prepare
================

.. c:function:: int pm_genpd_prepare(struct device *dev)

    Start power transition of a device in a PM domain.

    :param struct device \*dev:
        Device to start the transition of.

.. _`pm_genpd_prepare.description`:

Description
-----------

Start a power transition of a device (during a system-wide power transition)
under the assumption that its pm_domain field points to the domain member of
an object of type struct generic_pm_domain representing a PM domain
consisting of I/O devices.

.. _`pm_genpd_suspend_noirq`:

pm_genpd_suspend_noirq
======================

.. c:function:: int pm_genpd_suspend_noirq(struct device *dev)

    Completion of suspend of device in an I/O PM domain.

    :param struct device \*dev:
        Device to suspend.

.. _`pm_genpd_suspend_noirq.description`:

Description
-----------

Stop the device and remove power from the domain if all devices in it have
been stopped.

.. _`pm_genpd_resume_noirq`:

pm_genpd_resume_noirq
=====================

.. c:function:: int pm_genpd_resume_noirq(struct device *dev)

    Start of resume of device in an I/O PM domain.

    :param struct device \*dev:
        Device to resume.

.. _`pm_genpd_resume_noirq.description`:

Description
-----------

Restore power to the device's PM domain, if necessary, and start the device.

.. _`pm_genpd_freeze_noirq`:

pm_genpd_freeze_noirq
=====================

.. c:function:: int pm_genpd_freeze_noirq(struct device *dev)

    Completion of freezing a device in an I/O PM domain.

    :param struct device \*dev:
        Device to freeze.

.. _`pm_genpd_freeze_noirq.description`:

Description
-----------

Carry out a late freeze of a device under the assumption that its
pm_domain field points to the domain member of an object of type
struct generic_pm_domain representing a power domain consisting of I/O
devices.

.. _`pm_genpd_thaw_noirq`:

pm_genpd_thaw_noirq
===================

.. c:function:: int pm_genpd_thaw_noirq(struct device *dev)

    Early thaw of device in an I/O PM domain.

    :param struct device \*dev:
        Device to thaw.

.. _`pm_genpd_thaw_noirq.description`:

Description
-----------

Start the device, unless power has been removed from the domain already
before the system transition.

.. _`pm_genpd_restore_noirq`:

pm_genpd_restore_noirq
======================

.. c:function:: int pm_genpd_restore_noirq(struct device *dev)

    Start of restore of device in an I/O PM domain.

    :param struct device \*dev:
        Device to resume.

.. _`pm_genpd_restore_noirq.description`:

Description
-----------

Make sure the domain will be in the same power state as before the
hibernation the system is resuming from and start the device if necessary.

.. _`pm_genpd_complete`:

pm_genpd_complete
=================

.. c:function:: void pm_genpd_complete(struct device *dev)

    Complete power transition of a device in a power domain.

    :param struct device \*dev:
        Device to complete the transition of.

.. _`pm_genpd_complete.description`:

Description
-----------

Complete a power transition of a device (during a system-wide power
transition) under the assumption that its pm_domain field points to the
domain member of an object of type struct generic_pm_domain representing
a power domain consisting of I/O devices.

.. _`genpd_syscore_switch`:

genpd_syscore_switch
====================

.. c:function:: void genpd_syscore_switch(struct device *dev, bool suspend)

    Switch power during system core suspend or resume.

    :param struct device \*dev:
        Device that normally is marked as "always on" to switch power for.

    :param bool suspend:
        *undescribed*

.. _`genpd_syscore_switch.description`:

Description
-----------

This routine may only be called during the system core (syscore) suspend or
resume phase for devices whose "always on" flags are set.

.. _`__pm_genpd_add_device`:

__pm_genpd_add_device
=====================

.. c:function:: int __pm_genpd_add_device(struct generic_pm_domain *genpd, struct device *dev, struct gpd_timing_data *td)

    Add a device to an I/O PM domain.

    :param struct generic_pm_domain \*genpd:
        PM domain to add the device to.

    :param struct device \*dev:
        Device to be added.

    :param struct gpd_timing_data \*td:
        Set of PM QoS timing parameters to attach to the device.

.. _`pm_genpd_remove_device`:

pm_genpd_remove_device
======================

.. c:function:: int pm_genpd_remove_device(struct generic_pm_domain *genpd, struct device *dev)

    Remove a device from an I/O PM domain.

    :param struct generic_pm_domain \*genpd:
        PM domain to remove the device from.

    :param struct device \*dev:
        Device to be removed.

.. _`pm_genpd_add_subdomain`:

pm_genpd_add_subdomain
======================

.. c:function:: int pm_genpd_add_subdomain(struct generic_pm_domain *genpd, struct generic_pm_domain *subdomain)

    Add a subdomain to an I/O PM domain.

    :param struct generic_pm_domain \*genpd:
        Master PM domain to add the subdomain to.

    :param struct generic_pm_domain \*subdomain:
        Subdomain to be added.

.. _`pm_genpd_remove_subdomain`:

pm_genpd_remove_subdomain
=========================

.. c:function:: int pm_genpd_remove_subdomain(struct generic_pm_domain *genpd, struct generic_pm_domain *subdomain)

    Remove a subdomain from an I/O PM domain.

    :param struct generic_pm_domain \*genpd:
        Master PM domain to remove the subdomain from.

    :param struct generic_pm_domain \*subdomain:
        Subdomain to be removed.

.. _`pm_genpd_init`:

pm_genpd_init
=============

.. c:function:: int pm_genpd_init(struct generic_pm_domain *genpd, struct dev_power_governor *gov, bool is_off)

    Initialize a generic I/O PM domain object.

    :param struct generic_pm_domain \*genpd:
        PM domain object to initialize.

    :param struct dev_power_governor \*gov:
        PM domain governor to associate with the domain (may be NULL).

    :param bool is_off:
        Initial value of the domain's power_is_off field.

.. _`pm_genpd_init.description`:

Description
-----------

Returns 0 on successful initialization, else a negative error code.

.. _`pm_genpd_remove`:

pm_genpd_remove
===============

.. c:function:: int pm_genpd_remove(struct generic_pm_domain *genpd)

    Remove a generic I/O PM domain

    :param struct generic_pm_domain \*genpd:
        Pointer to PM domain that is to be removed.

.. _`pm_genpd_remove.description`:

Description
-----------

To remove the PM domain, this function:
- Removes the PM domain as a subdomain to any parent domains,
if it was added.
- Removes the PM domain from the list of registered PM domains.

The PM domain will only be removed, if the associated provider has
been removed, it is not a parent to any other PM domain and has no
devices associated with it.

.. _`of_genpd_provider`:

struct of_genpd_provider
========================

.. c:type:: struct of_genpd_provider

    PM domain provider registration structure

.. _`of_genpd_provider.definition`:

Definition
----------

.. code-block:: c

    struct of_genpd_provider {
        struct list_head link;
        struct device_node *node;
        genpd_xlate_t xlate;
        void *data;
    }

.. _`of_genpd_provider.members`:

Members
-------

link
    Entry in global list of PM domain providers

node
    Pointer to device tree node of PM domain provider

xlate
    Provider-specific xlate callback mapping a set of specifier cells
    into a PM domain.

data
    context pointer to be passed into \ ``xlate``\  callback

.. _`genpd_xlate_simple`:

genpd_xlate_simple
==================

.. c:function:: struct generic_pm_domain *genpd_xlate_simple(struct of_phandle_args *genpdspec, void *data)

    Xlate function for direct node-domain mapping

    :param struct of_phandle_args \*genpdspec:
        OF phandle args to map into a PM domain

    :param void \*data:
        xlate function private data - pointer to struct generic_pm_domain

.. _`genpd_xlate_simple.description`:

Description
-----------

This is a generic xlate function that can be used to model PM domains that
have their own device tree nodes. The private data of xlate function needs
to be a valid pointer to struct generic_pm_domain.

.. _`genpd_xlate_onecell`:

genpd_xlate_onecell
===================

.. c:function:: struct generic_pm_domain *genpd_xlate_onecell(struct of_phandle_args *genpdspec, void *data)

    Xlate function using a single index.

    :param struct of_phandle_args \*genpdspec:
        OF phandle args to map into a PM domain

    :param void \*data:
        xlate function private data - pointer to struct genpd_onecell_data

.. _`genpd_xlate_onecell.description`:

Description
-----------

This is a generic xlate function that can be used to model simple PM domain
controllers that have one device tree node and provide multiple PM domains.
A single cell is used as an index into an array of PM domains specified in
the genpd_onecell_data struct when registering the provider.

.. _`genpd_add_provider`:

genpd_add_provider
==================

.. c:function:: int genpd_add_provider(struct device_node *np, genpd_xlate_t xlate, void *data)

    Register a PM domain provider for a node

    :param struct device_node \*np:
        Device node pointer associated with the PM domain provider.

    :param genpd_xlate_t xlate:
        Callback for decoding PM domain from phandle arguments.

    :param void \*data:
        Context pointer for \ ``xlate``\  callback.

.. _`of_genpd_add_provider_simple`:

of_genpd_add_provider_simple
============================

.. c:function:: int of_genpd_add_provider_simple(struct device_node *np, struct generic_pm_domain *genpd)

    Register a simple PM domain provider

    :param struct device_node \*np:
        Device node pointer associated with the PM domain provider.

    :param struct generic_pm_domain \*genpd:
        Pointer to PM domain associated with the PM domain provider.

.. _`of_genpd_add_provider_onecell`:

of_genpd_add_provider_onecell
=============================

.. c:function:: int of_genpd_add_provider_onecell(struct device_node *np, struct genpd_onecell_data *data)

    Register a onecell PM domain provider

    :param struct device_node \*np:
        Device node pointer associated with the PM domain provider.

    :param struct genpd_onecell_data \*data:
        Pointer to the data associated with the PM domain provider.

.. _`of_genpd_del_provider`:

of_genpd_del_provider
=====================

.. c:function:: void of_genpd_del_provider(struct device_node *np)

    Remove a previously registered PM domain provider

    :param struct device_node \*np:
        Device node pointer associated with the PM domain provider

.. _`genpd_get_from_provider`:

genpd_get_from_provider
=======================

.. c:function:: struct generic_pm_domain *genpd_get_from_provider(struct of_phandle_args *genpdspec)

    Look-up PM domain

    :param struct of_phandle_args \*genpdspec:
        OF phandle args to use for look-up

.. _`genpd_get_from_provider.description`:

Description
-----------

Looks for a PM domain provider under the node specified by \ ``genpdspec``\  and if
found, uses xlate function of the provider to map phandle args to a PM
domain.

Returns a valid pointer to struct generic_pm_domain on success or \ :c:func:`ERR_PTR`\ 
on failure.

.. _`of_genpd_add_device`:

of_genpd_add_device
===================

.. c:function:: int of_genpd_add_device(struct of_phandle_args *genpdspec, struct device *dev)

    Add a device to an I/O PM domain

    :param struct of_phandle_args \*genpdspec:
        OF phandle args to use for look-up PM domain

    :param struct device \*dev:
        Device to be added.

.. _`of_genpd_add_device.description`:

Description
-----------

Looks-up an I/O PM domain based upon phandle args provided and adds
the device to the PM domain. Returns a negative error code on failure.

.. _`of_genpd_add_subdomain`:

of_genpd_add_subdomain
======================

.. c:function:: int of_genpd_add_subdomain(struct of_phandle_args *parent_spec, struct of_phandle_args *subdomain_spec)

    Add a subdomain to an I/O PM domain.

    :param struct of_phandle_args \*parent_spec:
        OF phandle args to use for parent PM domain look-up

    :param struct of_phandle_args \*subdomain_spec:
        OF phandle args to use for subdomain look-up

.. _`of_genpd_add_subdomain.description`:

Description
-----------

Looks-up a parent PM domain and subdomain based upon phandle args
provided and adds the subdomain to the parent PM domain. Returns a
negative error code on failure.

.. _`of_genpd_remove_last`:

of_genpd_remove_last
====================

.. c:function:: struct generic_pm_domain *of_genpd_remove_last(struct device_node *np)

    Remove the last PM domain registered for a provider

    :param struct device_node \*np:
        *undescribed*

.. _`of_genpd_remove_last.description`:

Description
-----------

Find the last PM domain that was added by a particular provider and
remove this PM domain from the list of PM domains. The provider is
identified by the 'provider' device structure that is passed. The PM
domain will only be removed, if the provider associated with domain
has been removed.

Returns a valid pointer to struct generic_pm_domain on success or
\ :c:func:`ERR_PTR`\  on failure.

.. _`genpd_dev_pm_detach`:

genpd_dev_pm_detach
===================

.. c:function:: void genpd_dev_pm_detach(struct device *dev, bool power_off)

    Detach a device from its PM domain.

    :param struct device \*dev:
        Device to detach.

    :param bool power_off:
        Currently not used

.. _`genpd_dev_pm_detach.description`:

Description
-----------

Try to locate a corresponding generic PM domain, which the device was
attached to previously. If such is found, the device is detached from it.

.. _`genpd_dev_pm_attach`:

genpd_dev_pm_attach
===================

.. c:function:: int genpd_dev_pm_attach(struct device *dev)

    Attach a device to its PM domain using DT.

    :param struct device \*dev:
        Device to attach.

.. _`genpd_dev_pm_attach.description`:

Description
-----------

Parse device's OF node to find a PM domain specifier. If such is found,
attaches the device to retrieved pm_domain ops.

Both generic and legacy Samsung-specific DT bindings are supported to keep
backwards compatibility with existing DTBs.

Returns 0 on successfully attached PM domain or negative error code. Note
that if a power-domain exists for the device, but it cannot be found or
turned on, then return -EPROBE_DEFER to ensure that the device is not
probed and to re-try again later.

.. _`of_genpd_parse_idle_states`:

of_genpd_parse_idle_states
==========================

.. c:function:: int of_genpd_parse_idle_states(struct device_node *dn, struct genpd_power_state **states, int *n)

    Return array of idle states for the genpd.

    :param struct device_node \*dn:
        The genpd device node

    :param struct genpd_power_state \*\*states:
        The pointer to which the state array will be saved.

    :param int \*n:
        The count of elements in the array returned from this function.

.. _`of_genpd_parse_idle_states.description`:

Description
-----------

Returns the device states parsed from the OF node. The memory for the states
is allocated by this function and is the responsibility of the caller to
free the memory after use.

.. This file was automatic generated / don't edit.

