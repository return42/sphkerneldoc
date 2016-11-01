.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/sfc/mcdi.c

.. _`efx_mcdi_rpc`:

efx_mcdi_rpc
============

.. c:function:: int efx_mcdi_rpc(struct efx_nic *efx, unsigned cmd, const efx_dword_t *inbuf, size_t inlen, efx_dword_t *outbuf, size_t outlen, size_t *outlen_actual)

    Issue an MCDI command and wait for completion

    :param struct efx_nic \*efx:
        NIC through which to issue the command

    :param unsigned cmd:
        Command type number

    :param const efx_dword_t \*inbuf:
        Command parameters

    :param size_t inlen:
        Length of command parameters, in bytes.  Must be a multiple
        of 4 and no greater than \ ``MCDI_CTL_SDU_LEN_MAX_V1``\ .

    :param efx_dword_t \*outbuf:
        Response buffer.  May be \ ``NULL``\  if \ ``outlen``\  is 0.

    :param size_t outlen:
        Length of response buffer, in bytes.  If the actual
        response is longer than \ ``outlen``\  & ~3, it will be truncated
        to that length.

    :param size_t \*outlen_actual:
        Pointer through which to return the actual response
        length.  May be \ ``NULL``\  if this is not needed.

.. _`efx_mcdi_rpc.description`:

Description
-----------

This function may sleep and therefore must be called in an appropriate
context.

.. _`efx_mcdi_rpc.return`:

Return
------

A negative error code, or zero if successful.  The error
code may come from the MCDI response or may indicate a failure
to communicate with the MC.  In the former case, the response
will still be copied to \ ``outbuf``\  and \*@outlen_actual will be
set accordingly.  In the latter case, \*@outlen_actual will be
set to zero.

.. _`efx_mcdi_rpc_async`:

efx_mcdi_rpc_async
==================

.. c:function:: int efx_mcdi_rpc_async(struct efx_nic *efx, unsigned int cmd, const efx_dword_t *inbuf, size_t inlen, size_t outlen, efx_mcdi_async_completer *complete, unsigned long cookie)

    Schedule an MCDI command to run asynchronously

    :param struct efx_nic \*efx:
        NIC through which to issue the command

    :param unsigned int cmd:
        Command type number

    :param const efx_dword_t \*inbuf:
        Command parameters

    :param size_t inlen:
        Length of command parameters, in bytes

    :param size_t outlen:
        Length to allocate for response buffer, in bytes

    :param efx_mcdi_async_completer \*complete:
        Function to be called on completion or cancellation.

    :param unsigned long cookie:
        Arbitrary value to be passed to \ ``complete``\ .

.. _`efx_mcdi_rpc_async.description`:

Description
-----------

This function does not sleep and therefore may be called in atomic
context.  It will fail if event queues are disabled or if MCDI
event completions have been disabled due to an error.

If it succeeds, the \ ``complete``\  function will be called exactly once
in atomic context, when one of the following occurs:
(a) the completion event is received (in NAPI context)
(b) event queues are disabled (in the process that disables them)
(c) the request times-out (in timer context)

.. This file was automatic generated / don't edit.

