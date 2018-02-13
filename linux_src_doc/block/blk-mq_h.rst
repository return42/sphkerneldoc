.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/blk-mq.h

.. _`blk_mq_rq_state`:

blk_mq_rq_state
===============

.. c:function:: int blk_mq_rq_state(struct request *rq)

    read the current MQ_RQ\_\* state of a request

    :param struct request \*rq:
        target request.

.. _`blk_mq_rq_update_state`:

blk_mq_rq_update_state
======================

.. c:function:: void blk_mq_rq_update_state(struct request *rq, enum mq_rq_state state)

    set the current MQ_RQ\_\* state of a request

    :param struct request \*rq:
        target request.

    :param enum mq_rq_state state:
        new state to set.

.. _`blk_mq_rq_update_state.description`:

Description
-----------

Set \ ``rq``\ 's state to \ ``state``\ .  The caller is responsible for ensuring that
there are no other updaters.  A request can transition into IN_FLIGHT
only from IDLE and doing so increments the generation number.

.. This file was automatic generated / don't edit.

