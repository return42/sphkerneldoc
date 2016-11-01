.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/attribute_container.c

.. _`attribute_container_classdev_to_container`:

attribute_container_classdev_to_container
=========================================

.. c:function:: struct attribute_container *attribute_container_classdev_to_container(struct device *classdev)

    given a classdev, return the container

    :param struct device \*classdev:
        the class device created by attribute_container_add_device.

.. _`attribute_container_classdev_to_container.description`:

Description
-----------

Returns the container associated with this classdev.

.. _`attribute_container_register`:

attribute_container_register
============================

.. c:function:: int attribute_container_register(struct attribute_container *cont)

    register an attribute container

    :param struct attribute_container \*cont:
        The container to register.  This must be allocated by the
        callee and should also be zeroed by it.

.. _`attribute_container_unregister`:

attribute_container_unregister
==============================

.. c:function:: int attribute_container_unregister(struct attribute_container *cont)

    remove a container registration

    :param struct attribute_container \*cont:
        previously registered container to remove

.. _`attribute_container_add_device`:

attribute_container_add_device
==============================

.. c:function:: void attribute_container_add_device(struct device *dev, int (*fn)(struct attribute_container *, struct device *, struct device *))

    see if any container is interested in dev

    :param struct device \*dev:
        device to add attributes to

    :param int (\*fn)(struct attribute_container \*, struct device \*, struct device \*):
        function to trigger addition of class device.

.. _`attribute_container_add_device.description`:

Description
-----------

This function allocates storage for the class device(s) to be
attached to dev (one for each matching attribute_container).  If no
fn is provided, the code will simply register the class device via
device_add.  If a function is provided, it is expected to add
the class device at the appropriate time.  One of the things that
might be necessary is to allocate and initialise the classdev and
then add it a later time.  To do this, call this routine for
allocation and initialisation and then use
\ :c:func:`attribute_container_device_trigger`\  to call \ :c:func:`device_add`\  on
it.  Note: after this, the class device contains a reference to dev
which is not relinquished until the release of the classdev.

.. _`attribute_container_remove_device`:

attribute_container_remove_device
=================================

.. c:function:: void attribute_container_remove_device(struct device *dev, void (*fn)(struct attribute_container *, struct device *, struct device *))

    make device eligible for removal.

    :param struct device \*dev:
        The generic device

    :param void (\*fn)(struct attribute_container \*, struct device \*, struct device \*):
        A function to call to remove the device

.. _`attribute_container_remove_device.description`:

Description
-----------

This routine triggers device removal.  If fn is NULL, then it is
simply done via device_unregister (note that if something
still has a reference to the classdev, then the memory occupied
will not be freed until the classdev is released).  If you want a

.. _`attribute_container_remove_device.two-phase-release`:

two phase release
-----------------

remove from visibility and then delete the
device, then you should use this routine with a fn that calls
\ :c:func:`device_del`\  and then use \ :c:func:`attribute_container_device_trigger`\ 
to do the final put on the classdev.

.. _`attribute_container_device_trigger`:

attribute_container_device_trigger
==================================

.. c:function:: void attribute_container_device_trigger(struct device *dev, int (*fn)(struct attribute_container *, struct device *, struct device *))

    execute a trigger for each matching classdev

    :param struct device \*dev:
        The generic device to run the trigger for
        \ ``fn``\     the function to execute for each classdev.

    :param int (\*fn)(struct attribute_container \*, struct device \*, struct device \*):
        *undescribed*

.. _`attribute_container_device_trigger.description`:

Description
-----------

This function is for executing a trigger when you need to know both
the container and the classdev.  If you only care about the
container, then use \ :c:func:`attribute_container_trigger`\  instead.

.. _`attribute_container_trigger`:

attribute_container_trigger
===========================

.. c:function:: void attribute_container_trigger(struct device *dev, int (*fn)(struct attribute_container *, struct device *))

    trigger a function for each matching container

    :param struct device \*dev:
        The generic device to activate the trigger for

    :param int (\*fn)(struct attribute_container \*, struct device \*):
        the function to trigger

.. _`attribute_container_trigger.description`:

Description
-----------

This routine triggers a function that only needs to know the
matching containers (not the classdev) associated with a device.
It is more lightweight than attribute_container_device_trigger, so
should be used in preference unless the triggering function
actually needs to know the classdev.

.. _`attribute_container_add_attrs`:

attribute_container_add_attrs
=============================

.. c:function:: int attribute_container_add_attrs(struct device *classdev)

    add attributes

    :param struct device \*classdev:
        The class device

.. _`attribute_container_add_attrs.description`:

Description
-----------

This simply creates all the class device sysfs files from the
attributes listed in the container

.. _`attribute_container_add_class_device`:

attribute_container_add_class_device
====================================

.. c:function:: int attribute_container_add_class_device(struct device *classdev)

    same function as device_add

    :param struct device \*classdev:
        the class device to add

.. _`attribute_container_add_class_device.description`:

Description
-----------

This performs essentially the same function as device_add except for
attribute containers, namely add the classdev to the system and then
create the attribute files

.. _`attribute_container_add_class_device_adapter`:

attribute_container_add_class_device_adapter
============================================

.. c:function:: int attribute_container_add_class_device_adapter(struct attribute_container *cont, struct device *dev, struct device *classdev)

    simple adapter for triggers

    :param struct attribute_container \*cont:
        *undescribed*

    :param struct device \*dev:
        *undescribed*

    :param struct device \*classdev:
        *undescribed*

.. _`attribute_container_add_class_device_adapter.description`:

Description
-----------

This function is identical to attribute_container_add_class_device except
that it is designed to be called from the triggers

.. _`attribute_container_remove_attrs`:

attribute_container_remove_attrs
================================

.. c:function:: void attribute_container_remove_attrs(struct device *classdev)

    remove any attribute files

    :param struct device \*classdev:
        The class device to remove the files from

.. _`attribute_container_class_device_del`:

attribute_container_class_device_del
====================================

.. c:function:: void attribute_container_class_device_del(struct device *classdev)

    equivalent of class_device_del

    :param struct device \*classdev:
        the class device

.. _`attribute_container_class_device_del.description`:

Description
-----------

This function simply removes all the attribute files and then calls
device_del.

.. _`attribute_container_find_class_device`:

attribute_container_find_class_device
=====================================

.. c:function:: struct device *attribute_container_find_class_device(struct attribute_container *cont, struct device *dev)

    find the corresponding class_device

    :param struct attribute_container \*cont:
        the container

    :param struct device \*dev:
        the generic device

.. _`attribute_container_find_class_device.description`:

Description
-----------

Looks up the device in the container's list of class devices and returns
the corresponding class_device.

.. This file was automatic generated / don't edit.

