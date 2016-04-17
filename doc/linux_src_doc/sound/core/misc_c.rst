.. -*- coding: utf-8; mode: rst -*-

======
misc.c
======


.. _`snd_pci_quirk_lookup_id`:

snd_pci_quirk_lookup_id
=======================

.. c:function:: const struct snd_pci_quirk *snd_pci_quirk_lookup_id (u16 vendor, u16 device, const struct snd_pci_quirk *list)

    look up a PCI SSID quirk list

    :param u16 vendor:
        PCI SSV id

    :param u16 device:
        PCI SSD id

    :param const struct snd_pci_quirk \*list:
        quirk list, terminated by a null entry



.. _`snd_pci_quirk_lookup_id.description`:

Description
-----------

Look through the given quirk list and finds a matching entry
with the same PCI SSID.  When subdevice is 0, all subdevice
values may match.

Returns the matched entry pointer, or NULL if nothing matched.



.. _`snd_pci_quirk_lookup`:

snd_pci_quirk_lookup
====================

.. c:function:: const struct snd_pci_quirk *snd_pci_quirk_lookup (struct pci_dev *pci, const struct snd_pci_quirk *list)

    look up a PCI SSID quirk list

    :param struct pci_dev \*pci:
        pci_dev handle

    :param const struct snd_pci_quirk \*list:
        quirk list, terminated by a null entry



.. _`snd_pci_quirk_lookup.description`:

Description
-----------

Look through the given quirk list and finds a matching entry
with the same PCI SSID.  When subdevice is 0, all subdevice
values may match.

Returns the matched entry pointer, or NULL if nothing matched.

