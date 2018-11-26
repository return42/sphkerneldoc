.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libata-transport.c

.. _`ata_is_port`:

ata_is_port
===========

.. c:function:: int ata_is_port(const struct device *dev)

    -  check if a struct device represents a ATA port

    :param dev:
        device to check
    :type dev: const struct device \*

.. _`ata_is_port.return`:

Return
------

\ ``1``\  if the device represents a ATA Port, \ ``0``\  else

.. _`ata_tport_delete`:

ata_tport_delete
================

.. c:function:: void ata_tport_delete(struct ata_port *ap)

    -  remove ATA PORT

    :param ap:
        *undescribed*
    :type ap: struct ata_port \*

.. _`ata_tport_delete.description`:

Description
-----------

Removes the specified ATA PORT.  Remove the associated link as well.

.. _`ata_is_link`:

ata_is_link
===========

.. c:function:: int ata_is_link(const struct device *dev)

    -  check if a struct device represents a ATA link

    :param dev:
        device to check
    :type dev: const struct device \*

.. _`ata_is_link.return`:

Return
------

\ ``1``\  if the device represents a ATA link, \ ``0``\  else

.. _`ata_tlink_delete`:

ata_tlink_delete
================

.. c:function:: void ata_tlink_delete(struct ata_link *link)

    -  remove ATA LINK

    :param link:
        *undescribed*
    :type link: struct ata_link \*

.. _`ata_tlink_delete.description`:

Description
-----------

Removes the specified ATA LINK.  remove associated ATA device(s) as well.

.. _`ata_tlink_add`:

ata_tlink_add
=============

.. c:function:: int ata_tlink_add(struct ata_link *link)

    -  initialize a transport ATA link structure

    :param link:
        allocated ata_link structure.
    :type link: struct ata_link \*

.. _`ata_tlink_add.description`:

Description
-----------

Initialize an ATA LINK structure for sysfs.  It will be added in the
device tree below the ATA PORT it belongs to.

Returns \ ``0``\  on success

.. _`ata_is_ata_dev`:

ata_is_ata_dev
==============

.. c:function:: int ata_is_ata_dev(const struct device *dev)

    -  check if a struct device represents a ATA device

    :param dev:
        device to check
    :type dev: const struct device \*

.. _`ata_is_ata_dev.return`:

Return
------

\ ``1``\  if the device represents a ATA device, \ ``0``\  else

.. _`ata_tdev_free`:

ata_tdev_free
=============

.. c:function:: void ata_tdev_free(struct ata_device *dev)

    -  free a ATA LINK

    :param dev:
        ATA PHY to free
    :type dev: struct ata_device \*

.. _`ata_tdev_free.description`:

Description
-----------

Frees the specified ATA PHY.

.. _`ata_tdev_free.note`:

Note
----

This function must only be called on a PHY that has not
successfully been added using \ :c:func:`ata_tdev_add`\ .

.. _`ata_tdev_delete`:

ata_tdev_delete
===============

.. c:function:: void ata_tdev_delete(struct ata_device *ata_dev)

    -  remove ATA device

    :param ata_dev:
        *undescribed*
    :type ata_dev: struct ata_device \*

.. _`ata_tdev_delete.description`:

Description
-----------

Removes the specified ATA device.

.. _`ata_tdev_add`:

ata_tdev_add
============

.. c:function:: int ata_tdev_add(struct ata_device *ata_dev)

    -  initialize a transport ATA device structure.

    :param ata_dev:
        ata_dev structure.
    :type ata_dev: struct ata_device \*

.. _`ata_tdev_add.description`:

Description
-----------

Initialize an ATA device structure for sysfs.  It will be added in the
device tree below the ATA LINK device it belongs to.

Returns \ ``0``\  on success

.. _`ata_attach_transport`:

ata_attach_transport
====================

.. c:function:: struct scsi_transport_template *ata_attach_transport( void)

    -  instantiate ATA transport template

    :param void:
        no arguments
    :type void: 

.. _`ata_release_transport`:

ata_release_transport
=====================

.. c:function:: void ata_release_transport(struct scsi_transport_template *t)

    -  release ATA transport template instance

    :param t:
        transport template instance
    :type t: struct scsi_transport_template \*

.. This file was automatic generated / don't edit.

