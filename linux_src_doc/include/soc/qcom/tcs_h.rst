.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/soc/qcom/tcs.h

.. _`tcs_cmd`:

struct tcs_cmd
==============

.. c:type:: struct tcs_cmd

    an individual request to RPMH.

.. _`tcs_cmd.definition`:

Definition
----------

.. code-block:: c

    struct tcs_cmd {
        u32 addr;
        u32 data;
        u32 wait;
    }

.. _`tcs_cmd.members`:

Members
-------

addr
    the address of the resource slv_id:18:16 \| offset:0:15

data
    the resource state request

wait
    wait for this request to be complete before sending the next

.. _`tcs_request`:

struct tcs_request
==================

.. c:type:: struct tcs_request

    A set of tcs_cmds sent together in a TCS

.. _`tcs_request.definition`:

Definition
----------

.. code-block:: c

    struct tcs_request {
        enum rpmh_state state;
        u32 wait_for_compl;
        u32 num_cmds;
        struct tcs_cmd *cmds;
    }

.. _`tcs_request.members`:

Members
-------

state
    state for the request.

wait_for_compl
    wait until we get a response from the h/w accelerator

num_cmds
    the number of \ ``cmds``\  in this request

cmds
    an array of tcs_cmds

.. This file was automatic generated / don't edit.

