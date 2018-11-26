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
        struct rpmsg_endpoint *channel;
        struct completion ack;
        struct completion cbc;
        int ack_status;
        struct work_struct probe_work;
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

cbc
    completion for cbc complete indication

ack_status
    status of the outstanding request

probe_work
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

.. c:function:: int wcnss_ctrl_smd_callback(struct rpmsg_device *rpdev, void *data, int count, void *priv, u32 addr)

    handler from SMD responses

    :param rpdev:
        *undescribed*
    :type rpdev: struct rpmsg_device \*

    :param data:
        pointer to the incoming data packet
    :type data: void \*

    :param count:
        size of the incoming data packet
    :type count: int

    :param priv:
        *undescribed*
    :type priv: void \*

    :param addr:
        *undescribed*
    :type addr: u32

.. _`wcnss_ctrl_smd_callback.description`:

Description
-----------

Handles any incoming packets from the remote WCNSS_CTRL service.

.. _`wcnss_request_version`:

wcnss_request_version
=====================

.. c:function:: int wcnss_request_version(struct wcnss_ctrl *wcnss)

    send a version request to WCNSS

    :param wcnss:
        wcnss ctrl driver context
    :type wcnss: struct wcnss_ctrl \*

.. _`wcnss_download_nv`:

wcnss_download_nv
=================

.. c:function:: int wcnss_download_nv(struct wcnss_ctrl *wcnss, bool *expect_cbc)

    send nv binary to WCNSS

    :param wcnss:
        wcnss_ctrl state handle
    :type wcnss: struct wcnss_ctrl \*

    :param expect_cbc:
        indicator to caller that an cbc event is expected
    :type expect_cbc: bool \*

.. _`wcnss_download_nv.description`:

Description
-----------

Returns 0 on success. Negative errno on failure.

.. _`qcom_wcnss_open_channel`:

qcom_wcnss_open_channel
=======================

.. c:function:: struct rpmsg_endpoint *qcom_wcnss_open_channel(void *wcnss, const char *name, rpmsg_rx_cb_t cb, void *priv)

    open additional SMD channel to WCNSS

    :param wcnss:
        wcnss handle, retrieved from drvdata
    :type wcnss: void \*

    :param name:
        SMD channel name
    :type name: const char \*

    :param cb:
        callback to handle incoming data on the channel
    :type cb: rpmsg_rx_cb_t

    :param priv:
        *undescribed*
    :type priv: void \*

.. This file was automatic generated / don't edit.

