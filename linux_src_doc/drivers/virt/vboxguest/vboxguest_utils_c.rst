.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virt/vboxguest/vboxguest_utils.c

.. _`hgcm_call_preprocess`:

hgcm_call_preprocess
====================

.. c:function:: int hgcm_call_preprocess(const struct vmmdev_hgcm_function_parameter *src_parm, u32 parm_count, void ***bounce_bufs_ret, size_t *extra)

    figure out how much extra storage we need for page lists.

    :param const struct vmmdev_hgcm_function_parameter \*src_parm:
        Pointer to source function call parameters

    :param u32 parm_count:
        Number of function call parameters.

    :param void \*\*\*bounce_bufs_ret:
        Where to return the allocated bouncebuffer array

    :param size_t \*extra:
        Where to return the extra request space needed for
        physical page lists.

.. _`hgcm_call_preprocess.return`:

Return
------

0 or negative errno value.

.. _`hgcm_call_linear_addr_type_to_pagelist_flags`:

hgcm_call_linear_addr_type_to_pagelist_flags
============================================

.. c:function:: u32 hgcm_call_linear_addr_type_to_pagelist_flags(enum vmmdev_hgcm_function_parameter_type type)

    :param enum vmmdev_hgcm_function_parameter_type type:
        The type.

.. _`hgcm_call_linear_addr_type_to_pagelist_flags.return`:

Return
------

page list flags.

.. _`hgcm_call_init_call`:

hgcm_call_init_call
===================

.. c:function:: void hgcm_call_init_call(struct vmmdev_hgcm_call *call, u32 client_id, u32 function, const struct vmmdev_hgcm_function_parameter *src_parm, u32 parm_count, void **bounce_bufs)

    :param struct vmmdev_hgcm_call \*call:
        The call to initialize.

    :param u32 client_id:
        The client ID of the caller.

    :param u32 function:
        The function number of the function to call.

    :param const struct vmmdev_hgcm_function_parameter \*src_parm:
        Pointer to source function call parameters.

    :param u32 parm_count:
        Number of function call parameters.

    :param void \*\*bounce_bufs:
        The bouncebuffer array.

.. _`hgcm_cancel_call`:

hgcm_cancel_call
================

.. c:function:: int hgcm_cancel_call(struct vbg_dev *gdev, struct vmmdev_hgcm_call *call)

    :param struct vbg_dev \*gdev:
        *undescribed*

    :param struct vmmdev_hgcm_call \*call:
        *undescribed*

.. _`hgcm_cancel_call.return`:

Return
------

VBox status code

.. _`vbg_hgcm_do_call`:

vbg_hgcm_do_call
================

.. c:function:: int vbg_hgcm_do_call(struct vbg_dev *gdev, struct vmmdev_hgcm_call *call, u32 timeout_ms, bool *leak_it)

    :param struct vbg_dev \*gdev:
        The VBoxGuest device extension.

    :param struct vmmdev_hgcm_call \*call:
        The call to execute.

    :param u32 timeout_ms:
        Timeout in ms.

    :param bool \*leak_it:
        Where to return the leak it / free it, indicator.
        Cancellation fun.

.. _`vbg_hgcm_do_call.return`:

Return
------

0 or negative errno value.

.. _`hgcm_call_copy_back_result`:

hgcm_call_copy_back_result
==========================

.. c:function:: int hgcm_call_copy_back_result(const struct vmmdev_hgcm_call *call, struct vmmdev_hgcm_function_parameter *dst_parm, u32 parm_count, void **bounce_bufs)

    buffers.

    :param const struct vmmdev_hgcm_call \*call:
        HGCM call request.

    :param struct vmmdev_hgcm_function_parameter \*dst_parm:
        Pointer to function call parameters destination.

    :param u32 parm_count:
        Number of function call parameters.

    :param void \*\*bounce_bufs:
        The bouncebuffer array.

.. _`hgcm_call_copy_back_result.return`:

Return
------

0 or negative errno value.

.. This file was automatic generated / don't edit.

