.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_x550.c

.. _`ixgbe_read_cs4227`:

ixgbe_read_cs4227
=================

.. c:function:: s32 ixgbe_read_cs4227(struct ixgbe_hw *hw, u16 reg, u16 *value)

    Read CS4227 register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg:
        register number to write
    :type reg: u16

    :param value:
        pointer to receive value read
    :type value: u16 \*

.. _`ixgbe_read_cs4227.description`:

Description
-----------

Returns status code

.. _`ixgbe_write_cs4227`:

ixgbe_write_cs4227
==================

.. c:function:: s32 ixgbe_write_cs4227(struct ixgbe_hw *hw, u16 reg, u16 value)

    Write CS4227 register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg:
        register number to write
    :type reg: u16

    :param value:
        value to write to register
    :type value: u16

.. _`ixgbe_write_cs4227.description`:

Description
-----------

Returns status code

.. _`ixgbe_read_pe`:

ixgbe_read_pe
=============

.. c:function:: s32 ixgbe_read_pe(struct ixgbe_hw *hw, u8 reg, u8 *value)

    Read register from port expander

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg:
        register number to read
    :type reg: u8

    :param value:
        pointer to receive read value
    :type value: u8 \*

.. _`ixgbe_read_pe.description`:

Description
-----------

Returns status code

.. _`ixgbe_write_pe`:

ixgbe_write_pe
==============

.. c:function:: s32 ixgbe_write_pe(struct ixgbe_hw *hw, u8 reg, u8 value)

    Write register to port expander

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg:
        register number to write
    :type reg: u8

    :param value:
        value to write
    :type value: u8

.. _`ixgbe_write_pe.description`:

Description
-----------

Returns status code

.. _`ixgbe_reset_cs4227`:

ixgbe_reset_cs4227
==================

.. c:function:: s32 ixgbe_reset_cs4227(struct ixgbe_hw *hw)

    Reset CS4227 using port expander

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_reset_cs4227.description`:

Description
-----------

This function assumes that the caller has acquired the proper semaphore.
Returns error code

.. _`ixgbe_check_cs4227`:

ixgbe_check_cs4227
==================

.. c:function:: void ixgbe_check_cs4227(struct ixgbe_hw *hw)

    Check CS4227 and reset as needed

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_read_i2c_combined_generic`:

ixgbe_read_i2c_combined_generic
===============================

.. c:function:: s32 ixgbe_read_i2c_combined_generic(struct ixgbe_hw *hw, u8 addr, u16 reg, u16 *val)

    Perform I2C read combined operation

    :param hw:
        pointer to the hardware structure
    :type hw: struct ixgbe_hw \*

    :param addr:
        I2C bus address to read from
    :type addr: u8

    :param reg:
        I2C device register to read from
    :type reg: u16

    :param val:
        pointer to location to receive read value
    :type val: u16 \*

.. _`ixgbe_read_i2c_combined_generic.description`:

Description
-----------

Returns an error code on error.

.. _`ixgbe_read_i2c_combined_generic_unlocked`:

ixgbe_read_i2c_combined_generic_unlocked
========================================

.. c:function:: s32 ixgbe_read_i2c_combined_generic_unlocked(struct ixgbe_hw *hw, u8 addr, u16 reg, u16 *val)

    Do I2C read combined operation

    :param hw:
        pointer to the hardware structure
    :type hw: struct ixgbe_hw \*

    :param addr:
        I2C bus address to read from
    :type addr: u8

    :param reg:
        I2C device register to read from
    :type reg: u16

    :param val:
        pointer to location to receive read value
    :type val: u16 \*

.. _`ixgbe_read_i2c_combined_generic_unlocked.description`:

Description
-----------

Returns an error code on error.

.. _`ixgbe_write_i2c_combined_generic`:

ixgbe_write_i2c_combined_generic
================================

.. c:function:: s32 ixgbe_write_i2c_combined_generic(struct ixgbe_hw *hw, u8 addr, u16 reg, u16 val)

    Perform I2C write combined operation

    :param hw:
        pointer to the hardware structure
    :type hw: struct ixgbe_hw \*

    :param addr:
        I2C bus address to write to
    :type addr: u8

    :param reg:
        I2C device register to write to
    :type reg: u16

    :param val:
        value to write
    :type val: u16

.. _`ixgbe_write_i2c_combined_generic.description`:

Description
-----------

Returns an error code on error.

.. _`ixgbe_write_i2c_combined_generic_unlocked`:

ixgbe_write_i2c_combined_generic_unlocked
=========================================

.. c:function:: s32 ixgbe_write_i2c_combined_generic_unlocked(struct ixgbe_hw *hw, u8 addr, u16 reg, u16 val)

    Do I2C write combined operation

    :param hw:
        pointer to the hardware structure
    :type hw: struct ixgbe_hw \*

    :param addr:
        I2C bus address to write to
    :type addr: u8

    :param reg:
        I2C device register to write to
    :type reg: u16

    :param val:
        value to write
    :type val: u16

.. _`ixgbe_write_i2c_combined_generic_unlocked.description`:

Description
-----------

Returns an error code on error.

.. _`ixgbe_fw_phy_activity`:

ixgbe_fw_phy_activity
=====================

.. c:function:: s32 ixgbe_fw_phy_activity(struct ixgbe_hw *hw, u16 activity, u32 data)

    Perform an activity on a PHY

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param activity:
        activity to perform
    :type activity: u16

    :param data:
        Pointer to 4 32-bit words of data
    :type data: u32

.. _`ixgbe_get_phy_id_fw`:

ixgbe_get_phy_id_fw
===================

.. c:function:: s32 ixgbe_get_phy_id_fw(struct ixgbe_hw *hw)

    Get the phy ID via firmware command

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_get_phy_id_fw.description`:

Description
-----------

Returns error code

.. _`ixgbe_identify_phy_fw`:

ixgbe_identify_phy_fw
=====================

.. c:function:: s32 ixgbe_identify_phy_fw(struct ixgbe_hw *hw)

    Get PHY type based on firmware command

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_identify_phy_fw.description`:

Description
-----------

Returns error code

.. _`ixgbe_shutdown_fw_phy`:

ixgbe_shutdown_fw_phy
=====================

.. c:function:: s32 ixgbe_shutdown_fw_phy(struct ixgbe_hw *hw)

    Shutdown a firmware-controlled PHY

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_shutdown_fw_phy.description`:

Description
-----------

Returns error code

.. _`ixgbe_setup_fw_link`:

ixgbe_setup_fw_link
===================

.. c:function:: s32 ixgbe_setup_fw_link(struct ixgbe_hw *hw)

    Setup firmware-controlled PHYs

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_fc_autoneg_fw`:

ixgbe_fc_autoneg_fw
===================

.. c:function:: s32 ixgbe_fc_autoneg_fw(struct ixgbe_hw *hw)

    Set up flow control for FW-controlled PHYs

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_fc_autoneg_fw.description`:

Description
-----------

Called at init time to set up flow control.

.. _`ixgbe_iosf_wait`:

ixgbe_iosf_wait
===============

.. c:function:: s32 ixgbe_iosf_wait(struct ixgbe_hw *hw, u32 *ctrl)

    Wait for IOSF command completion

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param ctrl:
        pointer to location to receive final IOSF control value
    :type ctrl: u32 \*

.. _`ixgbe_iosf_wait.return`:

Return
------

failing status on timeout

.. _`ixgbe_iosf_wait.note`:

Note
----

ctrl can be NULL if the IOSF control register value is not needed

.. _`ixgbe_get_phy_token`:

ixgbe_get_phy_token
===================

.. c:function:: s32 ixgbe_get_phy_token(struct ixgbe_hw *hw)

    Get the token for shared PHY access

    :param hw:
        Pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_put_phy_token`:

ixgbe_put_phy_token
===================

.. c:function:: s32 ixgbe_put_phy_token(struct ixgbe_hw *hw)

    Put the token for shared PHY access

    :param hw:
        Pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_write_iosf_sb_reg_x550a`:

ixgbe_write_iosf_sb_reg_x550a
=============================

.. c:function:: s32 ixgbe_write_iosf_sb_reg_x550a(struct ixgbe_hw *hw, u32 reg_addr, __always_unused u32 device_type, u32 data)

    Write to IOSF PHY register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg_addr:
        32 bit PHY register to write
    :type reg_addr: u32

    :param device_type:
        3 bit device type
    :type device_type: __always_unused u32

    :param data:
        Data to write to the register
    :type data: u32

.. _`ixgbe_read_iosf_sb_reg_x550a`:

ixgbe_read_iosf_sb_reg_x550a
============================

.. c:function:: s32 ixgbe_read_iosf_sb_reg_x550a(struct ixgbe_hw *hw, u32 reg_addr, __always_unused u32 device_type, u32 *data)

    Read from IOSF PHY register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg_addr:
        32 bit PHY register to write
    :type reg_addr: u32

    :param device_type:
        3 bit device type
    :type device_type: __always_unused u32

    :param data:
        Pointer to read data from the register
    :type data: u32 \*

.. _`ixgbe_get_bus_info_x550em`:

ixgbe_get_bus_info_X550em
=========================

.. c:function:: s32 ixgbe_get_bus_info_X550em(struct ixgbe_hw *hw)

    Set PCI bus info

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_get_bus_info_x550em.description`:

Description
-----------

Sets bus link width and speed to unknown because X550em is
not a PCI device.

.. _`ixgbe_fw_recovery_mode_x550`:

ixgbe_fw_recovery_mode_X550
===========================

.. c:function:: bool ixgbe_fw_recovery_mode_X550(struct ixgbe_hw *hw)

    Check FW NVM recovery mode

    :param hw:
        pointer t hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_fw_recovery_mode_x550.description`:

Description
-----------

Returns true if in FW NVM recovery mode.

.. _`ixgbe_setup_ixfi_x550em_x`:

ixgbe_setup_ixfi_x550em_x
=========================

.. c:function:: s32 ixgbe_setup_ixfi_x550em_x(struct ixgbe_hw *hw)

    MAC specific iXFI configuration

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_setup_ixfi_x550em_x.description`:

Description
-----------

iXfI configuration needed for ixgbe_mac_X550EM_x devices.

.. _`ixgbe_restart_an_internal_phy_x550em`:

ixgbe_restart_an_internal_phy_x550em
====================================

.. c:function:: s32 ixgbe_restart_an_internal_phy_x550em(struct ixgbe_hw *hw)

    restart autonegotiation for the internal PHY

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_supported_sfp_modules_x550em`:

ixgbe_supported_sfp_modules_X550em
==================================

.. c:function:: s32 ixgbe_supported_sfp_modules_X550em(struct ixgbe_hw *hw, bool *linear)

    Check if SFP module type is supported

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param linear:
        true if SFP module is linear
    :type linear: bool \*

.. _`ixgbe_setup_mac_link_sfp_x550em`:

ixgbe_setup_mac_link_sfp_x550em
===============================

.. c:function:: s32 ixgbe_setup_mac_link_sfp_x550em(struct ixgbe_hw *hw, ixgbe_link_speed speed, __always_unused bool autoneg_wait_to_complete)

    Configure the KR PHY for SFP.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        the link speed to force
    :type speed: ixgbe_link_speed

    :param autoneg_wait_to_complete:
        unused
    :type autoneg_wait_to_complete: __always_unused bool

.. _`ixgbe_setup_mac_link_sfp_x550em.description`:

Description
-----------

Configures the extern PHY and the integrated KR PHY for SFP support.

.. _`ixgbe_setup_sfi_x550a`:

ixgbe_setup_sfi_x550a
=====================

.. c:function:: s32 ixgbe_setup_sfi_x550a(struct ixgbe_hw *hw, ixgbe_link_speed *speed)

    Configure the internal PHY for native SFI mode

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        the link speed to force
    :type speed: ixgbe_link_speed \*

.. _`ixgbe_setup_sfi_x550a.description`:

Description
-----------

Configures the integrated PHY for native SFI mode. Used to connect the
internal PHY directly to an SFP cage, without autonegotiation.

.. _`ixgbe_setup_mac_link_sfp_n`:

ixgbe_setup_mac_link_sfp_n
==========================

.. c:function:: s32 ixgbe_setup_mac_link_sfp_n(struct ixgbe_hw *hw, ixgbe_link_speed speed, __always_unused bool autoneg_wait_to_complete)

    Setup internal PHY for native SFP

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        link speed
    :type speed: ixgbe_link_speed

    :param autoneg_wait_to_complete:
        unused
    :type autoneg_wait_to_complete: __always_unused bool

.. _`ixgbe_setup_mac_link_sfp_n.description`:

Description
-----------

Configure the the integrated PHY for native SFP support.

.. _`ixgbe_setup_mac_link_sfp_x550a`:

ixgbe_setup_mac_link_sfp_x550a
==============================

.. c:function:: s32 ixgbe_setup_mac_link_sfp_x550a(struct ixgbe_hw *hw, ixgbe_link_speed speed, __always_unused bool autoneg_wait_to_complete)

    Setup internal PHY for SFP

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        link speed
    :type speed: ixgbe_link_speed

    :param autoneg_wait_to_complete:
        unused
    :type autoneg_wait_to_complete: __always_unused bool

.. _`ixgbe_setup_mac_link_sfp_x550a.description`:

Description
-----------

Configure the the integrated PHY for SFP support.

.. _`ixgbe_setup_mac_link_t_x550em`:

ixgbe_setup_mac_link_t_X550em
=============================

.. c:function:: s32 ixgbe_setup_mac_link_t_X550em(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait)

    Sets the auto advertised link speed

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        new link speed
    :type speed: ixgbe_link_speed

    :param autoneg_wait:
        true when waiting for completion is needed
    :type autoneg_wait: bool

.. _`ixgbe_setup_mac_link_t_x550em.description`:

Description
-----------

Setup internal/external PHY link speed based on link speed, then set
external PHY auto advertised link speed.

Returns error status for any failure

.. _`ixgbe_setup_sgmii`:

ixgbe_setup_sgmii
=================

.. c:function:: s32 ixgbe_setup_sgmii(struct ixgbe_hw *hw, __always_unused ixgbe_link_speed speed, __always_unused bool autoneg_wait_to_complete)

    Set up link for sgmii

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        unused
    :type speed: __always_unused ixgbe_link_speed

    :param autoneg_wait_to_complete:
        unused
    :type autoneg_wait_to_complete: __always_unused bool

.. _`ixgbe_setup_sgmii_fw`:

ixgbe_setup_sgmii_fw
====================

.. c:function:: s32 ixgbe_setup_sgmii_fw(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait)

    Set up link for sgmii with firmware-controlled PHYs

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        the link speed to force
    :type speed: ixgbe_link_speed

    :param autoneg_wait:
        true when waiting for completion is needed
    :type autoneg_wait: bool

.. _`ixgbe_fc_autoneg_sgmii_x550em_a`:

ixgbe_fc_autoneg_sgmii_x550em_a
===============================

.. c:function:: void ixgbe_fc_autoneg_sgmii_x550em_a(struct ixgbe_hw *hw)

    Enable flow control IEEE clause 37

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_fc_autoneg_sgmii_x550em_a.description`:

Description
-----------

Enable flow control according to IEEE clause 37.

.. _`ixgbe_get_lasi_ext_t_x550em`:

ixgbe_get_lasi_ext_t_x550em
===========================

.. c:function:: s32 ixgbe_get_lasi_ext_t_x550em(struct ixgbe_hw *hw, bool *lsc)

    Determime external Base T PHY interrupt cause

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param lsc:
        pointer to boolean flag which indicates whether external Base T
        PHY interrupt is lsc
    :type lsc: bool \*

.. _`ixgbe_get_lasi_ext_t_x550em.description`:

Description
-----------

Determime if external Base T PHY interrupt cause is high temperature
failure alarm or link status change.

Return IXGBE_ERR_OVERTEMP if interrupt is high temperature
failure alarm, else return PHY access status.

.. _`ixgbe_enable_lasi_ext_t_x550em`:

ixgbe_enable_lasi_ext_t_x550em
==============================

.. c:function:: s32 ixgbe_enable_lasi_ext_t_x550em(struct ixgbe_hw *hw)

    Enable external Base T PHY interrupts

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_enable_lasi_ext_t_x550em.description`:

Description
-----------

Enable link status change and temperature failure alarm for the external
Base T PHY

Returns PHY access status

.. _`ixgbe_handle_lasi_ext_t_x550em`:

ixgbe_handle_lasi_ext_t_x550em
==============================

.. c:function:: s32 ixgbe_handle_lasi_ext_t_x550em(struct ixgbe_hw *hw)

    Handle external Base T PHY interrupt

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_handle_lasi_ext_t_x550em.description`:

Description
-----------

Handle external Base T PHY interrupt. If high temperature
failure alarm then return error, else if link status change
then setup internal/external PHY link

Return IXGBE_ERR_OVERTEMP if interrupt is high temperature
failure alarm, else return PHY access status.

.. _`ixgbe_setup_kr_speed_x550em`:

ixgbe_setup_kr_speed_x550em
===========================

.. c:function:: s32 ixgbe_setup_kr_speed_x550em(struct ixgbe_hw *hw, ixgbe_link_speed speed)

    Configure the KR PHY for link speed.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param speed:
        link speed
    :type speed: ixgbe_link_speed

.. _`ixgbe_setup_kr_speed_x550em.description`:

Description
-----------

Configures the integrated KR PHY.

.. _`ixgbe_setup_kr_x550em`:

ixgbe_setup_kr_x550em
=====================

.. c:function:: s32 ixgbe_setup_kr_x550em(struct ixgbe_hw *hw)

    Configure the KR PHY

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_led_on_t_x550em`:

ixgbe_led_on_t_x550em
=====================

.. c:function:: s32 ixgbe_led_on_t_x550em(struct ixgbe_hw *hw, u32 led_idx)

    Turns on the software controllable LEDs.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param led_idx:
        led number to turn on
    :type led_idx: u32

.. _`ixgbe_led_off_t_x550em`:

ixgbe_led_off_t_x550em
======================

.. c:function:: s32 ixgbe_led_off_t_x550em(struct ixgbe_hw *hw, u32 led_idx)

    Turns off the software controllable LEDs.

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param led_idx:
        led number to turn off
    :type led_idx: u32

.. _`ixgbe_set_fw_drv_ver_x550`:

ixgbe_set_fw_drv_ver_x550
=========================

.. c:function:: s32 ixgbe_set_fw_drv_ver_x550(struct ixgbe_hw *hw, u8 maj, u8 min, u8 build, u8 sub, u16 len, const char *driver_ver)

    Sends driver version to firmware

    :param hw:
        pointer to the HW structure
    :type hw: struct ixgbe_hw \*

    :param maj:
        driver version major number
    :type maj: u8

    :param min:
        driver version minor number
    :type min: u8

    :param build:
        driver version build number
    :type build: u8

    :param sub:
        driver version sub build number
    :type sub: u8

    :param len:
        length of driver_ver string
    :type len: u16

    :param driver_ver:
        driver string
    :type driver_ver: const char \*

.. _`ixgbe_set_fw_drv_ver_x550.description`:

Description
-----------

Sends driver version number to firmware through the manageability
block.  On success return 0
else returns IXGBE_ERR_SWFW_SYNC when encountering an error acquiring
semaphore or IXGBE_ERR_HOST_INTERFACE_COMMAND when command fails.

.. _`ixgbe_setup_fc_x550em`:

ixgbe_setup_fc_x550em
=====================

.. c:function:: s32 ixgbe_setup_fc_x550em(struct ixgbe_hw *hw)

    Set up flow control

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_fc_autoneg_backplane_x550em_a`:

ixgbe_fc_autoneg_backplane_x550em_a
===================================

.. c:function:: void ixgbe_fc_autoneg_backplane_x550em_a(struct ixgbe_hw *hw)

    Enable flow control IEEE clause 37

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_fc_autoneg_fiber_x550em_a`:

ixgbe_fc_autoneg_fiber_x550em_a
===============================

.. c:function:: void ixgbe_fc_autoneg_fiber_x550em_a(struct ixgbe_hw *hw)

    passthrough FC settings

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_reset_phy_fw`:

ixgbe_reset_phy_fw
==================

.. c:function:: s32 ixgbe_reset_phy_fw(struct ixgbe_hw *hw)

    Reset firmware-controlled PHYs

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_check_overtemp_fw`:

ixgbe_check_overtemp_fw
=======================

.. c:function:: s32 ixgbe_check_overtemp_fw(struct ixgbe_hw *hw)

    Check firmware-controlled PHYs for overtemp

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_read_mng_if_sel_x550em`:

ixgbe_read_mng_if_sel_x550em
============================

.. c:function:: void ixgbe_read_mng_if_sel_x550em(struct ixgbe_hw *hw)

    Read NW_MNG_IF_SEL register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_read_mng_if_sel_x550em.description`:

Description
-----------

Read NW_MNG_IF_SEL register and save field values.

.. _`ixgbe_set_mdio_speed`:

ixgbe_set_mdio_speed
====================

.. c:function:: void ixgbe_set_mdio_speed(struct ixgbe_hw *hw)

    Set MDIO clock speed

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_setup_fc_backplane_x550em_a`:

ixgbe_setup_fc_backplane_x550em_a
=================================

.. c:function:: s32 ixgbe_setup_fc_backplane_x550em_a(struct ixgbe_hw *hw)

    Set up flow control

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

.. _`ixgbe_setup_fc_backplane_x550em_a.description`:

Description
-----------

Called at init time to set up flow control.

.. _`ixgbe_set_mux`:

ixgbe_set_mux
=============

.. c:function:: void ixgbe_set_mux(struct ixgbe_hw *hw, u8 state)

    Set mux for port 1 access with CS4227

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param state:
        set mux if 1, clear if 0
    :type state: u8

.. _`ixgbe_acquire_swfw_sync_x550em`:

ixgbe_acquire_swfw_sync_X550em
==============================

.. c:function:: s32 ixgbe_acquire_swfw_sync_X550em(struct ixgbe_hw *hw, u32 mask)

    Acquire SWFW semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param mask:
        Mask to specify which semaphore to acquire
    :type mask: u32

.. _`ixgbe_acquire_swfw_sync_x550em.description`:

Description
-----------

Acquires the SWFW semaphore and sets the I2C MUX

.. _`ixgbe_release_swfw_sync_x550em`:

ixgbe_release_swfw_sync_X550em
==============================

.. c:function:: void ixgbe_release_swfw_sync_X550em(struct ixgbe_hw *hw, u32 mask)

    Release SWFW semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param mask:
        Mask to specify which semaphore to release
    :type mask: u32

.. _`ixgbe_release_swfw_sync_x550em.description`:

Description
-----------

Releases the SWFW semaphore and sets the I2C MUX

.. _`ixgbe_acquire_swfw_sync_x550em_a`:

ixgbe_acquire_swfw_sync_x550em_a
================================

.. c:function:: s32 ixgbe_acquire_swfw_sync_x550em_a(struct ixgbe_hw *hw, u32 mask)

    Acquire SWFW semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param mask:
        Mask to specify which semaphore to acquire
    :type mask: u32

.. _`ixgbe_acquire_swfw_sync_x550em_a.description`:

Description
-----------

Acquires the SWFW semaphore and get the shared PHY token as needed

.. _`ixgbe_release_swfw_sync_x550em_a`:

ixgbe_release_swfw_sync_x550em_a
================================

.. c:function:: void ixgbe_release_swfw_sync_x550em_a(struct ixgbe_hw *hw, u32 mask)

    Release SWFW semaphore

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param mask:
        Mask to specify which semaphore to release
    :type mask: u32

.. _`ixgbe_release_swfw_sync_x550em_a.description`:

Description
-----------

Release the SWFW semaphore and puts the shared PHY token as needed

.. _`ixgbe_read_phy_reg_x550a`:

ixgbe_read_phy_reg_x550a
========================

.. c:function:: s32 ixgbe_read_phy_reg_x550a(struct ixgbe_hw *hw, u32 reg_addr, u32 device_type, u16 *phy_data)

    Reads specified PHY register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg_addr:
        32 bit address of PHY register to read
    :type reg_addr: u32

    :param device_type:
        5 bit device type
    :type device_type: u32

    :param phy_data:
        Pointer to read data from PHY register
    :type phy_data: u16 \*

.. _`ixgbe_read_phy_reg_x550a.description`:

Description
-----------

Reads a value from a specified PHY register using the SWFW lock and PHY
Token. The PHY Token is needed since the MDIO is shared between to MAC
instances.

.. _`ixgbe_write_phy_reg_x550a`:

ixgbe_write_phy_reg_x550a
=========================

.. c:function:: s32 ixgbe_write_phy_reg_x550a(struct ixgbe_hw *hw, u32 reg_addr, u32 device_type, u16 phy_data)

    Writes specified PHY register

    :param hw:
        pointer to hardware structure
    :type hw: struct ixgbe_hw \*

    :param reg_addr:
        32 bit PHY register to write
    :type reg_addr: u32

    :param device_type:
        5 bit device type
    :type device_type: u32

    :param phy_data:
        Data to write to the PHY register
    :type phy_data: u16

.. _`ixgbe_write_phy_reg_x550a.description`:

Description
-----------

Writes a value to specified PHY register using the SWFW lock and PHY Token.
The PHY Token is needed since the MDIO is shared between to MAC instances.

.. This file was automatic generated / don't edit.

