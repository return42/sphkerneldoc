.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/neterion/vxge/vxge-config.c

.. _`vxge_hw_device_hw_info_get`:

vxge_hw_device_hw_info_get
==========================

.. c:function:: enum vxge_hw_status vxge_hw_device_hw_info_get(void __iomem *bar0, struct vxge_hw_device_hw_info *hw_info)

    Get the hw information Returns the vpath mask that has the bits set for each vpath allocated for the driver, FW version information, and the first mac address for each vpath

    :param bar0:
        *undescribed*
    :type bar0: void __iomem \*

    :param hw_info:
        *undescribed*
    :type hw_info: struct vxge_hw_device_hw_info \*

.. _`vxge_hw_device_flick_link_led`:

vxge_hw_device_flick_link_led
=============================

.. c:function:: enum vxge_hw_status vxge_hw_device_flick_link_led(struct __vxge_hw_device *hldev, u64 on_off)

    Flick (blink) link LED.

    :param hldev:
        HW device.
    :type hldev: struct __vxge_hw_device \*

    :param on_off:
        TRUE if flickering to be on, FALSE to be off
    :type on_off: u64

.. _`vxge_hw_device_flick_link_led.description`:

Description
-----------

Flicker the link LED.

.. _`vxge_hw_vpath_check_leak`:

vxge_hw_vpath_check_leak
========================

.. c:function:: enum vxge_hw_status vxge_hw_vpath_check_leak(struct __vxge_hw_ring *ring)

    Check for memory leak

    :param ring:
        *undescribed*
    :type ring: struct __vxge_hw_ring \*

.. _`vxge_hw_vpath_check_leak.description`:

Description
-----------

If PRC_RXD_DOORBELL_VPn.NEW_QW_CNT is larger or equal to
PRC_CFG6_VPn.RXD_SPAT then a leak has occurred.

.. _`vxge_hw_vpath_check_leak.return`:

Return
------

VXGE_HW_FAIL, if leak has occurred.

.. _`vxge_hw_vpath_rx_doorbell_init`:

vxge_hw_vpath_rx_doorbell_init
==============================

.. c:function:: void vxge_hw_vpath_rx_doorbell_init(struct __vxge_hw_vpath_handle *vp)

    Close the handle got from previous vpath (vpath) open

    :param vp:
        Handle got from previous vpath open
    :type vp: struct __vxge_hw_vpath_handle \*

.. _`vxge_hw_vpath_rx_doorbell_init.description`:

Description
-----------

This function is used to close access to virtual path opened
earlier.

.. This file was automatic generated / don't edit.

