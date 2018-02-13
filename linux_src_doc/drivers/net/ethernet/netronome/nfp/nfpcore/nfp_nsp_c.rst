.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_nsp.c

.. _`nfp_nsp_open`:

nfp_nsp_open
============

.. c:function:: struct nfp_nsp *nfp_nsp_open(struct nfp_cpp *cpp)

    Prepare for communication and lock the NSP resource.

    :param struct nfp_cpp \*cpp:
        NFP CPP Handle

.. _`nfp_nsp_close`:

nfp_nsp_close
=============

.. c:function:: void nfp_nsp_close(struct nfp_nsp *state)

    Clean up and unlock the NSP resource.

    :param struct nfp_nsp \*state:
        NFP SP state

.. _`__nfp_nsp_command`:

__nfp_nsp_command
=================

.. c:function:: int __nfp_nsp_command(struct nfp_nsp *state, u16 code, u32 option, u32 buff_cpp, u64 buff_addr, u32 timeout_sec)

    Execute a command on the NFP Service Processor

    :param struct nfp_nsp \*state:
        NFP SP state

    :param u16 code:
        NFP SP Command Code

    :param u32 option:
        NFP SP Command Argument

    :param u32 buff_cpp:
        NFP SP Buffer CPP Address info

    :param u64 buff_addr:
        NFP SP Buffer Host address

    :param u32 timeout_sec:
        Timeout value to wait for completion in seconds

.. _`__nfp_nsp_command.return`:

Return
------

0 for success with no result

positive value for NSP completion with a result code

-EAGAIN if the NSP is not yet present
-ENODEV if the NSP is not a supported model
-EBUSY if the NSP is stuck
-EINTR if interrupted while waiting for completion
-ETIMEDOUT if the NSP took longer than \ ``timeout_sec``\  seconds to complete

.. This file was automatic generated / don't edit.

