.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/psp-sev.h

.. _`sev_ret_code`:

typedef sev_ret_code
====================

.. c:type:: typedef sev_ret_code


.. _`sev_user_data_status`:

struct sev_user_data_status
===========================

.. c:type:: struct sev_user_data_status

    PLATFORM_STATUS command parameters

.. _`sev_user_data_status.definition`:

Definition
----------

.. code-block:: c

    struct sev_user_data_status {
        __u8 api_major;
        __u8 api_minor;
        __u8 state;
        __u32 flags;
        __u8 build;
        __u32 guest_count;
    }

.. _`sev_user_data_status.members`:

Members
-------

api_major
    *undescribed*

api_minor
    *undescribed*

state
    platform state

flags
    platform config flags

build
    firmware build id for API version

guest_count
    number of active guests

.. _`sev_user_data_pek_csr`:

struct sev_user_data_pek_csr
============================

.. c:type:: struct sev_user_data_pek_csr

    PEK_CSR command parameters

.. _`sev_user_data_pek_csr.definition`:

Definition
----------

.. code-block:: c

    struct sev_user_data_pek_csr {
        __u64 address;
        __u32 length;
    }

.. _`sev_user_data_pek_csr.members`:

Members
-------

address
    PEK certificate chain

length
    length of certificate

.. _`sev_user_data_pek_cert_import`:

struct sev_user_data_pek_cert_import
====================================

.. c:type:: struct sev_user_data_pek_cert_import

    PEK_CERT_IMPORT command parameters

.. _`sev_user_data_pek_cert_import.definition`:

Definition
----------

.. code-block:: c

    struct sev_user_data_pek_cert_import {
        __u64 pek_cert_address;
        __u32 pek_cert_len;
        __u64 oca_cert_address;
        __u32 oca_cert_len;
    }

.. _`sev_user_data_pek_cert_import.members`:

Members
-------

pek_cert_address
    *undescribed*

pek_cert_len
    *undescribed*

oca_cert_address
    *undescribed*

oca_cert_len
    *undescribed*

.. _`sev_user_data_pdh_cert_export`:

struct sev_user_data_pdh_cert_export
====================================

.. c:type:: struct sev_user_data_pdh_cert_export

    PDH_CERT_EXPORT command parameters

.. _`sev_user_data_pdh_cert_export.definition`:

Definition
----------

.. code-block:: c

    struct sev_user_data_pdh_cert_export {
        __u64 pdh_cert_address;
        __u32 pdh_cert_len;
        __u64 cert_chain_address;
        __u32 cert_chain_len;
    }

.. _`sev_user_data_pdh_cert_export.members`:

Members
-------

pdh_cert_address
    *undescribed*

pdh_cert_len
    *undescribed*

cert_chain_address
    PDH certificate chain

cert_chain_len
    length of PDH certificate chain

.. _`sev_user_data_get_id`:

struct sev_user_data_get_id
===========================

.. c:type:: struct sev_user_data_get_id

    GET_ID command parameters

.. _`sev_user_data_get_id.definition`:

Definition
----------

.. code-block:: c

    struct sev_user_data_get_id {
        __u8 socket1[64];
        __u8 socket2[64];
    }

.. _`sev_user_data_get_id.members`:

Members
-------

socket1
    Buffer to pass unique ID of first socket

socket2
    Buffer to pass unique ID of second socket

.. _`sev_issue_cmd`:

struct sev_issue_cmd
====================

.. c:type:: struct sev_issue_cmd

    SEV ioctl parameters

.. _`sev_issue_cmd.definition`:

Definition
----------

.. code-block:: c

    struct sev_issue_cmd {
        __u32 cmd;
        __u64 data;
        __u32 error;
    }

.. _`sev_issue_cmd.members`:

Members
-------

cmd
    SEV commands to execute

data
    *undescribed*

error
    SEV FW return code on failure

.. This file was automatic generated / don't edit.

