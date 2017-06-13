.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/supp.c

.. _`optee_supp_thrd_req`:

optee_supp_thrd_req
===================

.. c:function:: u32 optee_supp_thrd_req(struct tee_context *ctx, u32 func, size_t num_params, struct tee_param *param)

    request service from supplicant

    :param struct tee_context \*ctx:
        context doing the request

    :param u32 func:
        function requested

    :param size_t num_params:
        number of elements in \ ``param``\  array

    :param struct tee_param \*param:
        parameters for function

.. _`optee_supp_thrd_req.description`:

Description
-----------

Returns result of operation to be passed to secure world

.. _`optee_supp_recv`:

optee_supp_recv
===============

.. c:function:: int optee_supp_recv(struct tee_context *ctx, u32 *func, u32 *num_params, struct tee_param *param)

    receive request for supplicant

    :param struct tee_context \*ctx:
        context receiving the request

    :param u32 \*func:
        requested function in supplicant

    :param u32 \*num_params:
        number of elements allocated in \ ``param``\ , updated with number
        used elements

    :param struct tee_param \*param:
        space for parameters for \ ``func``\ 

.. _`optee_supp_recv.description`:

Description
-----------

Returns 0 on success or <0 on failure

.. _`optee_supp_send`:

optee_supp_send
===============

.. c:function:: int optee_supp_send(struct tee_context *ctx, u32 ret, u32 num_params, struct tee_param *param)

    send result of request from supplicant

    :param struct tee_context \*ctx:
        context sending result

    :param u32 ret:
        return value of request

    :param u32 num_params:
        number of parameters returned

    :param struct tee_param \*param:
        returned parameters

.. _`optee_supp_send.description`:

Description
-----------

Returns 0 on success or <0 on failure.

.. This file was automatic generated / don't edit.

