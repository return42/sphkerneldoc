.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/chipidea/core.c

.. _`hw_read_intr_enable`:

hw_read_intr_enable
===================

.. c:function:: u32 hw_read_intr_enable(struct ci_hdrc *ci)

    returns interrupt enable register

    :param struct ci_hdrc \*ci:
        the controller

.. _`hw_read_intr_enable.description`:

Description
-----------

This function returns register data

.. _`hw_read_intr_status`:

hw_read_intr_status
===================

.. c:function:: u32 hw_read_intr_status(struct ci_hdrc *ci)

    returns interrupt status register

    :param struct ci_hdrc \*ci:
        the controller

.. _`hw_read_intr_status.description`:

Description
-----------

This function returns register data

.. _`hw_port_test_set`:

hw_port_test_set
================

.. c:function:: int hw_port_test_set(struct ci_hdrc *ci, u8 mode)

    writes port test mode (execute without interruption)

    :param struct ci_hdrc \*ci:
        *undescribed*

    :param u8 mode:
        new value

.. _`hw_port_test_set.description`:

Description
-----------

This function returns an error code

.. _`hw_port_test_get`:

hw_port_test_get
================

.. c:function:: u8 hw_port_test_get(struct ci_hdrc *ci)

    reads port test mode value

    :param struct ci_hdrc \*ci:
        the controller

.. _`hw_port_test_get.description`:

Description
-----------

This function returns port test mode value

.. _`_ci_usb_phy_init`:

_ci_usb_phy_init
================

.. c:function:: int _ci_usb_phy_init(struct ci_hdrc *ci)

    initialize phy taking in account both phy and usb_phy interfaces

    :param struct ci_hdrc \*ci:
        the controller

.. _`_ci_usb_phy_init.description`:

Description
-----------

This function returns an error code if the phy failed to init

.. _`ci_usb_phy_exit`:

ci_usb_phy_exit
===============

.. c:function:: void ci_usb_phy_exit(struct ci_hdrc *ci)

    deinitialize phy taking in account both phy and usb_phy interfaces

    :param struct ci_hdrc \*ci:
        the controller

.. _`ci_usb_phy_init`:

ci_usb_phy_init
===============

.. c:function:: int ci_usb_phy_init(struct ci_hdrc *ci)

    initialize phy according to different phy type

    :param struct ci_hdrc \*ci:
        the controller

.. _`ci_usb_phy_init.description`:

Description
-----------

This function returns an error code if usb_phy_init has failed

.. _`ci_platform_configure`:

ci_platform_configure
=====================

.. c:function:: void ci_platform_configure(struct ci_hdrc *ci)

    do controller configure

    :param struct ci_hdrc \*ci:
        the controller

.. _`hw_controller_reset`:

hw_controller_reset
===================

.. c:function:: int hw_controller_reset(struct ci_hdrc *ci)

    do controller reset

    :param struct ci_hdrc \*ci:
        the controller

.. _`hw_controller_reset.description`:

Description
-----------

This function returns an error code

.. _`hw_device_reset`:

hw_device_reset
===============

.. c:function:: int hw_device_reset(struct ci_hdrc *ci)

    resets chip (execute without interruption)

    :param struct ci_hdrc \*ci:
        the controller

.. _`hw_device_reset.description`:

Description
-----------

This function returns an error code

.. _`hw_wait_reg`:

hw_wait_reg
===========

.. c:function:: int hw_wait_reg(struct ci_hdrc *ci, enum ci_hw_regs reg, u32 mask, u32 value, unsigned int timeout_ms)

    wait the register value

    :param struct ci_hdrc \*ci:
        the controller

    :param enum ci_hw_regs reg:
        register index

    :param u32 mask:
        mast bit

    :param u32 value:
        the bit value to wait

    :param unsigned int timeout_ms:
        timeout in millisecond

.. _`hw_wait_reg.description`:

Description
-----------

Sometimes, it needs to wait register value before going on.
Eg, when switch to device mode, the vbus value should be lower
than OTGSC_BSV before connects to host.

This function returns an error code if timeout

.. This file was automatic generated / don't edit.

