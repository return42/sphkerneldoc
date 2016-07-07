.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/class.c

.. _`__class_create`:

__class_create
==============

.. c:function:: struct class *__class_create(struct module *owner, const char *name, struct lock_class_key *key)

    create a struct class structure

    :param struct module \*owner:
        pointer to the module that is to "own" this struct class

    :param const char \*name:
        pointer to a string for the name of this class.

    :param struct lock_class_key \*key:
        the lock_class_key for this class; used by mutex lock debugging

.. _`__class_create.description`:

Description
-----------

This is used to create a struct class pointer that can then be used
in calls to \ :c:func:`device_create`\ .

Returns \ :c:type:`struct class <class>`\  pointer on success, or \ :c:func:`ERR_PTR`\  on error.

Note, the pointer created here is to be destroyed when finished by
making a call to \ :c:func:`class_destroy`\ .

.. _`class_destroy`:

class_destroy
=============

.. c:function:: void class_destroy(struct class *cls)

    destroys a struct class structure

    :param struct class \*cls:
        pointer to the struct class that is to be destroyed

.. _`class_destroy.description`:

Description
-----------

Note, the pointer to be destroyed must have been created with a call
to \ :c:func:`class_create`\ .

.. _`class_dev_iter_init`:

class_dev_iter_init
===================

.. c:function:: void class_dev_iter_init(struct class_dev_iter *iter, struct class *class, struct device *start, const struct device_type *type)

    initialize class device iterator

    :param struct class_dev_iter \*iter:
        class iterator to initialize

    :param struct class \*class:
        the class we wanna iterate over

    :param struct device \*start:
        the device to start iterating from, if any

    :param const struct device_type \*type:
        device_type of the devices to iterate over, NULL for all

.. _`class_dev_iter_init.description`:

Description
-----------

Initialize class iterator \ ``iter``\  such that it iterates over devices
of \ ``class``\ .  If \ ``start``\  is set, the list iteration will start there,
otherwise if it is NULL, the iteration starts at the beginning of
the list.

.. _`class_dev_iter_next`:

class_dev_iter_next
===================

.. c:function:: struct device *class_dev_iter_next(struct class_dev_iter *iter)

    iterate to the next device

    :param struct class_dev_iter \*iter:
        class iterator to proceed

.. _`class_dev_iter_next.description`:

Description
-----------

Proceed \ ``iter``\  to the next device and return it.  Returns NULL if
iteration is complete.

The returned device is referenced and won't be released till
iterator is proceed to the next device or exited.  The caller is
free to do whatever it wants to do with the device including
calling back into class code.

.. _`class_dev_iter_exit`:

class_dev_iter_exit
===================

.. c:function:: void class_dev_iter_exit(struct class_dev_iter *iter)

    finish iteration

    :param struct class_dev_iter \*iter:
        class iterator to finish

.. _`class_dev_iter_exit.description`:

Description
-----------

Finish an iteration.  Always call this function after iteration is
complete whether the iteration ran till the end or not.

.. _`class_for_each_device`:

class_for_each_device
=====================

.. c:function:: int class_for_each_device(struct class *class, struct device *start, void *data, int (*) fn (struct device *, void *)

    device iterator

    :param struct class \*class:
        the class we're iterating

    :param struct device \*start:
        the device to start with in the list, if any.

    :param void \*data:
        data for the callback

    :param (int (\*) fn (struct device \*, void \*):
        function to be called for each device

.. _`class_for_each_device.description`:

Description
-----------

Iterate over \ ``class``\ 's list of devices, and call \ ``fn``\  for each,
passing it \ ``data``\ .  If \ ``start``\  is set, the list iteration will start
there, otherwise if it is NULL, the iteration starts at the
beginning of the list.

We check the return of \ ``fn``\  each time. If it returns anything
other than 0, we break out and return that value.

\ ``fn``\  is allowed to do anything including calling back into class
code.  There's no locking restriction.

.. _`class_find_device`:

class_find_device
=================

.. c:function:: struct device *class_find_device(struct class *class, struct device *start, const void *data, int (*) match (struct device *, const void *)

    device iterator for locating a particular device

    :param struct class \*class:
        the class we're iterating

    :param struct device \*start:
        Device to begin with

    :param const void \*data:
        data for the match function

    :param (int (\*) match (struct device \*, const void \*):
        function to check device

.. _`class_find_device.description`:

Description
-----------

This is similar to the \ :c:func:`class_for_each_dev`\  function above, but it
returns a reference to a device that is 'found' for later use, as
determined by the \ ``match``\  callback.

The callback should return 0 if the device doesn't match and non-zero
if it does.  If the callback returns non-zero, this function will
return to the caller and not iterate over any more devices.

Note, you will need to drop the reference with \ :c:func:`put_device`\  after use.

\ ``match``\  is allowed to do anything including calling back into class
code.  There's no locking restriction.

.. _`class_compat_register`:

class_compat_register
=====================

.. c:function:: struct class_compat *class_compat_register(const char *name)

    register a compatibility class

    :param const char \*name:
        the name of the class

.. _`class_compat_register.description`:

Description
-----------

Compatibility class are meant as a temporary user-space compatibility
workaround when converting a family of class devices to a bus devices.

.. _`class_compat_unregister`:

class_compat_unregister
=======================

.. c:function:: void class_compat_unregister(struct class_compat *cls)

    unregister a compatibility class

    :param struct class_compat \*cls:
        the class to unregister

.. _`class_compat_create_link`:

class_compat_create_link
========================

.. c:function:: int class_compat_create_link(struct class_compat *cls, struct device *dev, struct device *device_link)

    create a compatibility class device link to a bus device

    :param struct class_compat \*cls:
        the compatibility class

    :param struct device \*dev:
        the target bus device

    :param struct device \*device_link:
        an optional device to which a "device" link should be created

.. _`class_compat_remove_link`:

class_compat_remove_link
========================

.. c:function:: void class_compat_remove_link(struct class_compat *cls, struct device *dev, struct device *device_link)

    remove a compatibility class device link to a bus device

    :param struct class_compat \*cls:
        the compatibility class

    :param struct device \*dev:
        the target bus device

    :param struct device \*device_link:
        an optional device to which a "device" link was previously
        created

.. This file was automatic generated / don't edit.

