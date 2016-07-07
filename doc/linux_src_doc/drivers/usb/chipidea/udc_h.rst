.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/chipidea/udc.h

.. _`ci_hw_req`:

struct ci_hw_req
================

.. c:type:: struct ci_hw_req

    usb request representation

.. _`ci_hw_req.definition`:

Definition
----------

.. code-block:: c

    struct ci_hw_req {
        struct usb_request req;
        struct list_head queue;
        struct list_head tds;
    }

.. _`ci_hw_req.members`:

Members
-------

req
    request structure for gadget drivers

queue
    link to QH list

tds
    *undescribed*

.. This file was automatic generated / don't edit.

