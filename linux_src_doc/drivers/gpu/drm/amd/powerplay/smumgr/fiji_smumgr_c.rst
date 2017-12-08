.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/powerplay/smumgr/fiji_smumgr.c

.. _`fiji_get_mclk_frequency_ratio`:

fiji_get_mclk_frequency_ratio
=============================

.. c:function:: uint8_t fiji_get_mclk_frequency_ratio(uint32_t mem_clock)

    SEQ_CG_RESP  Bit[31:24] - 0x0 Bit[27:24] \96 DDR3 Frequency ratio 0x0 <= 100MHz,       450 < 0x8 <= 500MHz 100 < 0x1 <= 150MHz,       500 < 0x9 <= 550MHz 150 < 0x2 <= 200MHz,       550 < 0xA <= 600MHz 200 < 0x3 <= 250MHz,       600 < 0xB <= 650MHz 250 < 0x4 <= 300MHz,       650 < 0xC <= 700MHz 300 < 0x5 <= 350MHz,       700 < 0xD <= 750MHz 350 < 0x6 <= 400MHz,       750 < 0xE <= 800MHz 400 < 0x7 <= 450MHz,       800 < 0xF

    :param uint32_t mem_clock:
        *undescribed*

.. This file was automatic generated / don't edit.

