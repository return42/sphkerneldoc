.. -*- coding: utf-8; mode: rst -*-

.. _API-sil-dev-config:

==============
sil_dev_config
==============

*man sil_dev_config(9)*

*4.6.0-rc5*

Apply device/host-specific errata fixups


Synopsis
========

.. c:function:: void sil_dev_config( struct ata_device * dev )

Arguments
=========

``dev``
    Device to be examined


Description
===========

After the IDENTIFY [PACKET] DEVICE step is complete, and a device is
known to be present, this function is called. We apply two errata fixups
which are specific to Silicon Image, a Seagate and a Maxtor fixup.

For certain Seagate devices, we must limit the maximum sectors to under
8K.

For certain Maxtor devices, we must not program the drive beyond udma5.

Both fixups are unfairly pessimistic. As soon as I get more information
on these errata, I will create a more exhaustive list, and apply the
fixups to only the specific devices/hosts/firmwares that need it.

20040111 - Seagate drives affected by the Mod15Write bug are blacklisted
The Maxtor quirk is in the blacklist, but I'm keeping the original
pessimistic fix for the following reasons... - There seems to be less
info on it, only one device gleaned off the Windows driver, maybe only
one is affected. More info would be greatly appreciated. - But then
again UDMA5 is hardly anything to complain about


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
