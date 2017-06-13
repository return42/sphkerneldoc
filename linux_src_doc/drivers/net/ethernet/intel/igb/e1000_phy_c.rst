.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igb/e1000_phy.c

.. _`igb_check_reset_block`:

igb_check_reset_block
=====================

.. c:function:: s32 igb_check_reset_block(struct e1000_hw *hw)

    Check if PHY reset is blocked

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_check_reset_block.description`:

Description
-----------

Read the PHY management control register and check whether a PHY reset
is blocked.  If a reset is not blocked return 0, otherwise
return E1000_BLK_PHY_RESET (12).

.. _`igb_get_phy_id`:

igb_get_phy_id
==============

.. c:function:: s32 igb_get_phy_id(struct e1000_hw *hw)

    Retrieve the PHY ID and revision

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_get_phy_id.description`:

Description
-----------

Reads the PHY registers and stores the PHY ID and possibly the PHY
revision in the hardware structure.

.. _`igb_phy_reset_dsp`:

igb_phy_reset_dsp
=================

.. c:function:: s32 igb_phy_reset_dsp(struct e1000_hw *hw)

    Reset PHY DSP

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_phy_reset_dsp.description`:

Description
-----------

Reset the digital signal processor.

.. _`igb_read_phy_reg_mdic`:

igb_read_phy_reg_mdic
=====================

.. c:function:: s32 igb_read_phy_reg_mdic(struct e1000_hw *hw, u32 offset, u16 *data)

    Read MDI control register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`igb_read_phy_reg_mdic.description`:

Description
-----------

Reads the MDI control register in the PHY at offset and stores the
information read to data.

.. _`igb_write_phy_reg_mdic`:

igb_write_phy_reg_mdic
======================

.. c:function:: s32 igb_write_phy_reg_mdic(struct e1000_hw *hw, u32 offset, u16 data)

    Write MDI control register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write to register at offset

.. _`igb_write_phy_reg_mdic.description`:

Description
-----------

Writes data to MDI control register in the PHY at offset.

.. _`igb_read_phy_reg_i2c`:

igb_read_phy_reg_i2c
====================

.. c:function:: s32 igb_read_phy_reg_i2c(struct e1000_hw *hw, u32 offset, u16 *data)

    Read PHY register using i2c

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`igb_read_phy_reg_i2c.description`:

Description
-----------

Reads the PHY register at offset using the i2c interface and stores the
retrieved information in data.

.. _`igb_write_phy_reg_i2c`:

igb_write_phy_reg_i2c
=====================

.. c:function:: s32 igb_write_phy_reg_i2c(struct e1000_hw *hw, u32 offset, u16 data)

    Write PHY register using i2c

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`igb_write_phy_reg_i2c.description`:

Description
-----------

Writes the data to PHY register at the offset using the i2c interface.

.. _`igb_read_sfp_data_byte`:

igb_read_sfp_data_byte
======================

.. c:function:: s32 igb_read_sfp_data_byte(struct e1000_hw *hw, u16 offset, u8 *data)

    Reads SFP module data.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 offset:
        byte location offset to be read

    :param u8 \*data:
        read data buffer pointer

.. _`igb_read_sfp_data_byte.description`:

Description
-----------

Reads one byte from SFP module data stored
in SFP resided EEPROM memory or SFP diagnostic area.
Function should be called with
E1000_I2CCMD_SFP_DATA_ADDR(<byte offset>) for SFP module database access
E1000_I2CCMD_SFP_DIAG_ADDR(<byte offset>) for SFP diagnostics parameters
access

.. _`igb_read_phy_reg_igp`:

igb_read_phy_reg_igp
====================

.. c:function:: s32 igb_read_phy_reg_igp(struct e1000_hw *hw, u32 offset, u16 *data)

    Read igp PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`igb_read_phy_reg_igp.description`:

Description
-----------

Acquires semaphore, if necessary, then reads the PHY register at offset
and storing the retrieved information in data.  Release any acquired
semaphores before exiting.

.. _`igb_write_phy_reg_igp`:

igb_write_phy_reg_igp
=====================

.. c:function:: s32 igb_write_phy_reg_igp(struct e1000_hw *hw, u32 offset, u16 data)

    Write igp PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`igb_write_phy_reg_igp.description`:

Description
-----------

Acquires semaphore, if necessary, then writes the data to PHY register
at the offset.  Release any acquired semaphores before exiting.

.. _`igb_copper_link_setup_82580`:

igb_copper_link_setup_82580
===========================

.. c:function:: s32 igb_copper_link_setup_82580(struct e1000_hw *hw)

    Setup 82580 PHY for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_copper_link_setup_82580.description`:

Description
-----------

Sets up Carrier-sense on Transmit and downshift values.

.. _`igb_copper_link_setup_m88`:

igb_copper_link_setup_m88
=========================

.. c:function:: s32 igb_copper_link_setup_m88(struct e1000_hw *hw)

    Setup m88 PHY's for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_copper_link_setup_m88.description`:

Description
-----------

Sets up MDI/MDI-X and polarity for m88 PHY's.  If necessary, transmit clock
and downshift values are set also.

.. _`igb_copper_link_setup_m88_gen2`:

igb_copper_link_setup_m88_gen2
==============================

.. c:function:: s32 igb_copper_link_setup_m88_gen2(struct e1000_hw *hw)

    Setup m88 PHY's for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_copper_link_setup_m88_gen2.description`:

Description
-----------

Sets up MDI/MDI-X and polarity for i347-AT4, m88e1322 and m88e1112 PHY's.
Also enables and sets the downshift parameters.

.. _`igb_copper_link_setup_igp`:

igb_copper_link_setup_igp
=========================

.. c:function:: s32 igb_copper_link_setup_igp(struct e1000_hw *hw)

    Setup igp PHY's for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_copper_link_setup_igp.description`:

Description
-----------

Sets up LPLU, MDI/MDI-X, polarity, Smartspeed and Master/Slave config for
igp PHY's.

.. _`igb_copper_link_autoneg`:

igb_copper_link_autoneg
=======================

.. c:function:: s32 igb_copper_link_autoneg(struct e1000_hw *hw)

    Setup/Enable autoneg for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_copper_link_autoneg.description`:

Description
-----------

Performs initial bounds checking on autoneg advertisement parameter, then
configure to advertise the full capability.  Setup the PHY to autoneg
and restart the negotiation process between the link partner.  If
autoneg_wait_to_complete, then wait for autoneg to complete before exiting.

.. _`igb_phy_setup_autoneg`:

igb_phy_setup_autoneg
=====================

.. c:function:: s32 igb_phy_setup_autoneg(struct e1000_hw *hw)

    Configure PHY for auto-negotiation

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_phy_setup_autoneg.description`:

Description
-----------

Reads the MII auto-neg advertisement register and/or the 1000T control
register and if the PHY is already setup for auto-negotiation, then
return successful.  Otherwise, setup advertisement and flow control to
the appropriate values for the wanted auto-negotiation.

.. _`igb_setup_copper_link`:

igb_setup_copper_link
=====================

.. c:function:: s32 igb_setup_copper_link(struct e1000_hw *hw)

    Configure copper link settings

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_setup_copper_link.description`:

Description
-----------

Calls the appropriate function to configure the link for auto-neg or forced
speed and duplex.  Then we check for link, once link is established calls
to configure collision distance and flow control are called.  If link is
not established, we return -E1000_ERR_PHY (-2).

.. _`igb_phy_force_speed_duplex_igp`:

igb_phy_force_speed_duplex_igp
==============================

.. c:function:: s32 igb_phy_force_speed_duplex_igp(struct e1000_hw *hw)

    Force speed/duplex for igp PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_phy_force_speed_duplex_igp.description`:

Description
-----------

Calls the PHY setup function to force speed and duplex.  Clears the
auto-crossover to force MDI manually.  Waits for link and returns
successful if link up is successful, else -E1000_ERR_PHY (-2).

.. _`igb_phy_force_speed_duplex_m88`:

igb_phy_force_speed_duplex_m88
==============================

.. c:function:: s32 igb_phy_force_speed_duplex_m88(struct e1000_hw *hw)

    Force speed/duplex for m88 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_phy_force_speed_duplex_m88.description`:

Description
-----------

Calls the PHY setup function to force speed and duplex.  Clears the
auto-crossover to force MDI manually.  Resets the PHY to commit the
changes.  If time expires while waiting for link up, we reset the DSP.
After reset, TX_CLK and CRS on TX must be set.  Return successful upon
successful completion, else return corresponding error code.

.. _`igb_phy_force_speed_duplex_setup`:

igb_phy_force_speed_duplex_setup
================================

.. c:function:: void igb_phy_force_speed_duplex_setup(struct e1000_hw *hw, u16 *phy_ctrl)

    Configure forced PHY speed/duplex

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 \*phy_ctrl:
        pointer to current value of PHY_CONTROL

.. _`igb_phy_force_speed_duplex_setup.forces-speed-and-duplex-on-the-phy-by-doing-the-following`:

Forces speed and duplex on the PHY by doing the following
---------------------------------------------------------

disable flow
control, force speed/duplex on the MAC, disable auto speed detection,
disable auto-negotiation, configure duplex, configure speed, configure
the collision distance, write configuration to CTRL register.  The
caller must write to the PHY_CONTROL register for these settings to
take affect.

.. _`igb_set_d3_lplu_state`:

igb_set_d3_lplu_state
=====================

.. c:function:: s32 igb_set_d3_lplu_state(struct e1000_hw *hw, bool active)

    Sets low power link up state for D3

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param bool active:
        boolean used to enable/disable lplu

.. _`igb_set_d3_lplu_state.description`:

Description
-----------

Success returns 0, Failure returns 1

The low power link up (lplu) state is set to the power management level D3
and SmartSpeed is disabled when active is true, else clear lplu for D3
and enable Smartspeed.  LPLU and Smartspeed are mutually exclusive.  LPLU
is used during Dx states where the power conservation is most important.
During driver activity, SmartSpeed should be enabled so performance is
maintained.

.. _`igb_check_downshift`:

igb_check_downshift
===================

.. c:function:: s32 igb_check_downshift(struct e1000_hw *hw)

    Checks whether a downshift in speed occurred

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_check_downshift.description`:

Description
-----------

Success returns 0, Failure returns 1

A downshift is detected by querying the PHY link health.

.. _`igb_check_polarity_m88`:

igb_check_polarity_m88
======================

.. c:function:: s32 igb_check_polarity_m88(struct e1000_hw *hw)

    Checks the polarity.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_check_polarity_m88.description`:

Description
-----------

Success returns 0, Failure returns -E1000_ERR_PHY (-2)

Polarity is determined based on the PHY specific status register.

.. _`igb_check_polarity_igp`:

igb_check_polarity_igp
======================

.. c:function:: s32 igb_check_polarity_igp(struct e1000_hw *hw)

    Checks the polarity.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_check_polarity_igp.description`:

Description
-----------

Success returns 0, Failure returns -E1000_ERR_PHY (-2)

Polarity is determined based on the PHY port status register, and the
current speed (since there is no polarity at 100Mbps).

.. _`igb_wait_autoneg`:

igb_wait_autoneg
================

.. c:function:: s32 igb_wait_autoneg(struct e1000_hw *hw)

    Wait for auto-neg completion

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_wait_autoneg.description`:

Description
-----------

Waits for auto-negotiation to complete or for the auto-negotiation time
limit to expire, which ever happens first.

.. _`igb_phy_has_link`:

igb_phy_has_link
================

.. c:function:: s32 igb_phy_has_link(struct e1000_hw *hw, u32 iterations, u32 usec_interval, bool *success)

    Polls PHY for link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 iterations:
        number of times to poll for link

    :param u32 usec_interval:
        delay between polling attempts

    :param bool \*success:
        pointer to whether polling was successful or not

.. _`igb_phy_has_link.description`:

Description
-----------

Polls the PHY status register for link, 'iterations' number of times.

.. _`igb_get_cable_length_m88`:

igb_get_cable_length_m88
========================

.. c:function:: s32 igb_get_cable_length_m88(struct e1000_hw *hw)

    Determine cable length for m88 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_get_cable_length_m88.description`:

Description
-----------

Reads the PHY specific status register to retrieve the cable length
information.  The cable length is determined by averaging the minimum and
maximum values to get the "average" cable length.  The m88 PHY has four
possible cable length values, which are:
Register Value          Cable Length
0                       < 50 meters
1                       50 - 80 meters
2                       80 - 110 meters
3                       110 - 140 meters
4                       > 140 meters

.. _`igb_get_cable_length_igp_2`:

igb_get_cable_length_igp_2
==========================

.. c:function:: s32 igb_get_cable_length_igp_2(struct e1000_hw *hw)

    Determine cable length for igp2 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_get_cable_length_igp_2.description`:

Description
-----------

The automatic gain control (agc) normalizes the amplitude of the
received signal, adjusting for the attenuation produced by the
cable.  By reading the AGC registers, which represent the
combination of coarse and fine gain value, the value can be put
into a lookup table to obtain the approximate cable length
for each channel.

.. _`igb_get_phy_info_m88`:

igb_get_phy_info_m88
====================

.. c:function:: s32 igb_get_phy_info_m88(struct e1000_hw *hw)

    Retrieve PHY information

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_get_phy_info_m88.description`:

Description
-----------

Valid for only copper links.  Read the PHY status register (sticky read)
to verify that link is up.  Read the PHY special control register to
determine the polarity and 10base-T extended distance.  Read the PHY
special status register to determine MDI/MDIx and current speed.  If
speed is 1000, then determine cable length, local and remote receiver.

.. _`igb_get_phy_info_igp`:

igb_get_phy_info_igp
====================

.. c:function:: s32 igb_get_phy_info_igp(struct e1000_hw *hw)

    Retrieve igp PHY information

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_get_phy_info_igp.description`:

Description
-----------

Read PHY status to determine if link is up.  If link is up, then
set/determine 10base-T extended distance and polarity correction.  Read
PHY port status to determine MDI/MDIx and speed.  Based on the speed,
determine on the cable length, local and remote receiver.

.. _`igb_phy_sw_reset`:

igb_phy_sw_reset
================

.. c:function:: s32 igb_phy_sw_reset(struct e1000_hw *hw)

    PHY software reset

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_phy_sw_reset.description`:

Description
-----------

Does a software reset of the PHY by reading the PHY control register and
setting/write the control register reset bit to the PHY.

.. _`igb_phy_hw_reset`:

igb_phy_hw_reset
================

.. c:function:: s32 igb_phy_hw_reset(struct e1000_hw *hw)

    PHY hardware reset

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_phy_hw_reset.description`:

Description
-----------

Verify the reset block is not blocking us from resetting.  Acquire
semaphore (if necessary) and read/set/write the device control reset
bit in the PHY.  Wait the appropriate delay time for the device to
reset and release the semaphore (if necessary).

.. _`igb_phy_init_script_igp3`:

igb_phy_init_script_igp3
========================

.. c:function:: s32 igb_phy_init_script_igp3(struct e1000_hw *hw)

    Inits the IGP3 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_phy_init_script_igp3.description`:

Description
-----------

Initializes a Intel Gigabit PHY3 when an EEPROM is not present.

.. _`igb_initialize_m88e1512_phy`:

igb_initialize_M88E1512_phy
===========================

.. c:function:: s32 igb_initialize_M88E1512_phy(struct e1000_hw *hw)

    Initialize M88E1512 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_initialize_m88e1512_phy.description`:

Description
-----------

Initialize Marvel 1512 to work correctly with Avoton.

.. _`igb_initialize_m88e1543_phy`:

igb_initialize_M88E1543_phy
===========================

.. c:function:: s32 igb_initialize_M88E1543_phy(struct e1000_hw *hw)

    Initialize M88E1512 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_initialize_m88e1543_phy.description`:

Description
-----------

Initialize Marvell 1543 to work correctly with Avoton.

.. _`igb_power_up_phy_copper`:

igb_power_up_phy_copper
=======================

.. c:function:: void igb_power_up_phy_copper(struct e1000_hw *hw)

    Restore copper link in case of PHY power down

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_power_up_phy_copper.description`:

Description
-----------

In the case of a PHY power down to save power, or to turn off link during a
driver unload, restore the link to previous settings.

.. _`igb_power_down_phy_copper`:

igb_power_down_phy_copper
=========================

.. c:function:: void igb_power_down_phy_copper(struct e1000_hw *hw)

    Power down copper PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_power_down_phy_copper.description`:

Description
-----------

Power down PHY to save power when interface is down and wake on lan
is not enabled.

.. _`igb_check_polarity_82580`:

igb_check_polarity_82580
========================

.. c:function:: s32 igb_check_polarity_82580(struct e1000_hw *hw)

    Checks the polarity.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_check_polarity_82580.description`:

Description
-----------

Success returns 0, Failure returns -E1000_ERR_PHY (-2)

Polarity is determined based on the PHY specific status register.

.. _`igb_phy_force_speed_duplex_82580`:

igb_phy_force_speed_duplex_82580
================================

.. c:function:: s32 igb_phy_force_speed_duplex_82580(struct e1000_hw *hw)

    Force speed/duplex for I82580 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_phy_force_speed_duplex_82580.description`:

Description
-----------

Calls the PHY setup function to force speed and duplex.  Clears the
auto-crossover to force MDI manually.  Waits for link and returns
successful if link up is successful, else -E1000_ERR_PHY (-2).

.. _`igb_get_phy_info_82580`:

igb_get_phy_info_82580
======================

.. c:function:: s32 igb_get_phy_info_82580(struct e1000_hw *hw)

    Retrieve I82580 PHY information

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_get_phy_info_82580.description`:

Description
-----------

Read PHY status to determine if link is up.  If link is up, then
set/determine 10base-T extended distance and polarity correction.  Read
PHY port status to determine MDI/MDIx and speed.  Based on the speed,
determine on the cable length, local and remote receiver.

.. _`igb_get_cable_length_82580`:

igb_get_cable_length_82580
==========================

.. c:function:: s32 igb_get_cable_length_82580(struct e1000_hw *hw)

    Determine cable length for 82580 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_get_cable_length_82580.description`:

Description
-----------

Reads the diagnostic status register and verifies result is valid before
placing it in the phy_cable_length field.

.. _`igb_set_master_slave_mode`:

igb_set_master_slave_mode
=========================

.. c:function:: s32 igb_set_master_slave_mode(struct e1000_hw *hw)

    Setup PHY for Master/slave mode

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`igb_set_master_slave_mode.description`:

Description
-----------

Sets up Master/slave mode

.. This file was automatic generated / don't edit.

