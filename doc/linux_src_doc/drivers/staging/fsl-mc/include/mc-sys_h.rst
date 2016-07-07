.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/include/mc-sys.h

.. _`fsl_mc_io_atomic_context_portal`:

FSL_MC_IO_ATOMIC_CONTEXT_PORTAL
===============================

.. c:function::  FSL_MC_IO_ATOMIC_CONTEXT_PORTAL()

.. _`fsl_mc_io`:

struct fsl_mc_io
================

.. c:type:: struct fsl_mc_io

    MC I/O object to be passed-in to \ :c:func:`mc_send_command`\ 

.. _`fsl_mc_io.definition`:

Definition
----------

.. code-block:: c

    struct fsl_mc_io {
        struct device *dev;
        u16 flags;
        u16 portal_size;
        phys_addr_t portal_phys_addr;
        void __iomem *portal_virt_addr;
        struct fsl_mc_device *dpmcp_dev;
        union {unnamed_union};
    }

.. _`fsl_mc_io.members`:

Members
-------

dev
    device associated with this Mc I/O object

flags
    flags for \ :c:func:`mc_send_command`\ 

portal_size
    MC command portal size in bytes

portal_phys_addr
    MC command portal physical address

portal_virt_addr
    MC command portal virtual address

dpmcp_dev
    pointer to the DPMCP device associated with the MC portal.

{unnamed_union}
    anonymous


.. _`fsl_mc_io.description`:

Description
-----------

Fields are only meaningful if the FSL_MC_IO_ATOMIC_CONTEXT_PORTAL flag is not

Fields are only meaningful if the FSL_MC_IO_ATOMIC_CONTEXT_PORTAL flag is

.. This file was automatic generated / don't edit.

