.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/crypto_engine.c

.. _`crypto_finalize_request`:

crypto_finalize_request
=======================

.. c:function:: void crypto_finalize_request(struct crypto_engine *engine, struct crypto_async_request *req, int err)

    finalize one request if the request is done

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be finalized
    :type req: struct crypto_async_request \*

    :param err:
        error number
    :type err: int

.. _`crypto_pump_requests`:

crypto_pump_requests
====================

.. c:function:: void crypto_pump_requests(struct crypto_engine *engine, bool in_kthread)

    dequeue one request from engine queue to process

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param in_kthread:
        true if we are in the context of the request pump thread
    :type in_kthread: bool

.. _`crypto_pump_requests.description`:

Description
-----------

This function checks if there is any request in the engine queue that
needs processing and if so call out to the driver to initialize hardware
and handle each request.

.. _`crypto_transfer_request`:

crypto_transfer_request
=======================

.. c:function:: int crypto_transfer_request(struct crypto_engine *engine, struct crypto_async_request *req, bool need_pump)

    transfer the new request into the engine queue

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be listed into the engine queue
    :type req: struct crypto_async_request \*

    :param need_pump:
        *undescribed*
    :type need_pump: bool

.. _`crypto_transfer_request_to_engine`:

crypto_transfer_request_to_engine
=================================

.. c:function:: int crypto_transfer_request_to_engine(struct crypto_engine *engine, struct crypto_async_request *req)

    transfer one request to list into the engine queue

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be listed into the engine queue
    :type req: struct crypto_async_request \*

.. _`crypto_transfer_ablkcipher_request_to_engine`:

crypto_transfer_ablkcipher_request_to_engine
============================================

.. c:function:: int crypto_transfer_ablkcipher_request_to_engine(struct crypto_engine *engine, struct ablkcipher_request *req)

    transfer one ablkcipher_request to list into the engine queue

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be listed into the engine queue
    :type req: struct ablkcipher_request \*

.. _`crypto_transfer_ablkcipher_request_to_engine.todo`:

TODO
----

Remove this function when skcipher conversion is finished

.. _`crypto_transfer_aead_request_to_engine`:

crypto_transfer_aead_request_to_engine
======================================

.. c:function:: int crypto_transfer_aead_request_to_engine(struct crypto_engine *engine, struct aead_request *req)

    transfer one aead_request to list into the engine queue

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be listed into the engine queue
    :type req: struct aead_request \*

.. _`crypto_transfer_akcipher_request_to_engine`:

crypto_transfer_akcipher_request_to_engine
==========================================

.. c:function:: int crypto_transfer_akcipher_request_to_engine(struct crypto_engine *engine, struct akcipher_request *req)

    transfer one akcipher_request to list into the engine queue

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be listed into the engine queue
    :type req: struct akcipher_request \*

.. _`crypto_transfer_hash_request_to_engine`:

crypto_transfer_hash_request_to_engine
======================================

.. c:function:: int crypto_transfer_hash_request_to_engine(struct crypto_engine *engine, struct ahash_request *req)

    transfer one ahash_request to list into the engine queue

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be listed into the engine queue
    :type req: struct ahash_request \*

.. _`crypto_transfer_skcipher_request_to_engine`:

crypto_transfer_skcipher_request_to_engine
==========================================

.. c:function:: int crypto_transfer_skcipher_request_to_engine(struct crypto_engine *engine, struct skcipher_request *req)

    transfer one skcipher_request to list into the engine queue

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be listed into the engine queue
    :type req: struct skcipher_request \*

.. _`crypto_finalize_ablkcipher_request`:

crypto_finalize_ablkcipher_request
==================================

.. c:function:: void crypto_finalize_ablkcipher_request(struct crypto_engine *engine, struct ablkcipher_request *req, int err)

    finalize one ablkcipher_request if the request is done

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be finalized
    :type req: struct ablkcipher_request \*

    :param err:
        error number
    :type err: int

.. _`crypto_finalize_ablkcipher_request.todo`:

TODO
----

Remove this function when skcipher conversion is finished

.. _`crypto_finalize_aead_request`:

crypto_finalize_aead_request
============================

.. c:function:: void crypto_finalize_aead_request(struct crypto_engine *engine, struct aead_request *req, int err)

    finalize one aead_request if the request is done

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be finalized
    :type req: struct aead_request \*

    :param err:
        error number
    :type err: int

.. _`crypto_finalize_akcipher_request`:

crypto_finalize_akcipher_request
================================

.. c:function:: void crypto_finalize_akcipher_request(struct crypto_engine *engine, struct akcipher_request *req, int err)

    finalize one akcipher_request if the request is done

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be finalized
    :type req: struct akcipher_request \*

    :param err:
        error number
    :type err: int

.. _`crypto_finalize_hash_request`:

crypto_finalize_hash_request
============================

.. c:function:: void crypto_finalize_hash_request(struct crypto_engine *engine, struct ahash_request *req, int err)

    finalize one ahash_request if the request is done

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be finalized
    :type req: struct ahash_request \*

    :param err:
        error number
    :type err: int

.. _`crypto_finalize_skcipher_request`:

crypto_finalize_skcipher_request
================================

.. c:function:: void crypto_finalize_skcipher_request(struct crypto_engine *engine, struct skcipher_request *req, int err)

    finalize one skcipher_request if the request is done

    :param engine:
        the hardware engine
    :type engine: struct crypto_engine \*

    :param req:
        the request need to be finalized
    :type req: struct skcipher_request \*

    :param err:
        error number
    :type err: int

.. _`crypto_engine_start`:

crypto_engine_start
===================

.. c:function:: int crypto_engine_start(struct crypto_engine *engine)

    start the hardware engine

    :param engine:
        the hardware engine need to be started
    :type engine: struct crypto_engine \*

.. _`crypto_engine_start.description`:

Description
-----------

Return 0 on success, else on fail.

.. _`crypto_engine_stop`:

crypto_engine_stop
==================

.. c:function:: int crypto_engine_stop(struct crypto_engine *engine)

    stop the hardware engine

    :param engine:
        the hardware engine need to be stopped
    :type engine: struct crypto_engine \*

.. _`crypto_engine_stop.description`:

Description
-----------

Return 0 on success, else on fail.

.. _`crypto_engine_alloc_init`:

crypto_engine_alloc_init
========================

.. c:function:: struct crypto_engine *crypto_engine_alloc_init(struct device *dev, bool rt)

    allocate crypto hardware engine structure and initialize it.

    :param dev:
        the device attached with one hardware engine
    :type dev: struct device \*

    :param rt:
        whether this queue is set to run as a realtime task
    :type rt: bool

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

    :param engine:
        the hardware engine need to be freed
    :type engine: struct crypto_engine \*

.. _`crypto_engine_exit.description`:

Description
-----------

Return 0 for success.

.. This file was automatic generated / don't edit.

