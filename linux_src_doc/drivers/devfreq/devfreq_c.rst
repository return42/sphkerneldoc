.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/devfreq/devfreq.c

.. _`find_device_devfreq`:

find_device_devfreq
===================

.. c:function:: struct devfreq *find_device_devfreq(struct device *dev)

    find devfreq struct using device pointer

    :param struct device \*dev:
        device pointer used to lookup device devfreq.

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

    :param struct devfreq \*devfreq:
        the devfreq instance

    :param unsigned long freq:
        the target frequency

.. _`devfreq_set_freq_table`:

devfreq_set_freq_table
======================

.. c:function:: void devfreq_set_freq_table(struct devfreq *devfreq)

    Initialize freq_table for the frequency

    :param struct devfreq \*devfreq:
        the devfreq instance

.. _`devfreq_update_status`:

devfreq_update_status
=====================

.. c:function:: int devfreq_update_status(struct devfreq *devfreq, unsigned long freq)

    Update statistics of devfreq behavior

    :param struct devfreq \*devfreq:
        the devfreq instance

    :param unsigned long freq:
        the update target frequency

.. _`find_devfreq_governor`:

find_devfreq_governor
=====================

.. c:function:: struct devfreq_governor *find_devfreq_governor(const char *name)

    find devfreq governor from name

    :param const char \*name:
        name of the governor

.. _`find_devfreq_governor.description`:

Description
-----------

Search the list of devfreq governors and return the matched
governor's pointer. devfreq_list_lock should be held by the caller.

.. _`update_devfreq`:

update_devfreq
==============

.. c:function:: int update_devfreq(struct devfreq *devfreq)

    Reevaluate the device and configure frequency.

    :param struct devfreq \*devfreq:
        the devfreq instance.

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

    :param struct work_struct \*work:
        the work struct used to run devfreq_monitor periodically.

.. _`devfreq_monitor_start`:

devfreq_monitor_start
=====================

.. c:function:: void devfreq_monitor_start(struct devfreq *devfreq)

    Start load monitoring of devfreq instance

    :param struct devfreq \*devfreq:
        the devfreq instance.

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

    :param struct devfreq \*devfreq:
        the devfreq instance.

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

    :param struct devfreq \*devfreq:
        the devfreq instance.

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

    :param struct devfreq \*devfreq:
        the devfreq instance.

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

    :param struct devfreq \*devfreq:
        the devfreq instance.

    :param unsigned int \*delay:
        new polling interval to be set.

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

    :param struct notifier_block \*nb:
        the notifier_block (supposed to be devfreq->nb)

    :param unsigned long type:
        not used

    :param void \*devp:
        not used

.. _`devfreq_notifier_call.description`:

Description
-----------

Called by a notifier that uses devfreq->nb.

.. _`devfreq_dev_release`:

devfreq_dev_release
===================

.. c:function:: void devfreq_dev_release(struct device *dev)

    Callback for struct device to release the device.

    :param struct device \*dev:
        the devfreq device

.. _`devfreq_dev_release.description`:

Description
-----------

Remove devfreq from the list and release its resources.

.. _`devfreq_add_device`:

devfreq_add_device
==================

.. c:function:: struct devfreq *devfreq_add_device(struct device *dev, struct devfreq_dev_profile *profile, const char *governor_name, void *data)

    Add devfreq feature to the device

    :param struct device \*dev:
        the device to add devfreq feature.

    :param struct devfreq_dev_profile \*profile:
        device-specific profile to run devfreq.

    :param const char \*governor_name:
        name of the policy to choose frequency.

    :param void \*data:
        private data for the governor. The devfreq framework does not
        touch this value.

.. _`devfreq_remove_device`:

devfreq_remove_device
=====================

.. c:function:: int devfreq_remove_device(struct devfreq *devfreq)

    Remove devfreq feature from a device.

    :param struct devfreq \*devfreq:
        the devfreq instance to be removed

.. _`devfreq_remove_device.description`:

Description
-----------

The opposite of \ :c:func:`devfreq_add_device`\ .

.. _`devm_devfreq_add_device`:

devm_devfreq_add_device
=======================

.. c:function:: struct devfreq *devm_devfreq_add_device(struct device *dev, struct devfreq_dev_profile *profile, const char *governor_name, void *data)

    Resource-managed \ :c:func:`devfreq_add_device`\ 

    :param struct device \*dev:
        the device to add devfreq feature.

    :param struct devfreq_dev_profile \*profile:
        device-specific profile to run devfreq.

    :param const char \*governor_name:
        name of the policy to choose frequency.

    :param void \*data:
        private data for the governor. The devfreq framework does not
        touch this value.

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

    :param struct device \*dev:
        the device to add devfreq feature.

    :param struct devfreq \*devfreq:
        the devfreq instance to be removed

.. _`devfreq_suspend_device`:

devfreq_suspend_device
======================

.. c:function:: int devfreq_suspend_device(struct devfreq *devfreq)

    Suspend devfreq of a device.

    :param struct devfreq \*devfreq:
        the devfreq instance to be suspended

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

    :param struct devfreq \*devfreq:
        the devfreq instance to be resumed

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

    :param struct devfreq_governor \*governor:
        the devfreq governor to be added

.. _`devfreq_remove_governor`:

devfreq_remove_governor
=======================

.. c:function:: int devfreq_remove_governor(struct devfreq_governor *governor)

    Remove devfreq feature from a device.

    :param struct devfreq_governor \*governor:
        the devfreq governor to be removed

.. _`devfreq_recommended_opp`:

devfreq_recommended_opp
=======================

.. c:function:: struct dev_pm_opp *devfreq_recommended_opp(struct device *dev, unsigned long *freq, u32 flags)

    Helper function to get proper OPP for the freq value given to target callback.

    :param struct device \*dev:
        The devfreq user device. (parent of devfreq)

    :param unsigned long \*freq:
        The frequency given to target function

    :param u32 flags:
        Flags handed from devfreq framework.

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

    :param struct device \*dev:
        The devfreq user device. (parent of devfreq)

    :param struct devfreq \*devfreq:
        The devfreq object.

.. _`devfreq_unregister_opp_notifier`:

devfreq_unregister_opp_notifier
===============================

.. c:function:: int devfreq_unregister_opp_notifier(struct device *dev, struct devfreq *devfreq)

    Helper function to stop getting devfreq notified for any changes in the OPP availability changes anymore.

    :param struct device \*dev:
        The devfreq user device. (parent of devfreq)

    :param struct devfreq \*devfreq:
        The devfreq object.

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

    :param struct device \*dev:
        The devfreq user device. (parent of devfreq)

    :param struct devfreq \*devfreq:
        The devfreq object.

.. _`devm_devfreq_unregister_opp_notifier`:

devm_devfreq_unregister_opp_notifier
====================================

.. c:function:: void devm_devfreq_unregister_opp_notifier(struct device *dev, struct devfreq *devfreq)

    - Resource-managed \ :c:func:`devfreq_unregister_opp_notifier`\ 

    :param struct device \*dev:
        The devfreq user device. (parent of devfreq)

    :param struct devfreq \*devfreq:
        The devfreq object.

.. _`devfreq_register_notifier`:

devfreq_register_notifier
=========================

.. c:function:: int devfreq_register_notifier(struct devfreq *devfreq, struct notifier_block *nb, unsigned int list)

    Register a driver with devfreq

    :param struct devfreq \*devfreq:
        The devfreq object.

    :param struct notifier_block \*nb:
        The notifier block to register.

    :param unsigned int list:
        DEVFREQ_TRANSITION_NOTIFIER.

.. _`devm_devfreq_register_notifier`:

devm_devfreq_register_notifier
==============================

.. c:function:: int devm_devfreq_register_notifier(struct device *dev, struct devfreq *devfreq, struct notifier_block *nb, unsigned int list)

    :param struct device \*dev:
        The devfreq user device. (parent of devfreq)

    :param struct devfreq \*devfreq:
        The devfreq object.

    :param struct notifier_block \*nb:
        The notifier block to be unregistered.

    :param unsigned int list:
        DEVFREQ_TRANSITION_NOTIFIER.

.. _`devm_devfreq_unregister_notifier`:

devm_devfreq_unregister_notifier
================================

.. c:function:: void devm_devfreq_unregister_notifier(struct device *dev, struct devfreq *devfreq, struct notifier_block *nb, unsigned int list)

    :param struct device \*dev:
        The devfreq user device. (parent of devfreq)

    :param struct devfreq \*devfreq:
        The devfreq object.

    :param struct notifier_block \*nb:
        The notifier block to be unregistered.

    :param unsigned int list:
        DEVFREQ_TRANSITION_NOTIFIER.

.. This file was automatic generated / don't edit.

