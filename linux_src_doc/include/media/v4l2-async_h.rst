.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-async.h

.. _`v4l2_async_subdev`:

struct v4l2_async_subdev
========================

.. c:type:: struct v4l2_async_subdev

    sub-device descriptor, as known to a bridge

.. _`v4l2_async_subdev.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_async_subdev {
        enum v4l2_async_match_type match_type;
        union match;
        struct list_head list;
    }

.. _`v4l2_async_subdev.members`:

Members
-------

match_type
    type of match that will be used

match
    union of per-bus type matching data sets

list
    used to link struct v4l2_async_subdev objects, waiting to be
    probed, to a notifier->waiting list

.. _`v4l2_async_notifier`:

struct v4l2_async_notifier
==========================

.. c:type:: struct v4l2_async_notifier

    v4l2_device notifier data

.. _`v4l2_async_notifier.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_async_notifier {
        unsigned int num_subdevs;
        struct v4l2_async_subdev **subdevs;
        struct v4l2_device *v4l2_dev;
        struct list_head waiting;
        struct list_head done;
        struct list_head list;
        int (*bound)(struct v4l2_async_notifier *notifier,struct v4l2_subdev *subdev,struct v4l2_async_subdev *asd);
        int (*complete)(struct v4l2_async_notifier *notifier);
        void (*unbind)(struct v4l2_async_notifier *notifier,struct v4l2_subdev *subdev,struct v4l2_async_subdev *asd);
    }

.. _`v4l2_async_notifier.members`:

Members
-------

num_subdevs
    number of subdevices

subdevs
    array of pointers to subdevice descriptors

v4l2_dev
    pointer to struct v4l2_device

waiting
    list of struct v4l2_async_subdev, waiting for their drivers

done
    list of struct v4l2_subdev, already probed

list
    member in a global list of notifiers

bound
    a subdevice driver has successfully probed one of subdevices

complete
    all subdevices have been probed successfully

unbind
    a subdevice is leaving

.. This file was automatic generated / don't edit.

