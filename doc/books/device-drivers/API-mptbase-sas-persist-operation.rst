
.. _API-mptbase-sas-persist-operation:

=============================
mptbase_sas_persist_operation
=============================

*man mptbase_sas_persist_operation(9)*

*4.6.0-rc1*

Perform operation on SAS Persistent Table


Synopsis
========

.. c:function:: int mptbase_sas_persist_operation( MPT_ADAPTER * ioc, u8 persist_opcode )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``persist_opcode``
    see below


Description
===========

MPI_SAS_OP_CLEAR_NOT_PRESENT - Free all persist TargetID mappings for devices not currently present. MPI_SAS_OP_CLEAR_ALL_PERSISTENT - Clear al persist TargetID mappings


NOTE
====

Don't use not this function during interrupt time.

Returns 0 for success, non-zero error
