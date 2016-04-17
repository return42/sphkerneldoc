.. -*- coding: utf-8; mode: rst -*-

=========
netlink.c
=========


.. _`quota_send_warning`:

quota_send_warning
==================

.. c:function:: void quota_send_warning (struct kqid qid, dev_t dev, const char warntype)

    Send warning to userspace about exceeded quota

    :param struct kqid qid:
        The kernel internal quota identifier.

    :param dev_t dev:
        The device on which the fs is mounted (sb->s_dev)

    :param const char warntype:
        The type of the warning: QUOTA_NL_...



.. _`quota_send_warning.description`:

Description
-----------

This can be used by filesystems (including those which don't use
dquot) to send a message to userspace relating to quota limits.

