.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/marvell/octeontx2/af/cgx.c

.. _`lmac`:

struct lmac
===========

.. c:type:: struct lmac


.. _`lmac.definition`:

Definition
----------

.. code-block:: c

    struct lmac {
        wait_queue_head_t wq_cmd_cmplt;
        struct mutex cmd_lock;
        u64 resp;
        struct cgx_link_user_info link_info;
        struct cgx_event_cb event_cb;
        bool cmd_pend;
        struct cgx *cgx;
        u8 lmac_id;
        char *name;
    }

.. _`lmac.members`:

Members
-------

wq_cmd_cmplt
    waitq to keep the process blocked until cmd completion

cmd_lock
    Lock to serialize the command interface

resp
    command response

link_info
    link related information

event_cb
    callback for linkchange events

cmd_pend
    flag set before new command is started
    flag cleared after command response is received

cgx
    parent cgx port

lmac_id
    lmac port id

name
    lmac port name

.. This file was automatic generated / don't edit.

