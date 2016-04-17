.. -*- coding: utf-8; mode: rst -*-

====
vi.c
====


.. _`vi_get_xclk`:

vi_get_xclk
===========

.. c:function:: u32 vi_get_xclk (struct amdgpu_device *adev)

    get the xclk

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`vi_get_xclk.description`:

Description
-----------

Returns the reference clock used by the gfx engine
(VI).



.. _`vi_srbm_select`:

vi_srbm_select
==============

.. c:function:: void vi_srbm_select (struct amdgpu_device *adev, u32 me, u32 pipe, u32 queue, u32 vmid)

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



.. _`vi_srbm_select.description`:

Description
-----------

Switches the currently active registers instances.  Some
registers are instanced per VMID, others are instanced per
me/pipe/queue combination.



.. _`vi_asic_reset`:

vi_asic_reset
=============

.. c:function:: int vi_asic_reset (struct amdgpu_device *adev)

    soft reset GPU

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`vi_asic_reset.description`:

Description
-----------

Look up which blocks are hung and attempt
to reset them.
Returns 0 for success.

