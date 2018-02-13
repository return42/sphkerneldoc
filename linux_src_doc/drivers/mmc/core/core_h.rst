.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/core.h

.. _`mmc_claim_host`:

mmc_claim_host
==============

.. c:function:: void mmc_claim_host(struct mmc_host *host)

    exclusively claim a host

    :param struct mmc_host \*host:
        mmc host to claim

.. _`mmc_claim_host.description`:

Description
-----------

Claim a host for a set of operations.

.. _`mmc_pre_req`:

mmc_pre_req
===========

.. c:function:: void mmc_pre_req(struct mmc_host *host, struct mmc_request *mrq)

    Prepare for a new request

    :param struct mmc_host \*host:
        MMC host to prepare command

    :param struct mmc_request \*mrq:
        MMC request to prepare for

.. _`mmc_pre_req.description`:

Description
-----------

\ :c:func:`mmc_pre_req`\  is called in prior to \ :c:func:`mmc_start_req`\  to let
host prepare for the new request. Preparation of a request may be
performed while another request is running on the host.

.. _`mmc_post_req`:

mmc_post_req
============

.. c:function:: void mmc_post_req(struct mmc_host *host, struct mmc_request *mrq, int err)

    Post process a completed request

    :param struct mmc_host \*host:
        MMC host to post process command

    :param struct mmc_request \*mrq:
        MMC request to post process for

    :param int err:
        Error, if non zero, clean up any resources made in pre_req

.. _`mmc_post_req.description`:

Description
-----------

Let the host post process a completed request. Post processing of
a request may be performed while another request is running.

.. This file was automatic generated / don't edit.

