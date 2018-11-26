.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/time/tick-oneshot.c

.. _`tick_program_event`:

tick_program_event
==================

.. c:function:: int tick_program_event(ktime_t expires, int force)

    :param expires:
        *undescribed*
    :type expires: ktime_t

    :param force:
        *undescribed*
    :type force: int

.. _`tick_resume_oneshot`:

tick_resume_oneshot
===================

.. c:function:: void tick_resume_oneshot( void)

    resume oneshot mode

    :param void:
        no arguments
    :type void: 

.. _`tick_setup_oneshot`:

tick_setup_oneshot
==================

.. c:function:: void tick_setup_oneshot(struct clock_event_device *newdev, void (*handler)(struct clock_event_device *), ktime_t next_event)

    setup the event device for oneshot mode (hres or nohz)

    :param newdev:
        *undescribed*
    :type newdev: struct clock_event_device \*

    :param void (\*handler)(struct clock_event_device \*):
        *undescribed*

    :param next_event:
        *undescribed*
    :type next_event: ktime_t

.. _`tick_switch_to_oneshot`:

tick_switch_to_oneshot
======================

.. c:function:: int tick_switch_to_oneshot(void (*handler)(struct clock_event_device *))

    switch to oneshot mode

    :param void (\*handler)(struct clock_event_device \*):
        *undescribed*

.. _`tick_oneshot_mode_active`:

tick_oneshot_mode_active
========================

.. c:function:: int tick_oneshot_mode_active( void)

    check whether the system is in oneshot mode

    :param void:
        no arguments
    :type void: 

.. _`tick_oneshot_mode_active.description`:

Description
-----------

returns 1 when either nohz or highres are enabled. otherwise 0.

.. _`tick_init_highres`:

tick_init_highres
=================

.. c:function:: int tick_init_highres( void)

    switch to high resolution mode

    :param void:
        no arguments
    :type void: 

.. _`tick_init_highres.description`:

Description
-----------

Called with interrupts disabled.

.. This file was automatic generated / don't edit.

