.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/keys/asymmetric-subtype.h

.. _`asymmetric_key_subtype`:

asymmetric_key_subtype
======================

.. c:function:: struct asymmetric_key_subtype *asymmetric_key_subtype(const struct key *key)

    Get the subtype from an asymmetric key

    :param key:
        The key of interest.
    :type key: const struct key \*

.. _`asymmetric_key_subtype.description`:

Description
-----------

Retrieves and returns the subtype pointer of the asymmetric key from the
type-specific data attached to the key.

.. This file was automatic generated / don't edit.

