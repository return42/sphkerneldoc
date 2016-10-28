.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/smd-rpm.c

.. _`qcom_smd_rpm`:

struct qcom_smd_rpm
===================

.. c:type:: struct qcom_smd_rpm

    state of the rpm device driver

.. _`qcom_smd_rpm.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smd_rpm {
        struct qcom_smd_channel *rpm_channel;
        struct device *dev;
        struct completion ack;
        struct mutex lock;
        int ack_status;
    }

.. _`qcom_smd_rpm.members`:

Members
-------

rpm_channel
    reference to the smd channel

dev
    *undescribed*

ack
    completion for acks

lock
    mutual exclusion around the send/complete pair

ack_status
    result of the rpm request

.. _`qcom_rpm_header`:

struct qcom_rpm_header
======================

.. c:type:: struct qcom_rpm_header

    header for all rpm requests and responses

.. _`qcom_rpm_header.definition`:

Definition
----------

.. code-block:: c

    struct qcom_rpm_header {
        __le32 service_type;
        __le32 length;
    }

.. _`qcom_rpm_header.members`:

Members
-------

service_type
    identifier of the service

length
    length of the payload

.. _`qcom_rpm_request`:

struct qcom_rpm_request
=======================

.. c:type:: struct qcom_rpm_request

    request message to the rpm

.. _`qcom_rpm_request.definition`:

Definition
----------

.. code-block:: c

    struct qcom_rpm_request {
        __le32 msg_id;
        __le32 flags;
        __le32 type;
        __le32 id;
        __le32 data_len;
    }

.. _`qcom_rpm_request.members`:

Members
-------

msg_id
    identifier of the outgoing message

flags
    active/sleep state flags

type
    resource type

id
    resource id

data_len
    length of the payload following this header

.. _`qcom_rpm_message`:

struct qcom_rpm_message
=======================

.. c:type:: struct qcom_rpm_message

    response message from the rpm

.. _`qcom_rpm_message.definition`:

Definition
----------

.. code-block:: c

    struct qcom_rpm_message {
        __le32 msg_type;
        __le32 length;
        union {unnamed_union};
    }

.. _`qcom_rpm_message.members`:

Members
-------

msg_type
    indicator of the type of message

length
    the size of this message, including the message header

{unnamed_union}
    anonymous


.. _`qcom_rpm_message.description`:

Description
-----------

Multiple of these messages can be stacked in an rpm message.

.. _`qcom_rpm_smd_write`:

qcom_rpm_smd_write
==================

.. c:function:: int qcom_rpm_smd_write(struct qcom_smd_rpm *rpm, int state, u32 type, u32 id, void *buf, size_t count)

    write \ ``buf``\  to \ ``type``\ :\ ``id``\ 

    :param struct qcom_smd_rpm \*rpm:
        rpm handle

    :param int state:
        *undescribed*

    :param u32 type:
        resource type

    :param u32 id:
        resource identifier

    :param void \*buf:
        the data to be written

    :param size_t count:
        number of bytes in \ ``buf``\ 

.. This file was automatic generated / don't edit.

