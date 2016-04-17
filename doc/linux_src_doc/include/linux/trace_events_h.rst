.. -*- coding: utf-8; mode: rst -*-

==============
trace_events.h
==============


.. _`trace_trigger_soft_disabled`:

trace_trigger_soft_disabled
===========================

.. c:function:: bool trace_trigger_soft_disabled (struct trace_event_file *file)

    do triggers and test if soft disabled

    :param struct trace_event_file \*file:
        The file pointer of the event to test



.. _`trace_trigger_soft_disabled.description`:

Description
-----------

If any triggers without filters are attached to this event, they
will be called here. If the event is soft disabled and has no
triggers that require testing the fields, it will return true,
otherwise false.



.. _`event_trigger_unlock_commit`:

event_trigger_unlock_commit
===========================

.. c:function:: void event_trigger_unlock_commit (struct trace_event_file *file, struct ring_buffer *buffer, struct ring_buffer_event *event, void *entry, unsigned long irq_flags, int pc)

    handle triggers and finish event commit

    :param struct trace_event_file \*file:
        The file pointer assoctiated to the event

    :param struct ring_buffer \*buffer:
        The ring buffer that the event is being written to

    :param struct ring_buffer_event \*event:
        The event meta data in the ring buffer

    :param void \*entry:
        The event itself

    :param unsigned long irq_flags:
        The state of the interrupts at the start of the event

    :param int pc:
        The state of the preempt count at the start of the event.



.. _`event_trigger_unlock_commit.description`:

Description
-----------

This is a helper function to handle triggers that require data
from the event itself. It also tests the event against filters and
if the event is soft disabled and should be discarded.



.. _`event_trigger_unlock_commit_regs`:

event_trigger_unlock_commit_regs
================================

.. c:function:: void event_trigger_unlock_commit_regs (struct trace_event_file *file, struct ring_buffer *buffer, struct ring_buffer_event *event, void *entry, unsigned long irq_flags, int pc, struct pt_regs *regs)

    handle triggers and finish event commit

    :param struct trace_event_file \*file:
        The file pointer assoctiated to the event

    :param struct ring_buffer \*buffer:
        The ring buffer that the event is being written to

    :param struct ring_buffer_event \*event:
        The event meta data in the ring buffer

    :param void \*entry:
        The event itself

    :param unsigned long irq_flags:
        The state of the interrupts at the start of the event

    :param int pc:
        The state of the preempt count at the start of the event.

    :param struct pt_regs \*regs:

        *undescribed*



.. _`event_trigger_unlock_commit_regs.description`:

Description
-----------

This is a helper function to handle triggers that require data
from the event itself. It also tests the event against filters and
if the event is soft disabled and should be discarded.

Same as :c:func:`event_trigger_unlock_commit` but calls
:c:func:`trace_buffer_unlock_commit_regs` instead of :c:func:`trace_buffer_unlock_commit`.

