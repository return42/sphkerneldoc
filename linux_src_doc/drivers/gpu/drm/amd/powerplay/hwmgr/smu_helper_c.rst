.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/hwmgr/smu_helper.c

.. _`phm_wait_on_register`:

phm_wait_on_register
====================

.. c:function:: int phm_wait_on_register(struct pp_hwmgr *hwmgr, uint32_t index, uint32_t value, uint32_t mask)

    reached the given value.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param index:
        *undescribed*
    :type index: uint32_t

    :param value:
        *undescribed*
    :type value: uint32_t

    :param mask:
        *undescribed*
    :type mask: uint32_t

.. _`phm_wait_on_indirect_register`:

phm_wait_on_indirect_register
=============================

.. c:function:: int phm_wait_on_indirect_register(struct pp_hwmgr *hwmgr, uint32_t indirect_port, uint32_t index, uint32_t value, uint32_t mask)

    reached the given value.The indirect space is described by giving the memory-mapped index of the indirect index register.

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

    :param indirect_port:
        *undescribed*
    :type indirect_port: uint32_t

    :param index:
        *undescribed*
    :type index: uint32_t

    :param value:
        *undescribed*
    :type value: uint32_t

    :param mask:
        *undescribed*
    :type mask: uint32_t

.. _`phm_initializa_dynamic_state_adjustment_rule_settings`:

phm_initializa_dynamic_state_adjustment_rule_settings
=====================================================

.. c:function:: int phm_initializa_dynamic_state_adjustment_rule_settings(struct pp_hwmgr *hwmgr)

    :param hwmgr:
        *undescribed*
    :type hwmgr: struct pp_hwmgr \*

.. _`phm_initializa_dynamic_state_adjustment_rule_settings.description`:

Description
-----------

\ ``param``\     hwmgr  the address of the powerplay hardware manager.

.. This file was automatic generated / don't edit.

