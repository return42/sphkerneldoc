.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/libata-transport.c

.. _`ata_is_port`:

ata_is_port
===========

.. c:function:: int ata_is_port(const struct device *dev)

    -  check if a struct device represents a ATA port

    :param const struct device \*dev:
        device to check

.. _`ata_is_port.return`:

Return
------

\ ``1``\  if the device represents a ATA Port, \ ``0``\  else

.. _`ata_tport_delete`:

ata_tport_delete
================

.. c:function:: void ata_tport_delete(struct ata_port *ap)

    -  remove ATA PORT

    :param struct ata_port \*ap:
        *undescribed*

.. _`ata_tport_delete.description`:

Description
-----------

Removes the specified ATA PORT.  Remove the associated link as well.

.. _`ata_is_link`:

ata_is_link
===========

.. c:function:: int ata_is_link(const struct device *dev)

    -  check if a struct device represents a ATA link

    :param const struct device \*dev:
        device to check

.. _`ata_is_link.return`:

Return
------

\ ``1``\  if the device represents a ATA link, \ ``0``\  else

.. _`ata_tlink_delete`:

ata_tlink_delete
================

.. c:function:: void ata_tlink_delete(struct ata_link *link)

    -  remove ATA LINK

    :param struct ata_link \*link:
        *undescribed*

.. _`ata_tlink_delete.description`:

Description
-----------

Removes the specified ATA LINK.  remove associated ATA device(s) as well.

.. _`ata_tlink_add`:

ata_tlink_add
=============

.. c:function:: int ata_tlink_add(struct ata_link *link)

    -  initialize a transport ATA link structure

    :param struct ata_link \*link:
        allocated ata_link structure.

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

    :param const struct device \*dev:
        device to check

.. _`ata_is_ata_dev.return`:

Return
------

\ ``1``\  if the device represents a ATA device, \ ``0``\  else

.. _`ata_tdev_free`:

ata_tdev_free
=============

.. c:function:: void ata_tdev_free(struct ata_device *dev)

    -  free a ATA LINK

    :param struct ata_device \*dev:
        ATA PHY to free

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

    :param struct ata_device \*ata_dev:
        *undescribed*

.. _`ata_tdev_delete.description`:

Description
-----------

Removes the specified ATA device.

.. _`ata_tdev_add`:

ata_tdev_add
============

.. c:function:: int ata_tdev_add(struct ata_device *ata_dev)

    -  initialize a transport ATA device structure.

    :param struct ata_device \*ata_dev:
        ata_dev structure.

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

    :param  void:
        no arguments

.. _`ata_release_transport`:

ata_release_transport
=====================

.. c:function:: void ata_release_transport(struct scsi_transport_template *t)

    -  release ATA transport template instance

    :param struct scsi_transport_template \*t:
        transport template instance

.. This file was automatic generated / don't edit.

