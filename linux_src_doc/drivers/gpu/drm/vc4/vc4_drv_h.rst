.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_drv.h

.. _`vc4_texture_sample_info`:

struct vc4_texture_sample_info
==============================

.. c:type:: struct vc4_texture_sample_info

    saves the offsets into the UBO for texture setup parameters.

.. _`vc4_texture_sample_info.definition`:

Definition
----------

.. code-block:: c

    struct vc4_texture_sample_info {
        bool is_direct;
        uint32_t p_offset[4];
    }

.. _`vc4_texture_sample_info.members`:

Members
-------

is_direct
    *undescribed*

.. _`vc4_texture_sample_info.description`:

Description
-----------

This will be used at draw time to relocate the reference to the texture
contents in p0, and validate that the offset combined with
width/height/stride/etc. from p1 and p2/p3 doesn't sample outside the BO.
Note that the hardware treats unprovided config parameters as 0, so not all
of them need to be set up for every texure sample, and we'll store ~0 as
the offset to mark the unused ones.

See the VC4 3D architecture guide page 41 ("Texture and Memory Lookup Unit
Setup") for definitions of the texture parameters.

.. _`vc4_validated_shader_info`:

struct vc4_validated_shader_info
================================

.. c:type:: struct vc4_validated_shader_info

    information about validated shaders that needs to be used from command list validation.

.. _`vc4_validated_shader_info.definition`:

Definition
----------

.. code-block:: c

    struct vc4_validated_shader_info {
        uint32_t uniforms_size;
        uint32_t uniforms_src_size;
        uint32_t num_texture_samples;
        struct vc4_texture_sample_info *texture_samples;
        uint32_t num_uniform_addr_offsets;
        uint32_t *uniform_addr_offsets;
        bool is_threaded;
    }

.. _`vc4_validated_shader_info.members`:

Members
-------

uniforms_size
    *undescribed*

uniforms_src_size
    *undescribed*

num_texture_samples
    *undescribed*

texture_samples
    *undescribed*

num_uniform_addr_offsets
    *undescribed*

uniform_addr_offsets
    *undescribed*

is_threaded
    *undescribed*

.. _`vc4_validated_shader_info.description`:

Description
-----------

For a given shader, each time a shader state record references it, we need
to verify that the shader doesn't read more uniforms than the shader state
record's uniform BO pointer can provide, and we need to apply relocations
and validate the shader state record's uniforms that define the texture
samples.

.. _`_wait_for`:

_wait_for
=========

.. c:function::  _wait_for( COND,  MS,  W)

    magic (register) wait macro

    :param  COND:
        *undescribed*

    :param  MS:
        *undescribed*

    :param  W:
        *undescribed*

.. _`_wait_for.description`:

Description
-----------

Does the right thing for modeset paths when run under kdgb or similar atomic
contexts. Note that it's important that we check the condition again after
having timed out, since the timeout could be due to preemption or similar and
we've never had a chance to check the condition before the timeout.

.. This file was automatic generated / don't edit.

