.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/client.h

.. _`mei_me_cl_is_active`:

mei_me_cl_is_active
===================

.. c:function:: bool mei_me_cl_is_active(const struct mei_me_client *me_cl)

    check whether me client is active in the fw

    :param me_cl:
        me client
    :type me_cl: const struct mei_me_client \*

.. _`mei_me_cl_is_active.return`:

Return
------

true if the me client is active in the firmware

.. _`mei_me_cl_uuid`:

mei_me_cl_uuid
==============

.. c:function:: const uuid_le *mei_me_cl_uuid(const struct mei_me_client *me_cl)

    return me client protocol name (uuid)

    :param me_cl:
        me client
    :type me_cl: const struct mei_me_client \*

.. _`mei_me_cl_uuid.return`:

Return
------

me client protocol name

.. _`mei_me_cl_ver`:

mei_me_cl_ver
=============

.. c:function:: u8 mei_me_cl_ver(const struct mei_me_client *me_cl)

    return me client protocol version

    :param me_cl:
        me client
    :type me_cl: const struct mei_me_client \*

.. _`mei_me_cl_ver.return`:

Return
------

me client protocol version

.. _`mei_cl_is_connected`:

mei_cl_is_connected
===================

.. c:function:: bool mei_cl_is_connected(struct mei_cl *cl)

    host client is connected

    :param cl:
        host client
    :type cl: struct mei_cl \*

.. _`mei_cl_is_connected.return`:

Return
------

true if the host client is connected

.. _`mei_cl_me_id`:

mei_cl_me_id
============

.. c:function:: u8 mei_cl_me_id(const struct mei_cl *cl)

    me client id

    :param cl:
        host client
    :type cl: const struct mei_cl \*

.. _`mei_cl_me_id.return`:

Return
------

me client id or 0 if client is not connected

.. _`mei_cl_mtu`:

mei_cl_mtu
==========

.. c:function:: size_t mei_cl_mtu(const struct mei_cl *cl)

    maximal message that client can send and receive

    :param cl:
        host client
    :type cl: const struct mei_cl \*

.. _`mei_cl_mtu.return`:

Return
------

mtu

.. _`mei_cl_is_fixed_address`:

mei_cl_is_fixed_address
=======================

.. c:function:: bool mei_cl_is_fixed_address(const struct mei_cl *cl)

    check whether the me client uses fixed address

    :param cl:
        host client
    :type cl: const struct mei_cl \*

.. _`mei_cl_is_fixed_address.return`:

Return
------

true if the client is connected and it has fixed me address

.. _`mei_cl_is_single_recv_buf`:

mei_cl_is_single_recv_buf
=========================

.. c:function:: bool mei_cl_is_single_recv_buf(const struct mei_cl *cl)

    check whether the me client uses single receiving buffer

    :param cl:
        host client
    :type cl: const struct mei_cl \*

.. _`mei_cl_is_single_recv_buf.return`:

Return
------

true if single_recv_buf == 1; 0 otherwise

.. _`mei_cl_uuid`:

mei_cl_uuid
===========

.. c:function:: const uuid_le *mei_cl_uuid(const struct mei_cl *cl)

    client's uuid

    :param cl:
        host client
    :type cl: const struct mei_cl \*

.. _`mei_cl_uuid.return`:

Return
------

return uuid of connected me client

.. _`mei_cl_host_addr`:

mei_cl_host_addr
================

.. c:function:: u8 mei_cl_host_addr(const struct mei_cl *cl)

    client's host address

    :param cl:
        host client
    :type cl: const struct mei_cl \*

.. _`mei_cl_host_addr.return`:

Return
------

0 for fixed address client, host address for dynamic client

.. This file was automatic generated / don't edit.

