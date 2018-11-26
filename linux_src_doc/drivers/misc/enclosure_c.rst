.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/enclosure.c

.. _`enclosure_find`:

enclosure_find
==============

.. c:function:: struct enclosure_device *enclosure_find(struct device *dev, struct enclosure_device *start)

    find an enclosure given a parent device

    :param dev:
        the parent to match against
    :type dev: struct device \*

    :param start:
        Optional enclosure device to start from (NULL if none)
    :type start: struct enclosure_device \*

.. _`enclosure_find.description`:

Description
-----------

Looks through the list of registered enclosures to find all those
with \ ``dev``\  as a parent.  Returns NULL if no enclosure is
found. \ ``start``\  can be used as a starting point to obtain multiple
enclosures per parent (should begin with NULL and then be set to
each returned enclosure device). Obtains a reference to the
enclosure class device which must be released with \ :c:func:`device_put`\ .
If \ ``start``\  is not NULL, a reference must be taken on it which is
released before returning (this allows a loop through all
enclosures to exit with only the reference on the enclosure of
interest held).  Note that the \ ``dev``\  may correspond to the actual
device housing the enclosure, in which case no iteration via \ ``start``\ 
is required.

.. _`enclosure_for_each_device`:

enclosure_for_each_device
=========================

.. c:function:: int enclosure_for_each_device(int (*fn)(struct enclosure_device *, void *), void *data)

    calls a function for each enclosure

    :param int (\*fn)(struct enclosure_device \*, void \*):
        the function to call

    :param data:
        the data to pass to each call
    :type data: void \*

.. _`enclosure_for_each_device.description`:

Description
-----------

Loops over all the enclosures calling the function.

Note, this function uses a mutex which will be held across calls to
\ ``fn``\ , so it must have non atomic context, and \ ``fn``\  may (although it
should not) sleep or otherwise cause the mutex to be held for
indefinite periods

.. _`enclosure_register`:

enclosure_register
==================

.. c:function:: struct enclosure_device *enclosure_register(struct device *dev, const char *name, int components, struct enclosure_component_callbacks *cb)

    register device as an enclosure

    :param dev:
        device containing the enclosure
    :type dev: struct device \*

    :param name:
        *undescribed*
    :type name: const char \*

    :param components:
        number of components in the enclosure
    :type components: int

    :param cb:
        *undescribed*
    :type cb: struct enclosure_component_callbacks \*

.. _`enclosure_register.description`:

Description
-----------

This sets up the device for being an enclosure.  Note that \ ``dev``\  does
not have to be a dedicated enclosure device.  It may be some other type
of device that additionally responds to enclosure services

.. _`enclosure_unregister`:

enclosure_unregister
====================

.. c:function:: void enclosure_unregister(struct enclosure_device *edev)

    remove an enclosure

    :param edev:
        the registered enclosure to remove;
    :type edev: struct enclosure_device \*

.. _`enclosure_component_alloc`:

enclosure_component_alloc
=========================

.. c:function:: struct enclosure_component *enclosure_component_alloc(struct enclosure_device *edev, unsigned int number, enum enclosure_component_type type, const char *name)

    prepare a new enclosure component

    :param edev:
        the enclosure to add the component
    :type edev: struct enclosure_device \*

    :param number:
        *undescribed*
    :type number: unsigned int

    :param type:
        the type of component being added
    :type type: enum enclosure_component_type

    :param name:
        an optional name to appear in sysfs (leave NULL if none)
    :type name: const char \*

.. _`enclosure_component_alloc.description`:

Description
-----------

The name is optional for enclosures that give their components a unique
name.  If not, leave the field NULL and a name will be assigned.

Returns a pointer to the enclosure component or an error.

.. _`enclosure_component_register`:

enclosure_component_register
============================

.. c:function:: int enclosure_component_register(struct enclosure_component *ecomp)

    publishes an initialized enclosure component

    :param ecomp:
        component to add
    :type ecomp: struct enclosure_component \*

.. _`enclosure_component_register.description`:

Description
-----------

Returns 0 on successful registration, releases the component otherwise

.. _`enclosure_add_device`:

enclosure_add_device
====================

.. c:function:: int enclosure_add_device(struct enclosure_device *edev, int component, struct device *dev)

    add a device as being part of an enclosure

    :param edev:
        the enclosure device being added to.
    :type edev: struct enclosure_device \*

    :param component:
        *undescribed*
    :type component: int

    :param dev:
        the device being added
    :type dev: struct device \*

.. _`enclosure_add_device.description`:

Description
-----------

Declares a real device to reside in slot (or identifier) \ ``num``\  of an
enclosure.  This will cause the relevant sysfs links to appear.
This function may also be used to change a device associated with
an enclosure without having to call \ :c:func:`enclosure_remove_device`\  in
between.

Returns zero on success or an error.

.. _`enclosure_remove_device`:

enclosure_remove_device
=======================

.. c:function:: int enclosure_remove_device(struct enclosure_device *edev, struct device *dev)

    remove a device from an enclosure

    :param edev:
        the enclosure device
    :type edev: struct enclosure_device \*

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`enclosure_remove_device.description`:

Description
-----------

Returns zero on success or an error.

.. This file was automatic generated / don't edit.

