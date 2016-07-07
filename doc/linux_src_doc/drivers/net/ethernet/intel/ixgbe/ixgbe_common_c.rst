.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/ixgbe/ixgbe_common.c

.. _`ixgbe_device_supports_autoneg_fc`:

ixgbe_device_supports_autoneg_fc
================================

.. c:function:: bool ixgbe_device_supports_autoneg_fc(struct ixgbe_hw *hw)

    Check if phy supports autoneg flow control

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_device_supports_autoneg_fc.description`:

Description
-----------

There are several phys that do not support autoneg flow control. This
function check the device id to see if the associated phy supports
autoneg flow control.

.. _`ixgbe_setup_fc_generic`:

ixgbe_setup_fc_generic
======================

.. c:function:: s32 ixgbe_setup_fc_generic(struct ixgbe_hw *hw)

    Set up flow control

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_setup_fc_generic.description`:

Description
-----------

Called at init time to set up flow control.

.. _`ixgbe_start_hw_generic`:

ixgbe_start_hw_generic
======================

.. c:function:: s32 ixgbe_start_hw_generic(struct ixgbe_hw *hw)

    Prepare hardware for Tx/Rx

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_start_hw_generic.description`:

Description
-----------

Starts the hardware by filling the bus info structure and media type, clears
all on chip counters, initializes receive address registers, multicast
table, VLAN filter table, calls routine to set up link and flow control
settings, and leaves transmit and receive units disabled and uninitialized

.. _`ixgbe_start_hw_gen2`:

ixgbe_start_hw_gen2
===================

.. c:function:: s32 ixgbe_start_hw_gen2(struct ixgbe_hw *hw)

    Init sequence for common device family

    :param struct ixgbe_hw \*hw:
        pointer to hw structure

.. _`ixgbe_start_hw_gen2.description`:

Description
-----------

Performs the init sequence common to the second generation
of 10 GbE devices.

.. _`ixgbe_start_hw_gen2.devices-in-the-second-generation`:

Devices in the second generation
--------------------------------

82599
X540

.. _`ixgbe_init_hw_generic`:

ixgbe_init_hw_generic
=====================

.. c:function:: s32 ixgbe_init_hw_generic(struct ixgbe_hw *hw)

    Generic hardware initialization

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_init_hw_generic.description`:

Description
-----------

Initialize the hardware by resetting the hardware, filling the bus info
structure and media type, clears all on chip counters, initializes receive
address registers, multicast table, VLAN filter table, calls routine to set
up link and flow control settings, and leaves transmit and receive units
disabled and uninitialized

.. _`ixgbe_clear_hw_cntrs_generic`:

ixgbe_clear_hw_cntrs_generic
============================

.. c:function:: s32 ixgbe_clear_hw_cntrs_generic(struct ixgbe_hw *hw)

    Generic clear hardware counters

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_clear_hw_cntrs_generic.description`:

Description
-----------

Clears all hardware statistics counters by reading them from the hardware
Statistics counters are clear on read.

.. _`ixgbe_read_pba_string_generic`:

ixgbe_read_pba_string_generic
=============================

.. c:function:: s32 ixgbe_read_pba_string_generic(struct ixgbe_hw *hw, u8 *pba_num, u32 pba_num_size)

    Reads part number string from EEPROM

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 \*pba_num:
        stores the part number string from the EEPROM

    :param u32 pba_num_size:
        part number string buffer length

.. _`ixgbe_read_pba_string_generic.description`:

Description
-----------

Reads the part number string from the EEPROM.

.. _`ixgbe_get_mac_addr_generic`:

ixgbe_get_mac_addr_generic
==========================

.. c:function:: s32 ixgbe_get_mac_addr_generic(struct ixgbe_hw *hw, u8 *mac_addr)

    Generic get MAC address

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 \*mac_addr:
        Adapter MAC address

.. _`ixgbe_get_mac_addr_generic.description`:

Description
-----------

Reads the adapter's MAC address from first Receive Address Register (RAR0)
A reset of the adapter must be performed prior to calling this function
in order for the MAC address to have been loaded from the EEPROM into RAR0

.. _`ixgbe_get_bus_info_generic`:

ixgbe_get_bus_info_generic
==========================

.. c:function:: s32 ixgbe_get_bus_info_generic(struct ixgbe_hw *hw)

    Generic set PCI bus info

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_get_bus_info_generic.description`:

Description
-----------

Sets the PCI bus info (speed, width, type) within the ixgbe_hw structure

.. _`ixgbe_set_lan_id_multi_port_pcie`:

ixgbe_set_lan_id_multi_port_pcie
================================

.. c:function:: void ixgbe_set_lan_id_multi_port_pcie(struct ixgbe_hw *hw)

    Set LAN id for PCIe multiple port devices

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

.. _`ixgbe_set_lan_id_multi_port_pcie.description`:

Description
-----------

Determines the LAN function id by reading memory-mapped registers
and swaps the port value if requested.

.. _`ixgbe_stop_adapter_generic`:

ixgbe_stop_adapter_generic
==========================

.. c:function:: s32 ixgbe_stop_adapter_generic(struct ixgbe_hw *hw)

    Generic stop Tx/Rx units

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_stop_adapter_generic.description`:

Description
-----------

Sets the adapter_stopped flag within ixgbe_hw struct. Clears interrupts,
disables transmit and receive units. The adapter_stopped flag is used by
the shared code and drivers to determine if the adapter is in a stopped
state and should not touch the hardware.

.. _`ixgbe_led_on_generic`:

ixgbe_led_on_generic
====================

.. c:function:: s32 ixgbe_led_on_generic(struct ixgbe_hw *hw, u32 index)

    Turns on the software controllable LEDs.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 index:
        led number to turn on

.. _`ixgbe_led_off_generic`:

ixgbe_led_off_generic
=====================

.. c:function:: s32 ixgbe_led_off_generic(struct ixgbe_hw *hw, u32 index)

    Turns off the software controllable LEDs.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 index:
        led number to turn off

.. _`ixgbe_init_eeprom_params_generic`:

ixgbe_init_eeprom_params_generic
================================

.. c:function:: s32 ixgbe_init_eeprom_params_generic(struct ixgbe_hw *hw)

    Initialize EEPROM params

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_init_eeprom_params_generic.description`:

Description
-----------

Initializes the EEPROM parameters ixgbe_eeprom_info within the
ixgbe_hw struct in order to set up EEPROM access.

.. _`ixgbe_write_eeprom_buffer_bit_bang_generic`:

ixgbe_write_eeprom_buffer_bit_bang_generic
==========================================

.. c:function:: s32 ixgbe_write_eeprom_buffer_bit_bang_generic(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Write EEPROM using bit-bang

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset within the EEPROM to write

    :param u16 words:
        number of words

    :param u16 \*data:
        16 bit word(s) to write to EEPROM

.. _`ixgbe_write_eeprom_buffer_bit_bang_generic.description`:

Description
-----------

Reads 16 bit word(s) from EEPROM through bit-bang method

.. _`ixgbe_write_eeprom_buffer_bit_bang`:

ixgbe_write_eeprom_buffer_bit_bang
==================================

.. c:function:: s32 ixgbe_write_eeprom_buffer_bit_bang(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Writes 16 bit word(s) to EEPROM

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset within the EEPROM to be written to

    :param u16 words:
        number of word(s)

    :param u16 \*data:
        16 bit word(s) to be written to the EEPROM

.. _`ixgbe_write_eeprom_buffer_bit_bang.description`:

Description
-----------

If ixgbe_eeprom_update_checksum is not called after this function, the
EEPROM will most likely contain an invalid checksum.

.. _`ixgbe_write_eeprom_generic`:

ixgbe_write_eeprom_generic
==========================

.. c:function:: s32 ixgbe_write_eeprom_generic(struct ixgbe_hw *hw, u16 offset, u16 data)

    Writes 16 bit value to EEPROM

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset within the EEPROM to be written to

    :param u16 data:
        16 bit word to be written to the EEPROM

.. _`ixgbe_write_eeprom_generic.description`:

Description
-----------

If ixgbe_eeprom_update_checksum is not called after this function, the
EEPROM will most likely contain an invalid checksum.

.. _`ixgbe_read_eeprom_buffer_bit_bang_generic`:

ixgbe_read_eeprom_buffer_bit_bang_generic
=========================================

.. c:function:: s32 ixgbe_read_eeprom_buffer_bit_bang_generic(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Read EEPROM using bit-bang

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset within the EEPROM to be read

    :param u16 words:
        number of word(s)

    :param u16 \*data:
        read 16 bit words(s) from EEPROM

.. _`ixgbe_read_eeprom_buffer_bit_bang_generic.description`:

Description
-----------

Reads 16 bit word(s) from EEPROM through bit-bang method

.. _`ixgbe_read_eeprom_buffer_bit_bang`:

ixgbe_read_eeprom_buffer_bit_bang
=================================

.. c:function:: s32 ixgbe_read_eeprom_buffer_bit_bang(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Read EEPROM using bit-bang

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset within the EEPROM to be read

    :param u16 words:
        number of word(s)

    :param u16 \*data:
        read 16 bit word(s) from EEPROM

.. _`ixgbe_read_eeprom_buffer_bit_bang.description`:

Description
-----------

Reads 16 bit word(s) from EEPROM through bit-bang method

.. _`ixgbe_read_eeprom_bit_bang_generic`:

ixgbe_read_eeprom_bit_bang_generic
==================================

.. c:function:: s32 ixgbe_read_eeprom_bit_bang_generic(struct ixgbe_hw *hw, u16 offset, u16 *data)

    Read EEPROM word using bit-bang

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset within the EEPROM to be read

    :param u16 \*data:
        read 16 bit value from EEPROM

.. _`ixgbe_read_eeprom_bit_bang_generic.description`:

Description
-----------

Reads 16 bit value from EEPROM through bit-bang method

.. _`ixgbe_read_eerd_buffer_generic`:

ixgbe_read_eerd_buffer_generic
==============================

.. c:function:: s32 ixgbe_read_eerd_buffer_generic(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Read EEPROM word(s) using EERD

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset of word in the EEPROM to read

    :param u16 words:
        number of word(s)

    :param u16 \*data:
        16 bit word(s) from the EEPROM

.. _`ixgbe_read_eerd_buffer_generic.description`:

Description
-----------

Reads a 16 bit word(s) from the EEPROM using the EERD register.

.. _`ixgbe_detect_eeprom_page_size_generic`:

ixgbe_detect_eeprom_page_size_generic
=====================================

.. c:function:: s32 ixgbe_detect_eeprom_page_size_generic(struct ixgbe_hw *hw, u16 offset)

    Detect EEPROM page size

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset within the EEPROM to be used as a scratch pad

.. _`ixgbe_detect_eeprom_page_size_generic.description`:

Description
-----------

Discover EEPROM page size by writing marching data at given offset.
This function is called only when we are writing a new large buffer
at given offset so the data would be overwritten anyway.

.. _`ixgbe_read_eerd_generic`:

ixgbe_read_eerd_generic
=======================

.. c:function:: s32 ixgbe_read_eerd_generic(struct ixgbe_hw *hw, u16 offset, u16 *data)

    Read EEPROM word using EERD

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset of  word in the EEPROM to read

    :param u16 \*data:
        word read from the EEPROM

.. _`ixgbe_read_eerd_generic.description`:

Description
-----------

Reads a 16 bit word from the EEPROM using the EERD register.

.. _`ixgbe_write_eewr_buffer_generic`:

ixgbe_write_eewr_buffer_generic
===============================

.. c:function:: s32 ixgbe_write_eewr_buffer_generic(struct ixgbe_hw *hw, u16 offset, u16 words, u16 *data)

    Write EEPROM word(s) using EEWR

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset of  word in the EEPROM to write

    :param u16 words:
        number of words

    :param u16 \*data:
        word(s) write to the EEPROM

.. _`ixgbe_write_eewr_buffer_generic.description`:

Description
-----------

Write a 16 bit word(s) to the EEPROM using the EEWR register.

.. _`ixgbe_write_eewr_generic`:

ixgbe_write_eewr_generic
========================

.. c:function:: s32 ixgbe_write_eewr_generic(struct ixgbe_hw *hw, u16 offset, u16 data)

    Write EEPROM word using EEWR

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 offset:
        offset of  word in the EEPROM to write

    :param u16 data:
        word write to the EEPROM

.. _`ixgbe_write_eewr_generic.description`:

Description
-----------

Write a 16 bit word to the EEPROM using the EEWR register.

.. _`ixgbe_poll_eerd_eewr_done`:

ixgbe_poll_eerd_eewr_done
=========================

.. c:function:: s32 ixgbe_poll_eerd_eewr_done(struct ixgbe_hw *hw, u32 ee_reg)

    Poll EERD read or EEWR write status

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 ee_reg:
        EEPROM flag for polling

.. _`ixgbe_poll_eerd_eewr_done.description`:

Description
-----------

Polls the status bit (bit 1) of the EERD or EEWR to determine when the
read or write is done respectively.

.. _`ixgbe_acquire_eeprom`:

ixgbe_acquire_eeprom
====================

.. c:function:: s32 ixgbe_acquire_eeprom(struct ixgbe_hw *hw)

    Acquire EEPROM using bit-bang

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_acquire_eeprom.description`:

Description
-----------

Prepares EEPROM for access using bit-bang method. This function should
be called before issuing a command to the EEPROM.

.. _`ixgbe_get_eeprom_semaphore`:

ixgbe_get_eeprom_semaphore
==========================

.. c:function:: s32 ixgbe_get_eeprom_semaphore(struct ixgbe_hw *hw)

    Get hardware semaphore

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_get_eeprom_semaphore.description`:

Description
-----------

Sets the hardware semaphores so EEPROM access can occur for bit-bang method

.. _`ixgbe_release_eeprom_semaphore`:

ixgbe_release_eeprom_semaphore
==============================

.. c:function:: void ixgbe_release_eeprom_semaphore(struct ixgbe_hw *hw)

    Release hardware semaphore

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_release_eeprom_semaphore.description`:

Description
-----------

This function clears hardware semaphore bits.

.. _`ixgbe_ready_eeprom`:

ixgbe_ready_eeprom
==================

.. c:function:: s32 ixgbe_ready_eeprom(struct ixgbe_hw *hw)

    Polls for EEPROM ready

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_standby_eeprom`:

ixgbe_standby_eeprom
====================

.. c:function:: void ixgbe_standby_eeprom(struct ixgbe_hw *hw)

    Returns EEPROM to a "standby" state

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_shift_out_eeprom_bits`:

ixgbe_shift_out_eeprom_bits
===========================

.. c:function:: void ixgbe_shift_out_eeprom_bits(struct ixgbe_hw *hw, u16 data, u16 count)

    Shift data bits out to the EEPROM.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 data:
        data to send to the EEPROM

    :param u16 count:
        number of bits to shift out

.. _`ixgbe_shift_in_eeprom_bits`:

ixgbe_shift_in_eeprom_bits
==========================

.. c:function:: u16 ixgbe_shift_in_eeprom_bits(struct ixgbe_hw *hw, u16 count)

    Shift data bits in from the EEPROM

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 count:
        *undescribed*

.. _`ixgbe_raise_eeprom_clk`:

ixgbe_raise_eeprom_clk
======================

.. c:function:: void ixgbe_raise_eeprom_clk(struct ixgbe_hw *hw, u32 *eec)

    Raises the EEPROM's clock input.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 \*eec:
        EEC register's current value

.. _`ixgbe_lower_eeprom_clk`:

ixgbe_lower_eeprom_clk
======================

.. c:function:: void ixgbe_lower_eeprom_clk(struct ixgbe_hw *hw, u32 *eec)

    Lowers the EEPROM's clock input.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 \*eec:
        *undescribed*

.. _`ixgbe_release_eeprom`:

ixgbe_release_eeprom
====================

.. c:function:: void ixgbe_release_eeprom(struct ixgbe_hw *hw)

    Release EEPROM, release semaphores

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_calc_eeprom_checksum_generic`:

ixgbe_calc_eeprom_checksum_generic
==================================

.. c:function:: s32 ixgbe_calc_eeprom_checksum_generic(struct ixgbe_hw *hw)

    Calculates and returns the checksum

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_validate_eeprom_checksum_generic`:

ixgbe_validate_eeprom_checksum_generic
======================================

.. c:function:: s32 ixgbe_validate_eeprom_checksum_generic(struct ixgbe_hw *hw, u16 *checksum_val)

    Validate EEPROM checksum

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 \*checksum_val:
        calculated checksum

.. _`ixgbe_validate_eeprom_checksum_generic.description`:

Description
-----------

Performs checksum calculation and validates the EEPROM checksum.  If the
caller does not need checksum_val, the value can be NULL.

.. _`ixgbe_update_eeprom_checksum_generic`:

ixgbe_update_eeprom_checksum_generic
====================================

.. c:function:: s32 ixgbe_update_eeprom_checksum_generic(struct ixgbe_hw *hw)

    Updates the EEPROM checksum

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_set_rar_generic`:

ixgbe_set_rar_generic
=====================

.. c:function:: s32 ixgbe_set_rar_generic(struct ixgbe_hw *hw, u32 index, u8 *addr, u32 vmdq, u32 enable_addr)

    Set Rx address register

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 index:
        Receive address register to write

    :param u8 \*addr:
        Address to put into receive address register

    :param u32 vmdq:
        VMDq "set" or "pool" index

    :param u32 enable_addr:
        set flag that address is active

.. _`ixgbe_set_rar_generic.description`:

Description
-----------

Puts an ethernet address into a receive address register.

.. _`ixgbe_clear_rar_generic`:

ixgbe_clear_rar_generic
=======================

.. c:function:: s32 ixgbe_clear_rar_generic(struct ixgbe_hw *hw, u32 index)

    Remove Rx address register

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 index:
        Receive address register to write

.. _`ixgbe_clear_rar_generic.description`:

Description
-----------

Clears an ethernet address from a receive address register.

.. _`ixgbe_init_rx_addrs_generic`:

ixgbe_init_rx_addrs_generic
===========================

.. c:function:: s32 ixgbe_init_rx_addrs_generic(struct ixgbe_hw *hw)

    Initializes receive address filters.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_init_rx_addrs_generic.description`:

Description
-----------

Places the MAC address in receive address register 0 and clears the rest
of the receive address registers. Clears the multicast table. Assumes
the receiver is in reset when the routine is called.

.. _`ixgbe_mta_vector`:

ixgbe_mta_vector
================

.. c:function:: s32 ixgbe_mta_vector(struct ixgbe_hw *hw, u8 *mc_addr)

    Determines bit-vector in multicast table to set

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 \*mc_addr:
        the multicast address

.. _`ixgbe_mta_vector.description`:

Description
-----------

Extracts the 12 bits, from a multicast address, to determine which
bit-vector to set in the multicast table. The hardware uses 12 bits, from
incoming rx multicast addresses, to determine the bit-vector to check in
the MTA. Which of the 4 combination, of 12-bits, the hardware uses is set
by the MO field of the MCSTCTRL. The MO field is set during initialization
to mc_filter_type.

.. _`ixgbe_set_mta`:

ixgbe_set_mta
=============

.. c:function:: void ixgbe_set_mta(struct ixgbe_hw *hw, u8 *mc_addr)

    Set bit-vector in multicast table

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 \*mc_addr:
        *undescribed*

.. _`ixgbe_set_mta.description`:

Description
-----------

Sets the bit-vector in the multicast table.

.. _`ixgbe_update_mc_addr_list_generic`:

ixgbe_update_mc_addr_list_generic
=================================

.. c:function:: s32 ixgbe_update_mc_addr_list_generic(struct ixgbe_hw *hw, struct net_device *netdev)

    Updates MAC list of multicast addresses

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param struct net_device \*netdev:
        pointer to net device structure

.. _`ixgbe_update_mc_addr_list_generic.description`:

Description
-----------

The given list replaces any existing list. Clears the MC addrs from receive
address registers and the multicast table. Uses unused receive address
registers for the first multicast addresses, and hashes the rest into the
multicast table.

.. _`ixgbe_enable_mc_generic`:

ixgbe_enable_mc_generic
=======================

.. c:function:: s32 ixgbe_enable_mc_generic(struct ixgbe_hw *hw)

    Enable multicast address in RAR

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_enable_mc_generic.description`:

Description
-----------

Enables multicast address in RAR and the use of the multicast hash table.

.. _`ixgbe_disable_mc_generic`:

ixgbe_disable_mc_generic
========================

.. c:function:: s32 ixgbe_disable_mc_generic(struct ixgbe_hw *hw)

    Disable multicast address in RAR

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_disable_mc_generic.description`:

Description
-----------

Disables multicast address in RAR and the use of the multicast hash table.

.. _`ixgbe_fc_enable_generic`:

ixgbe_fc_enable_generic
=======================

.. c:function:: s32 ixgbe_fc_enable_generic(struct ixgbe_hw *hw)

    Enable flow control

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_fc_enable_generic.description`:

Description
-----------

Enable flow control according to the current settings.

.. _`ixgbe_negotiate_fc`:

ixgbe_negotiate_fc
==================

.. c:function:: s32 ixgbe_negotiate_fc(struct ixgbe_hw *hw, u32 adv_reg, u32 lp_reg, u32 adv_sym, u32 adv_asm, u32 lp_sym, u32 lp_asm)

    Negotiate flow control

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 adv_reg:
        flow control advertised settings

    :param u32 lp_reg:
        link partner's flow control settings

    :param u32 adv_sym:
        symmetric pause bit in advertisement

    :param u32 adv_asm:
        asymmetric pause bit in advertisement

    :param u32 lp_sym:
        symmetric pause bit in link partner advertisement

    :param u32 lp_asm:
        asymmetric pause bit in link partner advertisement

.. _`ixgbe_negotiate_fc.description`:

Description
-----------

Find the intersection between advertised settings and link partner's
advertised settings

.. _`ixgbe_fc_autoneg_fiber`:

ixgbe_fc_autoneg_fiber
======================

.. c:function:: s32 ixgbe_fc_autoneg_fiber(struct ixgbe_hw *hw)

    Enable flow control on 1 gig fiber

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_fc_autoneg_fiber.description`:

Description
-----------

Enable flow control according on 1 gig fiber.

.. _`ixgbe_fc_autoneg_backplane`:

ixgbe_fc_autoneg_backplane
==========================

.. c:function:: s32 ixgbe_fc_autoneg_backplane(struct ixgbe_hw *hw)

    Enable flow control IEEE clause 37

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_fc_autoneg_backplane.description`:

Description
-----------

Enable flow control according to IEEE clause 37.

.. _`ixgbe_fc_autoneg_copper`:

ixgbe_fc_autoneg_copper
=======================

.. c:function:: s32 ixgbe_fc_autoneg_copper(struct ixgbe_hw *hw)

    Enable flow control IEEE clause 37

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_fc_autoneg_copper.description`:

Description
-----------

Enable flow control according to IEEE clause 37.

.. _`ixgbe_fc_autoneg`:

ixgbe_fc_autoneg
================

.. c:function:: void ixgbe_fc_autoneg(struct ixgbe_hw *hw)

    Configure flow control

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_fc_autoneg.description`:

Description
-----------

Compares our advertised flow control capabilities to those advertised by
our link partner, and determines the proper flow control mode to use.

.. _`ixgbe_pcie_timeout_poll`:

ixgbe_pcie_timeout_poll
=======================

.. c:function:: u32 ixgbe_pcie_timeout_poll(struct ixgbe_hw *hw)

    Return number of times to poll for completion

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_pcie_timeout_poll.description`:

Description
-----------

System-wide timeout range is encoded in PCIe Device Control2 register.

Add 10% to specified maximum and return the number of times to poll for
completion timeout, in units of 100 microsec.  Never return less than
800 = 80 millisec.

.. _`ixgbe_disable_pcie_master`:

ixgbe_disable_pcie_master
=========================

.. c:function:: s32 ixgbe_disable_pcie_master(struct ixgbe_hw *hw)

    Disable PCI-express master access

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_disable_pcie_master.description`:

Description
-----------

Disables PCI-Express master access and verifies there are no pending
requests. IXGBE_ERR_MASTER_REQUESTS_PENDING is returned if master disable
bit hasn't caused the master requests to be disabled, else 0
is returned signifying master requests disabled.

.. _`ixgbe_acquire_swfw_sync`:

ixgbe_acquire_swfw_sync
=======================

.. c:function:: s32 ixgbe_acquire_swfw_sync(struct ixgbe_hw *hw, u32 mask)

    Acquire SWFW semaphore

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 mask:
        Mask to specify which semaphore to acquire

.. _`ixgbe_acquire_swfw_sync.description`:

Description
-----------

Acquires the SWFW semaphore through the GSSR register for the specified
function (CSR, PHY0, PHY1, EEPROM, Flash)

.. _`ixgbe_release_swfw_sync`:

ixgbe_release_swfw_sync
=======================

.. c:function:: void ixgbe_release_swfw_sync(struct ixgbe_hw *hw, u32 mask)

    Release SWFW semaphore

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 mask:
        Mask to specify which semaphore to release

.. _`ixgbe_release_swfw_sync.description`:

Description
-----------

Releases the SWFW semaphore through the GSSR register for the specified
function (CSR, PHY0, PHY1, EEPROM, Flash)

.. _`prot_autoc_read_generic`:

prot_autoc_read_generic
=======================

.. c:function:: s32 prot_autoc_read_generic(struct ixgbe_hw *hw, bool *locked, u32 *reg_val)

    Hides MAC differences needed for AUTOC read

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param bool \*locked:
        bool to indicate whether the SW/FW lock should be taken.  Never
        true in this the generic case.

    :param u32 \*reg_val:
        Value we read from AUTOC

.. _`prot_autoc_read_generic.description`:

Description
-----------

The default case requires no protection so just to the register read.

.. _`prot_autoc_write_generic`:

prot_autoc_write_generic
========================

.. c:function:: s32 prot_autoc_write_generic(struct ixgbe_hw *hw, u32 reg_val, bool locked)

    Hides MAC differences needed for AUTOC write

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 reg_val:
        value to write to AUTOC

    :param bool locked:
        bool to indicate whether the SW/FW lock was already taken by
        previous read.

.. _`ixgbe_disable_rx_buff_generic`:

ixgbe_disable_rx_buff_generic
=============================

.. c:function:: s32 ixgbe_disable_rx_buff_generic(struct ixgbe_hw *hw)

    Stops the receive data path

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_disable_rx_buff_generic.description`:

Description
-----------

Stops the receive data path and waits for the HW to internally
empty the Rx security block.

.. _`ixgbe_enable_rx_buff_generic`:

ixgbe_enable_rx_buff_generic
============================

.. c:function:: s32 ixgbe_enable_rx_buff_generic(struct ixgbe_hw *hw)

    Enables the receive data path

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_enable_rx_buff_generic.description`:

Description
-----------

Enables the receive data path

.. _`ixgbe_enable_rx_dma_generic`:

ixgbe_enable_rx_dma_generic
===========================

.. c:function:: s32 ixgbe_enable_rx_dma_generic(struct ixgbe_hw *hw, u32 regval)

    Enable the Rx DMA unit

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 regval:
        register value to write to RXCTRL

.. _`ixgbe_enable_rx_dma_generic.description`:

Description
-----------

Enables the Rx DMA unit

.. _`ixgbe_blink_led_start_generic`:

ixgbe_blink_led_start_generic
=============================

.. c:function:: s32 ixgbe_blink_led_start_generic(struct ixgbe_hw *hw, u32 index)

    Blink LED based on index.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 index:
        led number to blink

.. _`ixgbe_blink_led_stop_generic`:

ixgbe_blink_led_stop_generic
============================

.. c:function:: s32 ixgbe_blink_led_stop_generic(struct ixgbe_hw *hw, u32 index)

    Stop blinking LED based on index.

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 index:
        led number to stop blinking

.. _`ixgbe_get_san_mac_addr_offset`:

ixgbe_get_san_mac_addr_offset
=============================

.. c:function:: s32 ixgbe_get_san_mac_addr_offset(struct ixgbe_hw *hw, u16 *san_mac_offset)

    Get SAN MAC address offset from the EEPROM

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 \*san_mac_offset:
        SAN MAC address offset

.. _`ixgbe_get_san_mac_addr_offset.description`:

Description
-----------

This function will read the EEPROM location for the SAN MAC address
pointer, and returns the value at that location.  This is used in both
get and set mac_addr routines.

.. _`ixgbe_get_san_mac_addr_generic`:

ixgbe_get_san_mac_addr_generic
==============================

.. c:function:: s32 ixgbe_get_san_mac_addr_generic(struct ixgbe_hw *hw, u8 *san_mac_addr)

    SAN MAC address retrieval from the EEPROM

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u8 \*san_mac_addr:
        SAN MAC address

.. _`ixgbe_get_san_mac_addr_generic.description`:

Description
-----------

Reads the SAN MAC address from the EEPROM, if it's available.  This is
per-port, so \ :c:func:`set_lan_id`\  must be called before reading the addresses.
\ :c:func:`set_lan_id`\  is called by \ :c:func:`identify_sfp`\ , but this cannot be relied
upon for non-SFP connections, so we must call it here.

.. _`ixgbe_get_pcie_msix_count_generic`:

ixgbe_get_pcie_msix_count_generic
=================================

.. c:function:: u16 ixgbe_get_pcie_msix_count_generic(struct ixgbe_hw *hw)

    Gets MSI-X vector count

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_get_pcie_msix_count_generic.description`:

Description
-----------

Read PCIe configuration space, and get the MSI-X vector count from
the capabilities table.

.. _`ixgbe_clear_vmdq_generic`:

ixgbe_clear_vmdq_generic
========================

.. c:function:: s32 ixgbe_clear_vmdq_generic(struct ixgbe_hw *hw, u32 rar, u32 vmdq)

    Disassociate a VMDq pool index from a rx address

    :param struct ixgbe_hw \*hw:
        pointer to hardware struct

    :param u32 rar:
        receive address register index to disassociate

    :param u32 vmdq:
        VMDq pool index to remove from the rar

.. _`ixgbe_set_vmdq_generic`:

ixgbe_set_vmdq_generic
======================

.. c:function:: s32 ixgbe_set_vmdq_generic(struct ixgbe_hw *hw, u32 rar, u32 vmdq)

    Associate a VMDq pool index with a rx address

    :param struct ixgbe_hw \*hw:
        pointer to hardware struct

    :param u32 rar:
        receive address register index to associate with a VMDq index

    :param u32 vmdq:
        VMDq pool index

.. _`ixgbe_set_vmdq_san_mac_generic`:

ixgbe_set_vmdq_san_mac_generic
==============================

.. c:function:: s32 ixgbe_set_vmdq_san_mac_generic(struct ixgbe_hw *hw, u32 vmdq)

    In IOV mode, Default pool is next pool after the number of VFs advertized and not 0. MPSAR table needs to be updated for SAN_MAC RAR [hw->mac.san_mac_rar_index]

    :param struct ixgbe_hw \*hw:
        pointer to hardware struct

    :param u32 vmdq:
        VMDq pool index

.. _`ixgbe_set_vmdq_san_mac_generic.description`:

Description
-----------

ixgbe_set_vmdq_san_mac - Associate default VMDq pool index with a rx address

.. _`ixgbe_init_uta_tables_generic`:

ixgbe_init_uta_tables_generic
=============================

.. c:function:: s32 ixgbe_init_uta_tables_generic(struct ixgbe_hw *hw)

    Initialize the Unicast Table Array

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_find_vlvf_slot`:

ixgbe_find_vlvf_slot
====================

.. c:function:: s32 ixgbe_find_vlvf_slot(struct ixgbe_hw *hw, u32 vlan, bool vlvf_bypass)

    find the vlanid or the first empty slot

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 vlan:
        VLAN id to write to VLAN filter

    :param bool vlvf_bypass:
        *undescribed*

.. _`ixgbe_find_vlvf_slot.description`:

Description
-----------

return the VLVF index where this VLAN id should be placed

.. _`ixgbe_set_vfta_generic`:

ixgbe_set_vfta_generic
======================

.. c:function:: s32 ixgbe_set_vfta_generic(struct ixgbe_hw *hw, u32 vlan, u32 vind, bool vlan_on, bool vlvf_bypass)

    Set VLAN filter table

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u32 vlan:
        VLAN id to write to VLAN filter

    :param u32 vind:
        VMDq output index that maps queue to VLAN id in VFVFB

    :param bool vlan_on:
        boolean flag to turn on/off VLAN in VFVF

    :param bool vlvf_bypass:
        boolean flag indicating updating default pool is okay

.. _`ixgbe_set_vfta_generic.description`:

Description
-----------

Turn on/off specified VLAN in the VLAN filter table.

.. _`ixgbe_clear_vfta_generic`:

ixgbe_clear_vfta_generic
========================

.. c:function:: s32 ixgbe_clear_vfta_generic(struct ixgbe_hw *hw)

    Clear VLAN filter table

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_clear_vfta_generic.description`:

Description
-----------

Clears the VLAN filer table, and the VMDq index associated with the filter

.. _`ixgbe_check_mac_link_generic`:

ixgbe_check_mac_link_generic
============================

.. c:function:: s32 ixgbe_check_mac_link_generic(struct ixgbe_hw *hw, ixgbe_link_speed *speed, bool *link_up, bool link_up_wait_to_complete)

    Determine link and speed status

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed \*speed:
        pointer to link speed

    :param bool \*link_up:
        true when link is up

    :param bool link_up_wait_to_complete:
        bool used to wait for link up or not

.. _`ixgbe_check_mac_link_generic.description`:

Description
-----------

Reads the links register to determine if link is up and the current speed

.. _`ixgbe_get_wwn_prefix_generic`:

ixgbe_get_wwn_prefix_generic
============================

.. c:function:: s32 ixgbe_get_wwn_prefix_generic(struct ixgbe_hw *hw, u16 *wwnn_prefix, u16 *wwpn_prefix)

    Get alternative WWNN/WWPN prefix from the EEPROM

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 \*wwnn_prefix:
        the alternative WWNN prefix

    :param u16 \*wwpn_prefix:
        the alternative WWPN prefix

.. _`ixgbe_get_wwn_prefix_generic.description`:

Description
-----------

This function will read the EEPROM from the alternative SAN MAC address
block to check the support for the alternative WWNN/WWPN prefix support.

.. _`ixgbe_set_mac_anti_spoofing`:

ixgbe_set_mac_anti_spoofing
===========================

.. c:function:: void ixgbe_set_mac_anti_spoofing(struct ixgbe_hw *hw, bool enable, int vf)

    Enable/Disable MAC anti-spoofing

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param bool enable:
        enable or disable switch for MAC anti-spoofing

    :param int vf:
        Virtual Function pool - VF Pool to set for MAC anti-spoofing

.. _`ixgbe_set_vlan_anti_spoofing`:

ixgbe_set_vlan_anti_spoofing
============================

.. c:function:: void ixgbe_set_vlan_anti_spoofing(struct ixgbe_hw *hw, bool enable, int vf)

    Enable/Disable VLAN anti-spoofing

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param bool enable:
        enable or disable switch for VLAN anti-spoofing

    :param int vf:
        *undescribed*

.. _`ixgbe_get_device_caps_generic`:

ixgbe_get_device_caps_generic
=============================

.. c:function:: s32 ixgbe_get_device_caps_generic(struct ixgbe_hw *hw, u16 *device_caps)

    Get additional device capabilities

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 \*device_caps:
        the EEPROM word with the extra device capabilities

.. _`ixgbe_get_device_caps_generic.description`:

Description
-----------

This function will read the EEPROM location for the device capabilities,
and return the word through device_caps.

.. _`ixgbe_set_rxpba_generic`:

ixgbe_set_rxpba_generic
=======================

.. c:function:: void ixgbe_set_rxpba_generic(struct ixgbe_hw *hw, int num_pb, u32 headroom, int strategy)

    Initialize RX packet buffer

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param int num_pb:
        number of packet buffers to allocate

    :param u32 headroom:
        reserve n KB of headroom

    :param int strategy:
        packet buffer allocation strategy

.. _`ixgbe_calculate_checksum`:

ixgbe_calculate_checksum
========================

.. c:function:: u8 ixgbe_calculate_checksum(u8 *buffer, u32 length)

    Calculate checksum for buffer

    :param u8 \*buffer:
        pointer to EEPROM

    :param u32 length:
        size of EEPROM to calculate a checksum for

.. _`ixgbe_calculate_checksum.description`:

Description
-----------

Calculates the checksum for some buffer on a specified length.  The
checksum calculated is returned.

.. _`ixgbe_host_interface_command`:

ixgbe_host_interface_command
============================

.. c:function:: s32 ixgbe_host_interface_command(struct ixgbe_hw *hw, void *buffer, u32 length, u32 timeout, bool return_data)

    Issue command to manageability block

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

    :param void \*buffer:
        contains the command to write and where the return status will
        be placed

    :param u32 length:
        length of buffer, must be multiple of 4 bytes

    :param u32 timeout:
        time in ms to wait for command completion

    :param bool return_data:
        read and return data from the buffer (true) or not (false)
        Needed because FW structures are big endian and decoding of
        these fields can be 8 bit or 16 bit based on command. Decoding
        is not easily understood without making a table of commands.
        So we will leave this up to the caller to read back the data
        in these cases.

.. _`ixgbe_host_interface_command.description`:

Description
-----------

Communicates with the manageability block.  On success return 0
else return IXGBE_ERR_HOST_INTERFACE_COMMAND.

.. _`ixgbe_set_fw_drv_ver_generic`:

ixgbe_set_fw_drv_ver_generic
============================

.. c:function:: s32 ixgbe_set_fw_drv_ver_generic(struct ixgbe_hw *hw, u8 maj, u8 min, u8 build, u8 sub)

    Sends driver version to firmware

    :param struct ixgbe_hw \*hw:
        pointer to the HW structure

    :param u8 maj:
        driver version major number

    :param u8 min:
        driver version minor number

    :param u8 build:
        driver version build number

    :param u8 sub:
        driver version sub build number

.. _`ixgbe_set_fw_drv_ver_generic.description`:

Description
-----------

Sends driver version number to firmware through the manageability
block.  On success return 0
else returns IXGBE_ERR_SWFW_SYNC when encountering an error acquiring
semaphore or IXGBE_ERR_HOST_INTERFACE_COMMAND when command fails.

.. _`ixgbe_clear_tx_pending`:

ixgbe_clear_tx_pending
======================

.. c:function:: void ixgbe_clear_tx_pending(struct ixgbe_hw *hw)

    Clear pending TX work from the PCIe fifo

    :param struct ixgbe_hw \*hw:
        pointer to the hardware structure

.. _`ixgbe_clear_tx_pending.description`:

Description
-----------

The 82599 and x540 MACs can experience issues if TX work is still pending
when a reset occurs.  This function prevents this by flushing the PCIe
buffers on the system.

.. _`ixgbe_get_ets_data`:

ixgbe_get_ets_data
==================

.. c:function:: s32 ixgbe_get_ets_data(struct ixgbe_hw *hw, u16 *ets_cfg, u16 *ets_offset)

    Extracts the ETS bit data

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param u16 \*ets_cfg:
        extected ETS data

    :param u16 \*ets_offset:
        offset of ETS data

.. _`ixgbe_get_ets_data.description`:

Description
-----------

Returns error code.

.. _`ixgbe_get_thermal_sensor_data_generic`:

ixgbe_get_thermal_sensor_data_generic
=====================================

.. c:function:: s32 ixgbe_get_thermal_sensor_data_generic(struct ixgbe_hw *hw)

    Gathers thermal sensor data

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_get_thermal_sensor_data_generic.description`:

Description
-----------

Returns the thermal sensor data structure

.. _`ixgbe_init_thermal_sensor_thresh_generic`:

ixgbe_init_thermal_sensor_thresh_generic
========================================

.. c:function:: s32 ixgbe_init_thermal_sensor_thresh_generic(struct ixgbe_hw *hw)

    Inits thermal sensor thresholds

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

.. _`ixgbe_init_thermal_sensor_thresh_generic.description`:

Description
-----------

Inits the thermal sensor thresholds according to the NVM map
and save off the threshold and location values into mac.thermal_sensor_data

.. _`ixgbe_setup_mac_link_multispeed_fiber`:

ixgbe_setup_mac_link_multispeed_fiber
=====================================

.. c:function:: s32 ixgbe_setup_mac_link_multispeed_fiber(struct ixgbe_hw *hw, ixgbe_link_speed speed, bool autoneg_wait_to_complete)

    Set MAC link speed

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed speed:
        new link speed

    :param bool autoneg_wait_to_complete:
        true when waiting for completion is needed

.. _`ixgbe_setup_mac_link_multispeed_fiber.description`:

Description
-----------

Set the link speed in the MAC and/or PHY register and restarts link.

.. _`ixgbe_set_soft_rate_select_speed`:

ixgbe_set_soft_rate_select_speed
================================

.. c:function:: void ixgbe_set_soft_rate_select_speed(struct ixgbe_hw *hw, ixgbe_link_speed speed)

    Set module link speed

    :param struct ixgbe_hw \*hw:
        pointer to hardware structure

    :param ixgbe_link_speed speed:
        link speed to set

.. _`ixgbe_set_soft_rate_select_speed.description`:

Description
-----------

Set module link speed via the soft rate select.

.. This file was automatic generated / don't edit.

