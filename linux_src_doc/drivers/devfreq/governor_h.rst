.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/devfreq/governor.h

.. _`devfreq_governor`:

struct devfreq_governor
=======================

.. c:type:: struct devfreq_governor

    Devfreq policy governor

.. _`devfreq_governor.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_governor {
        struct list_head node;
        const char name[DEVFREQ_NAME_LEN];
        const unsigned int immutable;
        int (*get_target_freq)(struct devfreq *this, unsigned long *freq);
        int (*event_handler)(struct devfreq *devfreq,unsigned int event, void *data);
    }

.. _`devfreq_governor.members`:

Members
-------

node
    list node - contains registered devfreq governors

name
    Governor's name

immutable
    Immutable flag for governor. If the value is 1,
    this govenror is never changeable to other governor.

get_target_freq
    Returns desired operating frequency for the device.
    Basically, get_target_freq will run
    devfreq_dev_profile.get_dev_status() to get the
    status of the device (load = busy_time / total_time).
    If no_central_polling is set, this callback is called
    only with \ :c:func:`update_devfreq`\  notified by OPP.

event_handler
    Callback for devfreq core framework to notify events
    to governors. Events include per device governor
    init and exit, opp changes out of devfreq, suspend
    and resume of per device devfreq during device idle.

.. _`devfreq_governor.description`:

Description
-----------

Note that the callbacks are called with devfreq->lock locked by devfreq.

.. This file was automatic generated / don't edit.

