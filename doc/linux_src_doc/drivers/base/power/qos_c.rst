.. -*- coding: utf-8; mode: rst -*-

=====
qos.c
=====


.. _`__dev_pm_qos_flags`:

__dev_pm_qos_flags
==================

.. c:function:: enum pm_qos_flags_status __dev_pm_qos_flags (struct device *dev, s32 mask)

    Check PM QoS flags for a given device.

    :param struct device \*dev:
        Device to check the PM QoS flags for.

    :param s32 mask:
        Flags to check against.



.. _`__dev_pm_qos_flags.description`:

Description
-----------

This routine must be called with dev->power.lock held.



.. _`dev_pm_qos_flags`:

dev_pm_qos_flags
================

.. c:function:: enum pm_qos_flags_status dev_pm_qos_flags (struct device *dev, s32 mask)

    Check PM QoS flags for a given device (locked).

    :param struct device \*dev:
        Device to check the PM QoS flags for.

    :param s32 mask:
        Flags to check against.



.. _`__dev_pm_qos_read_value`:

__dev_pm_qos_read_value
=======================

.. c:function:: s32 __dev_pm_qos_read_value (struct device *dev)

    Get PM QoS constraint for a given device.

    :param struct device \*dev:
        Device to get the PM QoS constraint value for.



.. _`__dev_pm_qos_read_value.description`:

Description
-----------

This routine must be called with dev->power.lock held.



.. _`dev_pm_qos_read_value`:

dev_pm_qos_read_value
=====================

.. c:function:: s32 dev_pm_qos_read_value (struct device *dev)

    Get PM QoS constraint for a given device (locked).

    :param struct device \*dev:
        Device to get the PM QoS constraint value for.



.. _`apply_constraint`:

apply_constraint
================

.. c:function:: int apply_constraint (struct dev_pm_qos_request *req, enum pm_qos_req_action action, s32 value)

    Add/modify/remove device PM QoS request.

    :param struct dev_pm_qos_request \*req:
        Constraint request to apply

    :param enum pm_qos_req_action action:
        Action to perform (add/update/remove).

    :param s32 value:
        Value to assign to the QoS request.



.. _`apply_constraint.description`:

Description
-----------

Internal function to update the constraints list using the PM QoS core
code and if needed call the per-device and the global notification
callbacks



.. _`dev_pm_qos_constraints_destroy`:

dev_pm_qos_constraints_destroy
==============================

.. c:function:: void dev_pm_qos_constraints_destroy (struct device *dev)

    :param struct device \*dev:
        target device



.. _`dev_pm_qos_constraints_destroy.description`:

Description
-----------

Called from the device PM subsystem on device removal under :c:func:`device_pm_lock`.



.. _`dev_pm_qos_add_request`:

dev_pm_qos_add_request
======================

.. c:function:: int dev_pm_qos_add_request (struct device *dev, struct dev_pm_qos_request *req, enum dev_pm_qos_req_type type, s32 value)

    inserts new qos request into the list

    :param struct device \*dev:
        target device for the constraint

    :param struct dev_pm_qos_request \*req:
        pointer to a preallocated handle

    :param enum dev_pm_qos_req_type type:
        type of the request

    :param s32 value:
        defines the qos request



.. _`dev_pm_qos_add_request.description`:

Description
-----------

This function inserts a new entry in the device constraints list of
requested qos performance characteristics. It recomputes the aggregate
QoS expectations of parameters and initializes the dev_pm_qos_request
handle.  Caller needs to save this handle for later use in updates and
removal.

Returns 1 if the aggregated constraint value has changed,
0 if the aggregated constraint value has not changed,
-EINVAL in case of wrong parameters, -ENOMEM if there's not enough memory
to allocate for data structures, -ENODEV if the device has just been removed
from the system.

Callers should ensure that the target device is not RPM_SUSPENDED before
using this function for requests of type DEV_PM_QOS_FLAGS.



.. _`__dev_pm_qos_update_request`:

__dev_pm_qos_update_request
===========================

.. c:function:: int __dev_pm_qos_update_request (struct dev_pm_qos_request *req, s32 new_value)

    Modify an existing device PM QoS request.

    :param struct dev_pm_qos_request \*req:
        PM QoS request to modify.

    :param s32 new_value:
        New value to request.



.. _`dev_pm_qos_update_request`:

dev_pm_qos_update_request
=========================

.. c:function:: int dev_pm_qos_update_request (struct dev_pm_qos_request *req, s32 new_value)

    modifies an existing qos request

    :param struct dev_pm_qos_request \*req:
        handle to list element holding a dev_pm_qos request to use

    :param s32 new_value:
        defines the qos request



.. _`dev_pm_qos_update_request.description`:

Description
-----------

Updates an existing dev PM qos request along with updating the
target value.

Attempts are made to make this code callable on hot code paths.

Returns 1 if the aggregated constraint value has changed,
0 if the aggregated constraint value has not changed,
-EINVAL in case of wrong parameters, -ENODEV if the device has been
removed from the system

Callers should ensure that the target device is not RPM_SUSPENDED before
using this function for requests of type DEV_PM_QOS_FLAGS.



.. _`dev_pm_qos_remove_request`:

dev_pm_qos_remove_request
=========================

.. c:function:: int dev_pm_qos_remove_request (struct dev_pm_qos_request *req)

    modifies an existing qos request

    :param struct dev_pm_qos_request \*req:
        handle to request list element



.. _`dev_pm_qos_remove_request.description`:

Description
-----------

Will remove pm qos request from the list of constraints and
recompute the current target value. Call this on slow code paths.

Returns 1 if the aggregated constraint value has changed,
0 if the aggregated constraint value has not changed,
-EINVAL in case of wrong parameters, -ENODEV if the device has been
removed from the system

Callers should ensure that the target device is not RPM_SUSPENDED before
using this function for requests of type DEV_PM_QOS_FLAGS.



.. _`dev_pm_qos_add_notifier`:

dev_pm_qos_add_notifier
=======================

.. c:function:: int dev_pm_qos_add_notifier (struct device *dev, struct notifier_block *notifier)

    sets notification entry for changes to target value of per-device PM QoS constraints

    :param struct device \*dev:
        target device for the constraint

    :param struct notifier_block \*notifier:
        notifier block managed by caller.



.. _`dev_pm_qos_add_notifier.description`:

Description
-----------

Will register the notifier into a notification chain that gets called
upon changes to the target value for the device.

If the device's constraints object doesn't exist when this routine is called,
it will be created (or error code will be returned if that fails).



.. _`dev_pm_qos_remove_notifier`:

dev_pm_qos_remove_notifier
==========================

.. c:function:: int dev_pm_qos_remove_notifier (struct device *dev, struct notifier_block *notifier)

    deletes notification for changes to target value of per-device PM QoS constraints

    :param struct device \*dev:
        target device for the constraint

    :param struct notifier_block \*notifier:
        notifier block to be removed.



.. _`dev_pm_qos_remove_notifier.description`:

Description
-----------

Will remove the notifier from the notification chain that gets called
upon changes to the target value.



.. _`dev_pm_qos_add_global_notifier`:

dev_pm_qos_add_global_notifier
==============================

.. c:function:: int dev_pm_qos_add_global_notifier (struct notifier_block *notifier)

    sets notification entry for changes to target value of the PM QoS constraints for any device

    :param struct notifier_block \*notifier:
        notifier block managed by caller.



.. _`dev_pm_qos_add_global_notifier.description`:

Description
-----------

Will register the notifier into a notification chain that gets called
upon changes to the target value for any device.



.. _`dev_pm_qos_remove_global_notifier`:

dev_pm_qos_remove_global_notifier
=================================

.. c:function:: int dev_pm_qos_remove_global_notifier (struct notifier_block *notifier)

    deletes notification for changes to target value of PM QoS constraints for any device

    :param struct notifier_block \*notifier:
        notifier block to be removed.



.. _`dev_pm_qos_remove_global_notifier.description`:

Description
-----------

Will remove the notifier from the notification chain that gets called
upon changes to the target value for any device.



.. _`dev_pm_qos_add_ancestor_request`:

dev_pm_qos_add_ancestor_request
===============================

.. c:function:: int dev_pm_qos_add_ancestor_request (struct device *dev, struct dev_pm_qos_request *req, enum dev_pm_qos_req_type type, s32 value)

    Add PM QoS request for device's ancestor.

    :param struct device \*dev:
        Device whose ancestor to add the request for.

    :param struct dev_pm_qos_request \*req:
        Pointer to the preallocated handle.

    :param enum dev_pm_qos_req_type type:
        Type of the request.

    :param s32 value:
        Constraint latency value.



.. _`dev_pm_qos_expose_latency_limit`:

dev_pm_qos_expose_latency_limit
===============================

.. c:function:: int dev_pm_qos_expose_latency_limit (struct device *dev, s32 value)

    Expose PM QoS latency limit to user space.

    :param struct device \*dev:
        Device whose PM QoS latency limit is to be exposed to user space.

    :param s32 value:
        Initial value of the latency limit.



.. _`dev_pm_qos_hide_latency_limit`:

dev_pm_qos_hide_latency_limit
=============================

.. c:function:: void dev_pm_qos_hide_latency_limit (struct device *dev)

    Hide PM QoS latency limit from user space.

    :param struct device \*dev:
        Device whose PM QoS latency limit is to be hidden from user space.



.. _`dev_pm_qos_expose_flags`:

dev_pm_qos_expose_flags
=======================

.. c:function:: int dev_pm_qos_expose_flags (struct device *dev, s32 val)

    Expose PM QoS flags of a device to user space.

    :param struct device \*dev:
        Device whose PM QoS flags are to be exposed to user space.

    :param s32 val:
        Initial values of the flags.



.. _`dev_pm_qos_hide_flags`:

dev_pm_qos_hide_flags
=====================

.. c:function:: void dev_pm_qos_hide_flags (struct device *dev)

    Hide PM QoS flags of a device from user space.

    :param struct device \*dev:
        Device whose PM QoS flags are to be hidden from user space.



.. _`dev_pm_qos_update_flags`:

dev_pm_qos_update_flags
=======================

.. c:function:: int dev_pm_qos_update_flags (struct device *dev, s32 mask, bool set)

    Update PM QoS flags request owned by user space.

    :param struct device \*dev:
        Device to update the PM QoS flags request for.

    :param s32 mask:
        Flags to set/clear.

    :param bool set:
        Whether to set or clear the flags (true means set).



.. _`dev_pm_qos_get_user_latency_tolerance`:

dev_pm_qos_get_user_latency_tolerance
=====================================

.. c:function:: s32 dev_pm_qos_get_user_latency_tolerance (struct device *dev)

    Get user space latency tolerance.

    :param struct device \*dev:
        Device to obtain the user space latency tolerance for.



.. _`dev_pm_qos_update_user_latency_tolerance`:

dev_pm_qos_update_user_latency_tolerance
========================================

.. c:function:: int dev_pm_qos_update_user_latency_tolerance (struct device *dev, s32 val)

    Update user space latency tolerance.

    :param struct device \*dev:
        Device to update the user space latency tolerance for.

    :param s32 val:
        New user space latency tolerance for ``dev`` (negative values disable).



.. _`dev_pm_qos_expose_latency_tolerance`:

dev_pm_qos_expose_latency_tolerance
===================================

.. c:function:: int dev_pm_qos_expose_latency_tolerance (struct device *dev)

    Expose latency tolerance to userspace

    :param struct device \*dev:
        Device whose latency tolerance to expose



.. _`dev_pm_qos_hide_latency_tolerance`:

dev_pm_qos_hide_latency_tolerance
=================================

.. c:function:: void dev_pm_qos_hide_latency_tolerance (struct device *dev)

    Hide latency tolerance from userspace

    :param struct device \*dev:
        Device whose latency tolerance to hide

