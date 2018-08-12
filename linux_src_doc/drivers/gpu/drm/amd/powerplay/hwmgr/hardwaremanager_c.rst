.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/hardwaremanager.c

.. _`phm_start_thermal_controller`:

phm_start_thermal_controller
============================

.. c:function:: int phm_start_thermal_controller(struct pp_hwmgr *hwmgr)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

.. _`phm_start_thermal_controller.description`:

Description
-----------

\ ``param``\     pHwMgr  the address of the powerplay hardware manager.
\ ``exception``\  PP_Result_Failed if any of the paramters is NULL, otherwise the return value from the dispatcher.

.. _`phm_get_clock_info`:

phm_get_clock_info
==================

.. c:function:: int phm_get_clock_info(struct pp_hwmgr *hwmgr, const struct pp_hw_power_state *state, struct pp_clock_info *pclock_info, PHM_PerformanceLevelDesignation designation)

    :param struct pp_hwmgr \*hwmgr:
        *undescribed*

    :param const struct pp_hw_power_state \*state:
        *undescribed*

    :param struct pp_clock_info \*pclock_info:
        *undescribed*

    :param PHM_PerformanceLevelDesignation designation:
        *undescribed*

.. _`phm_get_clock_info.description`:

Description
-----------

\ ``param``\     pHwMgr  the address of the powerplay hardware manager.
\ ``param``\     pPowerState the address of the Power State structure.
\ ``param``\     pClockInfo the address of PP_ClockInfo structure where the result will be returned.
\ ``exception``\  PP_Result_Failed if any of the paramters is NULL, otherwise the return value from the back-end.

.. This file was automatic generated / don't edit.

