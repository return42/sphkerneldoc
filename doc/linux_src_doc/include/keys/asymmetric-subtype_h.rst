.. -*- coding: utf-8; mode: rst -*-

====================
asymmetric-subtype.h
====================


.. _`asymmetric_key_subtype`:

asymmetric_key_subtype
======================

.. c:function:: struct asymmetric_key_subtype *asymmetric_key_subtype (const struct key *key)

    Get the subtype from an asymmetric key

    :param const struct key \*key:
        The key of interest.



.. _`asymmetric_key_subtype.description`:

Description
-----------

Retrieves and returns the subtype pointer of the asymmetric key from the
type-specific data attached to the key.

