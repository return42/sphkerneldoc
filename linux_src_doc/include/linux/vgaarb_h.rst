.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/vgaarb.h

.. _`vga_set_legacy_decoding`:

vga_set_legacy_decoding
=======================

.. c:function:: void vga_set_legacy_decoding(struct pci_dev *pdev, unsigned int decodes)

    :param struct pci_dev \*pdev:
        pci device of the VGA card

    :param unsigned int decodes:
        bit mask of what legacy regions the card decodes

.. _`vga_set_legacy_decoding.description`:

Description
-----------

    Indicates to the arbiter if the card decodes legacy VGA IOs,
    legacy VGA Memory, both, or none. All cards default to both,
    the card driver (fbdev for example) should tell the arbiter
    if it has disabled legacy decoding, so the card can be left
    out of the arbitration process (and can be safe to take
    interrupts at any time.

.. _`vga_get_interruptible`:

vga_get_interruptible
=====================

.. c:function:: int vga_get_interruptible(struct pci_dev *pdev, unsigned int rsrc)

    :param struct pci_dev \*pdev:
        pci device of the VGA card or NULL for the system default

    :param unsigned int rsrc:
        bit mask of resources to acquire and lock

.. _`vga_get_interruptible.description`:

Description
-----------

Shortcut to vga_get with interruptible set to true.

On success, release the VGA resource again with \ :c:func:`vga_put`\ .

.. _`vga_get_uninterruptible`:

vga_get_uninterruptible
=======================

.. c:function:: int vga_get_uninterruptible(struct pci_dev *pdev, unsigned int rsrc)

    shortcut to \ :c:func:`vga_get`\ 

    :param struct pci_dev \*pdev:
        pci device of the VGA card or NULL for the system default

    :param unsigned int rsrc:
        bit mask of resources to acquire and lock

.. _`vga_get_uninterruptible.description`:

Description
-----------

Shortcut to vga_get with interruptible set to false.

On success, release the VGA resource again with \ :c:func:`vga_put`\ .

.. This file was automatic generated / don't edit.

