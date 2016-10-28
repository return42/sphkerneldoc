.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/crypto/internal/akcipher.h

.. _`crypto_register_akcipher`:

crypto_register_akcipher
========================

.. c:function:: int crypto_register_akcipher(struct akcipher_alg *alg)

    - Register public key algorithm

    :param struct akcipher_alg \*alg:
        algorithm definition

.. _`crypto_register_akcipher.description`:

Description
-----------

Function registers an implementation of a public key verify algorithm

.. _`crypto_register_akcipher.return`:

Return
------

zero on success; error code in case of error

.. _`crypto_unregister_akcipher`:

crypto_unregister_akcipher
==========================

.. c:function:: void crypto_unregister_akcipher(struct akcipher_alg *alg)

    - Unregister public key algorithm

    :param struct akcipher_alg \*alg:
        algorithm definition

.. _`crypto_unregister_akcipher.description`:

Description
-----------

Function unregisters an implementation of a public key verify algorithm

.. _`akcipher_register_instance`:

akcipher_register_instance
==========================

.. c:function:: int akcipher_register_instance(struct crypto_template *tmpl, struct akcipher_instance *inst)

    - Unregister public key template instance

    :param struct crypto_template \*tmpl:
        the template from which the algorithm was created

    :param struct akcipher_instance \*inst:
        the template instance

.. _`akcipher_register_instance.description`:

Description
-----------

Function registers an implementation of an asymmetric key algorithm
created from a template

.. This file was automatic generated / don't edit.

