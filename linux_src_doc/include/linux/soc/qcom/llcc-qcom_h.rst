.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/soc/qcom/llcc-qcom.h

.. _`llcc_slice_getd`:

llcc_slice_getd
===============

.. c:function:: struct llcc_slice_desc *llcc_slice_getd(u32 uid)

    get llcc slice descriptor

    :param uid:
        usecase_id of the client
    :type uid: u32

.. _`llcc_slice_putd`:

llcc_slice_putd
===============

.. c:function:: void llcc_slice_putd(struct llcc_slice_desc *desc)

    llcc slice descritpor

    :param desc:
        Pointer to llcc slice descriptor
    :type desc: struct llcc_slice_desc \*

.. _`llcc_get_slice_id`:

llcc_get_slice_id
=================

.. c:function:: int llcc_get_slice_id(struct llcc_slice_desc *desc)

    get slice id

    :param desc:
        Pointer to llcc slice descriptor
    :type desc: struct llcc_slice_desc \*

.. _`llcc_get_slice_size`:

llcc_get_slice_size
===================

.. c:function:: size_t llcc_get_slice_size(struct llcc_slice_desc *desc)

    llcc slice size

    :param desc:
        Pointer to llcc slice descriptor
    :type desc: struct llcc_slice_desc \*

.. _`llcc_slice_activate`:

llcc_slice_activate
===================

.. c:function:: int llcc_slice_activate(struct llcc_slice_desc *desc)

    Activate the llcc slice

    :param desc:
        Pointer to llcc slice descriptor
    :type desc: struct llcc_slice_desc \*

.. _`llcc_slice_deactivate`:

llcc_slice_deactivate
=====================

.. c:function:: int llcc_slice_deactivate(struct llcc_slice_desc *desc)

    Deactivate the llcc slice

    :param desc:
        Pointer to llcc slice descriptor
    :type desc: struct llcc_slice_desc \*

.. _`qcom_llcc_probe`:

qcom_llcc_probe
===============

.. c:function:: int qcom_llcc_probe(struct platform_device *pdev, const struct llcc_slice_config *table, u32 sz)

    program the sct table

    :param pdev:
        platform device pointer
    :type pdev: struct platform_device \*

    :param table:
        soc sct table
    :type table: const struct llcc_slice_config \*

    :param sz:
        Size of the config table
    :type sz: u32

.. This file was automatic generated / don't edit.

