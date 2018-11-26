.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_nsp.c

.. _`nfp_nsp_command_arg`:

struct nfp_nsp_command_arg
==========================

.. c:type:: struct nfp_nsp_command_arg

    NFP command argument structure

.. _`nfp_nsp_command_arg.definition`:

Definition
----------

.. code-block:: c

    struct nfp_nsp_command_arg {
        u16 code;
        unsigned int timeout_sec;
        u32 option;
        u32 buff_cpp;
        u64 buff_addr;
        void (*error_cb)(struct nfp_nsp *state, u32 ret_val);
    }

.. _`nfp_nsp_command_arg.members`:

Members
-------

code
    NFP SP Command Code

timeout_sec
    Timeout value to wait for completion in seconds

option
    NFP SP Command Argument

buff_cpp
    NFP SP Buffer CPP Address info

buff_addr
    NFP SP Buffer Host address

error_cb
    Callback for interpreting option if error occurred

.. _`nfp_nsp_command_buf_arg`:

struct nfp_nsp_command_buf_arg
==============================

.. c:type:: struct nfp_nsp_command_buf_arg

    NFP command with buffer argument structure

.. _`nfp_nsp_command_buf_arg.definition`:

Definition
----------

.. code-block:: c

    struct nfp_nsp_command_buf_arg {
        struct nfp_nsp_command_arg arg;
        const void *in_buf;
        unsigned int in_size;
        void *out_buf;
        unsigned int out_size;
    }

.. _`nfp_nsp_command_buf_arg.members`:

Members
-------

arg
    NFP command argument structure

in_buf
    Buffer with data for input

in_size
    Size of \ ``in_buf``\ 

out_buf
    Buffer for output data

out_size
    Size of \ ``out_buf``\ 

.. _`nfp_nsp_open`:

nfp_nsp_open
============

.. c:function:: struct nfp_nsp *nfp_nsp_open(struct nfp_cpp *cpp)

    Prepare for communication and lock the NSP resource.

    :param cpp:
        NFP CPP Handle
    :type cpp: struct nfp_cpp \*

.. _`nfp_nsp_close`:

nfp_nsp_close
=============

.. c:function:: void nfp_nsp_close(struct nfp_nsp *state)

    Clean up and unlock the NSP resource.

    :param state:
        NFP SP state
    :type state: struct nfp_nsp \*

.. _`__nfp_nsp_command`:

\__nfp_nsp_command
==================

.. c:function:: int __nfp_nsp_command(struct nfp_nsp *state, const struct nfp_nsp_command_arg *arg)

    Execute a command on the NFP Service Processor

    :param state:
        NFP SP state
    :type state: struct nfp_nsp \*

    :param arg:
        NFP command argument structure
    :type arg: const struct nfp_nsp_command_arg \*

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

