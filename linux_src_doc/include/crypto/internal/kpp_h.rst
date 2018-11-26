.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/internal/kpp.h

.. _`crypto_register_kpp`:

crypto_register_kpp
===================

.. c:function:: int crypto_register_kpp(struct kpp_alg *alg)

    - Register key-agreement protocol primitives algorithm

    :param alg:
        algorithm definition
    :type alg: struct kpp_alg \*

.. _`crypto_register_kpp.description`:

Description
-----------

Function registers an implementation of a key-agreement protocol primitive
algorithm

.. _`crypto_register_kpp.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_unregister_kpp`:

crypto_unregister_kpp
=====================

.. c:function:: void crypto_unregister_kpp(struct kpp_alg *alg)

    - Unregister key-agreement protocol primitive algorithm

    :param alg:
        algorithm definition
    :type alg: struct kpp_alg \*

.. _`crypto_unregister_kpp.description`:

Description
-----------

Function unregisters an implementation of a key-agreement protocol primitive
algorithm

.. This file was automatic generated / don't edit.

