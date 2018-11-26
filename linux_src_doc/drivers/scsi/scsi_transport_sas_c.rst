.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/scsi_transport_sas.c

.. _`sas_remove_children`:

sas_remove_children
===================

.. c:function:: void sas_remove_children(struct device *dev)

    tear down a devices SAS data structures

    :param dev:
        device belonging to the sas object
    :type dev: struct device \*

.. _`sas_remove_children.description`:

Description
-----------

Removes all SAS PHYs and remote PHYs for a given object

.. _`sas_remove_host`:

sas_remove_host
===============

.. c:function:: void sas_remove_host(struct Scsi_Host *shost)

    tear down a Scsi_Host's SAS data structures

    :param shost:
        Scsi Host that is torn down
    :type shost: struct Scsi_Host \*

.. _`sas_remove_host.description`:

Description
-----------

Removes all SAS PHYs and remote PHYs for a given Scsi_Host and remove the
Scsi_Host as well.

.. _`sas_remove_host.note`:

Note
----

Do not call \ :c:func:`scsi_remove_host`\  on the Scsi_Host any more, as it is
already removed.

.. _`sas_get_address`:

sas_get_address
===============

.. c:function:: u64 sas_get_address(struct scsi_device *sdev)

    return the SAS address of the device

    :param sdev:
        scsi device
    :type sdev: struct scsi_device \*

.. _`sas_get_address.description`:

Description
-----------

Returns the SAS address of the scsi device

.. _`sas_tlr_supported`:

sas_tlr_supported
=================

.. c:function:: unsigned int sas_tlr_supported(struct scsi_device *sdev)

    checking TLR bit in vpd 0x90

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`sas_tlr_supported.description`:

Description
-----------

Check Transport Layer Retries are supported or not.
If vpd page 0x90 is present, TRL is supported.

.. _`sas_disable_tlr`:

sas_disable_tlr
===============

.. c:function:: void sas_disable_tlr(struct scsi_device *sdev)

    setting TLR flags

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`sas_disable_tlr.description`:

Description
-----------

Seting tlr_enabled flag to 0.

.. _`sas_enable_tlr`:

sas_enable_tlr
==============

.. c:function:: void sas_enable_tlr(struct scsi_device *sdev)

    setting TLR flags

    :param sdev:
        scsi device struct
    :type sdev: struct scsi_device \*

.. _`sas_enable_tlr.description`:

Description
-----------

Seting tlr_enabled flag 1.

.. _`sas_phy_alloc`:

sas_phy_alloc
=============

.. c:function:: struct sas_phy *sas_phy_alloc(struct device *parent, int number)

    allocates and initialize a SAS PHY structure

    :param parent:
        Parent device
    :type parent: struct device \*

    :param number:
        Phy index
    :type number: int

.. _`sas_phy_alloc.description`:

Description
-----------

Allocates an SAS PHY structure.  It will be added in the device tree
below the device specified by \ ``parent``\ , which has to be either a Scsi_Host
or sas_rphy.

.. _`sas_phy_alloc.return`:

Return
------

     SAS PHY allocated or \ ``NULL``\  if the allocation failed.

.. _`sas_phy_add`:

sas_phy_add
===========

.. c:function:: int sas_phy_add(struct sas_phy *phy)

    add a SAS PHY to the device hierarchy

    :param phy:
        The PHY to be added
    :type phy: struct sas_phy \*

.. _`sas_phy_add.description`:

Description
-----------

Publishes a SAS PHY to the rest of the system.

.. _`sas_phy_free`:

sas_phy_free
============

.. c:function:: void sas_phy_free(struct sas_phy *phy)

    free a SAS PHY

    :param phy:
        SAS PHY to free
    :type phy: struct sas_phy \*

.. _`sas_phy_free.description`:

Description
-----------

Frees the specified SAS PHY.

.. _`sas_phy_free.note`:

Note
----

  This function must only be called on a PHY that has not
  successfully been added using \ :c:func:`sas_phy_add`\ .

.. _`sas_phy_delete`:

sas_phy_delete
==============

.. c:function:: void sas_phy_delete(struct sas_phy *phy)

    remove SAS PHY

    :param phy:
        SAS PHY to remove
    :type phy: struct sas_phy \*

.. _`sas_phy_delete.description`:

Description
-----------

Removes the specified SAS PHY.  If the SAS PHY has an
associated remote PHY it is removed before.

.. _`scsi_is_sas_phy`:

scsi_is_sas_phy
===============

.. c:function:: int scsi_is_sas_phy(const struct device *dev)

    check if a struct device represents a SAS PHY

    :param dev:
        device to check
    :type dev: const struct device \*

.. _`scsi_is_sas_phy.return`:

Return
------

     \ ``1``\  if the device represents a SAS PHY, \ ``0``\  else

.. _`sas_port_add`:

sas_port_add
============

.. c:function:: int sas_port_add(struct sas_port *port)

    add a SAS port to the device hierarchy

    :param port:
        port to be added
    :type port: struct sas_port \*

.. _`sas_port_add.description`:

Description
-----------

publishes a port to the rest of the system

.. _`sas_port_free`:

sas_port_free
=============

.. c:function:: void sas_port_free(struct sas_port *port)

    free a SAS PORT

    :param port:
        SAS PORT to free
    :type port: struct sas_port \*

.. _`sas_port_free.description`:

Description
-----------

Frees the specified SAS PORT.

.. _`sas_port_free.note`:

Note
----

  This function must only be called on a PORT that has not
  successfully been added using \ :c:func:`sas_port_add`\ .

.. _`sas_port_delete`:

sas_port_delete
===============

.. c:function:: void sas_port_delete(struct sas_port *port)

    remove SAS PORT

    :param port:
        SAS PORT to remove
    :type port: struct sas_port \*

.. _`sas_port_delete.description`:

Description
-----------

Removes the specified SAS PORT.  If the SAS PORT has an
associated phys, unlink them from the port as well.

.. _`scsi_is_sas_port`:

scsi_is_sas_port
================

.. c:function:: int scsi_is_sas_port(const struct device *dev)

    check if a struct device represents a SAS port

    :param dev:
        device to check
    :type dev: const struct device \*

.. _`scsi_is_sas_port.return`:

Return
------

     \ ``1``\  if the device represents a SAS Port, \ ``0``\  else

.. _`sas_port_get_phy`:

sas_port_get_phy
================

.. c:function:: struct sas_phy *sas_port_get_phy(struct sas_port *port)

    try to take a reference on a port member

    :param port:
        port to check
    :type port: struct sas_port \*

.. _`sas_port_add_phy`:

sas_port_add_phy
================

.. c:function:: void sas_port_add_phy(struct sas_port *port, struct sas_phy *phy)

    add another phy to a port to form a wide port

    :param port:
        port to add the phy to
    :type port: struct sas_port \*

    :param phy:
        phy to add
    :type phy: struct sas_phy \*

.. _`sas_port_add_phy.description`:

Description
-----------

When a port is initially created, it is empty (has no phys).  All
ports must have at least one phy to operated, and all wide ports
must have at least two.  The current code makes no difference
between ports and wide ports, but the only object that can be
connected to a remote device is a port, so ports must be formed on
all devices with phys if they're connected to anything.

.. _`sas_port_delete_phy`:

sas_port_delete_phy
===================

.. c:function:: void sas_port_delete_phy(struct sas_port *port, struct sas_phy *phy)

    remove a phy from a port or wide port

    :param port:
        port to remove the phy from
    :type port: struct sas_port \*

    :param phy:
        phy to remove
    :type phy: struct sas_phy \*

.. _`sas_port_delete_phy.description`:

Description
-----------

This operation is used for tearing down ports again.  It must be
done to every port or wide port before calling sas_port_delete.

.. _`sas_rphy_initialize`:

sas_rphy_initialize
===================

.. c:function:: void sas_rphy_initialize(struct sas_rphy *rphy)

    common rphy initialization

    :param rphy:
        rphy to initialise
    :type rphy: struct sas_rphy \*

.. _`sas_rphy_initialize.description`:

Description
-----------

Used by both \ :c:func:`sas_end_device_alloc`\  and \ :c:func:`sas_expander_alloc`\  to
initialise the common rphy component of each.

.. _`sas_end_device_alloc`:

sas_end_device_alloc
====================

.. c:function:: struct sas_rphy *sas_end_device_alloc(struct sas_port *parent)

    allocate an rphy for an end device

    :param parent:
        which port
    :type parent: struct sas_port \*

.. _`sas_end_device_alloc.description`:

Description
-----------

Allocates an SAS remote PHY structure, connected to \ ``parent``\ .

.. _`sas_end_device_alloc.return`:

Return
------

     SAS PHY allocated or \ ``NULL``\  if the allocation failed.

.. _`sas_expander_alloc`:

sas_expander_alloc
==================

.. c:function:: struct sas_rphy *sas_expander_alloc(struct sas_port *parent, enum sas_device_type type)

    allocate an rphy for an end device

    :param parent:
        which port
    :type parent: struct sas_port \*

    :param type:
        SAS_EDGE_EXPANDER_DEVICE or SAS_FANOUT_EXPANDER_DEVICE
    :type type: enum sas_device_type

.. _`sas_expander_alloc.description`:

Description
-----------

Allocates an SAS remote PHY structure, connected to \ ``parent``\ .

.. _`sas_expander_alloc.return`:

Return
------

     SAS PHY allocated or \ ``NULL``\  if the allocation failed.

.. _`sas_rphy_add`:

sas_rphy_add
============

.. c:function:: int sas_rphy_add(struct sas_rphy *rphy)

    add a SAS remote PHY to the device hierarchy

    :param rphy:
        The remote PHY to be added
    :type rphy: struct sas_rphy \*

.. _`sas_rphy_add.description`:

Description
-----------

Publishes a SAS remote PHY to the rest of the system.

.. _`sas_rphy_free`:

sas_rphy_free
=============

.. c:function:: void sas_rphy_free(struct sas_rphy *rphy)

    free a SAS remote PHY

    :param rphy:
        SAS remote PHY to free
    :type rphy: struct sas_rphy \*

.. _`sas_rphy_free.description`:

Description
-----------

Frees the specified SAS remote PHY.

.. _`sas_rphy_free.note`:

Note
----

  This function must only be called on a remote
  PHY that has not successfully been added using
  \ :c:func:`sas_rphy_add`\  (or has been \ :c:func:`sas_rphy_remove`\ 'd)

.. _`sas_rphy_delete`:

sas_rphy_delete
===============

.. c:function:: void sas_rphy_delete(struct sas_rphy *rphy)

    remove and free SAS remote PHY

    :param rphy:
        SAS remote PHY to remove and free
    :type rphy: struct sas_rphy \*

.. _`sas_rphy_delete.description`:

Description
-----------

Removes the specified SAS remote PHY and frees it.

.. _`sas_rphy_unlink`:

sas_rphy_unlink
===============

.. c:function:: void sas_rphy_unlink(struct sas_rphy *rphy)

    unlink SAS remote PHY

    :param rphy:
        SAS remote phy to unlink from its parent port
    :type rphy: struct sas_rphy \*

.. _`sas_rphy_unlink.description`:

Description
-----------

Removes port reference to an rphy

.. _`sas_rphy_remove`:

sas_rphy_remove
===============

.. c:function:: void sas_rphy_remove(struct sas_rphy *rphy)

    remove SAS remote PHY

    :param rphy:
        SAS remote phy to remove
    :type rphy: struct sas_rphy \*

.. _`sas_rphy_remove.description`:

Description
-----------

Removes the specified SAS remote PHY.

.. _`scsi_is_sas_rphy`:

scsi_is_sas_rphy
================

.. c:function:: int scsi_is_sas_rphy(const struct device *dev)

    check if a struct device represents a SAS remote PHY

    :param dev:
        device to check
    :type dev: const struct device \*

.. _`scsi_is_sas_rphy.return`:

Return
------

     \ ``1``\  if the device represents a SAS remote PHY, \ ``0``\  else

.. _`sas_attach_transport`:

sas_attach_transport
====================

.. c:function:: struct scsi_transport_template *sas_attach_transport(struct sas_function_template *ft)

    instantiate SAS transport template

    :param ft:
        SAS transport class function template
    :type ft: struct sas_function_template \*

.. _`sas_release_transport`:

sas_release_transport
=====================

.. c:function:: void sas_release_transport(struct scsi_transport_template *t)

    release SAS transport template instance

    :param t:
        transport template instance
    :type t: struct scsi_transport_template \*

.. This file was automatic generated / don't edit.

