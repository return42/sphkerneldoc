.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/bios/bios_parser2.c

.. _`bios_parser_get_gpio_pin_info`:

bios_parser_get_gpio_pin_info
=============================

.. c:function:: enum bp_result bios_parser_get_gpio_pin_info(struct dc_bios *dcb, uint32_t gpio_id, struct gpio_pin_info *info)

    Get GpioPin information of input gpio id

    :param struct dc_bios \*dcb:
        *undescribed*

    :param uint32_t gpio_id:
        *undescribed*

    :param struct gpio_pin_info \*info:
        *undescribed*

.. _`bios_parser_get_gpio_pin_info.description`:

Description
-----------

\ ``param``\  gpio_id, GPIO ID
\ ``param``\  info, GpioPin information structure
\ ``return``\  Bios parser result code
\ ``note``\ 
to get the GPIO PIN INFO, we need:
1. get the GPIO_ID from other object table, see \ :c:func:`GetHPDInfo`\ 
2. in DATA_TABLE.GPIO_Pin_LUT, search all records,
to get the registerA  offset/mask

.. _`bios_parser_get_spread_spectrum_info`:

bios_parser_get_spread_spectrum_info
====================================

.. c:function:: enum bp_result bios_parser_get_spread_spectrum_info(struct dc_bios *dcb, enum as_signal_type signal, uint32_t index, struct spread_spectrum_info *ss_info)

    Get spread spectrum information from the ASIC_InternalSS_Info(ver 2.1 or ver 3.1) or SS_Info table from the VBIOS. Currently ASIC_InternalSS_Info ver 2.1 can co-exist with SS_Info table. Expect ASIC_InternalSS_Info ver 3.1, there is only one entry for each signal /ss id.  However, there is no planning of supporting multiple spread Sprectum entry for EverGreen \ ``param``\  [in] this \ ``param``\  [in] signal, ASSignalType to be converted to info index \ ``param``\  [in] index, number of entries that match the converted info index \ ``param``\  [out] ss_info, sprectrum information structure, \ ``return``\  Bios parser result code

    :param struct dc_bios \*dcb:
        *undescribed*

    :param enum as_signal_type signal:
        *undescribed*

    :param uint32_t index:
        *undescribed*

    :param struct spread_spectrum_info \*ss_info:
        *undescribed*

.. _`bios_parser_set_scratch_critical_state`:

bios_parser_set_scratch_critical_state
======================================

.. c:function:: void bios_parser_set_scratch_critical_state(struct dc_bios *dcb, bool state)

    :param struct dc_bios \*dcb:
        *undescribed*

    :param bool state:
        *undescribed*

.. _`bios_parser_set_scratch_critical_state.description`:

Description
-----------

\ ``brief``\ 
update critical state bit in VBIOS scratch register

\ ``param``\ 
bool - to set or reset state

.. This file was automatic generated / don't edit.

