.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/ppatomfwctrl.c

.. _`pp_atomfwctrl_is_voltage_controlled_by_gpio_v4`:

pp_atomfwctrl_is_voltage_controlled_by_gpio_v4
==============================================

.. c:function:: bool pp_atomfwctrl_is_voltage_controlled_by_gpio_v4(struct pp_hwmgr *hwmgr, uint8_t voltage_type, uint8_t voltage_mode)

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

.. _`pp_atomfwctrl_get_pp_assign_pin`:

pp_atomfwctrl_get_pp_assign_pin
===============================

.. c:function:: bool pp_atomfwctrl_get_pp_assign_pin(struct pp_hwmgr *hwmgr, const uint32_t pin_id, struct pp_atomfwctrl_gpio_pin_assignment *gpio_pin_assignment)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param pin_id:
        *undescribed*
    :type pin_id: const uint32_t

    :param gpio_pin_assignment:
        *undescribed*
    :type gpio_pin_assignment: struct pp_atomfwctrl_gpio_pin_assignment \*

.. _`pp_atomfwctrl_enter_self_refresh`:

pp_atomfwctrl_enter_self_refresh
================================

.. c:function:: int pp_atomfwctrl_enter_self_refresh(struct pp_hwmgr *hwmgr)

    \ ``param``\  hwmgr

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. This file was automatic generated / don't edit.

