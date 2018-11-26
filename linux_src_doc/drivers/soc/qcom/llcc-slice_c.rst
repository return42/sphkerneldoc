.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/llcc-slice.c

.. _`llcc_slice_getd`:

llcc_slice_getd
===============

.. c:function:: struct llcc_slice_desc *llcc_slice_getd(u32 uid)

    get llcc slice descriptor

    :param uid:
        usecase_id for the client
    :type uid: u32

.. _`llcc_slice_getd.description`:

Description
-----------

A pointer to llcc slice descriptor will be returned on success and
and error pointer is returned on failure

.. _`llcc_slice_putd`:

llcc_slice_putd
===============

.. c:function:: void llcc_slice_putd(struct llcc_slice_desc *desc)

    llcc slice descritpor

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

.. _`llcc_slice_activate.description`:

Description
-----------

A value of zero will be returned on success and a negative errno will
be returned in error cases

.. _`llcc_slice_deactivate`:

llcc_slice_deactivate
=====================

.. c:function:: int llcc_slice_deactivate(struct llcc_slice_desc *desc)

    Deactivate the llcc slice

    :param desc:
        Pointer to llcc slice descriptor
    :type desc: struct llcc_slice_desc \*

.. _`llcc_slice_deactivate.description`:

Description
-----------

A value of zero will be returned on success and a negative errno will
be returned in error cases

.. _`llcc_get_slice_id`:

llcc_get_slice_id
=================

.. c:function:: int llcc_get_slice_id(struct llcc_slice_desc *desc)

    return the slice id

    :param desc:
        Pointer to llcc slice descriptor
    :type desc: struct llcc_slice_desc \*

.. _`llcc_get_slice_size`:

llcc_get_slice_size
===================

.. c:function:: size_t llcc_get_slice_size(struct llcc_slice_desc *desc)

    return the slice id

    :param desc:
        Pointer to llcc slice descriptor
    :type desc: struct llcc_slice_desc \*

.. This file was automatic generated / don't edit.

