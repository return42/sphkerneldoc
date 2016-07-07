.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/transport_class.c

.. _`transport_class_register`:

transport_class_register
========================

.. c:function:: int transport_class_register(struct transport_class *tclass)

    register an initial transport class

    :param struct transport_class \*tclass:
        a pointer to the transport class structure to be initialised

.. _`transport_class_register.description`:

Description
-----------

The transport class contains an embedded class which is used to
identify it.  The caller should initialise this structure with
zeros and then generic class must have been initialised with the
actual transport class unique name.  There's a macro
\ :c:func:`DECLARE_TRANSPORT_CLASS`\  to do this (declared classes still must
be registered).

Returns 0 on success or error on failure.

.. _`transport_class_unregister`:

transport_class_unregister
==========================

.. c:function:: void transport_class_unregister(struct transport_class *tclass)

    unregister a previously registered class

    :param struct transport_class \*tclass:
        The transport class to unregister

.. _`transport_class_unregister.description`:

Description
-----------

Must be called prior to deallocating the memory for the transport
class.

.. _`anon_transport_class_register`:

anon_transport_class_register
=============================

.. c:function:: int anon_transport_class_register(struct anon_transport_class *atc)

    register an anonymous class

    :param struct anon_transport_class \*atc:
        The anon transport class to register

.. _`anon_transport_class_register.description`:

Description
-----------

The anonymous transport class contains both a transport class and a
container.  The idea of an anonymous class is that it never
actually has any device attributes associated with it (and thus
saves on container storage).  So it can only be used for triggering
events.  Use prezero and then use \ :c:func:`DECLARE_ANON_TRANSPORT_CLASS`\  to
initialise the anon transport class storage.

.. _`anon_transport_class_unregister`:

anon_transport_class_unregister
===============================

.. c:function:: void anon_transport_class_unregister(struct anon_transport_class *atc)

    unregister an anon class

    :param struct anon_transport_class \*atc:
        Pointer to the anon transport class to unregister

.. _`anon_transport_class_unregister.description`:

Description
-----------

Must be called prior to deallocating the memory for the anon
transport class.

.. _`transport_setup_device`:

transport_setup_device
======================

.. c:function:: void transport_setup_device(struct device *dev)

    declare a new dev for transport class association but don't make it visible yet.

    :param struct device \*dev:
        the generic device representing the entity being added

.. _`transport_setup_device.description`:

Description
-----------

Usually, dev represents some component in the HBA system (either
the HBA itself or a device remote across the HBA bus).  This
routine is simply a trigger point to see if any set of transport
classes wishes to associate with the added device.  This allocates
storage for the class device and initialises it, but does not yet
add it to the system or add attributes to it (you do this with
transport_add_device).  If you have no need for a separate setup
and add operations, use transport_register_device (see
transport_class.h).

.. _`transport_add_device`:

transport_add_device
====================

.. c:function:: void transport_add_device(struct device *dev)

    declare a new dev for transport class association

    :param struct device \*dev:
        the generic device representing the entity being added

.. _`transport_add_device.description`:

Description
-----------

Usually, dev represents some component in the HBA system (either
the HBA itself or a device remote across the HBA bus).  This
routine is simply a trigger point used to add the device to the
system and register attributes for it.

.. _`transport_configure_device`:

transport_configure_device
==========================

.. c:function:: void transport_configure_device(struct device *dev)

    configure an already set up device

    :param struct device \*dev:
        generic device representing device to be configured

.. _`transport_configure_device.description`:

Description
-----------

The idea of configure is simply to provide a point within the setup
process to allow the transport class to extract information from a
device after it has been setup.  This is used in SCSI because we
have to have a setup device to begin using the HBA, but after we
send the initial inquiry, we use configure to extract the device
parameters.  The device need not have been added to be configured.

.. _`transport_remove_device`:

transport_remove_device
=======================

.. c:function:: void transport_remove_device(struct device *dev)

    remove the visibility of a device

    :param struct device \*dev:
        generic device to remove

.. _`transport_remove_device.description`:

Description
-----------

This call removes the visibility of the device (to the user from
sysfs), but does not destroy it.  To eliminate a device entirely
you must also call transport_destroy_device.  If you don't need to
do remove and destroy as separate operations, use
\ :c:func:`transport_unregister_device`\  (see transport_class.h) which will
perform both calls for you.

.. _`transport_destroy_device`:

transport_destroy_device
========================

.. c:function:: void transport_destroy_device(struct device *dev)

    destroy a removed device

    :param struct device \*dev:
        device to eliminate from the transport class.

.. _`transport_destroy_device.description`:

Description
-----------

This call triggers the elimination of storage associated with the
transport classdev.  Note: all it really does is relinquish a
reference to the classdev.  The memory will not be freed until the
last reference goes to zero.  Note also that the classdev retains a
reference count on dev, so dev too will remain for as long as the
transport class device remains around.

.. This file was automatic generated / don't edit.

