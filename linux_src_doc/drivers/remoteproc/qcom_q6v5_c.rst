.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/remoteproc/qcom_q6v5.c

.. _`qcom_q6v5_prepare`:

qcom_q6v5_prepare
=================

.. c:function:: int qcom_q6v5_prepare(struct qcom_q6v5 *q6v5)

    reinitialize the qcom_q6v5 context before start

    :param q6v5:
        reference to qcom_q6v5 context to be reinitialized
    :type q6v5: struct qcom_q6v5 \*

.. _`qcom_q6v5_prepare.return`:

Return
------

0 on success, negative errno on failure

.. _`qcom_q6v5_unprepare`:

qcom_q6v5_unprepare
===================

.. c:function:: int qcom_q6v5_unprepare(struct qcom_q6v5 *q6v5)

    unprepare the qcom_q6v5 context after stop

    :param q6v5:
        reference to qcom_q6v5 context to be unprepared
    :type q6v5: struct qcom_q6v5 \*

.. _`qcom_q6v5_unprepare.return`:

Return
------

0 on success, 1 if handover hasn't yet been called

.. _`qcom_q6v5_wait_for_start`:

qcom_q6v5_wait_for_start
========================

.. c:function:: int qcom_q6v5_wait_for_start(struct qcom_q6v5 *q6v5, int timeout)

    wait for remote processor start signal

    :param q6v5:
        reference to qcom_q6v5 context
    :type q6v5: struct qcom_q6v5 \*

    :param timeout:
        timeout to wait for the event, in jiffies
    :type timeout: int

.. _`qcom_q6v5_wait_for_start.description`:

Description
-----------

\ :c:func:`qcom_q6v5_unprepare`\  should not be called when this function fails.

.. _`qcom_q6v5_wait_for_start.return`:

Return
------

0 on success, -ETIMEDOUT on timeout

.. _`qcom_q6v5_request_stop`:

qcom_q6v5_request_stop
======================

.. c:function:: int qcom_q6v5_request_stop(struct qcom_q6v5 *q6v5)

    request the remote processor to stop

    :param q6v5:
        reference to qcom_q6v5 context
    :type q6v5: struct qcom_q6v5 \*

.. _`qcom_q6v5_request_stop.return`:

Return
------

0 on success, negative errno on failure

.. _`qcom_q6v5_init`:

qcom_q6v5_init
==============

.. c:function:: int qcom_q6v5_init(struct qcom_q6v5 *q6v5, struct platform_device *pdev, struct rproc *rproc, int crash_reason, void (*handover)(struct qcom_q6v5 *q6v5))

    initializer of the q6v5 common struct

    :param q6v5:
        handle to be initialized
    :type q6v5: struct qcom_q6v5 \*

    :param pdev:
        platform_device reference for acquiring resources
    :type pdev: struct platform_device \*

    :param rproc:
        associated remoteproc instance
    :type rproc: struct rproc \*

    :param crash_reason:
        SMEM id for crash reason string, or 0 if none
    :type crash_reason: int

    :param void (\*handover)(struct qcom_q6v5 \*q6v5):
        function to be called when proxy resources should be released

.. _`qcom_q6v5_init.return`:

Return
------

0 on success, negative errno on failure

.. This file was automatic generated / don't edit.

