.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/host/xhci-ext-caps.h

.. _`xhci_find_next_ext_cap`:

xhci_find_next_ext_cap
======================

.. c:function:: int xhci_find_next_ext_cap(void __iomem *base, u32 start, int id)

    :param base:
        *undescribed*
    :type base: void __iomem \*

    :param start:
        *undescribed*
    :type start: u32

    :param id:
        *undescribed*
    :type id: int

.. _`xhci_find_next_ext_cap.description`:

Description
-----------

\ ``base``\         PCI MMIO registers base address.
\ ``start``\        address at which to start looking, (0 or HCC_PARAMS to start at
beginning of list)
\ ``id``\           Extended capability ID to search for, or 0 for the next
capability

Returns the offset of the next matching extended capability structure.
Some capabilities can occur several times, e.g., the XHCI_EXT_CAPS_PROTOCOL,
and this provides a way to find them all.

.. This file was automatic generated / don't edit.

