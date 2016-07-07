.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/ibmasm/r_heartbeat.c

.. _`ibmasm_start_reverse_heartbeat`:

ibmasm_start_reverse_heartbeat
==============================

.. c:function:: int ibmasm_start_reverse_heartbeat(struct service_processor *sp, struct reverse_heartbeat *rhb)

    Loop forever, sending a reverse heartbeat dot command to the service processor, then sleeping. The loop comes to an end if the service processor fails to respond 3 times or we were interrupted.

    :param struct service_processor \*sp:
        *undescribed*

    :param struct reverse_heartbeat \*rhb:
        *undescribed*

.. This file was automatic generated / don't edit.

