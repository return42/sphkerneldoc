.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/fuse/cuse.c

.. _`cuse_parse_one`:

cuse_parse_one
==============

.. c:function:: int cuse_parse_one(char **pp, char *end, char **keyp, char **valp)

    parse one key=value pair

    :param pp:
        i/o parameter for the current position
    :type pp: char \*\*

    :param end:
        points to one past the end of the packed string
    :type end: char \*

    :param keyp:
        out parameter for key
    :type keyp: char \*\*

    :param valp:
        out parameter for value
    :type valp: char \*\*

.. _`cuse_parse_one.description`:

Description
-----------

\*@pp points to packed strings - "key0=val0\0key1=val1\0" which ends
at \ ``end``\  - 1.  This function parses one pair and set \*@keyp to the
start of the key and \*@valp to the start of the value.  Note that
the original string is modified such that the key string is
terminated with '\0'.  \*@pp is updated to point to the next string.

.. _`cuse_parse_one.return`:

Return
------

1 on successful parse, 0 on EOF, -errno on failure.

.. _`cuse_parse_devinfo`:

cuse_parse_devinfo
==================

.. c:function:: int cuse_parse_devinfo(char *p, size_t len, struct cuse_devinfo *devinfo)

    parse device info

    :param p:
        device info string
    :type p: char \*

    :param len:
        length of device info string
    :type len: size_t

    :param devinfo:
        out parameter for parsed device info
    :type devinfo: struct cuse_devinfo \*

.. _`cuse_parse_devinfo.description`:

Description
-----------

Parse \ ``p``\  to extract device info and store it into \ ``devinfo``\ .  String
pointed to by \ ``p``\  is modified by parsing and \ ``devinfo``\  points into
them, so \ ``p``\  shouldn't be freed while \ ``devinfo``\  is in use.

.. _`cuse_parse_devinfo.return`:

Return
------

0 on success, -errno on failure.

.. _`cuse_process_init_reply`:

cuse_process_init_reply
=======================

.. c:function:: void cuse_process_init_reply(struct fuse_conn *fc, struct fuse_req *req)

    finish initializing CUSE channel

    :param fc:
        *undescribed*
    :type fc: struct fuse_conn \*

    :param req:
        *undescribed*
    :type req: struct fuse_req \*

.. _`cuse_process_init_reply.description`:

Description
-----------

This function creates the character device and sets up all the
required data structures for it.  Please read the comment at the
top of this file for high level overview.

.. _`cuse_channel_open`:

cuse_channel_open
=================

.. c:function:: int cuse_channel_open(struct inode *inode, struct file *file)

    open method for /dev/cuse

    :param inode:
        inode for /dev/cuse
    :type inode: struct inode \*

    :param file:
        file struct being opened
    :type file: struct file \*

.. _`cuse_channel_open.description`:

Description
-----------

Userland CUSE server can create a CUSE device by opening /dev/cuse
and replying to the initialization request kernel sends.  This
function is responsible for handling CUSE device initialization.
Because the fd opened by this function is used during
initialization, this function only creates cuse_conn and sends
init.  The rest is delegated to a kthread.

.. _`cuse_channel_open.return`:

Return
------

0 on success, -errno on failure.

.. _`cuse_channel_release`:

cuse_channel_release
====================

.. c:function:: int cuse_channel_release(struct inode *inode, struct file *file)

    release method for /dev/cuse

    :param inode:
        inode for /dev/cuse
    :type inode: struct inode \*

    :param file:
        file struct being closed
    :type file: struct file \*

.. _`cuse_channel_release.description`:

Description
-----------

Disconnect the channel, deregister CUSE device and initiate
destruction by putting the default reference.

.. _`cuse_channel_release.return`:

Return
------

0 on success, -errno on failure.

.. This file was automatic generated / don't edit.

