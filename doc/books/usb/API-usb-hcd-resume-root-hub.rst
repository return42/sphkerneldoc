
.. _API-usb-hcd-resume-root-hub:

=======================
usb_hcd_resume_root_hub
=======================

*man usb_hcd_resume_root_hub(9)*

*4.6.0-rc1*

called by HCD to resume its root hub


Synopsis
========

.. c:function:: void usb_hcd_resume_root_hub( struct usb_hcd * hcd )

Arguments
=========

``hcd``
    host controller for this root hub


Description
===========

The USB host controller calls this function when its root hub is suspended (with the remote wakeup feature enabled) and a remote wakeup request is received. The routine submits a
workqueue request to resume the root hub (that is, manage its downstream ports again).
