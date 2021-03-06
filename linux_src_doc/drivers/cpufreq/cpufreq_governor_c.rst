.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/cpufreq/cpufreq_governor.c

.. _`store_sampling_rate`:

store_sampling_rate
===================

.. c:function:: ssize_t store_sampling_rate(struct gov_attr_set *attr_set, const char *buf, size_t count)

    update sampling rate effective immediately if needed.

    :param attr_set:
        *undescribed*
    :type attr_set: struct gov_attr_set \*

    :param buf:
        *undescribed*
    :type buf: const char \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`store_sampling_rate.description`:

Description
-----------

If new rate is smaller than the old, simply updating
dbs.sampling_rate might not be appropriate. For example, if the
original sampling_rate was 1 second and the requested new sampling rate is 10
ms because the user needs immediate reaction from ondemand governor, but not
sure if higher frequency will be required or not, then, the governor may
change the sampling rate too late; up to 1 second later. Thus, if we are
reducing the sampling rate, we need to make the new value effective
immediately.

This must be called with dbs_data->mutex held, otherwise traversing
policy_dbs_list isn't safe.

.. _`gov_update_cpu_data`:

gov_update_cpu_data
===================

.. c:function:: void gov_update_cpu_data(struct dbs_data *dbs_data)

    Update CPU load data.

    :param dbs_data:
        Top-level governor data pointer.
    :type dbs_data: struct dbs_data \*

.. _`gov_update_cpu_data.description`:

Description
-----------

Update CPU load data for all CPUs in the domain governed by \ ``dbs_data``\ 
(that may be a single policy or a bunch of them if governor tunables are
system-wide).

Call under the \ ``dbs_data``\  mutex.

.. This file was automatic generated / don't edit.

