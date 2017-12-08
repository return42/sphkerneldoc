.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/user_sdma.h

.. _`ahg_header_set`:

ahg_header_set
==============

.. c:function:: int ahg_header_set(u32 *arr, int idx, size_t array_size, u8 dw, u8 bit, u8 width, u16 value)

    @arr        - Array to save the descriptor to. \ ``idx``\         - Index of the array at which the descriptor will be saved. \ ``array_size``\  - Size of the array arr. \ ``dw``\          - Update index into the header in DWs. \ ``bit``\         - Start bit. \ ``width``\       - Field width. \ ``value``\       - 16 bits of immediate data to write into the field. Returns -ERANGE if idx is invalid. If successful, returns the next index (idx + 1) of the array to be used for the next descriptor.

    :param u32 \*arr:
        *undescribed*

    :param int idx:
        *undescribed*

    :param size_t array_size:
        *undescribed*

    :param u8 dw:
        *undescribed*

    :param u8 bit:
        *undescribed*

    :param u8 width:
        *undescribed*

    :param u16 value:
        *undescribed*

.. This file was automatic generated / don't edit.

