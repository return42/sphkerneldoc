.. -*- coding: utf-8; mode: rst -*-

========
ap_bus.c
========


.. _`ap_using_interrupts`:

ap_using_interrupts
===================

.. c:function:: int ap_using_interrupts ( void)

    Returns non-zero if interrupt support is available.

    :param void:
        no arguments



.. _`ap_instructions_available`:

ap_instructions_available
=========================

.. c:function:: int ap_instructions_available ( void)

    Test if AP instructions are available.

    :param void:
        no arguments



.. _`ap_instructions_available.description`:

Description
-----------


Returns 0 if the AP instructions are installed.



.. _`ap_interrupts_available`:

ap_interrupts_available
=======================

.. c:function:: int ap_interrupts_available ( void)

    :param void:
        no arguments



.. _`ap_interrupts_available.description`:

Description
-----------


Returns 1 if AP interrupts are available.



.. _`ap_configuration_available`:

ap_configuration_available
==========================

.. c:function:: int ap_configuration_available ( void)

    :param void:
        no arguments



.. _`ap_configuration_available.description`:

Description
-----------

information is available.

Returns 1 if AP configuration information is available.



.. _`ap_test_queue`:

ap_test_queue
=============

.. c:function:: struct ap_queue_status ap_test_queue (ap_qid_t qid, unsigned long *info)

    :param ap_qid_t qid:
        The AP queue number

    :param unsigned long \*info:
        Pointer to queue descriptor



.. _`ap_test_queue.description`:

Description
-----------

Returns AP queue status structure.



.. _`ap_reset_queue`:

ap_reset_queue
==============

.. c:function:: struct ap_queue_status ap_reset_queue (ap_qid_t qid)

    :param ap_qid_t qid:
        The AP queue number



.. _`ap_reset_queue.description`:

Description
-----------

Returns AP queue status structure.



.. _`ap_queue_interruption_control`:

ap_queue_interruption_control
=============================

.. c:function:: struct ap_queue_status ap_queue_interruption_control (ap_qid_t qid, void *ind)

    :param ap_qid_t qid:
        The AP queue number

    :param void \*ind:
        The notification indicator byte



.. _`ap_queue_interruption_control.description`:

Description
-----------

Returns AP queue status.



.. _`ap_query_configuration`:

ap_query_configuration
======================

.. c:function:: int ap_query_configuration ( void)

    :param void:
        no arguments



.. _`ap_query_configuration.description`:

Description
-----------


Returns 0 on success, or -EOPNOTSUPP.



.. _`ap_init_configuration`:

ap_init_configuration
=====================

.. c:function:: void ap_init_configuration ( void)

    :param void:
        no arguments



.. _`ap_queue_enable_interruption`:

ap_queue_enable_interruption
============================

.. c:function:: int ap_queue_enable_interruption (struct ap_device *ap_dev, void *ind)

    :param struct ap_device \*ap_dev:

        *undescribed*

    :param void \*ind:
        the notification indicator byte



.. _`ap_queue_enable_interruption.description`:

Description
-----------

Enables interruption on AP queue via :c:func:`ap_queue_interruption_control`. Based
on the return value it waits a while and tests the AP queue if interrupts
have been switched on using :c:func:`ap_test_queue`.



.. _`__ap_send`:

__ap_send
=========

.. c:function:: struct ap_queue_status __ap_send (ap_qid_t qid, unsigned long long psmid, void *msg, size_t length, unsigned int special)

    :param ap_qid_t qid:
        The AP queue number

    :param unsigned long long psmid:
        The program supplied message identifier

    :param void \*msg:
        The message text

    :param size_t length:
        The message length

    :param unsigned int special:
        Special Bit



.. _`__ap_send.description`:

Description
-----------

Returns AP queue status structure.
Condition code 1 on NQAP can't happen because the L bit is 1.
Condition code 2 on NQAP also means the send is incomplete,
because a segment boundary was reached. The NQAP is repeated.



.. _`__ap_recv`:

__ap_recv
=========

.. c:function:: struct ap_queue_status __ap_recv (ap_qid_t qid, unsigned long long *psmid, void *msg, size_t length)

    :param ap_qid_t qid:
        The AP queue number

    :param unsigned long long \*psmid:
        Pointer to program supplied message identifier

    :param void \*msg:
        The message text

    :param size_t length:
        The message length



.. _`__ap_recv.description`:

Description
-----------

Returns AP queue status structure.
Condition code 1 on DQAP means the receive has taken place
but only partially.        The response is incomplete, hence the
DQAP is repeated.
Condition code 2 on DQAP also means the receive is incomplete,
this time because a segment boundary was reached. Again, the
DQAP is repeated.
Note that gpr2 is used by the DQAP instruction to keep track of
any 'residual' length, in case the instruction gets interrupted.
Hence it gets zeroed before the instruction.



.. _`ap_query_queue`:

ap_query_queue
==============

.. c:function:: int ap_query_queue (ap_qid_t qid, int *queue_depth, int *device_type, unsigned int *facilities)

    :param ap_qid_t qid:
        The AP queue number

    :param int \*queue_depth:
        Pointer to queue depth value

    :param int \*device_type:
        Pointer to device type value

    :param unsigned int \*facilities:
        Pointer to facility indicator



.. _`ap_sm_recv`:

ap_sm_recv
==========

.. c:function:: struct ap_queue_status ap_sm_recv (struct ap_device *ap_dev)

    :param struct ap_device \*ap_dev:
        pointer to the AP device



.. _`ap_sm_recv.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT



.. _`ap_sm_recv.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT



.. _`ap_sm_read`:

ap_sm_read
==========

.. c:function:: enum ap_wait ap_sm_read (struct ap_device *ap_dev)

    :param struct ap_device \*ap_dev:
        pointer to the AP device



.. _`ap_sm_read.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT



.. _`ap_sm_write`:

ap_sm_write
===========

.. c:function:: enum ap_wait ap_sm_write (struct ap_device *ap_dev)

    :param struct ap_device \*ap_dev:
        pointer to the AP device



.. _`ap_sm_write.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT



.. _`ap_sm_read_write`:

ap_sm_read_write
================

.. c:function:: enum ap_wait ap_sm_read_write (struct ap_device *ap_dev)

    :param struct ap_device \*ap_dev:
        pointer to the AP device



.. _`ap_sm_read_write.description`:

Description
-----------

Returns AP_WAIT_NONE, AP_WAIT_AGAIN, or AP_WAIT_INTERRUPT



.. _`ap_sm_reset`:

ap_sm_reset
===========

.. c:function:: enum ap_wait ap_sm_reset (struct ap_device *ap_dev)

    :param struct ap_device \*ap_dev:

        *undescribed*



.. _`ap_sm_reset.description`:

Description
-----------

Submit the Reset command to an AP queue.



.. _`ap_sm_reset_wait`:

ap_sm_reset_wait
================

.. c:function:: enum ap_wait ap_sm_reset_wait (struct ap_device *ap_dev)

    :param struct ap_device \*ap_dev:
        pointer to the AP device



.. _`ap_sm_reset_wait.description`:

Description
-----------

Returns AP_POLL_IMMEDIATELY, AP_POLL_AFTER_TIMEROUT or 0.



.. _`ap_sm_setirq_wait`:

ap_sm_setirq_wait
=================

.. c:function:: enum ap_wait ap_sm_setirq_wait (struct ap_device *ap_dev)

    :param struct ap_device \*ap_dev:
        pointer to the AP device



.. _`ap_sm_setirq_wait.description`:

Description
-----------

Returns AP_POLL_IMMEDIATELY, AP_POLL_AFTER_TIMEROUT or 0.



.. _`ap_request_timeout`:

ap_request_timeout
==================

.. c:function:: void ap_request_timeout (unsigned long data)

    :param unsigned long data:
        Holds the AP device.



.. _`ap_request_timeout.description`:

Description
-----------

Handles request timeouts.



.. _`ap_poll_timeout`:

ap_poll_timeout
===============

.. c:function:: enum hrtimer_restart ap_poll_timeout (struct hrtimer *unused)

    :param struct hrtimer \*unused:
        Unused pointer.



.. _`ap_poll_timeout.description`:

Description
-----------

Schedules the AP tasklet using a high resolution timer.



.. _`ap_interrupt_handler`:

ap_interrupt_handler
====================

.. c:function:: void ap_interrupt_handler (struct airq_struct *airq)

    Schedule ap_tasklet on interrupt

    :param struct airq_struct \*airq:
        pointer to adapter interrupt descriptor



.. _`ap_tasklet_fn`:

ap_tasklet_fn
=============

.. c:function:: void ap_tasklet_fn (unsigned long dummy)

    :param unsigned long dummy:
        Unused variable



.. _`ap_tasklet_fn.description`:

Description
-----------

Poll all AP devices on the bus.



.. _`ap_poll_thread`:

ap_poll_thread
==============

.. c:function:: int ap_poll_thread (void *data)

    :param void \*data:
        Unused pointer



.. _`ap_poll_thread.description`:

Description
-----------

AP bus poll thread. The purpose of this thread is to poll for
finished requests in a loop if there is a "free" cpu - that is
a cpu that doesn't have anything better to do. The polling stops
as soon as there is another task or if all messages have been
delivered.



.. _`ap_queue_message`:

ap_queue_message
================

.. c:function:: void ap_queue_message (struct ap_device *ap_dev, struct ap_message *ap_msg)

    :param struct ap_device \*ap_dev:
        The AP device to queue the message to

    :param struct ap_message \*ap_msg:
        The message that is to be added



.. _`ap_cancel_message`:

ap_cancel_message
=================

.. c:function:: void ap_cancel_message (struct ap_device *ap_dev, struct ap_message *ap_msg)

    :param struct ap_device \*ap_dev:
        The AP device that has the message queued

    :param struct ap_message \*ap_msg:
        The message that is to be removed



.. _`ap_cancel_message.description`:

Description
-----------

Cancel a crypto request. This is done by removing the request
from the device pending or request queue. Note that the
request stays on the AP queue. When it finishes the message
reply will be discarded because the psmid can't be found.



.. _`ap_bus_match`:

ap_bus_match
============

.. c:function:: int ap_bus_match (struct device *dev, struct device_driver *drv)

    :param struct device \*dev:
        Pointer to device

    :param struct device_driver \*drv:
        Pointer to device_driver



.. _`ap_bus_match.description`:

Description
-----------

AP bus driver registration/unregistration.



.. _`ap_uevent`:

ap_uevent
=========

.. c:function:: int ap_uevent (struct device *dev, struct kobj_uevent_env *env)

    :param struct device \*dev:
        Pointer to device

    :param struct kobj_uevent_env \*env:
        Pointer to kobj_uevent_env



.. _`ap_uevent.description`:

Description
-----------

It sets up a single environment variable DEV_TYPE which contains the
hardware device type.



.. _`__ap_flush_queue`:

__ap_flush_queue
================

.. c:function:: void __ap_flush_queue (struct ap_device *ap_dev)

    :param struct ap_device \*ap_dev:
        Pointer to the AP device



.. _`__ap_flush_queue.description`:

Description
-----------

Flush all requests from the request/pending queue of an AP device.



.. _`ap_select_domain`:

ap_select_domain
================

.. c:function:: int ap_select_domain ( void)

    :param void:
        no arguments



.. _`ap_select_domain.description`:

Description
-----------


Pick one of the 16 AP domains.



.. _`__ap_scan_bus`:

__ap_scan_bus
=============

.. c:function:: int __ap_scan_bus (struct device *dev, void *data)

    :param struct device \*dev:
        Pointer to device

    :param void \*data:
        Pointer to data



.. _`__ap_scan_bus.description`:

Description
-----------

Scan the AP bus for new devices.



.. _`ap_module_init`:

ap_module_init
==============

.. c:function:: int ap_module_init ( void)

    :param void:
        no arguments



.. _`ap_module_init.description`:

Description
-----------


Initializes the module.



.. _`ap_module_exit`:

ap_module_exit
==============

.. c:function:: void ap_module_exit ( void)

    :param void:
        no arguments



.. _`ap_module_exit.description`:

Description
-----------


Terminates the module.

