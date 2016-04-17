.. -*- coding: utf-8; mode: rst -*-

===========
vmwgfx_so.h
===========


.. _`vmw_view_destroy`:

union vmw_view_destroy
======================

.. c:type:: vmw_view_destroy

    view destruction command body


.. _`vmw_view_destroy.definition`:

Definition
----------

.. code-block:: c

  union vmw_view_destroy {
    struct SVGA3dCmdDXDestroyRenderTargetView rtv;
    struct SVGA3dCmdDXDestroyShaderResourceView srv;
    struct SVGA3dCmdDXDestroyDepthStencilView dsv;
    u32 view_id;
  };


.. _`vmw_view_destroy.members`:

Members
-------

:``rtv``:
    RenderTarget view destruction command body

:``srv``:
    ShaderResource view destruction command body

:``dsv``:
    DepthStencil view destruction command body

:``view_id``:
    A single u32 view id.




.. _`vmw_view_destroy.description`:

Description
-----------

The assumption here is that all union members are really represented by a
single u32 in the command stream. If that's not the case,
the size of this union will not equal the size of an u32, and the
assumption is invalid, and we detect that at compile time in the
:c:func:`vmw_so_build_asserts` function.

