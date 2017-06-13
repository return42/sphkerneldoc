.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/ccree/ssi_buffer_mgr.c

.. _`ssi_buffer_mgr_get_sgl_nents`:

ssi_buffer_mgr_get_sgl_nents
============================

.. c:function:: unsigned int ssi_buffer_mgr_get_sgl_nents(struct scatterlist *sg_list, unsigned int nbytes, uint32_t *lbytes, bool *is_chained)

    Get scatterlist number of entries.

    :param struct scatterlist \*sg_list:
        SG list

    :param unsigned int nbytes:
        [IN] Total SGL data bytes.

    :param uint32_t \*lbytes:
        [OUT] Returns the amount of bytes at the last entry

    :param bool \*is_chained:
        *undescribed*

.. _`ssi_buffer_mgr_zero_sgl`:

ssi_buffer_mgr_zero_sgl
=======================

.. c:function:: void ssi_buffer_mgr_zero_sgl(struct scatterlist *sgl, uint32_t data_len)

    Zero scatter scatter list data.

    :param struct scatterlist \*sgl:
        *undescribed*

    :param uint32_t data_len:
        *undescribed*

.. _`ssi_buffer_mgr_copy_scatterlist_portion`:

ssi_buffer_mgr_copy_scatterlist_portion
=======================================

.. c:function:: void ssi_buffer_mgr_copy_scatterlist_portion(u8 *dest, struct scatterlist *sg, uint32_t to_skip, uint32_t end, enum ssi_sg_cpy_direct direct)

    Copy scatter list data, from to_skip to end, to dest and vice versa

    :param u8 \*dest:
        *undescribed*

    :param struct scatterlist \*sg:
        *undescribed*

    :param uint32_t to_skip:
        *undescribed*

    :param uint32_t end:
        *undescribed*

    :param enum ssi_sg_cpy_direct direct:
        *undescribed*

.. This file was automatic generated / don't edit.

