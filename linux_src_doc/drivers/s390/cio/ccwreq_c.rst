.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/ccwreq.c

.. _`lpm_adjust`:

lpm_adjust
==========

.. c:function:: int lpm_adjust(int lpm, int mask)

    adjust path mask

    :param lpm:
        path mask to adjust
    :type lpm: int

    :param mask:
        mask of available paths
    :type mask: int

.. _`lpm_adjust.description`:

Description
-----------

Shift \ ``lpm``\  right until \ ``lpm``\  and \ ``mask``\  have at least one bit in common or
until \ ``lpm``\  is zero. Return the resulting lpm.

.. _`ccw_request_start`:

ccw_request_start
=================

.. c:function:: void ccw_request_start(struct ccw_device *cdev)

    perform I/O request

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_request_start.description`:

Description
-----------

Perform the I/O request specified by cdev->req.

.. _`ccw_request_cancel`:

ccw_request_cancel
==================

.. c:function:: int ccw_request_cancel(struct ccw_device *cdev)

    cancel running I/O request

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_request_cancel.description`:

Description
-----------

Cancel the I/O request specified by cdev->req. Return non-zero if request
has already finished, zero otherwise.

.. _`ccw_request_handler`:

ccw_request_handler
===================

.. c:function:: void ccw_request_handler(struct ccw_device *cdev)

    interrupt handler for I/O request procedure.

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_request_handler.description`:

Description
-----------

Handle interrupt during I/O request procedure.

.. _`ccw_request_timeout`:

ccw_request_timeout
===================

.. c:function:: void ccw_request_timeout(struct ccw_device *cdev)

    timeout handler for I/O request procedure

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_request_timeout.description`:

Description
-----------

Handle timeout during I/O request procedure.

.. _`ccw_request_notoper`:

ccw_request_notoper
===================

.. c:function:: void ccw_request_notoper(struct ccw_device *cdev)

    notoper handler for I/O request procedure

    :param cdev:
        ccw device
    :type cdev: struct ccw_device \*

.. _`ccw_request_notoper.description`:

Description
-----------

Handle notoper during I/O request procedure.

.. This file was automatic generated / don't edit.

