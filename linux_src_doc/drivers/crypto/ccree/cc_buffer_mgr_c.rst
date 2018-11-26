.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/ccree/cc_buffer_mgr.c

.. _`cc_copy_mac`:

cc_copy_mac
===========

.. c:function:: void cc_copy_mac(struct device *dev, struct aead_request *req, enum cc_sg_cpy_direct dir)

    Copy MAC to temporary location

    :param dev:
        device object
    :type dev: struct device \*

    :param req:
        aead request object
    :type req: struct aead_request \*

    :param dir:
        [IN] copy from/to sgl
    :type dir: enum cc_sg_cpy_direct

.. _`cc_get_sgl_nents`:

cc_get_sgl_nents
================

.. c:function:: unsigned int cc_get_sgl_nents(struct device *dev, struct scatterlist *sg_list, unsigned int nbytes, u32 *lbytes, bool *is_chained)

    Get scatterlist number of entries.

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param sg_list:
        SG list
    :type sg_list: struct scatterlist \*

    :param nbytes:
        [IN] Total SGL data bytes.
    :type nbytes: unsigned int

    :param lbytes:
        [OUT] Returns the amount of bytes at the last entry
    :type lbytes: u32 \*

    :param is_chained:
        *undescribed*
    :type is_chained: bool \*

.. _`cc_zero_sgl`:

cc_zero_sgl
===========

.. c:function:: void cc_zero_sgl(struct scatterlist *sgl, u32 data_len)

    Zero scatter scatter list data.

    :param sgl:
        *undescribed*
    :type sgl: struct scatterlist \*

    :param data_len:
        *undescribed*
    :type data_len: u32

.. _`cc_copy_sg_portion`:

cc_copy_sg_portion
==================

.. c:function:: void cc_copy_sg_portion(struct device *dev, u8 *dest, struct scatterlist *sg, u32 to_skip, u32 end, enum cc_sg_cpy_direct direct)

    Copy scatter list data, from to_skip to end, to dest and vice versa

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param dest:
        *undescribed*
    :type dest: u8 \*

    :param sg:
        *undescribed*
    :type sg: struct scatterlist \*

    :param to_skip:
        *undescribed*
    :type to_skip: u32

    :param end:
        *undescribed*
    :type end: u32

    :param direct:
        *undescribed*
    :type direct: enum cc_sg_cpy_direct

.. This file was automatic generated / don't edit.

