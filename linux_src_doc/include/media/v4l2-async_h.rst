.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-async.h

.. _`v4l2_async_match_type`:

enum v4l2_async_match_type
==========================

.. c:type:: enum v4l2_async_match_type

    type of asynchronous subdevice logic to be used in order to identify a match

.. _`v4l2_async_match_type.definition`:

Definition
----------

.. code-block:: c

    enum v4l2_async_match_type {
        V4L2_ASYNC_MATCH_CUSTOM,
        V4L2_ASYNC_MATCH_DEVNAME,
        V4L2_ASYNC_MATCH_I2C,
        V4L2_ASYNC_MATCH_FWNODE
    };

.. _`v4l2_async_match_type.constants`:

Constants
---------

V4L2_ASYNC_MATCH_CUSTOM
    Match will use the logic provided by \ :c:type:`struct v4l2_async_subdev <v4l2_async_subdev>`\ .match ops

V4L2_ASYNC_MATCH_DEVNAME
    Match will use the device name

V4L2_ASYNC_MATCH_I2C
    Match will check for I2C adapter ID and address

V4L2_ASYNC_MATCH_FWNODE
    Match will use firmware node

.. _`v4l2_async_match_type.description`:

Description
-----------

This enum is used by the asyncrhronous sub-device logic to define the
algorithm that will be used to match an asynchronous device.

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
        union {
            struct {
                struct fwnode_handle *fwnode;
            } fwnode;
            struct {
                const char *name;
            } device_name;
            struct {
                int adapter_id;
                unsigned short address;
            } i2c;
            struct {
                bool (*match)(struct device *, struct v4l2_async_subdev *);
                void *priv;
            } custom;
        } match;
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
        int (*bound)(struct v4l2_async_notifier *notifier,struct v4l2_subdev *subdev, struct v4l2_async_subdev *asd);
        int (*complete)(struct v4l2_async_notifier *notifier);
        void (*unbind)(struct v4l2_async_notifier *notifier,struct v4l2_subdev *subdev, struct v4l2_async_subdev *asd);
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

.. _`v4l2_async_notifier_register`:

v4l2_async_notifier_register
============================

.. c:function:: int v4l2_async_notifier_register(struct v4l2_device *v4l2_dev, struct v4l2_async_notifier *notifier)

    registers a subdevice asynchronous notifier

    :param struct v4l2_device \*v4l2_dev:
        pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\ 

    :param struct v4l2_async_notifier \*notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 

.. _`v4l2_async_notifier_unregister`:

v4l2_async_notifier_unregister
==============================

.. c:function:: void v4l2_async_notifier_unregister(struct v4l2_async_notifier *notifier)

    unregisters a subdevice asynchronous notifier

    :param struct v4l2_async_notifier \*notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 

.. _`v4l2_async_register_subdev`:

v4l2_async_register_subdev
==========================

.. c:function:: int v4l2_async_register_subdev(struct v4l2_subdev *sd)

    registers a sub-device to the asynchronous subdevice framework

    :param struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

.. _`v4l2_async_unregister_subdev`:

v4l2_async_unregister_subdev
============================

.. c:function:: void v4l2_async_unregister_subdev(struct v4l2_subdev *sd)

    unregisters a sub-device to the asynchronous subdevice framework

    :param struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

.. This file was automatic generated / don't edit.

