.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/e1000e/ich8lan.c

.. _`e1000_phy_is_accessible_pchlan`:

e1000_phy_is_accessible_pchlan
==============================

.. c:function:: bool e1000_phy_is_accessible_pchlan(struct e1000_hw *hw)

    Check if able to access PHY registers

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_phy_is_accessible_pchlan.description`:

Description
-----------

Test access to the PHY registers by reading the PHY ID registers.  If
the PHY ID is already known (e.g. resume path) compare it with known ID,
otherwise assume the read PHY ID is correct if it is valid.

Assumes the sw/fw/hw semaphore is already acquired.

.. _`e1000_toggle_lanphypc_pch_lpt`:

e1000_toggle_lanphypc_pch_lpt
=============================

.. c:function:: void e1000_toggle_lanphypc_pch_lpt(struct e1000_hw *hw)

    toggle the LANPHYPC pin value

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_toggle_lanphypc_pch_lpt.description`:

Description
-----------

Toggling the LANPHYPC pin value fully power-cycles the PHY and is
used to reset the PHY to a quiescent state when necessary.

.. _`e1000_init_phy_workarounds_pchlan`:

e1000_init_phy_workarounds_pchlan
=================================

.. c:function:: s32 e1000_init_phy_workarounds_pchlan(struct e1000_hw *hw)

    PHY initialization workarounds

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_init_phy_workarounds_pchlan.description`:

Description
-----------

Workarounds/flow necessary for PHY initialization during driver load
and resume paths.

.. _`e1000_init_phy_params_pchlan`:

e1000_init_phy_params_pchlan
============================

.. c:function:: s32 e1000_init_phy_params_pchlan(struct e1000_hw *hw)

    Initialize PHY function pointers

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_init_phy_params_pchlan.description`:

Description
-----------

Initialize family-specific PHY parameters and function pointers.

.. _`e1000_init_phy_params_ich8lan`:

e1000_init_phy_params_ich8lan
=============================

.. c:function:: s32 e1000_init_phy_params_ich8lan(struct e1000_hw *hw)

    Initialize PHY function pointers

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_init_phy_params_ich8lan.description`:

Description
-----------

Initialize family-specific PHY parameters and function pointers.

.. _`e1000_init_nvm_params_ich8lan`:

e1000_init_nvm_params_ich8lan
=============================

.. c:function:: s32 e1000_init_nvm_params_ich8lan(struct e1000_hw *hw)

    Initialize NVM function pointers

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_init_nvm_params_ich8lan.description`:

Description
-----------

Initialize family-specific NVM parameters and function
pointers.

.. _`e1000_init_mac_params_ich8lan`:

e1000_init_mac_params_ich8lan
=============================

.. c:function:: s32 e1000_init_mac_params_ich8lan(struct e1000_hw *hw)

    Initialize MAC function pointers

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_init_mac_params_ich8lan.description`:

Description
-----------

Initialize family-specific MAC parameters and function
pointers.

.. _`__e1000_access_emi_reg_locked`:

\__e1000_access_emi_reg_locked
==============================

.. c:function:: s32 __e1000_access_emi_reg_locked(struct e1000_hw *hw, u16 address, u16 *data, bool read)

    Read/write EMI register

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param address:
        *undescribed*
    :type address: u16

    :param data:
        pointer to value to read/write from/to the EMI address
    :type data: u16 \*

    :param read:
        boolean flag to indicate read or write
    :type read: bool

.. _`__e1000_access_emi_reg_locked.description`:

Description
-----------

This helper function assumes the SW/FW/HW Semaphore is already acquired.

.. _`e1000_read_emi_reg_locked`:

e1000_read_emi_reg_locked
=========================

.. c:function:: s32 e1000_read_emi_reg_locked(struct e1000_hw *hw, u16 addr, u16 *data)

    Read Extended Management Interface register

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param addr:
        EMI address to program
    :type addr: u16

    :param data:
        value to be read from the EMI address
    :type data: u16 \*

.. _`e1000_read_emi_reg_locked.description`:

Description
-----------

Assumes the SW/FW/HW Semaphore is already acquired.

.. _`e1000_write_emi_reg_locked`:

e1000_write_emi_reg_locked
==========================

.. c:function:: s32 e1000_write_emi_reg_locked(struct e1000_hw *hw, u16 addr, u16 data)

    Write Extended Management Interface register

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param addr:
        EMI address to program
    :type addr: u16

    :param data:
        value to be written to the EMI address
    :type data: u16

.. _`e1000_write_emi_reg_locked.description`:

Description
-----------

Assumes the SW/FW/HW Semaphore is already acquired.

.. _`e1000_set_eee_pchlan`:

e1000_set_eee_pchlan
====================

.. c:function:: s32 e1000_set_eee_pchlan(struct e1000_hw *hw)

    Enable/disable EEE support

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_set_eee_pchlan.description`:

Description
-----------

Enable/disable EEE based on setting in dev_spec structure, the duplex of
the link and the EEE capabilities of the link partner.  The LPI Control
register bits will remain set only if/when link is up.

EEE LPI must not be asserted earlier than one second after link is up.
On 82579, EEE LPI should not be enabled until such time otherwise there
can be link issues with some switches.  Other devices can have EEE LPI
enabled immediately upon link up since they have a timer in hardware which
prevents LPI from being asserted too early.

.. _`e1000_k1_workaround_lpt_lp`:

e1000_k1_workaround_lpt_lp
==========================

.. c:function:: s32 e1000_k1_workaround_lpt_lp(struct e1000_hw *hw, bool link)

    K1 workaround on Lynxpoint-LP

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param link:
        link up bool flag
    :type link: bool

.. _`e1000_k1_workaround_lpt_lp.description`:

Description
-----------

When K1 is enabled for 1Gbps, the MAC can miss 2 DMA completion indications
preventing further DMA write requests.  Workaround the issue by disabling
the de-assertion of the clock request when in 1Gpbs mode.
Also, set appropriate Tx re-transmission timeouts for 10 and 100Half link
speeds in order to avoid Tx hangs.

.. _`e1000_platform_pm_pch_lpt`:

e1000_platform_pm_pch_lpt
=========================

.. c:function:: s32 e1000_platform_pm_pch_lpt(struct e1000_hw *hw, bool link)

    Set platform power management values

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param link:
        bool indicating link status
    :type link: bool

.. _`e1000_platform_pm_pch_lpt.description`:

Description
-----------

Set the Latency Tolerance Reporting (LTR) values for the "PCIe-like"
GbE MAC in the Lynx Point PCH based on Rx buffer size and link speed
when link is up (which must not exceed the maximum latency supported
by the platform), otherwise specify there is no LTR requirement.
Unlike true-PCIe devices which set the LTR maximum snoop/no-snoop
latencies in the LTR Extended Capability Structure in the PCIe Extended
Capability register set, on this device LTR is set by writing the
equivalent snoop/no-snoop latencies in the LTRV register in the MAC and
set the SEND bit to send an Intel On-chip System Fabric sideband (IOSF-SB)
message to the PMC.

.. _`e1000_enable_ulp_lpt_lp`:

e1000_enable_ulp_lpt_lp
=======================

.. c:function:: s32 e1000_enable_ulp_lpt_lp(struct e1000_hw *hw, bool to_sx)

    configure Ultra Low Power mode for LynxPoint-LP

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param to_sx:
        boolean indicating a system power state transition to Sx
    :type to_sx: bool

.. _`e1000_enable_ulp_lpt_lp.description`:

Description
-----------

When link is down, configure ULP mode to significantly reduce the power
to the PHY.  If on a Manageability Engine (ME) enabled system, tell the
ME firmware to start the ULP configuration.  If not on an ME enabled
system, configure the ULP mode by software.

.. _`e1000_disable_ulp_lpt_lp`:

e1000_disable_ulp_lpt_lp
========================

.. c:function:: s32 e1000_disable_ulp_lpt_lp(struct e1000_hw *hw, bool force)

    unconfigure Ultra Low Power mode for LynxPoint-LP

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param force:
        boolean indicating whether or not to force disabling ULP
    :type force: bool

.. _`e1000_disable_ulp_lpt_lp.description`:

Description
-----------

Un-configure ULP mode when link is up, the system is transitioned from
Sx or the driver is unloaded.  If on a Manageability Engine (ME) enabled
system, poll for an indication from ME that ULP has been un-configured.
If not on an ME enabled system, un-configure the ULP mode by software.

During nominal operation, this function is called when link is acquired
to disable ULP mode (force=false); otherwise, for example when unloading
the driver or during Sx->S0 transitions, this is called with force=true
to forcibly disable ULP.

.. _`e1000_check_for_copper_link_ich8lan`:

e1000_check_for_copper_link_ich8lan
===================================

.. c:function:: s32 e1000_check_for_copper_link_ich8lan(struct e1000_hw *hw)

    Check for link (Copper)

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_check_for_copper_link_ich8lan.description`:

Description
-----------

Checks to see of the link status of the hardware has changed.  If a
change in link status has been detected, then we read the PHY registers
to get the current speed/duplex if link exists.

.. _`e1000_acquire_nvm_ich8lan`:

e1000_acquire_nvm_ich8lan
=========================

.. c:function:: s32 e1000_acquire_nvm_ich8lan(struct e1000_hw __always_unused *hw)

    Acquire NVM mutex

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw __always_unused \*

.. _`e1000_acquire_nvm_ich8lan.description`:

Description
-----------

Acquires the mutex for performing NVM operations.

.. _`e1000_release_nvm_ich8lan`:

e1000_release_nvm_ich8lan
=========================

.. c:function:: void e1000_release_nvm_ich8lan(struct e1000_hw __always_unused *hw)

    Release NVM mutex

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw __always_unused \*

.. _`e1000_release_nvm_ich8lan.description`:

Description
-----------

Releases the mutex used while performing NVM operations.

.. _`e1000_acquire_swflag_ich8lan`:

e1000_acquire_swflag_ich8lan
============================

.. c:function:: s32 e1000_acquire_swflag_ich8lan(struct e1000_hw *hw)

    Acquire software control flag

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_acquire_swflag_ich8lan.description`:

Description
-----------

Acquires the software control flag for performing PHY and select
MAC CSR accesses.

.. _`e1000_release_swflag_ich8lan`:

e1000_release_swflag_ich8lan
============================

.. c:function:: void e1000_release_swflag_ich8lan(struct e1000_hw *hw)

    Release software control flag

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_release_swflag_ich8lan.description`:

Description
-----------

Releases the software control flag for performing PHY and select
MAC CSR accesses.

.. _`e1000_check_mng_mode_ich8lan`:

e1000_check_mng_mode_ich8lan
============================

.. c:function:: bool e1000_check_mng_mode_ich8lan(struct e1000_hw *hw)

    Checks management mode

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_check_mng_mode_ich8lan.description`:

Description
-----------

This checks if the adapter has any manageability enabled.
This is a function pointer entry point only called by read/write
routines for the PHY and NVM parts.

.. _`e1000_check_mng_mode_pchlan`:

e1000_check_mng_mode_pchlan
===========================

.. c:function:: bool e1000_check_mng_mode_pchlan(struct e1000_hw *hw)

    Checks management mode

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_check_mng_mode_pchlan.description`:

Description
-----------

This checks if the adapter has iAMT enabled.
This is a function pointer entry point only called by read/write
routines for the PHY and NVM parts.

.. _`e1000_rar_set_pch2lan`:

e1000_rar_set_pch2lan
=====================

.. c:function:: int e1000_rar_set_pch2lan(struct e1000_hw *hw, u8 *addr, u32 index)

    Set receive address register

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param addr:
        pointer to the receive address
    :type addr: u8 \*

    :param index:
        receive address array register
    :type index: u32

.. _`e1000_rar_set_pch2lan.description`:

Description
-----------

Sets the receive address array register at index to the address passed
in by addr.  For 82579, RAR[0] is the base address register that is to
contain the MAC address but RAR[1-6] are reserved for manageability (ME).
Use SHRA[0-3] in place of those reserved for ME.

.. _`e1000_rar_get_count_pch_lpt`:

e1000_rar_get_count_pch_lpt
===========================

.. c:function:: u32 e1000_rar_get_count_pch_lpt(struct e1000_hw *hw)

    Get the number of available SHRA

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_rar_get_count_pch_lpt.description`:

Description
-----------

Get the number of available receive registers that the Host can
program. SHRA[0-10] are the shared receive address registers
that are shared between the Host and manageability engine (ME).
ME can reserve any number of addresses and the host needs to be
able to tell how many available registers it has access to.

.. _`e1000_rar_set_pch_lpt`:

e1000_rar_set_pch_lpt
=====================

.. c:function:: int e1000_rar_set_pch_lpt(struct e1000_hw *hw, u8 *addr, u32 index)

    Set receive address registers

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param addr:
        pointer to the receive address
    :type addr: u8 \*

    :param index:
        receive address array register
    :type index: u32

.. _`e1000_rar_set_pch_lpt.description`:

Description
-----------

Sets the receive address register array at index to the address passed
in by addr. For LPT, RAR[0] is the base address register that is to
contain the MAC address. SHRA[0-10] are the shared receive address
registers that are shared between the Host and manageability engine (ME).

.. _`e1000_check_reset_block_ich8lan`:

e1000_check_reset_block_ich8lan
===============================

.. c:function:: s32 e1000_check_reset_block_ich8lan(struct e1000_hw *hw)

    Check if PHY reset is blocked

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_check_reset_block_ich8lan.description`:

Description
-----------

Checks if firmware is blocking the reset of the PHY.
This is a function pointer entry point only called by
reset routines.

.. _`e1000_write_smbus_addr`:

e1000_write_smbus_addr
======================

.. c:function:: s32 e1000_write_smbus_addr(struct e1000_hw *hw)

    Write SMBus address to PHY needed during Sx states

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_write_smbus_addr.description`:

Description
-----------

Assumes semaphore already acquired.

.. _`e1000_sw_lcd_config_ich8lan`:

e1000_sw_lcd_config_ich8lan
===========================

.. c:function:: s32 e1000_sw_lcd_config_ich8lan(struct e1000_hw *hw)

    SW-based LCD Configuration

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_sw_lcd_config_ich8lan.description`:

Description
-----------

SW should configure the LCD from the NVM extended configuration region
as a workaround for certain parts.

.. _`e1000_k1_gig_workaround_hv`:

e1000_k1_gig_workaround_hv
==========================

.. c:function:: s32 e1000_k1_gig_workaround_hv(struct e1000_hw *hw, bool link)

    K1 Si workaround

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param link:
        link up bool flag
    :type link: bool

.. _`e1000_k1_gig_workaround_hv.description`:

Description
-----------

If K1 is enabled for 1Gbps, the MAC might stall when transitioning
from a lower speed.  This workaround disables K1 whenever link is at 1Gig
If link is down, the function will restore the default K1 setting located
in the NVM.

.. _`e1000_configure_k1_ich8lan`:

e1000_configure_k1_ich8lan
==========================

.. c:function:: s32 e1000_configure_k1_ich8lan(struct e1000_hw *hw, bool k1_enable)

    Configure K1 power state

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param k1_enable:
        *undescribed*
    :type k1_enable: bool

.. _`e1000_configure_k1_ich8lan.description`:

Description
-----------

Configure the K1 power state based on the provided parameter.
Assumes semaphore already acquired.

Success returns 0, Failure returns -E1000_ERR_PHY (-2)

.. _`e1000_oem_bits_config_ich8lan`:

e1000_oem_bits_config_ich8lan
=============================

.. c:function:: s32 e1000_oem_bits_config_ich8lan(struct e1000_hw *hw, bool d0_state)

    SW-based LCD Configuration

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param d0_state:
        boolean if entering d0 or d3 device state
    :type d0_state: bool

.. _`e1000_oem_bits_config_ich8lan.description`:

Description
-----------

SW will configure Gbe Disable and LPLU based on the NVM. The four bits are
collectively called OEM bits.  The OEM Write Enable bit and SW Config bit
in NVM determines whether HW should configure LPLU and Gbe Disable.

.. _`e1000_set_mdio_slow_mode_hv`:

e1000_set_mdio_slow_mode_hv
===========================

.. c:function:: s32 e1000_set_mdio_slow_mode_hv(struct e1000_hw *hw)

    Set slow MDIO access mode

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_hv_phy_workarounds_ich8lan`:

e1000_hv_phy_workarounds_ich8lan
================================

.. c:function:: s32 e1000_hv_phy_workarounds_ich8lan(struct e1000_hw *hw)

    A series of Phy workarounds to be done after every PHY reset.

    :param hw:
        *undescribed*
    :type hw: struct e1000_hw \*

.. _`e1000_copy_rx_addrs_to_phy_ich8lan`:

e1000_copy_rx_addrs_to_phy_ich8lan
==================================

.. c:function:: void e1000_copy_rx_addrs_to_phy_ich8lan(struct e1000_hw *hw)

    Copy Rx addresses from MAC to PHY

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_lv_jumbo_workaround_ich8lan`:

e1000_lv_jumbo_workaround_ich8lan
=================================

.. c:function:: s32 e1000_lv_jumbo_workaround_ich8lan(struct e1000_hw *hw, bool enable)

    required for jumbo frame operation with 82579 PHY

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param enable:
        flag to enable/disable workaround when enabling/disabling jumbos
    :type enable: bool

.. _`e1000_lv_phy_workarounds_ich8lan`:

e1000_lv_phy_workarounds_ich8lan
================================

.. c:function:: s32 e1000_lv_phy_workarounds_ich8lan(struct e1000_hw *hw)

    A series of Phy workarounds to be done after every PHY reset.

    :param hw:
        *undescribed*
    :type hw: struct e1000_hw \*

.. _`e1000_k1_workaround_lv`:

e1000_k1_workaround_lv
======================

.. c:function:: s32 e1000_k1_workaround_lv(struct e1000_hw *hw)

    K1 Si workaround

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_k1_workaround_lv.description`:

Description
-----------

Workaround to set the K1 beacon duration for 82579 parts in 10Mbps
Disable K1 in 1000Mbps and 100Mbps

.. _`e1000_gate_hw_phy_config_ich8lan`:

e1000_gate_hw_phy_config_ich8lan
================================

.. c:function:: void e1000_gate_hw_phy_config_ich8lan(struct e1000_hw *hw, bool gate)

    disable PHY config via hardware

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param gate:
        boolean set to true to gate, false to ungate
    :type gate: bool

.. _`e1000_gate_hw_phy_config_ich8lan.description`:

Description
-----------

Gate/ungate the automatic PHY configuration via hardware; perform
the configuration via software instead.

.. _`e1000_lan_init_done_ich8lan`:

e1000_lan_init_done_ich8lan
===========================

.. c:function:: void e1000_lan_init_done_ich8lan(struct e1000_hw *hw)

    Check for PHY config completion

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_lan_init_done_ich8lan.description`:

Description
-----------

Check the appropriate indication the MAC has finished configuring the
PHY after a software reset.

.. _`e1000_post_phy_reset_ich8lan`:

e1000_post_phy_reset_ich8lan
============================

.. c:function:: s32 e1000_post_phy_reset_ich8lan(struct e1000_hw *hw)

    Perform steps required after a PHY reset

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_phy_hw_reset_ich8lan`:

e1000_phy_hw_reset_ich8lan
==========================

.. c:function:: s32 e1000_phy_hw_reset_ich8lan(struct e1000_hw *hw)

    Performs a PHY reset

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_phy_hw_reset_ich8lan.description`:

Description
-----------

Resets the PHY
This is a function pointer entry point called by drivers
or other shared routines.

.. _`e1000_set_lplu_state_pchlan`:

e1000_set_lplu_state_pchlan
===========================

.. c:function:: s32 e1000_set_lplu_state_pchlan(struct e1000_hw *hw, bool active)

    Set Low Power Link Up state

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param active:
        true to enable LPLU, false to disable
    :type active: bool

.. _`e1000_set_lplu_state_pchlan.description`:

Description
-----------

Sets the LPLU state according to the active flag.  For PCH, if OEM write
bit are disabled in the NVM, writing the LPLU bits in the MAC will not set
the phy speed. This function will manually set the LPLU bit and restart
auto-neg as hw would do. D3 and D0 LPLU will call the same function
since it configures the same bit.

.. _`e1000_set_d0_lplu_state_ich8lan`:

e1000_set_d0_lplu_state_ich8lan
===============================

.. c:function:: s32 e1000_set_d0_lplu_state_ich8lan(struct e1000_hw *hw, bool active)

    Set Low Power Linkup D0 state

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param active:
        true to enable LPLU, false to disable
    :type active: bool

.. _`e1000_set_d0_lplu_state_ich8lan.description`:

Description
-----------

Sets the LPLU D0 state according to the active flag.  When
activating LPLU this function also disables smart speed
and vice versa.  LPLU will not be activated unless the
device autonegotiation advertisement meets standards of
either 10 or 10/100 or 10/100/1000 at all duplexes.
This is a function pointer entry point only called by
PHY setup routines.

.. _`e1000_set_d3_lplu_state_ich8lan`:

e1000_set_d3_lplu_state_ich8lan
===============================

.. c:function:: s32 e1000_set_d3_lplu_state_ich8lan(struct e1000_hw *hw, bool active)

    Set Low Power Linkup D3 state

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param active:
        true to enable LPLU, false to disable
    :type active: bool

.. _`e1000_set_d3_lplu_state_ich8lan.description`:

Description
-----------

Sets the LPLU D3 state according to the active flag.  When
activating LPLU this function also disables smart speed
and vice versa.  LPLU will not be activated unless the
device autonegotiation advertisement meets standards of
either 10 or 10/100 or 10/100/1000 at all duplexes.
This is a function pointer entry point only called by
PHY setup routines.

.. _`e1000_valid_nvm_bank_detect_ich8lan`:

e1000_valid_nvm_bank_detect_ich8lan
===================================

.. c:function:: s32 e1000_valid_nvm_bank_detect_ich8lan(struct e1000_hw *hw, u32 *bank)

    finds out the valid bank 0 or 1

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param bank:
        pointer to the variable that returns the active bank
    :type bank: u32 \*

.. _`e1000_valid_nvm_bank_detect_ich8lan.description`:

Description
-----------

Reads signature byte from the NVM using the flash access registers.
Word 0x13 bits 15:14 = 10b indicate a valid signature for that bank.

.. _`e1000_read_nvm_spt`:

e1000_read_nvm_spt
==================

.. c:function:: s32 e1000_read_nvm_spt(struct e1000_hw *hw, u16 offset, u16 words, u16 *data)

    NVM access for SPT

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset (in bytes) of the word(s) to read.
    :type offset: u16

    :param words:
        Size of data to read in words.
    :type words: u16

    :param data:
        pointer to the word(s) to read at offset.
    :type data: u16 \*

.. _`e1000_read_nvm_spt.description`:

Description
-----------

Reads a word(s) from the NVM

.. _`e1000_read_nvm_ich8lan`:

e1000_read_nvm_ich8lan
======================

.. c:function:: s32 e1000_read_nvm_ich8lan(struct e1000_hw *hw, u16 offset, u16 words, u16 *data)

    Read word(s) from the NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset (in bytes) of the word(s) to read.
    :type offset: u16

    :param words:
        Size of data to read in words
    :type words: u16

    :param data:
        Pointer to the word(s) to read at offset.
    :type data: u16 \*

.. _`e1000_read_nvm_ich8lan.description`:

Description
-----------

Reads a word(s) from the NVM using the flash access registers.

.. _`e1000_flash_cycle_init_ich8lan`:

e1000_flash_cycle_init_ich8lan
==============================

.. c:function:: s32 e1000_flash_cycle_init_ich8lan(struct e1000_hw *hw)

    Initialize flash

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_flash_cycle_init_ich8lan.description`:

Description
-----------

This function does initial flash setup so that a new read/write/erase cycle
can be started.

.. _`e1000_flash_cycle_ich8lan`:

e1000_flash_cycle_ich8lan
=========================

.. c:function:: s32 e1000_flash_cycle_ich8lan(struct e1000_hw *hw, u32 timeout)

    Starts flash cycle (read/write/erase)

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param timeout:
        maximum time to wait for completion
    :type timeout: u32

.. _`e1000_flash_cycle_ich8lan.description`:

Description
-----------

This function starts a flash cycle and waits for its completion.

.. _`e1000_read_flash_dword_ich8lan`:

e1000_read_flash_dword_ich8lan
==============================

.. c:function:: s32 e1000_read_flash_dword_ich8lan(struct e1000_hw *hw, u32 offset, u32 *data)

    Read dword from flash

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        offset to data location
    :type offset: u32

    :param data:
        pointer to the location for storing the data
    :type data: u32 \*

.. _`e1000_read_flash_dword_ich8lan.description`:

Description
-----------

Reads the flash dword at offset into data.  Offset is converted
to bytes before read.

.. _`e1000_read_flash_word_ich8lan`:

e1000_read_flash_word_ich8lan
=============================

.. c:function:: s32 e1000_read_flash_word_ich8lan(struct e1000_hw *hw, u32 offset, u16 *data)

    Read word from flash

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        offset to data location
    :type offset: u32

    :param data:
        pointer to the location for storing the data
    :type data: u16 \*

.. _`e1000_read_flash_word_ich8lan.description`:

Description
-----------

Reads the flash word at offset into data.  Offset is converted
to bytes before read.

.. _`e1000_read_flash_byte_ich8lan`:

e1000_read_flash_byte_ich8lan
=============================

.. c:function:: s32 e1000_read_flash_byte_ich8lan(struct e1000_hw *hw, u32 offset, u8 *data)

    Read byte from flash

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset of the byte to read.
    :type offset: u32

    :param data:
        Pointer to a byte to store the value read.
    :type data: u8 \*

.. _`e1000_read_flash_byte_ich8lan.description`:

Description
-----------

Reads a single byte from the NVM using the flash access registers.

.. _`e1000_read_flash_data_ich8lan`:

e1000_read_flash_data_ich8lan
=============================

.. c:function:: s32 e1000_read_flash_data_ich8lan(struct e1000_hw *hw, u32 offset, u8 size, u16 *data)

    Read byte or word from NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset (in bytes) of the byte or word to read.
    :type offset: u32

    :param size:
        Size of data to read, 1=byte 2=word
    :type size: u8

    :param data:
        Pointer to the word to store the value read.
    :type data: u16 \*

.. _`e1000_read_flash_data_ich8lan.description`:

Description
-----------

Reads a byte or word from the NVM using the flash access registers.

.. _`e1000_read_flash_data32_ich8lan`:

e1000_read_flash_data32_ich8lan
===============================

.. c:function:: s32 e1000_read_flash_data32_ich8lan(struct e1000_hw *hw, u32 offset, u32 *data)

    Read dword from NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset (in bytes) of the dword to read.
    :type offset: u32

    :param data:
        Pointer to the dword to store the value read.
    :type data: u32 \*

.. _`e1000_read_flash_data32_ich8lan.description`:

Description
-----------

Reads a byte or word from the NVM using the flash access registers.

.. _`e1000_write_nvm_ich8lan`:

e1000_write_nvm_ich8lan
=======================

.. c:function:: s32 e1000_write_nvm_ich8lan(struct e1000_hw *hw, u16 offset, u16 words, u16 *data)

    Write word(s) to the NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset (in bytes) of the word(s) to write.
    :type offset: u16

    :param words:
        Size of data to write in words
    :type words: u16

    :param data:
        Pointer to the word(s) to write at offset.
    :type data: u16 \*

.. _`e1000_write_nvm_ich8lan.description`:

Description
-----------

Writes a byte or word to the NVM using the flash access registers.

.. _`e1000_update_nvm_checksum_spt`:

e1000_update_nvm_checksum_spt
=============================

.. c:function:: s32 e1000_update_nvm_checksum_spt(struct e1000_hw *hw)

    Update the checksum for NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_update_nvm_checksum_spt.description`:

Description
-----------

The NVM checksum is updated by calling the generic update_nvm_checksum,
which writes the checksum to the shadow ram.  The changes in the shadow
ram are then committed to the EEPROM by processing each bank at a time
checking for the modified bit and writing only the pending changes.
After a successful commit, the shadow ram is cleared and is ready for
future writes.

.. _`e1000_update_nvm_checksum_ich8lan`:

e1000_update_nvm_checksum_ich8lan
=================================

.. c:function:: s32 e1000_update_nvm_checksum_ich8lan(struct e1000_hw *hw)

    Update the checksum for NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_update_nvm_checksum_ich8lan.description`:

Description
-----------

The NVM checksum is updated by calling the generic update_nvm_checksum,
which writes the checksum to the shadow ram.  The changes in the shadow
ram are then committed to the EEPROM by processing each bank at a time
checking for the modified bit and writing only the pending changes.
After a successful commit, the shadow ram is cleared and is ready for
future writes.

.. _`e1000_validate_nvm_checksum_ich8lan`:

e1000_validate_nvm_checksum_ich8lan
===================================

.. c:function:: s32 e1000_validate_nvm_checksum_ich8lan(struct e1000_hw *hw)

    Validate EEPROM checksum

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_validate_nvm_checksum_ich8lan.description`:

Description
-----------

Check to see if checksum needs to be fixed by reading bit 6 in word 0x19.
If the bit is 0, that the EEPROM had been modified, but the checksum was not
calculated, in which case we need to calculate the checksum and set bit 6.

.. _`e1000e_write_protect_nvm_ich8lan`:

e1000e_write_protect_nvm_ich8lan
================================

.. c:function:: void e1000e_write_protect_nvm_ich8lan(struct e1000_hw *hw)

    Make the NVM read-only

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000e_write_protect_nvm_ich8lan.description`:

Description
-----------

To prevent malicious write/erase of the NVM, set it to be read-only
so that the hardware ignores all write/erase cycles of the NVM via
the flash control registers.  The shadow-ram copy of the NVM will
still be updated, however any updates to this copy will not stick
across driver reloads.

.. _`e1000_write_flash_data_ich8lan`:

e1000_write_flash_data_ich8lan
==============================

.. c:function:: s32 e1000_write_flash_data_ich8lan(struct e1000_hw *hw, u32 offset, u8 size, u16 data)

    Writes bytes to the NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset (in bytes) of the byte/word to read.
    :type offset: u32

    :param size:
        Size of data to read, 1=byte 2=word
    :type size: u8

    :param data:
        The byte(s) to write to the NVM.
    :type data: u16

.. _`e1000_write_flash_data_ich8lan.description`:

Description
-----------

Writes one/two bytes to the NVM using the flash access registers.

.. _`e1000_write_flash_data32_ich8lan`:

e1000_write_flash_data32_ich8lan
================================

.. c:function:: s32 e1000_write_flash_data32_ich8lan(struct e1000_hw *hw, u32 offset, u32 data)

    Writes 4 bytes to the NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset (in bytes) of the dwords to read.
    :type offset: u32

    :param data:
        The 4 bytes to write to the NVM.
    :type data: u32

.. _`e1000_write_flash_data32_ich8lan.description`:

Description
-----------

Writes one/two/four bytes to the NVM using the flash access registers.

.. _`e1000_write_flash_byte_ich8lan`:

e1000_write_flash_byte_ich8lan
==============================

.. c:function:: s32 e1000_write_flash_byte_ich8lan(struct e1000_hw *hw, u32 offset, u8 data)

    Write a single byte to NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The index of the byte to read.
    :type offset: u32

    :param data:
        The byte to write to the NVM.
    :type data: u8

.. _`e1000_write_flash_byte_ich8lan.description`:

Description
-----------

Writes a single byte to the NVM using the flash access registers.

.. _`e1000_retry_write_flash_dword_ich8lan`:

e1000_retry_write_flash_dword_ich8lan
=====================================

.. c:function:: s32 e1000_retry_write_flash_dword_ich8lan(struct e1000_hw *hw, u32 offset, u32 dword)

    Writes a dword to NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset of the word to write.
    :type offset: u32

    :param dword:
        The dword to write to the NVM.
    :type dword: u32

.. _`e1000_retry_write_flash_dword_ich8lan.description`:

Description
-----------

Writes a single dword to the NVM using the flash access registers.
Goes through a retry algorithm before giving up.

.. _`e1000_retry_write_flash_byte_ich8lan`:

e1000_retry_write_flash_byte_ich8lan
====================================

.. c:function:: s32 e1000_retry_write_flash_byte_ich8lan(struct e1000_hw *hw, u32 offset, u8 byte)

    Writes a single byte to NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param offset:
        The offset of the byte to write.
    :type offset: u32

    :param byte:
        The byte to write to the NVM.
    :type byte: u8

.. _`e1000_retry_write_flash_byte_ich8lan.description`:

Description
-----------

Writes a single byte to the NVM using the flash access registers.
Goes through a retry algorithm before giving up.

.. _`e1000_erase_flash_bank_ich8lan`:

e1000_erase_flash_bank_ich8lan
==============================

.. c:function:: s32 e1000_erase_flash_bank_ich8lan(struct e1000_hw *hw, u32 bank)

    Erase a bank (4k) from NVM

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param bank:
        0 for first bank, 1 for second bank, etc.
    :type bank: u32

.. _`e1000_erase_flash_bank_ich8lan.description`:

Description
-----------

Erases the bank specified. Each bank is a 4k block. Banks are 0 based.
bank N is 4096 \* N + flash_reg_addr.

.. _`e1000_valid_led_default_ich8lan`:

e1000_valid_led_default_ich8lan
===============================

.. c:function:: s32 e1000_valid_led_default_ich8lan(struct e1000_hw *hw, u16 *data)

    Set the default LED settings

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param data:
        Pointer to the LED settings
    :type data: u16 \*

.. _`e1000_valid_led_default_ich8lan.description`:

Description
-----------

Reads the LED default settings from the NVM to data.  If the NVM LED
settings is all 0's or F's, set the LED default to a valid LED default
setting.

.. _`e1000_id_led_init_pchlan`:

e1000_id_led_init_pchlan
========================

.. c:function:: s32 e1000_id_led_init_pchlan(struct e1000_hw *hw)

    store LED configurations

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_id_led_init_pchlan.description`:

Description
-----------

PCH does not control LEDs via the LEDCTL register, rather it uses
the PHY LED configuration register.

PCH also does not have an "always on" or "always off" mode which
complicates the ID feature.  Instead of using the "on" mode to indicate
in ledctl_mode2 the LEDs to use for ID (see \ :c:func:`e1000e_id_led_init_generic`\ ),
use "link_up" mode.  The LEDs will still ID on request if there is no
link based on logic in e1000_led_[on\|off]_pchlan().

.. _`e1000_get_bus_info_ich8lan`:

e1000_get_bus_info_ich8lan
==========================

.. c:function:: s32 e1000_get_bus_info_ich8lan(struct e1000_hw *hw)

    Get/Set the bus type and width

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_get_bus_info_ich8lan.description`:

Description
-----------

ICH8 use the PCI Express bus, but does not contain a PCI Express Capability
register, so the the bus width is hard coded.

.. _`e1000_reset_hw_ich8lan`:

e1000_reset_hw_ich8lan
======================

.. c:function:: s32 e1000_reset_hw_ich8lan(struct e1000_hw *hw)

    Reset the hardware

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_reset_hw_ich8lan.description`:

Description
-----------

Does a full reset of the hardware which includes a reset of the PHY and
MAC.

.. _`e1000_init_hw_ich8lan`:

e1000_init_hw_ich8lan
=====================

.. c:function:: s32 e1000_init_hw_ich8lan(struct e1000_hw *hw)

    Initialize the hardware

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_init_hw_ich8lan.prepares-the-hardware-for-transmit-and-receive-by-doing-the-following`:

Prepares the hardware for transmit and receive by doing the following
---------------------------------------------------------------------

- initialize hardware bits
- initialize LED identification
- setup receive address registers
- setup flow control
- setup transmit descriptors
- clear statistics

.. _`e1000_initialize_hw_bits_ich8lan`:

e1000_initialize_hw_bits_ich8lan
================================

.. c:function:: void e1000_initialize_hw_bits_ich8lan(struct e1000_hw *hw)

    Initialize required hardware bits

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_initialize_hw_bits_ich8lan.description`:

Description
-----------

Sets/Clears required hardware bits necessary for correctly setting up the
hardware for transmit and receive.

.. _`e1000_setup_link_ich8lan`:

e1000_setup_link_ich8lan
========================

.. c:function:: s32 e1000_setup_link_ich8lan(struct e1000_hw *hw)

    Setup flow control and link settings

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_setup_link_ich8lan.description`:

Description
-----------

Determines which flow control settings to use, then configures flow
control.  Calls the appropriate media-specific link configuration
function.  Assuming the adapter has a valid link partner, a valid link
should be established.  Assumes the hardware has previously been reset
and the transmitter and receiver are not enabled.

.. _`e1000_setup_copper_link_ich8lan`:

e1000_setup_copper_link_ich8lan
===============================

.. c:function:: s32 e1000_setup_copper_link_ich8lan(struct e1000_hw *hw)

    Configure MAC/PHY interface

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_setup_copper_link_ich8lan.description`:

Description
-----------

Configures the kumeran interface to the PHY to wait the appropriate time
when polling the PHY, then call the generic setup_copper_link to finish
configuring the copper link.

.. _`e1000_setup_copper_link_pch_lpt`:

e1000_setup_copper_link_pch_lpt
===============================

.. c:function:: s32 e1000_setup_copper_link_pch_lpt(struct e1000_hw *hw)

    Configure MAC/PHY interface

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_setup_copper_link_pch_lpt.description`:

Description
-----------

Calls the PHY specific link setup function and then calls the
generic setup_copper_link to finish configuring the link for
Lynxpoint PCH devices

.. _`e1000_get_link_up_info_ich8lan`:

e1000_get_link_up_info_ich8lan
==============================

.. c:function:: s32 e1000_get_link_up_info_ich8lan(struct e1000_hw *hw, u16 *speed, u16 *duplex)

    Get current link speed and duplex

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param speed:
        pointer to store current link speed
    :type speed: u16 \*

    :param duplex:
        pointer to store the current link duplex
    :type duplex: u16 \*

.. _`e1000_get_link_up_info_ich8lan.description`:

Description
-----------

Calls the generic get_speed_and_duplex to retrieve the current link
information and then calls the Kumeran lock loss workaround for links at
gigabit speeds.

.. _`e1000_kmrn_lock_loss_workaround_ich8lan`:

e1000_kmrn_lock_loss_workaround_ich8lan
=======================================

.. c:function:: s32 e1000_kmrn_lock_loss_workaround_ich8lan(struct e1000_hw *hw)

    Kumeran workaround

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_kmrn_lock_loss_workaround_ich8lan.description`:

Description
-----------

Work-around for 82566 Kumeran PCS lock loss:
On link status change (i.e. PCI reset, speed change) and link is up and
speed is gigabit-
0) if workaround is optionally disabled do nothing
1) wait 1ms for Kumeran link to come up
2) check Kumeran Diagnostic register PCS lock loss bit
3) if not set the link is locked (all is good), otherwise...
4) reset the PHY
5) repeat up to 10 times

.. _`e1000_kmrn_lock_loss_workaround_ich8lan.note`:

Note
----

this is only called for IGP3 copper when speed is 1gb.

.. _`e1000e_set_kmrn_lock_loss_workaround_ich8lan`:

e1000e_set_kmrn_lock_loss_workaround_ich8lan
============================================

.. c:function:: void e1000e_set_kmrn_lock_loss_workaround_ich8lan(struct e1000_hw *hw, bool state)

    Set Kumeran workaround state

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

    :param state:
        boolean value used to set the current Kumeran workaround state
    :type state: bool

.. _`e1000e_set_kmrn_lock_loss_workaround_ich8lan.description`:

Description
-----------

If ICH8, set the current Kumeran workaround state (enabled - true
/disabled - false).

.. _`e1000e_igp3_phy_powerdown_workaround_ich8lan`:

e1000e_igp3_phy_powerdown_workaround_ich8lan
============================================

.. c:function:: void e1000e_igp3_phy_powerdown_workaround_ich8lan(struct e1000_hw *hw)

    Power down workaround on D3

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000e_igp3_phy_powerdown_workaround_ich8lan.description`:

Description
-----------

Workaround for 82566 power-down on D3 entry:
1) disable gigabit link
2) write VR power-down enable
3) read it back
Continue if successful, else issue LCD reset and repeat

.. _`e1000e_gig_downshift_workaround_ich8lan`:

e1000e_gig_downshift_workaround_ich8lan
=======================================

.. c:function:: void e1000e_gig_downshift_workaround_ich8lan(struct e1000_hw *hw)

    WoL from S5 stops working

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000e_gig_downshift_workaround_ich8lan.description`:

Description
-----------

Steps to take when dropping from 1Gb/s (eg. link cable removal (LSC),
LPLU, Gig disable, MDIC PHY reset):
1) Set Kumeran Near-end loopback
2) Clear Kumeran Near-end loopback
Should only be called for ICH8[m] devices with any 1G Phy.

.. _`e1000_suspend_workarounds_ich8lan`:

e1000_suspend_workarounds_ich8lan
=================================

.. c:function:: void e1000_suspend_workarounds_ich8lan(struct e1000_hw *hw)

    workarounds needed during S0->Sx

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_suspend_workarounds_ich8lan.description`:

Description
-----------

During S0 to Sx transition, it is possible the link remains at gig
instead of negotiating to a lower speed.  Before going to Sx, set
'Gig Disable' to force link speed negotiation to a lower speed based on
the LPLU setting in the NVM or custom setting.  For PCH and newer parts,
the OEM bits PHY register (LED, GbE disable and LPLU configurations) also
needs to be written.
Parts that support (and are linked to a partner which support) EEE in
100Mbps should disable LPLU since 100Mbps w/ EEE requires less power
than 10Mbps w/o EEE.

.. _`e1000_resume_workarounds_pchlan`:

e1000_resume_workarounds_pchlan
===============================

.. c:function:: void e1000_resume_workarounds_pchlan(struct e1000_hw *hw)

    workarounds needed during Sx->S0

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_resume_workarounds_pchlan.description`:

Description
-----------

During Sx to S0 transitions on non-managed devices or managed devices
on which PHY resets are not blocked, if the PHY registers cannot be
accessed properly by the s/w toggle the LANPHYPC value to power cycle
the PHY.
On i217, setup Intel Rapid Start Technology.

.. _`e1000_cleanup_led_ich8lan`:

e1000_cleanup_led_ich8lan
=========================

.. c:function:: s32 e1000_cleanup_led_ich8lan(struct e1000_hw *hw)

    Restore the default LED operation

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_cleanup_led_ich8lan.description`:

Description
-----------

Return the LED back to the default configuration.

.. _`e1000_led_on_ich8lan`:

e1000_led_on_ich8lan
====================

.. c:function:: s32 e1000_led_on_ich8lan(struct e1000_hw *hw)

    Turn LEDs on

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_led_on_ich8lan.description`:

Description
-----------

Turn on the LEDs.

.. _`e1000_led_off_ich8lan`:

e1000_led_off_ich8lan
=====================

.. c:function:: s32 e1000_led_off_ich8lan(struct e1000_hw *hw)

    Turn LEDs off

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_led_off_ich8lan.description`:

Description
-----------

Turn off the LEDs.

.. _`e1000_setup_led_pchlan`:

e1000_setup_led_pchlan
======================

.. c:function:: s32 e1000_setup_led_pchlan(struct e1000_hw *hw)

    Configures SW controllable LED

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_setup_led_pchlan.description`:

Description
-----------

This prepares the SW controllable LED for use.

.. _`e1000_cleanup_led_pchlan`:

e1000_cleanup_led_pchlan
========================

.. c:function:: s32 e1000_cleanup_led_pchlan(struct e1000_hw *hw)

    Restore the default LED operation

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_cleanup_led_pchlan.description`:

Description
-----------

Return the LED back to the default configuration.

.. _`e1000_led_on_pchlan`:

e1000_led_on_pchlan
===================

.. c:function:: s32 e1000_led_on_pchlan(struct e1000_hw *hw)

    Turn LEDs on

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_led_on_pchlan.description`:

Description
-----------

Turn on the LEDs.

.. _`e1000_led_off_pchlan`:

e1000_led_off_pchlan
====================

.. c:function:: s32 e1000_led_off_pchlan(struct e1000_hw *hw)

    Turn LEDs off

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_led_off_pchlan.description`:

Description
-----------

Turn off the LEDs.

.. _`e1000_get_cfg_done_ich8lan`:

e1000_get_cfg_done_ich8lan
==========================

.. c:function:: s32 e1000_get_cfg_done_ich8lan(struct e1000_hw *hw)

    Read config done bit after Full or PHY reset

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_get_cfg_done_ich8lan.description`:

Description
-----------

Read appropriate register for the config done bit for completion status
and configure the PHY through s/w for EEPROM-less parts.

.. _`e1000_get_cfg_done_ich8lan.note`:

NOTE
----

some silicon which is EEPROM-less will fail trying to read the
config done bit, so only an error is logged and continues.  If we were
to return with error, EEPROM-less silicon would not be able to be reset
or change link.

.. _`e1000_power_down_phy_copper_ich8lan`:

e1000_power_down_phy_copper_ich8lan
===================================

.. c:function:: void e1000_power_down_phy_copper_ich8lan(struct e1000_hw *hw)

    Remove link during PHY power down

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_power_down_phy_copper_ich8lan.description`:

Description
-----------

In the case of a PHY power down to save power, or to turn off link during a
driver unload, or wake on lan is not enabled, remove the link.

.. _`e1000_clear_hw_cntrs_ich8lan`:

e1000_clear_hw_cntrs_ich8lan
============================

.. c:function:: void e1000_clear_hw_cntrs_ich8lan(struct e1000_hw *hw)

    Clear statistical counters

    :param hw:
        pointer to the HW structure
    :type hw: struct e1000_hw \*

.. _`e1000_clear_hw_cntrs_ich8lan.description`:

Description
-----------

Clears hardware counters specific to the silicon family and calls
clear_hw_cntrs_generic to clear all general purpose counters.

.. This file was automatic generated / don't edit.

