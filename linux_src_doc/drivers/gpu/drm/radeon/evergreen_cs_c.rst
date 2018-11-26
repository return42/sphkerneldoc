.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/evergreen_cs.c

.. _`evergreen_cs_packet_parse_vline`:

evergreen_cs_packet_parse_vline
===============================

.. c:function:: int evergreen_cs_packet_parse_vline(struct radeon_cs_parser *p)

    parse userspace VLINE packet

    :param p:
        *undescribed*
    :type p: struct radeon_cs_parser \*

.. _`evergreen_cs_packet_parse_vline.description`:

Description
-----------

This is an Evergreen(+)-specific function for parsing VLINE packets.
Real work is done by r600_cs_common_vline_parse function.
Here we just set up ASIC-specific register table and call
the common implementation function.

.. _`evergreen_cs_handle_reg`:

evergreen_cs_handle_reg
=======================

.. c:function:: int evergreen_cs_handle_reg(struct radeon_cs_parser *p, u32 reg, u32 idx)

    process registers that need special handling.

    :param p:
        *undescribed*
    :type p: struct radeon_cs_parser \*

    :param reg:
        register we are testing
    :type reg: u32

    :param idx:
        index into the cs buffer
    :type idx: u32

.. _`evergreen_is_safe_reg`:

evergreen_is_safe_reg
=====================

.. c:function:: bool evergreen_is_safe_reg(struct radeon_cs_parser *p, u32 reg)

    check if register is authorized or not

    :param p:
        *undescribed*
    :type p: struct radeon_cs_parser \*

    :param reg:
        register we are testing
    :type reg: u32

.. _`evergreen_is_safe_reg.description`:

Description
-----------

This function will test against reg_safe_bm and return true
if register is safe or false otherwise.

.. _`evergreen_dma_cs_parse`:

evergreen_dma_cs_parse
======================

.. c:function:: int evergreen_dma_cs_parse(struct radeon_cs_parser *p)

    parse the DMA IB

    :param p:
        parser structure holding parsing context.
    :type p: struct radeon_cs_parser \*

.. _`evergreen_dma_cs_parse.description`:

Description
-----------

Parses the DMA IB from the CS ioctl and updates
the GPU addresses based on the reloc information and
checks for errors. (Evergreen-Cayman)
Returns 0 for success and an error on failure.

.. _`evergreen_dma_ib_parse`:

evergreen_dma_ib_parse
======================

.. c:function:: int evergreen_dma_ib_parse(struct radeon_device *rdev, struct radeon_ib *ib)

    parse the DMA IB for VM

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param ib:
        radeon_ib pointer
    :type ib: struct radeon_ib \*

.. _`evergreen_dma_ib_parse.description`:

Description
-----------

Parses the DMA IB from the VM CS ioctl
checks for errors. (Cayman-SI)
Returns 0 for success and an error on failure.

.. This file was automatic generated / don't edit.

