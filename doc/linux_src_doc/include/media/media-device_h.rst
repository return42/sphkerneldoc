.. -*- coding: utf-8; mode: rst -*-

==============
media-device.h
==============


.. _`media-controller`:

Media Controller
================

The media controller userspace API is documented in DocBook format in
Documentation/DocBook/media/v4l/media-controller.xml. This document focus
on the kernel-side implementation of the media framework.

* Abstract media device model:

Discovering a device internal topology, and configuring it at runtime, is one
of the goals of the media framework. To achieve this, hardware devices are
modelled as an oriented graph of building blocks called entities connected
through pads.

An entity is a basic media hardware building block. It can correspond to
a large variety of logical blocks such as physical hardware devices
(CMOS sensor for instance), logical hardware devices (a building block
in a System-on-Chip image processing pipeline), DMA channels or physical
connectors.

A pad is a connection endpoint through which an entity can interact with
other entities. Data (not restricted to video) produced by an entity
flows from the entity's output to one or more entity inputs. Pads should
not be confused with physical pins at chip boundaries.

A link is a point-to-point oriented connection between two pads, either
on the same entity or on different entities. Data flows from a source
pad to a sink pad.


* Media device:

A media device is represented by a struct :c:type:`struct media_device <media_device>` instance, defined in
include/media/media-device.h. Allocation of the structure is handled by the
media device driver, usually by embedding the :c:type:`struct media_device <media_device>` instance in a
larger driver-specific structure.

Drivers register media device instances by calling
:c:func:`__media_device_register` via the macro :c:func:`media_device_register`

and unregistered by calling
:c:func:`media_device_unregister`.

* Entities, pads and links:

- Entities

Entities are represented by a struct :c:type:`struct media_entity <media_entity>` instance, defined in
include/media/media-entity.h. The structure is usually embedded into a
higher-level structure, such as a v4l2_subdev or video_device instance,
although drivers can allocate entities directly.

Drivers initialize entity pads by calling
:c:func:`media_entity_pads_init`.

Drivers register entities with a media device by calling
:c:func:`media_device_register_entity`

and unregistred by calling
:c:func:`media_device_unregister_entity`.

- Interfaces

Interfaces are represented by a struct :c:type:`struct media_interface <media_interface>` instance, defined in
include/media/media-entity.h. Currently, only one type of interface is
defined: a device node. Such interfaces are represented by a struct
:c:type:`struct media_intf_devnode <media_intf_devnode>`.

Drivers initialize and create device node interfaces by calling
:c:func:`media_devnode_create`

and remove them by calling::

        :c:func:`media_devnode_remove`.

- Pads

Pads are represented by a struct :c:type:`struct media_pad <media_pad>` instance, defined in
include/media/media-entity.h. Each entity stores its pads in a pads array
managed by the entity driver. Drivers usually embed the array in a
driver-specific structure.

Pads are identified by their entity and their 0-based index in the pads
array.
Both information are stored in the :c:type:`struct media_pad <media_pad>` structure, making the
:c:type:`struct media_pad <media_pad>` pointer the canonical way to store and pass link references.

Pads have flags that describe the pad capabilities and state.::

        ``MEDIA_PAD_FL_SINK`` indicates that the pad supports sinking data.
        ``MEDIA_PAD_FL_SOURCE`` indicates that the pad supports sourcing data.

NOTE: One and only one of ``MEDIA_PAD_FL_SINK`` and ``MEDIA_PAD_FL_SOURCE`` must
be set for each pad.

- Links

Links are represented by a struct :c:type:`struct media_link <media_link>` instance, defined in
include/media/media-entity.h. There are two types of links:

1. pad to pad links:

Associate two entities via their PADs. Each entity has a list that points
to all links originating at or targeting any of its pads.
A given link is thus stored twice, once in the source entity and once in
the target entity.

Drivers create pad to pad links by calling::

        :c:func:`media_create_pad_link` and remove with :c:func:`media_entity_remove_links`.

2. interface to entity links:

Associate one interface to a Link.

Drivers create interface to entity links by calling::

        :c:func:`media_create_intf_link` and remove with :c:func:`media_remove_intf_links`.

NOTE:

Links can only be created after having both ends already created.

Links have flags that describe the link capabilities and state. The
valid values are described at :c:func:`media_create_pad_link` and
:c:func:`media_create_intf_link`.

Graph traversal:

The media framework provides APIs to iterate over entities in a graph.

To iterate over all entities belonging to a media device, drivers can use
the media_device_for_each_entity macro, defined in
include/media/media-device.h.::

        struct media_entity \*entity;

        media_device_for_each_entity(entity, mdev) {
                // entity will point to each entity in turn
                ...
        }

Drivers might also need to iterate over all entities in a graph that can be
reached only through enabled links starting at a given entity. The media
framework provides a depth-first graph traversal API for that purpose.

Note that graphs with cycles (whether directed or undirected) are \*NOT*
supported by the graph traversal API. To prevent infinite loops, the graph
traversal code limits the maximum depth to MEDIA_ENTITY_ENUM_MAX_DEPTH,
currently defined as 16.

Drivers initiate a graph traversal by calling
:c:func:`media_entity_graph_walk_start`

The graph structure, provided by the caller, is initialized to start graph
traversal at the given entity.

Drivers can then retrieve the next entity by calling
:c:func:`media_entity_graph_walk_next`

When the graph traversal is complete the function will return NULL.

Graph traversal can be interrupted at any moment. No cleanup function call
is required and the graph structure can be freed normally.

Helper functions can be used to find a link between two given pads, or a pad
connected to another pad through an enabled link
:c:func:`media_entity_find_link` and :c:func:`media_entity_remote_pad`

Use count and power handling:

Due to the wide differences between drivers regarding power management
needs, the media controller does not implement power management. However,
the :c:type:`struct media_entity <media_entity>` structure includes a use_count field that media drivers
can use to track the number of users of every entity for power management
needs.

The :c:type:`struct media_entity <media_entity>`.\ ``use_count`` field is owned by media drivers and must not be
touched by entity drivers. Access to the field must be protected by the
:c:type:`struct media_device <media_device>`.\ ``graph_mutex`` lock.

Links setup:

Link properties can be modified at runtime by calling
:c:func:`media_entity_setup_link`

Pipelines and media streams:

When starting streaming, drivers must notify all entities in the pipeline to
prevent link states from being modified during streaming by calling
:c:func:`media_entity_pipeline_start`.

The function will mark all entities connected to the given entity through
enabled links, either directly or indirectly, as streaming.

The :c:type:`struct media_pipeline <media_pipeline>` instance pointed to by the pipe argument will be stored
in every entity in the pipeline. Drivers should embed the :c:type:`struct media_pipeline <media_pipeline>`
structure in higher-level pipeline structures and can then access the
pipeline through the :c:type:`struct media_entity <media_entity>` pipe field.

Calls to :c:func:`media_entity_pipeline_start` can be nested. The pipeline pointer
must be identical for all nested calls to the function.

:c:func:`media_entity_pipeline_start` may return an error. In that case, it will
clean up any of the changes it did by itself.

When stopping the stream, drivers must notify the entities with
:c:func:`media_entity_pipeline_stop`.

If multiple calls to :c:func:`media_entity_pipeline_start` have been made the same
number of :c:func:`media_entity_pipeline_stop` calls are required to stop streaming.
The :c:type:`struct media_entity <media_entity>` pipe field is reset to NULL on the last nested stop call.

Link configuration will fail with -\ ``EBUSY`` by default if either end of the
link is a streaming entity. Links that can be modified while streaming must
be marked with the ``MEDIA_LNK_FL_DYNAMIC`` flag.

If other operations need to be disallowed on streaming entities (such as
changing entities configuration parameters) drivers can explicitly check the
media_entity stream_count field to find out if an entity is streaming. This
operation must be done with the media_device graph_mutex held.

Link validation:

Link validation is performed by :c:func:`media_entity_pipeline_start` for any
entity which has sink pads in the pipeline. The
:c:type:`struct media_entity <media_entity>`.@:c:func:`link_validate` callback is used for that purpose. In
@:c:func:`link_validate` callback, entity driver should check that the properties of
the source pad of the connected entity and its own sink pad match. It is up
to the type of the entity (and in the end, the properties of the hardware)
what matching actually means.

Subsystems should facilitate link validation by providing subsystem specific
helper functions to provide easy access for commonly needed information, and
in the end provide a way to use driver-specific callbacks.



.. _`media_entity_notify`:

struct media_entity_notify
==========================

.. c:type:: media_entity_notify

    Media Entity Notify


.. _`media_entity_notify.definition`:

Definition
----------

.. code-block:: c

  struct media_entity_notify {
    struct list_head list;
    void * notify_data;
    void (* notify) (struct media_entity *entity, void *notify_data);
  };


.. _`media_entity_notify.members`:

Members
-------

:``list``:
    List head

:``notify_data``:
    Input data to invoke the callback

:``notify``:
    Callback function pointer




.. _`media_entity_notify.description`:

Description
-----------

Drivers may register a callback to take action when
new entities get registered with the media device.



.. _`media_device`:

struct media_device
===================

.. c:type:: media_device

    Media device


.. _`media_device.definition`:

Definition
----------

.. code-block:: c

  struct media_device {
    struct device * dev;
    struct media_devnode devnode;
    char model[32];
    char driver_name[32];
    char serial[40];
    char bus_info[32];
    u32 hw_revision;
    u32 driver_version;
    u32 topology_version;
    u32 id;
    struct ida entity_internal_idx;
    int entity_internal_idx_max;
    struct list_head entities;
    struct list_head interfaces;
    struct list_head pads;
    struct list_head links;
    struct list_head entity_notify;
    spinlock_t lock;
    struct mutex graph_mutex;
    struct media_entity_graph pm_count_walk;
    void * source_priv;
    int (* enable_source) (struct media_entity *entity,struct media_pipeline *pipe);
    void (* disable_source) (struct media_entity *entity);
    int (* link_notify) (struct media_link *link, u32 flags,unsigned int notification);
  };


.. _`media_device.members`:

Members
-------

:``dev``:
    Parent device

:``devnode``:
    Media device node

:``model[32]``:
    Device model name

:``driver_name[32]``:
    Optional device driver name. If not set, calls to
    ``MEDIA_IOC_DEVICE_INFO`` will return dev->driver->name.
    This is needed for USB drivers for example, as otherwise
    they'll all appear as if the driver name was "usb".

:``serial[40]``:
    Device serial number (optional)

:``bus_info[32]``:
    Unique and stable device location identifier

:``hw_revision``:
    Hardware device revision

:``driver_version``:
    Device driver version

:``topology_version``:
    Monotonic counter for storing the version of the graph
    topology. Should be incremented each time the topology changes.

:``id``:
    Unique ID used on the last registered graph object

:``entity_internal_idx``:
    Unique internal entity ID used by the graph traversal
    algorithms

:``entity_internal_idx_max``:
    Allocated internal entity indices

:``entities``:
    List of registered entities

:``interfaces``:
    List of registered interfaces

:``pads``:
    List of registered pads

:``links``:
    List of registered links

:``entity_notify``:
    List of registered entity_notify callbacks

:``lock``:
    Entities list lock

:``graph_mutex``:
    Entities graph operation lock

:``pm_count_walk``:
    Graph walk for power state walk. Access serialised using
    graph_mutex.

:``source_priv``:
    Driver Private data for enable/disable source handlers

:``enable_source``:
    Enable Source Handler function pointer

:``disable_source``:
    Disable Source Handler function pointer

:``link_notify``:
    Link state change notification callback




.. _`media_device.description`:

Description
-----------

This structure represents an abstract high-level media device. It allows easy
access to entities and provides basic media device-level support. The
structure can be allocated directly or embedded in a larger structure.

The parent ``dev`` is a physical device. It must be set before registering the
media device.

``model`` is a descriptive model name exported through sysfs. It doesn't have to
be unique.

``enable_source`` is a handler to find source entity for the
sink entity  and activate the link between them if source
entity is free. Drivers should call this handler before
accessing the source.

``disable_source`` is a handler to find source entity for the
sink entity  and deactivate the link between them. Drivers
should call this handler to release the source.



.. _`media_device.note`:

Note
----

Bridge driver is expected to implement and set the
handler when media_device is registered or when
bridge driver finds the media_device during probe.
Bridge driver sets source_priv with information
necessary to run enable/disable source handlers.

Use-case: find tuner entity connected to the decoder
entity and check if it is available, and activate the
the link between them from enable_source and deactivate
from disable_source.



.. _`media_entity_enum_init`:

media_entity_enum_init
======================

.. c:function:: int media_entity_enum_init (struct media_entity_enum *ent_enum, struct media_device *mdev)

    Initialise an entity enumeration

    :param struct media_entity_enum \*ent_enum:
        Entity enumeration to be initialised

    :param struct media_device \*mdev:
        The related media device



.. _`media_entity_enum_init.description`:

Description
-----------

Returns zero on success or a negative error code.



.. _`media_device_init`:

media_device_init
=================

.. c:function:: void media_device_init (struct media_device *mdev)

    Initializes a media device element

    :param struct media_device \*mdev:
        pointer to struct :c:type:`struct media_device <media_device>`



.. _`media_device_init.description`:

Description
-----------

This function initializes the media device prior to its registration.
The media device initialization and registration is split in two functions
to avoid race conditions and make the media device available to user-space
before the media graph has been completed.

So drivers need to first initialize the media device, register any entity
within the media device, create pad to pad links and then finally register
the media device by calling :c:func:`media_device_register` as a final step.



.. _`media_device_cleanup`:

media_device_cleanup
====================

.. c:function:: void media_device_cleanup (struct media_device *mdev)

    Cleanups a media device element

    :param struct media_device \*mdev:
        pointer to struct :c:type:`struct media_device <media_device>`



.. _`media_device_cleanup.description`:

Description
-----------

This function that will destroy the graph_mutex that is
initialized in :c:func:`media_device_init`.



.. _`__media_device_register`:

__media_device_register
=======================

.. c:function:: int __media_device_register (struct media_device *mdev, struct module *owner)

    Registers a media device element

    :param struct media_device \*mdev:
        pointer to struct :c:type:`struct media_device <media_device>`

    :param struct module \*owner:
        should be filled with ``THIS_MODULE``



.. _`__media_device_register.description`:

Description
-----------

Users, should, instead, call the :c:func:`media_device_register` macro.

The caller is responsible for initializing the media_device structure before
registration. The following fields must be set:

 - dev must point to the parent device (usually a :c:type:`struct pci_dev <pci_dev>`, :c:type:`struct usb_interface <usb_interface>` or
   :c:type:`struct platform_device <platform_device>` instance).

 - model must be filled with the device model name as a NUL-terminated UTF-8
   string. The device/model revision must not be stored in this field.



.. _`__media_device_register.the-following-fields-are-optional`:

The following fields are optional
---------------------------------


- serial is a unique serial number stored as a NUL-terminated ASCII string.

  The field is big enough to store a GUID in text form. If the hardware
  doesn't provide a unique serial number this field must be left empty.

- bus_info represents the location of the device in the system as a

  NUL-terminated ASCII string. For PCI/PCIe devices bus_info must be set to
  "PCI:" (or "PCIe:") followed by the value of :c:func:`pci_name`. For USB devices,
  the :c:func:`usb_make_path` function must be used. This field is used by
  applications to distinguish between otherwise identical devices that don't
  provide a serial number.

- hw_revision is the hardware device revision in a driver-specific format.

  When possible the revision should be formatted with the KERNEL_VERSION
  macro.

- driver_version is formatted with the KERNEL_VERSION macro. The version

  minor must be incremented when new features are added to the userspace API
  without breaking binary compatibility. The version major must be
  incremented when binary compatibility is broken.



.. _`__media_device_register.notes`:

Notes
-----


Upon successful registration a character device named media[0-9]+ is created.
The device major and minor numbers are dynamic. The model name is exported as
a sysfs attribute.

Unregistering a media device that hasn't been registered is \*NOT\* safe.



.. _`__media_device_register.return`:

Return
------

returns zero on success or a negative error code.



.. _`media_device_unregister`:

media_device_unregister
=======================

.. c:function:: void media_device_unregister (struct media_device *mdev)

    Unegisters a media device element

    :param struct media_device \*mdev:
        pointer to struct :c:type:`struct media_device <media_device>`



.. _`media_device_unregister.description`:

Description
-----------


It is safe to call this function on an unregistered (but initialised)
media device.



.. _`media_device_register_entity`:

media_device_register_entity
============================

.. c:function:: int media_device_register_entity (struct media_device *mdev, struct media_entity *entity)

    registers a media entity inside a previously registered media device.

    :param struct media_device \*mdev:
        pointer to struct :c:type:`struct media_device <media_device>`

    :param struct media_entity \*entity:
        pointer to struct :c:type:`struct media_entity <media_entity>` to be registered



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
calling :c:func:`media_device_register_entity`. Entities embedded in higher-level
standard structures can have some of those fields set by the higher-level
framework.

If the device has pads, :c:func:`media_entity_pads_init` should be called before
this function. Otherwise, the :c:type:`struct media_entity <media_entity>`.\ ``pad`` and :c:type:`struct media_entity <media_entity>`.\ ``num_pads``
should be zeroed before calling this function.



.. _`media_device_register_entity.entities-have-flags-that-describe-the-entity-capabilities-and-state`:

Entities have flags that describe the entity capabilities and state
-------------------------------------------------------------------


``MEDIA_ENT_FL_DEFAULT`` indicates the default entity for a given type.
This can be used to report the default audio and video devices or the
default camera sensor.



.. _`media_device_register_entity.note`:

NOTE
----

Drivers should set the entity function before calling this function.
Please notice that the values ``MEDIA_ENT_F_V4L2_SUBDEV_UNKNOWN`` and
``MEDIA_ENT_F_UNKNOWN`` should not be used by the drivers.



.. _`media_device_register_entity_notify`:

media_device_register_entity_notify
===================================

.. c:function:: int media_device_register_entity_notify (struct media_device *mdev, struct media_entity_notify *nptr)

    Registers a media entity_notify callback

    :param struct media_device \*mdev:
        The media device

    :param struct media_entity_notify \*nptr:
        The media_entity_notify



.. _`media_device_register_entity_notify.note`:

Note
----

When a new entity is registered, all the registered
media_entity_notify callbacks are invoked.



.. _`media_device_unregister_entity_notify`:

media_device_unregister_entity_notify
=====================================

.. c:function:: void media_device_unregister_entity_notify (struct media_device *mdev, struct media_entity_notify *nptr)

    Unregister a media entity notify callback

    :param struct media_device \*mdev:
        The media device

    :param struct media_entity_notify \*nptr:
        The media_entity_notify



.. _`media_device_get_devres`:

media_device_get_devres
=======================

.. c:function:: struct media_device *media_device_get_devres (struct device *dev)

    get media device as device resource creates if one doesn't exist

    :param struct device \*dev:
        pointer to struct :c:type:`struct device <device>`.



.. _`media_device_get_devres.description`:

Description
-----------

Sometimes, the media controller :c:type:`struct media_device <media_device>` needs to be shared by more
than one driver. This function adds support for that, by dynamically
allocating the :c:type:`struct media_device <media_device>` and allowing it to be obtained from the
struct :c:type:`struct device <device>` associated with the common device where all sub-device
components belong. So, for example, on an USB device with multiple
interfaces, each interface may be handled by a separate per-interface
drivers. While each interface have its own :c:type:`struct device <device>`, they all share a
common :c:type:`struct device <device>` associated with the hole USB device.



.. _`media_device_find_devres`:

media_device_find_devres
========================

.. c:function:: struct media_device *media_device_find_devres (struct device *dev)

    find media device as device resource

    :param struct device \*dev:
        pointer to struct :c:type:`struct device <device>`.



.. _`media_device_pci_init`:

media_device_pci_init
=====================

.. c:function:: void media_device_pci_init (struct media_device *mdev, struct pci_dev *pci_dev, const char *name)

    create and initialize a struct &media_device from a PCI device.

    :param struct media_device \*mdev:
        pointer to struct :c:type:`struct media_device <media_device>`

    :param struct pci_dev \*pci_dev:
        pointer to struct pci_dev

    :param const char \*name:
        media device name. If ``NULL``\ , the routine will use the default
        name for the pci device, given by :c:func:`pci_name` macro.



.. _`__media_device_usb_init`:

__media_device_usb_init
=======================

.. c:function:: void __media_device_usb_init (struct media_device *mdev, struct usb_device *udev, const char *board_name, const char *driver_name)

    create and initialize a struct &media_device from a PCI device.

    :param struct media_device \*mdev:
        pointer to struct :c:type:`struct media_device <media_device>`

    :param struct usb_device \*udev:
        pointer to struct usb_device

    :param const char \*board_name:
        media device name. If ``NULL``\ , the routine will use the usb
        product name, if available.

    :param const char \*driver_name:
        name of the driver. if ``NULL``\ , the routine will use the name
        given by udev->dev->driver->name, with is usually the wrong
        thing to do.



.. _`__media_device_usb_init.note`:

NOTE
----

It is better to call :c:func:`media_device_usb_init` instead, as
such macro fills driver_name with ``KBUILD_MODNAME``\ .

