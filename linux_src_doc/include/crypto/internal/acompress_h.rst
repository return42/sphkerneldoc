.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/internal/acompress.h

.. _`crypto_register_acomp`:

crypto_register_acomp
=====================

.. c:function:: int crypto_register_acomp(struct acomp_alg *alg)

    - Register asynchronous compression algorithm

    :param alg:
        algorithm definition
    :type alg: struct acomp_alg \*

.. _`crypto_register_acomp.description`:

Description
-----------

Function registers an implementation of an asynchronous
compression algorithm

.. _`crypto_register_acomp.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_unregister_acomp`:

crypto_unregister_acomp
=======================

.. c:function:: int crypto_unregister_acomp(struct acomp_alg *alg)

    - Unregister asynchronous compression algorithm

    :param alg:
        algorithm definition
    :type alg: struct acomp_alg \*

.. _`crypto_unregister_acomp.description`:

Description
-----------

Function unregisters an implementation of an asynchronous
compression algorithm

.. _`crypto_unregister_acomp.return`:

Return
------

zero on success; error code in case of error

.. This file was automatic generated / don't edit.

