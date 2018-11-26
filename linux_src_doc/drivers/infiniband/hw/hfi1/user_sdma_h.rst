.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/user_sdma.h

.. _`ahg_header_set`:

ahg_header_set
==============

.. c:function:: int ahg_header_set(u32 *arr, int idx, size_t array_size, u8 dw, u8 bit, u8 width, u16 value)

    \ ``arr``\         - Array to save the descriptor to. \ ``idx``\         - Index of the array at which the descriptor will be saved. \ ``array_size``\  - Size of the array arr. \ ``dw``\          - Update index into the header in DWs. \ ``bit``\         - Start bit. \ ``width``\       - Field width. \ ``value``\       - 16 bits of immediate data to write into the field. Returns -ERANGE if idx is invalid. If successful, returns the next index (idx + 1) of the array to be used for the next descriptor.

    :param arr:
        *undescribed*
    :type arr: u32 \*

    :param idx:
        *undescribed*
    :type idx: int

    :param array_size:
        *undescribed*
    :type array_size: size_t

    :param dw:
        *undescribed*
    :type dw: u8

    :param bit:
        *undescribed*
    :type bit: u8

    :param width:
        *undescribed*
    :type width: u8

    :param value:
        *undescribed*
    :type value: u16

.. This file was automatic generated / don't edit.

