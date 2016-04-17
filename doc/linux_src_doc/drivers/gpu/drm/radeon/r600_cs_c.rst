.. -*- coding: utf-8; mode: rst -*-

=========
r600_cs.c
=========


.. _`r600_cs_packet_parse_vline`:

r600_cs_packet_parse_vline
==========================

.. c:function:: int r600_cs_packet_parse_vline (struct radeon_cs_parser *p)

    parse userspace VLINE packet

    :param struct radeon_cs_parser \*p:

        *undescribed*



.. _`r600_cs_packet_parse_vline.description`:

Description
-----------

This is an R600-specific function for parsing VLINE packets.
Real work is done by r600_cs_common_vline_parse function.
Here we just set up ASIC-specific register table and call
the common implementation function.



.. _`r600_cs_common_vline_parse`:

r600_cs_common_vline_parse
==========================

.. c:function:: int r600_cs_common_vline_parse (struct radeon_cs_parser *p, uint32_t *vline_start_end, uint32_t *vline_status)

    common vline parser

    :param struct radeon_cs_parser \*p:

        *undescribed*

    :param uint32_t \*vline_start_end:
        table of vline_start_end registers

    :param uint32_t \*vline_status:
        table of vline_status registers



.. _`r600_cs_common_vline_parse.description`:

Description
-----------

Userspace sends a special sequence for VLINE waits.
PACKET0 - VLINE_START_END + value
PACKET3 - WAIT_REG_MEM poll vline status reg
RELOC (P3) - crtc_id in reloc.

This function parses this and relocates the VLINE START END
and WAIT_REG_MEM packets to the correct crtc.
It also detects a switched off crtc and nulls out the
wait in that case. This function is common for all ASICs that
are R600 and newer. The parsing algorithm is the same, and only
differs in which registers are used.

Caller is the ASIC-specific function which passes the parser
context and ASIC-specific register table



.. _`r600_cs_check_reg`:

r600_cs_check_reg
=================

.. c:function:: int r600_cs_check_reg (struct radeon_cs_parser *p, u32 reg, u32 idx)

    check if register is authorized or not

    :param struct radeon_cs_parser \*p:

        *undescribed*

    :param u32 reg:
        register we are testing

    :param u32 idx:
        index into the cs buffer



.. _`r600_cs_check_reg.description`:

Description
-----------

This function will test against r600_reg_safe_bm and return 0
if register is safe. If register is not flag as safe this function
will test it against a list of register needind special handling.



.. _`r600_check_texture_resource`:

r600_check_texture_resource
===========================

.. c:function:: int r600_check_texture_resource (struct radeon_cs_parser *p, u32 idx, struct radeon_bo *texture, struct radeon_bo *mipmap, u64 base_offset, u64 mip_offset, u32 tiling_flags)

    check if register is authorized or not

    :param struct radeon_cs_parser \*p:
        parser structure holding parsing context

    :param u32 idx:
        index into the cs buffer

    :param struct radeon_bo \*texture:
        texture's bo structure

    :param struct radeon_bo \*mipmap:
        mipmap's bo structure

    :param u64 base_offset:

        *undescribed*

    :param u64 mip_offset:

        *undescribed*

    :param u32 tiling_flags:

        *undescribed*



.. _`r600_check_texture_resource.description`:

Description
-----------

This function will check that the resource has valid field and that
the texture and mipmap bo object are big enough to cover this resource.



.. _`r600_dma_cs_next_reloc`:

r600_dma_cs_next_reloc
======================

.. c:function:: int r600_dma_cs_next_reloc (struct radeon_cs_parser *p, struct radeon_bo_list **cs_reloc)

    parse next reloc

    :param struct radeon_cs_parser \*p:
        parser structure holding parsing context.

    :param struct radeon_bo_list \*\*cs_reloc:
        reloc informations



.. _`r600_dma_cs_next_reloc.description`:

Description
-----------

Return the next reloc, do bo validation and compute
GPU offset using the provided start.



.. _`r600_dma_cs_parse`:

r600_dma_cs_parse
=================

.. c:function:: int r600_dma_cs_parse (struct radeon_cs_parser *p)

    parse the DMA IB

    :param struct radeon_cs_parser \*p:
        parser structure holding parsing context.



.. _`r600_dma_cs_parse.description`:

Description
-----------

Parses the DMA IB from the CS ioctl and updates
the GPU addresses based on the reloc information and
checks for errors. (R6xx-R7xx)
Returns 0 for success and an error on failure.

