.. -*- coding: utf-8; mode: rst -*-

==========
char_dev.c
==========

.. _`register_chrdev_region`:

register_chrdev_region
======================

.. c:function:: int register_chrdev_region (dev_t from, unsigned count, const char *name)

    register a range of device numbers

    :param dev_t from:
        the first in the desired range of device numbers; must include
        the major number.

    :param unsigned count:
        the number of consecutive device numbers required

    :param const char \*name:
        the name of the device or driver.


.. _`register_chrdev_region.description`:

Description
-----------

Return value is zero on success, a negative error code on failure.


.. _`alloc_chrdev_region`:

alloc_chrdev_region
===================

.. c:function:: int alloc_chrdev_region (dev_t *dev, unsigned baseminor, unsigned count, const char *name)

    register a range of char device numbers

    :param dev_t \*dev:
        output parameter for first assigned number

    :param unsigned baseminor:
        first of the requested range of minor numbers

    :param unsigned count:
        the number of minor numbers required

    :param const char \*name:
        the name of the associated device or driver


.. _`alloc_chrdev_region.description`:

Description
-----------

Allocates a range of char device numbers.  The major number will be
chosen dynamically, and returned (along with the first minor number)
in ``dev``\ .  Returns zero or a negative error code.


.. _`__register_chrdev`:

__register_chrdev
=================

.. c:function:: int __register_chrdev (unsigned int major, unsigned int baseminor, unsigned int count, const char *name, const struct file_operations *fops)

    create and register a cdev occupying a range of minors

    :param unsigned int major:
        major device number or 0 for dynamic allocation

    :param unsigned int baseminor:
        first of the requested range of minor numbers

    :param unsigned int count:
        the number of minor numbers required

    :param const char \*name:
        name of this range of devices

    :param const struct file_operations \*fops:
        file operations associated with this devices


.. _`__register_chrdev.description`:

Description
-----------

If ``major`` == 0 this functions will dynamically allocate a major and return
its number.

If ``major`` > 0 this function will attempt to reserve a device with the given
major number and will return zero on success.

Returns a -ve errno on failure.

The name of this device has nothing to do with the name of the device in
/dev. It only helps to keep track of the different owners of devices. If
your module name has only one type of devices it's ok to use e.g. the name
of the module here.


.. _`unregister_chrdev_region`:

unregister_chrdev_region
========================

.. c:function:: void unregister_chrdev_region (dev_t from, unsigned count)

    unregister a range of device numbers

    :param dev_t from:
        the first in the range of numbers to unregister

    :param unsigned count:
        the number of device numbers to unregister


.. _`unregister_chrdev_region.description`:

Description
-----------

This function will unregister a range of ``count`` device numbers,
starting with ``from``\ .  The caller should normally be the one who
allocated those numbers in the first place...


.. _`__unregister_chrdev`:

__unregister_chrdev
===================

.. c:function:: void __unregister_chrdev (unsigned int major, unsigned int baseminor, unsigned int count, const char *name)

    unregister and destroy a cdev

    :param unsigned int major:
        major device number

    :param unsigned int baseminor:
        first of the range of minor numbers

    :param unsigned int count:
        the number of minor numbers this cdev is occupying

    :param const char \*name:
        name of this range of devices


.. _`__unregister_chrdev.description`:

Description
-----------

Unregister and destroy the cdev occupying the region described by
``major``\ , ``baseminor`` and ``count``\ .  This function undoes what
:c:func:`__register_chrdev` did.


.. _`cdev_add`:

cdev_add
========

.. c:function:: int cdev_add (struct cdev *p, dev_t dev, unsigned count)

    add a char device to the system

    :param struct cdev \*p:
        the cdev structure for the device

    :param dev_t dev:
        the first device number for which this device is responsible

    :param unsigned count:
        the number of consecutive minor numbers corresponding to this
        device


.. _`cdev_add.description`:

Description
-----------

:c:func:`cdev_add` adds the device represented by ``p`` to the system, making it
live immediately.  A negative error code is returned on failure.


.. _`cdev_del`:

cdev_del
========

.. c:function:: void cdev_del (struct cdev *p)

    remove a cdev from the system

    :param struct cdev \*p:
        the cdev structure to be removed


.. _`cdev_del.description`:

Description
-----------

:c:func:`cdev_del` removes ``p`` from the system, possibly freeing the structure
itself.


.. _`cdev_alloc`:

cdev_alloc
==========

.. c:function:: struct cdev *cdev_alloc ( void)

    allocate a cdev structure

    :param void:
        no arguments


.. _`cdev_alloc.description`:

Description
-----------


Allocates and returns a cdev structure, or NULL on failure.


.. _`cdev_init`:

cdev_init
=========

.. c:function:: void cdev_init (struct cdev *cdev, const struct file_operations *fops)

    initialize a cdev structure

    :param struct cdev \*cdev:
        the structure to initialize

    :param const struct file_operations \*fops:
        the file_operations for this device


.. _`cdev_init.description`:

Description
-----------

Initializes ``cdev``\ , remembering ``fops``\ , making it ready to add to the
system with :c:func:`cdev_add`.

