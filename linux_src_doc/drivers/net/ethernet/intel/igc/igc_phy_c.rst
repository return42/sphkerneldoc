.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igc/igc_phy.c

.. _`igc_check_reset_block`:

igc_check_reset_block
=====================

.. c:function:: s32 igc_check_reset_block(struct igc_hw *hw)

    Check if PHY reset is blocked

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_check_reset_block.description`:

Description
-----------

Read the PHY management control register and check whether a PHY reset
is blocked.  If a reset is not blocked return 0, otherwise
return IGC_ERR_BLK_PHY_RESET (12).

.. _`igc_get_phy_id`:

igc_get_phy_id
==============

.. c:function:: s32 igc_get_phy_id(struct igc_hw *hw)

    Retrieve the PHY ID and revision

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_get_phy_id.description`:

Description
-----------

Reads the PHY registers and stores the PHY ID and possibly the PHY
revision in the hardware structure.

.. _`igc_phy_has_link`:

igc_phy_has_link
================

.. c:function:: s32 igc_phy_has_link(struct igc_hw *hw, u32 iterations, u32 usec_interval, bool *success)

    Polls PHY for link

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param iterations:
        number of times to poll for link
    :type iterations: u32

    :param usec_interval:
        delay between polling attempts
    :type usec_interval: u32

    :param success:
        pointer to whether polling was successful or not
    :type success: bool \*

.. _`igc_phy_has_link.description`:

Description
-----------

Polls the PHY status register for link, 'iterations' number of times.

.. _`igc_power_up_phy_copper`:

igc_power_up_phy_copper
=======================

.. c:function:: void igc_power_up_phy_copper(struct igc_hw *hw)

    Restore copper link in case of PHY power down

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_power_up_phy_copper.description`:

Description
-----------

In the case of a PHY power down to save power, or to turn off link during a
driver unload, restore the link to previous settings.

.. _`igc_power_down_phy_copper`:

igc_power_down_phy_copper
=========================

.. c:function:: void igc_power_down_phy_copper(struct igc_hw *hw)

    Power down copper PHY

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_power_down_phy_copper.description`:

Description
-----------

Power down PHY to save power when interface is down and wake on lan
is not enabled.

.. _`igc_check_downshift`:

igc_check_downshift
===================

.. c:function:: s32 igc_check_downshift(struct igc_hw *hw)

    Checks whether a downshift in speed occurred

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_check_downshift.description`:

Description
-----------

Success returns 0, Failure returns 1

A downshift is detected by querying the PHY link health.

.. _`igc_phy_hw_reset`:

igc_phy_hw_reset
================

.. c:function:: s32 igc_phy_hw_reset(struct igc_hw *hw)

    PHY hardware reset

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_phy_hw_reset.description`:

Description
-----------

Verify the reset block is not blocking us from resetting.  Acquire
semaphore (if necessary) and read/set/write the device control reset
bit in the PHY.  Wait the appropriate delay time for the device to
reset and release the semaphore (if necessary).

.. _`igc_copper_link_autoneg`:

igc_copper_link_autoneg
=======================

.. c:function:: s32 igc_copper_link_autoneg(struct igc_hw *hw)

    Setup/Enable autoneg for copper link

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_copper_link_autoneg.description`:

Description
-----------

Performs initial bounds checking on autoneg advertisement parameter, then
configure to advertise the full capability.  Setup the PHY to autoneg
and restart the negotiation process between the link partner.  If
autoneg_wait_to_complete, then wait for autoneg to complete before exiting.

.. _`igc_wait_autoneg`:

igc_wait_autoneg
================

.. c:function:: s32 igc_wait_autoneg(struct igc_hw *hw)

    Wait for auto-neg completion

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_wait_autoneg.description`:

Description
-----------

Waits for auto-negotiation to complete or for the auto-negotiation time
limit to expire, which ever happens first.

.. _`igc_phy_setup_autoneg`:

igc_phy_setup_autoneg
=====================

.. c:function:: s32 igc_phy_setup_autoneg(struct igc_hw *hw)

    Configure PHY for auto-negotiation

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_phy_setup_autoneg.description`:

Description
-----------

Reads the MII auto-neg advertisement register and/or the 1000T control
register and if the PHY is already setup for auto-negotiation, then
return successful.  Otherwise, setup advertisement and flow control to
the appropriate values for the wanted auto-negotiation.

.. _`igc_setup_copper_link`:

igc_setup_copper_link
=====================

.. c:function:: s32 igc_setup_copper_link(struct igc_hw *hw)

    Configure copper link settings

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_setup_copper_link.description`:

Description
-----------

Calls the appropriate function to configure the link for auto-neg or forced
speed and duplex.  Then we check for link, once link is established calls
to configure collision distance and flow control are called.  If link is
not established, we return -IGC_ERR_PHY (-2).

.. _`igc_read_phy_reg_mdic`:

igc_read_phy_reg_mdic
=====================

.. c:function:: s32 igc_read_phy_reg_mdic(struct igc_hw *hw, u32 offset, u16 *data)

    Read MDI control register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param offset:
        register offset to be read
    :type offset: u32

    :param data:
        pointer to the read data
    :type data: u16 \*

.. _`igc_read_phy_reg_mdic.description`:

Description
-----------

Reads the MDI control register in the PHY at offset and stores the
information read to data.

.. _`igc_write_phy_reg_mdic`:

igc_write_phy_reg_mdic
======================

.. c:function:: s32 igc_write_phy_reg_mdic(struct igc_hw *hw, u32 offset, u16 data)

    Write MDI control register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param offset:
        register offset to write to
    :type offset: u32

    :param data:
        data to write to register at offset
    :type data: u16

.. _`igc_write_phy_reg_mdic.description`:

Description
-----------

Writes data to MDI control register in the PHY at offset.

.. _`__igc_access_xmdio_reg`:

\__igc_access_xmdio_reg
=======================

.. c:function:: s32 __igc_access_xmdio_reg(struct igc_hw *hw, u16 address, u8 dev_addr, u16 *data, bool read)

    Read/write XMDIO register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param address:
        XMDIO address to program
    :type address: u16

    :param dev_addr:
        device address to program
    :type dev_addr: u8

    :param data:
        pointer to value to read/write from/to the XMDIO address
    :type data: u16 \*

    :param read:
        boolean flag to indicate read or write
    :type read: bool

.. _`igc_read_xmdio_reg`:

igc_read_xmdio_reg
==================

.. c:function:: s32 igc_read_xmdio_reg(struct igc_hw *hw, u16 addr, u8 dev_addr, u16 *data)

    Read XMDIO register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param addr:
        XMDIO address to program
    :type addr: u16

    :param dev_addr:
        device address to program
    :type dev_addr: u8

    :param data:
        value to be read from the EMI address
    :type data: u16 \*

.. _`igc_write_xmdio_reg`:

igc_write_xmdio_reg
===================

.. c:function:: s32 igc_write_xmdio_reg(struct igc_hw *hw, u16 addr, u8 dev_addr, u16 data)

    Write XMDIO register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param addr:
        XMDIO address to program
    :type addr: u16

    :param dev_addr:
        device address to program
    :type dev_addr: u8

    :param data:
        value to be written to the XMDIO address
    :type data: u16

.. _`igc_write_phy_reg_gpy`:

igc_write_phy_reg_gpy
=====================

.. c:function:: s32 igc_write_phy_reg_gpy(struct igc_hw *hw, u32 offset, u16 data)

    Write GPY PHY register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param offset:
        register offset to write to
    :type offset: u32

    :param data:
        data to write at register offset
    :type data: u16

.. _`igc_write_phy_reg_gpy.description`:

Description
-----------

Acquires semaphore, if necessary, then writes the data to PHY register
at the offset. Release any acquired semaphores before exiting.

.. _`igc_read_phy_reg_gpy`:

igc_read_phy_reg_gpy
====================

.. c:function:: s32 igc_read_phy_reg_gpy(struct igc_hw *hw, u32 offset, u16 *data)

    Read GPY PHY register

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param offset:
        lower half is register offset to read to
        upper half is MMD to use.
    :type offset: u32

    :param data:
        data to read at register offset
    :type data: u16 \*

.. _`igc_read_phy_reg_gpy.description`:

Description
-----------

Acquires semaphore, if necessary, then reads the data in the PHY register
at the offset. Release any acquired semaphores before exiting.

.. This file was automatic generated / don't edit.

