
.. _API-srp-attach-transport:

====================
srp_attach_transport
====================

*man srp_attach_transport(9)*

*4.6.0-rc1*

instantiate SRP transport template


Synopsis
========

.. c:function:: struct scsi_transport_template ⋆ srp_attach_transport( struct srp_function_template * ft )

Arguments
=========

``ft``
    SRP transport class function template
