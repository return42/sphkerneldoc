.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/phy/ti/phy-omap-usb2.c

.. _`omap_usb2_set_comparator`:

omap_usb2_set_comparator
========================

.. c:function:: int omap_usb2_set_comparator(struct phy_companion *comparator)

    links the comparator present in the sytem with this phy \ ``comparator``\  - the companion phy(comparator) for this phy

    :param comparator:
        *undescribed*
    :type comparator: struct phy_companion \*

.. _`omap_usb2_set_comparator.description`:

Description
-----------

The phy companion driver should call this API passing the phy_companion
filled with set_vbus and start_srp to be used by usb phy.

For use by phy companion driver

.. This file was automatic generated / don't edit.

