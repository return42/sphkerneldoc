.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/ipr.h

.. _`ipr_is_ioa_resource`:

ipr_is_ioa_resource
===================

.. c:function:: int ipr_is_ioa_resource(struct ipr_resource_entry *res)

    Determine if a resource is the IOA

    :param struct ipr_resource_entry \*res:
        resource entry struct

.. _`ipr_is_ioa_resource.return-value`:

Return value
------------

1 if IOA / 0 if not IOA

.. _`ipr_is_af_dasd_device`:

ipr_is_af_dasd_device
=====================

.. c:function:: int ipr_is_af_dasd_device(struct ipr_resource_entry *res)

    Determine if a resource is an AF DASD

    :param struct ipr_resource_entry \*res:
        resource entry struct

.. _`ipr_is_af_dasd_device.return-value`:

Return value
------------

1 if AF DASD / 0 if not AF DASD

.. _`ipr_is_vset_device`:

ipr_is_vset_device
==================

.. c:function:: int ipr_is_vset_device(struct ipr_resource_entry *res)

    Determine if a resource is a VSET

    :param struct ipr_resource_entry \*res:
        resource entry struct

.. _`ipr_is_vset_device.return-value`:

Return value
------------

1 if VSET / 0 if not VSET

.. _`ipr_is_gscsi`:

ipr_is_gscsi
============

.. c:function:: int ipr_is_gscsi(struct ipr_resource_entry *res)

    Determine if a resource is a generic scsi resource

    :param struct ipr_resource_entry \*res:
        resource entry struct

.. _`ipr_is_gscsi.return-value`:

Return value
------------

1 if GSCSI / 0 if not GSCSI

.. _`ipr_is_scsi_disk`:

ipr_is_scsi_disk
================

.. c:function:: int ipr_is_scsi_disk(struct ipr_resource_entry *res)

    Determine if a resource is a SCSI disk

    :param struct ipr_resource_entry \*res:
        resource entry struct

.. _`ipr_is_scsi_disk.return-value`:

Return value
------------

1 if SCSI disk / 0 if not SCSI disk

.. _`ipr_is_gata`:

ipr_is_gata
===========

.. c:function:: int ipr_is_gata(struct ipr_resource_entry *res)

    Determine if a resource is a generic ATA resource

    :param struct ipr_resource_entry \*res:
        resource entry struct

.. _`ipr_is_gata.return-value`:

Return value
------------

1 if GATA / 0 if not GATA

.. _`ipr_is_naca_model`:

ipr_is_naca_model
=================

.. c:function:: int ipr_is_naca_model(struct ipr_resource_entry *res)

    Determine if a resource is using NACA queueing model

    :param struct ipr_resource_entry \*res:
        resource entry struct

.. _`ipr_is_naca_model.return-value`:

Return value
------------

1 if NACA queueing model / 0 if not NACA queueing model

.. _`ipr_is_device`:

ipr_is_device
=============

.. c:function:: int ipr_is_device(struct ipr_hostrcb *hostrcb)

    Determine if the hostrcb structure is related to a device

    :param struct ipr_hostrcb \*hostrcb:
        host resource control blocks struct

.. _`ipr_is_device.return-value`:

Return value
------------

1 if AF / 0 if not AF

.. _`ipr_sdt_is_fmt2`:

ipr_sdt_is_fmt2
===============

.. c:function:: int ipr_sdt_is_fmt2(u32 sdt_word)

    Determine if a SDT address is in format 2

    :param u32 sdt_word:
        SDT address

.. _`ipr_sdt_is_fmt2.return-value`:

Return value
------------

1 if format 2 / 0 if not

.. This file was automatic generated / don't edit.

