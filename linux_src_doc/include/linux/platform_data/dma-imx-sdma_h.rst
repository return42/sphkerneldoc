.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/dma-imx-sdma.h

.. _`sdma_script_start_addrs`:

struct sdma_script_start_addrs
==============================

.. c:type:: struct sdma_script_start_addrs

    SDMA script start pointers

.. _`sdma_script_start_addrs.definition`:

Definition
----------

.. code-block:: c

    struct sdma_script_start_addrs {
        s32 ap_2_ap_addr;
        s32 ap_2_bp_addr;
        s32 ap_2_ap_fixed_addr;
        s32 bp_2_ap_addr;
        s32 loopback_on_dsp_side_addr;
        s32 mcu_interrupt_only_addr;
        s32 firi_2_per_addr;
        s32 firi_2_mcu_addr;
        s32 per_2_firi_addr;
        s32 mcu_2_firi_addr;
        s32 uart_2_per_addr;
        s32 uart_2_mcu_addr;
        s32 per_2_app_addr;
        s32 mcu_2_app_addr;
        s32 per_2_per_addr;
        s32 uartsh_2_per_addr;
        s32 uartsh_2_mcu_addr;
        s32 per_2_shp_addr;
        s32 mcu_2_shp_addr;
        s32 ata_2_mcu_addr;
        s32 mcu_2_ata_addr;
        s32 app_2_per_addr;
        s32 app_2_mcu_addr;
        s32 shp_2_per_addr;
        s32 shp_2_mcu_addr;
        s32 mshc_2_mcu_addr;
        s32 mcu_2_mshc_addr;
        s32 spdif_2_mcu_addr;
        s32 mcu_2_spdif_addr;
        s32 asrc_2_mcu_addr;
        s32 ext_mem_2_ipu_addr;
        s32 descrambler_addr;
        s32 dptc_dvfs_addr;
        s32 utra_addr;
        s32 ram_code_start_addr;
        s32 mcu_2_ssish_addr;
        s32 ssish_2_mcu_addr;
        s32 hdmi_dma_addr;
        s32 zcanfd_2_mcu_addr;
        s32 zqspi_2_mcu_addr;
    }

.. _`sdma_script_start_addrs.members`:

Members
-------

ap_2_ap_addr
    *undescribed*

ap_2_bp_addr
    *undescribed*

ap_2_ap_fixed_addr
    *undescribed*

bp_2_ap_addr
    *undescribed*

loopback_on_dsp_side_addr
    *undescribed*

mcu_interrupt_only_addr
    *undescribed*

firi_2_per_addr
    *undescribed*

firi_2_mcu_addr
    *undescribed*

per_2_firi_addr
    *undescribed*

mcu_2_firi_addr
    *undescribed*

uart_2_per_addr
    *undescribed*

uart_2_mcu_addr
    *undescribed*

per_2_app_addr
    *undescribed*

mcu_2_app_addr
    *undescribed*

per_2_per_addr
    *undescribed*

uartsh_2_per_addr
    *undescribed*

uartsh_2_mcu_addr
    *undescribed*

per_2_shp_addr
    *undescribed*

mcu_2_shp_addr
    *undescribed*

ata_2_mcu_addr
    *undescribed*

mcu_2_ata_addr
    *undescribed*

app_2_per_addr
    *undescribed*

app_2_mcu_addr
    *undescribed*

shp_2_per_addr
    *undescribed*

shp_2_mcu_addr
    *undescribed*

mshc_2_mcu_addr
    *undescribed*

mcu_2_mshc_addr
    *undescribed*

spdif_2_mcu_addr
    *undescribed*

mcu_2_spdif_addr
    *undescribed*

asrc_2_mcu_addr
    *undescribed*

ext_mem_2_ipu_addr
    *undescribed*

descrambler_addr
    *undescribed*

dptc_dvfs_addr
    *undescribed*

utra_addr
    *undescribed*

ram_code_start_addr
    *undescribed*

mcu_2_ssish_addr
    *undescribed*

ssish_2_mcu_addr
    *undescribed*

hdmi_dma_addr
    *undescribed*

zcanfd_2_mcu_addr
    *undescribed*

zqspi_2_mcu_addr
    *undescribed*

.. _`sdma_script_start_addrs.description`:

Description
-----------

start addresses of the different functions in the physical
address space of the SDMA engine.

.. _`sdma_platform_data`:

struct sdma_platform_data
=========================

.. c:type:: struct sdma_platform_data

    platform specific data for SDMA engine

.. _`sdma_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct sdma_platform_data {
        char *fw_name;
        struct sdma_script_start_addrs *script_addrs;
    }

.. _`sdma_platform_data.members`:

Members
-------

fw_name
    *undescribed*

script_addrs
    *undescribed*

.. _`sdma_platform_data.description`:

Description
-----------

@fw_name             The firmware name
\ ``script_addrs``\         SDMA scripts addresses in SDMA ROM

.. This file was automatic generated / don't edit.

