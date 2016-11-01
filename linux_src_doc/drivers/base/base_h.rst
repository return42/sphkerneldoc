.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/base.h

.. _`subsys_private`:

struct subsys_private
=====================

.. c:type:: struct subsys_private

    structure to hold the private to the driver core portions of the bus_type/class structure.

.. _`subsys_private.definition`:

Definition
----------

.. code-block:: c

    struct subsys_private {
        struct kset subsys;
        struct kset *devices_kset;
        struct list_head interfaces;
        struct mutex mutex;
        struct kset *drivers_kset;
        struct klist klist_devices;
        struct klist klist_drivers;
        struct blocking_notifier_head bus_notifier;
        unsigned int drivers_autoprobe:1;
        struct bus_type *bus;
        struct kset glue_dirs;
        struct class *class;
    }

.. _`subsys_private.members`:

Members
-------

subsys
    *undescribed*

devices_kset
    *undescribed*

interfaces
    *undescribed*

mutex
    *undescribed*

drivers_kset
    *undescribed*

klist_devices
    *undescribed*

klist_drivers
    *undescribed*

bus_notifier
    *undescribed*

drivers_autoprobe
    *undescribed*

bus
    *undescribed*

glue_dirs
    *undescribed*

class
    *undescribed*

.. _`subsys_private.description`:

Description
-----------

@subsys - the struct kset that defines this subsystem
\ ``devices_kset``\  - the subsystem's 'devices' directory
\ ``interfaces``\  - list of subsystem interfaces associated
\ ``mutex``\  - protect the devices, and interfaces lists.

\ ``drivers_kset``\  - the list of drivers associated
\ ``klist_devices``\  - the klist to iterate over the \ ``devices_kset``\ 
\ ``klist_drivers``\  - the klist to iterate over the \ ``drivers_kset``\ 
\ ``bus_notifier``\  - the bus notifier list for anything that cares about things
on this bus.
\ ``bus``\  - pointer back to the struct bus_type that this structure is associated
with.

\ ``glue_dirs``\  - "glue" directory to put in-between the parent device to
avoid namespace conflicts
\ ``class``\  - pointer back to the struct class that this structure is associated
with.

This structure is the one that is the actual kobject allowing struct
bus_type/class to be statically allocated safely.  Nothing outside of the
driver core should ever touch these fields.

.. _`device_private`:

struct device_private
=====================

.. c:type:: struct device_private

    structure to hold the private to the driver core portions of the device structure.

.. _`device_private.definition`:

Definition
----------

.. code-block:: c

    struct device_private {
        struct klist klist_children;
        struct klist_node knode_parent;
        struct klist_node knode_driver;
        struct klist_node knode_bus;
        struct list_head deferred_probe;
        struct device *device;
    }

.. _`device_private.members`:

Members
-------

klist_children
    *undescribed*

knode_parent
    *undescribed*

knode_driver
    *undescribed*

knode_bus
    *undescribed*

deferred_probe
    *undescribed*

device
    *undescribed*

.. _`device_private.description`:

Description
-----------

@klist_children - klist containing all children of this device
\ ``knode_parent``\  - node in sibling list
\ ``knode_driver``\  - node in driver list
\ ``knode_bus``\  - node in bus list
\ ``deferred_probe``\  - entry in deferred_probe_list which is used to retry the
binding of drivers which were unable to get all the resources needed by
the device; typically because it depends on another driver getting
probed first.
\ ``device``\  - pointer back to the struct device that this structure is
associated with.

Nothing outside of the driver core should ever touch these fields.

.. This file was automatic generated / don't edit.

