.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/ap_bus.c

.. _`ap_using_interrupts`:

ap_using_interrupts
===================

.. c:function:: int ap_using_interrupts( void)

    Returns non-zero if interrupt support is available.

    :param void:
        no arguments
    :type void: 

.. _`ap_airq_ptr`:

ap_airq_ptr
===========

.. c:function:: void *ap_airq_ptr( void)

    Get the address of the adapter interrupt indicator

    :param void:
        no arguments
    :type void: 

.. _`ap_airq_ptr.description`:

Description
-----------

Returns the address of the local-summary-indicator of the adapter
interrupt handler for AP, or NULL if adapter interrupts are not
available.

.. _`ap_interrupts_available`:

ap_interrupts_available
=======================

.. c:function:: int ap_interrupts_available( void)

    Test if AP interrupts are available.

    :param void:
        no arguments
    :type void: 

.. _`ap_interrupts_available.description`:

Description
-----------

Returns 1 if AP interrupts are available.

.. _`ap_configuration_available`:

ap_configuration_available
==========================

.. c:function:: int ap_configuration_available( void)

    Test if AP configuration information is available.

    :param void:
        no arguments
    :type void: 

.. _`ap_configuration_available.description`:

Description
-----------

Returns 1 if AP configuration information is available.

.. _`ap_apft_available`:

ap_apft_available
=================

.. c:function:: int ap_apft_available( void)

    Test if AP facilities test (APFT) facility is available.

    :param void:
        no arguments
    :type void: 

.. _`ap_apft_available.description`:

Description
-----------

Returns 1 if APFT is is available.

.. _`ap_init_configuration`:

ap_init_configuration
=====================

.. c:function:: void ap_init_configuration( void)

    Allocate and query configuration array.

    :param void:
        no arguments
    :type void: 

.. _`ap_query_queue`:

ap_query_queue
==============

.. c:function:: int ap_query_queue(ap_qid_t qid, int *queue_depth, int *device_type, unsigned int *facilities)

    Check if an AP queue is available.

    :param qid:
        The AP queue number
    :type qid: ap_qid_t

    :param queue_depth:
        Pointer to queue depth value
    :type queue_depth: int \*

    :param device_type:
        Pointer to device type value
    :type device_type: int \*

    :param facilities:
        Pointer to facility indicator
    :type facilities: unsigned int \*

.. _`ap_request_timeout`:

ap_request_timeout
==================

.. c:function:: void ap_request_timeout(struct timer_list *t)

    Handling of request timeouts

    :param t:
        timer making this callback
    :type t: struct timer_list \*

.. _`ap_request_timeout.description`:

Description
-----------

Handles request timeouts.

.. _`ap_poll_timeout`:

ap_poll_timeout
===============

.. c:function:: enum hrtimer_restart ap_poll_timeout(struct hrtimer *unused)

    AP receive polling for finished AP requests.

    :param unused:
        Unused pointer.
    :type unused: struct hrtimer \*

.. _`ap_poll_timeout.description`:

Description
-----------

Schedules the AP tasklet using a high resolution timer.

.. _`ap_interrupt_handler`:

ap_interrupt_handler
====================

.. c:function:: void ap_interrupt_handler(struct airq_struct *airq)

    Schedule ap_tasklet on interrupt

    :param airq:
        pointer to adapter interrupt descriptor
    :type airq: struct airq_struct \*

.. _`ap_tasklet_fn`:

ap_tasklet_fn
=============

.. c:function:: void ap_tasklet_fn(unsigned long dummy)

    Tasklet to poll all AP devices.

    :param dummy:
        Unused variable
    :type dummy: unsigned long

.. _`ap_tasklet_fn.description`:

Description
-----------

Poll all AP devices on the bus.

.. _`ap_poll_thread`:

ap_poll_thread
==============

.. c:function:: int ap_poll_thread(void *data)

    Thread that polls for finished requests.

    :param data:
        Unused pointer
    :type data: void \*

.. _`ap_poll_thread.description`:

Description
-----------

AP bus poll thread. The purpose of this thread is to poll for
finished requests in a loop if there is a "free" cpu - that is
a cpu that doesn't have anything better to do. The polling stops
as soon as there is another task or if all messages have been
delivered.

.. _`ap_bus_match`:

ap_bus_match
============

.. c:function:: int ap_bus_match(struct device *dev, struct device_driver *drv)

    :param dev:
        Pointer to device
    :type dev: struct device \*

    :param drv:
        Pointer to device_driver
    :type drv: struct device_driver \*

.. _`ap_bus_match.description`:

Description
-----------

AP bus driver registration/unregistration.

.. _`ap_uevent`:

ap_uevent
=========

.. c:function:: int ap_uevent(struct device *dev, struct kobj_uevent_env *env)

    Uevent function for AP devices.

    :param dev:
        Pointer to device
    :type dev: struct device \*

    :param env:
        Pointer to kobj_uevent_env
    :type env: struct kobj_uevent_env \*

.. _`ap_uevent.description`:

Description
-----------

It sets up a single environment variable DEV_TYPE which contains the
hardware device type.

.. _`ap_select_domain`:

ap_select_domain
================

.. c:function:: void ap_select_domain( void)

    Select an AP domain if possible and we haven't already done so before.

    :param void:
        no arguments
    :type void: 

.. _`ap_scan_bus`:

ap_scan_bus
===========

.. c:function:: void ap_scan_bus(struct work_struct *unused)

    Scan the AP bus for new devices Runs periodically, workqueue timer (ap_config_time)

    :param unused:
        *undescribed*
    :type unused: struct work_struct \*

.. _`ap_module_init`:

ap_module_init
==============

.. c:function:: int ap_module_init( void)

    The module initialization code.

    :param void:
        no arguments
    :type void: 

.. _`ap_module_init.description`:

Description
-----------

Initializes the module.

.. This file was automatic generated / don't edit.

