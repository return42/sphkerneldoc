.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_uvd.c

.. _`amdgpu_uvd_entity_init`:

amdgpu_uvd_entity_init
======================

.. c:function:: int amdgpu_uvd_entity_init(struct amdgpu_device *adev)

    init entity

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_uvd_cs_pass1`:

amdgpu_uvd_cs_pass1
===================

.. c:function:: int amdgpu_uvd_cs_pass1(struct amdgpu_uvd_cs_ctx *ctx)

    first parsing round

    :param ctx:
        UVD parser context
    :type ctx: struct amdgpu_uvd_cs_ctx \*

.. _`amdgpu_uvd_cs_pass1.description`:

Description
-----------

Make sure UVD message and feedback buffers are in VRAM and
nobody is violating an 256MB boundary.

.. _`amdgpu_uvd_cs_msg_decode`:

amdgpu_uvd_cs_msg_decode
========================

.. c:function:: int amdgpu_uvd_cs_msg_decode(struct amdgpu_device *adev, uint32_t *msg, unsigned buf_sizes)

    handle UVD decode message

    :param adev:
        *undescribed*
    :type adev: struct amdgpu_device \*

    :param msg:
        pointer to message structure
    :type msg: uint32_t \*

    :param buf_sizes:
        returned buffer sizes
    :type buf_sizes: unsigned

.. _`amdgpu_uvd_cs_msg_decode.description`:

Description
-----------

Peek into the decode message and calculate the necessary buffer sizes.

.. _`amdgpu_uvd_cs_msg`:

amdgpu_uvd_cs_msg
=================

.. c:function:: int amdgpu_uvd_cs_msg(struct amdgpu_uvd_cs_ctx *ctx, struct amdgpu_bo *bo, unsigned offset)

    handle UVD message

    :param ctx:
        UVD parser context
    :type ctx: struct amdgpu_uvd_cs_ctx \*

    :param bo:
        buffer object containing the message
    :type bo: struct amdgpu_bo \*

    :param offset:
        offset into the buffer object
    :type offset: unsigned

.. _`amdgpu_uvd_cs_msg.description`:

Description
-----------

Peek into the UVD message and extract the session id.
Make sure that we don't open up to many sessions.

.. _`amdgpu_uvd_cs_pass2`:

amdgpu_uvd_cs_pass2
===================

.. c:function:: int amdgpu_uvd_cs_pass2(struct amdgpu_uvd_cs_ctx *ctx)

    second parsing round

    :param ctx:
        UVD parser context
    :type ctx: struct amdgpu_uvd_cs_ctx \*

.. _`amdgpu_uvd_cs_pass2.description`:

Description
-----------

Patch buffer addresses, make sure buffer sizes are correct.

.. _`amdgpu_uvd_cs_reg`:

amdgpu_uvd_cs_reg
=================

.. c:function:: int amdgpu_uvd_cs_reg(struct amdgpu_uvd_cs_ctx *ctx, int (*cb)(struct amdgpu_uvd_cs_ctx *ctx))

    parse register writes

    :param ctx:
        UVD parser context
    :type ctx: struct amdgpu_uvd_cs_ctx \*

    :param int (\*cb)(struct amdgpu_uvd_cs_ctx \*ctx):
        callback function

.. _`amdgpu_uvd_cs_reg.description`:

Description
-----------

Parse the register writes, call cb on each complete command.

.. _`amdgpu_uvd_cs_packets`:

amdgpu_uvd_cs_packets
=====================

.. c:function:: int amdgpu_uvd_cs_packets(struct amdgpu_uvd_cs_ctx *ctx, int (*cb)(struct amdgpu_uvd_cs_ctx *ctx))

    parse UVD packets

    :param ctx:
        UVD parser context
    :type ctx: struct amdgpu_uvd_cs_ctx \*

    :param int (\*cb)(struct amdgpu_uvd_cs_ctx \*ctx):
        callback function

.. _`amdgpu_uvd_cs_packets.description`:

Description
-----------

Parse the command stream packets.

.. _`amdgpu_uvd_ring_parse_cs`:

amdgpu_uvd_ring_parse_cs
========================

.. c:function:: int amdgpu_uvd_ring_parse_cs(struct amdgpu_cs_parser *parser, uint32_t ib_idx)

    UVD command submission parser

    :param parser:
        Command submission parser context
    :type parser: struct amdgpu_cs_parser \*

    :param ib_idx:
        *undescribed*
    :type ib_idx: uint32_t

.. _`amdgpu_uvd_ring_parse_cs.description`:

Description
-----------

Parse the command stream, patch in addresses as necessary.

.. _`amdgpu_uvd_ring_test_ib`:

amdgpu_uvd_ring_test_ib
=======================

.. c:function:: int amdgpu_uvd_ring_test_ib(struct amdgpu_ring *ring, long timeout)

    test ib execution

    :param ring:
        amdgpu_ring pointer
    :type ring: struct amdgpu_ring \*

    :param timeout:
        *undescribed*
    :type timeout: long

.. _`amdgpu_uvd_ring_test_ib.description`:

Description
-----------

Test if we can successfully execute an IB

.. _`amdgpu_uvd_used_handles`:

amdgpu_uvd_used_handles
=======================

.. c:function:: uint32_t amdgpu_uvd_used_handles(struct amdgpu_device *adev)

    returns used UVD handles

    :param adev:
        amdgpu_device pointer
    :type adev: struct amdgpu_device \*

.. _`amdgpu_uvd_used_handles.description`:

Description
-----------

Returns the number of UVD handles in use

.. This file was automatic generated / don't edit.

