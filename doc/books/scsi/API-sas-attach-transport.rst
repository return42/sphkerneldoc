
.. _API-sas-attach-transport:

====================
sas_attach_transport
====================

*man sas_attach_transport(9)*

*4.6.0-rc1*

instantiate SAS transport template


Synopsis
========

.. c:function:: struct scsi_transport_template ⋆ sas_attach_transport( struct sas_function_template * ft )

Arguments
=========

``ft``
    SAS transport class function template
