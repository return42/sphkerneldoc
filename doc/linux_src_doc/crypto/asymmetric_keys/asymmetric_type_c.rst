.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/asymmetric_keys/asymmetric_type.c

.. _`find_asymmetric_key`:

find_asymmetric_key
===================

.. c:function:: struct key *find_asymmetric_key(struct key *keyring, const struct asymmetric_key_id *id_0, const struct asymmetric_key_id *id_1, bool partial)

    Find a key by ID.

    :param struct key \*keyring:
        The keys to search.

    :param const struct asymmetric_key_id \*id_0:
        The first ID to look for or NULL.

    :param const struct asymmetric_key_id \*id_1:
        The second ID to look for or NULL.

    :param bool partial:
        Use partial match if true, exact if false.

.. _`find_asymmetric_key.description`:

Description
-----------

Find a key in the given keyring by identifier.  The preferred identifier is
the id_0 and the fallback identifier is the id_1.  If both are given, the
lookup is by the former, but the latter must also match.

.. _`asymmetric_key_generate_id`:

asymmetric_key_generate_id
==========================

.. c:function:: struct asymmetric_key_id *asymmetric_key_generate_id(const void *val_1, size_t len_1, const void *val_2, size_t len_2)

    Construct an asymmetric key ID

    :param const void \*val_1:
        First binary blob

    :param size_t len_1:
        Length of first binary blob

    :param const void \*val_2:
        Second binary blob

    :param size_t len_2:
        Length of second binary blob

.. _`asymmetric_key_generate_id.description`:

Description
-----------

Construct an asymmetric key ID from a pair of binary blobs.

.. _`asymmetric_key_id_same`:

asymmetric_key_id_same
======================

.. c:function:: bool asymmetric_key_id_same(const struct asymmetric_key_id *kid1, const struct asymmetric_key_id *kid2)

    Return true if two asymmetric keys IDs are the same.

    :param const struct asymmetric_key_id \*kid1:
        *undescribed*

    :param const struct asymmetric_key_id \*kid2:
        *undescribed*

.. _`asymmetric_key_id_partial`:

asymmetric_key_id_partial
=========================

.. c:function:: bool asymmetric_key_id_partial(const struct asymmetric_key_id *kid1, const struct asymmetric_key_id *kid2)

    Return true if two asymmetric keys IDs partially match

    :param const struct asymmetric_key_id \*kid1:
        *undescribed*

    :param const struct asymmetric_key_id \*kid2:
        *undescribed*

.. _`asymmetric_match_key_ids`:

asymmetric_match_key_ids
========================

.. c:function:: bool asymmetric_match_key_ids(const struct asymmetric_key_ids *kids, const struct asymmetric_key_id *match_id, bool (*) match (const struct asymmetric_key_id *kid1, const struct asymmetric_key_id *kid2)

    Search asymmetric key IDs

    :param const struct asymmetric_key_ids \*kids:
        The list of key IDs to check

    :param const struct asymmetric_key_id \*match_id:
        The key ID we're looking for

    :param (bool (\*) match (const struct asymmetric_key_id \*kid1, const struct asymmetric_key_id \*kid2):
        The match function to use

.. _`asymmetric_key_hex_to_key_id`:

asymmetric_key_hex_to_key_id
============================

.. c:function:: struct asymmetric_key_id *asymmetric_key_hex_to_key_id(const char *id)

    Convert a hex string into a key ID.

    :param const char \*id:
        The ID as a hex string.

.. _`register_asymmetric_key_parser`:

register_asymmetric_key_parser
==============================

.. c:function:: int register_asymmetric_key_parser(struct asymmetric_key_parser *parser)

    Register a asymmetric key blob parser

    :param struct asymmetric_key_parser \*parser:
        The parser to register

.. _`unregister_asymmetric_key_parser`:

unregister_asymmetric_key_parser
================================

.. c:function:: void unregister_asymmetric_key_parser(struct asymmetric_key_parser *parser)

    Unregister a asymmetric key blob parser

    :param struct asymmetric_key_parser \*parser:
        The parser to unregister

.. This file was automatic generated / don't edit.

