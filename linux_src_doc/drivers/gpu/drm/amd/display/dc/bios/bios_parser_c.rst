.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/display/dc/bios/bios_parser.c

.. _`bios_parser_get_spread_spectrum_info`:

bios_parser_get_spread_spectrum_info
====================================

.. c:function:: enum bp_result bios_parser_get_spread_spectrum_info(struct dc_bios *dcb, enum as_signal_type signal, uint32_t index, struct spread_spectrum_info *ss_info)

    Get spread spectrum information from the ASIC_InternalSS_Info(ver 2.1 or ver 3.1) or SS_Info table from the VBIOS. Currently ASIC_InternalSS_Info ver 2.1 can co-exist with SS_Info table. Expect ASIC_InternalSS_Info ver 3.1, there is only one entry for each signal /ss id.  However, there is no planning of supporting multiple spread Sprectum entry for EverGreen \ ``param``\  [in] this \ ``param``\  [in] signal, ASSignalType to be converted to info index \ ``param``\  [in] index, number of entries that match the converted info index \ ``param``\  [out] ss_info, sprectrum information structure, \ ``return``\  Bios parser result code

    :param dcb:
        *undescribed*
    :type dcb: struct dc_bios \*

    :param signal:
        *undescribed*
    :type signal: enum as_signal_type

    :param index:
        *undescribed*
    :type index: uint32_t

    :param ss_info:
        *undescribed*
    :type ss_info: struct spread_spectrum_info \*

.. _`get_ss_info_from_tbl`:

get_ss_info_from_tbl
====================

.. c:function:: enum bp_result get_ss_info_from_tbl(struct bios_parser *bp, uint32_t id, struct spread_spectrum_info *ss_info)

    Get spread sprectrum information from the ASIC_InternalSS_Info Ver 2.1 or SS_Info table from the VBIOS There can not be more than 1 entry for  ASIC_InternalSS_Info Ver 2.1 or SS_Info.

    :param bp:
        *undescribed*
    :type bp: struct bios_parser \*

    :param id:
        *undescribed*
    :type id: uint32_t

    :param ss_info:
        *undescribed*
    :type ss_info: struct spread_spectrum_info \*

.. _`get_ss_info_from_tbl.description`:

Description
-----------

\ ``param``\  this
\ ``param``\  id, spread sprectrum info index
\ ``param``\  pSSinfo, sprectrum information structure,
\ ``return``\  Bios parser result code

.. _`get_ss_info_from_internal_ss_info_tbl_v2_1`:

get_ss_info_from_internal_ss_info_tbl_V2_1
==========================================

.. c:function:: enum bp_result get_ss_info_from_internal_ss_info_tbl_V2_1(struct bios_parser *bp, uint32_t id, struct spread_spectrum_info *info)

    Get spread sprectrum information from the ASIC_InternalSS_Info table Ver 2.1 from the VBIOS There will not be multiple entry for Ver 2.1

    :param bp:
        *undescribed*
    :type bp: struct bios_parser \*

    :param id:
        *undescribed*
    :type id: uint32_t

    :param info:
        *undescribed*
    :type info: struct spread_spectrum_info \*

.. _`get_ss_info_from_internal_ss_info_tbl_v2_1.description`:

Description
-----------

\ ``param``\  id, spread sprectrum info index
\ ``param``\  pSSinfo, sprectrum information structure,
\ ``return``\  Bios parser result code

.. _`get_ss_info_from_ss_info_table`:

get_ss_info_from_ss_info_table
==============================

.. c:function:: enum bp_result get_ss_info_from_ss_info_table(struct bios_parser *bp, uint32_t id, struct spread_spectrum_info *ss_info)

    Get spread sprectrum information from the SS_Info table from the VBIOS if the pointer to info is NULL, indicate the caller what to know the number of entries that matches the id for, the SS_Info table, there should not be more than 1 entry match.

    :param bp:
        *undescribed*
    :type bp: struct bios_parser \*

    :param id:
        *undescribed*
    :type id: uint32_t

    :param ss_info:
        *undescribed*
    :type ss_info: struct spread_spectrum_info \*

.. _`get_ss_info_from_ss_info_table.description`:

Description
-----------

\ ``param``\  [in] id, spread sprectrum id
\ ``param``\  [out] pSSinfo, sprectrum information structure,
\ ``return``\  Bios parser result code

.. _`bios_parser_get_encoder_cap_info`:

bios_parser_get_encoder_cap_info
================================

.. c:function:: enum bp_result bios_parser_get_encoder_cap_info(struct dc_bios *dcb, struct graphics_object_id object_id, struct bp_encoder_cap_info *info)

    :param dcb:
        *undescribed*
    :type dcb: struct dc_bios \*

    :param object_id:
        *undescribed*
    :type object_id: struct graphics_object_id

    :param info:
        *undescribed*
    :type info: struct bp_encoder_cap_info \*

.. _`bios_parser_get_encoder_cap_info.description`:

Description
-----------

\ ``brief``\ 
Get encoder capability information of input object id

\ ``param``\  object_id, Object id
\ ``param``\  object_id, encoder cap information structure

\ ``return``\  Bios parser result code

.. _`get_encoder_cap_record`:

get_encoder_cap_record
======================

.. c:function:: ATOM_ENCODER_CAP_RECORD_V2 *get_encoder_cap_record(struct bios_parser *bp, ATOM_OBJECT *object)

    :param bp:
        *undescribed*
    :type bp: struct bios_parser \*

    :param object:
        *undescribed*
    :type object: ATOM_OBJECT \*

.. _`get_encoder_cap_record.description`:

Description
-----------

\ ``brief``\ 
Get encoder cap record for the object

\ ``param``\  object, ATOM object

\ ``return``\  atom encoder cap record

\ ``note``\ 
search all records to find the ATOM_ENCODER_CAP_RECORD_V2 record

.. _`bios_parser_get_ss_entry_number`:

bios_parser_get_ss_entry_number
===============================

.. c:function:: uint32_t bios_parser_get_ss_entry_number(struct dc_bios *dcb, enum as_signal_type signal)

    :GetNumberofSpreadSpectrumEntry Get Number of SpreadSpectrum Entry from the ASIC_InternalSS_Info table from the VBIOS that match the SSid (to be converted from signal)

    :param dcb:
        *undescribed*
    :type dcb: struct dc_bios \*

    :param signal:
        *undescribed*
    :type signal: enum as_signal_type

.. _`bios_parser_get_ss_entry_number.description`:

Description
-----------

\ ``param``\ [in] signal, ASSignalType to be converted to SSid
\ ``return``\  number of SS Entry that match the signal

.. _`get_ss_entry_number_from_ss_info_tbl`:

get_ss_entry_number_from_ss_info_tbl
====================================

.. c:function:: uint32_t get_ss_entry_number_from_ss_info_tbl(struct bios_parser *bp, uint32_t id)

    Get Number of spread spectrum entry from the SS_Info table from the VBIOS.

    :param bp:
        *undescribed*
    :type bp: struct bios_parser \*

    :param id:
        *undescribed*
    :type id: uint32_t

.. _`get_ss_entry_number_from_ss_info_tbl.description`:

Description
-----------

\ ``note``\  There can only be one entry for each id for SS_Info Table

\ ``param``\  [in] id, spread spectrum id
\ ``return``\  number of SS Entry that match the id

.. _`get_ss_entry_number`:

get_ss_entry_number
===================

.. c:function:: uint32_t get_ss_entry_number(struct bios_parser *bp, uint32_t id)

    Get spread sprectrum information from the ASIC_InternalSS_Info Ver 2.1 or SS_Info table from the VBIOS There can not be more than 1 entry for  ASIC_InternalSS_Info Ver 2.1 or SS_Info.

    :param bp:
        *undescribed*
    :type bp: struct bios_parser \*

    :param id:
        *undescribed*
    :type id: uint32_t

.. _`get_ss_entry_number.description`:

Description
-----------

\ ``param``\  id, spread sprectrum info index
\ ``return``\  Bios parser result code

.. _`get_ss_entry_number_from_internal_ss_info_tbl_v2_1`:

get_ss_entry_number_from_internal_ss_info_tbl_v2_1
==================================================

.. c:function:: uint32_t get_ss_entry_number_from_internal_ss_info_tbl_v2_1(struct bios_parser *bp, uint32_t id)

    Get NUmber of spread sprectrum entry from the ASIC_InternalSS_Info table Ver 2.1 from the VBIOS There will not be multiple entry for Ver 2.1

    :param bp:
        *undescribed*
    :type bp: struct bios_parser \*

    :param id:
        *undescribed*
    :type id: uint32_t

.. _`get_ss_entry_number_from_internal_ss_info_tbl_v2_1.description`:

Description
-----------

\ ``param``\  id, spread sprectrum info index
\ ``return``\  number of SS Entry that match the id

.. _`get_ss_entry_number_from_internal_ss_info_tbl_v3_1`:

get_ss_entry_number_from_internal_ss_info_tbl_V3_1
==================================================

.. c:function:: uint32_t get_ss_entry_number_from_internal_ss_info_tbl_V3_1(struct bios_parser *bp, uint32_t id)

    Get Number of SpreadSpectrum Entry from the ASIC_InternalSS_Info table of the VBIOS that matches id

    :param bp:
        *undescribed*
    :type bp: struct bios_parser \*

    :param id:
        *undescribed*
    :type id: uint32_t

.. _`get_ss_entry_number_from_internal_ss_info_tbl_v3_1.description`:

Description
-----------

\ ``param``\ [in]  id, spread sprectrum id
\ ``return``\  number of SS Entry that match the id

.. _`bios_parser_get_gpio_pin_info`:

bios_parser_get_gpio_pin_info
=============================

.. c:function:: enum bp_result bios_parser_get_gpio_pin_info(struct dc_bios *dcb, uint32_t gpio_id, struct gpio_pin_info *info)

    Get GpioPin information of input gpio id

    :param dcb:
        *undescribed*
    :type dcb: struct dc_bios \*

    :param gpio_id:
        *undescribed*
    :type gpio_id: uint32_t

    :param info:
        *undescribed*
    :type info: struct gpio_pin_info \*

.. _`bios_parser_get_gpio_pin_info.description`:

Description
-----------

\ ``param``\  gpio_id, GPIO ID
\ ``param``\  info, GpioPin information structure
\ ``return``\  Bios parser result code
\ ``note``\ 
to get the GPIO PIN INFO, we need:
1. get the GPIO_ID from other object table, see \ :c:func:`GetHPDInfo`\ 
2. in DATA_TABLE.GPIO_Pin_LUT, search all records, to get the registerA
offset/mask

.. _`bios_parser_set_scratch_critical_state`:

bios_parser_set_scratch_critical_state
======================================

.. c:function:: void bios_parser_set_scratch_critical_state(struct dc_bios *dcb, bool state)

    :param dcb:
        *undescribed*
    :type dcb: struct dc_bios \*

    :param state:
        *undescribed*
    :type state: bool

.. _`bios_parser_set_scratch_critical_state.description`:

Description
-----------

\ ``brief``\ 
update critical state bit in VBIOS scratch register

\ ``param``\ 
bool - to set or reset state

.. This file was automatic generated / don't edit.

