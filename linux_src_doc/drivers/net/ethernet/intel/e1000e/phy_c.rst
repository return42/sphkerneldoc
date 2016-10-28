.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000e/phy.c

.. _`e1000e_check_reset_block_generic`:

e1000e_check_reset_block_generic
================================

.. c:function:: s32 e1000e_check_reset_block_generic(struct e1000_hw *hw)

    Check if PHY reset is blocked

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_check_reset_block_generic.description`:

Description
-----------

Read the PHY management control register and check whether a PHY reset
is blocked.  If a reset is not blocked return 0, otherwise
return E1000_BLK_PHY_RESET (12).

.. _`e1000e_get_phy_id`:

e1000e_get_phy_id
=================

.. c:function:: s32 e1000e_get_phy_id(struct e1000_hw *hw)

    Retrieve the PHY ID and revision

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_get_phy_id.description`:

Description
-----------

Reads the PHY registers and stores the PHY ID and possibly the PHY
revision in the hardware structure.

.. _`e1000e_phy_reset_dsp`:

e1000e_phy_reset_dsp
====================

.. c:function:: s32 e1000e_phy_reset_dsp(struct e1000_hw *hw)

    Reset PHY DSP

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_phy_reset_dsp.description`:

Description
-----------

Reset the digital signal processor.

.. _`e1000e_read_phy_reg_mdic`:

e1000e_read_phy_reg_mdic
========================

.. c:function:: s32 e1000e_read_phy_reg_mdic(struct e1000_hw *hw, u32 offset, u16 *data)

    Read MDI control register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000e_read_phy_reg_mdic.description`:

Description
-----------

Reads the MDI control register in the PHY at offset and stores the
information read to data.

.. _`e1000e_write_phy_reg_mdic`:

e1000e_write_phy_reg_mdic
=========================

.. c:function:: s32 e1000e_write_phy_reg_mdic(struct e1000_hw *hw, u32 offset, u16 data)

    Write MDI control register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write to register at offset

.. _`e1000e_write_phy_reg_mdic.description`:

Description
-----------

Writes data to MDI control register in the PHY at offset.

.. _`e1000e_read_phy_reg_m88`:

e1000e_read_phy_reg_m88
=======================

.. c:function:: s32 e1000e_read_phy_reg_m88(struct e1000_hw *hw, u32 offset, u16 *data)

    Read m88 PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000e_read_phy_reg_m88.description`:

Description
-----------

Acquires semaphore, if necessary, then reads the PHY register at offset
and storing the retrieved information in data.  Release any acquired
semaphores before exiting.

.. _`e1000e_write_phy_reg_m88`:

e1000e_write_phy_reg_m88
========================

.. c:function:: s32 e1000e_write_phy_reg_m88(struct e1000_hw *hw, u32 offset, u16 data)

    Write m88 PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000e_write_phy_reg_m88.description`:

Description
-----------

Acquires semaphore, if necessary, then writes the data to PHY register
at the offset.  Release any acquired semaphores before exiting.

.. _`e1000_set_page_igp`:

e1000_set_page_igp
==================

.. c:function:: s32 e1000_set_page_igp(struct e1000_hw *hw, u16 page)

    Set page as on IGP-like PHY(s)

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 page:
        page to set (shifted left when necessary)

.. _`e1000_set_page_igp.description`:

Description
-----------

Sets PHY page required for PHY register access.  Assumes semaphore is
already acquired.  Note, this function sets phy.addr to 1 so the caller
must set it appropriately (if necessary) after this function returns.

.. _`__e1000e_read_phy_reg_igp`:

__e1000e_read_phy_reg_igp
=========================

.. c:function:: s32 __e1000e_read_phy_reg_igp(struct e1000_hw *hw, u32 offset, u16 *data, bool locked)

    Read igp PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

    :param bool locked:
        semaphore has already been acquired or not

.. _`__e1000e_read_phy_reg_igp.description`:

Description
-----------

Acquires semaphore, if necessary, then reads the PHY register at offset
and stores the retrieved information in data.  Release any acquired
semaphores before exiting.

.. _`e1000e_read_phy_reg_igp`:

e1000e_read_phy_reg_igp
=======================

.. c:function:: s32 e1000e_read_phy_reg_igp(struct e1000_hw *hw, u32 offset, u16 *data)

    Read igp PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000e_read_phy_reg_igp.description`:

Description
-----------

Acquires semaphore then reads the PHY register at offset and stores the
retrieved information in data.
Release the acquired semaphore before exiting.

.. _`e1000e_read_phy_reg_igp_locked`:

e1000e_read_phy_reg_igp_locked
==============================

.. c:function:: s32 e1000e_read_phy_reg_igp_locked(struct e1000_hw *hw, u32 offset, u16 *data)

    Read igp PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000e_read_phy_reg_igp_locked.description`:

Description
-----------

Reads the PHY register at offset and stores the retrieved information
in data.  Assumes semaphore already acquired.

.. _`__e1000e_write_phy_reg_igp`:

__e1000e_write_phy_reg_igp
==========================

.. c:function:: s32 __e1000e_write_phy_reg_igp(struct e1000_hw *hw, u32 offset, u16 data, bool locked)

    Write igp PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

    :param bool locked:
        semaphore has already been acquired or not

.. _`__e1000e_write_phy_reg_igp.description`:

Description
-----------

Acquires semaphore, if necessary, then writes the data to PHY register
at the offset.  Release any acquired semaphores before exiting.

.. _`e1000e_write_phy_reg_igp`:

e1000e_write_phy_reg_igp
========================

.. c:function:: s32 e1000e_write_phy_reg_igp(struct e1000_hw *hw, u32 offset, u16 data)

    Write igp PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000e_write_phy_reg_igp.description`:

Description
-----------

Acquires semaphore then writes the data to PHY register
at the offset.  Release any acquired semaphores before exiting.

.. _`e1000e_write_phy_reg_igp_locked`:

e1000e_write_phy_reg_igp_locked
===============================

.. c:function:: s32 e1000e_write_phy_reg_igp_locked(struct e1000_hw *hw, u32 offset, u16 data)

    Write igp PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000e_write_phy_reg_igp_locked.description`:

Description
-----------

Writes the data to PHY register at the offset.
Assumes semaphore already acquired.

.. _`__e1000_read_kmrn_reg`:

__e1000_read_kmrn_reg
=====================

.. c:function:: s32 __e1000_read_kmrn_reg(struct e1000_hw *hw, u32 offset, u16 *data, bool locked)

    Read kumeran register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

    :param bool locked:
        semaphore has already been acquired or not

.. _`__e1000_read_kmrn_reg.description`:

Description
-----------

Acquires semaphore, if necessary.  Then reads the PHY register at offset
using the kumeran interface.  The information retrieved is stored in data.
Release any acquired semaphores before exiting.

.. _`e1000e_read_kmrn_reg`:

e1000e_read_kmrn_reg
====================

.. c:function:: s32 e1000e_read_kmrn_reg(struct e1000_hw *hw, u32 offset, u16 *data)

    Read kumeran register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000e_read_kmrn_reg.description`:

Description
-----------

Acquires semaphore then reads the PHY register at offset using the
kumeran interface.  The information retrieved is stored in data.
Release the acquired semaphore before exiting.

.. _`e1000e_read_kmrn_reg_locked`:

e1000e_read_kmrn_reg_locked
===========================

.. c:function:: s32 e1000e_read_kmrn_reg_locked(struct e1000_hw *hw, u32 offset, u16 *data)

    Read kumeran register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000e_read_kmrn_reg_locked.description`:

Description
-----------

Reads the PHY register at offset using the kumeran interface.  The
information retrieved is stored in data.
Assumes semaphore already acquired.

.. _`__e1000_write_kmrn_reg`:

__e1000_write_kmrn_reg
======================

.. c:function:: s32 __e1000_write_kmrn_reg(struct e1000_hw *hw, u32 offset, u16 data, bool locked)

    Write kumeran register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

    :param bool locked:
        semaphore has already been acquired or not

.. _`__e1000_write_kmrn_reg.description`:

Description
-----------

Acquires semaphore, if necessary.  Then write the data to PHY register
at the offset using the kumeran interface.  Release any acquired semaphores
before exiting.

.. _`e1000e_write_kmrn_reg`:

e1000e_write_kmrn_reg
=====================

.. c:function:: s32 e1000e_write_kmrn_reg(struct e1000_hw *hw, u32 offset, u16 data)

    Write kumeran register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000e_write_kmrn_reg.description`:

Description
-----------

Acquires semaphore then writes the data to the PHY register at the offset
using the kumeran interface.  Release the acquired semaphore before exiting.

.. _`e1000e_write_kmrn_reg_locked`:

e1000e_write_kmrn_reg_locked
============================

.. c:function:: s32 e1000e_write_kmrn_reg_locked(struct e1000_hw *hw, u32 offset, u16 data)

    Write kumeran register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000e_write_kmrn_reg_locked.description`:

Description
-----------

Write the data to PHY register at the offset using the kumeran interface.
Assumes semaphore already acquired.

.. _`e1000_set_master_slave_mode`:

e1000_set_master_slave_mode
===========================

.. c:function:: s32 e1000_set_master_slave_mode(struct e1000_hw *hw)

    Setup PHY for Master/slave mode

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_set_master_slave_mode.description`:

Description
-----------

Sets up Master/slave mode

.. _`e1000_copper_link_setup_82577`:

e1000_copper_link_setup_82577
=============================

.. c:function:: s32 e1000_copper_link_setup_82577(struct e1000_hw *hw)

    Setup 82577 PHY for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_copper_link_setup_82577.description`:

Description
-----------

Sets up Carrier-sense on Transmit and downshift values.

.. _`e1000e_copper_link_setup_m88`:

e1000e_copper_link_setup_m88
============================

.. c:function:: s32 e1000e_copper_link_setup_m88(struct e1000_hw *hw)

    Setup m88 PHY's for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_copper_link_setup_m88.description`:

Description
-----------

Sets up MDI/MDI-X and polarity for m88 PHY's.  If necessary, transmit clock
and downshift values are set also.

.. _`e1000e_copper_link_setup_igp`:

e1000e_copper_link_setup_igp
============================

.. c:function:: s32 e1000e_copper_link_setup_igp(struct e1000_hw *hw)

    Setup igp PHY's for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_copper_link_setup_igp.description`:

Description
-----------

Sets up LPLU, MDI/MDI-X, polarity, Smartspeed and Master/Slave config for
igp PHY's.

.. _`e1000_phy_setup_autoneg`:

e1000_phy_setup_autoneg
=======================

.. c:function:: s32 e1000_phy_setup_autoneg(struct e1000_hw *hw)

    Configure PHY for auto-negotiation

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_phy_setup_autoneg.description`:

Description
-----------

Reads the MII auto-neg advertisement register and/or the 1000T control
register and if the PHY is already setup for auto-negotiation, then
return successful.  Otherwise, setup advertisement and flow control to
the appropriate values for the wanted auto-negotiation.

.. _`e1000_copper_link_autoneg`:

e1000_copper_link_autoneg
=========================

.. c:function:: s32 e1000_copper_link_autoneg(struct e1000_hw *hw)

    Setup/Enable autoneg for copper link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_copper_link_autoneg.description`:

Description
-----------

Performs initial bounds checking on autoneg advertisement parameter, then
configure to advertise the full capability.  Setup the PHY to autoneg
and restart the negotiation process between the link partner.  If
autoneg_wait_to_complete, then wait for autoneg to complete before exiting.

.. _`e1000e_setup_copper_link`:

e1000e_setup_copper_link
========================

.. c:function:: s32 e1000e_setup_copper_link(struct e1000_hw *hw)

    Configure copper link settings

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_setup_copper_link.description`:

Description
-----------

Calls the appropriate function to configure the link for auto-neg or forced
speed and duplex.  Then we check for link, once link is established calls
to configure collision distance and flow control are called.  If link is
not established, we return -E1000_ERR_PHY (-2).

.. _`e1000e_phy_force_speed_duplex_igp`:

e1000e_phy_force_speed_duplex_igp
=================================

.. c:function:: s32 e1000e_phy_force_speed_duplex_igp(struct e1000_hw *hw)

    Force speed/duplex for igp PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_phy_force_speed_duplex_igp.description`:

Description
-----------

Calls the PHY setup function to force speed and duplex.  Clears the
auto-crossover to force MDI manually.  Waits for link and returns
successful if link up is successful, else -E1000_ERR_PHY (-2).

.. _`e1000e_phy_force_speed_duplex_m88`:

e1000e_phy_force_speed_duplex_m88
=================================

.. c:function:: s32 e1000e_phy_force_speed_duplex_m88(struct e1000_hw *hw)

    Force speed/duplex for m88 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_phy_force_speed_duplex_m88.description`:

Description
-----------

Calls the PHY setup function to force speed and duplex.  Clears the
auto-crossover to force MDI manually.  Resets the PHY to commit the
changes.  If time expires while waiting for link up, we reset the DSP.
After reset, TX_CLK and CRS on Tx must be set.  Return successful upon
successful completion, else return corresponding error code.

.. _`e1000_phy_force_speed_duplex_ife`:

e1000_phy_force_speed_duplex_ife
================================

.. c:function:: s32 e1000_phy_force_speed_duplex_ife(struct e1000_hw *hw)

    Force PHY speed & duplex

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_phy_force_speed_duplex_ife.description`:

Description
-----------

Forces the speed and duplex settings of the PHY.
This is a function pointer entry point only called by
PHY setup routines.

.. _`e1000e_phy_force_speed_duplex_setup`:

e1000e_phy_force_speed_duplex_setup
===================================

.. c:function:: void e1000e_phy_force_speed_duplex_setup(struct e1000_hw *hw, u16 *phy_ctrl)

    Configure forced PHY speed/duplex

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 \*phy_ctrl:
        pointer to current value of MII_BMCR

.. _`e1000e_phy_force_speed_duplex_setup.forces-speed-and-duplex-on-the-phy-by-doing-the-following`:

Forces speed and duplex on the PHY by doing the following
---------------------------------------------------------

disable flow
control, force speed/duplex on the MAC, disable auto speed detection,
disable auto-negotiation, configure duplex, configure speed, configure
the collision distance, write configuration to CTRL register.  The
caller must write to the MII_BMCR register for these settings to
take affect.

.. _`e1000e_set_d3_lplu_state`:

e1000e_set_d3_lplu_state
========================

.. c:function:: s32 e1000e_set_d3_lplu_state(struct e1000_hw *hw, bool active)

    Sets low power link up state for D3

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param bool active:
        boolean used to enable/disable lplu

.. _`e1000e_set_d3_lplu_state.description`:

Description
-----------

Success returns 0, Failure returns 1

The low power link up (lplu) state is set to the power management level D3
and SmartSpeed is disabled when active is true, else clear lplu for D3
and enable Smartspeed.  LPLU and Smartspeed are mutually exclusive.  LPLU
is used during Dx states where the power conservation is most important.
During driver activity, SmartSpeed should be enabled so performance is
maintained.

.. _`e1000e_check_downshift`:

e1000e_check_downshift
======================

.. c:function:: s32 e1000e_check_downshift(struct e1000_hw *hw)

    Checks whether a downshift in speed occurred

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_check_downshift.description`:

Description
-----------

Success returns 0, Failure returns 1

A downshift is detected by querying the PHY link health.

.. _`e1000_check_polarity_m88`:

e1000_check_polarity_m88
========================

.. c:function:: s32 e1000_check_polarity_m88(struct e1000_hw *hw)

    Checks the polarity.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_polarity_m88.description`:

Description
-----------

Success returns 0, Failure returns -E1000_ERR_PHY (-2)

Polarity is determined based on the PHY specific status register.

.. _`e1000_check_polarity_igp`:

e1000_check_polarity_igp
========================

.. c:function:: s32 e1000_check_polarity_igp(struct e1000_hw *hw)

    Checks the polarity.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_polarity_igp.description`:

Description
-----------

Success returns 0, Failure returns -E1000_ERR_PHY (-2)

Polarity is determined based on the PHY port status register, and the
current speed (since there is no polarity at 100Mbps).

.. _`e1000_check_polarity_ife`:

e1000_check_polarity_ife
========================

.. c:function:: s32 e1000_check_polarity_ife(struct e1000_hw *hw)

    Check cable polarity for IFE PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_polarity_ife.description`:

Description
-----------

Polarity is determined on the polarity reversal feature being enabled.

.. _`e1000_wait_autoneg`:

e1000_wait_autoneg
==================

.. c:function:: s32 e1000_wait_autoneg(struct e1000_hw *hw)

    Wait for auto-neg completion

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_wait_autoneg.description`:

Description
-----------

Waits for auto-negotiation to complete or for the auto-negotiation time
limit to expire, which ever happens first.

.. _`e1000e_phy_has_link_generic`:

e1000e_phy_has_link_generic
===========================

.. c:function:: s32 e1000e_phy_has_link_generic(struct e1000_hw *hw, u32 iterations, u32 usec_interval, bool *success)

    Polls PHY for link

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 iterations:
        number of times to poll for link

    :param u32 usec_interval:
        delay between polling attempts

    :param bool \*success:
        pointer to whether polling was successful or not

.. _`e1000e_phy_has_link_generic.description`:

Description
-----------

Polls the PHY status register for link, 'iterations' number of times.

.. _`e1000e_get_cable_length_m88`:

e1000e_get_cable_length_m88
===========================

.. c:function:: s32 e1000e_get_cable_length_m88(struct e1000_hw *hw)

    Determine cable length for m88 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_get_cable_length_m88.description`:

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

.. _`e1000e_get_cable_length_igp_2`:

e1000e_get_cable_length_igp_2
=============================

.. c:function:: s32 e1000e_get_cable_length_igp_2(struct e1000_hw *hw)

    Determine cable length for igp2 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_get_cable_length_igp_2.description`:

Description
-----------

The automatic gain control (agc) normalizes the amplitude of the
received signal, adjusting for the attenuation produced by the
cable.  By reading the AGC registers, which represent the
combination of coarse and fine gain value, the value can be put
into a lookup table to obtain the approximate cable length
for each channel.

.. _`e1000e_get_phy_info_m88`:

e1000e_get_phy_info_m88
=======================

.. c:function:: s32 e1000e_get_phy_info_m88(struct e1000_hw *hw)

    Retrieve PHY information

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_get_phy_info_m88.description`:

Description
-----------

Valid for only copper links.  Read the PHY status register (sticky read)
to verify that link is up.  Read the PHY special control register to
determine the polarity and 10base-T extended distance.  Read the PHY
special status register to determine MDI/MDIx and current speed.  If
speed is 1000, then determine cable length, local and remote receiver.

.. _`e1000e_get_phy_info_igp`:

e1000e_get_phy_info_igp
=======================

.. c:function:: s32 e1000e_get_phy_info_igp(struct e1000_hw *hw)

    Retrieve igp PHY information

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_get_phy_info_igp.description`:

Description
-----------

Read PHY status to determine if link is up.  If link is up, then
set/determine 10base-T extended distance and polarity correction.  Read
PHY port status to determine MDI/MDIx and speed.  Based on the speed,
determine on the cable length, local and remote receiver.

.. _`e1000_get_phy_info_ife`:

e1000_get_phy_info_ife
======================

.. c:function:: s32 e1000_get_phy_info_ife(struct e1000_hw *hw)

    Retrieves various IFE PHY states

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_get_phy_info_ife.description`:

Description
-----------

Populates "phy" structure with various feature states.

.. _`e1000e_phy_sw_reset`:

e1000e_phy_sw_reset
===================

.. c:function:: s32 e1000e_phy_sw_reset(struct e1000_hw *hw)

    PHY software reset

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_phy_sw_reset.description`:

Description
-----------

Does a software reset of the PHY by reading the PHY control register and
setting/write the control register reset bit to the PHY.

.. _`e1000e_phy_hw_reset_generic`:

e1000e_phy_hw_reset_generic
===========================

.. c:function:: s32 e1000e_phy_hw_reset_generic(struct e1000_hw *hw)

    PHY hardware reset

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_phy_hw_reset_generic.description`:

Description
-----------

Verify the reset block is not blocking us from resetting.  Acquire
semaphore (if necessary) and read/set/write the device control reset
bit in the PHY.  Wait the appropriate delay time for the device to
reset and release the semaphore (if necessary).

.. _`e1000e_get_cfg_done_generic`:

e1000e_get_cfg_done_generic
===========================

.. c:function:: s32 e1000e_get_cfg_done_generic(struct e1000_hw __always_unused *hw)

    Generic configuration done

    :param struct e1000_hw __always_unused \*hw:
        pointer to the HW structure

.. _`e1000e_get_cfg_done_generic.description`:

Description
-----------

Generic function to wait 10 milli-seconds for configuration to complete
and return success.

.. _`e1000e_phy_init_script_igp3`:

e1000e_phy_init_script_igp3
===========================

.. c:function:: s32 e1000e_phy_init_script_igp3(struct e1000_hw *hw)

    Inits the IGP3 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_phy_init_script_igp3.description`:

Description
-----------

Initializes a Intel Gigabit PHY3 when an EEPROM is not present.

.. _`e1000e_get_phy_type_from_id`:

e1000e_get_phy_type_from_id
===========================

.. c:function:: enum e1000_phy_type e1000e_get_phy_type_from_id(u32 phy_id)

    Get PHY type from id

    :param u32 phy_id:
        phy_id read from the phy

.. _`e1000e_get_phy_type_from_id.description`:

Description
-----------

Returns the phy type from the id.

.. _`e1000e_determine_phy_address`:

e1000e_determine_phy_address
============================

.. c:function:: s32 e1000e_determine_phy_address(struct e1000_hw *hw)

    Determines PHY address.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000e_determine_phy_address.description`:

Description
-----------

This uses a trial and error method to loop through possible PHY
addresses. It tests each by reading the PHY ID registers and
checking for a match.

.. _`e1000_get_phy_addr_for_bm_page`:

e1000_get_phy_addr_for_bm_page
==============================

.. c:function:: u32 e1000_get_phy_addr_for_bm_page(u32 page, u32 reg)

    Retrieve PHY page address

    :param u32 page:
        page to access

    :param u32 reg:
        *undescribed*

.. _`e1000_get_phy_addr_for_bm_page.description`:

Description
-----------

Returns the phy address for the page requested.

.. _`e1000e_write_phy_reg_bm`:

e1000e_write_phy_reg_bm
=======================

.. c:function:: s32 e1000e_write_phy_reg_bm(struct e1000_hw *hw, u32 offset, u16 data)

    Write BM PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000e_write_phy_reg_bm.description`:

Description
-----------

Acquires semaphore, if necessary, then writes the data to PHY register
at the offset.  Release any acquired semaphores before exiting.

.. _`e1000e_read_phy_reg_bm`:

e1000e_read_phy_reg_bm
======================

.. c:function:: s32 e1000e_read_phy_reg_bm(struct e1000_hw *hw, u32 offset, u16 *data)

    Read BM PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000e_read_phy_reg_bm.description`:

Description
-----------

Acquires semaphore, if necessary, then reads the PHY register at offset
and storing the retrieved information in data.  Release any acquired
semaphores before exiting.

.. _`e1000e_read_phy_reg_bm2`:

e1000e_read_phy_reg_bm2
=======================

.. c:function:: s32 e1000e_read_phy_reg_bm2(struct e1000_hw *hw, u32 offset, u16 *data)

    Read BM PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000e_read_phy_reg_bm2.description`:

Description
-----------

Acquires semaphore, if necessary, then reads the PHY register at offset
and storing the retrieved information in data.  Release any acquired
semaphores before exiting.

.. _`e1000e_write_phy_reg_bm2`:

e1000e_write_phy_reg_bm2
========================

.. c:function:: s32 e1000e_write_phy_reg_bm2(struct e1000_hw *hw, u32 offset, u16 data)

    Write BM PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000e_write_phy_reg_bm2.description`:

Description
-----------

Acquires semaphore, if necessary, then writes the data to PHY register
at the offset.  Release any acquired semaphores before exiting.

.. _`e1000_enable_phy_wakeup_reg_access_bm`:

e1000_enable_phy_wakeup_reg_access_bm
=====================================

.. c:function:: s32 e1000_enable_phy_wakeup_reg_access_bm(struct e1000_hw *hw, u16 *phy_reg)

    enable access to BM wakeup registers

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 \*phy_reg:
        pointer to store original contents of BM_WUC_ENABLE_REG

.. _`e1000_enable_phy_wakeup_reg_access_bm.description`:

Description
-----------

Assumes semaphore already acquired and phy_reg points to a valid memory
address to store contents of the BM_WUC_ENABLE_REG register.

.. _`e1000_disable_phy_wakeup_reg_access_bm`:

e1000_disable_phy_wakeup_reg_access_bm
======================================

.. c:function:: s32 e1000_disable_phy_wakeup_reg_access_bm(struct e1000_hw *hw, u16 *phy_reg)

    disable access to BM wakeup regs

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u16 \*phy_reg:
        pointer to original contents of BM_WUC_ENABLE_REG

.. _`e1000_disable_phy_wakeup_reg_access_bm.description`:

Description
-----------

Restore BM_WUC_ENABLE_REG to its original value.

Assumes semaphore already acquired and \*phy_reg is the contents of the
BM_WUC_ENABLE_REG before register(s) on BM_WUC_PAGE were accessed by
caller.

.. _`e1000_access_phy_wakeup_reg_bm`:

e1000_access_phy_wakeup_reg_bm
==============================

.. c:function:: s32 e1000_access_phy_wakeup_reg_bm(struct e1000_hw *hw, u32 offset, u16 *data, bool read, bool page_set)

    Read/write BM PHY wakeup register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read or written

    :param u16 \*data:
        pointer to the data to read or write

    :param bool read:
        determines if operation is read or write

    :param bool page_set:
        BM_WUC_PAGE already set and access enabled

.. _`e1000_access_phy_wakeup_reg_bm.description`:

Description
-----------

Read the PHY register at offset and store the retrieved information in
data, or write data to PHY register at offset.  Note the procedure to
access the PHY wakeup registers is different than reading the other PHY
registers. It works as such:
1) Set 769.17.2 (page 769, register 17, bit 2) = 1
2) Set page to 800 for host (801 if we were manageability)
3) Write the address using the address opcode (0x11)
4) Read or write the data using the data opcode (0x12)
5) Restore 769.17.2 to its original value

Steps 1 and 2 are done by \ :c:func:`e1000_enable_phy_wakeup_reg_access_bm`\  and
step 5 is done by \ :c:func:`e1000_disable_phy_wakeup_reg_access_bm`\ .

Assumes semaphore is already acquired.  When page_set==true, assumes
the PHY page is set to BM_WUC_PAGE (i.e. a function in the call stack
is responsible for calls to e1000_[enable\|disable]\ :c:func:`_phy_wakeup_reg_bm`\ ).

.. _`e1000_power_up_phy_copper`:

e1000_power_up_phy_copper
=========================

.. c:function:: void e1000_power_up_phy_copper(struct e1000_hw *hw)

    Restore copper link in case of PHY power down

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_power_up_phy_copper.description`:

Description
-----------

In the case of a PHY power down to save power, or to turn off link during a
driver unload, or wake on lan is not enabled, restore the link to previous
settings.

.. _`e1000_power_down_phy_copper`:

e1000_power_down_phy_copper
===========================

.. c:function:: void e1000_power_down_phy_copper(struct e1000_hw *hw)

    Restore copper link in case of PHY power down

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_power_down_phy_copper.description`:

Description
-----------

In the case of a PHY power down to save power, or to turn off link during a
driver unload, or wake on lan is not enabled, restore the link to previous
settings.

.. _`__e1000_read_phy_reg_hv`:

__e1000_read_phy_reg_hv
=======================

.. c:function:: s32 __e1000_read_phy_reg_hv(struct e1000_hw *hw, u32 offset, u16 *data, bool locked, bool page_set)

    Read HV PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

    :param bool locked:
        semaphore has already been acquired or not

    :param bool page_set:
        *undescribed*

.. _`__e1000_read_phy_reg_hv.description`:

Description
-----------

Acquires semaphore, if necessary, then reads the PHY register at offset
and stores the retrieved information in data.  Release any acquired
semaphore before exiting.

.. _`e1000_read_phy_reg_hv`:

e1000_read_phy_reg_hv
=====================

.. c:function:: s32 e1000_read_phy_reg_hv(struct e1000_hw *hw, u32 offset, u16 *data)

    Read HV PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000_read_phy_reg_hv.description`:

Description
-----------

Acquires semaphore then reads the PHY register at offset and stores
the retrieved information in data.  Release the acquired semaphore
before exiting.

.. _`e1000_read_phy_reg_hv_locked`:

e1000_read_phy_reg_hv_locked
============================

.. c:function:: s32 e1000_read_phy_reg_hv_locked(struct e1000_hw *hw, u32 offset, u16 *data)

    Read HV PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read

    :param u16 \*data:
        pointer to the read data

.. _`e1000_read_phy_reg_hv_locked.description`:

Description
-----------

Reads the PHY register at offset and stores the retrieved information
in data.  Assumes semaphore already acquired.

.. _`e1000_read_phy_reg_page_hv`:

e1000_read_phy_reg_page_hv
==========================

.. c:function:: s32 e1000_read_phy_reg_page_hv(struct e1000_hw *hw, u32 offset, u16 *data)

    Read HV PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 \*data:
        data to write at register offset

.. _`e1000_read_phy_reg_page_hv.description`:

Description
-----------

Reads the PHY register at offset and stores the retrieved information
in data.  Assumes semaphore already acquired and page already set.

.. _`__e1000_write_phy_reg_hv`:

__e1000_write_phy_reg_hv
========================

.. c:function:: s32 __e1000_write_phy_reg_hv(struct e1000_hw *hw, u32 offset, u16 data, bool locked, bool page_set)

    Write HV PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

    :param bool locked:
        semaphore has already been acquired or not

    :param bool page_set:
        *undescribed*

.. _`__e1000_write_phy_reg_hv.description`:

Description
-----------

Acquires semaphore, if necessary, then writes the data to PHY register
at the offset.  Release any acquired semaphores before exiting.

.. _`e1000_write_phy_reg_hv`:

e1000_write_phy_reg_hv
======================

.. c:function:: s32 e1000_write_phy_reg_hv(struct e1000_hw *hw, u32 offset, u16 data)

    Write HV PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000_write_phy_reg_hv.description`:

Description
-----------

Acquires semaphore then writes the data to PHY register at the offset.
Release the acquired semaphores before exiting.

.. _`e1000_write_phy_reg_hv_locked`:

e1000_write_phy_reg_hv_locked
=============================

.. c:function:: s32 e1000_write_phy_reg_hv_locked(struct e1000_hw *hw, u32 offset, u16 data)

    Write HV PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000_write_phy_reg_hv_locked.description`:

Description
-----------

Writes the data to PHY register at the offset.  Assumes semaphore
already acquired.

.. _`e1000_write_phy_reg_page_hv`:

e1000_write_phy_reg_page_hv
===========================

.. c:function:: s32 e1000_write_phy_reg_page_hv(struct e1000_hw *hw, u32 offset, u16 data)

    Write HV PHY register

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to write to

    :param u16 data:
        data to write at register offset

.. _`e1000_write_phy_reg_page_hv.description`:

Description
-----------

Writes the data to PHY register at the offset.  Assumes semaphore
already acquired and page already set.

.. _`e1000_get_phy_addr_for_hv_page`:

e1000_get_phy_addr_for_hv_page
==============================

.. c:function:: u32 e1000_get_phy_addr_for_hv_page(u32 page)

    Get PHY address based on page

    :param u32 page:
        page to be accessed

.. _`e1000_access_phy_debug_regs_hv`:

e1000_access_phy_debug_regs_hv
==============================

.. c:function:: s32 e1000_access_phy_debug_regs_hv(struct e1000_hw *hw, u32 offset, u16 *data, bool read)

    Read HV PHY vendor specific high registers

    :param struct e1000_hw \*hw:
        pointer to the HW structure

    :param u32 offset:
        register offset to be read or written

    :param u16 \*data:
        pointer to the data to be read or written

    :param bool read:
        determines if operation is read or write

.. _`e1000_access_phy_debug_regs_hv.description`:

Description
-----------

Reads the PHY register at offset and stores the retreived information
in data.  Assumes semaphore already acquired.  Note that the procedure
to access these regs uses the address port and data port to read/write.
These accesses done with PHY address 2 and without using pages.

.. _`e1000_link_stall_workaround_hv`:

e1000_link_stall_workaround_hv
==============================

.. c:function:: s32 e1000_link_stall_workaround_hv(struct e1000_hw *hw)

    Si workaround

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_link_stall_workaround_hv.description`:

Description
-----------

This function works around a Si bug where the link partner can get
a link up indication before the PHY does.  If small packets are sent
by the link partner they can be placed in the packet buffer without
being properly accounted for by the PHY and will stall preventing
further packets from being received.  The workaround is to clear the
packet buffer after the PHY detects link up.

.. _`e1000_check_polarity_82577`:

e1000_check_polarity_82577
==========================

.. c:function:: s32 e1000_check_polarity_82577(struct e1000_hw *hw)

    Checks the polarity.

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_check_polarity_82577.description`:

Description
-----------

Success returns 0, Failure returns -E1000_ERR_PHY (-2)

Polarity is determined based on the PHY specific status register.

.. _`e1000_phy_force_speed_duplex_82577`:

e1000_phy_force_speed_duplex_82577
==================================

.. c:function:: s32 e1000_phy_force_speed_duplex_82577(struct e1000_hw *hw)

    Force speed/duplex for I82577 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_phy_force_speed_duplex_82577.description`:

Description
-----------

Calls the PHY setup function to force speed and duplex.

.. _`e1000_get_phy_info_82577`:

e1000_get_phy_info_82577
========================

.. c:function:: s32 e1000_get_phy_info_82577(struct e1000_hw *hw)

    Retrieve I82577 PHY information

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_get_phy_info_82577.description`:

Description
-----------

Read PHY status to determine if link is up.  If link is up, then
set/determine 10base-T extended distance and polarity correction.  Read
PHY port status to determine MDI/MDIx and speed.  Based on the speed,
determine on the cable length, local and remote receiver.

.. _`e1000_get_cable_length_82577`:

e1000_get_cable_length_82577
============================

.. c:function:: s32 e1000_get_cable_length_82577(struct e1000_hw *hw)

    Determine cable length for 82577 PHY

    :param struct e1000_hw \*hw:
        pointer to the HW structure

.. _`e1000_get_cable_length_82577.description`:

Description
-----------

Reads the diagnostic status register and verifies result is valid before
placing it in the phy_cable_length field.

.. This file was automatic generated / don't edit.

