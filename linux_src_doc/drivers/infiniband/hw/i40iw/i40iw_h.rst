.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw.h

.. _`to_iwdev`:

to_iwdev
========

.. c:function:: struct i40iw_device *to_iwdev(struct ib_device *ibdev)

    get device

    :param ibdev:
        ib device
    :type ibdev: struct ib_device \*

.. _`to_ucontext`:

to_ucontext
===========

.. c:function:: struct i40iw_ucontext *to_ucontext(struct ib_ucontext *ibucontext)

    get user context

    :param ibucontext:
        ib user context
    :type ibucontext: struct ib_ucontext \*

.. _`to_iwpd`:

to_iwpd
=======

.. c:function:: struct i40iw_pd *to_iwpd(struct ib_pd *ibpd)

    get protection domain

    :param ibpd:
        ib pd
    :type ibpd: struct ib_pd \*

.. _`to_iwmr`:

to_iwmr
=======

.. c:function:: struct i40iw_mr *to_iwmr(struct ib_mr *ibmr)

    get device memory region

    :param ibmr:
        *undescribed*
    :type ibmr: struct ib_mr \*

.. _`to_iwmr_from_ibfmr`:

to_iwmr_from_ibfmr
==================

.. c:function:: struct i40iw_mr *to_iwmr_from_ibfmr(struct ib_fmr *ibfmr)

    get device memory region

    :param ibfmr:
        ib fmr
    :type ibfmr: struct ib_fmr \*

.. _`to_iwmw`:

to_iwmw
=======

.. c:function:: struct i40iw_mr *to_iwmw(struct ib_mw *ibmw)

    get device memory window

    :param ibmw:
        ib memory window
    :type ibmw: struct ib_mw \*

.. _`to_iwcq`:

to_iwcq
=======

.. c:function:: struct i40iw_cq *to_iwcq(struct ib_cq *ibcq)

    get completion queue

    :param ibcq:
        ib cqdevice
    :type ibcq: struct ib_cq \*

.. _`to_iwqp`:

to_iwqp
=======

.. c:function:: struct i40iw_qp *to_iwqp(struct ib_qp *ibqp)

    get device qp

    :param ibqp:
        ib qp
    :type ibqp: struct ib_qp \*

.. _`i40iw_alloc_resource`:

i40iw_alloc_resource
====================

.. c:function:: int i40iw_alloc_resource(struct i40iw_device *iwdev, unsigned long *resource_array, u32 max_resources, u32 *req_resource_num, u32 *next)

    allocate a resource

    :param iwdev:
        device pointer
    :type iwdev: struct i40iw_device \*

    :param resource_array:
        resource bit array:
    :type resource_array: unsigned long \*

    :param max_resources:
        maximum resource number
    :type max_resources: u32

    :param req_resource_num:
        *undescribed*
    :type req_resource_num: u32 \*

    :param next:
        next free id
    :type next: u32 \*

.. _`i40iw_is_resource_allocated`:

i40iw_is_resource_allocated
===========================

.. c:function:: bool i40iw_is_resource_allocated(struct i40iw_device *iwdev, unsigned long *resource_array, u32 resource_num)

    detrmine if resource is allocated

    :param iwdev:
        device pointer
    :type iwdev: struct i40iw_device \*

    :param resource_array:
        resource array for the resource_num
    :type resource_array: unsigned long \*

    :param resource_num:
        resource number to check
    :type resource_num: u32

.. _`i40iw_free_resource`:

i40iw_free_resource
===================

.. c:function:: void i40iw_free_resource(struct i40iw_device *iwdev, unsigned long *resource_array, u32 resource_num)

    free a resource

    :param iwdev:
        device pointer
    :type iwdev: struct i40iw_device \*

    :param resource_array:
        resource array for the resource_num
    :type resource_array: unsigned long \*

    :param resource_num:
        resource number to free
    :type resource_num: u32

.. _`to_iwhdl`:

to_iwhdl
========

.. c:function:: struct i40iw_handler *to_iwhdl(struct i40iw_device *iw_dev)

    Get the handler from the device pointer

    :param iw_dev:
        *undescribed*
    :type iw_dev: struct i40iw_device \*

.. _`i40iw_initialize_hw_resources`:

i40iw_initialize_hw_resources
=============================

.. c:function:: u32 i40iw_initialize_hw_resources(struct i40iw_device *iwdev)

    :param iwdev:
        *undescribed*
    :type iwdev: struct i40iw_device \*

.. This file was automatic generated / don't edit.

