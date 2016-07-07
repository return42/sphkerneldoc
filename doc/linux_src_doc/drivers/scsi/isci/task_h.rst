.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/task.h

.. _`isci_tmf_function_codes`:

enum isci_tmf_function_codes
============================

.. c:type:: enum isci_tmf_function_codes

    This enum defines the possible preparations of task management requests.

.. _`isci_tmf_function_codes.definition`:

Definition
----------

.. code-block:: c

    enum isci_tmf_function_codes {
        isci_tmf_func_none,
        isci_tmf_ssp_task_abort,
        isci_tmf_ssp_lun_reset
    };

.. _`isci_tmf_function_codes.constants`:

Constants
---------

isci_tmf_func_none
    *undescribed*

isci_tmf_ssp_task_abort
    *undescribed*

isci_tmf_ssp_lun_reset
    *undescribed*

.. _`isci_tmf_function_codes.description`:

Description
-----------

???

.. _`isci_tmf`:

struct isci_tmf
===============

.. c:type:: struct isci_tmf

    This class represents the task management object which acts as an interface to libsas for processing task management requests

.. _`isci_tmf.definition`:

Definition
----------

.. code-block:: c

    struct isci_tmf {
        struct completion *complete;
        enum sas_protocol proto;
        union resp;
        unsigned char lun[8];
        u16 io_tag;
        enum isci_tmf_function_codes tmf_code;
        int status;
    }

.. _`isci_tmf.members`:

Members
-------

complete
    *undescribed*

proto
    *undescribed*

resp
    *undescribed*

io_tag
    *undescribed*

tmf_code
    *undescribed*

status
    *undescribed*

.. _`isci_tmf.description`:

Description
-----------



.. This file was automatic generated / don't edit.

