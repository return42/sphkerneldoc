.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/drbd_genl_api.h

.. _`drbd_genlmsghdr`:

struct drbd_genlmsghdr
======================

.. c:type:: struct drbd_genlmsghdr

    DRBD specific header used in NETLINK_GENERIC requests

.. _`drbd_genlmsghdr.definition`:

Definition
----------

.. code-block:: c

    struct drbd_genlmsghdr {
        __u32 minor;
        union {
            __u32 flags;
            __s32 ret_code;
        } ;
    }

.. _`drbd_genlmsghdr.members`:

Members
-------

minor
    For admin requests (user -> kernel): which minor device to operate on.
    For (unicast) replies or informational (broadcast) messages
    (kernel -> user): which minor device the information is about.
    If we do not operate on minors, but on connections or resources,
    the minor value shall be (~0), and the attribute DRBD_NLA_CFG_CONTEXT
    is used instead.

{unnamed_union}
    anonymous

flags
    possible operation modifiers (relevant only for user->kernel):
    DRBD_GENL_F_SET_DEFAULTS

ret_code
    kernel->userland unicast cfg reply return code (union with flags);

.. This file was automatic generated / don't edit.

