.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/devfreq-event.h

.. _`devfreq_event_dev`:

struct devfreq_event_dev
========================

.. c:type:: struct devfreq_event_dev

    the devfreq-event device

.. _`devfreq_event_dev.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_event_dev {
        struct list_head node;
        struct device dev;
        struct mutex lock;
        u32 enable_count;
        const struct devfreq_event_desc *desc;
    }

.. _`devfreq_event_dev.members`:

Members
-------

node
    Contain the devfreq-event device that have been registered.

dev
    the device registered by devfreq-event class. dev.parent is
    the device using devfreq-event.

lock
    a mutex to protect accessing devfreq-event.

enable_count
    the number of enable function have been called.

desc
    the description for devfreq-event device.

.. _`devfreq_event_dev.description`:

Description
-----------

This structure contains devfreq-event device information.

.. _`devfreq_event_data`:

struct devfreq_event_data
=========================

.. c:type:: struct devfreq_event_data

    the devfreq-event data

.. _`devfreq_event_data.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_event_data {
        unsigned long load_count;
        unsigned long total_count;
    }

.. _`devfreq_event_data.members`:

Members
-------

load_count
    load count of devfreq-event device for the given period.

total_count
    total count of devfreq-event device for the given period.
    each count may represent a clock cycle, a time unit
    (ns/us/...), or anything the device driver wants.
    Generally, utilization is load_count / total_count.

.. _`devfreq_event_data.description`:

Description
-----------

This structure contains the data of devfreq-event device for polling period.

.. _`devfreq_event_ops`:

struct devfreq_event_ops
========================

.. c:type:: struct devfreq_event_ops

    the operations of devfreq-event device

.. _`devfreq_event_ops.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_event_ops {
        int (*enable)(struct devfreq_event_dev *edev);
        int (*disable)(struct devfreq_event_dev *edev);
        int (*reset)(struct devfreq_event_dev *edev);
        int (*set_event)(struct devfreq_event_dev *edev);
        int (*get_event)(struct devfreq_event_dev *edev, struct devfreq_event_data *edata);
    }

.. _`devfreq_event_ops.members`:

Members
-------

enable
    Enable the devfreq-event device.

disable
    Disable the devfreq-event device.

reset
    Reset all setting of the devfreq-event device.

set_event
    Set the specific event type for the devfreq-event device.

get_event
    Get the result of the devfreq-event devie with specific
    event type.

.. _`devfreq_event_ops.description`:

Description
-----------

This structure contains devfreq-event device operations which can be
implemented by devfreq-event device drivers.

.. _`devfreq_event_desc`:

struct devfreq_event_desc
=========================

.. c:type:: struct devfreq_event_desc

    the descriptor of devfreq-event device

.. _`devfreq_event_desc.definition`:

Definition
----------

.. code-block:: c

    struct devfreq_event_desc {
        const char *name;
        void *driver_data;
        const struct devfreq_event_ops *ops;
    }

.. _`devfreq_event_desc.members`:

Members
-------

name
    the name of devfreq-event device.

driver_data
    the private data for devfreq-event driver.

ops
    the operation to control devfreq-event device.

.. _`devfreq_event_desc.description`:

Description
-----------

Each devfreq-event device is described with a this structure.
This structure contains the various data for devfreq-event device.

.. This file was automatic generated / don't edit.

