.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/core.c

.. _`dev_driver_string`:

dev_driver_string
=================

.. c:function:: const char *dev_driver_string(const struct device *dev)

    Return a device's driver name, if at all possible

    :param const struct device \*dev:
        struct device to get the name of

.. _`dev_driver_string.description`:

Description
-----------

Will return the device's driver's name if it is bound to a device.  If
the device is not bound to a driver, it will return the name of the bus
it is attached to.  If it is not attached to a bus either, an empty
string will be returned.

.. _`device_release`:

device_release
==============

.. c:function:: void device_release(struct kobject *kobj)

    free device structure.

    :param struct kobject \*kobj:
        device's kobject.

.. _`device_release.description`:

Description
-----------

This is called once the reference count for the object
reaches 0. We forward the call to the device's release
method, which should handle actually freeing the structure.

.. _`devices_kset_move_before`:

devices_kset_move_before
========================

.. c:function:: void devices_kset_move_before(struct device *deva, struct device *devb)

    Move device in the devices_kset's list.

    :param struct device \*deva:
        Device to move.

    :param struct device \*devb:
        Device \ ``deva``\  should come before.

.. _`devices_kset_move_after`:

devices_kset_move_after
=======================

.. c:function:: void devices_kset_move_after(struct device *deva, struct device *devb)

    Move device in the devices_kset's list.

    :param struct device \*deva:
        Device to move

    :param struct device \*devb:
        Device \ ``deva``\  should come after.

.. _`devices_kset_move_last`:

devices_kset_move_last
======================

.. c:function:: void devices_kset_move_last(struct device *dev)

    move the device to the end of devices_kset's list.

    :param struct device \*dev:
        device to move

.. _`device_create_file`:

device_create_file
==================

.. c:function:: int device_create_file(struct device *dev, const struct device_attribute *attr)

    create sysfs attribute file for device.

    :param struct device \*dev:
        device.

    :param const struct device_attribute \*attr:
        device attribute descriptor.

.. _`device_remove_file`:

device_remove_file
==================

.. c:function:: void device_remove_file(struct device *dev, const struct device_attribute *attr)

    remove sysfs attribute file.

    :param struct device \*dev:
        device.

    :param const struct device_attribute \*attr:
        device attribute descriptor.

.. _`device_remove_file_self`:

device_remove_file_self
=======================

.. c:function:: bool device_remove_file_self(struct device *dev, const struct device_attribute *attr)

    remove sysfs attribute file from its own method.

    :param struct device \*dev:
        device.

    :param const struct device_attribute \*attr:
        device attribute descriptor.

.. _`device_remove_file_self.description`:

Description
-----------

See \ :c:func:`kernfs_remove_self`\  for details.

.. _`device_create_bin_file`:

device_create_bin_file
======================

.. c:function:: int device_create_bin_file(struct device *dev, const struct bin_attribute *attr)

    create sysfs binary attribute file for device.

    :param struct device \*dev:
        device.

    :param const struct bin_attribute \*attr:
        device binary attribute descriptor.

.. _`device_remove_bin_file`:

device_remove_bin_file
======================

.. c:function:: void device_remove_bin_file(struct device *dev, const struct bin_attribute *attr)

    remove sysfs binary attribute file

    :param struct device \*dev:
        device.

    :param const struct bin_attribute \*attr:
        device binary attribute descriptor.

.. _`device_initialize`:

device_initialize
=================

.. c:function:: void device_initialize(struct device *dev)

    init device structure.

    :param struct device \*dev:
        device.

.. _`device_initialize.description`:

Description
-----------

This prepares the device for use by other layers by initializing
its fields.
It is the first half of \ :c:func:`device_register`\ , if called by
that function, though it can also be called separately, so one
may use \ ``dev``\ 's fields. In particular, \ :c:func:`get_device`\ /\ :c:func:`put_device`\ 
may be used for reference counting of \ ``dev``\  after calling this
function.

All fields in \ ``dev``\  must be initialized by the caller to 0, except
for those explicitly set to some other value.  The simplest
approach is to use \ :c:func:`kzalloc`\  to allocate the structure containing
\ ``dev``\ .

.. _`device_initialize.note`:

NOTE
----

Use \ :c:func:`put_device`\  to give up your reference instead of freeing
\ ``dev``\  directly once you have called this function.

.. _`dev_set_name`:

dev_set_name
============

.. c:function:: int dev_set_name(struct device *dev, const char *fmt,  ...)

    set a device name

    :param struct device \*dev:
        device

    :param const char \*fmt:
        format string for the device's name

    :param ... :
        variable arguments

.. _`device_to_dev_kobj`:

device_to_dev_kobj
==================

.. c:function:: struct kobject *device_to_dev_kobj(struct device *dev)

    select a /sys/dev/ directory for the device

    :param struct device \*dev:
        device

.. _`device_to_dev_kobj.description`:

Description
-----------

By default we select char/ for new entries.  Setting class->dev_obj
to NULL prevents an entry from being created.  class->dev_kobj must
be set (or cleared) before any devices are registered to the class
otherwise \ :c:func:`device_create_sys_dev_entry`\  and
\ :c:func:`device_remove_sys_dev_entry`\  will disagree about the presence of
the link.

.. _`device_add`:

device_add
==========

.. c:function:: int device_add(struct device *dev)

    add device to device hierarchy.

    :param struct device \*dev:
        device.

.. _`device_add.description`:

Description
-----------

This is part 2 of \ :c:func:`device_register`\ , though may be called
separately \_iff\_ \ :c:func:`device_initialize`\  has been called separately.

This adds \ ``dev``\  to the kobject hierarchy via \ :c:func:`kobject_add`\ , adds it
to the global and sibling lists for the device, then
adds it to the other relevant subsystems of the driver model.

Do not call this routine or \ :c:func:`device_register`\  more than once for
any device structure.  The driver model core is not designed to work
with devices that get unregistered and then spring back to life.
(Among other things, it's very hard to guarantee that all references
to the previous incarnation of \ ``dev``\  have been dropped.)  Allocate
and register a fresh new struct device instead.

.. _`device_add.note`:

NOTE
----

_Never\_ directly free \ ``dev``\  after calling this function, even
if it returned an error! Always use \ :c:func:`put_device`\  to give up your
reference instead.

.. _`device_register`:

device_register
===============

.. c:function:: int device_register(struct device *dev)

    register a device with the system.

    :param struct device \*dev:
        pointer to the device structure

.. _`device_register.description`:

Description
-----------

This happens in two clean steps - initialize the device
and add it to the system. The two steps can be called
separately, but this is the easiest and most common.
I.e. you should only call the two helpers separately if
have a clearly defined need to use and refcount the device
before it is added to the hierarchy.

For more information, see the kerneldoc for \ :c:func:`device_initialize`\ 
and \ :c:func:`device_add`\ .

.. _`device_register.note`:

NOTE
----

_Never\_ directly free \ ``dev``\  after calling this function, even
if it returned an error! Always use \ :c:func:`put_device`\  to give up the
reference initialized in this function instead.

.. _`get_device`:

get_device
==========

.. c:function:: struct device *get_device(struct device *dev)

    increment reference count for device.

    :param struct device \*dev:
        device.

.. _`get_device.description`:

Description
-----------

This simply forwards the call to \ :c:func:`kobject_get`\ , though
we do take care to provide for the case that we get a NULL
pointer passed in.

.. _`put_device`:

put_device
==========

.. c:function:: void put_device(struct device *dev)

    decrement reference count.

    :param struct device \*dev:
        device in question.

.. _`device_del`:

device_del
==========

.. c:function:: void device_del(struct device *dev)

    delete device from system.

    :param struct device \*dev:
        device.

.. _`device_del.description`:

Description
-----------

This is the first part of the device unregistration
sequence. This removes the device from the lists we control
from here, has it removed from the other driver model
subsystems it was added to in \ :c:func:`device_add`\ , and removes it
from the kobject hierarchy.

.. _`device_del.note`:

NOTE
----

this should be called manually \_iff\_ \ :c:func:`device_add`\  was
also called manually.

.. _`device_unregister`:

device_unregister
=================

.. c:function:: void device_unregister(struct device *dev)

    unregister device from system.

    :param struct device \*dev:
        device going away.

.. _`device_unregister.description`:

Description
-----------

We do this in two parts, like we do \ :c:func:`device_register`\ . First,
we remove it from all the subsystems with \ :c:func:`device_del`\ , then
we decrement the reference count via \ :c:func:`put_device`\ . If that
is the final reference count, the device will be cleaned up
via \ :c:func:`device_release`\  above. Otherwise, the structure will
stick around until the final reference to the device is dropped.

.. _`device_get_devnode`:

device_get_devnode
==================

.. c:function:: const char *device_get_devnode(struct device *dev, umode_t *mode, kuid_t *uid, kgid_t *gid, const char **tmp)

    path of device node file

    :param struct device \*dev:
        device

    :param umode_t \*mode:
        returned file access mode

    :param kuid_t \*uid:
        returned file owner

    :param kgid_t \*gid:
        returned file group

    :param const char \*\*tmp:
        possibly allocated string

.. _`device_get_devnode.description`:

Description
-----------

Return the relative path of a possible device node.
Non-default names may need to allocate a memory to compose
a name. This memory is returned in tmp and needs to be
freed by the caller.

.. _`device_for_each_child`:

device_for_each_child
=====================

.. c:function:: int device_for_each_child(struct device *parent, void *data, int (*fn)(struct device *dev, void *data))

    device child iterator.

    :param struct device \*parent:
        parent struct device.

    :param void \*data:
        data for the callback.

    :param int (\*fn)(struct device \*dev, void \*data):
        function to be called for each device.

.. _`device_for_each_child.description`:

Description
-----------

Iterate over \ ``parent``\ 's child devices, and call \ ``fn``\  for each,
passing it \ ``data``\ .

We check the return of \ ``fn``\  each time. If it returns anything
other than 0, we break out and return that value.

.. _`device_for_each_child_reverse`:

device_for_each_child_reverse
=============================

.. c:function:: int device_for_each_child_reverse(struct device *parent, void *data, int (*fn)(struct device *dev, void *data))

    device child iterator in reversed order.

    :param struct device \*parent:
        parent struct device.

    :param void \*data:
        data for the callback.

    :param int (\*fn)(struct device \*dev, void \*data):
        function to be called for each device.

.. _`device_for_each_child_reverse.description`:

Description
-----------

Iterate over \ ``parent``\ 's child devices, and call \ ``fn``\  for each,
passing it \ ``data``\ .

We check the return of \ ``fn``\  each time. If it returns anything
other than 0, we break out and return that value.

.. _`device_find_child`:

device_find_child
=================

.. c:function:: struct device *device_find_child(struct device *parent, void *data, int (*match)(struct device *dev, void *data))

    device iterator for locating a particular device.

    :param struct device \*parent:
        parent struct device

    :param void \*data:
        Data to pass to match function

    :param int (\*match)(struct device \*dev, void \*data):
        Callback function to check device

.. _`device_find_child.description`:

Description
-----------

This is similar to the \ :c:func:`device_for_each_child`\  function above, but it
returns a reference to a device that is 'found' for later use, as
determined by the \ ``match``\  callback.

The callback should return 0 if the device doesn't match and non-zero
if it does.  If the callback returns non-zero and a reference to the
current device can be obtained, this function will return to the caller
and not iterate over any more devices.

.. _`device_find_child.note`:

NOTE
----

you will need to drop the reference with \ :c:func:`put_device`\  after use.

.. _`device_offline`:

device_offline
==============

.. c:function:: int device_offline(struct device *dev)

    Prepare the device for hot-removal.

    :param struct device \*dev:
        Device to be put offline.

.. _`device_offline.description`:

Description
-----------

Execute the device bus type's .\ :c:func:`offline`\  callback, if present, to prepare
the device for a subsequent hot-removal.  If that succeeds, the device must
not be used until either it is removed or its bus type's .\ :c:func:`online`\  callback
is executed.

Call under device_hotplug_lock.

.. _`device_online`:

device_online
=============

.. c:function:: int device_online(struct device *dev)

    Put the device back online after successful \ :c:func:`device_offline`\ .

    :param struct device \*dev:
        Device to be put back online.

.. _`device_online.description`:

Description
-----------

If \ :c:func:`device_offline`\  has been successfully executed for \ ``dev``\ , but the device
has not been removed subsequently, execute its bus type's .\ :c:func:`online`\  callback
to indicate that the device can be used again.

Call under device_hotplug_lock.

.. _`__root_device_register`:

__root_device_register
======================

.. c:function:: struct device *__root_device_register(const char *name, struct module *owner)

    allocate and register a root device

    :param const char \*name:
        root device name

    :param struct module \*owner:
        owner module of the root device, usually THIS_MODULE

.. _`__root_device_register.description`:

Description
-----------

This function allocates a root device and registers it
using \ :c:func:`device_register`\ . In order to free the returned
device, use \ :c:func:`root_device_unregister`\ .

Root devices are dummy devices which allow other devices
to be grouped under /sys/devices. Use this function to
allocate a root device and then use it as the parent of
any device which should appear under /sys/devices/{name}

The /sys/devices/{name} directory will also contain a
'module' symlink which points to the \ ``owner``\  directory
in sysfs.

Returns \ :c:type:`struct device <device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`__root_device_register.note`:

Note
----

You probably want to use \ :c:func:`root_device_register`\ .

.. _`root_device_unregister`:

root_device_unregister
======================

.. c:function:: void root_device_unregister(struct device *dev)

    unregister and free a root device

    :param struct device \*dev:
        device going away

.. _`root_device_unregister.description`:

Description
-----------

This function unregisters and cleans up a device that was created by
\ :c:func:`root_device_register`\ .

.. _`device_create_vargs`:

device_create_vargs
===================

.. c:function:: struct device *device_create_vargs(struct class *class, struct device *parent, dev_t devt, void *drvdata, const char *fmt, va_list args)

    creates a device and registers it with sysfs

    :param struct class \*class:
        pointer to the struct class that this device should be registered to

    :param struct device \*parent:
        pointer to the parent struct device of this new device, if any

    :param dev_t devt:
        the dev_t for the char device to be added

    :param void \*drvdata:
        the data to be added to the device for callbacks

    :param const char \*fmt:
        string for the device's name

    :param va_list args:
        va_list for the device's name

.. _`device_create_vargs.description`:

Description
-----------

This function can be used by char device classes.  A struct device
will be created in sysfs, registered to the specified class.

A "dev" file will be created, showing the dev_t for the device, if
the dev_t is not 0,0.
If a pointer to a parent struct device is passed in, the newly created
struct device will be a child of that device in sysfs.
The pointer to the struct device will be returned from the call.
Any further sysfs files that might be required can be created using this
pointer.

Returns \ :c:type:`struct device <device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`device_create_vargs.note`:

Note
----

the struct class passed to this function must have previously
been created with a call to \ :c:func:`class_create`\ .

.. _`device_create`:

device_create
=============

.. c:function:: struct device *device_create(struct class *class, struct device *parent, dev_t devt, void *drvdata, const char *fmt,  ...)

    creates a device and registers it with sysfs

    :param struct class \*class:
        pointer to the struct class that this device should be registered to

    :param struct device \*parent:
        pointer to the parent struct device of this new device, if any

    :param dev_t devt:
        the dev_t for the char device to be added

    :param void \*drvdata:
        the data to be added to the device for callbacks

    :param const char \*fmt:
        string for the device's name

    :param ... :
        variable arguments

.. _`device_create.description`:

Description
-----------

This function can be used by char device classes.  A struct device
will be created in sysfs, registered to the specified class.

A "dev" file will be created, showing the dev_t for the device, if
the dev_t is not 0,0.
If a pointer to a parent struct device is passed in, the newly created
struct device will be a child of that device in sysfs.
The pointer to the struct device will be returned from the call.
Any further sysfs files that might be required can be created using this
pointer.

Returns \ :c:type:`struct device <device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`device_create.note`:

Note
----

the struct class passed to this function must have previously
been created with a call to \ :c:func:`class_create`\ .

.. _`device_create_with_groups`:

device_create_with_groups
=========================

.. c:function:: struct device *device_create_with_groups(struct class *class, struct device *parent, dev_t devt, void *drvdata, const struct attribute_group **groups, const char *fmt,  ...)

    creates a device and registers it with sysfs

    :param struct class \*class:
        pointer to the struct class that this device should be registered to

    :param struct device \*parent:
        pointer to the parent struct device of this new device, if any

    :param dev_t devt:
        the dev_t for the char device to be added

    :param void \*drvdata:
        the data to be added to the device for callbacks

    :param const struct attribute_group \*\*groups:
        NULL-terminated list of attribute groups to be created

    :param const char \*fmt:
        string for the device's name

    :param ... :
        variable arguments

.. _`device_create_with_groups.description`:

Description
-----------

This function can be used by char device classes.  A struct device
will be created in sysfs, registered to the specified class.
Additional attributes specified in the groups parameter will also
be created automatically.

A "dev" file will be created, showing the dev_t for the device, if
the dev_t is not 0,0.
If a pointer to a parent struct device is passed in, the newly created
struct device will be a child of that device in sysfs.
The pointer to the struct device will be returned from the call.
Any further sysfs files that might be required can be created using this
pointer.

Returns \ :c:type:`struct device <device>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

.. _`device_create_with_groups.note`:

Note
----

the struct class passed to this function must have previously
been created with a call to \ :c:func:`class_create`\ .

.. _`device_destroy`:

device_destroy
==============

.. c:function:: void device_destroy(struct class *class, dev_t devt)

    removes a device that was created with \ :c:func:`device_create`\ 

    :param struct class \*class:
        pointer to the struct class that this device was registered with

    :param dev_t devt:
        the dev_t of the device that was previously registered

.. _`device_destroy.description`:

Description
-----------

This call unregisters and cleans up a device that was created with a
call to \ :c:func:`device_create`\ .

.. _`device_rename`:

device_rename
=============

.. c:function:: int device_rename(struct device *dev, const char *new_name)

    renames a device

    :param struct device \*dev:
        the pointer to the struct device to be renamed

    :param const char \*new_name:
        the new name of the device

.. _`device_rename.description`:

Description
-----------

It is the responsibility of the caller to provide mutual
exclusion between two different calls of device_rename
on the same device to ensure that new_name is valid and
won't conflict with other devices.

.. _`device_rename.note`:

Note
----

Don't call this function.  Currently, the networking layer calls this
function, but that will change.  The following text from Kay Sievers offers

.. _`device_rename.some-insight`:

some insight
------------


Renaming devices is racy at many levels, symlinks and other stuff are not
replaced atomically, and you get a "move" uevent, but it's not easy to
connect the event to the old and new device. Device nodes are not renamed at
all, there isn't even support for that in the kernel now.

In the meantime, during renaming, your target name might be taken by another
driver, creating conflicts. Or the old name is taken directly after you
renamed it -- then you get events for the same DEVPATH, before you even see
the "move" event. It's just a mess, and nothing new should ever rely on
kernel device renaming. Besides that, it's not even implemented now for
other things than (driver-core wise very simple) network devices.

We are currently about to change network renaming in udev to completely
disallow renaming of devices in the same namespace as the kernel uses,
because we can't solve the problems properly, that arise with swapping names
of multiple interfaces without races. Means, renaming of eth[0-9]\* will only
be allowed to some other name than eth[0-9]\*, for the aforementioned
reasons.

Make up a "real" name in the driver before you register anything, or add
some other attributes for userspace to find the device, or use udev to add
symlinks -- but never rename kernel devices later, it's a complete mess. We
don't even want to get into that and try to implement the missing pieces in
the core. We really have other pieces to fix in the driver core mess. :)

.. _`device_move`:

device_move
===========

.. c:function:: int device_move(struct device *dev, struct device *new_parent, enum dpm_order dpm_order)

    moves a device to a new parent

    :param struct device \*dev:
        the pointer to the struct device to be moved

    :param struct device \*new_parent:
        the new parent of the device (can by NULL)

    :param enum dpm_order dpm_order:
        how to reorder the dpm_list

.. _`device_shutdown`:

device_shutdown
===============

.. c:function:: void device_shutdown( void)

    call ->\ :c:func:`shutdown`\  on each device to shutdown.

    :param  void:
        no arguments

.. _`set_primary_fwnode`:

set_primary_fwnode
==================

.. c:function:: void set_primary_fwnode(struct device *dev, struct fwnode_handle *fwnode)

    Change the primary firmware node of a given device.

    :param struct device \*dev:
        Device to handle.

    :param struct fwnode_handle \*fwnode:
        New primary firmware node of the device.

.. _`set_primary_fwnode.description`:

Description
-----------

Set the device's firmware node pointer to \ ``fwnode``\ , but if a secondary
firmware node of the device is present, preserve it.

.. _`set_secondary_fwnode`:

set_secondary_fwnode
====================

.. c:function:: void set_secondary_fwnode(struct device *dev, struct fwnode_handle *fwnode)

    Change the secondary firmware node of a given device.

    :param struct device \*dev:
        Device to handle.

    :param struct fwnode_handle \*fwnode:
        New secondary firmware node of the device.

.. _`set_secondary_fwnode.description`:

Description
-----------

If a primary firmware node of the device is present, set its secondary
pointer to \ ``fwnode``\ .  Otherwise, set the device's firmware node pointer to
\ ``fwnode``\ .

.. This file was automatic generated / don't edit.

