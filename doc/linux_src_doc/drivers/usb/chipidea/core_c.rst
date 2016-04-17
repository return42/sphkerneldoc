.. -*- coding: utf-8; mode: rst -*-

======
core.c
======


.. _`hw_read_intr_enable`:

hw_read_intr_enable
===================

.. c:function:: u32 hw_read_intr_enable (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`hw_read_intr_enable.description`:

Description
-----------

This function returns register data



.. _`hw_read_intr_status`:

hw_read_intr_status
===================

.. c:function:: u32 hw_read_intr_status (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`hw_read_intr_status.description`:

Description
-----------

This function returns register data



.. _`hw_port_test_set`:

hw_port_test_set
================

.. c:function:: int hw_port_test_set (struct ci_hdrc *ci, u8 mode)

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

.. c:function:: u8 hw_port_test_get (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`hw_port_test_get.description`:

Description
-----------

This function returns port test mode value



.. _`_ci_usb_phy_init`:

_ci_usb_phy_init
================

.. c:function:: int _ci_usb_phy_init (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`_ci_usb_phy_init.description`:

Description
-----------

This function returns an error code if the phy failed to init



.. _`_ci_usb_phy_init.description`:

Description
-----------

This function returns an error code if the phy failed to init



.. _`ci_usb_phy_exit`:

ci_usb_phy_exit
===============

.. c:function:: void ci_usb_phy_exit (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`ci_usb_phy_exit.description`:

Description
-----------

interfaces



.. _`ci_usb_phy_init`:

ci_usb_phy_init
===============

.. c:function:: int ci_usb_phy_init (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`ci_usb_phy_init.description`:

Description
-----------

This function returns an error code if usb_phy_init has failed



.. _`ci_platform_configure`:

ci_platform_configure
=====================

.. c:function:: void ci_platform_configure (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`hw_controller_reset`:

hw_controller_reset
===================

.. c:function:: int hw_controller_reset (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`hw_controller_reset.description`:

Description
-----------

This function returns an error code



.. _`hw_device_reset`:

hw_device_reset
===============

.. c:function:: int hw_device_reset (struct ci_hdrc *ci)

    :param struct ci_hdrc \*ci:
        the controller



.. _`hw_device_reset.description`:

Description
-----------

This function returns an error code



.. _`hw_wait_reg`:

hw_wait_reg
===========

.. c:function:: int hw_wait_reg (struct ci_hdrc *ci, enum ci_hw_regs reg, u32 mask, u32 value, unsigned int timeout_ms)

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

This function returns an error code if timeout



.. _`hw_wait_reg.description`:

Description
-----------

This function returns an error code if timeout

