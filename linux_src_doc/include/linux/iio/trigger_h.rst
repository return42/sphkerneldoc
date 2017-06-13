.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/iio/trigger.h

.. _`iio_trigger_ops`:

struct iio_trigger_ops
======================

.. c:type:: struct iio_trigger_ops

    operations structure for an iio_trigger.

.. _`iio_trigger_ops.definition`:

Definition
----------

.. code-block:: c

    struct iio_trigger_ops {
        struct module *owner;
        int (*set_trigger_state)(struct iio_trigger *trig, bool state);
        int (*try_reenable)(struct iio_trigger *trig);
        int (*validate_device)(struct iio_trigger *trig,struct iio_dev *indio_dev);
    }

.. _`iio_trigger_ops.members`:

Members
-------

owner
    used to monitor usage count of the trigger.

set_trigger_state
    switch on/off the trigger on demand

try_reenable
    function to reenable the trigger when the
    use count is zero (may be NULL)

validate_device
    function to validate the device when the
    current trigger gets changed.

.. _`iio_trigger_ops.description`:

Description
-----------

This is typically static const within a driver and shared by
instances of a given device.

.. _`iio_trigger`:

struct iio_trigger
==================

.. c:type:: struct iio_trigger

    industrial I/O trigger device

.. _`iio_trigger.definition`:

Definition
----------

.. code-block:: c

    struct iio_trigger {
        const struct iio_trigger_ops *ops;
        int id;
        const char *name;
        struct device dev;
        struct list_head list;
        struct list_head alloc_list;
        atomic_t use_count;
        struct irq_chip subirq_chip;
        int subirq_base;
        struct iio_subirq subirqs;
        unsigned long pool;
        struct mutex pool_lock;
        bool attached_own_device;
    }

.. _`iio_trigger.members`:

Members
-------

ops
    [DRIVER] operations structure

id
    [INTERN] unique id number

name
    [DRIVER] unique name

dev
    [DRIVER] associated device (if relevant)

list
    [INTERN] used in maintenance of global trigger list

alloc_list
    [DRIVER] used for driver specific trigger list

use_count
    use count for the trigger

subirq_chip
    [INTERN] associate 'virtual' irq chip.

subirq_base
    [INTERN] base number for irqs provided by trigger.

subirqs
    [INTERN] information about the 'child' irqs.

pool
    [INTERN] bitmap of irqs currently in use.

pool_lock
    [INTERN] protection of the irq pool.

attached_own_device
    [INTERN] if we are using our own device as trigger,
    i.e. if we registered a poll function to the same
    device as the one providing the trigger.

.. _`iio_trigger_set_drvdata`:

iio_trigger_set_drvdata
=======================

.. c:function:: void iio_trigger_set_drvdata(struct iio_trigger *trig, void *data)

    Set trigger driver data

    :param struct iio_trigger \*trig:
        IIO trigger structure

    :param void \*data:
        Driver specific data

.. _`iio_trigger_set_drvdata.description`:

Description
-----------

Allows to attach an arbitrary pointer to an IIO trigger, which can later be
retrieved by \ :c:func:`iio_trigger_get_drvdata`\ .

.. _`iio_trigger_get_drvdata`:

iio_trigger_get_drvdata
=======================

.. c:function:: void *iio_trigger_get_drvdata(struct iio_trigger *trig)

    Get trigger driver data

    :param struct iio_trigger \*trig:
        IIO trigger structure

.. _`iio_trigger_get_drvdata.description`:

Description
-----------

Returns the data previously set with \ :c:func:`iio_trigger_set_drvdata`\ 

.. _`iio_trigger_register`:

iio_trigger_register
====================

.. c:function:: int iio_trigger_register(struct iio_trigger *trig_info)

    register a trigger with the IIO core

    :param struct iio_trigger \*trig_info:
        trigger to be registered

.. _`iio_trigger_unregister`:

iio_trigger_unregister
======================

.. c:function:: void iio_trigger_unregister(struct iio_trigger *trig_info)

    unregister a trigger from the core

    :param struct iio_trigger \*trig_info:
        trigger to be unregistered

.. _`iio_trigger_set_immutable`:

iio_trigger_set_immutable
=========================

.. c:function:: int iio_trigger_set_immutable(struct iio_dev *indio_dev, struct iio_trigger *trig)

    set an immutable trigger on destination

    :param struct iio_dev \*indio_dev:
        *undescribed*

    :param struct iio_trigger \*trig:
        *undescribed*

.. _`iio_trigger_set_immutable.description`:

Description
-----------

@indio_dev - IIO device structure containing the device
\ ``trig``\  - trigger to assign to device

.. _`iio_trigger_poll`:

iio_trigger_poll
================

.. c:function:: void iio_trigger_poll(struct iio_trigger *trig)

    called on a trigger occurring

    :param struct iio_trigger \*trig:
        trigger which occurred

.. _`iio_trigger_poll.description`:

Description
-----------

Typically called in relevant hardware interrupt handler.

.. _`iio_trigger_using_own`:

iio_trigger_using_own
=====================

.. c:function:: bool iio_trigger_using_own(struct iio_dev *indio_dev)

    tells us if we use our own HW trigger ourselves

    :param struct iio_dev \*indio_dev:
        device to check

.. This file was automatic generated / don't edit.

