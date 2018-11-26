.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netlabel/netlabel_user.c

.. _`netlbl_netlink_init`:

netlbl_netlink_init
===================

.. c:function:: int netlbl_netlink_init( void)

    Initialize the NETLINK communication channel

    :param void:
        no arguments
    :type void: 

.. _`netlbl_netlink_init.description`:

Description
-----------

Call out to the NetLabel components so they can register their families and
commands with the Generic NETLINK mechanism.  Returns zero on success and
non-zero on failure.

.. _`netlbl_audit_start_common`:

netlbl_audit_start_common
=========================

.. c:function:: struct audit_buffer *netlbl_audit_start_common(int type, struct netlbl_audit *audit_info)

    Start an audit message

    :param type:
        audit message type
    :type type: int

    :param audit_info:
        NetLabel audit information
    :type audit_info: struct netlbl_audit \*

.. _`netlbl_audit_start_common.description`:

Description
-----------

Start an audit message using the type specified in \ ``type``\  and fill the audit
message with some fields common to all NetLabel audit messages.  Returns
a pointer to the audit buffer on success, NULL on failure.

.. This file was automatic generated / don't edit.

