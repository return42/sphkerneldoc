.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/devfreq/devfreq.c

.. _`find_device_devfreq`:

find_device_devfreq
===================

.. c:function:: struct devfreq *find_device_devfreq(struct device *dev)

    find devfreq struct using device pointer

    :param dev:
        device pointer used to lookup device devfreq.
    :type dev: struct device \*

.. _`find_device_devfreq.description`:

Description
-----------

Search the list of device devfreqs and return the matched device's
devfreq info. devfreq_list_lock should be held by the caller.

.. _`devfreq_get_freq_level`:

devfreq_get_freq_level
======================

.. c:function:: int devfreq_get_freq_level(struct devfreq *devfreq, unsigned long freq)

    Lookup freq_table for the frequency

    :param devfreq:
        the devfreq instance
    :type devfreq: struct devfreq \*

    :param freq:
        the target frequency
    :type freq: unsigned long

.. _`devfreq_update_status`:

devfreq_update_status
=====================

.. c:function:: int devfreq_update_status(struct devfreq *devfreq, unsigned long freq)

    Update statistics of devfreq behavior

    :param devfreq:
        the devfreq instance
    :type devfreq: struct devfreq \*

    :param freq:
        the update target frequency
    :type freq: unsigned long

.. _`find_devfreq_governor`:

find_devfreq_governor
=====================

.. c:function:: struct devfreq_governor *find_devfreq_governor(const char *name)

    find devfreq governor from name

    :param name:
        name of the governor
    :type name: const char \*

.. _`find_devfreq_governor.description`:

Description
-----------

Search the list of devfreq governors and return the matched
governor's pointer. devfreq_list_lock should be held by the caller.

.. _`try_then_request_governor`:

try_then_request_governor
=========================

.. c:function:: struct devfreq_governor *try_then_request_governor(const char *name)

    Try to find the governor and request the module if is not found.

    :param name:
        name of the governor
    :type name: const char \*

.. _`try_then_request_governor.description`:

Description
-----------

Search the list of devfreq governors and request the module and try again
if is not found. This can happen when both drivers (the governor driver
and the driver that call devfreq_add_device) are built as modules.
devfreq_list_lock should be held by the caller. Returns the matched
governor's pointer.

.. _`update_devfreq`:

update_devfreq
==============

.. c:function:: int update_devfreq(struct devfreq *devfreq)

    Reevaluate the device and configure frequency.

    :param devfreq:
        the devfreq instance.
    :type devfreq: struct devfreq \*

.. _`update_devfreq.note`:

Note
----

Lock devfreq->lock before calling update_devfreq
This function is exported for governors.

.. _`devfreq_monitor`:

devfreq_monitor
===============

.. c:function:: void devfreq_monitor(struct work_struct *work)

    Periodically poll devfreq objects.

    :param work:
        the work struct used to run devfreq_monitor periodically.
    :type work: struct work_struct \*

.. _`devfreq_monitor_start`:

devfreq_monitor_start
=====================

.. c:function:: void devfreq_monitor_start(struct devfreq *devfreq)

    Start load monitoring of devfreq instance

    :param devfreq:
        the devfreq instance.
    :type devfreq: struct devfreq \*

.. _`devfreq_monitor_start.description`:

Description
-----------

Helper function for starting devfreq device load monitoing. By
default delayed work based monitoring is supported. Function
to be called from governor in response to DEVFREQ_GOV_START
event when device is added to devfreq framework.

.. _`devfreq_monitor_stop`:

devfreq_monitor_stop
====================

.. c:function:: void devfreq_monitor_stop(struct devfreq *devfreq)

    Stop load monitoring of a devfreq instance

    :param devfreq:
        the devfreq instance.
    :type devfreq: struct devfreq \*

.. _`devfreq_monitor_stop.description`:

Description
-----------

Helper function to stop devfreq device load monitoing. Function
to be called from governor in response to DEVFREQ_GOV_STOP
event when device is removed from devfreq framework.

.. _`devfreq_monitor_suspend`:

devfreq_monitor_suspend
=======================

.. c:function:: void devfreq_monitor_suspend(struct devfreq *devfreq)

    Suspend load monitoring of a devfreq instance

    :param devfreq:
        the devfreq instance.
    :type devfreq: struct devfreq \*

.. _`devfreq_monitor_suspend.description`:

Description
-----------

Helper function to suspend devfreq device load monitoing. Function
to be called from governor in response to DEVFREQ_GOV_SUSPEND
event or when polling interval is set to zero.

.. _`devfreq_monitor_suspend.note`:

Note
----

Though this function is same as \ :c:func:`devfreq_monitor_stop`\ ,
intentionally kept separate to provide hooks for collecting
transition statistics.

.. _`devfreq_monitor_resume`:

devfreq_monitor_resume
======================

.. c:function:: void devfreq_monitor_resume(struct devfreq *devfreq)

    Resume load monitoring of a devfreq instance

    :param devfreq:
        the devfreq instance.
    :type devfreq: struct devfreq \*

.. _`devfreq_monitor_resume.description`:

Description
-----------

Helper function to resume devfreq device load monitoing. Function
to be called from governor in response to DEVFREQ_GOV_RESUME
event or when polling interval is set to non-zero.

.. _`devfreq_interval_update`:

devfreq_interval_update
=======================

.. c:function:: void devfreq_interval_update(struct devfreq *devfreq, unsigned int *delay)

    Update device devfreq monitoring interval

    :param devfreq:
        the devfreq instance.
    :type devfreq: struct devfreq \*

    :param delay:
        new polling interval to be set.
    :type delay: unsigned int \*

.. _`devfreq_interval_update.description`:

Description
-----------

Helper function to set new load monitoring polling interval. Function
to be called from governor in response to DEVFREQ_GOV_INTERVAL event.

.. _`devfreq_notifier_call`:

devfreq_notifier_call
=====================

.. c:function:: int devfreq_notifier_call(struct notifier_block *nb, unsigned long type, void *devp)

    Notify that the device frequency requirements has been changed out of devfreq framework.

    :param nb:
        the notifier_block (supposed to be devfreq->nb)
    :type nb: struct notifier_block \*

    :param type:
        not used
    :type type: unsigned long

    :param devp:
        not used
    :type devp: void \*

.. _`devfreq_notifier_call.description`:

Description
-----------

Called by a notifier that uses devfreq->nb.

.. _`devfreq_dev_release`:

devfreq_dev_release
===================

.. c:function:: void devfreq_dev_release(struct device *dev)

    Callback for struct device to release the device.

    :param dev:
        the devfreq device
    :type dev: struct device \*

.. _`devfreq_dev_release.description`:

Description
-----------

Remove devfreq from the list and release its resources.

.. _`devfreq_add_device`:

devfreq_add_device
==================

.. c:function:: struct devfreq *devfreq_add_device(struct device *dev, struct devfreq_dev_profile *profile, const char *governor_name, void *data)

    Add devfreq feature to the device

    :param dev:
        the device to add devfreq feature.
    :type dev: struct device \*

    :param profile:
        device-specific profile to run devfreq.
    :type profile: struct devfreq_dev_profile \*

    :param governor_name:
        name of the policy to choose frequency.
    :type governor_name: const char \*

    :param data:
        private data for the governor. The devfreq framework does not
        touch this value.
    :type data: void \*

.. _`devfreq_remove_device`:

devfreq_remove_device
=====================

.. c:function:: int devfreq_remove_device(struct devfreq *devfreq)

    Remove devfreq feature from a device.

    :param devfreq:
        the devfreq instance to be removed
    :type devfreq: struct devfreq \*

.. _`devfreq_remove_device.description`:

Description
-----------

The opposite of \ :c:func:`devfreq_add_device`\ .

.. _`devm_devfreq_add_device`:

devm_devfreq_add_device
=======================

.. c:function:: struct devfreq *devm_devfreq_add_device(struct device *dev, struct devfreq_dev_profile *profile, const char *governor_name, void *data)

    Resource-managed \ :c:func:`devfreq_add_device`\ 

    :param dev:
        the device to add devfreq feature.
    :type dev: struct device \*

    :param profile:
        device-specific profile to run devfreq.
    :type profile: struct devfreq_dev_profile \*

    :param governor_name:
        name of the policy to choose frequency.
    :type governor_name: const char \*

    :param data:
        private data for the governor. The devfreq framework does not
        touch this value.
    :type data: void \*

.. _`devm_devfreq_add_device.description`:

Description
-----------

This function manages automatically the memory of devfreq device using device
resource management and simplify the free operation for memory of devfreq
device.

.. _`devm_devfreq_remove_device`:

devm_devfreq_remove_device
==========================

.. c:function:: void devm_devfreq_remove_device(struct device *dev, struct devfreq *devfreq)

    Resource-managed \ :c:func:`devfreq_remove_device`\ 

    :param dev:
        the device to add devfreq feature.
    :type dev: struct device \*

    :param devfreq:
        the devfreq instance to be removed
    :type devfreq: struct devfreq \*

.. _`devfreq_suspend_device`:

devfreq_suspend_device
======================

.. c:function:: int devfreq_suspend_device(struct devfreq *devfreq)

    Suspend devfreq of a device.

    :param devfreq:
        the devfreq instance to be suspended
    :type devfreq: struct devfreq \*

.. _`devfreq_suspend_device.description`:

Description
-----------

This function is intended to be called by the pm callbacks
(e.g., runtime_suspend, suspend) of the device driver that
holds the devfreq.

.. _`devfreq_resume_device`:

devfreq_resume_device
=====================

.. c:function:: int devfreq_resume_device(struct devfreq *devfreq)

    Resume devfreq of a device.

    :param devfreq:
        the devfreq instance to be resumed
    :type devfreq: struct devfreq \*

.. _`devfreq_resume_device.description`:

Description
-----------

This function is intended to be called by the pm callbacks
(e.g., runtime_resume, resume) of the device driver that
holds the devfreq.

.. _`devfreq_add_governor`:

devfreq_add_governor
====================

.. c:function:: int devfreq_add_governor(struct devfreq_governor *governor)

    Add devfreq governor

    :param governor:
        the devfreq governor to be added
    :type governor: struct devfreq_governor \*

.. _`devfreq_remove_governor`:

devfreq_remove_governor
=======================

.. c:function:: int devfreq_remove_governor(struct devfreq_governor *governor)

    Remove devfreq feature from a device.

    :param governor:
        the devfreq governor to be removed
    :type governor: struct devfreq_governor \*

.. _`devfreq_recommended_opp`:

devfreq_recommended_opp
=======================

.. c:function:: struct dev_pm_opp *devfreq_recommended_opp(struct device *dev, unsigned long *freq, u32 flags)

    Helper function to get proper OPP for the freq value given to target callback.

    :param dev:
        The devfreq user device. (parent of devfreq)
    :type dev: struct device \*

    :param freq:
        The frequency given to target function
    :type freq: unsigned long \*

    :param flags:
        Flags handed from devfreq framework.
    :type flags: u32

.. _`devfreq_recommended_opp.description`:

Description
-----------

The callers are required to call \ :c:func:`dev_pm_opp_put`\  for the returned OPP after
use.

.. _`devfreq_register_opp_notifier`:

devfreq_register_opp_notifier
=============================

.. c:function:: int devfreq_register_opp_notifier(struct device *dev, struct devfreq *devfreq)

    Helper function to get devfreq notified for any changes in the OPP availability changes

    :param dev:
        The devfreq user device. (parent of devfreq)
    :type dev: struct device \*

    :param devfreq:
        The devfreq object.
    :type devfreq: struct devfreq \*

.. _`devfreq_unregister_opp_notifier`:

devfreq_unregister_opp_notifier
===============================

.. c:function:: int devfreq_unregister_opp_notifier(struct device *dev, struct devfreq *devfreq)

    Helper function to stop getting devfreq notified for any changes in the OPP availability changes anymore.

    :param dev:
        The devfreq user device. (parent of devfreq)
    :type dev: struct device \*

    :param devfreq:
        The devfreq object.
    :type devfreq: struct devfreq \*

.. _`devfreq_unregister_opp_notifier.description`:

Description
-----------

At \ :c:func:`exit`\  callback of devfreq_dev_profile, this must be included if
devfreq_recommended_opp is used.

.. _`devm_devfreq_register_opp_notifier`:

devm_devfreq_register_opp_notifier
==================================

.. c:function:: int devm_devfreq_register_opp_notifier(struct device *dev, struct devfreq *devfreq)

    - Resource-managed \ :c:func:`devfreq_register_opp_notifier`\ 

    :param dev:
        The devfreq user device. (parent of devfreq)
    :type dev: struct device \*

    :param devfreq:
        The devfreq object.
    :type devfreq: struct devfreq \*

.. _`devm_devfreq_unregister_opp_notifier`:

devm_devfreq_unregister_opp_notifier
====================================

.. c:function:: void devm_devfreq_unregister_opp_notifier(struct device *dev, struct devfreq *devfreq)

    - Resource-managed \ :c:func:`devfreq_unregister_opp_notifier`\ 

    :param dev:
        The devfreq user device. (parent of devfreq)
    :type dev: struct device \*

    :param devfreq:
        The devfreq object.
    :type devfreq: struct devfreq \*

.. _`devfreq_register_notifier`:

devfreq_register_notifier
=========================

.. c:function:: int devfreq_register_notifier(struct devfreq *devfreq, struct notifier_block *nb, unsigned int list)

    Register a driver with devfreq

    :param devfreq:
        The devfreq object.
    :type devfreq: struct devfreq \*

    :param nb:
        The notifier block to register.
    :type nb: struct notifier_block \*

    :param list:
        DEVFREQ_TRANSITION_NOTIFIER.
    :type list: unsigned int

.. _`devm_devfreq_register_notifier`:

devm_devfreq_register_notifier
==============================

.. c:function:: int devm_devfreq_register_notifier(struct device *dev, struct devfreq *devfreq, struct notifier_block *nb, unsigned int list)

    :param dev:
        The devfreq user device. (parent of devfreq)
    :type dev: struct device \*

    :param devfreq:
        The devfreq object.
    :type devfreq: struct devfreq \*

    :param nb:
        The notifier block to be unregistered.
    :type nb: struct notifier_block \*

    :param list:
        DEVFREQ_TRANSITION_NOTIFIER.
    :type list: unsigned int

.. _`devm_devfreq_unregister_notifier`:

devm_devfreq_unregister_notifier
================================

.. c:function:: void devm_devfreq_unregister_notifier(struct device *dev, struct devfreq *devfreq, struct notifier_block *nb, unsigned int list)

    :param dev:
        The devfreq user device. (parent of devfreq)
    :type dev: struct device \*

    :param devfreq:
        The devfreq object.
    :type devfreq: struct devfreq \*

    :param nb:
        The notifier block to be unregistered.
    :type nb: struct notifier_block \*

    :param list:
        DEVFREQ_TRANSITION_NOTIFIER.
    :type list: unsigned int

.. This file was automatic generated / don't edit.

