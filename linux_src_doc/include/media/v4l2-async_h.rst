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
    Match will use the logic provided by \ :c:type:`struct struct <struct>`\ 
    v4l2_async_subdev.match ops

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
            struct fwnode_handle *fwnode;
            const char *device_name;
            struct {
                int adapter_id;
                unsigned short address;
            } i2c;
            struct {
                bool (*match)(struct device *dev, struct v4l2_async_subdev *sd);
                void *priv;
            } custom;
        } match;
        struct list_head list;
        struct list_head asd_list;
    }

.. _`v4l2_async_subdev.members`:

Members
-------

match_type
    type of match that will be used

match
    union of per-bus type matching data sets

match.fwnode
    pointer to \ :c:type:`struct fwnode_handle <fwnode_handle>`\  to be matched.
    Used if \ ``match_type``\  is \ ``V4L2_ASYNC_MATCH_FWNODE``\ .

match.device_name
    string containing the device name to be matched.
    Used if \ ``match_type``\  is \ ``V4L2_ASYNC_MATCH_DEVNAME``\ .

match.i2c
    embedded struct with I2C parameters to be matched.
    Both \ ``match.i2c.adapter_id``\  and \ ``match.i2c.address``\ 
    should be matched.
    Used if \ ``match_type``\  is \ ``V4L2_ASYNC_MATCH_I2C``\ .

match.i2c.adapter_id
    I2C adapter ID to be matched.
    Used if \ ``match_type``\  is \ ``V4L2_ASYNC_MATCH_I2C``\ .

match.i2c.address
    I2C address to be matched.
    Used if \ ``match_type``\  is \ ``V4L2_ASYNC_MATCH_I2C``\ .

match.custom
    Driver-specific match criteria.
    Used if \ ``match_type``\  is \ ``V4L2_ASYNC_MATCH_CUSTOM``\ .

match.custom.match
    Driver-specific match function to be used if
    \ ``V4L2_ASYNC_MATCH_CUSTOM``\ .

match.custom.priv
    Driver-specific private struct with match parameters
    to be used if \ ``V4L2_ASYNC_MATCH_CUSTOM``\ .

list
    used to link struct v4l2_async_subdev objects, waiting to be
    probed, to a notifier->waiting list

asd_list
    used to add struct v4l2_async_subdev objects to the
    master notifier \ ``asd_list``\ 

.. _`v4l2_async_subdev.description`:

Description
-----------

When this struct is used as a member in a driver specific struct,
the driver specific struct shall contain the \ :c:type:`struct struct <struct>`\ 
v4l2_async_subdev as its first member.

.. _`v4l2_async_notifier_operations`:

struct v4l2_async_notifier_operations
=====================================

.. c:type:: struct v4l2_async_notifier_operations

    Asynchronous V4L2 notifier operations

.. _`v4l2_async_notifier_operations.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_async_notifier_operations {
        int (*bound)(struct v4l2_async_notifier *notifier,struct v4l2_subdev *subdev, struct v4l2_async_subdev *asd);
        int (*complete)(struct v4l2_async_notifier *notifier);
        void (*unbind)(struct v4l2_async_notifier *notifier,struct v4l2_subdev *subdev, struct v4l2_async_subdev *asd);
    }

.. _`v4l2_async_notifier_operations.members`:

Members
-------

bound
    a subdevice driver has successfully probed one of the subdevices

complete
    All subdevices have been probed successfully. The complete
    callback is only executed for the root notifier.

unbind
    a subdevice is leaving

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
        const struct v4l2_async_notifier_operations *ops;
        struct v4l2_device *v4l2_dev;
        struct v4l2_subdev *sd;
        struct v4l2_async_notifier *parent;
        struct list_head asd_list;
        struct list_head waiting;
        struct list_head done;
        struct list_head list;
    }

.. _`v4l2_async_notifier.members`:

Members
-------

ops
    notifier operations

v4l2_dev
    v4l2_device of the root notifier, NULL otherwise

sd
    sub-device that registered the notifier, NULL otherwise

parent
    parent notifier

asd_list
    master list of struct v4l2_async_subdev

waiting
    list of struct v4l2_async_subdev, waiting for their drivers

done
    list of struct v4l2_subdev, already probed

list
    member in a global list of notifiers

.. _`v4l2_async_notifier_init`:

v4l2_async_notifier_init
========================

.. c:function:: void v4l2_async_notifier_init(struct v4l2_async_notifier *notifier)

    Initialize a notifier.

    :param notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 
    :type notifier: struct v4l2_async_notifier \*

.. _`v4l2_async_notifier_init.description`:

Description
-----------

This function initializes the notifier \ ``asd_list``\ . It must be called
before the first call to \ ``v4l2_async_notifier_add_subdev``\ .

.. _`v4l2_async_notifier_add_subdev`:

v4l2_async_notifier_add_subdev
==============================

.. c:function:: int v4l2_async_notifier_add_subdev(struct v4l2_async_notifier *notifier, struct v4l2_async_subdev *asd)

    Add an async subdev to the notifier's master asd list.

    :param notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 
    :type notifier: struct v4l2_async_notifier \*

    :param asd:
        pointer to \ :c:type:`struct v4l2_async_subdev <v4l2_async_subdev>`\ 
    :type asd: struct v4l2_async_subdev \*

.. _`v4l2_async_notifier_add_subdev.description`:

Description
-----------

Call this function before registering a notifier to link the
provided asd to the notifiers master \ ``asd_list``\ .

.. _`v4l2_async_notifier_add_fwnode_subdev`:

v4l2_async_notifier_add_fwnode_subdev
=====================================

.. c:function:: struct v4l2_async_subdev *v4l2_async_notifier_add_fwnode_subdev(struct v4l2_async_notifier *notifier, struct fwnode_handle *fwnode, unsigned int asd_struct_size)

    Allocate and add a fwnode async subdev to the notifier's master asd_list.

    :param notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 
    :type notifier: struct v4l2_async_notifier \*

    :param fwnode:
        fwnode handle of the sub-device to be matched
    :type fwnode: struct fwnode_handle \*

    :param asd_struct_size:
        size of the driver's async sub-device struct, including
        sizeof(struct v4l2_async_subdev). The \ :c:type:`struct struct <struct>`\ 
        v4l2_async_subdev shall be the first member of
        the driver's async sub-device struct, i.e. both
        begin at the same memory address.
    :type asd_struct_size: unsigned int

.. _`v4l2_async_notifier_add_fwnode_subdev.description`:

Description
-----------

Allocate a fwnode-matched asd of size asd_struct_size, and add it
to the notifiers \ ``asd_list``\ .

.. _`v4l2_async_notifier_add_i2c_subdev`:

v4l2_async_notifier_add_i2c_subdev
==================================

.. c:function:: struct v4l2_async_subdev *v4l2_async_notifier_add_i2c_subdev(struct v4l2_async_notifier *notifier, int adapter_id, unsigned short address, unsigned int asd_struct_size)

    Allocate and add an i2c async subdev to the notifier's master asd_list.

    :param notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 
    :type notifier: struct v4l2_async_notifier \*

    :param adapter_id:
        I2C adapter ID to be matched
    :type adapter_id: int

    :param address:
        I2C address of sub-device to be matched
    :type address: unsigned short

    :param asd_struct_size:
        size of the driver's async sub-device struct, including
        sizeof(struct v4l2_async_subdev). The \ :c:type:`struct struct <struct>`\ 
        v4l2_async_subdev shall be the first member of
        the driver's async sub-device struct, i.e. both
        begin at the same memory address.
    :type asd_struct_size: unsigned int

.. _`v4l2_async_notifier_add_i2c_subdev.description`:

Description
-----------

Same as above but for I2C matched sub-devices.

.. _`v4l2_async_notifier_add_devname_subdev`:

v4l2_async_notifier_add_devname_subdev
======================================

.. c:function:: struct v4l2_async_subdev *v4l2_async_notifier_add_devname_subdev(struct v4l2_async_notifier *notifier, const char *device_name, unsigned int asd_struct_size)

    Allocate and add a device-name async subdev to the notifier's master asd_list.

    :param notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 
    :type notifier: struct v4l2_async_notifier \*

    :param device_name:
        device name string to be matched
    :type device_name: const char \*

    :param asd_struct_size:
        size of the driver's async sub-device struct, including
        sizeof(struct v4l2_async_subdev). The \ :c:type:`struct struct <struct>`\ 
        v4l2_async_subdev shall be the first member of
        the driver's async sub-device struct, i.e. both
        begin at the same memory address.
    :type asd_struct_size: unsigned int

.. _`v4l2_async_notifier_add_devname_subdev.description`:

Description
-----------

Same as above but for device-name matched sub-devices.

.. _`v4l2_async_notifier_register`:

v4l2_async_notifier_register
============================

.. c:function:: int v4l2_async_notifier_register(struct v4l2_device *v4l2_dev, struct v4l2_async_notifier *notifier)

    registers a subdevice asynchronous notifier

    :param v4l2_dev:
        pointer to \ :c:type:`struct v4l2_device <v4l2_device>`\ 
    :type v4l2_dev: struct v4l2_device \*

    :param notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 
    :type notifier: struct v4l2_async_notifier \*

.. _`v4l2_async_subdev_notifier_register`:

v4l2_async_subdev_notifier_register
===================================

.. c:function:: int v4l2_async_subdev_notifier_register(struct v4l2_subdev *sd, struct v4l2_async_notifier *notifier)

    registers a subdevice asynchronous notifier for a sub-device

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

    :param notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 
    :type notifier: struct v4l2_async_notifier \*

.. _`v4l2_async_notifier_unregister`:

v4l2_async_notifier_unregister
==============================

.. c:function:: void v4l2_async_notifier_unregister(struct v4l2_async_notifier *notifier)

    unregisters a subdevice asynchronous notifier

    :param notifier:
        pointer to \ :c:type:`struct v4l2_async_notifier <v4l2_async_notifier>`\ 
    :type notifier: struct v4l2_async_notifier \*

.. _`v4l2_async_notifier_cleanup`:

v4l2_async_notifier_cleanup
===========================

.. c:function:: void v4l2_async_notifier_cleanup(struct v4l2_async_notifier *notifier)

    clean up notifier resources

    :param notifier:
        the notifier the resources of which are to be cleaned up
    :type notifier: struct v4l2_async_notifier \*

.. _`v4l2_async_notifier_cleanup.description`:

Description
-----------

Release memory resources related to a notifier, including the async
sub-devices allocated for the purposes of the notifier but not the notifier
itself. The user is responsible for calling this function to clean up the
notifier after calling
\ ``v4l2_async_notifier_add_subdev``\ ,
\ ``v4l2_async_notifier_parse_fwnode_endpoints``\  or
\ ``v4l2_fwnode_reference_parse_sensor_common``\ .

There is no harm from calling v4l2_async_notifier_cleanup in other
cases as long as its memory has been zeroed after it has been
allocated.

.. _`v4l2_async_register_subdev`:

v4l2_async_register_subdev
==========================

.. c:function:: int v4l2_async_register_subdev(struct v4l2_subdev *sd)

    registers a sub-device to the asynchronous subdevice framework

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

.. _`v4l2_async_register_subdev_sensor_common`:

v4l2_async_register_subdev_sensor_common
========================================

.. c:function:: int v4l2_async_register_subdev_sensor_common(struct v4l2_subdev *sd)

    registers a sensor sub-device to the asynchronous sub-device framework and parse set up common sensor related devices

    :param sd:
        pointer to struct \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

.. _`v4l2_async_register_subdev_sensor_common.description`:

Description
-----------

This function is just like \ :c:func:`v4l2_async_register_subdev`\  with the exception
that calling it will also parse firmware interfaces for remote references
using \ :c:func:`v4l2_async_notifier_parse_fwnode_sensor_common`\  and registers the
async sub-devices. The sub-device is similarly unregistered by calling
\ :c:func:`v4l2_async_unregister_subdev`\ .

While registered, the subdev module is marked as in-use.

An error is returned if the module is no longer loaded on any attempts
to register it.

.. _`v4l2_async_unregister_subdev`:

v4l2_async_unregister_subdev
============================

.. c:function:: void v4l2_async_unregister_subdev(struct v4l2_subdev *sd)

    unregisters a sub-device to the asynchronous subdevice framework

    :param sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 
    :type sd: struct v4l2_subdev \*

.. This file was automatic generated / don't edit.

