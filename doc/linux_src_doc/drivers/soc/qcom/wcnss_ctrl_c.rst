.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/wcnss_ctrl.c

.. _`wcnss_ctrl`:

struct wcnss_ctrl
=================

.. c:type:: struct wcnss_ctrl

    driver context

.. _`wcnss_ctrl.definition`:

Definition
----------

.. code-block:: c

    struct wcnss_ctrl {
        struct device *dev;
        struct qcom_smd_channel *channel;
        struct completion ack;
        int ack_status;
        struct work_struct download_nv_work;
    }

.. _`wcnss_ctrl.members`:

Members
-------

dev
    device handle

channel
    SMD channel handle

ack
    completion for outstanding requests

ack_status
    status of the outstanding request

download_nv_work
    worker for uploading nv binary

.. _`wcnss_msg_hdr`:

struct wcnss_msg_hdr
====================

.. c:type:: struct wcnss_msg_hdr

    common packet header for requests and responses

.. _`wcnss_msg_hdr.definition`:

Definition
----------

.. code-block:: c

    struct wcnss_msg_hdr {
        u32 type;
        u32 len;
    }

.. _`wcnss_msg_hdr.members`:

Members
-------

type
    packet message type

len
    total length of the packet, including this header

.. _`wcnss_version_resp`:

struct wcnss_version_resp
=========================

.. c:type:: struct wcnss_version_resp

    version request response

.. _`wcnss_version_resp.definition`:

Definition
----------

.. code-block:: c

    struct wcnss_version_resp {
        struct wcnss_msg_hdr hdr;
        u8 major;
        u8 minor;
        u8 version;
        u8 revision;
    }

.. _`wcnss_version_resp.members`:

Members
-------

hdr
    common packet wcnss_msg_hdr header

major
    *undescribed*

minor
    *undescribed*

version
    *undescribed*

revision
    *undescribed*

.. _`wcnss_download_nv_req`:

struct wcnss_download_nv_req
============================

.. c:type:: struct wcnss_download_nv_req

    firmware fragment request

.. _`wcnss_download_nv_req.definition`:

Definition
----------

.. code-block:: c

    struct wcnss_download_nv_req {
        struct wcnss_msg_hdr hdr;
        u16 seq;
        u16 last;
        u32 frag_size;
        u8 fragment[];
    }

.. _`wcnss_download_nv_req.members`:

Members
-------

hdr
    common packet wcnss_msg_hdr header

seq
    sequence number of this fragment

last
    boolean indicator of this being the last fragment of the binary

frag_size
    length of this fragment

fragment
    fragment data

.. _`wcnss_download_nv_resp`:

struct wcnss_download_nv_resp
=============================

.. c:type:: struct wcnss_download_nv_resp

    firmware download response

.. _`wcnss_download_nv_resp.definition`:

Definition
----------

.. code-block:: c

    struct wcnss_download_nv_resp {
        struct wcnss_msg_hdr hdr;
        u8 status;
    }

.. _`wcnss_download_nv_resp.members`:

Members
-------

hdr
    common packet wcnss_msg_hdr header

status
    boolean to indicate success of the download

.. _`wcnss_ctrl_smd_callback`:

wcnss_ctrl_smd_callback
=======================

.. c:function:: int wcnss_ctrl_smd_callback(struct qcom_smd_channel *channel, const void *data, size_t count)

    handler from SMD responses

    :param struct qcom_smd_channel \*channel:
        smd channel handle

    :param const void \*data:
        pointer to the incoming data packet

    :param size_t count:
        size of the incoming data packet

.. _`wcnss_ctrl_smd_callback.description`:

Description
-----------

Handles any incoming packets from the remote WCNSS_CTRL service.

.. _`wcnss_request_version`:

wcnss_request_version
=====================

.. c:function:: int wcnss_request_version(struct wcnss_ctrl *wcnss)

    send a version request to WCNSS

    :param struct wcnss_ctrl \*wcnss:
        wcnss ctrl driver context

.. _`wcnss_download_nv`:

wcnss_download_nv
=================

.. c:function:: void wcnss_download_nv(struct work_struct *work)

    send nv binary to WCNSS

    :param struct work_struct \*work:
        work struct to acquire wcnss context

.. This file was automatic generated / don't edit.

