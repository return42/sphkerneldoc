.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/qos.c

.. _`pm_qos_update_target`:

pm_qos_update_target
====================

.. c:function:: int pm_qos_update_target(struct pm_qos_constraints *c, struct plist_node *node, enum pm_qos_req_action action, int value)

    manages the constraints list and calls the notifiers if needed

    :param struct pm_qos_constraints \*c:
        constraints data struct

    :param struct plist_node \*node:
        request to add to the list, to update or to remove

    :param enum pm_qos_req_action action:
        action to take on the constraints list

    :param int value:
        value of the request to add or update

.. _`pm_qos_update_target.description`:

Description
-----------

This function returns 1 if the aggregated constraint value has changed, 0
otherwise.

.. _`pm_qos_flags_remove_req`:

pm_qos_flags_remove_req
=======================

.. c:function:: void pm_qos_flags_remove_req(struct pm_qos_flags *pqf, struct pm_qos_flags_request *req)

    Remove device PM QoS flags request.

    :param struct pm_qos_flags \*pqf:
        Device PM QoS flags set to remove the request from.

    :param struct pm_qos_flags_request \*req:
        Request to remove from the set.

.. _`pm_qos_update_flags`:

pm_qos_update_flags
===================

.. c:function:: bool pm_qos_update_flags(struct pm_qos_flags *pqf, struct pm_qos_flags_request *req, enum pm_qos_req_action action, s32 val)

    Update a set of PM QoS flags.

    :param struct pm_qos_flags \*pqf:
        Set of flags to update.

    :param struct pm_qos_flags_request \*req:
        Request to add to the set, to modify, or to remove from the set.

    :param enum pm_qos_req_action action:
        Action to take on the set.

    :param s32 val:
        Value of the request to add or modify.

.. _`pm_qos_update_flags.description`:

Description
-----------

Update the given set of PM QoS flags and call notifiers if the aggregate
value has changed.  Returns 1 if the aggregate constraint value has changed,
0 otherwise.

.. _`pm_qos_request`:

pm_qos_request
==============

.. c:function:: int pm_qos_request(int pm_qos_class)

    returns current system wide qos expectation

    :param int pm_qos_class:
        identification of which qos value is requested

.. _`pm_qos_request.description`:

Description
-----------

This function returns the current target value.

.. _`pm_qos_work_fn`:

pm_qos_work_fn
==============

.. c:function:: void pm_qos_work_fn(struct work_struct *work)

    the timeout handler of pm_qos_update_request_timeout

    :param struct work_struct \*work:
        work struct for the delayed work (timeout)

.. _`pm_qos_work_fn.description`:

Description
-----------

This cancels the timeout request by falling back to the default at timeout.

.. _`pm_qos_add_request`:

pm_qos_add_request
==================

.. c:function:: void pm_qos_add_request(struct pm_qos_request *req, int pm_qos_class, s32 value)

    inserts new qos request into the list

    :param struct pm_qos_request \*req:
        pointer to a preallocated handle

    :param int pm_qos_class:
        identifies which list of qos request to use

    :param s32 value:
        defines the qos request

.. _`pm_qos_add_request.description`:

Description
-----------

This function inserts a new entry in the pm_qos_class list of requested qos
performance characteristics.  It recomputes the aggregate QoS expectations
for the pm_qos_class of parameters and initializes the pm_qos_request
handle.  Caller needs to save this handle for later use in updates and
removal.

.. _`pm_qos_update_request`:

pm_qos_update_request
=====================

.. c:function:: void pm_qos_update_request(struct pm_qos_request *req, s32 new_value)

    modifies an existing qos request

    :param struct pm_qos_request \*req:
        handle to list element holding a pm_qos request to use

    :param s32 new_value:
        *undescribed*

.. _`pm_qos_update_request.description`:

Description
-----------

Updates an existing qos request for the pm_qos_class of parameters along
with updating the target pm_qos_class value.

Attempts are made to make this code callable on hot code paths.

.. _`pm_qos_update_request_timeout`:

pm_qos_update_request_timeout
=============================

.. c:function:: void pm_qos_update_request_timeout(struct pm_qos_request *req, s32 new_value, unsigned long timeout_us)

    modifies an existing qos request temporarily.

    :param struct pm_qos_request \*req:
        handle to list element holding a pm_qos request to use

    :param s32 new_value:
        defines the temporal qos request

    :param unsigned long timeout_us:
        the effective duration of this qos request in usecs.

.. _`pm_qos_update_request_timeout.description`:

Description
-----------

After timeout_us, this qos request is cancelled automatically.

.. _`pm_qos_remove_request`:

pm_qos_remove_request
=====================

.. c:function:: void pm_qos_remove_request(struct pm_qos_request *req)

    modifies an existing qos request

    :param struct pm_qos_request \*req:
        handle to request list element

.. _`pm_qos_remove_request.description`:

Description
-----------

Will remove pm qos request from the list of constraints and
recompute the current target value for the pm_qos_class.  Call this
on slow code paths.

.. _`pm_qos_add_notifier`:

pm_qos_add_notifier
===================

.. c:function:: int pm_qos_add_notifier(int pm_qos_class, struct notifier_block *notifier)

    sets notification entry for changes to target value

    :param int pm_qos_class:
        identifies which qos target changes should be notified.

    :param struct notifier_block \*notifier:
        notifier block managed by caller.

.. _`pm_qos_add_notifier.description`:

Description
-----------

will register the notifier into a notification chain that gets called
upon changes to the pm_qos_class target value.

.. _`pm_qos_remove_notifier`:

pm_qos_remove_notifier
======================

.. c:function:: int pm_qos_remove_notifier(int pm_qos_class, struct notifier_block *notifier)

    deletes notification entry from chain.

    :param int pm_qos_class:
        identifies which qos target changes are notified.

    :param struct notifier_block \*notifier:
        notifier block to be removed.

.. _`pm_qos_remove_notifier.description`:

Description
-----------

will remove the notifier from the notification chain that gets called
upon changes to the pm_qos_class target value.

.. This file was automatic generated / don't edit.

