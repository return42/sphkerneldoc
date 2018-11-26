.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/power/qos.c

.. _`__dev_pm_qos_flags`:

\__dev_pm_qos_flags
===================

.. c:function:: enum pm_qos_flags_status __dev_pm_qos_flags(struct device *dev, s32 mask)

    Check PM QoS flags for a given device.

    :param dev:
        Device to check the PM QoS flags for.
    :type dev: struct device \*

    :param mask:
        Flags to check against.
    :type mask: s32

.. _`__dev_pm_qos_flags.description`:

Description
-----------

This routine must be called with dev->power.lock held.

.. _`dev_pm_qos_flags`:

dev_pm_qos_flags
================

.. c:function:: enum pm_qos_flags_status dev_pm_qos_flags(struct device *dev, s32 mask)

    Check PM QoS flags for a given device (locked).

    :param dev:
        Device to check the PM QoS flags for.
    :type dev: struct device \*

    :param mask:
        Flags to check against.
    :type mask: s32

.. _`__dev_pm_qos_read_value`:

\__dev_pm_qos_read_value
========================

.. c:function:: s32 __dev_pm_qos_read_value(struct device *dev)

    Get PM QoS constraint for a given device.

    :param dev:
        Device to get the PM QoS constraint value for.
    :type dev: struct device \*

.. _`__dev_pm_qos_read_value.description`:

Description
-----------

This routine must be called with dev->power.lock held.

.. _`dev_pm_qos_read_value`:

dev_pm_qos_read_value
=====================

.. c:function:: s32 dev_pm_qos_read_value(struct device *dev)

    Get PM QoS constraint for a given device (locked).

    :param dev:
        Device to get the PM QoS constraint value for.
    :type dev: struct device \*

.. _`apply_constraint`:

apply_constraint
================

.. c:function:: int apply_constraint(struct dev_pm_qos_request *req, enum pm_qos_req_action action, s32 value)

    Add/modify/remove device PM QoS request.

    :param req:
        Constraint request to apply
    :type req: struct dev_pm_qos_request \*

    :param action:
        Action to perform (add/update/remove).
    :type action: enum pm_qos_req_action

    :param value:
        Value to assign to the QoS request.
    :type value: s32

.. _`apply_constraint.description`:

Description
-----------

Internal function to update the constraints list using the PM QoS core
code and if needed call the per-device callbacks.

.. _`dev_pm_qos_constraints_destroy`:

dev_pm_qos_constraints_destroy
==============================

.. c:function:: void dev_pm_qos_constraints_destroy(struct device *dev)

    :param dev:
        target device
    :type dev: struct device \*

.. _`dev_pm_qos_constraints_destroy.description`:

Description
-----------

Called from the device PM subsystem on device removal under \ :c:func:`device_pm_lock`\ .

.. _`dev_pm_qos_add_request`:

dev_pm_qos_add_request
======================

.. c:function:: int dev_pm_qos_add_request(struct device *dev, struct dev_pm_qos_request *req, enum dev_pm_qos_req_type type, s32 value)

    inserts new qos request into the list

    :param dev:
        target device for the constraint
    :type dev: struct device \*

    :param req:
        pointer to a preallocated handle
    :type req: struct dev_pm_qos_request \*

    :param type:
        type of the request
    :type type: enum dev_pm_qos_req_type

    :param value:
        defines the qos request
    :type value: s32

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

\__dev_pm_qos_update_request
============================

.. c:function:: int __dev_pm_qos_update_request(struct dev_pm_qos_request *req, s32 new_value)

    Modify an existing device PM QoS request.

    :param req:
        PM QoS request to modify.
    :type req: struct dev_pm_qos_request \*

    :param new_value:
        New value to request.
    :type new_value: s32

.. _`dev_pm_qos_update_request`:

dev_pm_qos_update_request
=========================

.. c:function:: int dev_pm_qos_update_request(struct dev_pm_qos_request *req, s32 new_value)

    modifies an existing qos request

    :param req:
        handle to list element holding a dev_pm_qos request to use
    :type req: struct dev_pm_qos_request \*

    :param new_value:
        defines the qos request
    :type new_value: s32

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

.. c:function:: int dev_pm_qos_remove_request(struct dev_pm_qos_request *req)

    modifies an existing qos request

    :param req:
        handle to request list element
    :type req: struct dev_pm_qos_request \*

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

.. c:function:: int dev_pm_qos_add_notifier(struct device *dev, struct notifier_block *notifier)

    sets notification entry for changes to target value of per-device PM QoS constraints

    :param dev:
        target device for the constraint
    :type dev: struct device \*

    :param notifier:
        notifier block managed by caller.
    :type notifier: struct notifier_block \*

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

.. c:function:: int dev_pm_qos_remove_notifier(struct device *dev, struct notifier_block *notifier)

    deletes notification for changes to target value of per-device PM QoS constraints

    :param dev:
        target device for the constraint
    :type dev: struct device \*

    :param notifier:
        notifier block to be removed.
    :type notifier: struct notifier_block \*

.. _`dev_pm_qos_remove_notifier.description`:

Description
-----------

Will remove the notifier from the notification chain that gets called
upon changes to the target value.

.. _`dev_pm_qos_add_ancestor_request`:

dev_pm_qos_add_ancestor_request
===============================

.. c:function:: int dev_pm_qos_add_ancestor_request(struct device *dev, struct dev_pm_qos_request *req, enum dev_pm_qos_req_type type, s32 value)

    Add PM QoS request for device's ancestor.

    :param dev:
        Device whose ancestor to add the request for.
    :type dev: struct device \*

    :param req:
        Pointer to the preallocated handle.
    :type req: struct dev_pm_qos_request \*

    :param type:
        Type of the request.
    :type type: enum dev_pm_qos_req_type

    :param value:
        Constraint latency value.
    :type value: s32

.. _`dev_pm_qos_expose_latency_limit`:

dev_pm_qos_expose_latency_limit
===============================

.. c:function:: int dev_pm_qos_expose_latency_limit(struct device *dev, s32 value)

    Expose PM QoS latency limit to user space.

    :param dev:
        Device whose PM QoS latency limit is to be exposed to user space.
    :type dev: struct device \*

    :param value:
        Initial value of the latency limit.
    :type value: s32

.. _`dev_pm_qos_hide_latency_limit`:

dev_pm_qos_hide_latency_limit
=============================

.. c:function:: void dev_pm_qos_hide_latency_limit(struct device *dev)

    Hide PM QoS latency limit from user space.

    :param dev:
        Device whose PM QoS latency limit is to be hidden from user space.
    :type dev: struct device \*

.. _`dev_pm_qos_expose_flags`:

dev_pm_qos_expose_flags
=======================

.. c:function:: int dev_pm_qos_expose_flags(struct device *dev, s32 val)

    Expose PM QoS flags of a device to user space.

    :param dev:
        Device whose PM QoS flags are to be exposed to user space.
    :type dev: struct device \*

    :param val:
        Initial values of the flags.
    :type val: s32

.. _`dev_pm_qos_hide_flags`:

dev_pm_qos_hide_flags
=====================

.. c:function:: void dev_pm_qos_hide_flags(struct device *dev)

    Hide PM QoS flags of a device from user space.

    :param dev:
        Device whose PM QoS flags are to be hidden from user space.
    :type dev: struct device \*

.. _`dev_pm_qos_update_flags`:

dev_pm_qos_update_flags
=======================

.. c:function:: int dev_pm_qos_update_flags(struct device *dev, s32 mask, bool set)

    Update PM QoS flags request owned by user space.

    :param dev:
        Device to update the PM QoS flags request for.
    :type dev: struct device \*

    :param mask:
        Flags to set/clear.
    :type mask: s32

    :param set:
        Whether to set or clear the flags (true means set).
    :type set: bool

.. _`dev_pm_qos_get_user_latency_tolerance`:

dev_pm_qos_get_user_latency_tolerance
=====================================

.. c:function:: s32 dev_pm_qos_get_user_latency_tolerance(struct device *dev)

    Get user space latency tolerance.

    :param dev:
        Device to obtain the user space latency tolerance for.
    :type dev: struct device \*

.. _`dev_pm_qos_update_user_latency_tolerance`:

dev_pm_qos_update_user_latency_tolerance
========================================

.. c:function:: int dev_pm_qos_update_user_latency_tolerance(struct device *dev, s32 val)

    Update user space latency tolerance.

    :param dev:
        Device to update the user space latency tolerance for.
    :type dev: struct device \*

    :param val:
        New user space latency tolerance for \ ``dev``\  (negative values disable).
    :type val: s32

.. _`dev_pm_qos_expose_latency_tolerance`:

dev_pm_qos_expose_latency_tolerance
===================================

.. c:function:: int dev_pm_qos_expose_latency_tolerance(struct device *dev)

    Expose latency tolerance to userspace

    :param dev:
        Device whose latency tolerance to expose
    :type dev: struct device \*

.. _`dev_pm_qos_hide_latency_tolerance`:

dev_pm_qos_hide_latency_tolerance
=================================

.. c:function:: void dev_pm_qos_hide_latency_tolerance(struct device *dev)

    Hide latency tolerance from userspace

    :param dev:
        Device whose latency tolerance to hide
    :type dev: struct device \*

.. This file was automatic generated / don't edit.

