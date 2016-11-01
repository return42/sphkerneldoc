.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/crypto_engine.c

.. _`crypto_pump_requests`:

crypto_pump_requests
====================

.. c:function:: void crypto_pump_requests(struct crypto_engine *engine, bool in_kthread)

    dequeue one request from engine queue to process

    :param struct crypto_engine \*engine:
        the hardware engine

    :param bool in_kthread:
        true if we are in the context of the request pump thread

.. _`crypto_pump_requests.description`:

Description
-----------

This function checks if there is any request in the engine queue that
needs processing and if so call out to the driver to initialize hardware
and handle each request.

.. _`crypto_transfer_cipher_request`:

crypto_transfer_cipher_request
==============================

.. c:function:: int crypto_transfer_cipher_request(struct crypto_engine *engine, struct ablkcipher_request *req, bool need_pump)

    transfer the new request into the enginequeue

    :param struct crypto_engine \*engine:
        the hardware engine

    :param struct ablkcipher_request \*req:
        the request need to be listed into the engine queue

    :param bool need_pump:
        *undescribed*

.. _`crypto_transfer_cipher_request_to_engine`:

crypto_transfer_cipher_request_to_engine
========================================

.. c:function:: int crypto_transfer_cipher_request_to_engine(struct crypto_engine *engine, struct ablkcipher_request *req)

    transfer one request to list into the engine queue

    :param struct crypto_engine \*engine:
        the hardware engine

    :param struct ablkcipher_request \*req:
        the request need to be listed into the engine queue

.. _`crypto_transfer_hash_request`:

crypto_transfer_hash_request
============================

.. c:function:: int crypto_transfer_hash_request(struct crypto_engine *engine, struct ahash_request *req, bool need_pump)

    transfer the new request into the enginequeue

    :param struct crypto_engine \*engine:
        the hardware engine

    :param struct ahash_request \*req:
        the request need to be listed into the engine queue

    :param bool need_pump:
        *undescribed*

.. _`crypto_transfer_hash_request_to_engine`:

crypto_transfer_hash_request_to_engine
======================================

.. c:function:: int crypto_transfer_hash_request_to_engine(struct crypto_engine *engine, struct ahash_request *req)

    transfer one request to list into the engine queue

    :param struct crypto_engine \*engine:
        the hardware engine

    :param struct ahash_request \*req:
        the request need to be listed into the engine queue

.. _`crypto_finalize_cipher_request`:

crypto_finalize_cipher_request
==============================

.. c:function:: void crypto_finalize_cipher_request(struct crypto_engine *engine, struct ablkcipher_request *req, int err)

    finalize one request if the request is done

    :param struct crypto_engine \*engine:
        the hardware engine

    :param struct ablkcipher_request \*req:
        the request need to be finalized

    :param int err:
        error number

.. _`crypto_finalize_hash_request`:

crypto_finalize_hash_request
============================

.. c:function:: void crypto_finalize_hash_request(struct crypto_engine *engine, struct ahash_request *req, int err)

    finalize one request if the request is done

    :param struct crypto_engine \*engine:
        the hardware engine

    :param struct ahash_request \*req:
        the request need to be finalized

    :param int err:
        error number

.. _`crypto_engine_start`:

crypto_engine_start
===================

.. c:function:: int crypto_engine_start(struct crypto_engine *engine)

    start the hardware engine

    :param struct crypto_engine \*engine:
        the hardware engine need to be started

.. _`crypto_engine_start.description`:

Description
-----------

Return 0 on success, else on fail.

.. _`crypto_engine_stop`:

crypto_engine_stop
==================

.. c:function:: int crypto_engine_stop(struct crypto_engine *engine)

    stop the hardware engine

    :param struct crypto_engine \*engine:
        the hardware engine need to be stopped

.. _`crypto_engine_stop.description`:

Description
-----------

Return 0 on success, else on fail.

.. _`crypto_engine_alloc_init`:

crypto_engine_alloc_init
========================

.. c:function:: struct crypto_engine *crypto_engine_alloc_init(struct device *dev, bool rt)

    allocate crypto hardware engine structure and initialize it.

    :param struct device \*dev:
        the device attached with one hardware engine

    :param bool rt:
        whether this queue is set to run as a realtime task

.. _`crypto_engine_alloc_init.description`:

Description
-----------

This must be called from context that can sleep.

.. _`crypto_engine_alloc_init.return`:

Return
------

the crypto engine structure on success, else NULL.

.. _`crypto_engine_exit`:

crypto_engine_exit
==================

.. c:function:: int crypto_engine_exit(struct crypto_engine *engine)

    free the resources of hardware engine when exit

    :param struct crypto_engine \*engine:
        the hardware engine need to be freed

.. _`crypto_engine_exit.description`:

Description
-----------

Return 0 for success.

.. This file was automatic generated / don't edit.

