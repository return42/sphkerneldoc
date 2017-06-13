.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/usb/chipidea.h

.. _`ci_hdrc_cable`:

struct ci_hdrc_cable
====================

.. c:type:: struct ci_hdrc_cable

    structure for external connector cable state tracking

.. _`ci_hdrc_cable.definition`:

Definition
----------

.. code-block:: c

    struct ci_hdrc_cable {
        bool connected;
        bool changed;
        bool enabled;
        struct extcon_dev *edev;
        struct ci_hdrc *ci;
        struct notifier_block nb;
    }

.. _`ci_hdrc_cable.members`:

Members
-------

connected
    true if cable is connected, false otherwise

changed
    set to true when extcon event happen

enabled
    set to true if we've enabled the vbus or id interrupt

edev
    device which generate events

ci
    driver state of the chipidea device

nb
    hold event notification callback

.. This file was automatic generated / don't edit.

