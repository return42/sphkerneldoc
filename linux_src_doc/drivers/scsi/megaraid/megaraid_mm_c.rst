.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/megaraid/megaraid_mm.c

.. _`mraid_mm_open`:

mraid_mm_open
=============

.. c:function:: int mraid_mm_open(struct inode *inode, struct file *filep)

    open routine for char node interface

    :param struct inode \*inode:
        unused

    :param struct file \*filep:
        unused

.. _`mraid_mm_open.description`:

Description
-----------

Allow ioctl operations by apps only if they have superuser privilege.

.. _`mraid_mm_ioctl`:

mraid_mm_ioctl
==============

.. c:function:: int mraid_mm_ioctl(struct file *filep, unsigned int cmd, unsigned long arg)

    module entry-point for ioctls

    :param struct file \*filep:
        file operations pointer (ignored)

    :param unsigned int cmd:
        ioctl command

    :param unsigned long arg:
        user ioctl packet

.. _`mraid_mm_get_adapter`:

mraid_mm_get_adapter
====================

.. c:function:: mraid_mmadp_t *mraid_mm_get_adapter(mimd_t __user *umimd, int *rval)

    Returns corresponding adapters for the mimd packet

    :param mimd_t __user \*umimd:
        User space mimd_t ioctl packet

    :param int \*rval:
        returned success/error status

.. _`mraid_mm_get_adapter.description`:

Description
-----------

The function return value is a pointer to the located \ ``adapter``\ .

.. _`handle_drvrcmd`:

handle_drvrcmd
==============

.. c:function:: int handle_drvrcmd(void __user *arg, uint8_t old_ioctl, int *rval)

    Checks if the opcode is a driver cmd and if it is, handles it.

    :param void __user \*arg:
        packet sent by the user app

    :param uint8_t old_ioctl:
        mimd if 1; uioc otherwise

    :param int \*rval:
        pointer for command's returned value (not function status)

.. _`mimd_to_kioc`:

mimd_to_kioc
============

.. c:function:: int mimd_to_kioc(mimd_t __user *umimd, mraid_mmadp_t *adp, uioc_t *kioc)

    Converter from old to new ioctl format

    :param mimd_t __user \*umimd:
        user space old MIMD IOCTL

    :param mraid_mmadp_t \*adp:
        adapter softstate

    :param uioc_t \*kioc:
        kernel space new format IOCTL

.. _`mimd_to_kioc.description`:

Description
-----------

Routine to convert MIMD interface IOCTL to new interface IOCTL packet. The
new packet is in kernel space so that driver can perform operations on it
freely.

.. _`mraid_mm_attach_buf`:

mraid_mm_attach_buf
===================

.. c:function:: int mraid_mm_attach_buf(mraid_mmadp_t *adp, uioc_t *kioc, int xferlen)

    Attach a free dma buffer for required size

    :param mraid_mmadp_t \*adp:
        Adapter softstate

    :param uioc_t \*kioc:
        kioc that the buffer needs to be attached to

    :param int xferlen:
        required length for buffer

.. _`mraid_mm_attach_buf.description`:

Description
-----------

First we search for a pool with smallest buffer that is >= \ ``xferlen``\ . If
that pool has no free buffer, we will try for the next bigger size. If none
is available, we will try to allocate the smallest buffer that is >=
\ ``xferlen``\  and attach it the pool.

.. _`mraid_mm_alloc_kioc`:

mraid_mm_alloc_kioc
===================

.. c:function:: uioc_t *mraid_mm_alloc_kioc(mraid_mmadp_t *adp)

    Returns a uioc_t from free list

    :param mraid_mmadp_t \*adp:
        Adapter softstate for this module

.. _`mraid_mm_alloc_kioc.description`:

Description
-----------

The kioc_semaphore is initialized with number of kioc nodes in the
free kioc pool. If the kioc pool is empty, this function blocks till
a kioc becomes free.

.. _`mraid_mm_dealloc_kioc`:

mraid_mm_dealloc_kioc
=====================

.. c:function:: void mraid_mm_dealloc_kioc(mraid_mmadp_t *adp, uioc_t *kioc)

    Return kioc to free pool

    :param mraid_mmadp_t \*adp:
        Adapter softstate

    :param uioc_t \*kioc:
        uioc_t node to be returned to free pool

.. _`lld_ioctl`:

lld_ioctl
=========

.. c:function:: int lld_ioctl(mraid_mmadp_t *adp, uioc_t *kioc)

    Routine to issue ioctl to low level drvr

    :param mraid_mmadp_t \*adp:
        The adapter handle

    :param uioc_t \*kioc:
        The ioctl packet with kernel addresses

.. _`ioctl_done`:

ioctl_done
==========

.. c:function:: void ioctl_done(uioc_t *kioc)

    callback from the low level driver

    :param uioc_t \*kioc:
        completed ioctl packet

.. _`lld_timedout`:

lld_timedout
============

.. c:function:: void lld_timedout(struct timer_list *t)

    callback from the expired timer

    :param struct timer_list \*t:
        timer that timed out

.. _`kioc_to_mimd`:

kioc_to_mimd
============

.. c:function:: int kioc_to_mimd(uioc_t *kioc, mimd_t __user *mimd)

    Converter from new back to old format

    :param uioc_t \*kioc:
        Kernel space IOCTL packet (successfully issued)

    :param mimd_t __user \*mimd:
        User space MIMD packet

.. _`hinfo_to_cinfo`:

hinfo_to_cinfo
==============

.. c:function:: void hinfo_to_cinfo(mraid_hba_info_t *hinfo, mcontroller_t *cinfo)

    Convert new format hba info into old format

    :param mraid_hba_info_t \*hinfo:
        New format, more comprehensive adapter info

    :param mcontroller_t \*cinfo:
        Old format adapter info to support mimd_t apps

.. _`mraid_mm_register_adp`:

mraid_mm_register_adp
=====================

.. c:function:: int mraid_mm_register_adp(mraid_mmadp_t *lld_adp)

    Registration routine for low level drivers

    :param mraid_mmadp_t \*lld_adp:
        Adapter object

.. _`mraid_mm_adapter_app_handle`:

mraid_mm_adapter_app_handle
===========================

.. c:function:: uint32_t mraid_mm_adapter_app_handle(uint32_t unique_id)

    return the application handle for this adapter

    :param uint32_t unique_id:
        adapter unique identifier

.. _`mraid_mm_adapter_app_handle.description`:

Description
-----------

For the given driver data, locate the adapter in our global list and
return the corresponding handle, which is also used by applications to
uniquely identify an adapter.

Return adapter handle if found in the list.
Return 0 if adapter could not be located, should never happen though.

.. _`mraid_mm_setup_dma_pools`:

mraid_mm_setup_dma_pools
========================

.. c:function:: int mraid_mm_setup_dma_pools(mraid_mmadp_t *adp)

    Set up dma buffer pools per adapter

    :param mraid_mmadp_t \*adp:
        Adapter softstate

.. _`mraid_mm_setup_dma_pools.description`:

Description
-----------

We maintain a pool of dma buffers per each adapter. Each pool has one
buffer. E.g, we may have 5 dma pools - one each for 4k, 8k ... 64k buffers.
We have just one 4k buffer in 4k pool, one 8k buffer in 8k pool etc. We
dont' want to waste too much memory by allocating more buffers per each
pool.

.. _`mraid_mm_unregister_adp`:

mraid_mm_unregister_adp
=======================

.. c:function:: int mraid_mm_unregister_adp(uint32_t unique_id)

    Unregister routine for low level drivers

    :param uint32_t unique_id:
        UID of the adpater

.. _`mraid_mm_unregister_adp.description`:

Description
-----------

Assumes no outstanding ioctls to llds.

.. _`mraid_mm_free_adp_resources`:

mraid_mm_free_adp_resources
===========================

.. c:function:: void mraid_mm_free_adp_resources(mraid_mmadp_t *adp)

    Free adapter softstate

    :param mraid_mmadp_t \*adp:
        Adapter softstate

.. _`mraid_mm_teardown_dma_pools`:

mraid_mm_teardown_dma_pools
===========================

.. c:function:: void mraid_mm_teardown_dma_pools(mraid_mmadp_t *adp)

    Free all per adapter dma buffers

    :param mraid_mmadp_t \*adp:
        Adapter softstate

.. _`mraid_mm_init`:

mraid_mm_init
=============

.. c:function:: int mraid_mm_init( void)

    Module entry point

    :param  void:
        no arguments

.. _`mraid_mm_compat_ioctl`:

mraid_mm_compat_ioctl
=====================

.. c:function:: long mraid_mm_compat_ioctl(struct file *filep, unsigned int cmd, unsigned long arg)

    32bit to 64bit ioctl conversion routine

    :param struct file \*filep:
        file operations pointer (ignored)

    :param unsigned int cmd:
        ioctl command

    :param unsigned long arg:
        user ioctl packet

.. _`mraid_mm_exit`:

mraid_mm_exit
=============

.. c:function:: void __exit mraid_mm_exit( void)

    Module exit point

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

