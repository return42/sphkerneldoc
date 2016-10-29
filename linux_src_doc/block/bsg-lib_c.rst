.. -*- coding: utf-8; mode: rst -*-
.. src-file: block/bsg-lib.c

.. _`bsg_destroy_job`:

bsg_destroy_job
===============

.. c:function:: void bsg_destroy_job(struct bsg_job *job)

    routine to teardown/delete a bsg job

    :param struct bsg_job \*job:
        bsg_job that is to be torn down

.. _`bsg_job_done`:

bsg_job_done
============

.. c:function:: void bsg_job_done(struct bsg_job *job, int result, unsigned int reply_payload_rcv_len)

    completion routine for bsg requests

    :param struct bsg_job \*job:
        bsg_job that is complete

    :param int result:
        job reply result

    :param unsigned int reply_payload_rcv_len:
        length of payload recvd

.. _`bsg_job_done.description`:

Description
-----------

The LLD should call this when the bsg job has completed.

.. _`bsg_softirq_done`:

bsg_softirq_done
================

.. c:function:: void bsg_softirq_done(struct request *rq)

    softirq done routine for destroying the bsg requests

    :param struct request \*rq:
        BSG request that holds the job to be destroyed

.. _`bsg_create_job`:

bsg_create_job
==============

.. c:function:: int bsg_create_job(struct device *dev, struct request *req)

    create the bsg_job structure for the bsg request

    :param struct device \*dev:
        device that is being sent the bsg request

    :param struct request \*req:
        BSG request that needs a job structure

.. _`bsg_request_fn`:

bsg_request_fn
==============

.. c:function:: void bsg_request_fn(struct request_queue *q)

    generic handler for bsg requests

    :param struct request_queue \*q:
        request queue to manage

.. _`bsg_request_fn.description`:

Description
-----------

On error the create_bsg_job function should return a -Exyz error value
that will be set to the req->errors.

Drivers/subsys should pass this to the queue init function.

.. _`bsg_setup_queue`:

bsg_setup_queue
===============

.. c:function:: int bsg_setup_queue(struct device *dev, struct request_queue *q, char *name, bsg_job_fn *job_fn, int dd_job_size)

    Create and add the bsg hooks so we can receive requests

    :param struct device \*dev:
        device to attach bsg device to

    :param struct request_queue \*q:
        request queue setup by caller

    :param char \*name:
        device to give bsg device

    :param bsg_job_fn \*job_fn:
        bsg job handler

    :param int dd_job_size:
        size of LLD data needed for each job

.. _`bsg_setup_queue.description`:

Description
-----------

The caller should have setup the reuqest queue with bsg_request_fn
as the request_fn.

.. This file was automatic generated / don't edit.
