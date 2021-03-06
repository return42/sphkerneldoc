.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_context.c

.. _`vmw_context_cotables_unref`:

vmw_context_cotables_unref
==========================

.. c:function:: void vmw_context_cotables_unref(struct vmw_user_context *uctx)

    :param uctx:
        *undescribed*
    :type uctx: struct vmw_user_context \*

.. _`vmw_dx_context_scrub_cotables`:

vmw_dx_context_scrub_cotables
=============================

.. c:function:: void vmw_dx_context_scrub_cotables(struct vmw_resource *ctx, bool readback)

    Scrub all bindings and cotables from a context

    :param ctx:
        Pointer to the context resource
    :type ctx: struct vmw_resource \*

    :param readback:
        Whether to save the otable contents on scrubbing.
    :type readback: bool

.. _`vmw_dx_context_scrub_cotables.description`:

Description
-----------

COtables must be unbound before their context, but unbinding requires
the backup buffer being reserved, whereas scrubbing does not.
This function scrubs all cotables of a context, potentially reading back
the contents into their backup buffers. However, scrubbing cotables
also makes the device context invalid, so scrub all bindings first so
that doesn't have to be done later with an invalid context.

.. _`vmw_user_context_base_to_res`:

vmw_user_context_base_to_res
============================

.. c:function:: struct vmw_resource *vmw_user_context_base_to_res(struct ttm_base_object *base)

    space context management:

    :param base:
        *undescribed*
    :type base: struct ttm_base_object \*

.. _`vmw_user_context_base_release`:

vmw_user_context_base_release
=============================

.. c:function:: void vmw_user_context_base_release(struct ttm_base_object **p_base)

    base object. It releases the base-object's reference on the resource object.

    :param p_base:
        *undescribed*
    :type p_base: struct ttm_base_object \*\*

.. _`vmw_context_binding_list`:

vmw_context_binding_list
========================

.. c:function:: struct list_head *vmw_context_binding_list(struct vmw_resource *ctx)

    Return a list of context bindings

    :param ctx:
        The context resource
    :type ctx: struct vmw_resource \*

.. _`vmw_context_binding_list.description`:

Description
-----------

Returns the current list of bindings of the given context. Note that
this list becomes stale as soon as the dev_priv::binding_mutex is unlocked.

.. _`vmw_context_binding_state`:

vmw_context_binding_state
=========================

.. c:function:: struct vmw_ctx_binding_state *vmw_context_binding_state(struct vmw_resource *ctx)

    Return a pointer to a context binding state structure

    :param ctx:
        The context resource
    :type ctx: struct vmw_resource \*

.. _`vmw_context_binding_state.description`:

Description
-----------

Returns the current state of bindings of the given context. Note that
this state becomes stale as soon as the dev_priv::binding_mutex is unlocked.

.. _`vmw_context_bind_dx_query`:

vmw_context_bind_dx_query
=========================

.. c:function:: int vmw_context_bind_dx_query(struct vmw_resource *ctx_res, struct vmw_buffer_object *mob)

    Sets query MOB for the context.  If \ ``mob``\  is NULL, then this function will remove the association between the MOB and the context.  This function assumes the binding_mutex is held.

    :param ctx_res:
        The context resource
    :type ctx_res: struct vmw_resource \*

    :param mob:
        a reference to the query MOB
    :type mob: struct vmw_buffer_object \*

.. _`vmw_context_bind_dx_query.description`:

Description
-----------

Returns -EINVAL if a MOB has already been set and does not match the one
specified in the parameter.  0 otherwise.

.. _`vmw_context_get_dx_query_mob`:

vmw_context_get_dx_query_mob
============================

.. c:function:: struct vmw_buffer_object *vmw_context_get_dx_query_mob(struct vmw_resource *ctx_res)

    Returns non-counted reference to DX query mob

    :param ctx_res:
        The context resource
    :type ctx_res: struct vmw_resource \*

.. This file was automatic generated / don't edit.

