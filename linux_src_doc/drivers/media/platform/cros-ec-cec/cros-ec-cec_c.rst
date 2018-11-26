.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/cros-ec-cec/cros-ec-cec.c

.. _`cros_ec_cec`:

struct cros_ec_cec
==================

.. c:type:: struct cros_ec_cec

    Driver data for EC CEC

.. _`cros_ec_cec.definition`:

Definition
----------

.. code-block:: c

    struct cros_ec_cec {
        struct cros_ec_device *cros_ec;
        struct notifier_block notifier;
        struct cec_adapter *adap;
        struct cec_notifier *notify;
        struct cec_msg rx_msg;
    }

.. _`cros_ec_cec.members`:

Members
-------

cros_ec
    Pointer to EC device

notifier
    Notifier info for responding to EC events

adap
    CEC adapter

notify
    CEC notifier pointer

rx_msg
    storage for a received message

.. This file was automatic generated / don't edit.

