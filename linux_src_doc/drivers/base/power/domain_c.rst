.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/domain.c

.. _`dev_pm_genpd_set_performance_state`:

dev_pm_genpd_set_performance_state
==================================

.. c:function:: int dev_pm_genpd_set_performance_state(struct device *dev, unsigned int state)

    Set performance state of device's power domain.

    :param dev:
        Device for which the performance-state needs to be set.
    :type dev: struct device \*

    :param state:
        Target performance state of the device. This can be set as 0 when the
        device doesn't have any performance state constraints left (And so
        the device wouldn't participate anymore to find the target
        performance state of the genpd).
    :type state: unsigned int

.. _`dev_pm_genpd_set_performance_state.description`:

Description
-----------

It is assumed that the users guarantee that the genpd wouldn't be detached
while this routine is getting called.

Returns 0 on success and negative error values on failures.

.. _`genpd_queue_power_off_work`:

genpd_queue_power_off_work
==========================

.. c:function:: void genpd_queue_power_off_work(struct generic_pm_domain *genpd)

    Queue up the execution of \ :c:func:`genpd_power_off`\ .

    :param genpd:
        PM domain to power off.
    :type genpd: struct generic_pm_domain \*

.. _`genpd_queue_power_off_work.description`:

Description
-----------

Queue up the execution of \ :c:func:`genpd_power_off`\  unless it's already been done
before.

.. _`genpd_power_off`:

genpd_power_off
===============

.. c:function:: int genpd_power_off(struct generic_pm_domain *genpd, bool one_dev_on, unsigned int depth)

    Remove power from a given PM domain.

    :param genpd:
        PM domain to power down.
    :type genpd: struct generic_pm_domain \*

    :param one_dev_on:
        If invoked from genpd's ->runtime_suspend\|resume() callback, the
        RPM status of the releated device is in an intermediate state, not yet turned
        into RPM_SUSPENDED. This means \ :c:func:`genpd_power_off`\  must allow one device to not
        be RPM_SUSPENDED, while it tries to power off the PM domain.
    :type one_dev_on: bool

    :param depth:
        *undescribed*
    :type depth: unsigned int

.. _`genpd_power_off.description`:

Description
-----------

If all of the \ ``genpd``\ 's devices have been suspended and all of its subdomains
have been powered down, remove power from \ ``genpd``\ .

.. _`genpd_power_on`:

genpd_power_on
==============

.. c:function:: int genpd_power_on(struct generic_pm_domain *genpd, unsigned int depth)

    Restore power to a given PM domain and its masters.

    :param genpd:
        PM domain to power up.
    :type genpd: struct generic_pm_domain \*

    :param depth:
        nesting count for lockdep.
    :type depth: unsigned int

.. _`genpd_power_on.description`:

Description
-----------

Restore power to \ ``genpd``\  and all of its masters so that it is possible to
resume a device belonging to it.

.. _`genpd_power_off_work_fn`:

genpd_power_off_work_fn
=======================

.. c:function:: void genpd_power_off_work_fn(struct work_struct *work)

    Power off PM domain whose subdomain count is 0.

    :param work:
        Work structure used for scheduling the execution of this function.
    :type work: struct work_struct \*

.. _`__genpd_runtime_suspend`:

\__genpd_runtime_suspend
========================

.. c:function:: int __genpd_runtime_suspend(struct device *dev)

    walk the hierarchy of ->runtime_suspend() callbacks

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`__genpd_runtime_resume`:

\__genpd_runtime_resume
=======================

.. c:function:: int __genpd_runtime_resume(struct device *dev)

    walk the hierarchy of ->runtime_resume() callbacks

    :param dev:
        Device to handle.
    :type dev: struct device \*

.. _`genpd_runtime_suspend`:

genpd_runtime_suspend
=====================

.. c:function:: int genpd_runtime_suspend(struct device *dev)

    Suspend a device belonging to I/O PM domain.

    :param dev:
        Device to suspend.
    :type dev: struct device \*

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

    :param dev:
        Device to resume.
    :type dev: struct device \*

.. _`genpd_runtime_resume.description`:

Description
-----------

Carry out a runtime resume of a device under the assumption that its
pm_domain field points to the domain member of an object of type
struct generic_pm_domain representing a PM domain consisting of I/O devices.

.. _`genpd_power_off_unused`:

genpd_power_off_unused
======================

.. c:function:: int genpd_power_off_unused( void)

    Power off all PM domains with no devices in use.

    :param void:
        no arguments
    :type void: 

.. _`genpd_sync_power_off`:

genpd_sync_power_off
====================

.. c:function:: void genpd_sync_power_off(struct generic_pm_domain *genpd, bool use_lock, unsigned int depth)

    Synchronously power off a PM domain and its masters.

    :param genpd:
        PM domain to power off, if possible.
    :type genpd: struct generic_pm_domain \*

    :param use_lock:
        use the lock.
    :type use_lock: bool

    :param depth:
        nesting count for lockdep.
    :type depth: unsigned int

.. _`genpd_sync_power_off.description`:

Description
-----------

Check if the given PM domain can be powered off (during system suspend or
hibernation) and do that if so.  Also, in that case propagate to its masters.

This function is only called in "noirq" and "syscore" stages of system power
transitions. The "noirq" callbacks may be executed asynchronously, thus in
these cases the lock must be held.

.. _`genpd_sync_power_on`:

genpd_sync_power_on
===================

.. c:function:: void genpd_sync_power_on(struct generic_pm_domain *genpd, bool use_lock, unsigned int depth)

    Synchronously power on a PM domain and its masters.

    :param genpd:
        PM domain to power on.
    :type genpd: struct generic_pm_domain \*

    :param use_lock:
        use the lock.
    :type use_lock: bool

    :param depth:
        nesting count for lockdep.
    :type depth: unsigned int

.. _`genpd_sync_power_on.description`:

Description
-----------

This function is only called in "noirq" and "syscore" stages of system power
transitions. The "noirq" callbacks may be executed asynchronously, thus in
these cases the lock must be held.

.. _`resume_needed`:

resume_needed
=============

.. c:function:: bool resume_needed(struct device *dev, const struct generic_pm_domain *genpd)

    Check whether to resume a device before system suspend.

    :param dev:
        Device to check.
    :type dev: struct device \*

    :param genpd:
        PM domain the device belongs to.
    :type genpd: const struct generic_pm_domain \*

.. _`resume_needed.description`:

Description
-----------

There are two cases in which a device that can wake up the system from sleep
states should be resumed by \ :c:func:`genpd_prepare`\ : (1) if the device is enabled
to wake up the system and it has to remain active for this purpose while the
system is in the sleep state and (2) if the device is not enabled to wake up
the system from sleep states and it generally doesn't generate wakeup signals
by itself (those signals are generated on its behalf by other parts of the
system).  In the latter case it may be necessary to reconfigure the device's
wakeup settings during system suspend, because it may have been set up to
signal remote wakeup from the system's working state as needed by runtime PM.
Return 'true' in either of the above cases.

.. _`genpd_prepare`:

genpd_prepare
=============

.. c:function:: int genpd_prepare(struct device *dev)

    Start power transition of a device in a PM domain.

    :param dev:
        Device to start the transition of.
    :type dev: struct device \*

.. _`genpd_prepare.description`:

Description
-----------

Start a power transition of a device (during a system-wide power transition)
under the assumption that its pm_domain field points to the domain member of
an object of type struct generic_pm_domain representing a PM domain
consisting of I/O devices.

.. _`genpd_finish_suspend`:

genpd_finish_suspend
====================

.. c:function:: int genpd_finish_suspend(struct device *dev, bool poweroff)

    Completion of suspend or hibernation of device in an I/O pm domain.

    :param dev:
        Device to suspend.
    :type dev: struct device \*

    :param poweroff:
        Specifies if this is a poweroff_noirq or suspend_noirq callback.
    :type poweroff: bool

.. _`genpd_finish_suspend.description`:

Description
-----------

Stop the device and remove power from the domain if all devices in it have
been stopped.

.. _`genpd_suspend_noirq`:

genpd_suspend_noirq
===================

.. c:function:: int genpd_suspend_noirq(struct device *dev)

    Completion of suspend of device in an I/O PM domain.

    :param dev:
        Device to suspend.
    :type dev: struct device \*

.. _`genpd_suspend_noirq.description`:

Description
-----------

Stop the device and remove power from the domain if all devices in it have
been stopped.

.. _`genpd_resume_noirq`:

genpd_resume_noirq
==================

.. c:function:: int genpd_resume_noirq(struct device *dev)

    Start of resume of device in an I/O PM domain.

    :param dev:
        Device to resume.
    :type dev: struct device \*

.. _`genpd_resume_noirq.description`:

Description
-----------

Restore power to the device's PM domain, if necessary, and start the device.

.. _`genpd_freeze_noirq`:

genpd_freeze_noirq
==================

.. c:function:: int genpd_freeze_noirq(struct device *dev)

    Completion of freezing a device in an I/O PM domain.

    :param dev:
        Device to freeze.
    :type dev: struct device \*

.. _`genpd_freeze_noirq.description`:

Description
-----------

Carry out a late freeze of a device under the assumption that its
pm_domain field points to the domain member of an object of type
struct generic_pm_domain representing a power domain consisting of I/O
devices.

.. _`genpd_thaw_noirq`:

genpd_thaw_noirq
================

.. c:function:: int genpd_thaw_noirq(struct device *dev)

    Early thaw of device in an I/O PM domain.

    :param dev:
        Device to thaw.
    :type dev: struct device \*

.. _`genpd_thaw_noirq.description`:

Description
-----------

Start the device, unless power has been removed from the domain already
before the system transition.

.. _`genpd_poweroff_noirq`:

genpd_poweroff_noirq
====================

.. c:function:: int genpd_poweroff_noirq(struct device *dev)

    Completion of hibernation of device in an I/O PM domain.

    :param dev:
        Device to poweroff.
    :type dev: struct device \*

.. _`genpd_poweroff_noirq.description`:

Description
-----------

Stop the device and remove power from the domain if all devices in it have
been stopped.

.. _`genpd_restore_noirq`:

genpd_restore_noirq
===================

.. c:function:: int genpd_restore_noirq(struct device *dev)

    Start of restore of device in an I/O PM domain.

    :param dev:
        Device to resume.
    :type dev: struct device \*

.. _`genpd_restore_noirq.description`:

Description
-----------

Make sure the domain will be in the same power state as before the
hibernation the system is resuming from and start the device if necessary.

.. _`genpd_complete`:

genpd_complete
==============

.. c:function:: void genpd_complete(struct device *dev)

    Complete power transition of a device in a power domain.

    :param dev:
        Device to complete the transition of.
    :type dev: struct device \*

.. _`genpd_complete.description`:

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

    :param dev:
        Device that normally is marked as "always on" to switch power for.
    :type dev: struct device \*

    :param suspend:
        *undescribed*
    :type suspend: bool

.. _`genpd_syscore_switch.description`:

Description
-----------

This routine may only be called during the system core (syscore) suspend or
resume phase for devices whose "always on" flags are set.

.. _`pm_genpd_add_device`:

pm_genpd_add_device
===================

.. c:function:: int pm_genpd_add_device(struct generic_pm_domain *genpd, struct device *dev)

    Add a device to an I/O PM domain.

    :param genpd:
        PM domain to add the device to.
    :type genpd: struct generic_pm_domain \*

    :param dev:
        Device to be added.
    :type dev: struct device \*

.. _`pm_genpd_remove_device`:

pm_genpd_remove_device
======================

.. c:function:: int pm_genpd_remove_device(struct device *dev)

    Remove a device from an I/O PM domain.

    :param dev:
        Device to be removed.
    :type dev: struct device \*

.. _`pm_genpd_add_subdomain`:

pm_genpd_add_subdomain
======================

.. c:function:: int pm_genpd_add_subdomain(struct generic_pm_domain *genpd, struct generic_pm_domain *subdomain)

    Add a subdomain to an I/O PM domain.

    :param genpd:
        Master PM domain to add the subdomain to.
    :type genpd: struct generic_pm_domain \*

    :param subdomain:
        Subdomain to be added.
    :type subdomain: struct generic_pm_domain \*

.. _`pm_genpd_remove_subdomain`:

pm_genpd_remove_subdomain
=========================

.. c:function:: int pm_genpd_remove_subdomain(struct generic_pm_domain *genpd, struct generic_pm_domain *subdomain)

    Remove a subdomain from an I/O PM domain.

    :param genpd:
        Master PM domain to remove the subdomain from.
    :type genpd: struct generic_pm_domain \*

    :param subdomain:
        Subdomain to be removed.
    :type subdomain: struct generic_pm_domain \*

.. _`pm_genpd_init`:

pm_genpd_init
=============

.. c:function:: int pm_genpd_init(struct generic_pm_domain *genpd, struct dev_power_governor *gov, bool is_off)

    Initialize a generic I/O PM domain object.

    :param genpd:
        PM domain object to initialize.
    :type genpd: struct generic_pm_domain \*

    :param gov:
        PM domain governor to associate with the domain (may be NULL).
    :type gov: struct dev_power_governor \*

    :param is_off:
        Initial value of the domain's power_is_off field.
    :type is_off: bool

.. _`pm_genpd_init.description`:

Description
-----------

Returns 0 on successful initialization, else a negative error code.

.. _`pm_genpd_remove`:

pm_genpd_remove
===============

.. c:function:: int pm_genpd_remove(struct generic_pm_domain *genpd)

    Remove a generic I/O PM domain

    :param genpd:
        Pointer to PM domain that is to be removed.
    :type genpd: struct generic_pm_domain \*

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

    :param genpdspec:
        OF phandle args to map into a PM domain
    :type genpdspec: struct of_phandle_args \*

    :param data:
        xlate function private data - pointer to struct generic_pm_domain
    :type data: void \*

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

    :param genpdspec:
        OF phandle args to map into a PM domain
    :type genpdspec: struct of_phandle_args \*

    :param data:
        xlate function private data - pointer to struct genpd_onecell_data
    :type data: void \*

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

    :param np:
        Device node pointer associated with the PM domain provider.
    :type np: struct device_node \*

    :param xlate:
        Callback for decoding PM domain from phandle arguments.
    :type xlate: genpd_xlate_t

    :param data:
        Context pointer for \ ``xlate``\  callback.
    :type data: void \*

.. _`of_genpd_add_provider_simple`:

of_genpd_add_provider_simple
============================

.. c:function:: int of_genpd_add_provider_simple(struct device_node *np, struct generic_pm_domain *genpd)

    Register a simple PM domain provider

    :param np:
        Device node pointer associated with the PM domain provider.
    :type np: struct device_node \*

    :param genpd:
        Pointer to PM domain associated with the PM domain provider.
    :type genpd: struct generic_pm_domain \*

.. _`of_genpd_add_provider_onecell`:

of_genpd_add_provider_onecell
=============================

.. c:function:: int of_genpd_add_provider_onecell(struct device_node *np, struct genpd_onecell_data *data)

    Register a onecell PM domain provider

    :param np:
        Device node pointer associated with the PM domain provider.
    :type np: struct device_node \*

    :param data:
        Pointer to the data associated with the PM domain provider.
    :type data: struct genpd_onecell_data \*

.. _`of_genpd_del_provider`:

of_genpd_del_provider
=====================

.. c:function:: void of_genpd_del_provider(struct device_node *np)

    Remove a previously registered PM domain provider

    :param np:
        Device node pointer associated with the PM domain provider
    :type np: struct device_node \*

.. _`genpd_get_from_provider`:

genpd_get_from_provider
=======================

.. c:function:: struct generic_pm_domain *genpd_get_from_provider(struct of_phandle_args *genpdspec)

    Look-up PM domain

    :param genpdspec:
        OF phandle args to use for look-up
    :type genpdspec: struct of_phandle_args \*

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

    :param genpdspec:
        OF phandle args to use for look-up PM domain
    :type genpdspec: struct of_phandle_args \*

    :param dev:
        Device to be added.
    :type dev: struct device \*

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

    :param parent_spec:
        OF phandle args to use for parent PM domain look-up
    :type parent_spec: struct of_phandle_args \*

    :param subdomain_spec:
        OF phandle args to use for subdomain look-up
    :type subdomain_spec: struct of_phandle_args \*

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

    :param np:
        *undescribed*
    :type np: struct device_node \*

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

    :param dev:
        Device to detach.
    :type dev: struct device \*

    :param power_off:
        Currently not used
    :type power_off: bool

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

    :param dev:
        Device to attach.
    :type dev: struct device \*

.. _`genpd_dev_pm_attach.description`:

Description
-----------

Parse device's OF node to find a PM domain specifier. If such is found,
attaches the device to retrieved pm_domain ops.

Returns 1 on successfully attached PM domain, 0 when the device don't need a
PM domain or when multiple power-domains exists for it, else a negative error
code. Note that if a power-domain exists for the device, but it cannot be
found or turned on, then return -EPROBE_DEFER to ensure that the device is
not probed and to re-try again later.

.. _`genpd_dev_pm_attach_by_id`:

genpd_dev_pm_attach_by_id
=========================

.. c:function:: struct device *genpd_dev_pm_attach_by_id(struct device *dev, unsigned int index)

    Associate a device with one of its PM domains.

    :param dev:
        The device used to lookup the PM domain.
    :type dev: struct device \*

    :param index:
        The index of the PM domain.
    :type index: unsigned int

.. _`genpd_dev_pm_attach_by_id.description`:

Description
-----------

Parse device's OF node to find a PM domain specifier at the provided \ ``index``\ .
If such is found, creates a virtual device and attaches it to the retrieved
pm_domain ops. To deal with detaching of the virtual device, the ->detach()
callback in the struct dev_pm_domain are assigned to \ :c:func:`genpd_dev_pm_detach`\ .

Returns the created virtual device if successfully attached PM domain, NULL
when the device don't need a PM domain, else an \ :c:func:`ERR_PTR`\  in case of
failures. If a power-domain exists for the device, but cannot be found or
turned on, then ERR_PTR(-EPROBE_DEFER) is returned to ensure that the device
is not probed and to re-try again later.

.. _`genpd_dev_pm_attach_by_name`:

genpd_dev_pm_attach_by_name
===========================

.. c:function:: struct device *genpd_dev_pm_attach_by_name(struct device *dev, char *name)

    Associate a device with one of its PM domains.

    :param dev:
        The device used to lookup the PM domain.
    :type dev: struct device \*

    :param name:
        The name of the PM domain.
    :type name: char \*

.. _`genpd_dev_pm_attach_by_name.description`:

Description
-----------

Parse device's OF node to find a PM domain specifier using the
power-domain-names DT property. For further description see
\ :c:func:`genpd_dev_pm_attach_by_id`\ .

.. _`of_genpd_parse_idle_states`:

of_genpd_parse_idle_states
==========================

.. c:function:: int of_genpd_parse_idle_states(struct device_node *dn, struct genpd_power_state **states, int *n)

    Return array of idle states for the genpd.

    :param dn:
        The genpd device node
    :type dn: struct device_node \*

    :param states:
        The pointer to which the state array will be saved.
    :type states: struct genpd_power_state \*\*

    :param n:
        The count of elements in the array returned from this function.
    :type n: int \*

.. _`of_genpd_parse_idle_states.description`:

Description
-----------

Returns the device states parsed from the OF node. The memory for the states
is allocated by this function and is the responsibility of the caller to
free the memory after use. If any or zero compatible domain idle states is
found it returns 0 and in case of errors, a negative error code is returned.

.. _`of_genpd_opp_to_performance_state`:

of_genpd_opp_to_performance_state
=================================

.. c:function:: unsigned int of_genpd_opp_to_performance_state(struct device *dev, struct device_node *np)

    Gets performance state of device's power domain corresponding to a DT node's "required-opps" property.

    :param dev:
        Device for which the performance-state needs to be found.
    :type dev: struct device \*

    :param np:
        DT node where the "required-opps" property is present. This can be
        the device node itself (if it doesn't have an OPP table) or a node
        within the OPP table of a device (if device has an OPP table).
    :type np: struct device_node \*

.. _`of_genpd_opp_to_performance_state.description`:

Description
-----------

Returns performance state corresponding to the "required-opps" property of
a DT node. This calls platform specific genpd->opp_to_performance_state()
callback to translate power domain OPP to performance state.

Returns performance state on success and 0 on failure.

.. This file was automatic generated / don't edit.

