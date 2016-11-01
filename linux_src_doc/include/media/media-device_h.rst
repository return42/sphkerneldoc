.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/media-device.h

.. _`media_entity_notify`:

struct media_entity_notify
==========================

.. c:type:: struct media_entity_notify

    Media Entity Notify

.. _`media_entity_notify.definition`:

Definition
----------

.. code-block:: c

    struct media_entity_notify {
        struct list_head list;
        void *notify_data;
        void (*notify)(struct media_entity *entity, void *notify_data);
    }

.. _`media_entity_notify.members`:

Members
-------

list
    List head

notify_data
    Input data to invoke the callback

notify
    Callback function pointer

.. _`media_entity_notify.description`:

Description
-----------

Drivers may register a callback to take action when
new entities get registered with the media device.

.. _`media_device_ops`:

struct media_device_ops
=======================

.. c:type:: struct media_device_ops

    Media device operations

.. _`media_device_ops.definition`:

Definition
----------

.. code-block:: c

    struct media_device_ops {
        int (*link_notify)(struct media_link *link, u32 flags,unsigned int notification);
    }

.. _`media_device_ops.members`:

Members
-------

link_notify
    Link state change notification callback. This callback is
    called with the graph_mutex held.

.. _`media_device`:

struct media_device
===================

.. c:type:: struct media_device

    Media device

.. _`media_device.definition`:

Definition
----------

.. code-block:: c

    struct media_device {
        struct device *dev;
        struct media_devnode *devnode;
        char model[32];
        char driver_name[32];
        char serial[40];
        char bus_info[32];
        u32 hw_revision;
        u32 driver_version;
        u64 topology_version;
        u32 id;
        struct ida entity_internal_idx;
        int entity_internal_idx_max;
        struct list_head entities;
        struct list_head interfaces;
        struct list_head pads;
        struct list_head links;
        struct list_head entity_notify;
        struct mutex graph_mutex;
        struct media_entity_graph pm_count_walk;
        void *source_priv;
        int (*enable_source)(struct media_entity *entity,struct media_pipeline *pipe);
        void (*disable_source)(struct media_entity *entity);
        const struct media_device_ops *ops;
    }

.. _`media_device.members`:

Members
-------

dev
    Parent device

devnode
    Media device node

model
    Device model name

driver_name
    Optional device driver name. If not set, calls to
    \ ``MEDIA_IOC_DEVICE_INFO``\  will return ``dev->driver->name``.
    This is needed for USB drivers for example, as otherwise
    they'll all appear as if the driver name was "usb".

serial
    Device serial number (optional)

bus_info
    Unique and stable device location identifier

hw_revision
    Hardware device revision

driver_version
    Device driver version

topology_version
    Monotonic counter for storing the version of the graph
    topology. Should be incremented each time the topology changes.

id
    Unique ID used on the last registered graph object

entity_internal_idx
    Unique internal entity ID used by the graph traversal
    algorithms

entity_internal_idx_max
    Allocated internal entity indices

entities
    List of registered entities

interfaces
    List of registered interfaces

pads
    List of registered pads

links
    List of registered links

entity_notify
    List of registered entity_notify callbacks

graph_mutex
    Protects access to struct media_device data

pm_count_walk
    Graph walk for power state walk. Access serialised using
    graph_mutex.

source_priv
    Driver Private data for enable/disable source handlers

enable_source
    Enable Source Handler function pointer

disable_source
    Disable Source Handler function pointer

ops
    Operation handler callbacks

.. _`media_device.description`:

Description
-----------

This structure represents an abstract high-level media device. It allows easy
access to entities and provides basic media device-level support. The
structure can be allocated directly or embedded in a larger structure.

The parent \ ``dev``\  is a physical device. It must be set before registering the
media device.

\ ``model``\  is a descriptive model name exported through sysfs. It doesn't have to
be unique.

\ ``enable_source``\  is a handler to find source entity for the
sink entity  and activate the link between them if source
entity is free. Drivers should call this handler before
accessing the source.

\ ``disable_source``\  is a handler to find source entity for the
sink entity  and deactivate the link between them. Drivers
should call this handler to release the source.

Use-case: find tuner entity connected to the decoder
entity and check if it is available, and activate the
the link between them from \ ``enable_source``\  and deactivate
from \ ``disable_source``\ .

.. note::

   Bridge driver is expected to implement and set the
   handler when \ :c:type:`struct media_device <media_device>`\  is registered or when
   bridge driver finds the media_device during probe.
   Bridge driver sets source_priv with information
   necessary to run \ ``enable_source``\  and \ ``disable_source``\  handlers.

.. _`media_entity_enum_init`:

media_entity_enum_init
======================

.. c:function:: int media_entity_enum_init(struct media_entity_enum *ent_enum, struct media_device *mdev)

    Initialise an entity enumeration

    :param struct media_entity_enum \*ent_enum:
        Entity enumeration to be initialised

    :param struct media_device \*mdev:
        The related media device

.. _`media_entity_enum_init.return`:

Return
------

zero on success or a negative error code.

.. _`media_device_init`:

media_device_init
=================

.. c:function:: void media_device_init(struct media_device *mdev)

    Initializes a media device element

    :param struct media_device \*mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

.. _`media_device_init.description`:

Description
-----------

This function initializes the media device prior to its registration.
The media device initialization and registration is split in two functions
to avoid race conditions and make the media device available to user-space
before the media graph has been completed.

So drivers need to first initialize the media device, register any entity
within the media device, create pad to pad links and then finally register
the media device by calling \ :c:func:`media_device_register`\  as a final step.

.. _`media_device_cleanup`:

media_device_cleanup
====================

.. c:function:: void media_device_cleanup(struct media_device *mdev)

    Cleanups a media device element

    :param struct media_device \*mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

.. _`media_device_cleanup.description`:

Description
-----------

This function that will destroy the graph_mutex that is
initialized in \ :c:func:`media_device_init`\ .

.. _`__media_device_register`:

__media_device_register
=======================

.. c:function:: int __media_device_register(struct media_device *mdev, struct module *owner)

    Registers a media device element

    :param struct media_device \*mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

    :param struct module \*owner:
        should be filled with \ ``THIS_MODULE``\ 

.. _`__media_device_register.description`:

Description
-----------

Users, should, instead, call the \ :c:func:`media_device_register`\  macro.

The caller is responsible for initializing the \ :c:type:`struct media_device <media_device>`\  structure
before registration. The following fields of \ :c:type:`struct media_device <media_device>`\  must be set:

 - \ :c:type:`media_entity.dev <media_entity>`\  must point to the parent device (usually a \ :c:type:`struct pci_dev <pci_dev>`\ ,
   \ :c:type:`struct usb_interface <usb_interface>`\  or \ :c:type:`struct platform_device <platform_device>`\  instance).

 - \ :c:type:`media_entity.model <media_entity>`\  must be filled with the device model name as a
   NUL-terminated UTF-8 string. The device/model revision must not be
   stored in this field.

.. _`__media_device_register.the-following-fields-are-optional`:

The following fields are optional
---------------------------------


 - \ :c:type:`media_entity.serial <media_entity>`\  is a unique serial number stored as a
   NUL-terminated ASCII string. The field is big enough to store a GUID
   in text form. If the hardware doesn't provide a unique serial number
   this field must be left empty.

 - \ :c:type:`media_entity.bus_info <media_entity>`\  represents the location of the device in the
   system as a NUL-terminated ASCII string. For PCI/PCIe devices
   \ :c:type:`media_entity.bus_info <media_entity>`\  must be set to "PCI:" (or "PCIe:") followed by
   the value of \ :c:func:`pci_name`\ . For USB devices,the \ :c:func:`usb_make_path`\  function
   must be used. This field is used by applications to distinguish between
   otherwise identical devices that don't provide a serial number.

 - \ :c:type:`media_entity.hw_revision <media_entity>`\  is the hardware device revision in a
   driver-specific format. When possible the revision should be formatted
   with the \ :c:func:`KERNEL_VERSION`\  macro.

 - \ :c:type:`media_entity.driver_version <media_entity>`\  is formatted with the \ :c:func:`KERNEL_VERSION`\ 
   macro. The version minor must be incremented when new features are added
   to the userspace API without breaking binary compatibility. The version
   major must be incremented when binary compatibility is broken.

.. note::

   #) Upon successful registration a character device named media[0-9]+ is created. The device major and minor numbers are dynamic. The model name is exported as a sysfs attribute.

   #) Unregistering a media device that hasn't been registered is **NOT** safe.

.. _`__media_device_register.return`:

Return
------

returns zero on success or a negative error code.

.. _`media_device_register`:

media_device_register
=====================

.. c:function::  media_device_register( mdev)

    Registers a media device element

    :param  mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

.. _`media_device_register.description`:

Description
-----------

This macro calls \ :c:func:`__media_device_register`\  passing \ ``THIS_MODULE``\  as
the \ :c:func:`__media_device_register`\  second argument (**owner**).

.. _`media_device_unregister`:

media_device_unregister
=======================

.. c:function:: void media_device_unregister(struct media_device *mdev)

    Unregisters a media device element

    :param struct media_device \*mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

.. _`media_device_unregister.description`:

Description
-----------

It is safe to call this function on an unregistered (but initialised)
media device.

.. _`media_device_register_entity`:

media_device_register_entity
============================

.. c:function:: int media_device_register_entity(struct media_device *mdev, struct media_entity *entity)

    registers a media entity inside a previously registered media device.

    :param struct media_device \*mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

    :param struct media_entity \*entity:
        pointer to struct \ :c:type:`struct media_entity <media_entity>`\  to be registered

.. _`media_device_register_entity.description`:

Description
-----------

Entities are identified by a unique positive integer ID. The media
controller framework will such ID automatically. IDs are not guaranteed
to be contiguous, and the ID number can change on newer Kernel versions.
So, neither the driver nor userspace should hardcode ID numbers to refer
to the entities, but, instead, use the framework to find the ID, when
needed.

The media_entity name, type and flags fields should be initialized before
calling \ :c:func:`media_device_register_entity`\ . Entities embedded in higher-level
standard structures can have some of those fields set by the higher-level
framework.

If the device has pads, \ :c:func:`media_entity_pads_init`\  should be called before
this function. Otherwise, the \ :c:type:`media_entity.pad <media_entity>`\  and \ :c:type:`media_entity.num_pads <media_entity>`\ 
should be zeroed before calling this function.

.. _`media_device_register_entity.entities-have-flags-that-describe-the-entity-capabilities-and-state`:

Entities have flags that describe the entity capabilities and state
-------------------------------------------------------------------


\ ``MEDIA_ENT_FL_DEFAULT``\ 
   indicates the default entity for a given type.
   This can be used to report the default audio and video devices or the
   default camera sensor.

.. note::

   Drivers should set the entity function before calling this function.
   Please notice that the values \ ``MEDIA_ENT_F_V4L2_SUBDEV_UNKNOWN``\  and
   \ ``MEDIA_ENT_F_UNKNOWN``\  should not be used by the drivers.

.. _`media_device_unregister_entity`:

media_device_unregister_entity
==============================

.. c:function:: void media_device_unregister_entity(struct media_entity *entity)

    unregisters a media entity.

    :param struct media_entity \*entity:
        pointer to struct \ :c:type:`struct media_entity <media_entity>`\  to be unregistered

.. _`media_device_unregister_entity.description`:

Description
-----------

All links associated with the entity and all PADs are automatically
unregistered from the media_device when this function is called.

Unregistering an entity will not change the IDs of the other entities and
the previoully used ID will never be reused for a newly registered entities.

When a media device is unregistered, all its entities are unregistered
automatically. No manual entities unregistration is then required.

.. note::

   The media_entity instance itself must be freed explicitly by
   the driver if required.

.. _`media_device_register_entity_notify`:

media_device_register_entity_notify
===================================

.. c:function:: int media_device_register_entity_notify(struct media_device *mdev, struct media_entity_notify *nptr)

    Registers a media entity_notify callback

    :param struct media_device \*mdev:
        The media device

    :param struct media_entity_notify \*nptr:
        The media_entity_notify

.. _`media_device_register_entity_notify.description`:

Description
-----------

.. note::

   When a new entity is registered, all the registered
   media_entity_notify callbacks are invoked.

.. _`media_device_unregister_entity_notify`:

media_device_unregister_entity_notify
=====================================

.. c:function:: void media_device_unregister_entity_notify(struct media_device *mdev, struct media_entity_notify *nptr)

    Unregister a media entity notify callback

    :param struct media_device \*mdev:
        The media device

    :param struct media_entity_notify \*nptr:
        The media_entity_notify

.. _`media_device_get_devres`:

media_device_get_devres
=======================

.. c:function:: struct media_device *media_device_get_devres(struct device *dev)

    get media device as device resource creates if one doesn't exist

    :param struct device \*dev:
        pointer to struct \ :c:type:`struct device <device>`\ .

.. _`media_device_get_devres.description`:

Description
-----------

Sometimes, the media controller \ :c:type:`struct media_device <media_device>`\  needs to be shared by more
than one driver. This function adds support for that, by dynamically
allocating the \ :c:type:`struct media_device <media_device>`\  and allowing it to be obtained from the
struct \ :c:type:`struct device <device>`\  associated with the common device where all sub-device
components belong. So, for example, on an USB device with multiple
interfaces, each interface may be handled by a separate per-interface
drivers. While each interface have its own \ :c:type:`struct device <device>`\ , they all share a
common \ :c:type:`struct device <device>`\  associated with the hole USB device.

.. _`media_device_find_devres`:

media_device_find_devres
========================

.. c:function:: struct media_device *media_device_find_devres(struct device *dev)

    find media device as device resource

    :param struct device \*dev:
        pointer to struct \ :c:type:`struct device <device>`\ .

.. _`media_device_pci_init`:

media_device_pci_init
=====================

.. c:function:: void media_device_pci_init(struct media_device *mdev, struct pci_dev *pci_dev, const char *name)

    create and initialize a struct \ :c:type:`struct media_device <media_device>`\  from a PCI device.

    :param struct media_device \*mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

    :param struct pci_dev \*pci_dev:
        pointer to struct pci_dev

    :param const char \*name:
        media device name. If \ ``NULL``\ , the routine will use the default
        name for the pci device, given by \ :c:func:`pci_name`\  macro.

.. _`__media_device_usb_init`:

__media_device_usb_init
=======================

.. c:function:: void __media_device_usb_init(struct media_device *mdev, struct usb_device *udev, const char *board_name, const char *driver_name)

    create and initialize a struct \ :c:type:`struct media_device <media_device>`\  from a PCI device.

    :param struct media_device \*mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

    :param struct usb_device \*udev:
        pointer to struct usb_device

    :param const char \*board_name:
        media device name. If \ ``NULL``\ , the routine will use the usb
        product name, if available.

    :param const char \*driver_name:
        name of the driver. if \ ``NULL``\ , the routine will use the name
        given by ``udev->dev->driver->name``, with is usually the wrong
        thing to do.

.. _`__media_device_usb_init.description`:

Description
-----------

.. note::

   It is better to call \ :c:func:`media_device_usb_init`\  instead, as
   such macro fills driver_name with \ ``KBUILD_MODNAME``\ .

.. _`media_device_usb_init`:

media_device_usb_init
=====================

.. c:function::  media_device_usb_init( mdev,  udev,  name)

    create and initialize a struct \ :c:type:`struct media_device <media_device>`\  from a PCI device.

    :param  mdev:
        pointer to struct \ :c:type:`struct media_device <media_device>`\ 

    :param  udev:
        pointer to struct usb_device

    :param  name:
        media device name. If \ ``NULL``\ , the routine will use the usb
        product name, if available.

.. _`media_device_usb_init.description`:

Description
-----------

This macro calls \ :c:func:`media_device_usb_init`\  passing the
\ :c:func:`media_device_usb_init`\  **driver_name** parameter filled with
\ ``KBUILD_MODNAME``\ .

.. This file was automatic generated / don't edit.

