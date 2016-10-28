.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/textsearch_fsm.h

.. _`ts_fsm_token`:

struct ts_fsm_token
===================

.. c:type:: struct ts_fsm_token

    state machine token (state)

.. _`ts_fsm_token.definition`:

Definition
----------

.. code-block:: c

    struct ts_fsm_token {
        __u16 type;
        __u8 recur;
        __u8 value;
    }

.. _`ts_fsm_token.members`:

Members
-------

type
    type of token

recur
    number of recurrences

value
    character value for TS_FSM_SPECIFIC

.. This file was automatic generated / don't edit.

