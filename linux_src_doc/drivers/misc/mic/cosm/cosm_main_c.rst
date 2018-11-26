.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/cosm/cosm_main.c

.. _`cosm_hw_reset`:

cosm_hw_reset
=============

.. c:function:: void cosm_hw_reset(struct cosm_device *cdev, bool force)

    Issue a HW reset for the MIC device

    :param cdev:
        pointer to cosm_device instance
    :type cdev: struct cosm_device \*

    :param force:
        *undescribed*
    :type force: bool

.. _`cosm_start`:

cosm_start
==========

.. c:function:: int cosm_start(struct cosm_device *cdev)

    Start the MIC

    :param cdev:
        pointer to cosm_device instance
    :type cdev: struct cosm_device \*

.. _`cosm_start.description`:

Description
-----------

This function prepares an MIC for boot and initiates boot.

.. _`cosm_start.return`:

Return
------

An appropriate -ERRNO error value on error, or 0 for success.

.. _`cosm_stop`:

cosm_stop
=========

.. c:function:: void cosm_stop(struct cosm_device *cdev, bool force)

    Prepare the MIC for reset and trigger reset

    :param cdev:
        pointer to cosm_device instance
    :type cdev: struct cosm_device \*

    :param force:
        force a MIC to reset even if it is already reset and ready.
    :type force: bool

.. _`cosm_stop.return`:

Return
------

None

.. _`cosm_reset_trigger_work`:

cosm_reset_trigger_work
=======================

.. c:function:: void cosm_reset_trigger_work(struct work_struct *work)

    Trigger MIC reset

    :param work:
        The work structure
    :type work: struct work_struct \*

.. _`cosm_reset_trigger_work.description`:

Description
-----------

This work is scheduled whenever the host wants to reset the MIC.

.. _`cosm_reset`:

cosm_reset
==========

.. c:function:: int cosm_reset(struct cosm_device *cdev)

    Schedule MIC reset

    :param cdev:
        pointer to cosm_device instance
    :type cdev: struct cosm_device \*

.. _`cosm_reset.return`:

Return
------

An -EINVAL if the card is already READY or 0 for success.

.. _`cosm_shutdown`:

cosm_shutdown
=============

.. c:function:: int cosm_shutdown(struct cosm_device *cdev)

    Initiate MIC shutdown.

    :param cdev:
        pointer to cosm_device instance
    :type cdev: struct cosm_device \*

.. _`cosm_shutdown.return`:

Return
------

None

.. This file was automatic generated / don't edit.

