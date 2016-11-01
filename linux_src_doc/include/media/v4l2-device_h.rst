.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-device.h

.. _`v4l2_device`:

struct v4l2_device
==================

.. c:type:: struct v4l2_device

    main struct to for V4L2 device drivers

.. _`v4l2_device.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_device {
        struct device *dev;
    #if defined(CONFIG_MEDIA_CONTROLLER)
        struct media_device *mdev;
    #endif
        struct list_head subdevs;
        spinlock_t lock;
        char name[V4L2_DEVICE_NAME_SIZE];
        void (*notify)(struct v4l2_subdev *sd,unsigned int notification, void *arg);
        struct v4l2_ctrl_handler *ctrl_handler;
        struct v4l2_prio_state prio;
        struct kref ref;
        void (*release)(struct v4l2_device *v4l2_dev);
    }

.. _`v4l2_device.members`:

Members
-------

dev
    pointer to struct device.

mdev
    pointer to struct media_device

subdevs
    used to keep track of the registered subdevs

lock
    lock this struct; can be used by the driver as well
    if this struct is embedded into a larger struct.

name
    unique device name, by default the driver name + bus ID

notify
    notify callback called by some sub-devices.

ctrl_handler
    The control handler. May be \ ``NULL``\ .

prio
    Device's priority state

ref
    Keep track of the references to this struct.

release
    Release function that is called when the ref count
    goes to 0.

.. _`v4l2_device.description`:

Description
-----------

Each instance of a V4L2 device should create the v4l2_device struct,
either stand-alone or embedded in a larger struct.

It allows easy access to sub-devices (see v4l2-subdev.h) and provides
basic V4L2 device-level support.

.. note::

   #) \ ``dev``\ ->driver_data points to this struct.
   #) \ ``dev``\  might be \ ``NULL``\  if there is no parent device

.. _`v4l2_device_get`:

v4l2_device_get
===============

.. c:function:: void v4l2_device_get(struct v4l2_device *v4l2_dev)

    gets a V4L2 device reference

    :param struct v4l2_device \*v4l2_dev:
        pointer to struct \ :c:type:`struct v4l2_device <v4l2_device>`\ 

.. _`v4l2_device_get.description`:

Description
-----------

This is an ancillary routine meant to increment the usage for the
struct \ :c:type:`struct v4l2_device <v4l2_device>`\  pointed by \ ``v4l2_dev``\ .

.. _`v4l2_device_put`:

v4l2_device_put
===============

.. c:function:: int v4l2_device_put(struct v4l2_device *v4l2_dev)

    putss a V4L2 device reference

    :param struct v4l2_device \*v4l2_dev:
        pointer to struct \ :c:type:`struct v4l2_device <v4l2_device>`\ 

.. _`v4l2_device_put.description`:

Description
-----------

This is an ancillary routine meant to decrement the usage for the
struct \ :c:type:`struct v4l2_device <v4l2_device>`\  pointed by \ ``v4l2_dev``\ .

.. _`v4l2_device_register`:

v4l2_device_register
====================

.. c:function:: int v4l2_device_register(struct device *dev, struct v4l2_device *v4l2_dev)

    Initialize v4l2_dev and make \ ``dev``\ ->driver_data point to \ ``v4l2_dev``\ .

    :param struct device \*dev:
        pointer to struct \ :c:type:`struct device <device>`\ 

    :param struct v4l2_device \*v4l2_dev:
        pointer to struct \ :c:type:`struct v4l2_device <v4l2_device>`\ 

.. _`v4l2_device_register.description`:

Description
-----------

.. note::
     \ ``dev``\  may be \ ``NULL``\  in rare cases (ISA devices).
     In such case the caller must fill in the \ ``v4l2_dev``\ ->name field
     before calling this function.

.. _`v4l2_device_set_name`:

v4l2_device_set_name
====================

.. c:function:: int v4l2_device_set_name(struct v4l2_device *v4l2_dev, const char *basename, atomic_t *instance)

    Optional function to initialize the name field of struct \ :c:type:`struct v4l2_device <v4l2_device>`\ 

    :param struct v4l2_device \*v4l2_dev:
        pointer to struct \ :c:type:`struct v4l2_device <v4l2_device>`\ 

    :param const char \*basename:
        base name for the device name

    :param atomic_t \*instance:
        pointer to a static atomic_t var with the instance usage for
        the device driver.

.. _`v4l2_device_set_name.description`:

Description
-----------

v4l2_device_set_name() initializes the name field of struct \ :c:type:`struct v4l2_device <v4l2_device>`\ 
using the driver name and a driver-global atomic_t instance.

This function will increment the instance counter and returns the
instance value used in the name.

.. _`v4l2_device_set_name.example`:

Example
-------

.. code-block:: c


      static atomic_t drv_instance = ATOMIC_INIT(0);

      ...

      instance = v4l2_device_set_name(&\ v4l2_dev, "foo", &\ drv_instance);

    The first time this is called the name field will be set to foo0 and
    this function returns 0. If the name ends with a digit (e.g. cx18),
    then the name will be set to cx18-0 since cx180 would look really odd.


.. _`v4l2_device_disconnect`:

v4l2_device_disconnect
======================

.. c:function:: void v4l2_device_disconnect(struct v4l2_device *v4l2_dev)

    Change V4L2 device state to disconnected.

    :param struct v4l2_device \*v4l2_dev:
        pointer to struct v4l2_device

.. _`v4l2_device_disconnect.description`:

Description
-----------

Should be called when the USB parent disconnects.
Since the parent disappears, this ensures that \ ``v4l2_dev``\  doesn't have
an invalid parent pointer.

.. note:: This function sets \ ``v4l2_dev``\ ->dev to NULL.

.. _`v4l2_device_unregister`:

v4l2_device_unregister
======================

.. c:function:: void v4l2_device_unregister(struct v4l2_device *v4l2_dev)

    Unregister all sub-devices and any other resources related to \ ``v4l2_dev``\ .

    :param struct v4l2_device \*v4l2_dev:
        pointer to struct v4l2_device

.. _`v4l2_device_register_subdev`:

v4l2_device_register_subdev
===========================

.. c:function:: int v4l2_device_register_subdev(struct v4l2_device *v4l2_dev, struct v4l2_subdev *sd)

    Registers a subdev with a v4l2 device.

    :param struct v4l2_device \*v4l2_dev:
        pointer to struct \ :c:type:`struct v4l2_device <v4l2_device>`\ 

    :param struct v4l2_subdev \*sd:
        pointer to struct \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

.. _`v4l2_device_register_subdev.description`:

Description
-----------

While registered, the subdev module is marked as in-use.

An error is returned if the module is no longer loaded on any attempts
to register it.

.. _`v4l2_device_unregister_subdev`:

v4l2_device_unregister_subdev
=============================

.. c:function:: void v4l2_device_unregister_subdev(struct v4l2_subdev *sd)

    Unregisters a subdev with a v4l2 device.

    :param struct v4l2_subdev \*sd:
        pointer to struct \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

.. _`v4l2_device_unregister_subdev.description`:

Description
-----------

.. note ::

     Can also be called if the subdev wasn't registered. In such
     case, it will do nothing.

.. _`v4l2_device_register_subdev_nodes`:

v4l2_device_register_subdev_nodes
=================================

.. c:function:: int v4l2_device_register_subdev_nodes(struct v4l2_device *v4l2_dev)

    Registers device nodes for all subdevs of the v4l2 device that are marked with the \ ``V4L2_SUBDEV_FL_HAS_DEVNODE``\  flag.

    :param struct v4l2_device \*v4l2_dev:
        pointer to struct v4l2_device

.. _`v4l2_subdev_notify`:

v4l2_subdev_notify
==================

.. c:function:: void v4l2_subdev_notify(struct v4l2_subdev *sd, unsigned int notification, void *arg)

    Sends a notification to v4l2_device.

    :param struct v4l2_subdev \*sd:
        pointer to struct \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

    :param unsigned int notification:
        type of notification. Please notice that the notification
        type is driver-specific.

    :param void \*arg:
        arguments for the notification. Those are specific to each
        notification type.

.. This file was automatic generated / don't edit.
