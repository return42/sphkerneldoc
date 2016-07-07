.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/i40iw/i40iw.h

.. _`to_iwdev`:

to_iwdev
========

.. c:function:: struct i40iw_device *to_iwdev(struct ib_device *ibdev)

    get device

    :param struct ib_device \*ibdev:
        ib device

.. _`to_ucontext`:

to_ucontext
===========

.. c:function:: struct i40iw_ucontext *to_ucontext(struct ib_ucontext *ibucontext)

    get user context

    :param struct ib_ucontext \*ibucontext:
        ib user context

.. _`to_iwpd`:

to_iwpd
=======

.. c:function:: struct i40iw_pd *to_iwpd(struct ib_pd *ibpd)

    get protection domain

    :param struct ib_pd \*ibpd:
        ib pd

.. _`to_iwmr`:

to_iwmr
=======

.. c:function:: struct i40iw_mr *to_iwmr(struct ib_mr *ibmr)

    get device memory region

    :param struct ib_mr \*ibmr:
        *undescribed*

.. _`to_iwmr_from_ibfmr`:

to_iwmr_from_ibfmr
==================

.. c:function:: struct i40iw_mr *to_iwmr_from_ibfmr(struct ib_fmr *ibfmr)

    get device memory region

    :param struct ib_fmr \*ibfmr:
        ib fmr

.. _`to_iwmw`:

to_iwmw
=======

.. c:function:: struct i40iw_mr *to_iwmw(struct ib_mw *ibmw)

    get device memory window

    :param struct ib_mw \*ibmw:
        ib memory window

.. _`to_iwcq`:

to_iwcq
=======

.. c:function:: struct i40iw_cq *to_iwcq(struct ib_cq *ibcq)

    get completion queue

    :param struct ib_cq \*ibcq:
        ib cqdevice

.. _`to_iwqp`:

to_iwqp
=======

.. c:function:: struct i40iw_qp *to_iwqp(struct ib_qp *ibqp)

    get device qp

    :param struct ib_qp \*ibqp:
        ib qp

.. _`i40iw_alloc_resource`:

i40iw_alloc_resource
====================

.. c:function:: int i40iw_alloc_resource(struct i40iw_device *iwdev, unsigned long *resource_array, u32 max_resources, u32 *req_resource_num, u32 *next)

    allocate a resource

    :param struct i40iw_device \*iwdev:
        device pointer

    :param unsigned long \*resource_array:
        resource bit array:

    :param u32 max_resources:
        maximum resource number

    :param u32 \*req_resource_num:
        *undescribed*

    :param u32 \*next:
        next free id

.. _`i40iw_is_resource_allocated`:

i40iw_is_resource_allocated
===========================

.. c:function:: bool i40iw_is_resource_allocated(struct i40iw_device *iwdev, unsigned long *resource_array, u32 resource_num)

    detrmine if resource is allocated

    :param struct i40iw_device \*iwdev:
        device pointer

    :param unsigned long \*resource_array:
        resource array for the resource_num

    :param u32 resource_num:
        resource number to check

.. _`i40iw_free_resource`:

i40iw_free_resource
===================

.. c:function:: void i40iw_free_resource(struct i40iw_device *iwdev, unsigned long *resource_array, u32 resource_num)

    free a resource

    :param struct i40iw_device \*iwdev:
        device pointer

    :param unsigned long \*resource_array:
        resource array for the resource_num

    :param u32 resource_num:
        resource number to free

.. _`to_iwhdl`:

to_iwhdl
========

.. c:function:: struct i40iw_handler *to_iwhdl(struct i40iw_device *iw_dev)

    Get the handler from the device pointer

    :param struct i40iw_device \*iw_dev:
        *undescribed*

.. _`i40iw_initialize_hw_resources`:

i40iw_initialize_hw_resources
=============================

.. c:function:: u32 i40iw_initialize_hw_resources(struct i40iw_device *iwdev)

    :param struct i40iw_device \*iwdev:
        *undescribed*

.. This file was automatic generated / don't edit.

