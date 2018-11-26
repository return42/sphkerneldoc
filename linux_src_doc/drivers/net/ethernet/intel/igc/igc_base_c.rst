.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/intel/igc/igc_base.c

.. _`igc_set_pcie_completion_timeout`:

igc_set_pcie_completion_timeout
===============================

.. c:function:: s32 igc_set_pcie_completion_timeout(struct igc_hw *hw)

    set pci-e completion timeout

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_check_for_link_base`:

igc_check_for_link_base
=======================

.. c:function:: s32 igc_check_for_link_base(struct igc_hw *hw)

    Check for link

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_check_for_link_base.description`:

Description
-----------

If sgmii is enabled, then use the pcs register to determine link, otherwise
use the generic interface for determining link.

.. _`igc_reset_hw_base`:

igc_reset_hw_base
=================

.. c:function:: s32 igc_reset_hw_base(struct igc_hw *hw)

    Reset hardware

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_reset_hw_base.description`:

Description
-----------

This resets the hardware into a known state.  This is a
function pointer entry point called by the api module.

.. _`igc_get_phy_id_base`:

igc_get_phy_id_base
===================

.. c:function:: s32 igc_get_phy_id_base(struct igc_hw *hw)

    Retrieve PHY addr and id

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_get_phy_id_base.description`:

Description
-----------

Retrieves the PHY address and ID for both PHY's which do and do not use
sgmi interface.

.. _`igc_init_nvm_params_base`:

igc_init_nvm_params_base
========================

.. c:function:: s32 igc_init_nvm_params_base(struct igc_hw *hw)

    Init NVM func ptrs.

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_setup_copper_link_base`:

igc_setup_copper_link_base
==========================

.. c:function:: s32 igc_setup_copper_link_base(struct igc_hw *hw)

    Configure copper link settings

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_setup_copper_link_base.description`:

Description
-----------

Configures the link for auto-neg or forced speed and duplex.  Then we check
for link, once link is established calls to configure collision distance
and flow control are called.

.. _`igc_init_mac_params_base`:

igc_init_mac_params_base
========================

.. c:function:: s32 igc_init_mac_params_base(struct igc_hw *hw)

    Init MAC func ptrs.

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_init_phy_params_base`:

igc_init_phy_params_base
========================

.. c:function:: s32 igc_init_phy_params_base(struct igc_hw *hw)

    Init PHY func ptrs.

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_acquire_phy_base`:

igc_acquire_phy_base
====================

.. c:function:: s32 igc_acquire_phy_base(struct igc_hw *hw)

    Acquire rights to access PHY

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_acquire_phy_base.description`:

Description
-----------

Acquire access rights to the correct PHY.  This is a
function pointer entry point called by the api module.

.. _`igc_release_phy_base`:

igc_release_phy_base
====================

.. c:function:: void igc_release_phy_base(struct igc_hw *hw)

    Release rights to access PHY

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_release_phy_base.description`:

Description
-----------

A wrapper to release access rights to the correct PHY.  This is a
function pointer entry point called by the api module.

.. _`igc_get_link_up_info_base`:

igc_get_link_up_info_base
=========================

.. c:function:: s32 igc_get_link_up_info_base(struct igc_hw *hw, u16 *speed, u16 *duplex)

    Get link speed/duplex info

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

    :param speed:
        stores the current speed
    :type speed: u16 \*

    :param duplex:
        stores the current duplex
    :type duplex: u16 \*

.. _`igc_get_link_up_info_base.description`:

Description
-----------

This is a wrapper function, if using the serial gigabit media independent
interface, use PCS to retrieve the link speed and duplex information.
Otherwise, use the generic function to get the link speed and duplex info.

.. _`igc_init_hw_base`:

igc_init_hw_base
================

.. c:function:: s32 igc_init_hw_base(struct igc_hw *hw)

    Initialize hardware

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_init_hw_base.description`:

Description
-----------

This inits the hardware readying it for operation.

.. _`igc_read_mac_addr_base`:

igc_read_mac_addr_base
======================

.. c:function:: s32 igc_read_mac_addr_base(struct igc_hw *hw)

    Read device MAC address

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_power_down_phy_copper_base`:

igc_power_down_phy_copper_base
==============================

.. c:function:: void igc_power_down_phy_copper_base(struct igc_hw *hw)

    Remove link during PHY power down

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_power_down_phy_copper_base.description`:

Description
-----------

In the case of a PHY power down to save power, or to turn off link during a
driver unload, or wake on lan is not enabled, remove the link.

.. _`igc_rx_fifo_flush_base`:

igc_rx_fifo_flush_base
======================

.. c:function:: void igc_rx_fifo_flush_base(struct igc_hw *hw)

    Clean rx fifo after Rx enable

    :param hw:
        pointer to the HW structure
    :type hw: struct igc_hw \*

.. _`igc_rx_fifo_flush_base.description`:

Description
-----------

After Rx enable, if manageability is enabled then there is likely some
bad data at the start of the fifo and possibly in the DMA fifo.  This
function clears the fifos and flushes any packets that came in as rx was
being enabled.

.. This file was automatic generated / don't edit.

