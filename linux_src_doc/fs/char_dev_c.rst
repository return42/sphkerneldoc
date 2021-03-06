.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/char_dev.c

.. _`register_chrdev_region`:

register_chrdev_region
======================

.. c:function:: int register_chrdev_region(dev_t from, unsigned count, const char *name)

    register a range of device numbers

    :param from:
        the first in the desired range of device numbers; must include
        the major number.
    :type from: dev_t

    :param count:
        the number of consecutive device numbers required
    :type count: unsigned

    :param name:
        the name of the device or driver.
    :type name: const char \*

.. _`register_chrdev_region.description`:

Description
-----------

Return value is zero on success, a negative error code on failure.

.. _`alloc_chrdev_region`:

alloc_chrdev_region
===================

.. c:function:: int alloc_chrdev_region(dev_t *dev, unsigned baseminor, unsigned count, const char *name)

    register a range of char device numbers

    :param dev:
        output parameter for first assigned number
    :type dev: dev_t \*

    :param baseminor:
        first of the requested range of minor numbers
    :type baseminor: unsigned

    :param count:
        the number of minor numbers required
    :type count: unsigned

    :param name:
        the name of the associated device or driver
    :type name: const char \*

.. _`alloc_chrdev_region.description`:

Description
-----------

Allocates a range of char device numbers.  The major number will be
chosen dynamically, and returned (along with the first minor number)
in \ ``dev``\ .  Returns zero or a negative error code.

.. _`__register_chrdev`:

__register_chrdev
=================

.. c:function:: int __register_chrdev(unsigned int major, unsigned int baseminor, unsigned int count, const char *name, const struct file_operations *fops)

    create and register a cdev occupying a range of minors

    :param major:
        major device number or 0 for dynamic allocation
    :type major: unsigned int

    :param baseminor:
        first of the requested range of minor numbers
    :type baseminor: unsigned int

    :param count:
        the number of minor numbers required
    :type count: unsigned int

    :param name:
        name of this range of devices
    :type name: const char \*

    :param fops:
        file operations associated with this devices
    :type fops: const struct file_operations \*

.. _`__register_chrdev.description`:

Description
-----------

If \ ``major``\  == 0 this functions will dynamically allocate a major and return
its number.

If \ ``major``\  > 0 this function will attempt to reserve a device with the given
major number and will return zero on success.

Returns a -ve errno on failure.

The name of this device has nothing to do with the name of the device in
/dev. It only helps to keep track of the different owners of devices. If
your module name has only one type of devices it's ok to use e.g. the name
of the module here.

.. _`unregister_chrdev_region`:

unregister_chrdev_region
========================

.. c:function:: void unregister_chrdev_region(dev_t from, unsigned count)

    unregister a range of device numbers

    :param from:
        the first in the range of numbers to unregister
    :type from: dev_t

    :param count:
        the number of device numbers to unregister
    :type count: unsigned

.. _`unregister_chrdev_region.description`:

Description
-----------

This function will unregister a range of \ ``count``\  device numbers,
starting with \ ``from``\ .  The caller should normally be the one who
allocated those numbers in the first place...

.. _`__unregister_chrdev`:

__unregister_chrdev
===================

.. c:function:: void __unregister_chrdev(unsigned int major, unsigned int baseminor, unsigned int count, const char *name)

    unregister and destroy a cdev

    :param major:
        major device number
    :type major: unsigned int

    :param baseminor:
        first of the range of minor numbers
    :type baseminor: unsigned int

    :param count:
        the number of minor numbers this cdev is occupying
    :type count: unsigned int

    :param name:
        name of this range of devices
    :type name: const char \*

.. _`__unregister_chrdev.description`:

Description
-----------

Unregister and destroy the cdev occupying the region described by
\ ``major``\ , \ ``baseminor``\  and \ ``count``\ .  This function undoes what
\ :c:func:`__register_chrdev`\  did.

.. _`cdev_add`:

cdev_add
========

.. c:function:: int cdev_add(struct cdev *p, dev_t dev, unsigned count)

    add a char device to the system

    :param p:
        the cdev structure for the device
    :type p: struct cdev \*

    :param dev:
        the first device number for which this device is responsible
    :type dev: dev_t

    :param count:
        the number of consecutive minor numbers corresponding to this
        device
    :type count: unsigned

.. _`cdev_add.description`:

Description
-----------

\ :c:func:`cdev_add`\  adds the device represented by \ ``p``\  to the system, making it
live immediately.  A negative error code is returned on failure.

.. _`cdev_set_parent`:

cdev_set_parent
===============

.. c:function:: void cdev_set_parent(struct cdev *p, struct kobject *kobj)

    set the parent kobject for a char device

    :param p:
        the cdev structure
    :type p: struct cdev \*

    :param kobj:
        the kobject to take a reference to
    :type kobj: struct kobject \*

.. _`cdev_set_parent.description`:

Description
-----------

\ :c:func:`cdev_set_parent`\  sets a parent kobject which will be referenced
appropriately so the parent is not freed before the cdev. This
should be called before cdev_add.

.. _`cdev_device_add`:

cdev_device_add
===============

.. c:function:: int cdev_device_add(struct cdev *cdev, struct device *dev)

    add a char device and it's corresponding struct device, linkink

    :param cdev:
        the cdev structure
    :type cdev: struct cdev \*

    :param dev:
        the device structure
    :type dev: struct device \*

.. _`cdev_device_add.description`:

Description
-----------

\ :c:func:`cdev_device_add`\  adds the char device represented by \ ``cdev``\  to the system,
just as cdev_add does. It then adds \ ``dev``\  to the system using device_add
The dev_t for the char device will be taken from the struct device which
needs to be initialized first. This helper function correctly takes a
reference to the parent device so the parent will not get released until
all references to the cdev are released.

This helper uses dev->devt for the device number. If it is not set
it will not add the cdev and it will be equivalent to device_add.

This function should be used whenever the struct cdev and the
struct device are members of the same structure whose lifetime is
managed by the struct device.

.. _`cdev_device_add.note`:

NOTE
----

Callers must assume that userspace was able to open the cdev and
can call cdev fops callbacks at any time, even if this function fails.

.. _`cdev_device_del`:

cdev_device_del
===============

.. c:function:: void cdev_device_del(struct cdev *cdev, struct device *dev)

    inverse of cdev_device_add

    :param cdev:
        the cdev structure
    :type cdev: struct cdev \*

    :param dev:
        the device structure
    :type dev: struct device \*

.. _`cdev_device_del.description`:

Description
-----------

\ :c:func:`cdev_device_del`\  is a helper function to call cdev_del and device_del.
It should be used whenever cdev_device_add is used.

If dev->devt is not set it will not remove the cdev and will be equivalent
to device_del.

.. _`cdev_device_del.note`:

NOTE
----

This guarantees that associated sysfs callbacks are not running
or runnable, however any cdevs already open will remain and their fops
will still be callable even after this function returns.

.. _`cdev_del`:

cdev_del
========

.. c:function:: void cdev_del(struct cdev *p)

    remove a cdev from the system

    :param p:
        the cdev structure to be removed
    :type p: struct cdev \*

.. _`cdev_del.description`:

Description
-----------

\ :c:func:`cdev_del`\  removes \ ``p``\  from the system, possibly freeing the structure
itself.

.. _`cdev_del.note`:

NOTE
----

This guarantees that cdev device will no longer be able to be
opened, however any cdevs already open will remain and their fops will
still be callable even after cdev_del returns.

.. _`cdev_alloc`:

cdev_alloc
==========

.. c:function:: struct cdev *cdev_alloc( void)

    allocate a cdev structure

    :param void:
        no arguments
    :type void: 

.. _`cdev_alloc.description`:

Description
-----------

Allocates and returns a cdev structure, or NULL on failure.

.. _`cdev_init`:

cdev_init
=========

.. c:function:: void cdev_init(struct cdev *cdev, const struct file_operations *fops)

    initialize a cdev structure

    :param cdev:
        the structure to initialize
    :type cdev: struct cdev \*

    :param fops:
        the file_operations for this device
    :type fops: const struct file_operations \*

.. _`cdev_init.description`:

Description
-----------

Initializes \ ``cdev``\ , remembering \ ``fops``\ , making it ready to add to the
system with \ :c:func:`cdev_add`\ .

.. This file was automatic generated / don't edit.

