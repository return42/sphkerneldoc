.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/glink_ssr.c

.. _`do_cleanup_msg`:

struct do_cleanup_msg
=====================

.. c:type:: struct do_cleanup_msg

    The data structure for an SSR do_cleanup message

.. _`do_cleanup_msg.definition`:

Definition
----------

.. code-block:: c

    struct do_cleanup_msg {
        __le32 version;
        __le32 command;
        __le32 seq_num;
        __le32 name_len;
        char name[32];
    }

.. _`do_cleanup_msg.members`:

Members
-------

version
    *undescribed*

command
    *undescribed*

seq_num
    *undescribed*

name_len
    *undescribed*

name
    *undescribed*

.. _`do_cleanup_msg.version`:

version
-------

The G-Link SSR protocol version

.. _`do_cleanup_msg.command`:

command
-------

The G-Link SSR command - do_cleanup

.. _`do_cleanup_msg.seq_num`:

seq_num
-------

Sequence number

.. _`do_cleanup_msg.name_len`:

name_len
--------

Length of the name of the subsystem being restarted

.. _`do_cleanup_msg.name`:

name
----

G-Link edge name of the subsystem being restarted

.. _`cleanup_done_msg`:

struct cleanup_done_msg
=======================

.. c:type:: struct cleanup_done_msg

    The data structure for an SSR cleanup_done message

.. _`cleanup_done_msg.definition`:

Definition
----------

.. code-block:: c

    struct cleanup_done_msg {
        __le32 version;
        __le32 response;
        __le32 seq_num;
    }

.. _`cleanup_done_msg.members`:

Members
-------

version
    *undescribed*

response
    *undescribed*

seq_num
    *undescribed*

.. _`cleanup_done_msg.version`:

version
-------

The G-Link SSR protocol version

.. _`cleanup_done_msg.response`:

response
--------

The G-Link SSR response to a do_cleanup command, cleanup_done

.. _`cleanup_done_msg.seq_num`:

seq_num
-------

Sequence number

.. _`glink_ssr_do_cleanup`:

GLINK_SSR_DO_CLEANUP
====================

.. c:function::  GLINK_SSR_DO_CLEANUP()

    Link SSR protocol commands

.. This file was automatic generated / don't edit.

