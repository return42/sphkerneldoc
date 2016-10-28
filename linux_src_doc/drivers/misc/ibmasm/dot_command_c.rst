.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/ibmasm/dot_command.c

.. _`ibmasm_receive_message`:

ibmasm_receive_message
======================

.. c:function:: void ibmasm_receive_message(struct service_processor *sp, void *message, int message_size)

    Called from interrupt context.

    :param struct service_processor \*sp:
        *undescribed*

    :param void \*message:
        *undescribed*

    :param int message_size:
        *undescribed*

.. _`ibmasm_send_driver_vpd`:

ibmasm_send_driver_vpd
======================

.. c:function:: int ibmasm_send_driver_vpd(struct service_processor *sp)

    :param struct service_processor \*sp:
        *undescribed*

.. _`ibmasm_send_os_state`:

ibmasm_send_os_state
====================

.. c:function:: int ibmasm_send_os_state(struct service_processor *sp, int os_state)

    During driver init this function is called with os state "up". This causes the service processor to start sending heartbeats the driver. During driver exit the function is called with os state "down", causing the service processor to stop the heartbeats.

    :param struct service_processor \*sp:
        *undescribed*

    :param int os_state:
        *undescribed*

.. This file was automatic generated / don't edit.

