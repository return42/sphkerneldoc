.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rxrpc/key.c

.. _`rxrpc_get_null_key`:

rxrpc_get_null_key
==================

.. c:function:: struct key *rxrpc_get_null_key(const char *keyname)

    Generate a null RxRPC key

    :param keyname:
        The name to give the key.
    :type keyname: const char \*

.. _`rxrpc_get_null_key.description`:

Description
-----------

Generate a null RxRPC key that can be used to indicate anonymous security is
required for a particular domain.

.. This file was automatic generated / don't edit.

