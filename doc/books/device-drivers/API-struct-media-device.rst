
.. _API-struct-media-device:

===================
struct media_device
===================

*man struct media_device(9)*

*4.6.0-rc1*

Media device


Synopsis
========

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


Members
=======

dev
    Parent device

devnode
    Media device node

model[32]
    Device model name

driver_name[32]
    Optional device driver name. If not set, calls to ``MEDIA_IOC_DEVICE_INFO`` will return dev->driver->name. This is needed for USB drivers for example, as otherwise they'll all
    appear as if the driver name was “usb”.

serial[40]
    Device serial number (optional)

bus_info[32]
    Unique and stable device location identifier

hw_revision
    Hardware device revision

driver_version
    Device driver version

topology_version
    Monotonic counter for storing the version of the graph topology. Should be incremented each time the topology changes.

id
    Unique ID used on the last registered graph object

entity_internal_idx
    Unique internal entity ID used by the graph traversal algorithms

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

lock
    Entities list lock

graph_mutex
    Entities graph operation lock

pm_count_walk
    Graph walk for power state walk. Access serialised using graph_mutex.

source_priv
    Driver Private data for enable/disable source handlers

enable_source
    Enable Source Handler function pointer

disable_source
    Disable Source Handler function pointer

link_notify
    Link state change notification callback


Description
===========

This structure represents an abstract high-level media device. It allows easy access to entities and provides basic media device-level support. The structure can be allocated
directly or embedded in a larger structure.

The parent ``dev`` is a physical device. It must be set before registering the media device.

``model`` is a descriptive model name exported through sysfs. It doesn't have to be unique.

``enable_source`` is a handler to find source entity for the sink entity and activate the link between them if source entity is free. Drivers should call this handler before
accessing the source.

``disable_source`` is a handler to find source entity for the sink entity and deactivate the link between them. Drivers should call this handler to release the source.


Note
====

Bridge driver is expected to implement and set the handler when media_device is registered or when bridge driver finds the media_device during probe. Bridge driver sets
source_priv with information necessary to run enable/disable source handlers.

Use-case: find tuner entity connected to the decoder entity and check if it is available, and activate the the link between them from enable_source and deactivate from
disable_source.
