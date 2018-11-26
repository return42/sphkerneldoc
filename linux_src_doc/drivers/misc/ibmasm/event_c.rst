.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/ibmasm/event.c

.. _`ibmasm_receive_event`:

ibmasm_receive_event
====================

.. c:function:: void ibmasm_receive_event(struct service_processor *sp, void *data, unsigned int data_size)

    Called by the interrupt handler when a dot command of type sp_event is received. Store the event in the circular event buffer, wake up any sleeping event readers. There is no reader marker in the buffer, therefore readers are responsible for keeping up with the writer, or they will lose events.

    :param sp:
        *undescribed*
    :type sp: struct service_processor \*

    :param data:
        *undescribed*
    :type data: void \*

    :param data_size:
        *undescribed*
    :type data_size: unsigned int

.. _`ibmasm_get_next_event`:

ibmasm_get_next_event
=====================

.. c:function:: int ibmasm_get_next_event(struct service_processor *sp, struct event_reader *reader)

    Called by event readers (initiated from user space through the file system). Sleeps until a new event is available.

    :param sp:
        *undescribed*
    :type sp: struct service_processor \*

    :param reader:
        *undescribed*
    :type reader: struct event_reader \*

.. This file was automatic generated / don't edit.

