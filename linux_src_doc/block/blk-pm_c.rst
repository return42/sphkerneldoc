.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-pm.c

.. _`blk_pm_runtime_init`:

blk_pm_runtime_init
===================

.. c:function:: void blk_pm_runtime_init(struct request_queue *q, struct device *dev)

    Block layer runtime PM initialization routine

    :param q:
        the queue of the device
    :type q: struct request_queue \*

    :param dev:
        the device the queue belongs to
    :type dev: struct device \*

.. _`blk_pm_runtime_init.description`:

Description
-----------

Initialize runtime-PM-related fields for \ ``q``\  and start auto suspend for
\ ``dev``\ . Drivers that want to take advantage of request-based runtime PM
should call this function after \ ``dev``\  has been initialized, and its
request queue \ ``q``\  has been allocated, and runtime PM for it can not happen
yet(either due to disabled/forbidden or its usage_count > 0). In most
cases, driver should call this function before any I/O has taken place.

This function takes care of setting up using auto suspend for the device,
the autosuspend delay is set to -1 to make runtime suspend impossible
until an updated value is either set by user or by driver. Drivers do
not need to touch other autosuspend settings.

The block layer runtime PM is request based, so only works for drivers
that use request as their IO unit instead of those directly use bio's.

.. _`blk_pre_runtime_suspend`:

blk_pre_runtime_suspend
=======================

.. c:function:: int blk_pre_runtime_suspend(struct request_queue *q)

    Pre runtime suspend check

    :param q:
        the queue of the device
    :type q: struct request_queue \*

.. _`blk_pre_runtime_suspend.description`:

Description
-----------

This function will check if runtime suspend is allowed for the device
by examining if there are any requests pending in the queue. If there
are requests pending, the device can not be runtime suspended; otherwise,
the queue's status will be updated to SUSPENDING and the driver can
proceed to suspend the device.

For the not allowed case, we mark last busy for the device so that
runtime PM core will try to autosuspend it some time later.

This function should be called near the start of the device's
runtime_suspend callback.

.. _`blk_pre_runtime_suspend.return`:

Return
------

0         - OK to runtime suspend the device
-EBUSY    - Device should not be runtime suspended

.. _`blk_post_runtime_suspend`:

blk_post_runtime_suspend
========================

.. c:function:: void blk_post_runtime_suspend(struct request_queue *q, int err)

    Post runtime suspend processing

    :param q:
        the queue of the device
    :type q: struct request_queue \*

    :param err:
        return value of the device's runtime_suspend function
    :type err: int

.. _`blk_post_runtime_suspend.description`:

Description
-----------

Update the queue's runtime status according to the return value of the
device's runtime suspend function and mark last busy for the device so
that PM core will try to auto suspend the device at a later time.

This function should be called near the end of the device's
runtime_suspend callback.

.. _`blk_pre_runtime_resume`:

blk_pre_runtime_resume
======================

.. c:function:: void blk_pre_runtime_resume(struct request_queue *q)

    Pre runtime resume processing

    :param q:
        the queue of the device
    :type q: struct request_queue \*

.. _`blk_pre_runtime_resume.description`:

Description
-----------

Update the queue's runtime status to RESUMING in preparation for the
runtime resume of the device.

This function should be called near the start of the device's
runtime_resume callback.

.. _`blk_post_runtime_resume`:

blk_post_runtime_resume
=======================

.. c:function:: void blk_post_runtime_resume(struct request_queue *q, int err)

    Post runtime resume processing

    :param q:
        the queue of the device
    :type q: struct request_queue \*

    :param err:
        return value of the device's runtime_resume function
    :type err: int

.. _`blk_post_runtime_resume.description`:

Description
-----------

Update the queue's runtime status according to the return value of the
device's runtime_resume function. If it is successfully resumed, process
the requests that are queued into the device's queue when it is resuming
and then mark last busy and initiate autosuspend for it.

This function should be called near the end of the device's
runtime_resume callback.

.. _`blk_set_runtime_active`:

blk_set_runtime_active
======================

.. c:function:: void blk_set_runtime_active(struct request_queue *q)

    Force runtime status of the queue to be active

    :param q:
        the queue of the device
    :type q: struct request_queue \*

.. _`blk_set_runtime_active.description`:

Description
-----------

If the device is left runtime suspended during system suspend the resume
hook typically resumes the device and corrects runtime status
accordingly. However, that does not affect the queue runtime PM status
which is still "suspended". This prevents processing requests from the
queue.

This function can be used in driver's resume hook to correct queue
runtime PM status and re-enable peeking requests from the queue. It
should be called before first request is added to the queue.

.. This file was automatic generated / don't edit.

