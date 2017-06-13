.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/devfreq.h

.. _`devfreq_dev_status`:

struct devfreq_dev_status
=========================

.. c:type:: struct devfreq_dev_status

    Data given from devfreq user device to governors. Represents the performance statistics.

.. _`devfreq_dev_status.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_dev_status {
        unsigned long total_time;
        unsigned long busy_time;
        unsigned long current_frequency;
        void *private_data;
    }

.. _`devfreq_dev_status.members`:

Members
-------

total_time
    The total time represented by this instance of
    devfreq_dev_status

busy_time
    The time that the device was working among the
    total_time.

current_frequency
    The operating frequency.

private_data
    An entry not specified by the devfreq framework.
    A device and a specific governor may have their
    own protocol with private_data. However, because
    this is governor-specific, a governor using this
    will be only compatible with devices aware of it.

.. _`devfreq_dev_profile`:

struct devfreq_dev_profile
==========================

.. c:type:: struct devfreq_dev_profile

    Devfreq's user device profile

.. _`devfreq_dev_profile.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_dev_profile {
        unsigned long initial_freq;
        unsigned int polling_ms;
        int (*target)(struct device *dev, unsigned long *freq, u32 flags);
        int (*get_dev_status)(struct device *dev,struct devfreq_dev_status *stat);
        int (*get_cur_freq)(struct device *dev, unsigned long *freq);
        void (*exit)(struct device *dev);
        unsigned long *freq_table;
        unsigned int max_state;
    }

.. _`devfreq_dev_profile.members`:

Members
-------

initial_freq
    The operating frequency when \ :c:func:`devfreq_add_device`\  is
    called.

polling_ms
    The polling interval in ms. 0 disables polling.

target
    The device should set its operating frequency at
    freq or lowest-upper-than-freq value. If freq is
    higher than any operable frequency, set maximum.
    Before returning, target function should set
    freq at the current frequency.
    The "flags" parameter's possible values are
    explained above with "DEVFREQ_FLAG\_\*" macros.

get_dev_status
    The device should provide the current performance
    status to devfreq. Governors are recommended not to
    use this directly. Instead, governors are recommended
    to use \ :c:func:`devfreq_update_stats`\  along with
    devfreq.last_status.

get_cur_freq
    The device should provide the current frequency
    at which it is operating.

exit
    An optional callback that is called when devfreq
    is removing the devfreq object due to error or
    from \ :c:func:`devfreq_remove_device`\  call. If the user
    has registered devfreq->nb at a notifier-head,
    this is the time to unregister it.

freq_table
    Optional list of frequencies to support statistics.

max_state
    The size of freq_table.

.. _`devfreq`:

struct devfreq
==============

.. c:type:: struct devfreq

    Device devfreq structure

.. _`devfreq.definition`:

Definition
----------

.. code-block:: c

    struct devfreq {
        struct list_head node;
        struct mutex lock;
        struct device dev;
        struct devfreq_dev_profile *profile;
        const struct devfreq_governor *governor;
        char governor_name;
        struct notifier_block nb;
        struct delayed_work work;
        unsigned long previous_freq;
        struct devfreq_dev_status last_status;
        void *data;
        unsigned long min_freq;
        unsigned long max_freq;
        bool stop_polling;
        unsigned int total_trans;
        unsigned int *trans_table;
        unsigned long *time_in_state;
        unsigned long last_stat_updated;
        struct srcu_notifier_head transition_notifier_list;
    }

.. _`devfreq.members`:

Members
-------

node
    list node - contains the devices with devfreq that have been
    registered.

lock
    a mutex to protect accessing devfreq.

dev
    device registered by devfreq class. dev.parent is the device
    using devfreq.

profile
    device-specific devfreq profile

governor
    method how to choose frequency based on the usage.

governor_name
    devfreq governor name for use with this devfreq

nb
    notifier block used to notify devfreq object that it should
    reevaluate operable frequencies. Devfreq users may use
    devfreq.nb to the corresponding register notifier call chain.

work
    delayed work for load monitoring.

previous_freq
    previously configured frequency value.

last_status
    *undescribed*

data
    Private data of the governor. The devfreq framework does not
    touch this.

min_freq
    Limit minimum frequency requested by user (0: none)

max_freq
    Limit maximum frequency requested by user (0: none)

stop_polling
    devfreq polling status of a device.

total_trans
    Number of devfreq transitions

trans_table
    Statistics of devfreq transitions

time_in_state
    Statistics of devfreq states

last_stat_updated
    The last time stat updated

transition_notifier_list
    list head of DEVFREQ_TRANSITION_NOTIFIER notifier

.. _`devfreq.description`:

Description
-----------

This structure stores the devfreq information for a give device.

Note that when a governor accesses entries in struct devfreq in its
functions except for the context of callbacks defined in struct
devfreq_governor, the governor should protect its access with the
struct mutex lock in struct devfreq. A governor may use this mutex
to protect its own private data in void \*data as well.

.. _`devfreq_update_stats`:

devfreq_update_stats
====================

.. c:function:: int devfreq_update_stats(struct devfreq *df)

    update the last_status pointer in struct devfreq

    :param struct devfreq \*df:
        the devfreq instance whose status needs updating

.. _`devfreq_update_stats.description`:

Description
-----------

Governors are recommended to use this function along with last_status,
which allows other entities to reuse the last_status without affecting
the values fetched later by governors.

.. _`devfreq_simple_ondemand_data`:

struct devfreq_simple_ondemand_data
===================================

.. c:type:: struct devfreq_simple_ondemand_data

    void \*data fed to struct devfreq and devfreq_add_device

.. _`devfreq_simple_ondemand_data.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_simple_ondemand_data {
        unsigned int upthreshold;
        unsigned int downdifferential;
    }

.. _`devfreq_simple_ondemand_data.members`:

Members
-------

upthreshold
    If the load is over this value, the frequency jumps.
    Specify 0 to use the default. Valid value = 0 to 100.

downdifferential
    If the load is under upthreshold - downdifferential,
    the governor may consider slowing the frequency down.
    Specify 0 to use the default. Valid value = 0 to 100.
    downdifferential < upthreshold must hold.

.. _`devfreq_simple_ondemand_data.description`:

Description
-----------

If the fed devfreq_simple_ondemand_data pointer is NULL to the governor,
the governor uses the default values.

.. _`devfreq_passive_data`:

struct devfreq_passive_data
===========================

.. c:type:: struct devfreq_passive_data

    void \*data fed to struct devfreq and devfreq_add_device

.. _`devfreq_passive_data.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_passive_data {
        struct devfreq *parent;
        int (*get_target_freq)(struct devfreq *this, unsigned long *freq);
        struct devfreq *this;
        struct notifier_block nb;
    }

.. _`devfreq_passive_data.members`:

Members
-------

parent
    the devfreq instance of parent device.

get_target_freq
    Optional callback, Returns desired operating frequency
    for the device using passive governor. That is called
    when passive governor should decide the next frequency
    by using the new frequency of parent devfreq device
    using governors except for passive governor.
    If the devfreq device has the specific method to decide
    the next frequency, should use this callback.

this
    the devfreq instance of own device.

nb
    the notifier block for DEVFREQ_TRANSITION_NOTIFIER list

.. _`devfreq_passive_data.description`:

Description
-----------

The devfreq_passive_data have to set the devfreq instance of parent
device with governors except for the passive governor. But, don't need to
initialize the 'this' and 'nb' field because the devfreq core will handle
them.

.. This file was automatic generated / don't edit.

