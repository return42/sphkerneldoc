.. -*- coding: utf-8; mode: rst -*-

==========
sata_sil.c
==========


.. _`sil_set_mode`:

sil_set_mode
============

.. c:function:: int sil_set_mode (struct ata_link *link, struct ata_device **r_failed)

    wrap set_mode functions

    :param struct ata_link \*link:
        link to set up

    :param struct ata_device \*\*r_failed:
        returned device when we fail



.. _`sil_set_mode.description`:

Description
-----------

Wrap the libata method for device setup as after the setup we need
to inspect the results and do some configuration work



.. _`sil_dev_config`:

sil_dev_config
==============

.. c:function:: void sil_dev_config (struct ata_device *dev)

    Apply device/host-specific errata fixups

    :param struct ata_device \*dev:
        Device to be examined



.. _`sil_dev_config.description`:

Description
-----------

After the IDENTIFY [PACKET] DEVICE step is complete, and a
device is known to be present, this function is called.
We apply two errata fixups which are specific to Silicon Image,
a Seagate and a Maxtor fixup.

For certain Seagate devices, we must limit the maximum sectors
to under 8K.

For certain Maxtor devices, we must not program the drive
beyond udma5.

Both fixups are unfairly pessimistic.  As soon as I get more
information on these errata, I will create a more exhaustive
list, and apply the fixups to only the specific
devices/hosts/firmwares that need it.

20040111 - Seagate drives affected by the Mod15Write bug are blacklisted
The Maxtor quirk is in the blacklist, but I'm keeping the original
pessimistic fix for the following reasons...
- There seems to be less info on it, only one device gleaned off the
Windows        driver, maybe only one is affected.  More info would be greatly
appreciated.
- But then again UDMA5 is hardly anything to complain about

