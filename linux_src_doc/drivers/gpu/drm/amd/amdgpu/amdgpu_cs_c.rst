.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_cs.c

.. _`amdgpu_cs_parser_fini`:

amdgpu_cs_parser_fini
=====================

.. c:function:: void amdgpu_cs_parser_fini(struct amdgpu_cs_parser *parser, int error, bool backoff)

    clean parser states

    :param struct amdgpu_cs_parser \*parser:
        parser structure holding parsing context.

    :param int error:
        error number

    :param bool backoff:
        *undescribed*

.. _`amdgpu_cs_parser_fini.description`:

Description
-----------

If error is set than unvalidate buffer, otherwise just free memory
used by parsing context.

.. _`amdgpu_cs_wait_ioctl`:

amdgpu_cs_wait_ioctl
====================

.. c:function:: int amdgpu_cs_wait_ioctl(struct drm_device *dev, void *data, struct drm_file *filp)

    wait for a command submission to finish

    :param struct drm_device \*dev:
        drm device

    :param void \*data:
        data from userspace

    :param struct drm_file \*filp:
        file private

.. _`amdgpu_cs_wait_ioctl.description`:

Description
-----------

Wait for the command submission identified by handle to finish.

.. _`amdgpu_cs_find_mapping`:

amdgpu_cs_find_mapping
======================

.. c:function:: struct amdgpu_bo_va_mapping *amdgpu_cs_find_mapping(struct amdgpu_cs_parser *parser, uint64_t addr, struct amdgpu_bo **bo)

    find bo_va for VM address

    :param struct amdgpu_cs_parser \*parser:
        command submission parser context

    :param uint64_t addr:
        VM address

    :param struct amdgpu_bo \*\*bo:
        resulting BO of the mapping found

.. _`amdgpu_cs_find_mapping.description`:

Description
-----------

Search the buffer objects in the command submission context for a certain
virtual memory address. Returns allocation structure when found, NULL
otherwise.

.. _`amdgpu_cs_sysvm_access_required`:

amdgpu_cs_sysvm_access_required
===============================

.. c:function:: int amdgpu_cs_sysvm_access_required(struct amdgpu_cs_parser *parser)

    make BOs accessible by the system VM

    :param struct amdgpu_cs_parser \*parser:
        command submission parser context

.. _`amdgpu_cs_sysvm_access_required.description`:

Description
-----------

Helper for UVD/VCE VM emulation, make sure BOs are accessible by the system VM.

.. This file was automatic generated / don't edit.

