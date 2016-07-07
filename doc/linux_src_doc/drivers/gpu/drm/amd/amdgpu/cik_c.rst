.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/cik.c

.. _`cik_get_xclk`:

cik_get_xclk
============

.. c:function:: u32 cik_get_xclk(struct amdgpu_device *adev)

    get the xclk

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_get_xclk.description`:

Description
-----------

Returns the reference clock used by the gfx engine
(CIK).

.. _`cik_srbm_select`:

cik_srbm_select
===============

.. c:function:: void cik_srbm_select(struct amdgpu_device *adev, u32 me, u32 pipe, u32 queue, u32 vmid)

    select specific register instances

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param u32 me:
        selected ME (micro engine)

    :param u32 pipe:
        pipe

    :param u32 queue:
        queue

    :param u32 vmid:
        VMID

.. _`cik_srbm_select.description`:

Description
-----------

Switches the currently active registers instances.  Some
registers are instanced per VMID, others are instanced per
me/pipe/queue combination.

.. _`cik_asic_reset`:

cik_asic_reset
==============

.. c:function:: int cik_asic_reset(struct amdgpu_device *adev)

    soft reset GPU

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

.. _`cik_asic_reset.description`:

Description
-----------

Look up which blocks are hung and attempt
to reset them.
Returns 0 for success.

.. This file was automatic generated / don't edit.

