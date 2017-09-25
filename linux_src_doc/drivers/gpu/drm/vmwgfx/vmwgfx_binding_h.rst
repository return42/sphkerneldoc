.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_binding.h

.. _`vmw_ctx_bindinfo`:

struct vmw_ctx_bindinfo
=======================

.. c:type:: struct vmw_ctx_bindinfo

    single binding metadata

.. _`vmw_ctx_bindinfo.definition`:

Definition
----------

.. code-block:: c

    struct vmw_ctx_bindinfo {
        struct list_head ctx_list;
        struct list_head res_list;
        struct vmw_resource *ctx;
        struct vmw_resource *res;
        enum vmw_ctx_binding_type bt;
        bool scrubbed;
    }

.. _`vmw_ctx_bindinfo.members`:

Members
-------

ctx_list
    List head for the context's list of bindings.

res_list
    List head for a resource's list of bindings.

ctx
    Non-refcounted pointer to the context that owns the binding. NULL
    indicates no binding present.

res
    Non-refcounted pointer to the resource the binding points to. This
    is typically a surface or a view.

bt
    Binding type.

scrubbed
    Whether the binding has been scrubbed from the context.

.. _`vmw_ctx_bindinfo_tex`:

struct vmw_ctx_bindinfo_tex
===========================

.. c:type:: struct vmw_ctx_bindinfo_tex

    texture stage binding metadata

.. _`vmw_ctx_bindinfo_tex.definition`:

Definition
----------

.. code-block:: c

    struct vmw_ctx_bindinfo_tex {
        struct vmw_ctx_bindinfo bi;
        uint32 texture_stage;
    }

.. _`vmw_ctx_bindinfo_tex.members`:

Members
-------

bi
    struct vmw_ctx_bindinfo we derive from.

texture_stage
    Device data used to reconstruct binding command.

.. _`vmw_ctx_bindinfo_shader`:

struct vmw_ctx_bindinfo_shader
==============================

.. c:type:: struct vmw_ctx_bindinfo_shader

    Shader binding metadata

.. _`vmw_ctx_bindinfo_shader.definition`:

Definition
----------

.. code-block:: c

    struct vmw_ctx_bindinfo_shader {
        struct vmw_ctx_bindinfo bi;
        SVGA3dShaderType shader_slot;
    }

.. _`vmw_ctx_bindinfo_shader.members`:

Members
-------

bi
    struct vmw_ctx_bindinfo we derive from.

shader_slot
    Device data used to reconstruct binding command.

.. _`vmw_ctx_bindinfo_cb`:

struct vmw_ctx_bindinfo_cb
==========================

.. c:type:: struct vmw_ctx_bindinfo_cb

    Constant buffer binding metadata

.. _`vmw_ctx_bindinfo_cb.definition`:

Definition
----------

.. code-block:: c

    struct vmw_ctx_bindinfo_cb {
        struct vmw_ctx_bindinfo bi;
        SVGA3dShaderType shader_slot;
        uint32 offset;
        uint32 size;
        uint32 slot;
    }

.. _`vmw_ctx_bindinfo_cb.members`:

Members
-------

bi
    struct vmw_ctx_bindinfo we derive from.

shader_slot
    Device data used to reconstruct binding command.

offset
    Device data used to reconstruct binding command.

size
    Device data used to reconstruct binding command.

slot
    Device data used to reconstruct binding command.

.. _`vmw_ctx_bindinfo_view`:

struct vmw_ctx_bindinfo_view
============================

.. c:type:: struct vmw_ctx_bindinfo_view

    View binding metadata

.. _`vmw_ctx_bindinfo_view.definition`:

Definition
----------

.. code-block:: c

    struct vmw_ctx_bindinfo_view {
        struct vmw_ctx_bindinfo bi;
        SVGA3dShaderType shader_slot;
        uint32 slot;
    }

.. _`vmw_ctx_bindinfo_view.members`:

Members
-------

bi
    struct vmw_ctx_bindinfo we derive from.

shader_slot
    Device data used to reconstruct binding command.

slot
    Device data used to reconstruct binding command.

.. _`vmw_ctx_bindinfo_so`:

struct vmw_ctx_bindinfo_so
==========================

.. c:type:: struct vmw_ctx_bindinfo_so

    StreamOutput binding metadata

.. _`vmw_ctx_bindinfo_so.definition`:

Definition
----------

.. code-block:: c

    struct vmw_ctx_bindinfo_so {
        struct vmw_ctx_bindinfo bi;
        uint32 offset;
        uint32 size;
        uint32 slot;
    }

.. _`vmw_ctx_bindinfo_so.members`:

Members
-------

bi
    struct vmw_ctx_bindinfo we derive from.

offset
    Device data used to reconstruct binding command.

size
    Device data used to reconstruct binding command.

slot
    Device data used to reconstruct binding command.

.. _`vmw_ctx_bindinfo_vb`:

struct vmw_ctx_bindinfo_vb
==========================

.. c:type:: struct vmw_ctx_bindinfo_vb

    Vertex buffer binding metadata

.. _`vmw_ctx_bindinfo_vb.definition`:

Definition
----------

.. code-block:: c

    struct vmw_ctx_bindinfo_vb {
        struct vmw_ctx_bindinfo bi;
        uint32 offset;
        uint32 stride;
        uint32 slot;
    }

.. _`vmw_ctx_bindinfo_vb.members`:

Members
-------

bi
    struct vmw_ctx_bindinfo we derive from.

offset
    Device data used to reconstruct binding command.

stride
    Device data used to reconstruct binding command.

slot
    Device data used to reconstruct binding command.

.. _`vmw_ctx_bindinfo_ib`:

struct vmw_ctx_bindinfo_ib
==========================

.. c:type:: struct vmw_ctx_bindinfo_ib

    StreamOutput binding metadata

.. _`vmw_ctx_bindinfo_ib.definition`:

Definition
----------

.. code-block:: c

    struct vmw_ctx_bindinfo_ib {
        struct vmw_ctx_bindinfo bi;
        uint32 offset;
        uint32 format;
    }

.. _`vmw_ctx_bindinfo_ib.members`:

Members
-------

bi
    struct vmw_ctx_bindinfo we derive from.

offset
    Device data used to reconstruct binding command.

format
    Device data used to reconstruct binding command.

.. _`vmw_dx_shader_bindings`:

struct vmw_dx_shader_bindings
=============================

.. c:type:: struct vmw_dx_shader_bindings

    per shader type context binding state

.. _`vmw_dx_shader_bindings.definition`:

Definition
----------

.. code-block:: c

    struct vmw_dx_shader_bindings {
        struct vmw_ctx_bindinfo_shader shader;
        struct vmw_ctx_bindinfo_cb const_buffers[SVGA3D_DX_MAX_CONSTBUFFERS];
        struct vmw_ctx_bindinfo_view shader_res[SVGA3D_DX_MAX_SRVIEWS];
        DECLARE_BITMAP(dirty_sr, SVGA3D_DX_MAX_SRVIEWS);
        unsigned long dirty;
    }

.. _`vmw_dx_shader_bindings.members`:

Members
-------

shader
    The shader binding for this shader type

const_buffers
    *undescribed*

shader_res
    Shader resource view bindings for this shader type.

dirty_sr
    Bitmap tracking individual shader resource bindings changes
    that have not yet been emitted to the device.

dirty
    Bitmap tracking per-binding type binding changes that have not
    yet been emitted to the device.

.. This file was automatic generated / don't edit.

