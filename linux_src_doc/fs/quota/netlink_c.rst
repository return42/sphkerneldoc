.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/quota/netlink.c

.. _`quota_send_warning`:

quota_send_warning
==================

.. c:function:: void quota_send_warning(struct kqid qid, dev_t dev, const char warntype)

    Send warning to userspace about exceeded quota

    :param qid:
        The kernel internal quota identifier.
    :type qid: struct kqid

    :param dev:
        The device on which the fs is mounted (sb->s_dev)
    :type dev: dev_t

    :param warntype:
        The type of the warning: QUOTA_NL_...
    :type warntype: const char

.. _`quota_send_warning.description`:

Description
-----------

This can be used by filesystems (including those which don't use
dquot) to send a message to userspace relating to quota limits.

.. This file was automatic generated / don't edit.

