.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/ppatomctrl.c

.. _`atomctrl_set_mc_reg_address_table`:

atomctrl_set_mc_reg_address_table
=================================

.. c:function:: int atomctrl_set_mc_reg_address_table(ATOM_INIT_REG_BLOCK *reg_block, pp_atomctrl_mc_reg_table *table)

    VBIOS set end of memory clock AC timing registers by ucPreRegDataLength bit6 = 1 \ ``param``\     reg_block the address ATOM_INIT_REG_BLOCK \ ``param``\     table the address of MCRegTable \ ``return``\    0

    :param reg_block:
        *undescribed*
    :type reg_block: ATOM_INIT_REG_BLOCK \*

    :param table:
        *undescribed*
    :type table: pp_atomctrl_mc_reg_table \*

.. _`atomctrl_set_engine_dram_timings_rv770`:

atomctrl_set_engine_dram_timings_rv770
======================================

.. c:function:: int atomctrl_set_engine_dram_timings_rv770(struct pp_hwmgr *hwmgr, uint32_t engine_clock, uint32_t memory_clock)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param engine_clock:
        *undescribed*
    :type engine_clock: uint32_t

    :param memory_clock:
        *undescribed*
    :type memory_clock: uint32_t

.. _`get_voltage_info_table`:

get_voltage_info_table
======================

.. c:function:: ATOM_VOLTAGE_OBJECT_INFO *get_voltage_info_table(void *device)

    :param device:
        *undescribed*
    :type device: void \*

.. _`get_voltage_info_table.warning`:

WARNING
-------

The tabled returned by this function is in
dynamically allocated memory.
The caller has to release if by calling kfree.

.. _`atomctrl_get_reference_clock`:

atomctrl_get_reference_clock
============================

.. c:function:: uint32_t atomctrl_get_reference_clock(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`atomctrl_is_voltage_controlled_by_gpio_v3`:

atomctrl_is_voltage_controlled_by_gpio_v3
=========================================

.. c:function:: bool atomctrl_is_voltage_controlled_by_gpio_v3(struct pp_hwmgr *hwmgr, uint8_t voltage_type, uint8_t voltage_mode)

    voltage_type is one of SET_VOLTAGE_TYPE_ASIC_VDDC, SET_VOLTAGE_TYPE_ASIC_MVDDC, SET_VOLTAGE_TYPE_ASIC_MVDDQ. voltage_mode is one of ATOM_SET_VOLTAGE, ATOM_SET_VOLTAGE_PHASE

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param voltage_type:
        *undescribed*
    :type voltage_type: uint8_t

    :param voltage_mode:
        *undescribed*
    :type voltage_mode: uint8_t

.. _`get_gpio_lookup_table`:

get_gpio_lookup_table
=====================

.. c:function:: ATOM_GPIO_PIN_LUT *get_gpio_lookup_table(void *device)

    :param device:
        *undescribed*
    :type device: void \*

.. _`get_gpio_lookup_table.warning`:

WARNING
-------

The tabled returned by this function is in
dynamically allocated memory.
The caller has to release if by calling kfree.

.. _`atomctrl_get_pp_assign_pin`:

atomctrl_get_pp_assign_pin
==========================

.. c:function:: bool atomctrl_get_pp_assign_pin(struct pp_hwmgr *hwmgr, const uint32_t pinId, pp_atomctrl_gpio_pin_assignment *gpio_pin_assignment)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param pinId:
        *undescribed*
    :type pinId: const uint32_t

    :param gpio_pin_assignment:
        *undescribed*
    :type gpio_pin_assignment: pp_atomctrl_gpio_pin_assignment \*

.. _`atomctrl_get_voltage_evv`:

atomctrl_get_voltage_evv
========================

.. c:function:: int atomctrl_get_voltage_evv(struct pp_hwmgr *hwmgr, uint16_t virtual_voltage_id, uint16_t *voltage)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param virtual_voltage_id:
        *undescribed*
    :type virtual_voltage_id: uint16_t

    :param voltage:
        *undescribed*
    :type voltage: uint16_t \*

.. _`atomctrl_get_mpll_reference_clock`:

atomctrl_get_mpll_reference_clock
=================================

.. c:function:: uint32_t atomctrl_get_mpll_reference_clock(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`asic_internal_ss_get_ss_table`:

asic_internal_ss_get_ss_table
=============================

.. c:function:: ATOM_ASIC_INTERNAL_SS_INFO *asic_internal_ss_get_ss_table(void *device)

    :param device:
        *undescribed*
    :type device: void \*

.. _`asic_internal_ss_get_ss_asignment`:

asic_internal_ss_get_ss_asignment
=================================

.. c:function:: int asic_internal_ss_get_ss_asignment(struct pp_hwmgr *hwmgr, const uint8_t clockSource, const uint32_t clockSpeed, pp_atomctrl_internal_ss_info *ssEntry)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param clockSource:
        *undescribed*
    :type clockSource: const uint8_t

    :param clockSpeed:
        *undescribed*
    :type clockSpeed: const uint32_t

    :param ssEntry:
        *undescribed*
    :type ssEntry: pp_atomctrl_internal_ss_info \*

.. _`atomctrl_get_memory_clock_spread_spectrum`:

atomctrl_get_memory_clock_spread_spectrum
=========================================

.. c:function:: int atomctrl_get_memory_clock_spread_spectrum(struct pp_hwmgr *hwmgr, const uint32_t memory_clock, pp_atomctrl_internal_ss_info *ssInfo)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param memory_clock:
        *undescribed*
    :type memory_clock: const uint32_t

    :param ssInfo:
        *undescribed*
    :type ssInfo: pp_atomctrl_internal_ss_info \*

.. _`atomctrl_get_engine_clock_spread_spectrum`:

atomctrl_get_engine_clock_spread_spectrum
=========================================

.. c:function:: int atomctrl_get_engine_clock_spread_spectrum(struct pp_hwmgr *hwmgr, const uint32_t engine_clock, pp_atomctrl_internal_ss_info *ssInfo)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param engine_clock:
        *undescribed*
    :type engine_clock: const uint32_t

    :param ssInfo:
        *undescribed*
    :type ssInfo: pp_atomctrl_internal_ss_info \*

.. This file was automatic generated / don't edit.

