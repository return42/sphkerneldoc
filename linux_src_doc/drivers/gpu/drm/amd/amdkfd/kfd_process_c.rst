.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdkfd/kfd_process.c

.. _`kfd_process_device_init_vm`:

kfd_process_device_init_vm
==========================

.. c:function:: int kfd_process_device_init_vm(struct kfd_process_device *pdd, struct file *drm_file)

    Initialize a VM for a process-device

    :param struct kfd_process_device \*pdd:
        The process-device

    :param struct file \*drm_file:
        Optional pointer to a DRM file descriptor

.. _`kfd_process_device_init_vm.description`:

Description
-----------

If \ ``drm_file``\  is specified, it will be used to acquire the VM from
that file descriptor. If successful, the \ ``pdd``\  takes ownership of
the file descriptor.

If \ ``drm_file``\  is NULL, a new VM is created.

Returns 0 on success, -errno on failure.

.. This file was automatic generated / don't edit.

