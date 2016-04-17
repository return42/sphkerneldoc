.. -*- coding: utf-8; mode: rst -*-

=================
x509_public_key.c
=================


.. _`x509_request_asymmetric_key`:

x509_request_asymmetric_key
===========================

.. c:function:: struct key *x509_request_asymmetric_key (struct key *keyring, const struct asymmetric_key_id *id, const struct asymmetric_key_id *skid, bool partial)

    Request a key by X.509 certificate params.

    :param struct key \*keyring:
        The keys to search.

    :param const struct asymmetric_key_id \*id:
        The issuer & serialNumber to look for or NULL.

    :param const struct asymmetric_key_id \*skid:
        The subjectKeyIdentifier to look for or NULL.

    :param bool partial:
        Use partial match if true, exact if false.



.. _`x509_request_asymmetric_key.description`:

Description
-----------

Find a key in the given keyring by identifier.  The preferred identifier is
the issuer + serialNumber and the fallback identifier is the
subjectKeyIdentifier.  If both are given, the lookup is by the former, but
the latter must also match.

