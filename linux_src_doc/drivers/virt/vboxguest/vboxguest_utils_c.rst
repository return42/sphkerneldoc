.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virt/vboxguest/vboxguest_utils.c

.. _`hgcm_call_preprocess`:

hgcm_call_preprocess
====================

.. c:function:: int hgcm_call_preprocess(const struct vmmdev_hgcm_function_parameter *src_parm, u32 parm_count, void ***bounce_bufs_ret, size_t *extra)

    figure out how much extra storage we need for page lists.

    :param src_parm:
        Pointer to source function call parameters
    :type src_parm: const struct vmmdev_hgcm_function_parameter \*

    :param parm_count:
        Number of function call parameters.
    :type parm_count: u32

    :param bounce_bufs_ret:
        Where to return the allocated bouncebuffer array
    :type bounce_bufs_ret: void \*\*\*

    :param extra:
        Where to return the extra request space needed for
        physical page lists.
    :type extra: size_t \*

.. _`hgcm_call_preprocess.return`:

Return
------

0 or negative errno value.

.. _`hgcm_call_linear_addr_type_to_pagelist_flags`:

hgcm_call_linear_addr_type_to_pagelist_flags
============================================

.. c:function:: u32 hgcm_call_linear_addr_type_to_pagelist_flags(enum vmmdev_hgcm_function_parameter_type type)

    :param type:
        The type.
    :type type: enum vmmdev_hgcm_function_parameter_type

.. _`hgcm_call_linear_addr_type_to_pagelist_flags.return`:

Return
------

page list flags.

.. _`hgcm_call_init_call`:

hgcm_call_init_call
===================

.. c:function:: void hgcm_call_init_call(struct vmmdev_hgcm_call *call, u32 client_id, u32 function, const struct vmmdev_hgcm_function_parameter *src_parm, u32 parm_count, void **bounce_bufs)

    :param call:
        The call to initialize.
    :type call: struct vmmdev_hgcm_call \*

    :param client_id:
        The client ID of the caller.
    :type client_id: u32

    :param function:
        The function number of the function to call.
    :type function: u32

    :param src_parm:
        Pointer to source function call parameters.
    :type src_parm: const struct vmmdev_hgcm_function_parameter \*

    :param parm_count:
        Number of function call parameters.
    :type parm_count: u32

    :param bounce_bufs:
        The bouncebuffer array.
    :type bounce_bufs: void \*\*

.. _`hgcm_cancel_call`:

hgcm_cancel_call
================

.. c:function:: int hgcm_cancel_call(struct vbg_dev *gdev, struct vmmdev_hgcm_call *call)

    :param gdev:
        *undescribed*
    :type gdev: struct vbg_dev \*

    :param call:
        *undescribed*
    :type call: struct vmmdev_hgcm_call \*

.. _`hgcm_cancel_call.return`:

Return
------

VBox status code

.. _`vbg_hgcm_do_call`:

vbg_hgcm_do_call
================

.. c:function:: int vbg_hgcm_do_call(struct vbg_dev *gdev, struct vmmdev_hgcm_call *call, u32 timeout_ms, bool *leak_it)

    :param gdev:
        The VBoxGuest device extension.
    :type gdev: struct vbg_dev \*

    :param call:
        The call to execute.
    :type call: struct vmmdev_hgcm_call \*

    :param timeout_ms:
        Timeout in ms.
    :type timeout_ms: u32

    :param leak_it:
        Where to return the leak it / free it, indicator.
        Cancellation fun.
    :type leak_it: bool \*

.. _`vbg_hgcm_do_call.return`:

Return
------

0 or negative errno value.

.. _`hgcm_call_copy_back_result`:

hgcm_call_copy_back_result
==========================

.. c:function:: int hgcm_call_copy_back_result(const struct vmmdev_hgcm_call *call, struct vmmdev_hgcm_function_parameter *dst_parm, u32 parm_count, void **bounce_bufs)

    buffers.

    :param call:
        HGCM call request.
    :type call: const struct vmmdev_hgcm_call \*

    :param dst_parm:
        Pointer to function call parameters destination.
    :type dst_parm: struct vmmdev_hgcm_function_parameter \*

    :param parm_count:
        Number of function call parameters.
    :type parm_count: u32

    :param bounce_bufs:
        The bouncebuffer array.
    :type bounce_bufs: void \*\*

.. _`hgcm_call_copy_back_result.return`:

Return
------

0 or negative errno value.

.. This file was automatic generated / don't edit.

