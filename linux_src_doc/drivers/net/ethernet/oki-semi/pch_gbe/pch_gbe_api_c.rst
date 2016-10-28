.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/oki-semi/pch_gbe/pch_gbe_api.c

.. _`pch_gbe_plat_get_bus_info`:

pch_gbe_plat_get_bus_info
=========================

.. c:function:: void pch_gbe_plat_get_bus_info(struct pch_gbe_hw *hw)

    Obtain bus information for adapter

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_plat_init_hw`:

pch_gbe_plat_init_hw
====================

.. c:function:: s32 pch_gbe_plat_init_hw(struct pch_gbe_hw *hw)

    Initialize hardware

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_plat_init_hw.return`:

Return
------

0:              Successfully

.. _`pch_gbe_plat_init_hw.negative-value`:

Negative value
--------------

Failed-EBUSY

.. _`pch_gbe_plat_init_function_pointers`:

pch_gbe_plat_init_function_pointers
===================================

.. c:function:: void pch_gbe_plat_init_function_pointers(struct pch_gbe_hw *hw)

    Init func ptrs

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_hal_setup_init_funcs`:

pch_gbe_hal_setup_init_funcs
============================

.. c:function:: s32 pch_gbe_hal_setup_init_funcs(struct pch_gbe_hw *hw)

    Initializes function pointers

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_hal_setup_init_funcs.return`:

Return
------

0:      Successfully

.. _`pch_gbe_hal_setup_init_funcs.enosys`:

ENOSYS
------

Function is not registered

.. _`pch_gbe_hal_get_bus_info`:

pch_gbe_hal_get_bus_info
========================

.. c:function:: void pch_gbe_hal_get_bus_info(struct pch_gbe_hw *hw)

    Obtain bus information for adapter

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_hal_init_hw`:

pch_gbe_hal_init_hw
===================

.. c:function:: s32 pch_gbe_hal_init_hw(struct pch_gbe_hw *hw)

    Initialize hardware

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_hal_init_hw.return`:

Return
------

0:      Successfully

.. _`pch_gbe_hal_init_hw.enosys`:

ENOSYS
------

Function is not registered

.. _`pch_gbe_hal_read_phy_reg`:

pch_gbe_hal_read_phy_reg
========================

.. c:function:: s32 pch_gbe_hal_read_phy_reg(struct pch_gbe_hw *hw, u32 offset, u16 *data)

    Reads PHY register

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

    :param u32 offset:
        The register to read

    :param u16 \*data:
        The buffer to store the 16-bit read.

.. _`pch_gbe_hal_read_phy_reg.return`:

Return
------

0:      Successfully

.. _`pch_gbe_hal_read_phy_reg.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_hal_write_phy_reg`:

pch_gbe_hal_write_phy_reg
=========================

.. c:function:: s32 pch_gbe_hal_write_phy_reg(struct pch_gbe_hw *hw, u32 offset, u16 data)

    Writes PHY register

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

    :param u32 offset:
        The register to read

    :param u16 data:
        The value to write.

.. _`pch_gbe_hal_write_phy_reg.return`:

Return
------

0:      Successfully

.. _`pch_gbe_hal_write_phy_reg.negative-value`:

Negative value
--------------

Failed

.. _`pch_gbe_hal_phy_hw_reset`:

pch_gbe_hal_phy_hw_reset
========================

.. c:function:: void pch_gbe_hal_phy_hw_reset(struct pch_gbe_hw *hw)

    Hard PHY reset

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_hal_phy_sw_reset`:

pch_gbe_hal_phy_sw_reset
========================

.. c:function:: void pch_gbe_hal_phy_sw_reset(struct pch_gbe_hw *hw)

    Soft PHY reset

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_hal_read_mac_addr`:

pch_gbe_hal_read_mac_addr
=========================

.. c:function:: s32 pch_gbe_hal_read_mac_addr(struct pch_gbe_hw *hw)

    Reads MAC address

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_hal_read_mac_addr.return`:

Return
------

0:      Successfully

.. _`pch_gbe_hal_read_mac_addr.enosys`:

ENOSYS
------

Function is not registered

.. _`pch_gbe_hal_power_up_phy`:

pch_gbe_hal_power_up_phy
========================

.. c:function:: void pch_gbe_hal_power_up_phy(struct pch_gbe_hw *hw)

    Power up PHY

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. _`pch_gbe_hal_power_down_phy`:

pch_gbe_hal_power_down_phy
==========================

.. c:function:: void pch_gbe_hal_power_down_phy(struct pch_gbe_hw *hw)

    Power down PHY

    :param struct pch_gbe_hw \*hw:
        Pointer to the HW structure

.. This file was automatic generated / don't edit.

