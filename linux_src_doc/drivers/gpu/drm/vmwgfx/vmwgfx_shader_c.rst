.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_shader.c

.. _`vmw_res_to_shader`:

vmw_res_to_shader
=================

.. c:function:: struct vmw_shader *vmw_res_to_shader(struct vmw_resource *res)

    :param res:
        *undescribed*
    :type res: struct vmw_resource \*

.. _`vmw_res_to_dx_shader`:

vmw_res_to_dx_shader
====================

.. c:function:: struct vmw_dx_shader *vmw_res_to_dx_shader(struct vmw_resource *res)

    typecast a struct vmw_resource to a struct vmw_dx_shader

    :param res:
        Pointer to the struct vmw_resource.
    :type res: struct vmw_resource \*

.. _`vmw_dx_shader_commit_notify`:

vmw_dx_shader_commit_notify
===========================

.. c:function:: void vmw_dx_shader_commit_notify(struct vmw_resource *res, enum vmw_cmdbuf_res_state state)

    Notify that a shader operation has been committed to hardware from a user-supplied command stream.

    :param res:
        Pointer to the shader resource.
    :type res: struct vmw_resource \*

    :param state:
        Indicating whether a creation or removal has been committed.
    :type state: enum vmw_cmdbuf_res_state

.. _`vmw_dx_shader_unscrub`:

vmw_dx_shader_unscrub
=====================

.. c:function:: int vmw_dx_shader_unscrub(struct vmw_resource *res)

    Have the device reattach a MOB to a DX shader.

    :param res:
        The shader resource
    :type res: struct vmw_resource \*

.. _`vmw_dx_shader_unscrub.description`:

Description
-----------

This function reverts a scrub operation.

.. _`vmw_dx_shader_create`:

vmw_dx_shader_create
====================

.. c:function:: int vmw_dx_shader_create(struct vmw_resource *res)

    The DX shader create callback

    :param res:
        The DX shader resource
    :type res: struct vmw_resource \*

.. _`vmw_dx_shader_create.description`:

Description
-----------

The create callback is called as part of resource validation and
makes sure that we unscrub the shader if it's previously been scrubbed.

.. _`vmw_dx_shader_bind`:

vmw_dx_shader_bind
==================

.. c:function:: int vmw_dx_shader_bind(struct vmw_resource *res, struct ttm_validate_buffer *val_buf)

    The DX shader bind callback

    :param res:
        The DX shader resource
    :type res: struct vmw_resource \*

    :param val_buf:
        Pointer to the validate buffer.
    :type val_buf: struct ttm_validate_buffer \*

.. _`vmw_dx_shader_scrub`:

vmw_dx_shader_scrub
===================

.. c:function:: int vmw_dx_shader_scrub(struct vmw_resource *res)

    Have the device unbind a MOB from a DX shader.

    :param res:
        The shader resource
    :type res: struct vmw_resource \*

.. _`vmw_dx_shader_scrub.description`:

Description
-----------

This function unbinds a MOB from the DX shader without requiring the
MOB dma_buffer to be reserved. The driver still considers the MOB bound.
However, once the driver eventually decides to unbind the MOB, it doesn't
need to access the context.

.. _`vmw_dx_shader_unbind`:

vmw_dx_shader_unbind
====================

.. c:function:: int vmw_dx_shader_unbind(struct vmw_resource *res, bool readback, struct ttm_validate_buffer *val_buf)

    The dx shader unbind callback.

    :param res:
        The shader resource
    :type res: struct vmw_resource \*

    :param readback:
        Whether this is a readback unbind. Currently unused.
    :type readback: bool

    :param val_buf:
        MOB buffer information.
    :type val_buf: struct ttm_validate_buffer \*

.. _`vmw_dx_shader_cotable_list_scrub`:

vmw_dx_shader_cotable_list_scrub
================================

.. c:function:: void vmw_dx_shader_cotable_list_scrub(struct vmw_private *dev_priv, struct list_head *list, bool readback)

    The cotable unbind_func callback for DX shaders.

    :param dev_priv:
        Pointer to device private structure.
    :type dev_priv: struct vmw_private \*

    :param list:
        The list of cotable resources.
    :type list: struct list_head \*

    :param readback:
        Whether the call was part of a readback unbind.
    :type readback: bool

.. _`vmw_dx_shader_cotable_list_scrub.description`:

Description
-----------

Scrubs all shader MOBs so that any subsequent shader unbind or shader
destroy operation won't need to swap in the context.

.. _`vmw_dx_shader_res_free`:

vmw_dx_shader_res_free
======================

.. c:function:: void vmw_dx_shader_res_free(struct vmw_resource *res)

    The DX shader free callback

    :param res:
        The shader resource
    :type res: struct vmw_resource \*

.. _`vmw_dx_shader_res_free.description`:

Description
-----------

Frees the DX shader resource and updates memory accounting.

.. _`vmw_dx_shader_add`:

vmw_dx_shader_add
=================

.. c:function:: int vmw_dx_shader_add(struct vmw_cmdbuf_res_manager *man, struct vmw_resource *ctx, u32 user_key, SVGA3dShaderType shader_type, struct list_head *list)

    Add a shader resource as a command buffer managed resource.

    :param man:
        The command buffer resource manager.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param ctx:
        Pointer to the context resource.
    :type ctx: struct vmw_resource \*

    :param user_key:
        The id used for this shader.
    :type user_key: u32

    :param shader_type:
        The shader type.
    :type shader_type: SVGA3dShaderType

    :param list:
        The list of staged command buffer managed resources.
    :type list: struct list_head \*

.. _`vmw_user_shader_base_to_res`:

vmw_user_shader_base_to_res
===========================

.. c:function:: struct vmw_resource *vmw_user_shader_base_to_res(struct ttm_base_object *base)

    space shader management:

    :param base:
        *undescribed*
    :type base: struct ttm_base_object \*

.. _`vmw_user_shader_base_release`:

vmw_user_shader_base_release
============================

.. c:function:: void vmw_user_shader_base_release(struct ttm_base_object **p_base)

    base object. It releases the base-object's reference on the resource object.

    :param p_base:
        *undescribed*
    :type p_base: struct ttm_base_object \*\*

.. _`vmw_shader_id_ok`:

vmw_shader_id_ok
================

.. c:function:: bool vmw_shader_id_ok(u32 user_key, SVGA3dShaderType shader_type)

    Check whether a compat shader user key and shader type are within valid bounds.

    :param user_key:
        User space id of the shader.
    :type user_key: u32

    :param shader_type:
        Shader type.
    :type shader_type: SVGA3dShaderType

.. _`vmw_shader_id_ok.description`:

Description
-----------

Returns true if valid false if not.

.. _`vmw_shader_key`:

vmw_shader_key
==============

.. c:function:: u32 vmw_shader_key(u32 user_key, SVGA3dShaderType shader_type)

    Compute a hash key suitable for a compat shader.

    :param user_key:
        User space id of the shader.
    :type user_key: u32

    :param shader_type:
        Shader type.
    :type shader_type: SVGA3dShaderType

.. _`vmw_shader_key.description`:

Description
-----------

Returns a hash key suitable for a command buffer managed resource
manager hash table.

.. _`vmw_shader_remove`:

vmw_shader_remove
=================

.. c:function:: int vmw_shader_remove(struct vmw_cmdbuf_res_manager *man, u32 user_key, SVGA3dShaderType shader_type, struct list_head *list)

    Stage a compat shader for removal.

    :param man:
        Pointer to the compat shader manager identifying the shader namespace.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param user_key:
        The key that is used to identify the shader. The key is
        unique to the shader type.
    :type user_key: u32

    :param shader_type:
        Shader type.
    :type shader_type: SVGA3dShaderType

    :param list:
        Caller's list of staged command buffer resource actions.
    :type list: struct list_head \*

.. _`vmw_compat_shader_add`:

vmw_compat_shader_add
=====================

.. c:function:: int vmw_compat_shader_add(struct vmw_private *dev_priv, struct vmw_cmdbuf_res_manager *man, u32 user_key, const void *bytecode, SVGA3dShaderType shader_type, size_t size, struct list_head *list)

    Create a compat shader and stage it for addition as a command buffer managed resource.

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param man:
        Pointer to the compat shader manager identifying the shader namespace.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param user_key:
        The key that is used to identify the shader. The key is
        unique to the shader type.
    :type user_key: u32

    :param bytecode:
        Pointer to the bytecode of the shader.
    :type bytecode: const void \*

    :param shader_type:
        Shader type.
    :type shader_type: SVGA3dShaderType

    :param size:
        *undescribed*
    :type size: size_t

    :param list:
        Caller's list of staged command buffer resource actions.
    :type list: struct list_head \*

.. _`vmw_shader_lookup`:

vmw_shader_lookup
=================

.. c:function:: struct vmw_resource *vmw_shader_lookup(struct vmw_cmdbuf_res_manager *man, u32 user_key, SVGA3dShaderType shader_type)

    Look up a compat shader

    :param man:
        Pointer to the command buffer managed resource manager identifying
        the shader namespace.
    :type man: struct vmw_cmdbuf_res_manager \*

    :param user_key:
        The user space id of the shader.
    :type user_key: u32

    :param shader_type:
        The shader type.
    :type shader_type: SVGA3dShaderType

.. _`vmw_shader_lookup.description`:

Description
-----------

Returns a refcounted pointer to a struct vmw_resource if the shader was
found. An error pointer otherwise.

.. This file was automatic generated / don't edit.

