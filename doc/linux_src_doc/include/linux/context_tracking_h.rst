.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/context_tracking.h

.. _`ct_state`:

ct_state
========

.. c:function:: enum ctx_state ct_state( void)

    return the current context tracking state if known

    :param  void:
        no arguments

.. _`ct_state.description`:

Description
-----------

Returns the current cpu's context tracking state if context tracking
is enabled.  If context tracking is disabled, returns
CONTEXT_DISABLED.  This should be used primarily for debugging.

.. This file was automatic generated / don't edit.

