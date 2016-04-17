.. -*- coding: utf-8; mode: rst -*-

=============
vmwgfx_fifo.c
=============


.. _`vmw_local_fifo_reserve`:

vmw_local_fifo_reserve
======================

.. c:function:: void *vmw_local_fifo_reserve (struct vmw_private *dev_priv, uint32_t bytes)

    :param struct vmw_private \*dev_priv:

        *undescribed*

    :param uint32_t bytes:

        *undescribed*



.. _`vmw_local_fifo_reserve.description`:

Description
-----------


This function will return NULL (error) on two conditions::

 If it timeouts waiting for fifo space, or if ``bytes`` is larger than the
  available fifo space.



.. _`vmw_local_fifo_reserve.returns`:

Returns
-------

Pointer to the fifo, or null on error (possible hardware hang).



.. _`vmw_fifo_commit_flush`:

vmw_fifo_commit_flush
=====================

.. c:function:: void vmw_fifo_commit_flush (struct vmw_private *dev_priv, uint32_t bytes)

    Commit fifo space and flush any buffered commands.

    :param struct vmw_private \*dev_priv:
        Pointer to device private structure.

    :param uint32_t bytes:
        Number of bytes to commit.



.. _`vmw_fifo_flush`:

vmw_fifo_flush
==============

.. c:function:: int vmw_fifo_flush (struct vmw_private *dev_priv, bool interruptible)

    Flush any buffered commands and make sure command processing starts.

    :param struct vmw_private \*dev_priv:
        Pointer to device private structure.

    :param bool interruptible:
        Whether to wait interruptible if function needs to sleep.



.. _`vmw_fifo_emit_dummy_legacy_query`:

vmw_fifo_emit_dummy_legacy_query
================================

.. c:function:: int vmw_fifo_emit_dummy_legacy_query (struct vmw_private *dev_priv, uint32_t cid)

    emits a dummy query to the fifo using legacy query commands.

    :param struct vmw_private \*dev_priv:
        The device private structure.

    :param uint32_t cid:
        The hardware context id used for the query.



.. _`vmw_fifo_emit_dummy_legacy_query.description`:

Description
-----------

See the vmw_fifo_emit_dummy_query documentation.



.. _`vmw_fifo_emit_dummy_gb_query`:

vmw_fifo_emit_dummy_gb_query
============================

.. c:function:: int vmw_fifo_emit_dummy_gb_query (struct vmw_private *dev_priv, uint32_t cid)

    emits a dummy query to the fifo using guest-backed resource query commands.

    :param struct vmw_private \*dev_priv:
        The device private structure.

    :param uint32_t cid:
        The hardware context id used for the query.



.. _`vmw_fifo_emit_dummy_gb_query.description`:

Description
-----------

See the vmw_fifo_emit_dummy_query documentation.



.. _`vmw_fifo_emit_dummy_query`:

vmw_fifo_emit_dummy_query
=========================

.. c:function:: int vmw_fifo_emit_dummy_query (struct vmw_private *dev_priv, uint32_t cid)

    emits a dummy query to the fifo using appropriate resource query commands.

    :param struct vmw_private \*dev_priv:
        The device private structure.

    :param uint32_t cid:
        The hardware context id used for the query.



.. _`vmw_fifo_emit_dummy_query.description`:

Description
-----------

This function is used to emit a dummy occlusion query with
no primitives rendered between query begin and query end.
It's used to provide a query barrier, in order to know that when
this query is finished, all preceding queries are also finished.

A Query results structure should have been initialized at the start
of the dev_priv->dummy_query_bo buffer object. And that buffer object
must also be either reserved or pinned when this function is called.

Returns -ENOMEM on failure to reserve fifo space.

