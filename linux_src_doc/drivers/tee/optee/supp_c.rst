.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/tee/optee/supp.c

.. _`optee_supp_thrd_req`:

optee_supp_thrd_req
===================

.. c:function:: u32 optee_supp_thrd_req(struct tee_context *ctx, u32 func, size_t num_params, struct tee_param *param)

    request service from supplicant

    :param ctx:
        context doing the request
    :type ctx: struct tee_context \*

    :param func:
        function requested
    :type func: u32

    :param num_params:
        number of elements in \ ``param``\  array
    :type num_params: size_t

    :param param:
        parameters for function
    :type param: struct tee_param \*

.. _`optee_supp_thrd_req.description`:

Description
-----------

Returns result of operation to be passed to secure world

.. _`optee_supp_recv`:

optee_supp_recv
===============

.. c:function:: int optee_supp_recv(struct tee_context *ctx, u32 *func, u32 *num_params, struct tee_param *param)

    receive request for supplicant

    :param ctx:
        context receiving the request
    :type ctx: struct tee_context \*

    :param func:
        requested function in supplicant
    :type func: u32 \*

    :param num_params:
        number of elements allocated in \ ``param``\ , updated with number
        used elements
    :type num_params: u32 \*

    :param param:
        space for parameters for \ ``func``\ 
    :type param: struct tee_param \*

.. _`optee_supp_recv.description`:

Description
-----------

Returns 0 on success or <0 on failure

.. _`optee_supp_send`:

optee_supp_send
===============

.. c:function:: int optee_supp_send(struct tee_context *ctx, u32 ret, u32 num_params, struct tee_param *param)

    send result of request from supplicant

    :param ctx:
        context sending result
    :type ctx: struct tee_context \*

    :param ret:
        return value of request
    :type ret: u32

    :param num_params:
        number of parameters returned
    :type num_params: u32

    :param param:
        returned parameters
    :type param: struct tee_param \*

.. _`optee_supp_send.description`:

Description
-----------

Returns 0 on success or <0 on failure.

.. This file was automatic generated / don't edit.

