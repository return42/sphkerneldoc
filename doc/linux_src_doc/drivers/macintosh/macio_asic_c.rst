.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/macintosh/macio_asic.c

.. _`macio_release_dev`:

macio_release_dev
=================

.. c:function:: void macio_release_dev(struct device *dev)

    free a macio device structure when all users of it are finished.

    :param struct device \*dev:
        device that's been disconnected

.. _`macio_release_dev.description`:

Description
-----------

Will be called only by the device core when all users of this macio device
are done. This currently means never as we don't hot remove any macio
device yet, though that will happen with mediabay based devices in a later
implementation.

.. _`macio_resource_quirks`:

macio_resource_quirks
=====================

.. c:function:: int macio_resource_quirks(struct device_node *np, struct resource *res, int index)

    tweak or skip some resources for a device

    :param struct device_node \*np:
        pointer to the device node

    :param struct resource \*res:
        resulting resource

    :param int index:
        index of resource in node

.. _`macio_resource_quirks.description`:

Description
-----------

If this routine returns non-null, then the resource is completely
skipped.

.. _`macio_add_one_device`:

macio_add_one_device
====================

.. c:function:: struct macio_dev *macio_add_one_device(struct macio_chip *chip, struct device *parent, struct device_node *np, struct macio_dev *in_bay, struct resource *parent_res)

    Add one device from OF node to the device tree

    :param struct macio_chip \*chip:
        pointer to the macio_chip holding the device

    :param struct device \*parent:
        *undescribed*

    :param struct device_node \*np:
        pointer to the device node in the OF tree

    :param struct macio_dev \*in_bay:
        set to 1 if device is part of a media-bay

    :param struct resource \*parent_res:
        *undescribed*

.. _`macio_add_one_device.description`:

Description
-----------

When media-bay is changed to hotswap drivers, this function will
be exposed to the bay driver some way...

.. _`macio_pci_add_devices`:

macio_pci_add_devices
=====================

.. c:function:: void macio_pci_add_devices(struct macio_chip *chip)

    Adds sub-devices of mac-io to the device tree

    :param struct macio_chip \*chip:
        pointer to the macio_chip holding the devices

.. _`macio_pci_add_devices.description`:

Description
-----------

This function will do the job of extracting devices from the
Open Firmware device tree, build macio_dev structures and add
them to the Linux device tree.

For now, childs of media-bay are added now as well. This will
change rsn though.

.. _`macio_register_driver`:

macio_register_driver
=====================

.. c:function:: int macio_register_driver(struct macio_driver *drv)

    Registers a new MacIO device driver

    :param struct macio_driver \*drv:
        pointer to the driver definition structure

.. _`macio_unregister_driver`:

macio_unregister_driver
=======================

.. c:function:: void macio_unregister_driver(struct macio_driver *drv)

    Unregisters a new MacIO device driver

    :param struct macio_driver \*drv:
        pointer to the driver definition structure

.. _`macio_request_resource`:

macio_request_resource
======================

.. c:function:: int macio_request_resource(struct macio_dev *dev, int resource_no, const char *name)

    Request an MMIO resource

    :param struct macio_dev \*dev:
        pointer to the device holding the resource

    :param int resource_no:
        resource number to request

    :param const char \*name:
        resource name

.. _`macio_request_resource.description`:

Description
-----------

Mark  memory region number \ ``resource_no``\  associated with MacIO
device \ ``dev``\  as being reserved by owner \ ``name``\ .  Do not access
any address inside the memory regions unless this call returns
successfully.

Returns 0 on success, or \ ``EBUSY``\  on error.  A warning
message is also printed on failure.

.. _`macio_release_resource`:

macio_release_resource
======================

.. c:function:: void macio_release_resource(struct macio_dev *dev, int resource_no)

    Release an MMIO resource

    :param struct macio_dev \*dev:
        pointer to the device holding the resource

    :param int resource_no:
        resource number to release

.. _`macio_request_resources`:

macio_request_resources
=======================

.. c:function:: int macio_request_resources(struct macio_dev *dev, const char *name)

    Reserve all memory resources

    :param struct macio_dev \*dev:
        MacIO device whose resources are to be reserved

    :param const char \*name:
        Name to be associated with resource.

.. _`macio_request_resources.description`:

Description
-----------

Mark all memory regions associated with MacIO device \ ``dev``\  as
being reserved by owner \ ``name``\ .  Do not access any address inside
the memory regions unless this call returns successfully.

Returns 0 on success, or \ ``EBUSY``\  on error.  A warning
message is also printed on failure.

.. _`macio_release_resources`:

macio_release_resources
=======================

.. c:function:: void macio_release_resources(struct macio_dev *dev)

    Release reserved memory resources

    :param struct macio_dev \*dev:
        MacIO device whose resources were previously reserved

.. This file was automatic generated / don't edit.

